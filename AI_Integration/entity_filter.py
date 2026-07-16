"""Entity-aware relevance helpers for company-specific retrieval."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable


COMPANY_ALIASES: dict[str, tuple[str, ...]] = {
    "tesla": ("tesla", "tsla", "tesla inc"),
    "apple": ("apple", "aapl", "apple inc"),
    "microsoft": ("microsoft", "msft", "microsoft corporation"),
    "nvidia": ("nvidia", "nvda", "nvidia corporation"),
    "adobe": ("adobe", "adbe", "adobe inc"),
    "target": ("target", "tgt", "target corporation"),
    "disney": ("disney", "dis", "walt disney", "the walt disney company"),
    "unilever": ("unilever", "ul", "ulvr"),
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "buy",
    "for",
    "from",
    "i",
    "in",
    "is",
    "of",
    "or",
    "outlook",
    "should",
    "stock",
    "strategic",
    "the",
    "to",
    "what",
    "with",
}


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def document_text(document: dict[str, Any]) -> str:
    source = Path(str(document.get("source", ""))).name
    parts = [
        source,
        document.get("section_title", ""),
        document.get("text", document.get("content", "")),
    ]
    return normalize_text(" ".join(str(part) for part in parts if part))


def extract_entity_aliases(query: str, metadata: dict[str, Any] | None = None) -> set[str]:
    """Return aliases that must be present when the user names a known company."""

    metadata = metadata or {}
    query_text = normalize_text(query)
    aliases: set[str] = set()

    company_name = normalize_text(metadata.get("company_name"))
    if company_name:
        aliases.add(company_name)

    for canonical, known_aliases in COMPANY_ALIASES.items():
        if any(_contains_alias(query_text, alias) for alias in known_aliases):
            aliases.update(known_aliases)
            aliases.add(canonical)

    for ticker in re.findall(r"\b[A-Z]{1,5}\b", str(query or "")):
        if ticker.lower() not in STOPWORDS:
            aliases.add(ticker.lower())

    return {alias for alias in aliases if alias}


def matches_query_entity(
    query: str,
    document: dict[str, Any],
    metadata: dict[str, Any] | None = None,
) -> bool:
    aliases = extract_entity_aliases(query, metadata)
    if not aliases:
        return True
    text = document_text(document)
    return any(_contains_alias(text, alias) for alias in aliases)


def filter_documents_for_query_entity(
    query: str,
    documents: Iterable[dict[str, Any]],
    metadata: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    return [doc for doc in documents if matches_query_entity(query, doc, metadata)]


def lexical_relevance_score(query: str, document: dict[str, Any], metadata: dict[str, Any] | None = None) -> float:
    text = document_text(document)
    query_terms = {
        term
        for term in re.findall(r"[a-zA-Z0-9]+", normalize_text(query))
        if term not in STOPWORDS and len(term) > 1
    }
    if not query_terms:
        return 0.0

    doc_terms = set(re.findall(r"[a-zA-Z0-9]+", text))
    score = len(query_terms & doc_terms) / len(query_terms)
    aliases = extract_entity_aliases(query, metadata)
    if aliases and any(_contains_alias(text, alias) for alias in aliases):
        score += 1.0
    return float(score)


def _contains_alias(text: str, alias: str) -> bool:
    alias = normalize_text(alias)
    if not alias:
        return False
    if len(alias) <= 5 and alias.isalnum():
        return re.search(rf"\b{re.escape(alias)}\b", text) is not None
    return alias in text
