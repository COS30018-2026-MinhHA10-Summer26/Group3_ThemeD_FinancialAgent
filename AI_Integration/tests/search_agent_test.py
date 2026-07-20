from ai_integration.agent5_searcher.searching_agent import SearchingAgent
from ai_integration.agent5_searcher import searching_agent as searching_agent_module
from ai_integration.tools.search_assess_tool import calculate_coverage


def test_calculate_coverage_with_no_documents():
    assert calculate_coverage("Tesla revenue in 2024?", []) == 0.0


def test_calculate_coverage_accepts_long_pdf_text_without_transformer_limits():
    long_document = "Tesla revenue strategic outlook " * 1_000

    coverage = calculate_coverage("Tesla strategic outlook", [long_document])

    assert 0.0 < coverage <= 1.0


def test_search_agent():
    search_agent = SearchingAgent()
    result = search_agent.run("Tesla revenue in 2024?", [])
    print(result)
    assert result


def test_search_agent_generates_a_query_for_a_missing_named_company(monkeypatch):
    agent = object.__new__(SearchingAgent)
    agent.coverage_threshold = 0.4
    agent.max_iterations = 1
    agent.top_k = 10
    agent._coverage = lambda _query, _documents: 1.0
    agent.identify_missing_information = lambda _query, _documents: "current improvements"
    agent.generate_search_queries = lambda _query, _documents, _missing: '{"search_queries": []}'

    captured_queries = []

    def fake_retrieve_documents(queries, _user_query):
        captured_queries.extend(queries)
        return [{"source": "Alphabet 10-K.pdf", "text": "Google and Alphabet reported improvements."}]

    agent.retrieve_documents = fake_retrieve_documents
    monkeypatch.setattr(
        searching_agent_module,
        "rerank_search_results",
        lambda query, raw_documents, top_k: raw_documents[:top_k],
    )

    result = agent.run(
        "Should I invest in Tesla or Google?",
        [{"source": "Tesla 10-K.pdf", "text": "Tesla reported improvements."}],
    )

    assert "Google annual report 10-K investor relations PDF" in captured_queries
    assert {doc["source"] for doc in result} == {"Tesla 10-K.pdf", "Alphabet 10-K.pdf"}

if __name__ == "__main__":
    test_search_agent()
