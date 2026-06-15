"""
Rule-based review tools for the Critic Agent.

These tools do not replace LLM judgment. They surface concrete audit signals
that help the critic ground its feedback in the user query, source context, and
advisor report.
"""

import re
import urllib.parse
from typing import Any, Dict, List


RISK_TOPICS = {
    "competition": ["competitor", "competition", "rival", "byd", "legacy automaker"],
    "valuation": ["valuation", "market cap", "share price", "multiple", "priced in"],
    "supply_chain": ["supply chain", "supplier", "raw material", "lithium", "nickel", "cobalt"],
    "regulation": ["regulation", "regulatory", "tax credit", "ira", "policy", "legal"],
    "margin_pressure": ["margin", "price cut", "cost pressure", "profitability"],
    "execution": ["execution", "production", "manufacturing", "delivery", "capacity"],
}


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip().lower()


def _context_text(context_docs: List[Dict[str, Any]]) -> str:
    parts = []
    for doc in context_docs:
        parts.append(str(doc.get("text", doc.get("content", ""))))
    return "\n".join(parts)


def _extract_numbers(text: str) -> List[str]:
    pattern = r"(?<![A-Za-z0-9])(?:\$?\d[\d,]*(?:\.\d+)?%?|\d+(?:\.\d+)?x)(?![A-Za-z0-9])"
    return sorted(set(re.findall(pattern, text or "")))


def _extract_markdown_images(text: str) -> List[Dict[str, str]]:
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return [
        {"alt_text": match.group(1).strip(), "url": match.group(2).strip()}
        for match in re.finditer(pattern, text or "")
    ]


def report_coverage_tool(query: str, advisor_report: str) -> Dict[str, Any]:
    """
    Checks whether the advisor report appears to answer the user's request.
    Returns simple signals for financial health, future outlook, advice, and
    caveats because these are common advisor-report requirements.
    """
    q = _normalize(query)
    report = _normalize(advisor_report)

    required_dimensions = {
        "financial_health": ["financial health", "liquidity", "solvency", "profitability", "debt"],
        "future_outlook": ["future outlook", "outlook", "growth", "future", "forecast"],
        "actionable_advice": ["advice", "recommend", "suggest", "action", "priority"],
        "risk_or_downside": ["risk", "downside", "threat", "caution", "uncertain"],
        "evidence_or_citation": ["source", "page", "document", "10-k", "financial statement"],
    }

    results = {}
    for dimension, keywords in required_dimensions.items():
        query_mentions_dimension = any(keyword in q for keyword in keywords)
        report_mentions_dimension = any(keyword in report for keyword in keywords)
        results[dimension] = {
            "expected_from_query": query_mentions_dimension or dimension in {"risk_or_downside", "evidence_or_citation"},
            "present_in_report": report_mentions_dimension,
        }

    missing_dimensions = [
        name
        for name, status in results.items()
        if status["expected_from_query"] and not status["present_in_report"]
    ]

    return {
        "coverage": results,
        "missing_dimensions": missing_dimensions,
        "critic_hint": (
            "Use missing dimensions as likely critique targets, but verify with judgment before claiming a failure."
        ),
    }


