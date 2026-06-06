"""
Official company report discovery and download tool.

This tool is shaped like `web_search_tool`, but it focuses on the target
company's official website and investor-relations pages to locate and download
annual reports into `data/raw`.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
from typing import Any
from urllib.parse import urljoin, urlparse

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional dependency
    load_dotenv = None

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover - optional dependency
    BeautifulSoup = None

try:
    import requests
except ImportError:  # pragma: no cover - optional dependency
    requests = None


RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
REPORT_KEYWORDS = (
    "annual report",
    "annual reports",
    "annual-report",
    "investor relations",
    "investors",
    "financial statements",
    "10-k",
)

if load_dotenv is not None:  # pragma: no branch - simple optional setup
    load_dotenv()


def official_report_tool(
    user_query: str,
    *,
    company_name: str | None = None,
    company_website: str | None = None,
    years: list[int] | None = None,
    download_dir: str | None = None,
    use_selenium: bool = False,
    dry_run: bool = False,
    max_reports: int = 3,
) -> dict[str, Any]:
    """
    Search an official company site for annual reports and download them.

    The response mirrors the structure of `web_search_tool` so the orchestrator
    can treat both tools similarly.
    """

    normalized_company = company_name or _infer_company_name(user_query)
    normalized_website = _normalize_website(company_website)
    target_years = years or _extract_years(user_query)
    target_dir = Path(download_dir) if download_dir else RAW_DATA_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    if not normalized_company:
        return {
            "prompts": [],
            "total_prompts": 0,
            "search_strategy": "Could not infer a target company from the user query.",
            "documents": [],
            "downloaded_files": [],
            "matched_links": [],
            "search_queries": [],
            "used_selenium": False,
            "dry_run": dry_run,
            "error": "company_name_missing",
        }

    if not normalized_website:
        normalized_website = _infer_company_website_via_serpapi(normalized_company)

    prompts = _build_prompts(
        user_query=user_query,
        company_name=normalized_company,
        company_website=normalized_website,
        years=target_years,
    )

    if dry_run:
        serpapi_query = _build_serpapi_query(
            company_name=normalized_company,
            company_website=normalized_website,
            years=target_years,
        )
        planned_files = [
            str(target_dir / _build_report_filename(normalized_company, year, index))
            for index, year in enumerate(target_years or [None], start=1)
        ]
        return {
            "prompts": prompts,
            "total_prompts": len(prompts),
            "search_strategy": "Dry run for SerpAPI-first official report discovery.",
            "documents": [
                {
                    "text": (
                        f"Dry run: would search for official annual report PDFs using SerpAPI query "
                        f"'{serpapi_query}', then download matches into {target_dir}. "
                        f"Fallback source: {normalized_website or 'inferred official website search'}. "
                        f"Query: {user_query}"
                    ),
                    "source": normalized_website or normalized_company,
                    "page": 1,
                    "section_title": "Official Report Dry Run",
                    "section_type": "body",
                    "score": 1.0,
                }
            ],
            "downloaded_files": planned_files,
            "matched_links": [],
            "search_queries": [serpapi_query],
            "used_selenium": False,
            "dry_run": True,
            "resolved_company_name": normalized_company,
            "resolved_company_website": normalized_website,
        }

    result = _discover_and_download_reports(
        company_name=normalized_company,
        company_website=normalized_website,
        years=target_years,
        download_dir=target_dir,
        max_reports=max_reports,
        use_selenium=use_selenium,
    )

    return {
        "prompts": prompts,
        "total_prompts": len(prompts),
        "search_strategy": result["search_strategy"],
        "documents": result["documents"],
        "downloaded_files": result["downloaded_files"],
        "matched_links": result["matched_links"],
        "search_queries": result.get("search_queries", []),
        "used_selenium": result["used_selenium"],
        "dry_run": False,
        "resolved_company_name": normalized_company,
        "resolved_company_website": normalized_website,
        **({"error": result["error"]} if result.get("error") else {}),
    }


def _build_prompts(
    *,
    user_query: str,
    company_name: str | None,
    company_website: str | None,
    years: list[int],
) -> list[dict[str, Any]]:
    label = company_name or user_query
    year_hint = ", ".join(str(year) for year in years) if years else "latest available years"
    website_hint = company_website or "official company website"
    return [
        {
            "query": f"Browse {website_hint} investor relations pages for annual reports",
            "rationale": "Find annual-report PDFs from the official source instead of third-party sites.",
            "priority": "high",
            "expected_sources": ["official_company_website"],
        },
        {
            "query": f"Locate {label} annual report PDF files for {year_hint}",
            "rationale": "Target the specific filing years requested by the user.",
            "priority": "high",
            "expected_sources": ["official_investor_relations", "official_filings"],
        },
    ]


def _discover_and_download_reports(
    *,
    company_name: str | None,
    company_website: str | None,
    years: list[int],
    download_dir: Path,
    max_reports: int,
    use_selenium: bool,
) -> dict[str, Any]:
    if requests is None or BeautifulSoup is None:
        return {
            "search_strategy": "Requests/BeautifulSoup are unavailable, so official-site crawling cannot run.",
            "documents": [],
            "downloaded_files": [],
            "matched_links": [],
            "search_queries": [],
            "used_selenium": False,
            "error": "crawler_dependencies_missing",
        }

    search_query = _build_serpapi_query(
        company_name=company_name,
        company_website=company_website,
        years=years,
    )
    matched_links = _search_report_links_via_serpapi(
        search_query,
        company_website=company_website,
        years=years,
    )

    candidate_pages = _candidate_pages(company_website) if company_website else []
    used_selenium_flag = False
    strategy = "Used SerpAPI PDF search modeled after ai_integration/search.py."

    if not matched_links and candidate_pages:
        page_links: list[str] = []
        if use_selenium:
            selenium_links = _collect_links_with_selenium(candidate_pages)
            if selenium_links:
                page_links.extend(selenium_links)
                used_selenium_flag = True

        if not page_links:
            page_links.extend(_collect_links_with_requests(candidate_pages))

        matched_links = _filter_report_links(page_links, company_website, years)
        strategy = (
            "SerpAPI returned no usable report links; fell back to Selenium-rendered investor-relations pages."
            if used_selenium_flag
            else "SerpAPI returned no usable report links; fell back to HTTP crawling of investor-relations pages."
        )

    matched_links = matched_links[:max(max_reports, 1)]

    downloaded_files: list[str] = []
    documents: list[dict[str, Any]] = []
    for index, link in enumerate(matched_links, start=1):
        try:
            file_path = _download_report(
                link,
                download_dir=download_dir,
                company_name=company_name,
                years=years,
                sequence=index,
            )
            downloaded_files.append(str(file_path))
            documents.append(
                {
                    "text": (
                        f"Downloaded official annual report from {link} to {file_path} "
                        f"for {company_name or 'target company'}."
                    ),
                    "source": link,
                    "page": 1,
                    "section_title": "Official Annual Report",
                    "section_type": "body",
                    "score": 1.0,
                }
            )
        except Exception:
            continue

    if not downloaded_files:
        return {
            "search_strategy": strategy,
            "documents": [
                {
                    "text": (
                        f"No downloadable annual report PDF links were found on {company_website}. "
                        "Try providing a more precise investor-relations URL."
                    ),
                    "source": company_website,
                    "page": 1,
                    "section_title": "Official Report Search",
                    "section_type": "body",
                    "score": 0.8,
                }
            ],
            "downloaded_files": [],
            "matched_links": matched_links,
            "search_queries": [search_query],
            "used_selenium": used_selenium_flag,
            "error": "no_reports_found",
        }

    return {
        "search_strategy": strategy,
        "documents": documents,
        "downloaded_files": downloaded_files,
        "matched_links": matched_links,
        "search_queries": [search_query],
        "used_selenium": used_selenium_flag,
    }


def _build_serpapi_query(
    *,
    company_name: str | None,
    company_website: str | None,
    years: list[int],
) -> str:
    label = company_name or "company"
    year_part = " OR ".join(str(year) for year in years) if years else ""
    parsed = urlparse(company_website) if company_website else None
    domain = parsed.netloc if parsed else ""
    parts = [label, "annual report"]
    if year_part:
        parts.append(year_part)
    if domain:
        parts.append(f"site:{domain}")
    parts.append("filetype:pdf")
    return " ".join(part for part in parts if part)


def _search_report_links_via_serpapi(
    search_query: str,
    *,
    company_website: str,
    years: list[int],
) -> list[str]:
    api_key = os.getenv("SERPAPI_API_KEY") or os.getenv("API_KEY")
    if requests is None or not api_key:
        return []

    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={
                "q": search_query,
                "api_key": api_key,
                "num": 10,
            },
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return []

    organic_results = payload.get("organic_results", [])
    raw_links = [
        result.get("link", "").strip()
        for result in organic_results
        if isinstance(result, dict) and result.get("link")
    ]
    return _filter_report_links(raw_links, company_website, years)


def _infer_company_website_via_serpapi(company_name: str) -> str | None:
    api_key = os.getenv("SERPAPI_API_KEY") or os.getenv("API_KEY")
    if requests is None or not api_key:
        return None

    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={
                "q": f"{company_name} investor relations official website",
                "api_key": api_key,
                "num": 5,
            },
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return None

    for result in payload.get("organic_results", []):
        if not isinstance(result, dict):
            continue
        link = result.get("link", "").strip()
        if not link:
            continue
        lowered = link.lower()
        if any(keyword in lowered for keyword in ("investor", "annual", "financial", "ir.")):
            return _normalize_website(link)

    for result in payload.get("organic_results", []):
        if not isinstance(result, dict):
            continue
        link = result.get("link", "").strip()
        if link:
            return _normalize_website(link)
    return None


def _candidate_pages(company_website: str) -> list[str]:
    base = company_website.rstrip("/")
    return [
        base,
        urljoin(f"{base}/", "investors"),
        urljoin(f"{base}/", "investor-relations"),
        urljoin(f"{base}/", "annual-reports"),
        urljoin(f"{base}/", "financials"),
    ]


def _collect_links_with_requests(candidate_pages: list[str]) -> list[str]:
    discovered_links: list[str] = []
    for page_url in candidate_pages:
        try:
            response = requests.get(page_url, timeout=10)
            response.raise_for_status()
        except Exception:
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        for anchor in soup.find_all("a", href=True):
            href = str(anchor.get("href", "")).strip()
            if not href:
                continue
            discovered_links.append(urljoin(page_url, href))
    return discovered_links


def _collect_links_with_selenium(candidate_pages: list[str]) -> list[str]:
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except ImportError:  # pragma: no cover - optional dependency
        return []

    links: list[str] = []
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    try:
        driver = webdriver.Chrome(options=options)
    except Exception:
        return []

    try:
        for page_url in candidate_pages:
            try:
                driver.get(page_url)
                anchors = driver.find_elements("tag name", "a")
                for anchor in anchors:
                    href = anchor.get_attribute("href")
                    if href:
                        links.append(href)
            except Exception:
                continue
    finally:
        driver.quit()

    return links


def _filter_report_links(
    links: list[str],
    company_website: str | None,
    years: list[int],
) -> list[str]:
    parsed_company = urlparse(company_website) if company_website else None
    base_domain = parsed_company.netloc.lower() if parsed_company else ""
    candidates: list[str] = []
    seen: set[str] = set()

    for link in links:
        normalized = link.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)

        parsed_link = urlparse(normalized)
        if base_domain and parsed_link.netloc and parsed_link.netloc.lower() != base_domain:
            continue

        lowered = normalized.lower()
        if ".pdf" not in lowered and not any(keyword in lowered for keyword in REPORT_KEYWORDS):
            continue

        if years and not any(str(year) in lowered for year in years):
            if ".pdf" in lowered:
                candidates.append(normalized)
            continue

        candidates.append(normalized)

    def sort_key(url: str) -> tuple[int, int]:
        lowered = url.lower()
        has_pdf = 0 if lowered.endswith(".pdf") or ".pdf?" in lowered else 1
        keyword_rank = 0 if "annual" in lowered or "10-k" in lowered else 1
        return (has_pdf, keyword_rank)

    return sorted(candidates, key=sort_key)


def _download_report(
    url: str,
    *,
    download_dir: Path,
    company_name: str | None,
    years: list[int],
    sequence: int,
) -> Path:
    if requests is None:
        raise RuntimeError("requests is unavailable")

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    year = _extract_year_from_text(url) or (years[sequence - 1] if sequence - 1 < len(years) else None)
    filename = _build_report_filename(company_name, year, sequence, url=url)
    path = download_dir / filename
    path.write_bytes(response.content)
    return path


def _build_report_filename(
    company_name: str | None,
    year: int | None,
    sequence: int,
    *,
    url: str | None = None,
) -> str:
    slug = _slugify(company_name or "company")
    suffix = f"_{year}" if year is not None else f"_{sequence}"
    extension = ".pdf"
    if url and ".pdf" not in url.lower():
        extension = ".bin"
    return f"{slug}_annual_report{suffix}{extension}"


def _normalize_website(company_website: str | None) -> str | None:
    if not company_website:
        return None
    website = company_website.strip()
    if not website:
        return None
    if not website.startswith(("http://", "https://")):
        website = f"https://{website}"
    return website


def _extract_years(text: str) -> list[int]:
    years = [int(match) for match in re.findall(r"\b((?:19|20)\d{2})\b", text)]
    unique_years: list[int] = []
    for year in years:
        if year not in unique_years:
            unique_years.append(year)
    return unique_years


def _extract_year_from_text(text: str) -> int | None:
    match = re.search(r"\b((?:19|20)\d{2})\b", text)
    if not match:
        return None
    return int(match.group(1))


def _infer_company_name(query: str) -> str | None:
    stopwords = {
        "download", "find", "get", "official", "company", "website", "annual",
        "report", "reports", "investor", "relations", "for", "the", "latest",
        "from", "and", "make", "a", "an", "of", "in", "to", "what", "is",
        "are", "financial", "statements", "please", "me", "show",
    }
    tokens = re.findall(r"[A-Za-z0-9&.\-]+", query)
    filtered = [
        token
        for token in tokens
        if token.lower() not in stopwords and not re.fullmatch(r"(?:19|20)\d{2}", token)
    ]
    cleaned = " ".join(filtered[:4]).strip(" -,:")
    return cleaned or None


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "company"
