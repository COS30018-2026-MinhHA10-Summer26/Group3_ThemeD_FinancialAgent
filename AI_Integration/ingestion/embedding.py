"""
Fallback embedding helpers based on token sets.

These utilities keep the project runnable before a real embedding model or
vector store is added.
"""

from __future__ import annotations

import math
import re


def tokenize(text: str) -> set[str]:
    """Normalize text into a set of lowercase tokens."""

    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def embed_text(text: str) -> set[str]:
    """Create a lightweight embedding representation."""

    return tokenize(text)


def cosine_like_similarity(left: set[str], right: set[str]) -> float:
    """Score two token sets with a cosine-style overlap metric."""

    if not left or not right:
        return 0.0
    overlap = len(left & right)
    denominator = math.sqrt(len(left)) * math.sqrt(len(right))
    if denominator == 0:
        return 0.0
    return overlap / denominator
