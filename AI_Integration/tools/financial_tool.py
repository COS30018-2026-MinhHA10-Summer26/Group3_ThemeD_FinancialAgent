"""
Financial analysis helper tool.
"""

from __future__ import annotations

import re
from typing import Any


TICKER_PATTERN = re.compile(r"\b[A-Z]{1,5}\b")


def financial_tool(
    query: str,
    *,
    retrieved_documents: list[dict[str, Any]] | None = None,
    similarity_score: float = 0.0,
) -> dict[str, Any]:
    """Extract finance-specific metadata from the user query and retrieval state."""

    documents = retrieved_documents or []
    tickers = [match.group(0) for match in TICKER_PATTERN.finditer(query)]
    keywords = [
        keyword
        for keyword in (
            "stock",
            "market",
            "earnings",
            "revenue",
            "guidance",
            "sentiment",
            "valuation",
            "analyst",
            "forecast",
        )
        if keyword in query.lower()
    ]

    return {
        "tool": "financial_tool",
        "query": query,
        "tickers": tickers,
        "matched_keywords": keywords,
        "retrieved_document_count": len(documents),
        "similarity_score": float(similarity_score),
        "summary": "Query metadata extracted for routing and response grounding.",
    }
