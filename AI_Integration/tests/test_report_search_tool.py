from __future__ import annotations

from pathlib import Path

import requests

from ai_integration.tools import report_search_tool as search_tool


class _FakeResponse:
    def __init__(self, *, payload=None, content=b"", content_type="application/pdf"):
        self._payload = payload or {}
        self.content = content
        self.headers = {"content-type": content_type}

    def raise_for_status(self) -> None:
        return None

    def json(self):
        return self._payload


def test_report_search_uses_only_a_request_scoped_temp_file(monkeypatch, tmp_path):
    """Web-search PDFs must never become part of the persistent raw corpus."""
    captured_pdf_paths: list[Path] = []

    def fake_get(url, **_kwargs):
        if url == "https://serpapi.com/search":
            return _FakeResponse(payload={
                "organic_results": [{"title": "Tesla annual report", "link": "https://example.test/tesla.pdf"}],
            })
        return _FakeResponse(content=b"%PDF-1.7 temporary test document")

    def fake_extract(pdf_path: str, **_kwargs):
        path = Path(pdf_path)
        captured_pdf_paths.append(path)
        assert path.exists()
        return [{"text": "Tesla reported revenue.", "source": pdf_path, "page": 1}]

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(search_tool.requests, "get", fake_get)
    monkeypatch.setattr(search_tool, "extract_documents", fake_extract)
    monkeypatch.setattr(search_tool, "_is_parseable_pdf", lambda _content: True)

    result = search_tool.report_search_tool("Tesla revenue", max_results=1)

    assert captured_pdf_paths
    assert all(not path.exists() for path in captured_pdf_paths)
    assert not (tmp_path / "data" / "raw").exists()
    assert result["synthetic_results"][0]["source"] == "https://example.test/tesla.pdf"
    assert result["sources"] == [{"title": "Tesla annual report", "url": "https://example.test/tesla.pdf"}]


def test_report_search_skips_invalid_tls_and_uses_next_candidate(monkeypatch):
    calls: list[tuple[str, dict]] = []

    def fake_get(url, **kwargs):
        calls.append((url, kwargs))
        if url == "https://serpapi.com/search":
            return _FakeResponse(payload={
                "organic_results": [
                    {"title": "Bad TLS report", "link": "https://invalid-cert.test/report.pdf"},
                    {"title": "Trusted report", "link": "https://trusted.test/report.pdf"},
                ],
            })
        if url == "https://invalid-cert.test/report.pdf":
            raise requests.exceptions.SSLError("certificate verify failed")
        return _FakeResponse(content=b"%PDF-1.7 trusted report")

    monkeypatch.setattr(search_tool.requests, "get", fake_get)
    monkeypatch.setattr(search_tool, "_is_parseable_pdf", lambda _content: True)
    monkeypatch.setattr(
        search_tool,
        "extract_documents",
        lambda _path, **_kwargs: [{"text": "Tesla revenue in the trusted report.", "page": 1}],
    )

    result = search_tool.report_search_tool("Tesla revenue", max_results=1)

    assert result["sources"] == [{"title": "Trusted report", "url": "https://trusted.test/report.pdf"}]
    assert all(kwargs.get("verify") is not False for _url, kwargs in calls)
    search_request = calls[0]
    assert search_request[1]["params"]["num"] == 5
