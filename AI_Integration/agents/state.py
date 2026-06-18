"""
Agent state definitions for the deterministic financial research workflow.
"""

from __future__ import annotations

from typing import Annotated, Any

try:
    from langgraph.graph.message import add_messages
except ImportError:  # pragma: no cover - fallback when langgraph is unavailable
    def add_messages(left: list[MessageLike], right: list[MessageLike]) -> list[MessageLike]:
        return [*left, *right]
from typing_extensions import TypedDict


MessageLike = dict[str, str] | tuple[str, str]
DocumentLike = dict[str, Any]


class AgentState(TypedDict, total=False):
    """State object shared across LangGraph workflow nodes."""

    # User input
    query: str
    cleaned_query: str
    report_requested: bool

    # Conversation history
    messages: Annotated[list[MessageLike], add_messages]

    # Retrieval inputs
    documents: list[DocumentLike]

    # Retrieval outputs
    retrieved_documents: list[DocumentLike]
    web_documents: list[DocumentLike]
    merged_documents: list[DocumentLike]
    reranked_documents: list[DocumentLike]
    final_context: list[DocumentLike]

    # Search and routing
    retrieval_threshold: float
    top_k: int
    similarity_score: float
    route: str
    expanded_queries: list[str]

    # Tooling and execution traces
    tool_calls: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]
    workflow_steps: list[str]
    metadata: dict[str, Any]
    errors: list[str]

    # Final outputs
    response: str
    report: str | None


def create_initial_state(query: str, memory: dict[str, Any] | None = None) -> AgentState:
    """Create a fully populated initial state with sensible defaults."""

    memory = memory or {}

    return AgentState(
        query=query,
        cleaned_query=query.strip(),
        report_requested=False,
        messages=list(memory.get("messages", [])),
        documents=list(memory.get("documents", [])),
        retrieved_documents=[],
        web_documents=[],
        merged_documents=[],
        reranked_documents=[],
        final_context=[],
        retrieval_threshold=float(memory.get("retrieval_threshold", 0.25)),
        top_k=int(memory.get("top_k", 5)),
        similarity_score=0.0,
        route="retrieve",
        expanded_queries=[],
        tool_calls=[],
        tool_results=[],
        workflow_steps=[],
        metadata=dict(memory.get("metadata", {})),
        errors=[],
        response="",
        report=None,
    )
