"""
Public Knowledge Base helpers for https://knowledge.ariasystems.net/.

This module provides small, dependency-light crawling and searching utilities
that are safe for MCP tool usage.
"""

from __future__ import annotations

import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests

DEFAULT_BASE_URL = "https://knowledge.ariasystems.net/"


class _HTMLTextExtractor(HTMLParser):
    """Extracts visible text and links from HTML."""

    def __init__(self) -> None:
        super().__init__()
        self._skip = False
        self.title = ""
        self._in_title = False
        self.text_parts: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        if tag in ("script", "style", "noscript"):
            self._skip = True
        if tag == "title":
            self._in_title = True
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        if tag in ("script", "style", "noscript"):
            self._skip = False
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        if self._skip:
            return
        value = data.strip()
        if not value:
            return
        if self._in_title:
            self.title = value if not self.title else f"{self.title} {value}"
        self.text_parts.append(value)


def _normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9_]{2,}", text.lower())


def _same_host(url: str, base_url: str) -> bool:
    return urlparse(url).netloc == urlparse(base_url).netloc


def fetch_kb_page(url: str, timeout_sec: int = 20, max_chars: int = 12000) -> dict:
    """Fetch and parse a KB page into title/text/links."""
    if not url:
        raise ValueError("url is required.")

    resp = requests.get(url, timeout=timeout_sec, headers={"User-Agent": "MCP-KB-Tool/1.0"})
    resp.raise_for_status()
    html = resp.text

    parser = _HTMLTextExtractor()
    parser.feed(html)

    text = _normalize_space(unescape(" ".join(parser.text_parts)))
    if len(text) > max_chars:
        text = text[:max_chars]

    normalized_links = []
    for href in parser.links:
        abs_url = urljoin(url, href)
        if abs_url.startswith("http://") or abs_url.startswith("https://"):
            normalized_links.append(abs_url)

    return {
        "url": url,
        "title": _normalize_space(unescape(parser.title)) or url,
        "text": text,
        "text_length": len(text),
        "links": sorted(set(normalized_links)),
    }


def search_kb(
    query: str,
    base_url: str = DEFAULT_BASE_URL,
    max_pages: int = 12,
    max_results: int = 5,
    timeout_sec: int = 20,
) -> dict:
    """
    Crawl a limited number of KB pages and return lexical matches.

    This is intentionally simple and deterministic for MCP usage.
    """
    if not query or not query.strip():
        raise ValueError("query is required.")
    if max_pages < 1:
        raise ValueError("max_pages must be at least 1.")
    if max_results < 1:
        raise ValueError("max_results must be at least 1.")

    query_terms = _tokenize(query)
    if not query_terms:
        raise ValueError("query must contain searchable terms.")
    query_counter = Counter(query_terms)

    visited: set[str] = set()
    queue: list[str] = [base_url]
    scored_pages: list[dict] = []

    while queue and len(visited) < max_pages:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        try:
            page = fetch_kb_page(current, timeout_sec=timeout_sec)
        except Exception:
            continue

        text_tokens = _tokenize(f"{page['title']} {page['text']}")
        token_counter = Counter(text_tokens)
        score = sum(min(token_counter[t], c) for t, c in query_counter.items())
        if score > 0:
            snippet = page["text"][:300]
            scored_pages.append(
                {
                    "url": page["url"],
                    "title": page["title"],
                    "score": score,
                    "snippet": snippet,
                }
            )

        for link in page["links"]:
            if _same_host(link, base_url) and link not in visited and link not in queue:
                queue.append(link)

    scored_pages.sort(key=lambda x: x["score"], reverse=True)
    return {
        "query": query,
        "base_url": base_url,
        "pages_scanned": len(visited),
        "results": scored_pages[:max_results],
    }
