"""
Test runner for the Evaluator Agent.
Runs offline tool checks first, then (if OPENAI_API_KEY is set) runs the
full EvaluatorAgent in both Mode A (RAG-only) and Mode B (full pipeline).
"""

import json
import os
import sys
from pathlib import Path


project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ai_integration.agent4_evaluator.mock_data import (
    MOCK_ADVISOR_REPORT_V2,
    MOCK_CONTEXT_DOCS,
    MOCK_CRITIC_REPORT,
    MOCK_RAG_RESPONSE,
    USER_QUERY,
)
from ai_integration.agent4_evaluator.tools import (
    evaluation_quality_tool,
    issues_resolution_tool,
    query_relevance_tool,
    response_completeness_tool,
)


def run_offline_tool_checks() -> None:
    print("=" * 60)
    print("OFFLINE EVALUATOR TOOL CHECKS")
    print("=" * 60)

    print("\n[1] Query Relevance — RAG Response")
    result = query_relevance_tool(USER_QUERY, MOCK_RAG_RESPONSE)
    print(json.dumps(result, indent=2))

    print("\n[2] Query Relevance — Advisor Report v2")
    result = query_relevance_tool(USER_QUERY, MOCK_ADVISOR_REPORT_V2)
    print(json.dumps(result, indent=2))

    print("\n[3] Issues Resolution — Critic vs Advisor v2")
    result = issues_resolution_tool(MOCK_CRITIC_REPORT, MOCK_ADVISOR_REPORT_V2)
    print(json.dumps(result, indent=2))

    print("\n[4] Response Completeness — RAG Response")
    result = response_completeness_tool(MOCK_RAG_RESPONSE)
    print(json.dumps(result, indent=2))

    print("\n[5] Response Completeness — Advisor Report v2")
    result = response_completeness_tool(MOCK_ADVISOR_REPORT_V2)
    print(json.dumps(result, indent=2))

    print("\n[6] Evaluation Quality Self-Check (sample)")
    sample = "## Evaluation Verdict\nThe response is incomplete.\n## Remaining Gaps\nMissing chart."
    result = evaluation_quality_tool(sample)
    print(json.dumps(result, indent=2))


def run_mode_a(agent) -> None:
    print("\n" + "=" * 60)
    print("MODE A — RAG-only Evaluation")
    print("=" * 60)

    try:
        evaluation = agent.run(
            query=USER_QUERY,
            context_docs=MOCK_CONTEXT_DOCS,
            response=MOCK_RAG_RESPONSE,
        )
        print("\n--- EVALUATOR OUTPUT (Mode A) ---\n")
        print(evaluation)
    except Exception as exc:
        print(f"\n[SKIP] Mode A failed: {exc}")


def run_mode_b(agent) -> None:
    print("\n" + "=" * 60)
    print("MODE B — Full Pipeline Evaluation")
    print("=" * 60)

    from ai_integration.agent3_critic.mock_data import MOCK_ADVISOR_REPORT

    try:
        evaluation = agent.run(
            query=USER_QUERY,
            context_docs=MOCK_CONTEXT_DOCS,
            response=MOCK_ADVISOR_REPORT,
            critic_issues=MOCK_CRITIC_REPORT,
            advisor_report_v2=MOCK_ADVISOR_REPORT_V2,
        )
        print("\n--- EVALUATOR OUTPUT (Mode B) ---\n")
        print(evaluation)
    except Exception as exc:
        print(f"\n[SKIP] Mode B failed: {exc}")


def main() -> None:
    print("=== STARTING EVALUATOR AGENT TEST ===")
    print(f"Project root added to path: {project_root}")
    print(f"User Query:\n{USER_QUERY}\n")

    run_offline_tool_checks()

    from dotenv import load_dotenv

    env_path = Path(project_root) / "backend" / ".env"
    load_dotenv(dotenv_path=str(env_path))

    if not os.getenv("OPENAI_API_KEY"):
        print("\n[SKIP] OPENAI_API_KEY is missing. Offline tool checks completed.")
        return

    from ai_integration.agent4_evaluator.evaluator import EvaluatorAgent

    agent = EvaluatorAgent(model="gpt-4o-mini")

    run_mode_a(agent)
    run_mode_b(agent)

    print("\n=== TEST COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()
