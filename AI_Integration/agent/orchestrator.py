"""
Deterministic orchestrator for the financial research agent.

The workflow follows the static agent design in `agent_readme.md`:
1. preprocess query
2. retrieve from local RAG
3. route on similarity threshold
4. expand query when confidence is low
5. search the web for augmentation
6. chunk searched documents
7. merge and rerank all context
8. generate a grounded response
9. optionally render a report
"""

from __future__ import annotations

from copy import deepcopy
import importlib
from pathlib import Path
import re
from typing import Any, Callable

try:
    from langgraph.graph import END, StateGraph
except ImportError:  # pragma: no cover - fallback when langgraph is unavailable
    END = "__END__"
    StateGraph = None

import yaml

from ai_integration.agent.state import AgentState, create_initial_state
from ai_integration.ingestion.chunking import chunk_documents
from ai_integration.tools.financial_tool import financial_tool
from ai_integration.tools.official_report_tool import official_report_tool
from ai_integration.tools.report_tool import write_report
from ai_integration.tools.web_search_tool import web_search_tool


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def _append_message(state: AgentState, role: str, content: str) -> None:
    state.setdefault("messages", []).append({"role": role, "content": content})


def _append_step(state: AgentState, step: str) -> None:
    state.setdefault("workflow_steps", []).append(step)


def _safe_get_llm():
    try:
        llm_module = importlib.import_module("ai_integration.models.llm")
        return llm_module.get_llm()
    except Exception:
        return None


def _load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        return {
            "top_k": 5,
            "chunk_size": 400,
            "chunk_overlap": 50,
            "retrieval": {"top_k": 5},
        }
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def _build_retriever(config: dict[str, Any]):
    try:
        retriever_module = importlib.import_module("ai_integration.rag.retriever")
        return retriever_module.Retriever(config)
    except Exception:
        return None


def _normalize_document(document: dict[str, Any]) -> dict[str, Any]:
    text = str(document.get("text") or document.get("content") or "").strip()
    return {
        "text": text,
        "content": text,
        "source": document.get("source", document.get("title", "unknown")),
        "page": document.get("page", 1),
        "chunk_id": document.get("chunk_id"),
        "section_title": document.get("section_title"),
        "section_type": document.get("section_type"),
        "score": float(document.get("score", 0.0) or 0.0),
    }


def _keyword_score(query: str, text: str) -> float:
    query_terms = set(re.findall(r"[a-zA-Z0-9]+", query.lower()))
    text_terms = set(re.findall(r"[a-zA-Z0-9]+", text.lower()))
    if not query_terms or not text_terms:
        return 0.0
    return len(query_terms & text_terms) / len(query_terms)


def _retrieve_from_memory(
    query: str,
    documents: list[dict[str, Any]],
    top_k: int,
) -> tuple[list[dict[str, Any]], float]:
    scored: list[dict[str, Any]] = []
    for document in documents:
        normalized = _normalize_document(document)
        normalized["score"] = _keyword_score(query, normalized["text"])
        scored.append(normalized)
    ranked = sorted(scored, key=lambda item: item.get("score", 0.0), reverse=True)
    top_documents = ranked[:top_k]
    similarity = float(top_documents[0]["score"]) if top_documents else 0.0
    return top_documents, similarity


def _rerank_documents(
    query: str,
    documents: list[dict[str, Any]],
    top_k: int,
) -> list[dict[str, Any]]:
    reranked: list[dict[str, Any]] = []
    for document in documents:
        normalized = _normalize_document(document)
        score = float(normalized.get("score", 0.0))
        rerank_bonus = _keyword_score(query, normalized["text"])
        normalized["rerank_score"] = score + rerank_bonus
        reranked.append(normalized)
    reranked.sort(key=lambda item: item.get("rerank_score", 0.0), reverse=True)
    return reranked[:top_k]


