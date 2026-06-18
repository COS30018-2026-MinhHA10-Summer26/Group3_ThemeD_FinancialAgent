import os
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

SERP_API_KEY = os.getenv("API_KEY")

DOWNLOAD_DIR = "data/raw/"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
def report_search_tool(
    query: str,
    max_results: int = 3
) -> Dict[str, Any]:
    """
    Search and retrieve relevant documents based on the user query using SerpAPI.

    Parameters
    ----------
    query : str
        Example:
            "NVIDIA annual report 2024"

    Returns
    -------
    dict
        {
            "query": str,
            "synthetic_results": list,
            "sources": list
        }
    """
    search_query = query
    response = requests.get(
        "https://serpapi.com/search",
        params={
            "q": search_query,
            "api_key": SERP_API_KEY,
            "num": max_results,
        },
        timeout=30,
    )
    response.raise_for_status()
    results = response.json()
    synthetic_results = []
    sources = []
    for result in results.get("organic_results", []):
        url = result.get("link")
        if not url:
            continue
        try:
            response = requests.get(
                url,
                timeout=60,
            )
            response.raise_for_status()
            # filename = (
            #     result["title"]
            #     .replace("/", "_")
            #     .replace("\\", "_")
            #     .replace(" ", "_")
            # )
            # filepath = os.path.join(
            #     DOWNLOAD_DIR,
            #     f"{filename}.pdf"
            # )
            # with open(filepath, "wb") as f:
            #     f.write(pdf_response.content)
            synthetic_results.append(str(response.content.decode("utf-8", errors="ignore")))
            sources.append(
                {
                    "title": result.get("title"),
                    "url": url,
                }
            )

        except Exception as e:
            print(
                f"Failed to download {url}: {e}"
            )

    return {
        "query": query,
        "synthetic_results": synthetic_results,
        "sources": sources,
    }