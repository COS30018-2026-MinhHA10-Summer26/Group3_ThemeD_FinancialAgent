"""
Simple chunking utilities for ingested financial documents.
"""

from __future__ import annotations

from typing import Any


def chunk_text(text: str, chunk_size: int = 600, overlap: int = 100) -> list[str]:
    """Split text into overlapping chunks using character windows."""

    cleaned = " ".join(text.split())
    if not cleaned:
        return []

    size = max(chunk_size, 1)
    step = max(size - max(overlap, 0), 1)
    return [cleaned[index : index + size] for index in range(0, len(cleaned), step)]


def chunk_documents(
    documents: list[dict[str, Any]],
    chunk_size: int = 600,
    overlap: int = 100,
) -> list[dict[str, Any]]:
    """Chunk a list of documents and preserve source metadata."""

    chunks: list[dict[str, Any]] = []
    for document in documents:
        base_content = str(document.get("content", ""))
        for position, content in enumerate(chunk_text(base_content, chunk_size, overlap), start=1):
            chunk = dict(document)
            chunk["content"] = content
            chunk["chunk_id"] = f"{document.get('source', 'doc')}#{position}"
            chunks.append(chunk)
    return chunks
