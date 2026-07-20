"""Lightweight, local relevance scoring for SearchAgent coverage checks."""

from __future__ import annotations

from collections import Counter
import math
import re


def _term_counts(text: str) -> Counter[str]:
    """Create a deterministic bag-of-words vector without a model download."""

    return Counter(re.findall(r"[a-z0-9]+", str(text or "").lower()))


def _cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0

    dot_product = sum(count * right.get(term, 0) for term, count in left.items())
    left_norm = math.sqrt(sum(count * count for count in left.values()))
    right_norm = math.sqrt(sum(count * count for count in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot_product / (left_norm * right_norm)


def similarity_score(query: str, documents: list[str]) -> float:
    """Return the best lexical cosine similarity between a query and documents.

    Coverage is only a routing signal, so it does not need a transformer model.
    Keeping it lexical avoids comparing integer token IDs (which caused the
    Long-vs-float error) and accepts arbitrarily long extracted PDF text.
    """

    query_terms = _term_counts(query)
    scores = [_cosine_similarity(query_terms, _term_counts(document)) for document in documents if document]
    return max(scores, default=0.0)


def calculate_coverage(query: str, documents: list[str]) -> float:
    return similarity_score(query, documents)
