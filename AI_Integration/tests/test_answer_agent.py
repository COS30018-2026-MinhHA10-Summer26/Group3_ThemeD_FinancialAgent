from __future__ import annotations

from ai_integration.agent1_planner.answer_agent import AnswerAgent


def test_answer_agent_generates_a_grounded_response_with_sources(monkeypatch):
    captured: dict[str, str] = {}

    class FakeLLM:
        def generate_response(self, prompt: str) -> str:
            captured["prompt"] = prompt
            return "Tesla revenue increased based on the supplied filing. [Source 1]"

    agent = AnswerAgent()
    monkeypatch.setattr(agent, "_build_external_llm", lambda: FakeLLM())

    response = agent.run(
        "How did Tesla revenue change?",
        [{"text": "Tesla revenue was 100.", "source": "https://example.test/filing.pdf"}],
    )

    assert response.endswith("[Source 1]")
    assert "https://example.test/filing.pdf" in captured["prompt"]
    assert agent.last_error is None


def test_answer_agent_records_generation_failure_instead_of_dumping_context(monkeypatch):
    class BrokenLLM:
        def generate_response(self, _prompt: str) -> str:
            raise RuntimeError("provider unavailable")

    agent = AnswerAgent()
    monkeypatch.setattr(agent, "_build_external_llm", lambda: BrokenLLM())

    response = agent.run("Tesla revenue?", [{"text": "Revenue data", "source": "filing"}])

    assert "could not complete a grounded response" in response
    assert "Grounded context:" not in response
    assert agent.last_error == "answer_llm_generation_error:RuntimeError: provider unavailable"
