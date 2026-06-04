"""
Structured web-search helper for financial query augmentation.
"""

from __future__ import annotations

import importlib
import json
import re
from typing import Any

try:
    from googlesearch import search as google_search
except ImportError:  # pragma: no cover - optional dependency
    google_search = None

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover - optional dependency
    BeautifulSoup = None

try:
    import requests
except ImportError:  # pragma: no cover - optional dependency
    requests = None


SEARCH_GENERATION_PROMPT = """Given the following financial query, generate concise web searches.

Output valid JSON:
{
  "prompts": [
    {
      "query": "specific search query",
      "rationale": "why this search helps",
      "priority": "high|medium|low",
      "expected_sources": ["financial_news", "official_filings"]
    }
  ],
  "search_strategy": "brief strategy"
}
"""


def web_search_tool(
    user_query: str,
    *,
    search_queries: list[str] | None = None,
    similarity_score: float = 0.0,
    max_results_per_query: int = 2,
) -> dict[str, Any]:
    """Generate search prompts and optionally fetch lightweight web documents."""

    prompts = _build_prompts(user_query, search_queries, similarity_score)
    documents = _fetch_documents(prompts, max_results_per_query=max_results_per_query)
    return {
        **prompts,
        "documents": documents,
    }


def _build_prompts(
    user_query: str,
    search_queries: list[str] | None,
    similarity_score: float,
) -> dict[str, Any]:
    if not user_query.strip():
        return {
            "prompts": [],
            "total_prompts": 0,
            "search_strategy": "No query provided",
            "confidence_score": similarity_score,
        }

    if search_queries:
        prompts = []
        for index, query in enumerate(search_queries[:3], start=1):
            prompts.append(
                {
                    "query": query,
                    "rationale": f"Expanded query {index} derived from the original financial question.",
                    "priority": "high" if index == 1 else "medium",
                    "expected_sources": _infer_expected_sources(query),
                }
            )
        return {
            "prompts": prompts,
            "total_prompts": len(prompts),
            "search_strategy": "Use orchestrator-expanded queries to fill retrieval gaps.",
            "confidence_score": similarity_score,
            "user_query": user_query,
        }

    llm = None
    try:
        llm_module = importlib.import_module("ai_integration.models.llm")
        llm = llm_module.get_llm()
    except Exception:
        llm = None

    if llm is not None:
        try:
            llm_response = llm.invoke(f"{SEARCH_GENERATION_PROMPT}\n\nUser Query: {user_query}")
            return _parse_llm_output_to_structured_format(
                str(llm_response),
                user_query,
                similarity_score,
            )
        except Exception:
            pass

    fallback_queries = [
        user_query,
        f"{user_query} latest financial news",
        f"{user_query} analyst outlook",
    ]
    return _build_prompts(user_query, fallback_queries, similarity_score)


def _fetch_documents(
    prompt_payload: dict[str, Any],
    *,
    max_results_per_query: int,
) -> list[dict[str, Any]]:
    prompts = prompt_payload.get("prompts", [])
    if not prompts:
        return []

    if google_search is None or requests is None or BeautifulSoup is None:
        return [
            {
                "text": (
                    "Live web search dependencies are not available in this environment. "
                    f"Placeholder document for query: {prompt['query']}"
                ),
                "source": f"web_search_placeholder:{index}",
                "page": 1,
                "section_title": "Web Search Placeholder",
                "section_type": "body",
            }
            for index, prompt in enumerate(prompts, start=1)
        ]

    documents: list[dict[str, Any]] = []
    for prompt in prompts:
        try:
            urls = list(google_search(prompt["query"], num_results=max_results_per_query))
        except Exception:
            urls = []

        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                text = soup.get_text(" ", strip=True)
                if not text:
                    continue
                documents.append(
                    {
                        "text": text[:4000],
                        "source": url,
                        "page": 1,
                        "section_title": prompt["query"],
                        "section_type": "body",
                    }
                )
            except Exception:
                continue

    if documents:
        return documents

    return [
        {
            "text": f"No live search results could be fetched for query: {prompt['query']}",
            "source": f"web_search_empty:{index}",
            "page": 1,
            "section_title": prompt["query"],
            "section_type": "body",
        }
        for index, prompt in enumerate(prompts, start=1)
    ]


def _parse_llm_output_to_structured_format(
    llm_output: str,
    user_query: str,
    similarity_score: float,
) -> dict[str, Any]:
    json_match = re.search(r"\{.*\}", llm_output, re.DOTALL)
    parsed_data = None

    if json_match:
        try:
            parsed_data = json.loads(json_match.group())
        except json.JSONDecodeError:
            parsed_data = None

    if parsed_data and isinstance(parsed_data, dict):
        prompts = parsed_data.get("prompts", [])
        if isinstance(prompts, list):
            return {
                "prompts": prompts,
                "total_prompts": len(prompts),
                "search_strategy": parsed_data.get("search_strategy", ""),
                "confidence_score": similarity_score,
                "user_query": user_query,
            }

    return _parse_text_to_structured_format(llm_output, user_query, similarity_score)


def _parse_text_to_structured_format(
    text_output: str,
    user_query: str,
    similarity_score: float,
) -> dict[str, Any]:
    queries: list[str] = []
    for raw_line in text_output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"^[\-\d\.\)\s•*]+", "", line).strip()
        if len(line) > 5 and line not in queries:
            queries.append(line)

    prompts = [
        {
            "query": query,
            "rationale": f"Complementary search to support: {user_query}",
            "priority": "high" if index == 1 else "medium",
            "expected_sources": _infer_expected_sources(query),
        }
        for index, query in enumerate(queries[:3], start=1)
    ]

    return {
        "prompts": prompts,
        "total_prompts": len(prompts),
        "search_strategy": "Parsed search prompts from text output.",
        "confidence_score": similarity_score,
        "user_query": user_query,
    }


def _infer_expected_sources(query: str) -> list[str]:
    query_lower = query.lower()
    sources: list[str] = []
    source_keywords = {
        "financial_news": ["market", "stock", "price", "earnings", "trading"],
        "official_filings": ["10-k", "10-q", "filing", "sec", "prospectus"],
        "research_reports": ["analysis", "research", "report", "forecast"],
        "news_sources": ["news", "announcement", "press"],
    }
    for source_type, keywords in source_keywords.items():
        if any(keyword in query_lower for keyword in keywords):
            sources.append(source_type)
    return sources or ["financial_news"]
