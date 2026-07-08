"""
Retrieval agent for the planner pipeline.
"""

from __future__ import annotations

import importlib
from pathlib import Path
import re
from typing import Any


class RetrievalAgent:
    """Loads local context and retrieves the most relevant documents."""

    def __init__(self, config: dict[str, Any], raw_dir: Path) -> None:
        self.config = config
        self.raw_dir = raw_dir

    def run(self, query: str, memory: dict[str, Any] | None = None) -> dict[str, Any]:
        memory = dict(memory or {})
        workflow_steps: list[str] = []
        tool_calls: list[dict[str, Any]] = []
        tool_results: list[dict[str, Any]] = []
        errors: list[str] = []
        metadata: dict[str, Any] = {}

        documents = list(memory.get("documents", []))
        if not documents and self.raw_dir.exists():
            try:
                documents = self._load_documents_from_raw(str(self.raw_dir))
                workflow_steps.append("loaded_raw_documents")
                metadata["raw_document_count"] = len(documents)
            except Exception as exc:
                errors.append(f"load_documents_error: {exc}")

        top_k = int(memory.get("top_k", self.config.get("top_k", 5)))
        retrieved_docs: list[dict[str, Any]] = []
        similarity_score = 0.0

        retriever = self._build_retriever()
        if retriever is not None:
            try:
                retrieved_docs, _latency = retriever.retrieve(query)
                similarity_score = float(retrieved_docs[0].get("score", 0.0)) if retrieved_docs else 0.0
                workflow_steps.append("retrieved_local_context")
                tool_calls.append({"tool": "Retriever"})
                tool_results.append({"tool": "Retriever", "document_count": len(retrieved_docs)})
            except Exception as exc:
                errors.append(f"retriever_error: {exc}")

        if not retrieved_docs and documents:
            retrieved_docs, similarity_score = self._score_documents(query, documents, top_k=top_k)
            workflow_steps.append("retrieved_memory_context")
            tool_calls.append({"tool": "KeywordRetriever"})
            tool_results.append({"tool": "KeywordRetriever", "document_count": len(retrieved_docs)})

        threshold = float(memory.get("retrieval_threshold", 0.25))
        deduped_docs = self._deduplicate_documents(retrieved_docs)[:top_k]
        coverage_score = max(similarity_score, min(1.0, len(deduped_docs) / max(top_k, 1)))

        metadata["retrieval_similarity"] = similarity_score
        metadata["retrieval_threshold"] = threshold
        metadata["coverage_score"] = coverage_score
        metadata["final_context_count"] = len(deduped_docs)

        return {
            "context_docs": deduped_docs,
            "coverage_score": coverage_score,
            "workflow_steps": workflow_steps,
            "tool_calls": tool_calls,
            "tool_results": tool_results,
            "errors": errors,
            "metadata": metadata,
        }

    def _build_retriever(self):
        try:
            module = importlib.import_module("ai_integration.rag.retriever")
            return module.Retriever(self.config)
        except Exception:
            return None

    def _load_documents_from_raw(self, folder: str) -> list[dict[str, Any]]:
        module = importlib.import_module("ai_integration.ingestion.loader")
        return module.load_documents(folder)

    def _score_documents(
        self,
        query: str,
        documents: list[dict[str, Any]],
        *,
        top_k: int,
    ) -> tuple[list[dict[str, Any]], float]:
        scored_docs: list[dict[str, Any]] = []
        query_terms = set(re.findall(r"[a-zA-Z0-9]+", query.lower()))
        for document in documents:
            text = str(document.get("text", document.get("content", ""))).strip()
            if not text:
                continue
            doc_terms = set(re.findall(r"[a-zA-Z0-9]+", text.lower()))
            score = len(query_terms & doc_terms) / len(query_terms) if query_terms else 0.0
            enriched = dict(document)
            enriched["score"] = float(score)
            scored_docs.append(enriched)
        ranked = sorted(scored_docs, key=lambda item: item.get("score", 0.0), reverse=True)
        top_docs = ranked[:top_k]
        top_score = float(top_docs[0]["score"]) if top_docs else 0.0
        return top_docs, top_score

    def _deduplicate_documents(self, documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
        seen: set[tuple[str, str]] = set()
        unique: list[dict[str, Any]] = []
        for document in documents:
            text = str(document.get("text", document.get("content", ""))).strip()
            source = str(document.get("source", "unknown"))
            key = (source, text)
            if key in seen:
                continue
            seen.add(key)
            normalized = dict(document)
            normalized["text"] = text
            normalized["content"] = text
            normalized["source"] = source
            normalized["page"] = normalized.get("page", 1)
            unique.append(normalized)
        return unique
