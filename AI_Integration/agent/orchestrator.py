"""
Deterministic LangGraph-style orchestrator for the financial research agent.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Callable

try:
    from langgraph.graph import END, StateGraph
except ImportError:  # pragma: no cover - fallback for environments without langgraph
    END = "__END__"
    StateGraph = None

from ai_integration.agent.state import AgentState, create_initial_state
from ai_integration.models.llm import get_llm
from ai_integration.rag.chunking import chunk_documents
from ai_integration.rag.retriever import rerank_documents, retrieve_documents
from ai_integration.tools.financial_tool import financial_tool
from ai_integration.tools.report_writer import write_report
from ai_integration.tools.web_search_tool import web_search_tool


def _append_message(state: AgentState, role: str, content: str) -> None:
    state.setdefault("messages", []).append({"role": role, "content": content})


def _append_step(state: AgentState, step: str) -> None:
    state.setdefault("workflow_steps", []).append(step)


def _deduplicate_documents(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    unique: list[dict[str, Any]] = []
    for document in documents:
        key = (
            str(document.get("source", document.get("title", ""))),
            str(document.get("content", "")),
        )
        if key not in seen:
            seen.add(key)
            unique.append(document)
    return unique


class _CompiledFallbackGraph:
    """Small fallback runner when LangGraph is unavailable."""

    def __init__(self, runner: Callable[[AgentState], AgentState]) -> None:
        self._runner = runner

    def invoke(self, state: AgentState) -> AgentState:
        return self._runner(deepcopy(state))


def create_orchestrator():
    """Create and return the deterministic orchestrator graph."""

    llm = get_llm()

    def input_node(state: AgentState) -> AgentState:
        state["cleaned_query"] = state["query"].strip()
        query_lower = state["cleaned_query"].lower()
        state["report_requested"] = any(
            keyword in query_lower for keyword in ("report", "pdf", "markdown", "docx")
        )
        _append_message(state, "user", state["cleaned_query"])
        _append_step(state, "input_processed")
        return state

    def retrieval_node(state: AgentState) -> AgentState:
        tool_result = financial_tool(state["cleaned_query"])
        state.setdefault("tool_results", []).append(tool_result)
        state.setdefault("tool_calls", []).append({"tool": "financial_tool"})

        retrieved_documents, top_score = retrieve_documents(
            state["cleaned_query"],
            state.get("documents", []),
            top_k=state.get("top_k", 5),
        )
        state["retrieved_documents"] = retrieved_documents
        state["similarity_score"] = top_score
        _append_step(state, "retrieval_completed")
        return state

    def threshold_node(state: AgentState) -> AgentState:
        threshold = state.get("retrieval_threshold", 0.25)
        if state.get("similarity_score", 0.0) >= threshold:
            state["route"] = "use_existing_context"
        else:
            state["route"] = "web_search"
        _append_step(state, f"threshold_checked:{state['route']}")
        return state

    def route_after_threshold(state: AgentState) -> str:
        return state.get("route", "use_existing_context")

    def query_expansion_node(state: AgentState) -> AgentState:
        state["expanded_queries"] = llm.expand_query(state["cleaned_query"])
        _append_step(state, "query_expanded")
        return state

    def web_search_node(state: AgentState) -> AgentState:
        results = web_search_tool(state.get("expanded_queries", []))
        state["web_documents"] = results
        state.setdefault("tool_calls", []).append({"tool": "web_search_tool"})
        state.setdefault("tool_results", []).append(
            {"tool": "web_search_tool", "count": len(results)}
        )
        _append_step(state, "web_search_completed")
        return state

    def ingestion_node(state: AgentState) -> AgentState:
        state["web_documents"] = chunk_documents(state.get("web_documents", []))
        _append_step(state, "documents_chunked")
        return state

    def merge_node(state: AgentState) -> AgentState:
        merged = state.get("retrieved_documents", []) + state.get("web_documents", [])
        state["merged_documents"] = _deduplicate_documents(merged)
        _append_step(state, "context_merged")
        return state

    def rerank_node(state: AgentState) -> AgentState:
        reranked = rerank_documents(
            state["cleaned_query"],
            state.get("merged_documents", []),
            top_k=state.get("top_k", 5),
        )
        state["reranked_documents"] = reranked
        state["final_context"] = reranked[: state.get("top_k", 5)]
        _append_step(state, "reranked")
        return state

    def generation_node(state: AgentState) -> AgentState:
        response = llm.synthesize(
            query=state["cleaned_query"],
            context_documents=state.get("final_context", []),
            similarity_score=state.get("similarity_score", 0.0),
            used_web_search=bool(state.get("web_documents")),
        )
        state["response"] = response
        _append_message(state, "assistant", response)
        _append_step(state, "response_generated")
        return state

    def report_node(state: AgentState) -> AgentState:
        state["report"] = write_report(
            query=state["cleaned_query"],
            response=state["response"],
            context_documents=state.get("final_context", []),
        )
        state.setdefault("tool_calls", []).append({"tool": "write_report"})
        _append_step(state, "report_generated")
        return state

    def route_after_generation(state: AgentState) -> str:
        return "report" if state.get("report_requested") else "output"

    def output_node(state: AgentState) -> AgentState:
        _append_step(state, "completed")
        return state

    def run_manually(initial_state: AgentState) -> AgentState:
        state = deepcopy(initial_state)
        for node in (input_node, retrieval_node, threshold_node):
            state = node(state)
        if route_after_threshold(state) == "web_search":
            for node in (query_expansion_node, web_search_node, ingestion_node):
                state = node(state)
        state = merge_node(state)
        state = rerank_node(state)
        state = generation_node(state)
        if route_after_generation(state) == "report":
            state = report_node(state)
        return output_node(state)

    if StateGraph is None:
        return _CompiledFallbackGraph(run_manually)

    workflow = StateGraph(AgentState)
    workflow.add_node("input_node", input_node)
    workflow.add_node("retrieval_node", retrieval_node)
    workflow.add_node("threshold_node", threshold_node)
    workflow.add_node("query_expansion_node", query_expansion_node)
    workflow.add_node("web_search_node", web_search_node)
    workflow.add_node("ingestion_node", ingestion_node)
    workflow.add_node("merge_node", merge_node)
    workflow.add_node("rerank_node", rerank_node)
    workflow.add_node("generation_node", generation_node)
    workflow.add_node("report_node", report_node)
    workflow.add_node("output_node", output_node)

    workflow.set_entry_point("input_node")
    workflow.add_edge("input_node", "retrieval_node")
    workflow.add_edge("retrieval_node", "threshold_node")
    workflow.add_conditional_edges(
        "threshold_node",
        route_after_threshold,
        {
            "use_existing_context": "merge_node",
            "web_search": "query_expansion_node",
        },
    )
    workflow.add_edge("query_expansion_node", "web_search_node")
    workflow.add_edge("web_search_node", "ingestion_node")
    workflow.add_edge("ingestion_node", "merge_node")
    workflow.add_edge("merge_node", "rerank_node")
    workflow.add_edge("rerank_node", "generation_node")
    workflow.add_conditional_edges(
        "generation_node",
        route_after_generation,
        {
            "report": "report_node",
            "output": "output_node",
        },
    )
    workflow.add_edge("report_node", "output_node")
    workflow.add_edge("output_node", END)

    return workflow.compile()


def run_agent(query: str, memory: dict[str, Any] | None = None) -> str:
    """Run the workflow and return the final user-facing response."""

    orchestrator = create_orchestrator()
    result = orchestrator.invoke(create_initial_state(query, memory))
    if result.get("report_requested") and result.get("report"):
        return result["report"]
    return result.get("response", "")