def _deduplicate_documents(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    unique: list[dict[str, Any]] = []
    for document in documents:
        normalized = _normalize_document(document)
        key = (str(normalized["source"]), normalized["text"])
        if key not in seen:
            seen.add(key)
            unique.append(normalized)
    return unique


def _needs_official_report_search(query: str) -> bool:
    query_lower = query.lower()
    keywords = (
        "annual report",
        "annual reports",
        "investor relations",
        "10-k",
        "official website",
        "financial statements",
    )
    return any(keyword in query_lower for keyword in keywords)


def _infer_company_name_from_query(query: str) -> str | None:
    cleaned = re.sub(
        r"\b(find|download|get|official|company|website|annual|report|reports|investor|relations|for|the|latest)\b",
        " ",
        query,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -,:")
    return cleaned or None


class _CompiledFallbackGraph:
    """Tiny fallback runner when LangGraph is unavailable."""

    def __init__(self, runner: Callable[[AgentState], AgentState]) -> None:
        self._runner = runner

    def invoke(self, state: AgentState) -> AgentState:
        return self._runner(deepcopy(state))


def create_orchestrator():
    """Create and return the deterministic financial workflow."""

    config = _load_config()
    llm = _safe_get_llm()
    retriever = _build_retriever(config)
    top_k = int(config.get("retrieval", {}).get("top_k", config.get("top_k", 5)))
    chunk_size = int(config.get("chunk_size", 400))
    chunk_overlap = int(config.get("chunk_overlap", 50))

    def input_node(state: AgentState) -> AgentState:
        state["cleaned_query"] = state["query"].strip()
        query_lower = state["cleaned_query"].lower()
        state["report_requested"] = any(
            keyword in query_lower for keyword in ("report", "pdf", "markdown", "docx")
        )
        state["top_k"] = int(state.get("top_k", top_k))
        _append_message(state, "user", state["cleaned_query"])
        _append_step(state, "input_processed")
        return state

    def retrieval_node(state: AgentState) -> AgentState:
        local_docs: list[dict[str, Any]] = []
        similarity_score = 0.0

        if retriever is not None:
            try:
                local_docs, _latency = retriever.retrieve(state["cleaned_query"])
                local_docs = [_normalize_document(document) for document in local_docs]
                if local_docs:
                    similarity_score = float(local_docs[0].get("score", 0.0))
            except Exception as exc:
                state.setdefault("errors", []).append(f"retriever_error: {exc}")

        if not local_docs:
            local_docs, similarity_score = _retrieve_from_memory(
                state["cleaned_query"],
                state.get("documents", []),
                state.get("top_k", top_k),
            )

        tool_result = financial_tool(
            state["cleaned_query"],
            retrieved_documents=local_docs,
            similarity_score=similarity_score,
        )

        state["retrieved_documents"] = local_docs
        state["similarity_score"] = similarity_score
        state.setdefault("tool_calls", []).append({"tool": "financial_tool"})
        state.setdefault("tool_results", []).append(tool_result)
        _append_step(state, "retrieval_completed")
        return state

    def threshold_node(state: AgentState) -> AgentState:
        threshold = float(state.get("retrieval_threshold", 0.8))
        state["route"] = (
            "use_existing_context"
            if state.get("similarity_score", 0.0) >= threshold
            else "report_search"
        )
        _append_step(state, f"threshold_checked:{state['route']}")
        return state

    def route_after_threshold(state: AgentState) -> str:        
        return state.get("route", "use_existing_context")

    def query_expansion_node(state: AgentState) -> AgentState:
        query = state["cleaned_query"]
        if llm is not None and hasattr(llm, "invoke"):
            try:
                generated = llm.invoke(
                    f"Generate 3 concise financial web search queries for: {query}"
                )
                lines = [line.strip("-• \t") for line in str(generated).splitlines()]
                expanded_queries = [line for line in lines if len(line) > 5][:3]
            except Exception:
                expanded_queries = []
        else:
            expanded_queries = []

        if not expanded_queries:
            expanded_queries = [
                query,
                f"{query} latest market news",
                f"{query} analyst sentiment",
            ]

        state["expanded_queries"] = expanded_queries
        _append_step(state, "query_expanded")
        return state

    def web_search_node(state: AgentState) -> AgentState:
        metadata = state.setdefault("metadata", {})
        official_result: dict[str, Any] | None = None

        if _needs_official_report_search(state["cleaned_query"]):
            official_result = official_report_tool(
                state["cleaned_query"],
                company_name=metadata.get("company_name") or _infer_company_name_from_query(state["cleaned_query"]),
                company_website=metadata.get("company_website"),
                years=metadata.get("target_years"),
                dry_run=bool(metadata.get("dry_run_downloads", False)),
                use_selenium=bool(metadata.get("use_selenium", False)),
            )
            state.setdefault("tool_calls", []).append({"tool": "official_report_tool"})
            state.setdefault("tool_results", []).append(
                {
                    "tool": "official_report_tool",
                    "downloaded_file_count": len(official_result.get("downloaded_files", [])),
                    "matched_link_count": len(official_result.get("matched_links", [])),
                    "dry_run": official_result.get("dry_run", False),
                }
            )

        result = web_search_tool(
            state["cleaned_query"],
            search_queries=state.get("expanded_queries", []),
            similarity_score=state.get("similarity_score", 0.0),
        )
        combined_documents = list(result.get("documents", []))
        if official_result:
            combined_documents = official_result.get("documents", []) + combined_documents

        state["web_documents"] = [
            _normalize_document(document) for document in combined_documents
        ]
        metadata["search_strategy"] = result.get("search_strategy", "")
        metadata["search_prompts"] = result.get("prompts", [])
        if official_result:
            metadata["official_report_strategy"] = official_result.get("search_strategy", "")
            metadata["downloaded_report_files"] = official_result.get("downloaded_files", [])
        state.setdefault("tool_calls", []).append({"tool": "web_search_tool"})
        state.setdefault("tool_results", []).append(
            {
                "tool": "web_search_tool",
                "prompt_count": result.get("total_prompts", 0),
                "document_count": len(state["web_documents"]),
            }
        )
        _append_step(state, "web_search_completed")
        return state
    
    def report_search_node(state: AgentState) -> AgentState:
        metadata = state.setdefault("metadata", {})
        combined_documents = []

        if _needs_official_report_search(state["cleaned_query"]):
            official_result = official_report_tool(
                state["cleaned_query"],
                company_name=metadata.get("company_name") or _infer_company_name_from_query(state["cleaned_query"]),
                company_website=metadata.get("company_website"),
                years=metadata.get("target_years"),
                dry_run=bool(metadata.get("dry_run_downloads", False)),
                use_selenium=bool(metadata.get("use_selenium", False)),
            )
            state.setdefault("tool_calls", []).append({"tool": "official_report_tool"})
            state.setdefault("tool_results", []).append(
                {
                    "tool": "official_report_tool",
                    "downloaded_file_count": len(official_result.get("downloaded_files", [])),
                    "matched_link_count": len(official_result.get("matched_links", [])),
                    "dry_run": official_result.get("dry_run", False),
                }
            )
            combined_documents = official_result.get("documents", [])
            metadata["official_report_strategy"] = official_result.get("search_strategy", "")
            metadata["downloaded_report_files"] = official_result.get("downloaded_files", [])

        state["web_documents"] = [
            _normalize_document(document) for document in combined_documents
        ]
        _append_step(state, "report_search_completed")
        return state

    def ingestion_node(state: AgentState) -> AgentState:
        documents = state.get("web_documents", [])
        state["web_documents"] = chunk_documents(documents, chunk_size, chunk_overlap)
        _append_step(state, "documents_chunked")
        return state

    def merge_node(state: AgentState) -> AgentState:
        merged = state.get("retrieved_documents", []) + state.get("web_documents", [])
        state["merged_documents"] = _deduplicate_documents(merged)
        _append_step(state, "context_merged")
        return state

    def rerank_node(state: AgentState) -> AgentState:
        reranked = _rerank_documents(
            state["cleaned_query"],
            state.get("merged_documents", []),
            state.get("top_k", top_k),
        )
        state["reranked_documents"] = reranked
        state["final_context"] = reranked[: state.get("top_k", top_k)]
        _append_step(state, "reranked")
        return state

    def generation_node(state: AgentState) -> AgentState:
        if llm is not None and hasattr(llm, "synthesize"):
            response = llm.synthesize(
                query=state["cleaned_query"],
                context_documents=state.get("final_context", []),
                similarity_score=state.get("similarity_score", 0.0),
                used_web_search=bool(state.get("web_documents")),
            )
        else:
            findings = [
                f"{index}. [{doc['source']}] {doc['text'][:280]}"
                for index, doc in enumerate(state.get("final_context", []), start=1)
            ]
            response_lines = [
                f"Query: {state['cleaned_query']}",
                f"Retrieval confidence: {state.get('similarity_score', 0.0):.2f}",
                "Grounded findings:",
            ]
            response_lines.extend(findings or ["No grounded findings were available."])
            response = "\n".join(response_lines)

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
            for node in (query_expansion_node, report_search_node, ingestion_node):
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
    workflow.add_node("report_search_node", report_search_node)
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
            "report_search": "query_expansion_node",
        },
    )
    workflow.add_edge("query_expansion_node", "report_search_node")
    workflow.add_edge("report_search_node", "ingestion_node")
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
    """Run the orchestrator and return the final user-facing output."""

    result = run_agent_state(query, memory)
    if result.get("report_requested") and result.get("report"):
        return result["report"]
    return result.get("response", "")


def run_agent_state(query: str, memory: dict[str, Any] | None = None) -> AgentState:
    """Run the orchestrator and return the full final workflow state."""

    orchestrator = create_orchestrator()
    return orchestrator.invoke(create_initial_state(query, memory))
