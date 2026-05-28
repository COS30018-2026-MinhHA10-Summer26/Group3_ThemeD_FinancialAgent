"""
Lightweight LLM helpers for the financial agent.

The module keeps the interface simple so the orchestrator can run even when
cloud or local model dependencies are not installed yet.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable
from transformers import AutoTokenizer, AutoModelForCausalLM

CONTEXT_PATH = "agent_context.md"
with open(CONTEXT_PATH, "r") as f:
    try:
        CONTEXT = f.read()
    except UnicodeDecodeError:
        f.seek(0)
        f.encoding = "utf-8"
        CONTEXT = f.read()

@dataclass
class LLMResponse:
    """Small response wrapper that mirrors `.content` access patterns."""
    content: str


def _message_content(messages: Iterable[dict[str, str] | tuple[str, str]]) -> list[str]:
    parts: list[str] = []
    for message in messages:
        if isinstance(message, tuple):
            _, content = message
        else:
            content = message.get("content", "")
        if content:
            parts.append(content.strip())
    return parts


class FinancialLLM:
    """A deterministic fallback used for planning and synthesis."""
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-7B-Instruct")
        self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-7B-Instruct", device_map="auto")
        self.model.eval()

    def synthesize(
        self,
        *,
        query: str,
        context_documents: list[dict[str, object]],
        similarity_score: float,
        used_web_search: bool,
    ) -> str:
        if not context_documents:
            return (
                f"I could not find grounded context for: {query}. "
                "Please provide more source material or enable a live data source."
            )

        lines = [
            f"Query: {query}",
            f"Retrieval confidence: {similarity_score:.2f}",
            f"Web augmentation used: {'yes' if used_web_search else 'no'}",
            "",
            "Grounded findings:",
        ]

        for index, document in enumerate(context_documents, start=1):
            source = str(document.get("source", document.get("title", f"document-{index}")))
            content = str(document.get("content", "")).strip()
            condensed = re.sub(r"\s+", " ", content)
            snippet = condensed[:280] + ("..." if len(condensed) > 280 else "")
            lines.append(f"{index}. [{source}] {snippet}")

        lines.append("")
        lines.append(
            "Summary: The answer above is synthesized from the highest ranked retrieved context."
        )
        return "\n".join(lines)
    def invoke(self,prompt: str,query:str) -> str:
        prompt = build_prompt(query,CONTEXT,prompt)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(
            device=self.model.device
        )
        outputs = self.model.generate(**inputs, max_new_tokens=300)
        generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        return self.tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()


def get_llm() -> FinancialLLM:
    """Return the default LLM interface for the orchestrator."""

    return FinancialLLM()

def build_prompt(query,context,prompt):
    return f"Context: {context}\n\n Task: {prompt}\n\nQuery: {query}\n\nAnswer:"