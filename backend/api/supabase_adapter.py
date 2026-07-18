"""Project-scoped retrieval bridge for the multi-agent pipeline.

The application database is the Supabase Postgres/pgvector store.  The
multi-agent code expects plain dictionaries, while the chat RAG layer returns
LangChain documents, so this module owns the conversion between those two
formats.
"""

from __future__ import annotations

from typing import Any, Sequence

from api.generate_answer import (
    HybridMultiQueryRetriever,
    RetrievedDocument,
    load_chunks_from_database,
)


def _document_to_context(result: RetrievedDocument) -> dict[str, Any]:
    document = result.document
    metadata = document.metadata or {}
    text = document.page_content.strip()
    return {
        "text": text,
        "content": text,
        "source": metadata.get("source_file", "unknown"),
        "page": metadata.get("page", metadata.get("page_number", 1)),
        "score": float(result.score),
        "chunk_id": str(metadata.get("_chunk_id", metadata.get("chunk_id", "unknown"))),
        "document_id": str(metadata.get("document_id", "")),
    }


def retrieve_context_docs(
    project_id: Any,
    query: str,
    max_results: int = 5,
    extra_chunks: Sequence[Any] | None = None,
) -> tuple[list[dict[str, Any]], list[str], list[dict[str, Any]]]:
    """Retrieve project chunks with the existing hybrid Supabase RAG index."""
    indexed_chunks = load_chunks_from_database(project_id)
    retriever = HybridMultiQueryRetriever(indexed_chunks, extra_chunks=extra_chunks)
    results, query_variations = retriever.search_multi_query(
        query=query,
        max_variants=3,
        candidate_k=max(max_results, 5),
        vector_weight=0.7,
        keyword_weight=0.3,
        query_fusion_k=60,
        retrieval_fusion_k=60,
    )
    selected = list(results[:max_results])
    context_docs = [_document_to_context(result) for result in selected]
    sources = [
        {
            "chunk_id": item["chunk_id"],
            "source_file": item["source"],
            "score": item["score"],
            "content": item["content"],
        }
        for item in context_docs
    ]
    return context_docs, query_variations, sources


def load_context_docs(project_id: Any, query: str, max_results: int = 5) -> list[dict[str, Any]]:
    """Return agent-compatible documents retrieved only from this project."""
    documents, _, _ = retrieve_context_docs(project_id, query, max_results=max_results)
    return documents


def search_additional_context(project_id: Any, query: str, max_results: int = 5) -> list[dict[str, Any]]:
    """Retrieve more project-scoped context for evaluator/advisor follow-ups."""
    return load_context_docs(project_id, query, max_results=max_results)
