"""
RAG-only evaluation pipeline: 7 documents × 8 queries = 56 scenarios.

Each scenario sends CONTEXT_DOCS + USER_QUERY directly to the LLM (no
multi-agent pipeline), then evaluates the response with EvaluatorAgent
in Mode A (RAG-only mode).

Output: evaluation_for_paper/result_for_rag_only/document_{i}/query_{q}/report_v0.py

Run from workspace root:
    python evaluation_for_paper/pipeline/run_pipeline_rag_only.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Project root  (file is 2 levels below workspace root)
# ---------------------------------------------------------------------------

project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ---------------------------------------------------------------------------
# .env loading
# ---------------------------------------------------------------------------

from dotenv import load_dotenv  # noqa: E402

env_path = Path(project_root) / "backend" / ".env"
load_dotenv(dotenv_path=str(env_path))

# ---------------------------------------------------------------------------
# Imports (after sys.path is set and .env is loaded)
# ---------------------------------------------------------------------------

import openai                                                            # noqa: E402
from openai import OpenAI                                               # noqa: E402
from ai_integration.agent4_evaluator.evaluator import EvaluatorAgent   # noqa: E402

# ---------------------------------------------------------------------------
# Context trimmer — prevents TPM overflow on large documents
# ---------------------------------------------------------------------------

def select_relevant_chunks(
    query: str,
    context_docs: List[Dict[str, Any]],
    max_chunks: int = 20,
) -> List[Dict[str, Any]]:
    """
    Return top-N most query-relevant chunks using token overlap scoring.
    Prevents TPM overflow on large documents like TSLA 2022 (458 chunks).
    """
    import re

    def _tokens(text: str) -> set:
        return set(re.findall(r"[a-z0-9]+", text.lower()))

    query_tokens = _tokens(query)
    if not query_tokens:
        return context_docs[:max_chunks]

    scored: List[tuple] = []
    for i, doc in enumerate(context_docs):
        text = str(doc.get("text", ""))
        doc_tokens = _tokens(text)
        overlap = len(query_tokens & doc_tokens)
        scored.append((overlap, i, doc))

    scored.sort(key=lambda x: (-x[0], x[1]))
    top = [doc for _, _, doc in scored[:max_chunks]]

    first = context_docs[0]
    if first not in top:
        top = [first] + top[:max_chunks - 1]

    original_order = {id(doc): i for i, doc in enumerate(context_docs)}
    top.sort(key=lambda doc: original_order.get(id(doc), 0))

    return top


# ---------------------------------------------------------------------------
# Stage 1: Direct RAG response (no multi-agent pipeline)
# ---------------------------------------------------------------------------

def generate_rag_response(
    client: OpenAI,
    model: str,
    query: str,
    context_docs: List[Dict[str, Any]],
) -> str:
    """Send context docs + query directly to the LLM. No agent pipeline."""
    context_parts = []
    for i, doc in enumerate(context_docs, 1):
        source = doc.get("source", f"Doc {i}")
        text = str(doc.get("text", "")).strip()
        # Truncate to 2500 chars per doc to stay within token limits
        if len(text) > 2500:
            text = text[:2500] + "\n... [truncated]"
        context_parts.append(f"--- Document {i} (Source: {source}) ---\n{text}")
    context_str = "\n\n".join(context_parts)

    prompt = (
        f"Based on the following documents, answer this question:\n\n"
        f"Question: {query}\n\n"
        f"Documents:\n{context_str}\n\n"
        "Provide a clear, concise answer grounded in the documents above. "
        "If the documents do not contain enough information to answer the question, say so explicitly."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


def _safe_generate_rag(
    client: OpenAI,
    model: str,
    query: str,
    context_docs: List[Dict[str, Any]],
) -> str:
    """Wrapper around generate_rag_response with retry logic for RateLimitError."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return generate_rag_response(client, model, query, context_docs)
        except openai.RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait = (attempt + 1) * 4
            print(f"   [RAG] RateLimitError, retrying in {wait}s...")
            time.sleep(wait)
    # Should never reach here due to raise above, but satisfies type checker
    raise RuntimeError("Exhausted retries in _safe_generate_rag")


# ---------------------------------------------------------------------------
# File writer
# ---------------------------------------------------------------------------

def write_report_v0(
    path: Path,
    doc_index: int,
    query_index: int,
    pdf_filename: str,
    user_query: str,
    rag_response: str,
    evaluation_report: str,
) -> None:
    """Write a report_v0.py file for a single (document, query) scenario."""
    content = (
        '"""\n'
        f"RAG-only Evaluation Report: document_{doc_index} / query_{query_index}\n"
        f"Source document: {pdf_filename}\n"
        f"Query: {user_query}\n"
        '"""\n'
        "from __future__ import annotations\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        'RAG_RESPONSE = """\n'
        f"{rag_response}\n"
        '"""\n\n'
        'EVALUATION_REPORT = """\n'
        f"{evaluation_report}\n"
        '"""\n'
    )
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Document module loader
# ---------------------------------------------------------------------------

