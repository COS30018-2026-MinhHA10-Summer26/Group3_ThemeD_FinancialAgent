"""
Test runner for the Evaluator Agent.
Loads advisor v1, critic feedback, and advisor v2 mock data, then runs the
full evaluator pipeline in Mode B.
"""

# pyright: reportMissingImports=false

import importlib.util
import os
import sys
from pathlib import Path


project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from ai_integration.agent4_evaluator.evaluator import EvaluatorAgent


def build_python_mock_file(source_report_v1: str, source_report_v2: str, evaluation_report: str, source_name: str) -> str:
    return (
        '"""\n'
        "Mock inputs for testing the Evaluator Agent.\n\n"
        f"Auto-generated from evaluator run: {source_name}.\n"
        '"""\n\n'
        "from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n\n"
        "MOCK_ADVISOR_REPORT_V1 = \"\"\"\n"
        f"{source_report_v1}\n"
        "\"\"\"\n\n"
        "MOCK_ADVISOR_REPORT_V2 = \"\"\"\n"
        f"{source_report_v2}\n"
        "\"\"\"\n\n"
        "MOCK_EVALUATION_REPORT = \"\"\"\n"
        f"{evaluation_report}\n"
        "\"\"\"\n"
    )


def load_mock_data_module(base_dir: str, index: int):
    source_path = Path(__file__).parent.parent / "agent2_advisor" / base_dir / f"mock_data_{index}.py"
    module_name = f"evaluator_mock_data_{base_dir}_{index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load mock data module from {source_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_mode_b(agent) -> None:
    print("\n" + "=" * 60)
    print("MODE B — Full Pipeline Evaluation Loop")
    print("=" * 60)

    after_critic_dir = "mock_data_after_critic"
    revision_dir = "mock_data_revision"
    output_dir = Path(project_root) / "evaluation" / "agent4_evaluator" / "mock_data"
    output_dir.mkdir(parents=True, exist_ok=True)

    for index in range(16, 21):
        after_critic_module = load_mock_data_module(after_critic_dir, index)
        revision_module = load_mock_data_module(revision_dir, index)

        user_query = after_critic_module.USER_QUERY
        mock_context_docs = after_critic_module.MOCK_CONTEXT_DOCS
        current_report = after_critic_module.MOCK_ADVISOR_REPORT_V1
        critic_feedback = after_critic_module.MOCK_CRITIC_FEEDBACK["revision_instructions"]
        revised_report = revision_module.MOCK_ADVISOR_REPORT_V2

        print(f"\n--- RUNNING MOCK DATA FILE: mock_data_{index}.py ---")
        print(f"User Query:\n{user_query}\n")
        print("Running evaluator (this will compare advisor report v1 and v2)...")

        evaluation_report = agent.run(
            query=user_query,
            context_docs=mock_context_docs,
            response=current_report,
            critic_issues=critic_feedback,
            advisor_report_v2=revised_report,
        )

        output_file = output_dir / f"mock_data_{index}.py"
        output_file.write_text(
            build_python_mock_file(current_report, revised_report, evaluation_report, f"mock_data_{index}.py"),
            encoding="utf-8",
        )

        print(f"\n=== FINAL REPORT SAVED TO: evaluation.agent4_evaluator.mock_data ===\n")


def main() -> None:
    print("=== STARTING EVALUATOR AGENT TEST LOOP ===")
    print(f"Project root added to path: {project_root}")
    print("Targeting model: gpt-4o-mini")

    from dotenv import load_dotenv

    env_path = Path(project_root) / "backend" / ".env"
    load_dotenv(dotenv_path=str(env_path))

    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY is missing! Please make sure it is defined in backend/.env")
        sys.exit(1)

    agent = EvaluatorAgent(model="gpt-4o-mini")
    run_mode_b(agent)

    print("\n=== TEST LOOP COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()