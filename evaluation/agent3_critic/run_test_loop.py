"""
Test runner for the Critic Agent.
Loads simulated Tesla 10-K mock data and runs the agent to generate critiques.
"""

# pyright: reportMissingImports=false

import json
import importlib.util
import os
import sys
from pathlib import Path


project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
	sys.path.insert(0, project_root)

from ai_integration.agent3_critic.critic import CriticAgent
from ai_integration.agent3_critic.tools import (
	critique_quality_tool,
	evidence_consistency_tool,
	report_coverage_tool,
	risk_gap_tool,
)


def build_python_mock_file(source_report: str, critique_markdown: str, source_name: str) -> str:
	return (
		'"""\n'
		"Mock inputs for testing the Critic Agent.\n\n"
		f"Auto-generated from critic run: {source_name}.\n"
		'"""\n\n'
		"from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n"
		"\n"
		"MOCK_ADVISOR_REPORT_V1 = \"\"\"\n"
		f"{source_report}\n"
		"\"\"\"\n\n"
		"MOCK_CRITIC_FEEDBACK = {\n"
		"    \"passes\": False,\n"
		"    \"issues\": [\n"
		"        \"See revision_instructions for the full critique output.\"\n"
		"    ],\n"
		"    \"revision_instructions\": "
		f"{json.dumps(critique_markdown, ensure_ascii=False)}"
		"\n"
		"}\n"
	)


def load_mock_data_module(index: int):
	source_path = Path(__file__).with_name("mock_data") / f"mock_data_{index}.py"
	module_name = f"critic_mock_data_{index}"
	spec = importlib.util.spec_from_file_location(module_name, source_path)
	if spec is None or spec.loader is None:
		raise ImportError(f"Unable to load mock data module from {source_path}")

	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


def get_source_report(module) -> str:
	if hasattr(module, "MOCK_ADVISOR_REPORT"):
		return module.MOCK_ADVISOR_REPORT
	if hasattr(module, "MOCK_CRITIC_REPORT"):
		return module.MOCK_CRITIC_REPORT
	raise AttributeError("Mock data module must define MOCK_ADVISOR_REPORT or MOCK_CRITIC_REPORT")


def run_offline_tool_checks(user_query: str, advisor_report: str, context_docs) -> None:
	print("=== OFFLINE CRITIC TOOL CHECKS ===")
	print("\n[Coverage]")
	print(report_coverage_tool(user_query, advisor_report))
	print("\n[Evidence]")
	print(evidence_consistency_tool(advisor_report, context_docs))
	print("\n[Risk Gaps]")
	print(risk_gap_tool(advisor_report, context_docs))
	print("\n[Quality Self-Check Sample]")
	print(critique_quality_tool("## Overall Verdict\nInvestor concern: unsupported claim."))


def main() -> None:
	print("=== STARTING CRITIC AGENT TEST LOOP ===")
	print(f"Project root added to path: {project_root}")
	print("Targeting model: gpt-4o-mini")

	from dotenv import load_dotenv

	env_path = Path(project_root) / "backend" / ".env"
	load_dotenv(dotenv_path=str(env_path))

	if not os.getenv("OPENAI_API_KEY"):
		print("\n[SKIP] OPENAI_API_KEY is missing. Offline tool checks completed.")
		return

	output_dir = Path(project_root) / "AI_Integration" / "agent2_advisor" / "mock_data_after_critic"
	output_dir.mkdir(parents=True, exist_ok=True)

	agent = CriticAgent(model="gpt-4o-mini")

	for index in range(16, 21):
		mock_module = load_mock_data_module(index)

		user_query = mock_module.USER_QUERY
		mock_context_docs = mock_module.MOCK_CONTEXT_DOCS
		source_report = get_source_report(mock_module)

		print(f"\n--- RUNNING MOCK DATA FILE: mock_data_{index}.py ---")
		print(f"User Query:\n{user_query}\n")
		run_offline_tool_checks(user_query, source_report, mock_context_docs)
		print("\nRunning agent (this will trigger tool calls to critique the report)...")

		final_critique = agent.run(user_query, mock_context_docs, source_report)

		output_file = output_dir / f"mock_data_{index}.py"
		output_file.write_text(
			build_python_mock_file(source_report, final_critique, f"mock_data_{index}.py"),
			encoding="utf-8",
		)

		print(f"\n=== FINAL REPORT SAVED TO: ai_integration.agent2_advisor.mock_data_after_critic ===\n")

	print("\n=== TEST LOOP COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
	main()