def evidence_consistency_tool(
    advisor_report: str,
    context_docs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Flags numeric values in the advisor report that do not appear in the context.
    This is conservative: it only detects possible unsupported numbers, not all
    unsupported claims.
    """
    context = _context_text(context_docs)
    report_numbers = _extract_numbers(advisor_report)
    context_numbers = set(_extract_numbers(context))

    unsupported_numbers = []
    for number in report_numbers:
        comparable = number.replace("$", "")
        if number not in context_numbers and comparable not in context_numbers:
            unsupported_numbers.append(number)

    source_names = [str(doc.get("source", "Unknown source")) for doc in context_docs]

    return {
        "numbers_in_report": report_numbers,
        "possibly_unsupported_numbers": unsupported_numbers,
        "available_sources": source_names,
        "critic_hint": (
            "Treat flagged numbers as evidence gaps unless the advisor clearly labels them as estimates or derived calculations."
        ),
    }


def risk_gap_tool(
    advisor_report: str,
    context_docs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Compares risk themes visible in context against risk themes discussed in the
    advisor report.
    """
    context = _normalize(_context_text(context_docs))
    report = _normalize(advisor_report)

    topic_results = {}
    for topic, keywords in RISK_TOPICS.items():
        context_has_topic = any(keyword in context for keyword in keywords)
        report_has_topic = any(keyword in report for keyword in keywords)
        topic_results[topic] = {
            "visible_in_context": context_has_topic,
            "addressed_in_report": report_has_topic,
        }

    missing_risk_topics = [
        topic
        for topic, status in topic_results.items()
        if status["visible_in_context"] and not status["addressed_in_report"]
    ]

    return {
        "risk_topic_matrix": topic_results,
        "missing_risk_topics": missing_risk_topics,
        "critic_hint": (
            "Missing context-visible risks are strong candidates for investor or competitor objections."
        ),
    }


def critique_quality_tool(critique_markdown: str) -> Dict[str, Any]:
    """
    Self-checks whether the critique is useful enough to send back to an advisor.
    This supports the Critic Agent's final self-review loop.
    """
    text = _normalize(critique_markdown)

    checklist = {
        "has_clear_verdict": any(term in text for term in ["verdict", "overall", "bottom line"]),
        "has_logic_gaps": any(term in text for term in ["logic gap", "assumption", "overstates", "unsupported"]),
        "has_investor_lens": "investor" in text,
        "has_competitor_lens": any(term in text for term in ["competitor", "competitive", "rival"]),
        "has_actionable_revision": any(term in text for term in ["revise", "revision", "recommend", "should"]),
        "mentions_evidence": any(term in text for term in ["source", "context", "document", "evidence", "citation"]),
        "has_figure_audit": any(term in text for term in ["figure", "visualization", "chart", "image"]),
    }

    missing_items = [name for name, passed in checklist.items() if not passed]

    return {
        "passes": not missing_items,
        "checklist": checklist,
        "missing_items": missing_items,
        "critic_hint": "Revise the critique if any required quality item is missing.",
    }


def figure_audit_tool(
    advisor_report: str,
    context_docs: List[Dict[str, Any]],
    figure_metadata: List[Dict[str, Any]] | None = None,
) -> Dict[str, Any]:
    """
    Audits chart/table figures referenced by an advisor report.

    This checks static quality signals only. It does not download images, so it
    can run offline and still catch common report visualization issues.
    """
    figure_metadata = figure_metadata or []
    context = _context_text(context_docs)
    context_numbers = set(_extract_numbers(context))
    report = advisor_report or ""
    report_lower = _normalize(report)
    images = _extract_markdown_images(report)

    issues = []
    warnings = []

    for image in images:
        url = image["url"]
        parsed = urllib.parse.urlparse(url)
        decoded_path = urllib.parse.unquote(parsed.path)

        if not image["alt_text"]:
            issues.append(f"Image '{url}' has empty alt text.")
        if "supabase" not in parsed.netloc.lower() and "supabase" not in url.lower():
            issues.append(f"Image URL may not be a Supabase-hosted link: {url}")
        if "/storage/v1/object/public/" not in decoded_path:
            warnings.append(f"Image URL does not look like a public Supabase Storage object URL: {url}")
        if "advisor_figure" not in decoded_path:
            issues.append(f"Image is not stored under the expected advisor_figure folder: {url}")
        if not decoded_path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            issues.append(f"Image URL does not point to a supported image extension: {url}")

    if images:
        figure_terms = ["figure:", "source:", "caption", "chart shows", "table shows", "visualization"]
        if not any(term in report_lower for term in figure_terms):
            issues.append("Report embeds an image but does not provide a visible caption, source note, or explanation.")
    elif any(term in report_lower for term in ["chart", "figure", "visualization", "image"]):
        issues.append("Report discusses a chart/figure but does not embed a Markdown image link.")

    metadata_results = []
    for item in figure_metadata:
        figure_type = str(item.get("figure_type", "")).lower()
        public_url = str(item.get("public_url") or item.get("url") or "")
        caption = str(item.get("caption") or "")
        source_note = str(item.get("source_note") or "")
        data_used = item.get("data_used") or item.get("data") or []
        item_issues = []

        if figure_type in {"bar_chart", "line_chart"} and not public_url:
            item_issues.append("Chart metadata is missing public_url.")
        if figure_type in {"bar_chart", "line_chart"} and "advisor_figure" not in public_url:
            item_issues.append("Chart public_url is not under advisor_figure.")
        if figure_type in {"bar_chart", "line_chart"} and not caption:
            item_issues.append("Chart metadata is missing caption.")
        if figure_type in {"bar_chart", "line_chart"} and not source_note:
            item_issues.append("Chart metadata is missing source_note.")
        if figure_type == "line_chart":
            x_values = [str(row.get(item.get("x_key", ""), "")) for row in data_used if isinstance(row, dict)]
            if len(x_values) < 2:
                item_issues.append("Line chart has fewer than two x-axis values.")

        metadata_numbers = _extract_numbers(str(data_used))
        unsupported_numbers = []
        for number in metadata_numbers:
            comparable = number.replace("$", "")
            if number not in context_numbers and comparable not in context_numbers:
                unsupported_numbers.append(number)

        if unsupported_numbers:
            item_issues.append(
                "Figure metadata contains numbers not found in context: "
                + ", ".join(unsupported_numbers[:8])
            )

        metadata_results.append({
            "figure_id": item.get("figure_id"),
            "figure_type": figure_type,
            "issues": item_issues,
        })
        issues.extend([f"{item.get('figure_id', 'figure')}: {issue}" for issue in item_issues])

    return {
        "embedded_images": images,
        "metadata_results": metadata_results,
        "issues": issues,
        "warnings": warnings,
        "passes": not issues,
        "critic_hint": (
            "Use figure issues to critique misleading, unsupported, missing, or frontend-unfriendly visualizations."
        ),
    }
