"""
Test runner for the Advisor Agent's Revision Process.
Loads mock advisor v1 report, mock critic feedback, and runs the revision logic to output V2.
"""

# pyright: reportMissingImports=false

import os
import sys
import importlib.util
from pathlib import Path

# Add project root to Python path so we can run this module directly
project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ai_integration.agent2_advisor.advisor import AdvisorAgent


def build_python_mock_file(source_report: str, source_name: str) -> str:
    return (
        '"""\n'
        "Mock inputs for testing the Advisor Agent revision process.\n\n"
        f"Auto-generated from advisor revision run: {source_name}.\n"
        '"""\n\n'
        "from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n\n"
        "MOCK_ADVISOR_REPORT_V2 = \"\"\"\n"
        f"{source_report}\n"
        "\"\"\"\n"
    )


def load_mock_data_module(index: int):
    source_path = Path(__file__).with_name("mock_data_after_critic") / f"mock_data_{index}.py"
    module_name = f"advisor_revision_mock_data_{index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load mock data module from {source_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    print("=== STARTING ADVISOR REVISION TEST LOOP ===")
    print(f"Project root added to path: {project_root}")
    print(f"Targeting model: gpt-4o-mini")

    # Check for OpenAI key
    from dotenv import load_dotenv

    ENV_PATH = Path(project_root) / "backend" / ".env"
    load_dotenv(dotenv_path=str(ENV_PATH))

    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY is missing! Please make sure it is defined in backend/.env")
        sys.exit(1)

    output_dir = Path(project_root) / "evaluation" / "agent2_advisor" / "mock_data_revision"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Initialize the Agent
        agent = AdvisorAgent(model="gpt-4o-mini")

        # Run the Agent for each mock data file
        for index in range(16, 21):
            mock_module = load_mock_data_module(index)

            user_query = mock_module.USER_QUERY
            mock_context_docs = mock_module.MOCK_CONTEXT_DOCS
            current_report = mock_module.MOCK_ADVISOR_REPORT_V1
            self_check = mock_module.MOCK_CRITIC_FEEDBACK

            print(f"\n--- RUNNING MOCK DATA FILE: mock_data_{index}.py ---")
            print(f"User Query:\n{user_query}\n")
            print("Running revision (this will trigger tool calls to address critic issues)...")

            context_str = agent._build_context_string(mock_context_docs)
            final_report = agent._revise_report(
                query=user_query,
                context_str=context_str,
                current_report=current_report,
                self_check=self_check,
            )

            output_file = output_dir / f"mock_data_{index}.py"
            output_file.write_text(
                build_python_mock_file(final_report, f"mock_data_{index}.py"),
                encoding="utf-8",
            )

            print(f"\n=== FINAL REPORT SAVED TO: evaluation.agent2_advisor.mock_data_revision ===\n")

        print("\n=== TEST LOOP COMPLETED SUCCESSFULLY ===")

    except Exception as e:
        print(f"\n[ERROR] An error occurred while running the test loop: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()