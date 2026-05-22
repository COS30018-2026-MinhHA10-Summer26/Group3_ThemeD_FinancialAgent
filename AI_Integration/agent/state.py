"""
Agent State Management

Defines the state structure for the LangGraph workflow.
"""

from typing import Annotated
from collections.abc import Sequence
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State object for the agent workflow."""

    # User input
    query: str

    # Conversation history
    messages: Annotated[Sequence[Any], add_messages]

    # Tool calls and results
    tool_calls: list[dict[str, Any]]
    tool_results: list[dict[str, Any]]

    # Planning and decision making
    plan: str
    next_action: str

    # Final outputs
    response: str
    report: str | None
