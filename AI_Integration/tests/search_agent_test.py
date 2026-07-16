from ai_integration.agent5_searcher.searching_agent import SearchingAgent
from ai_integration.tools.search_assess_tool import calculate_coverage


def test_calculate_coverage_with_no_documents():
    assert calculate_coverage("Tesla revenue in 2024?", []) == 0.0


def test_search_agent():
    search_agent = SearchingAgent()
    result = search_agent.run("Tesla revenue in 2024?", [])
    print(result)
    assert result

if __name__ == "__main__":
    test_search_agent()