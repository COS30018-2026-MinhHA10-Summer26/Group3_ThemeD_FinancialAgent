from email.mime import text
import os
import requests
from ai_integration.ingestion.pdf_extractor import extract_documents
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")

DOWNLOAD_DIR = "data/raw/"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def report_search_tool(
    query: str,
    max_results: int = 1
) -> Dict[str, Any]:
    """
    Search and retrieve relevant documents based on the user query using SerpAPI.

    Returns a best-effort result dictionary even when the external search service
    fails or returns no usable content.
    """
    if not query or not str(query).strip():
        return {"query": query, "synthetic_results": [], "sources": []}

    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={
                "q": f"{query} filetype:pdf",
                "api_key": SERP_API_KEY,
                "num": max_results,
            },
            timeout=30,
        )
        response.raise_for_status()
        results = response.json()
    except Exception as exc:
        print(f"Search request failed for query {query!r}: {exc}")
        return {"query": query, "synthetic_results": [], "sources": []}

    synthetic_results = []
    sources = []
    for result in results.get("organic_results", []) or []:
        url = result.get("link")
        if not url:
            continue
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            pdf_path = os.path.join(DOWNLOAD_DIR, f"{result.get('title', 'document')}.pdf")
            with open(pdf_path, "wb") as f:
                f.write(response.content)
            docs = extract_documents(pdf_path)
            synthetic_results.extend(docs)
            sources.append({"title": result.get("title"), "url": url})
        except Exception as exc:
            print(f"Failed to download {url}: {exc}")

    return {"query": query, "synthetic_results": synthetic_results, "sources": sources}