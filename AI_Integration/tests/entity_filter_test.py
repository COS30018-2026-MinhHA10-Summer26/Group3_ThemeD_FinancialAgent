from ai_integration.agent1_planner.retrieval_agent import RetrievalAgent
from ai_integration.entity_filter import filter_documents_for_query_entity


def test_filter_documents_for_query_entity_keeps_requested_company_only():
    docs = [
        {"source": "Walt Disney Annual Report.pdf", "text": "The Walt Disney Company revenue increased."},
        {"source": "Unilever Annual Report.pdf", "text": "Unilever brands and operating profit."},
        {"source": "Tesla 2024 Form 10-K.pdf", "text": "Tesla, Inc. automotive revenue and energy generation."},
    ]

    filtered = filter_documents_for_query_entity("Should I buy Tesla stock?", docs)

    assert [doc["source"] for doc in filtered] == ["Tesla 2024 Form 10-K.pdf"]


def test_retrieval_agent_does_not_count_wrong_company_docs_as_coverage(tmp_path):
    docs = [
        {"source": "Walt Disney Annual Report.pdf", "text": "annual report stock strategic outlook revenue"},
        {"source": "Unilever Annual Report.pdf", "text": "annual report stock strategic outlook revenue"},
    ]
    agent = RetrievalAgent({"top_k": 5}, tmp_path)

    result = agent.run("Should I buy Tesla stock and what is the strategic outlook?", {"documents": docs})

    assert result["context_docs"] == []
    assert result["coverage_score"] == 0.0


def test_retrieval_agent_keeps_apple_docs_for_apple_query(tmp_path):
    docs = [
        {"source": "Unilever Annual Report.pdf", "text": "annual report revenue stock"},
        {"source": "2024 Form 10-K - Apple Inc..pdf", "text": "Apple Inc. net sales services iPhone outlook"},
    ]
    agent = RetrievalAgent({"top_k": 5}, tmp_path)

    result = agent.run("Apple stock outlook", {"documents": docs})

    assert len(result["context_docs"]) == 1
    assert result["context_docs"][0]["source"] == "2024 Form 10-K - Apple Inc..pdf"
    assert result["coverage_score"] > 0.0
