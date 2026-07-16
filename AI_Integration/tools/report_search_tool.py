import os
import re
import requests
from ai_integration.ingestion.pdf_extractor import extract_documents
from ai_integration.entity_filter import filter_documents_for_query_entity
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")

DOWNLOAD_DIR = "data/raw/"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def _safe_pdf_name(title: str | None, index: int) -> str:
    safe_title = re.sub(r"[^a-zA-Z0-9._ -]+", "", title or f"document-{index}")
    safe_title = re.sub(r"\s+", " ", safe_title).strip()[:120]
    return f"{safe_title or f'document-{index}'}.pdf"


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
    for index, result in enumerate(results.get("organic_results", []) or [], start=1):
        url = result.get("link")
        if not url:
            continue
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")
            if "pdf" not in content_type.lower() and not url.lower().split("?")[0].endswith(".pdf"):
                continue
            pdf_path = os.path.join(DOWNLOAD_DIR, _safe_pdf_name(result.get("title"), index))
            with open(pdf_path, "wb") as f:
                f.write(response.content)
            docs = extract_documents(pdf_path)
            filtered_docs = filter_documents_for_query_entity(query, docs)
            synthetic_results.extend(filtered_docs)
            sources.append({"title": result.get("title"), "url": url})
        except Exception as exc:
            print(f"Failed to download {url}: {exc}")

    return {"query": query, "synthetic_results": synthetic_results, "sources": sources}
