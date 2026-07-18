from __future__ import annotations

from ai_integration.models.external_llm import CONTEXT, ExternalLLM


def test_external_llm_sends_context_as_a_literal_system_message():
    captured: dict[str, object] = {}

    class FakeLLM:
        def invoke(self, messages):
            captured["messages"] = messages
            return type("Response", (), {"content": "OK"})()

    client = ExternalLLM.__new__(ExternalLLM)
    client.llm = FakeLLM()

    assert client.generate_response("Reply with OK") == "OK"
    messages = captured["messages"]
    assert messages[0].content == CONTEXT
    assert messages[1].content == "Reply with OK"