def load_document_module(doc_index: int) -> Any:
    """Load evaluation_for_paper/paper_sources/document_{i}.py via importlib."""
    source_path = (
        Path(__file__).parent.parent / "paper_sources" / f"document_{doc_index}.py"
    )
    module_name = f"paper_document_rag_{doc_index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load from {source_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY is missing. Please define it in backend/.env")
        sys.exit(1)

    model = "gpt-4o-mini"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    evaluator = EvaluatorAgent(model=model)

    results_base = Path(project_root) / "evaluation_for_paper" / "result_for_rag_only"

    total_docs = 7
    total_scenarios = 0
    completed = 0
    failed: List[str] = []

    for doc_index in range(5, total_docs - 1):
        try:
            doc_module = load_document_module(doc_index)
            user_queries: List[str] = doc_module.USER_QUERIES
            context_docs: List[Dict[str, Any]] = doc_module.CONTEXT_DOCS
            pdf_filename: str = context_docs[0]["source"].split(" (")[0]

            print()
            print("=" * 60)
            print(f"DOCUMENT {doc_index}/{total_docs}: {pdf_filename}")
            print(f"  {len(user_queries)} queries -> {len(user_queries)} scenarios")
            print("=" * 60)

            for query_index, user_query in enumerate(user_queries, start=1):
                total_scenarios += 1
                scenario_label = f"document_{doc_index}/query_{query_index}"

                scenario_dir = (
                    results_base
                    / f"document_{doc_index}"
                    / f"query_{query_index}"
                )
                scenario_dir.mkdir(parents=True, exist_ok=True)

                # Resume-safe: skip if already completed
                if (scenario_dir / "report_v0.py").exists():
                    print(f"  [SKIP] {scenario_label} already complete.")
                    completed += 1
                    continue

                try:
                    # Trim context to top-20 relevant chunks to stay under TPM limits
                    context_docs_trimmed = select_relevant_chunks(user_query, context_docs, max_chunks=20)
                    print(f"    Context trimmed to {len(context_docs_trimmed)} relevant chunks")

                    # ----------------------------------------------------------
                    # Stage 1: Direct RAG response
                    # ----------------------------------------------------------
                    print(f"\n  [Stage 1] RAG response: {scenario_label}")
                    print(f"    Query: {user_query[:90]}{'...' if len(user_query) > 90 else ''}")
                    rag_response = _safe_generate_rag(client, model, user_query, context_docs_trimmed)
                    print(f"    RAG response generated ({len(rag_response)} chars)")

                    # ----------------------------------------------------------
                    # Stage 2: Evaluator Mode A (no critic_issues, no advisor_report_v2)
                    # ----------------------------------------------------------
                    print(f"\n  [Stage 2] Evaluator Mode A: {scenario_label}")
                    evaluation_report = evaluator.run(
                        query=user_query,
                        context_docs=context_docs_trimmed,
                        response=rag_response,
                        # critic_issues and advisor_report_v2 NOT passed -> Mode A
                    )
                    print(f"    Evaluation report generated ({len(evaluation_report)} chars)")

                    # ----------------------------------------------------------
                    # Save report_v0.py
                    # ----------------------------------------------------------
                    write_report_v0(
                        path=scenario_dir / "report_v0.py",
                        doc_index=doc_index,
                        query_index=query_index,
                        pdf_filename=pdf_filename,
                        user_query=user_query,
                        rag_response=rag_response,
                        evaluation_report=evaluation_report,
                    )
                    print(f"    Saved: {scenario_label}/report_v0.py")

                    completed += 1
                    print(f"\n  ✓ {scenario_label} DONE  ({completed} completed so far)")

                except Exception:
                    traceback.print_exc()
                    failed.append(scenario_label)
                    print(f"\n  [ERROR] {scenario_label} failed - skipping\n")
                    continue

        except Exception:
            traceback.print_exc()
            print(f"\n[ERROR] Failed to load document_{doc_index} - skipping entire document\n")
            continue

    print()
    print("=" * 60)
    print("PIPELINE COMPLETE")
    print(f"  Total scenarios : {total_scenarios}")
    print(f"  Completed       : {completed}")
    print(f"  Failed          : {len(failed)}")
    if failed:
        print("  Failed scenarios:")
        for s in failed:
            print(f"    - {s}")
    print("=" * 60)


if __name__ == "__main__":
    main()
