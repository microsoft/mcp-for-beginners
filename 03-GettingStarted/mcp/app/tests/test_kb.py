from __future__ import annotations

from unittest.mock import patch

import pytest

from kb import fetch_kb_page, search_kb


class _Resp:
    def __init__(self, text: str, status_code: int = 200) -> None:
        self.text = text
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError("http error")


def test_fetch_kb_page_extracts_title_text_and_links():
    html = """
    <html>
      <head><title>Aria KB Home</title></head>
      <body>
        <h1>Welcome</h1>
        <p>Billing release notes and docs.</p>
        <a href="/article1">Article 1</a>
      </body>
    </html>
    """
    with patch("kb.requests.get", return_value=_Resp(html)):
        out = fetch_kb_page("https://knowledge.ariasystems.net/")
    assert out["title"] == "Aria KB Home"
    assert "Billing release notes" in out["text"]
    assert "https://knowledge.ariasystems.net/article1" in out["links"]


def test_search_kb_scores_matching_page():
    home = """
    <html><head><title>Home</title></head>
    <body><a href="/release70">Release 70 notes</a></body></html>
    """
    rel = """
    <html><head><title>Aria Billing Release 70</title></head>
    <body>Release 70 introduces billing APIs and account updates.</body></html>
    """

    def _fake_get(url, timeout=20, headers=None):  # noqa: ANN001
        if url.endswith("/release70"):
            return _Resp(rel)
        return _Resp(home)

    with patch("kb.requests.get", side_effect=_fake_get):
        out = search_kb("billing release 70", max_pages=4, max_results=2)

    assert out["pages_scanned"] >= 1
    assert out["results"]
    assert "Release 70" in out["results"][0]["title"]


def test_search_kb_requires_query():
    with pytest.raises(ValueError):
        search_kb("")
