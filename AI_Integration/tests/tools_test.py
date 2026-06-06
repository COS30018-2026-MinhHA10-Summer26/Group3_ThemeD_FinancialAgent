"""
Simple smoke test runner for agent tools.

Run with:
`python3 ai_integration/tests/tools_test.py`
"""

from __future__ import annotations

from pprint import pprint
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai_integration.tools.financial_tool import financial_tool
from ai_integration.tools.official_report_tool import official_report_tool
from ai_integration.tools.report_tool import write_report
from ai_integration.tools.web_search_tool import web_search_tool


SAMPLE_QUERY = "Analyze TSLA stock performance and market sentiment this week"
SAMPLE_CONTEXT = [
    {
        "text": "Tesla stock rose this week after delivery updates and improved analyst sentiment.",
        "content": "Tesla stock rose this week after delivery updates and improved analyst sentiment.",
        "source": "sample:tsla",
        "page": 1,
        "score": 0.81,
    },
    {
        "text": "EV market competition remained intense, but sentiment around Tesla improved.",
        "content": "EV market competition remained intense, but sentiment around Tesla improved.",
        "source": "sample:market",
        "page": 1,
        "score": 0.72,
    },
]


def run_tools_test() -> None:
    print("== financial_tool ==")
    financial_result = financial_tool(
        SAMPLE_QUERY,
        retrieved_documents=SAMPLE_CONTEXT,
        similarity_score=0.81,
    )
    pprint(financial_result)

    print("\n== web_search_tool ==")
    web_result = web_search_tool(
        SAMPLE_QUERY,
        search_queries=[
            SAMPLE_QUERY,
            "TSLA latest market news",
            "Tesla analyst sentiment this week",
        ],
        similarity_score=0.18,
        max_results_per_query=1,
    )
    print(
        {
            "total_prompts": web_result.get("total_prompts"),
            "search_strategy": web_result.get("search_strategy"),
            "document_count": len(web_result.get("documents", [])),
        }
    )
    if web_result.get("prompts"):
        pprint(web_result["prompts"][0])
    if web_result.get("documents"):
        pprint(web_result["documents"][0])

    print("\n== official_report_tool ==")
    official_result = official_report_tool(
        "Download NVIDIA annual reports from the official company website for 2024",
        dry_run=True,
    )
    print(
        {
            "total_prompts": official_result.get("total_prompts"),
            "downloaded_file_count": len(official_result.get("downloaded_files", [])),
            "dry_run": official_result.get("dry_run"),
            "error": official_result.get("error"),
            "search_queries": official_result.get("search_queries", []),
        }
    )
    if official_result.get("documents"):
        pprint(official_result["documents"][0])

    print("\n== write_report ==")
    report = write_report(
        query=SAMPLE_QUERY,
        response="Tesla sentiment improved on stronger deliveries and supportive analyst commentary.",
        context_documents=SAMPLE_CONTEXT,
    )
    print(report[:800])


if __name__ == "__main__":
    run_tools_test()
