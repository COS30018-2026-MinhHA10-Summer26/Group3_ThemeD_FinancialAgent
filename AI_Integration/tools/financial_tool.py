"""
Financial domain helper tool.
"""

from __future__ import annotations

import re
from typing import Any


TICKER_PATTERN = re.compile(r"\b[A-Z]{1,5}\b")


def financial_tool(query: str) -> dict[str, Any]:
    """
    Extract simple finance-oriented metadata from a query.

    This is intentionally lightweight and deterministic until a live market
    data source is integrated.
    """

    tickers = [match.group(0) for match in TICKER_PATTERN.finditer(query)]
    finance_terms = [
        "stock",
        "earnings",
        "revenue",
        "guidance",
        "market",
        "sentiment",
        "analyst",
        "price",
        "valuation",
    ]
    matched_terms = [term for term in finance_terms if term in query.lower()]

    return {
        "tool": "financial_tool",
        "query": query,
        "tickers": tickers,
        "matched_terms": matched_terms,
        "summary": (
            "Detected finance-specific language to steer retrieval and search expansion."
        ),
    }
