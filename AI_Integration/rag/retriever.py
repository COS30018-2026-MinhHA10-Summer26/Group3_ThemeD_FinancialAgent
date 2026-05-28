"""
In-memory retrieval and reranking helpers for the financial agent.
"""

from __future__ import annotations

from typing import Any

from ai_integration.rag.embedding import cosine_like_similarity, embed_text


def score_document(query: str, document: dict[str, Any]) -> float:
    """Compute a similarity score between the query and document content."""

    query_embedding = embed_text(query)
    document_text = " ".join(
        str(part)
        for part in (
            document.get("title", ""),
            document.get("content", ""),
            document.get("summary", ""),
        )
        if part
    )
    document_embedding = embed_text(document_text)
    return cosine_like_similarity(query_embedding, document_embedding)


def retrieve_documents(
    query: str,
    documents: list[dict[str, Any]],
    top_k: int = 5,
) -> tuple[list[dict[str, Any]], float]:
    """Retrieve top-k documents from an in-memory corpus."""

    scored_documents: list[dict[str, Any]] = []
    for document in documents:
        enriched = dict(document)
        enriched["score"] = score_document(query, document)
        scored_documents.append(enriched)

    ranked = sorted(scored_documents, key=lambda item: item.get("score", 0.0), reverse=True)
    top_documents = ranked[: max(top_k, 1)]
    top_score = float(top_documents[0]["score"]) if top_documents else 0.0
    return top_documents, top_score


def rerank_documents(
    query: str,
    documents: list[dict[str, Any]],
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Rerank documents using the same fallback scoring function."""

    reranked, _ = retrieve_documents(query, documents, top_k=top_k)
    return reranked
