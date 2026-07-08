"""
Answer agent for finance Q&A.
"""

from __future__ import annotations

import importlib
from typing import Any


class AnswerAgent:
    """Generates the final grounded answer for Q&A queries."""

    def run(
        self,
        query: str,
        context_docs: list[dict[str, Any]],
        metadata: dict[str, Any] | None = None,
    ) -> str:
        metadata = metadata or {}
        llm = self._build_external_llm()
        if llm is not None and context_docs:
            context = self._context_to_string(context_docs)
            prompt = (
                "You are AnswerAgent in a financial multi-agent system. "
                "Answer the user's finance question using only the provided context. "
                "If the evidence is weak or incomplete, say that clearly.\n\n"
                f"User Query:\n{query}\n\n"
                f"Context Documents:\n{context}\n\n"
                "Return a concise grounded answer in Markdown."
            )
            try:
                return llm.generate_response(prompt)
            except Exception:
                pass

        if not context_docs:
            return (
                f"I could not find enough grounded financial context to answer: {query}\n\n"
                "Try asking about a company, filing, market topic, or add source documents to `data/raw`."
            )

        lines = [
            f"Query: {query}",
            f"Retrieved context score: {metadata.get('coverage_score', metadata.get('retrieval_similarity', 0.0)):.2f}",
            "",
            "Grounded context:",
        ]
        for index, doc in enumerate(context_docs, start=1):
            text = str(doc.get("text", doc.get("content", ""))).strip().replace("\n", " ")
            lines.append(f"{index}. [{doc.get('source', f'doc-{index}')}] {text[:280]}")
        lines.append("")
        lines.append("Answer: The response should be based on the context above; add stronger source material if you need a deeper conclusion.")
        return "\n".join(lines)

    def _build_external_llm(self):
        try:
            module = importlib.import_module("ai_integration.models.external_llm")
            return module.ExternalLLM()
        except Exception:
            return None

    def _context_to_string(self, context_docs: list[dict[str, Any]]) -> str:
        parts = []
        for index, doc in enumerate(context_docs, start=1):
            source = doc.get("source", f"doc-{index}")
            text = doc.get("text", doc.get("content", ""))
            parts.append(f"--- DOCUMENT {index} (Source: {source}) ---\n{text}")
        return "\n\n".join(parts)
