"""
Answer agent for finance Q&A.
"""

from __future__ import annotations

import importlib
from typing import Any


class AnswerAgent:
    """Generates the final grounded answer for Q&A queries."""

    def __init__(self) -> None:
        # Read by the orchestrator so an LLM failure is visible in the agent
        # run log instead of silently degrading to a context dump.
        self.last_error: str | None = None

    def run(
        self,
        query: str,
        context_docs: list[dict[str, Any]],
        metadata: dict[str, Any] | None = None,
    ) -> str:
        metadata = metadata or {}
        self.last_error = None
        llm = self._build_external_llm()
        if llm is not None and context_docs:
            context = self._context_to_string(context_docs)
            prompt = (
                "You are the final AnswerAgent in a financial multi-agent system. "
                "The context below was written by RetrievalAgent and SearchAgent into shared request memory. "
                "Answer the user's question directly, using only factual claims supported by that context. "
                "Do not describe the agent workflow or dump raw context. "
                "Cite factual claims as [Source 1], [Source 2], etc. "
                "If the evidence does not answer the question, state exactly what is missing instead of guessing. "
                "When the user requests a chart or illustration and the context has dated numerical values, include "
                "a compact Markdown table suitable for charting; do not invent values.\n\n"
                "FINANCIAL FIGURE GROUNDING RULES — STRICTLY ENFORCED:\n"
                "F1. Every financial number you write (revenue, net income, EPS, assets, debt, margins, ratios, "
                "percentages, share price, etc.) MUST appear verbatim in the Context Documents below. "
                "Never recall or infer a figure from your training knowledge.\n"
                "F2. Do NOT round or simplify source figures. "
                "If the document says '$21,301 million', write '$21,301 million', not '$21B' or '$21.3B'.\n"
                "F3. If a required figure is absent from the context, write exactly: "
                "'[Figure not available in provided documents]' — do not substitute an estimate.\n"
                "F4. Round numbers like '$3,000,000,000' or '$20,000,000,000' are a hallucination red flag. "
                "Only use such values if they appear exactly that way in the source text.\n\n"
                f"User Query:\n{query}\n\n"
                f"Context Documents:\n{context}\n\n"
                "Return a complete, concise answer in Markdown."
            )
            try:
                return llm.generate_response(prompt)
            except Exception as exc:
                self.last_error = self._format_error("generation", exc)
        elif llm is None and self.last_error is None:
            self.last_error = "AnswerAgent could not initialise the answer model."

        if not context_docs:
            return (
                f"I could not find enough grounded financial context to answer: {query}\n\n"
                "Try asking about a company, filing, or market topic, or add source documents to your project."
            )

        lines = [
            "I found relevant source material, but the answer model could not complete a grounded response for this request.",
            "Please retry after checking the server's `OPENAI_API_KEY` and agent run log.",
            "",
            "Available sources:",
        ]
        for index, doc in enumerate(context_docs[:5], start=1):
            lines.append(f"- [Source {index}] {doc.get('source', f'doc-{index}')}")
        return "\n".join(lines)

    def _build_external_llm(self):
        try:
            module = importlib.import_module("ai_integration.models.external_llm")
            return module.ExternalLLM()
        except Exception as exc:
            self.last_error = self._format_error("initialisation", exc)
            return None

    def _context_to_string(self, context_docs: list[dict[str, Any]]) -> str:
        parts = []
        # Keep the prompt bounded; SearchAgent already reranks this list.
        for index, doc in enumerate(context_docs[:8], start=1):
            source = doc.get("source", f"doc-{index}")
            title = doc.get("source_title", source)
            text = str(doc.get("text", doc.get("content", ""))).strip()[:3500]
            parts.append(f"--- SOURCE {index}: {title} ({source}) ---\n{text}")
        return "\n\n".join(parts)

    @staticmethod
    def _format_error(stage: str, exc: Exception) -> str:
        message = str(exc).replace("\n", " ").strip()[:300]
        return f"answer_llm_{stage}_error:{type(exc).__name__}: {message}"
