"""
Rule-based validation tools for the Evaluator Agent.

These tools run offline (no LLM calls) and surface concrete audit signals
to help the evaluator decide whether a response is ready for the user.
"""

import re
from typing import Any, Dict, List


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().lower()


def _extract_checklist_items(critic_report: str) -> List[str]:
    """Parse '- [ ] ...' items from a Critic report's Issues to Resolve section."""
    pattern = r"-\s*\[\s*[ ]\s*\]\s*(.+)"
    return [match.strip() for match in re.findall(pattern, critic_report or "")]


def query_relevance_tool(query: str, response: str) -> Dict[str, Any]:
    """
    Checks whether the response addresses the key topics implied by the
    user query.  Returns keyword-level signals so the evaluator can judge
    coverage.
    """
    q = _normalize(query)
    resp = _normalize(response)

    topic_keywords = {
        "financial_health": ["financial health", "liquidity", "solvency", "profitability", "debt", "balance sheet"],
        "future_outlook": ["future outlook", "outlook", "growth", "forecast", "forward"],
        "advice": ["advice", "recommend", "suggest", "action", "should", "priority"],
        "risk": ["risk", "downside", "threat", "caution", "uncertain", "limitation"],
        "chart_or_figure": ["chart", "figure", "table", "visualization", "graph", "image"],
        "evidence": ["source", "document", "10-k", "financial statement", "page", "citation"],
    }

    results = {}
    for topic, keywords in topic_keywords.items():
        query_asks = any(kw in q for kw in keywords)
        response_covers = any(kw in resp for kw in keywords)
        results[topic] = {
            "expected_from_query": query_asks,
            "present_in_response": response_covers,
        }

    missing_topics = [
        name
        for name, status in results.items()
        if status["expected_from_query"] and not status["present_in_response"]
    ]

    return {
        "topic_coverage": results,
        "missing_topics": missing_topics,
        "all_covered": not missing_topics,
        "evaluator_hint": "Missing topics are strong candidates for flagging the response as incomplete.",
    }


def issues_resolution_tool(
    critic_issues_markdown: str,
    advisor_report_v2: str,
) -> Dict[str, Any]:
    """
    Parses the '- [ ] ...' checklist items from the Critic's report and
    checks whether each issue appears to be addressed in the revised
    Advisor report (v2).

    Resolution detection is keyword-based: for each issue bullet, the tool
    extracts significant words and checks whether they appear in report v2.
    """
    items = _extract_checklist_items(critic_issues_markdown)
    if not items:
        return {
            "total_issues": 0,
            "resolved": [],
            "unresolved": [],
            "all_resolved": True,
            "evaluator_hint": "No checklist items found in critic report.",
        }

    report_lower = _normalize(advisor_report_v2)
    stopwords = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "shall",
        "should", "may", "might", "must", "can", "could", "to", "of", "in",
        "for", "on", "with", "at", "by", "from", "as", "into", "through",
        "and", "or", "but", "not", "no", "nor", "so", "yet", "both",
        "each", "its", "their", "this", "that", "these", "those",
        "provide", "include", "discuss", "explain", "address", "strengthen",
    }

    resolved: List[str] = []
    unresolved: List[str] = []

    for item in items:
        item_words = set(re.findall(r"[a-z0-9]+", item.lower())) - stopwords
        if not item_words:
            resolved.append(item)
            continue

        match_count = sum(1 for word in item_words if word in report_lower)
        coverage = match_count / len(item_words) if item_words else 0.0

        if coverage >= 0.5:
            resolved.append(item)
        else:
            unresolved.append(item)

    return {
        "total_issues": len(items),
        "resolved": resolved,
        "resolved_count": len(resolved),
        "unresolved": unresolved,
        "unresolved_count": len(unresolved),
        "all_resolved": len(unresolved) == 0,
        "evaluator_hint": (
            "Treat unresolved items as mandatory revision targets for the advisor."
            if unresolved
            else "All critic issues appear addressed in the revised report."
        ),
    }


def response_completeness_tool(response: str) -> Dict[str, Any]:
    """
    Checks whether a response contains expected structural elements:
    evidence/source citations, limitations/caveats, and actionable content.
    Works for both RAG responses and full advisor reports.
    """
    resp = _normalize(response)

    structural_checks = {
        "has_source_citation": any(
            term in resp
            for term in ["source:", "source", "document", "page", "10-k", "citation", "["]
        ),
        "has_limitations_or_caveats": any(
            term in resp
            for term in ["limitation", "caveat", "gap", "insufficient", "missing", "unavailable", "risk"]
        ),
        "has_actionable_content": any(
            term in resp
            for term in ["recommend", "suggest", "advice", "action", "should", "priority", "consider"]
        ),
        "has_structured_sections": any(
            term in resp
            for term in ["## ", "### ", "**", "finding", "summary", "conclusion", "verdict"]
        ),
    }

    missing_elements = [name for name, present in structural_checks.items() if not present]

    return {
        "checks": structural_checks,
        "missing_elements": missing_elements,
        "passes": not missing_elements,
        "evaluator_hint": "Missing structural elements weaken the response quality for end users.",
    }


def evaluation_quality_tool(evaluation_markdown: str) -> Dict[str, Any]:
    """
    Self-checks whether the evaluator's own output is complete enough to
    send back.  Supports the Evaluator Agent's self-review loop.
    """
    text = _normalize(evaluation_markdown)

    checklist = {
        "has_verdict": any(term in text for term in ["verdict", "overall", "conclusion", "bottom line"]),
        "has_query_satisfaction": any(
            term in text for term in ["query satisfaction", "query", "user request", "addresses"]
        ),
        "has_remaining_gaps": any(
            term in text for term in ["remaining gap", "unresolved", "missing", "gap", "incomplete"]
        ),
        "has_recommendation": any(
            term in text for term in ["recommend", "recommendation", "next step", "suggest", "should"]
        ),
    }

    missing_items = [name for name, passed in checklist.items() if not passed]

    return {
        "passes": not missing_items,
        "checklist": checklist,
        "missing_items": missing_items,
        "evaluator_hint": "Revise the evaluation if any required quality item is missing.",
    }
