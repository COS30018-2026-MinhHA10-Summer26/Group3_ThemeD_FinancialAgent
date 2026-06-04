"""
Official company report discovery and download tool.

This tool is shaped like `web_search_tool`, but it focuses on the target
company's official website and investor-relations pages to locate and download
annual reports into `data/raw`.
"""

from __future__ import annotations

from pathlib import Path
import re
from typing import Any
from urllib.parse import urljoin, urlparse

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

    normalized_website = _normalize_website(company_website)
    normalized_company = company_name or _infer_company_name(user_query)
    target_years = years or _extract_years(user_query)
    target_dir = Path(download_dir) if download_dir else RAW_DATA_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    prompts = _build_prompts(
        user_query=user_query,
        company_name=normalized_company,
        company_website=normalized_website,
        years=target_years,
    )

    if not normalized_website:
        return {
            "prompts": prompts,
            "total_prompts": len(prompts),
            "search_strategy": (
                "Official-site report lookup requires a company website or investor-relations URL."
            ),
            "documents": [],
            "downloaded_files": [],
            "matched_links": [],
            "used_selenium": False,
            "dry_run": dry_run,
            "error": "company_website_missing",
        }

    if dry_run:
        planned_files = [
            str(target_dir / _build_report_filename(normalized_company, year, index))
            for index, year in enumerate(target_years or [None], start=1)
        ]
        return {
            "prompts": prompts,
            "total_prompts": len(prompts),
            "search_strategy": "Dry run for official investor-relations report discovery.",
            "documents": [
                {
                    "text": (
                        f"Dry run: would search the official investor-relations website {normalized_website} "
                        f"and download annual reports for {normalized_company or 'target company'} "
                        f"into {target_dir}. Query: {user_query}"
                    ),
                    "source": normalized_website,
                    "page": 1,
                    "section_title": "Official Report Dry Run",
                    "section_type": "body",
                    "score": 1.0,
                }
            ],
            "downloaded_files": planned_files,
            "matched_links": [],
            "used_selenium": False,
            "dry_run": True,
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
        "used_selenium": result["used_selenium"],
        "dry_run": False,
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
    company_website: str,
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
            "used_selenium": False,
            "error": "crawler_dependencies_missing",
        }

    candidate_pages = _candidate_pages(company_website)
    page_links: list[str] = []
    used_selenium_flag = False

    if use_selenium:
        selenium_links = _collect_links_with_selenium(candidate_pages)
        if selenium_links:
            page_links.extend(selenium_links)
            used_selenium_flag = True

    if not page_links:
        page_links.extend(_collect_links_with_requests(candidate_pages))

    matched_links = _filter_report_links(page_links, company_website, years)
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

    strategy = (
        "Rendered investor-relations pages with Selenium before downloading PDFs."
        if used_selenium_flag
        else "Crawled investor-relations and annual-report pages with HTTP requests."
    )

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
            "used_selenium": used_selenium_flag,
            "error": "no_reports_found",
        }

    return {
        "search_strategy": strategy,
        "documents": documents,
        "downloaded_files": downloaded_files,
        "matched_links": matched_links,
        "used_selenium": used_selenium_flag,
    }


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
    company_website: str,
    years: list[int],
) -> list[str]:
    parsed_company = urlparse(company_website)
    base_domain = parsed_company.netloc.lower()
    candidates: list[str] = []
    seen: set[str] = set()

    for link in links:
        normalized = link.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)

        parsed_link = urlparse(normalized)
        if parsed_link.netloc and parsed_link.netloc.lower() != base_domain:
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
    cleaned = re.sub(
        r"\b(download|find|get|official|company|website|annual|report|reports|investor|relations|for|the|latest)\b",
        " ",
        query,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -,:")
    return cleaned or None


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "company"
