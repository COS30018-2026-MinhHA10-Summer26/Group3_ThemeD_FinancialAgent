"""
Agent Orchestrator

Implements LangGraph workflow for financial agent orchestration.
"""

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from backend.agent.state import AgentState
from backend.models.llm import get_llm
from backend.tools.financial_tool import financial_tool
from backend.tools.web_search_tool import web_search_tool
from backend.tools.report_writer import write_report


def create_orchestrator():
    """Create and return the agent orchestrator graph."""

    workflow = StateGraph(AgentState)

    # Initialize LLM
    llm = get_llm()

    # Define tools
    tools = [financial_tool, web_search_tool, write_report]
    tool_node = ToolNode(tools)

    # --- Node Definitions ---

    def planner_node(state: AgentState) -> dict:
        """Plan the approach for the user query."""
        # Add query to messages
        state["messages"].append(("user", state["query"]))

        # Get plan from LLM
        response = llm.invoke(state["messages"])
        state["plan"] = response.content
        state["next_action"] = "execute_tools"

        return state

    def tool_executor_node(state: AgentState) -> dict:
        """Execute selected tools."""
        # Call tool_node
        result = tool_node.invoke(state)

        return result

    def reasoner_node(state: AgentState) -> dict:
        """Reason over tool results and generate response."""
        state["messages"].append(("assistant", state["plan"]))

        # Generate final response from LLM
        response = llm.invoke(state["messages"])
        state["response"] = response.content

        return state

    # --- Add Nodes ---
    workflow.add_node("planner", planner_node)
    workflow.add_node("tools", tool_executor_node)
    workflow.add_node("reasoner", reasoner_node)

    # --- Add Edges ---
    workflow.add_edge("planner", "tools")
    workflow.add_edge("tools", "reasoner")
    workflow.add_edge("reasoner", END)

    # Set entry point
    workflow.set_entry_point("planner")

    return workflow.compile()


def run_agent(query: str, memory: dict | None = None) -> str:
    """Run the agent with a user query."""

    orchestrator = create_orchestrator()

    initial_state: AgentState = {
        "query": query,
        "messages": memory.get("messages", []) if memory else [],
        "tool_calls": [],
        "tool_results": [],
        "plan": "",
        "next_action": "",
        "response": "",
        "report": None,
    }

    result = orchestrator.invoke(initial_state)

    return result["response"]
