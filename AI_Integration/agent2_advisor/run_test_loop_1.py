"""
Test runner for the Advisor Agent.
Loads simulated Tesla 2022 10-K data and runs the agent to generate suggestions.
"""

import importlib
import importlib.util
import os
import sys
from pathlib import Path

# Add project root to Python path so we can run this module directly
project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ai_integration.agent2_advisor.advisor import AdvisorAgent


def build_python_mock_file(report_text: str, source_name: str) -> str:
    return (
        '"""\n'
        "Mock inputs for testing the Critic Agent.\n\n"
        f"Auto-generated from advisor run: {source_name}.\n"
        '"""\n\n'
        "from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n\n"
        "MOCK_ADVISOR_REPORT = \"\"\"\n"
        f"{report_text}\n"
        "\"\"\"\n"
    )


def load_mock_data_module(index: int):
    source_path = Path(__file__).with_name("mock_data") / f"mock_data_{index}.py"
    module_name = f"advisor_mock_data_{index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load mock data module from {source_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    print("=== STARTING ADVISOR AGENT TEST LOOP ===")
    print(f"Project root added to path: {project_root}")
    print(f"Targeting model: gpt-4o-mini")

    # Check for OpenAI key
    from dotenv import load_dotenv

    ENV_PATH = Path(project_root) / "backend" / ".env"
    load_dotenv(dotenv_path=str(ENV_PATH))

    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY is missing! Please make sure it is defined in backend/.env")
        sys.exit(1)

    output_dir = Path(project_root) / "AI_Integration" / "agent3_critic" / "mock_data"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Initialize the Agent
        agent = AdvisorAgent(model="gpt-4o-mini")

        # Run the Agent for each mock data file
        for index in range(20, 21):
            mock_module = load_mock_data_module(index)

            user_query = mock_module.USER_QUERY
            mock_context_docs = mock_module.MOCK_CONTEXT_DOCS

            print(f"\n--- RUNNING MOCK DATA FILE: mock_data_{index}.py ---")
            print(f"User Query:\n{user_query}\n")
            print("Running agent (this will trigger tool calls for Framework templates and Risk Assessment)...")

            final_report = agent.run(user_query, mock_context_docs)

            output_file = output_dir / f"mock_data_{index}.py"
            output_file.write_text(
                build_python_mock_file(final_report, f"mock_data_{index}.py"),
                encoding="utf-8",
            )

            print(f"\n=== FINAL REPORT SAVED TO: ai_integration.agent3_critic.mock_data ===\n")

        print("\n=== TEST LOOP COMPLETED SUCCESSFULLY ===")

    except Exception as e:
        print(f"\n[ERROR] An error occurred while running the test loop: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()