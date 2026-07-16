"""Planning/orchestration agent package."""

__all__ = ["PlanningOrchestrator", "run_agent", "run_agent_state"]


def __getattr__(name):
    if name in __all__:
        from ai_integration.agent1_planner.orchestrator import (
            PlanningOrchestrator,
            run_agent,
            run_agent_state,
        )

        return {
            "PlanningOrchestrator": PlanningOrchestrator,
            "run_agent": run_agent,
            "run_agent_state": run_agent_state,
        }[name]
    raise AttributeError(name)
