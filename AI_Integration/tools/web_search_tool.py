"""
Search tool abstraction for the financial research workflow.
"""

from __future__ import annotations

from typing import Any
from googlesearch import search
from bs4 import BeautifulSoup
import requests

from ai_integration.rag.chunking import chunk_documents
from ai_integration.rag.retriever import retrieve_documents
from ai_integration.models.llm import get_llm

searching_prompt = "Given the following query, generate a list of relevant search queries that could be used to find information about it. The queries should be concise and focused on different aspects of the main query. " \
"The output format should an array of strings, without any additional text or formatting."

def web_search_tool(queries) -> list[dict[str, Any]]:
    if not queries:
        return []

    llm = get_llm()
    if not llm:
        return []

    queries = llm.expand_query(queries)

    results: list[dict[str, Any]] = []
    for index, query in enumerate(queries, start=1):
        results.append(
            {
                "source": f"web_search:{index}",
                "title": f"Search result for {query}",
                "content": (
                    f""
                ),
                "query": query,
                "origin": "web_search",
            }
        )
    return results
