from pathlib import Path
import sys
import io
from contextlib import redirect_stdout

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import ai_integration.cli as cli


def test_cli_reports_called_agents():
    def stub_run_agent_state(query, memory=None):
        return {
            "route": "qa",
            "classification_reason": "stub",
            "executed_agents": ["RetrievalAgent", "SearchAgent", "AnswerAgent"],
            "workflow_steps": ["input_processed", "planned_workflow", "agent_started:RetrievalAgent"],
            "tool_calls": [{"tool": "RetrievalAgent"}, {"tool": "SearchAgent"}, {"tool": "AnswerAgent"}],
            "errors": [],
            "metadata": {},
            "final_output": "stub cli output",
        }

    cli.run_agent_state = stub_run_agent_state
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        exit_code = cli.main(
            [
                "--query",
                "What was Tesla revenue in 2024?",
                "--show-state",
            ]
        )
    output = buffer.getvalue()
    assert "executed_agents:" in output
    assert "RetrievalAgent" in output
    assert "AnswerAgent" in output
    assert exit_code == 0


if __name__ == "__main__":
    test_cli_reports_called_agents()
