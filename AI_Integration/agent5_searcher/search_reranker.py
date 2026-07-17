"""
Hybrid reranker for search results.

After the SearchAgent downloads and extracts raw documents from the web,
this module chunks them, embeds them with a local Sentence Transformer model
(free, no API cost), builds a temporary in-RAM vector store with BM25 + vector
hybrid search, and returns only the Top K most relevant chunks.

This eliminates information overload in shared memory and avoids sending
hundreds of raw pages to downstream agents.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from ai_integration.ingestion.chunking import chunk_documents
from ai_integration.rag.bm25 import BM25Index
from ai_integration.rag.embedding_model import EmbeddingModel


# Default settings (mirrors config.yaml for the main RAG pipeline)
_DEFAULT_CHUNK_SIZE = 400
_DEFAULT_CHUNK_OVERLAP = 50
_DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"
_DEFAULT_VECTOR_WEIGHT = 0.6
_DEFAULT_BM25_WEIGHT = 0.4


def rerank_search_results(
    query: str,
    raw_documents: list[dict[str, Any]],
    *,
    top_k: int = 10,
    chunk_size: int = _DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = _DEFAULT_CHUNK_OVERLAP,
    embedding_model_name: str = _DEFAULT_EMBEDDING_MODEL,
    vector_weight: float = _DEFAULT_VECTOR_WEIGHT,
    bm25_weight: float = _DEFAULT_BM25_WEIGHT,
) -> list[dict[str, Any]]:
    """Chunk, embed, and hybrid-search raw documents to return the Top K chunks.

    Parameters
    ----------
    query:
        The user's original search query.
    raw_documents:
        Raw sections extracted from downloaded PDFs (each dict must have a
        ``"text"`` key and ideally ``"source"``, ``"page"`` metadata).
    top_k:
        Number of best chunks to return.
    chunk_size / chunk_overlap:
        Chunking parameters passed to ``chunk_documents()``.
    embedding_model_name:
        Sentence Transformer model name (runs locally, free).
    vector_weight / bm25_weight:
        Weights for the hybrid RRF fusion.

    Returns
    -------
    list[dict[str, Any]]
        The top-K most relevant chunks with metadata and scores.
    """
    if not raw_documents or not query or not query.strip():
        return []

    # ── Step 1: Normalise raw documents ──────────────────────────────
    normalised = _normalise_documents(raw_documents)
    if not normalised:
        return []

    # ── Step 2: Chunk ────────────────────────────────────────────────
    chunks = chunk_documents(normalised, chunk_size, chunk_overlap)
    if not chunks:
        return []

    # ── Step 3: Embed (local Sentence Transformer, free) ─────────────
    texts = [chunk["text"] for chunk in chunks]
    model = EmbeddingModel(embedding_model_name)
    chunk_embeddings = model.embed(texts)
    query_embedding = model.embed_query(query)

    # ── Step 4: Hybrid search (BM25 + Vector via RRF) ────────────────
    ranked = _hybrid_search(
        query_text=query,
        query_embedding=query_embedding,
        chunk_embeddings=chunk_embeddings,
        chunks=chunks,
        top_k=top_k,
        vector_weight=vector_weight,
        bm25_weight=bm25_weight,
    )

    return ranked


# ── Internal helpers ─────────────────────────────────────────────────


def _normalise_documents(docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Ensure every document has at least ``text``, ``source``, ``page``."""
    normalised: list[dict[str, Any]] = []
    for doc in docs:
        text = str(doc.get("text", doc.get("content", ""))).strip()
        if not text:
            continue
        normalised.append({
            **doc,
            "text": text,
            "source": doc.get("source", "web_search"),
            "page": doc.get("page", 0),
        })
    return normalised


def _hybrid_search(
    query_text: str,
    query_embedding: np.ndarray,
    chunk_embeddings: np.ndarray,
    chunks: list[dict[str, Any]],
    top_k: int,
    vector_weight: float,
    bm25_weight: float,
) -> list[dict[str, Any]]:
    """RRF fusion of vector cosine-similarity and BM25 scores."""

    # --- Vector ranking (cosine similarity) ---
    query_vec = np.array(query_embedding, dtype="float32")
    if query_vec.ndim == 1:
        query_vec = query_vec.reshape(1, -1)
    chunk_vecs = np.array(chunk_embeddings, dtype="float32")

    # Normalise for cosine similarity
    query_norm = query_vec / (np.linalg.norm(query_vec, axis=1, keepdims=True) + 1e-10)
    chunk_norms = chunk_vecs / (np.linalg.norm(chunk_vecs, axis=1, keepdims=True) + 1e-10)
    cosine_scores = (chunk_norms @ query_norm.T).flatten()

    vector_ranked_indices = np.argsort(-cosine_scores)

    # --- BM25 ranking ---
    bm25 = BM25Index()
    bm25.add_documents([chunk["text"] for chunk in chunks])
    bm25_scores = bm25.score(query_text)
    bm25_ranked_indices = np.argsort(-np.array(bm25_scores))

    # --- RRF fusion ---
    rrf_scores: dict[int, float] = {}
    for rank, idx in enumerate(vector_ranked_indices):
        rrf_scores[int(idx)] = rrf_scores.get(int(idx), 0.0) + vector_weight / (rank + 1)
    for rank, idx in enumerate(bm25_ranked_indices):
        rrf_scores[int(idx)] = rrf_scores.get(int(idx), 0.0) + bm25_weight / (rank + 1)

    # Sort by RRF score descending, take top K
    top_indices = sorted(rrf_scores, key=lambda i: rrf_scores[i], reverse=True)[:top_k]

    results: list[dict[str, Any]] = []
    for idx in top_indices:
        chunk = dict(chunks[idx])
        chunk["score"] = round(rrf_scores[idx], 6)
        chunk["cosine_score"] = round(float(cosine_scores[idx]), 6)
        chunk["bm25_score"] = round(float(bm25_scores[idx]), 6)
        results.append(chunk)

    return results
