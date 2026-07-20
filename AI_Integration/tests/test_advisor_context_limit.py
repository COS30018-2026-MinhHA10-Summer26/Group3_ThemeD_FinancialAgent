from ai_integration.agent2_advisor.advisor import AdvisorAgent


def test_advisor_limits_llm_context_to_two_deduplicated_chunks():
    agent = object.__new__(AdvisorAgent)
    agent.max_context_documents = 2
    docs = [
        {"source": "one.pdf", "text": "first"},
        {"source": "two.pdf", "text": "second"},
        {"source": "three.pdf", "text": "third"},
        {"source": "one.pdf", "text": "first"},
    ]

    limited = agent._limit_context_documents(docs)

    assert [doc["source"] for doc in limited] == ["one.pdf", "two.pdf"]
