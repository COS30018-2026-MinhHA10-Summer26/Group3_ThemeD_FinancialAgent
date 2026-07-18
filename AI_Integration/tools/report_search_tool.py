import os
import re
import tempfile
from io import BytesIO
from pathlib import Path
import requests
from pypdf import PdfReader
from ai_integration.ingestion.pdf_extractor import extract_documents
from ai_integration.entity_filter import filter_documents_for_query_entity
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY") or os.getenv("API_KEY") or os.getenv("SERPAPI_API_KEY")

def _safe_pdf_name(title: str | None, index: int) -> str:
    safe_title = re.sub(r"[^a-zA-Z0-9._ -]+", "", title or f"document-{index}")
    safe_title = re.sub(r"\s+", " ", safe_title).strip()[:120]
    return f"{safe_title or f'document-{index}'}.pdf"


def _is_parseable_pdf(content: bytes) -> bool:
    """Reject obvious corrupt/HTML downloads before passing them to MuPDF."""
    try:
        reader = PdfReader(BytesIO(content), strict=False)
        return len(reader.pages) > 0
    except Exception:
        return False


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
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
            }
            response = requests.get(url, headers=headers, timeout=60)
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")
            if "pdf" not in content_type.lower() and not url.lower().split("?")[0].endswith(".pdf"):
                continue
            if not response.content.startswith(b"%PDF-"):
                continue
            if not _is_parseable_pdf(response.content):
                print(f"Search result skipped (unreadable PDF): {url}")
                continue
            # Search results are request-scoped.  The PDF is needed only while
            # extracting text, so never store it in data/raw (the persistent
            # corpus used by the CLI/indexing workflow).
            with tempfile.TemporaryDirectory(prefix="financial-agent-search-") as temp_dir:
                pdf_path = Path(temp_dir) / _safe_pdf_name(result.get("title"), index)
                pdf_path.write_bytes(response.content)
                # Tables are intentionally skipped for web-search PDFs: the
                # warning about optional pymupdf_layout is irrelevant to chat,
                # while text is sufficient for grounded retrieval.
                docs = extract_documents(str(pdf_path), extract_tables=False)

            # The temporary file no longer exists here. Preserve the original
            # source URL/title for citations instead of exposing its temp path.
            filtered_docs = filter_documents_for_query_entity(query, docs)
            for document in filtered_docs:
                enriched_document = dict(document)
                enriched_document["source"] = url
                enriched_document["source_title"] = result.get("title") or url
                synthetic_results.append(enriched_document)
            if filtered_docs:
                sources.append({"title": result.get("title"), "url": url})
        except Exception as exc:
            # A 403 often means the issuer's investor-relations CDN blocks
            # automated downloads. It should skip that result, not abort chat.
            print(f"Search result skipped ({type(exc).__name__}): {url}: {exc}")

    return {"query": query, "synthetic_results": synthetic_results, "sources": sources}
