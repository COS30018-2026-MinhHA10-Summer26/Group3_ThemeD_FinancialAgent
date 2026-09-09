"""Run the financial multi-agent workflow for a project chat message."""

from __future__ import annotations

from typing import Any, Callable

from ai_integration.agent1_planner.orchestrator import PlanningOrchestrator
from api.history_aware import prepare_history_aware_query
from api.supabase_adapter import retrieve_context_docs, search_additional_context


ProgressCallback = Callable[[str, str], None]


def _agent_run_log(state: dict[str, Any]) -> dict[str, Any]:
    shared_memory = state.get("shared_memory")
    evaluator_verdict = {}
    if shared_memory is not None:
        evaluator_verdict = shared_memory.get_evaluator_verdict()

    return {
        "route": state.get("route"),
        "classification_reason": state.get("classification_reason"),
        "classification_confidence": state.get("classification_confidence"),
        "workflow_steps": list(state.get("workflow_steps", [])),
        "executed_agents": list(state.get("executed_agents", [])),
        "coverage_score": state.get("coverage_score"),
        "evaluator_verdict": evaluator_verdict.get("verdict"),
        "errors": [str(error) for error in state.get("errors", [])],
    }


def run_multi_agent_chat(
    query: str,
    project_id: Any,
    conversation_id: Any,
    image_base64: str | None = None,
    pdf_chunks: list[Any] | None = None,
    progress_callback: ProgressCallback | None = None,
    user_id: Any = None,
) -> dict[str, Any]:
    """Return an orchestrated response grounded in the project's Supabase chunks."""
    contextual_query, conversation_history = prepare_history_aware_query(query, conversation_id)
    if progress_callback:
        progress_callback("classifying", "Classifying question...")
        progress_callback("retrieving", "Retrieving project documents...")

    context_docs, query_variations, sources = retrieve_context_docs(
        project_id,
        contextual_query,
        max_results=5,
        extra_chunks=pdf_chunks,
    )
    if progress_callback:
        progress_callback("retrieving", f"Found {len(context_docs)} related documents")

    metadata = {
        "project_id": str(project_id),
        "conversation_id": str(conversation_id),
        "user_id": str(user_id) if user_id is not None else None,
        "original_query": query,
        "contextual_query": contextual_query,
        "conversation_turn_count": len(conversation_history),
        "has_uploaded_image": bool(image_base64),
        "has_uploaded_pdf": bool(pdf_chunks),
        "retrieval_backend": "supabase_pgvector",
    }
    orchestrator = PlanningOrchestrator(
        progress_callback=progress_callback,
    )
    state = orchestrator.run(
        contextual_query,
        memory={"documents": context_docs, "top_k": 5, "metadata": metadata},
    )
    return {
        "answer": str(state.get("final_output", "")),
        "route": state.get("route"),
        "original_query": query,
        "contextual_query": contextual_query,
        "query_variations": query_variations,
        "sources": sources,
        "agent_run_log": _agent_run_log(state),
    }
