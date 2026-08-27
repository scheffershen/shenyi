#!/usr/bin/env python3
"""Verify the standalone RAG Formation lesson and reference page matrix."""
from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://shenyi.dev"

LANGUAGES = {
    "en": {"html_lang": "en", "root": Path("ai-lab/rag-formation")},
    "fr": {"html_lang": "fr", "root": Path("fr/ai-lab/rag-formation")},
    "zh": {"html_lang": "zh-CN", "root": Path("zh/ai-lab/rag-formation")},
}
DEVELOPMENT_MARKERS = {"en": "development", "fr": "développement", "zh": "开发"}
LESSONS = [
    "0001-from-question-to-cited-answer.html",
    "0002-trace-one-question.html",
    "0003-build-a-trustworthy-evaluation-set.html",
    "0004-establish-the-mvp-baseline.html",
    "0005-semantic-keyword-and-hybrid-retrieval.html",
    "0006-chunking-and-document-structure.html",
    "0007-metadata-filters-and-access-boundaries.html",
    "0008-query-handling-and-reranking.html",
    "0009-context-assembly-and-evidence-budgets.html",
    "0010-prompts-that-answer-only-from-evidence.html",
    "0011-citation-design-and-source-fidelity.html",
    "0012-refusal-uncertainty-and-hallucination-control.html",
    "0013-failure-isolation-and-graceful-degradation.html",
    "0014-latency-cost-and-observability.html",
    "0015-security-permissions-and-deployment-boundaries.html",
    "0016-pilot-review-and-30-day-implementation-plan.html",
]
REFERENCES = [
    "baseline-evaluation-cheatsheet.html",
    "chunking-and-document-structure-cheatsheet.html",
    "citation-design-and-source-fidelity-cheatsheet.html",
    "context-assembly-and-evidence-budgets-cheatsheet.html",
    "evaluation-set-cheatsheet.html",
    "failure-isolation-and-graceful-degradation-cheatsheet.html",
    "glossary-cheatsheet.html",
    "latency-cost-and-observability-cheatsheet.html",
    "metadata-filters-and-access-boundaries-cheatsheet.html",
    "pilot-review-and-30-day-implementation-plan-cheatsheet.html",
    "prompts-that-answer-only-from-evidence-cheatsheet.html",
    "query-handling-and-reranking-cheatsheet.html",
    "rag-quality-cheatsheet.html",
    "refusal-uncertainty-and-hallucination-control-cheatsheet.html",
    "request-path-cheatsheet.html",
    "security-permissions-and-deployment-boundaries-cheatsheet.html",
    "semantic-keyword-and-hybrid-retrieval-cheatsheet.html",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.title = ""
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.link_tags: list[dict[str, str]] = []
        self.scripts: list[str] = []
        self.images: list[dict[str, str]] = []
        self.visible_parts: list[str] = []
        self._in_title = False
        self._ignored_depth = 0
        self._in_body = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.html_lang = values.get("lang", "")
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            self.meta.append(values)
        if tag == "a":
            self.links.append(values)
        if tag == "link":
            self.link_tags.append(values)
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"])
        if tag == "img":
            self.images.append(values)
        if tag == "body":
            self._in_body = True
        if tag in ("script", "style"):
            self._ignored_depth += 1

        if self._in_body and self._ignored_depth == 0:
            if "data-quiz" in values:
                self.visible_parts.append(" data-quiz ")
            if "data-feedback" in values:
                self.visible_parts.append(" data-feedback ")

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_body and self._ignored_depth == 0:
            self.visible_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag in ("script", "style") and self._ignored_depth:
            self._ignored_depth -= 1
        if tag == "body":
            self._in_body = False

    @property
    def visible_text(self) -> str:
        return "".join(self.visible_parts)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def expected_url(locale: str, kind: str, basename: str) -> str:
    return f"{BASE}/{LANGUAGES[locale]['root'].as_posix()}/{kind}/{basename}"


def expected_alternates(kind: str, basename: str) -> dict[str, str]:
    return {
        "en": expected_url("en", kind, basename),
        "fr": expected_url("fr", kind, basename),
        "zh": expected_url("zh", kind, basename),
        "x-default": expected_url("en", kind, basename),
    }


def meta_content(parser: PageParser, name: str) -> list[str]:
    return [tag.get("content", "") for tag in parser.meta if tag.get("name") == name]


def local_target(page_path: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "http:", "https:", "mailto:", "tel:", "javascript:")):
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    clean = parsed.path
    if not clean:
        return None
    target = (page_path.parent / clean).resolve()
    if clean.endswith("/"):
        target /= "index.html"
    return target


def check_local_links(page_path: Path, parser: PageParser, route_label: str) -> None:
    for link in parser.links + parser.link_tags:
        href = link.get("href", "")
        target = local_target(page_path, href)
        if target is not None and not target.is_file():
            fail(f"{route_label}: broken local link {href}")
    for src in parser.scripts:
        target = local_target(page_path, src)
        if target is not None and not target.is_file():
            fail(f"{route_label}: missing local script {src}")
    for image in parser.images:
        src = image.get("src", "")
        target = local_target(page_path, src)
        if target is not None and not target.is_file():
            fail(f"{route_label}: missing local image {src}")
        if src and image.get("aria-hidden") != "true" and not image.get("alt", "").strip():
            fail(f"{route_label}: meaningful image is missing alt text {src}")


def check_metadata(page_path: Path, parser: PageParser, locale: str, kind: str, basename: str) -> None:
    route_label = page_path.relative_to(ROOT).as_posix()
    if parser.html_lang != LANGUAGES[locale]["html_lang"]:
        fail(f"{route_label}: expected html lang {LANGUAGES[locale]['html_lang']}")
    if not parser.title.strip():
        fail(f"{route_label}: missing title")
    descriptions = meta_content(parser, "description")
    if len(descriptions) != 1 or not descriptions[0].strip():
        fail(f"{route_label}: missing unique meta description")

    canonical = [
        tag.get("href", "")
        for tag in parser.link_tags
        if tag.get("rel") == "canonical"
    ]
    expected_canonical = expected_url(locale, kind, basename)
    if canonical != [expected_canonical]:
        fail(f"{route_label}: canonical is {canonical}, expected {expected_canonical}")

    alternates = {
        tag.get("hreflang", ""): tag.get("href", "")
        for tag in parser.link_tags
        if tag.get("rel") == "alternate" and tag.get("hreflang")
    }
    expected = expected_alternates(kind, basename)
    if alternates != expected:
        fail(f"{route_label}: alternates are {alternates}, expected {expected}")

    if not any(tag.get("property") == "og:title" and tag.get("content", "").strip() for tag in parser.meta):
        fail(f"{route_label}: missing og:title")
    if not any(tag.get("name") == "twitter:title" and tag.get("content", "").strip() for tag in parser.meta):
        fail(f"{route_label}: missing twitter:title")


def check_lesson(page_path: Path, parser: PageParser, locale: str, basename: str) -> None:
    route_label = page_path.relative_to(ROOT).as_posix()
    raw = page_path.read_text(encoding="utf-8")
    check_metadata(page_path, parser, locale, "lessons", basename)
    expected_main = "assets/js/main.js"
    expected_lesson = "assets/js/lesson.js"
    if not any(src.endswith(expected_main) for src in parser.scripts):
        fail(f"{route_label}: missing shared main.js")
    if not any(src.endswith(expected_lesson) for src in parser.scripts):
        fail(f"{route_label}: missing lesson.js")
    if "RAG Formation" not in parser.visible_text:
        fail(f"{route_label}: missing RAG Formation label")
    if DEVELOPMENT_MARKERS[locale].lower() not in parser.visible_text.lower():
        fail(f"{route_label}: missing course-in-development marker")
    quiz_count = raw.count("data-quiz")
    feedback_count = raw.count("data-feedback")
    answer_count = raw.count("data-answer=")
    if quiz_count < 1 or feedback_count < quiz_count or answer_count < quiz_count * 2:
        fail(f"{route_label}: incomplete browser exercise markup")
    if "github.com" in raw.lower() or "MISSION.md" in raw or "RESOURCES.md" in raw:
        fail(f"{route_label}: repository-only link remains")
    if not any("/reference/" in link.get("href", "") for link in parser.links):
        fail(f"{route_label}: missing local reference link")
    if not any(link.get("href") == "../" for link in parser.links):
        fail(f"{route_label}: missing course roadmap link")
    check_local_links(page_path, parser, route_label)
    print(f"PASS lesson {route_label}")


def check_reference(page_path: Path, parser: PageParser, locale: str, basename: str) -> None:
    route_label = page_path.relative_to(ROOT).as_posix()
    raw = page_path.read_text(encoding="utf-8")
    check_metadata(page_path, parser, locale, "reference", basename)
    if "RAG" not in parser.visible_text:
        fail(f"{route_label}: missing RAG content")
    if "github.com" in raw.lower() or "MISSION.md" in raw or "RESOURCES.md" in raw:
        fail(f"{route_label}: repository-only link remains")
    lesson_name = basename.removesuffix("-cheatsheet.html")
    if not any(lesson_name in link.get("href", "") for link in parser.links):
        fail(f"{route_label}: missing matching lesson link")
    check_local_links(page_path, parser, route_label)
    print(f"PASS reference {route_label}")


def check_kind(locale: str, kind: str) -> None:
    basenames = LESSONS if kind == "lessons" else REFERENCES
    for basename in basenames:
        page_path = ROOT / LANGUAGES[locale]["root"] / kind / basename
        if not page_path.is_file():
            fail(f"missing {page_path}")
        parser = PageParser()
        parser.feed(page_path.read_text(encoding="utf-8"))
        if kind == "lessons":
            check_lesson(page_path, parser, locale, basename)
        else:
            check_reference(page_path, parser, locale, basename)


def check_sitemap() -> None:
    sitemap_path = ROOT / "sitemap.xml"
    root = ET.parse(sitemap_path)
    namespace = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xhtml": "http://www.w3.org/1999/xhtml",
    }
    url_nodes = {
        node.findtext("sm:loc", namespaces=namespace): node
        for node in root.findall("sm:url", namespace)
    }
    for kind, basenames in (("lessons", LESSONS), ("reference", REFERENCES)):
        for basename in basenames:
            expected = expected_alternates(kind, basename)
            for loc in expected.values():
                node = url_nodes.get(loc)
                if node is None:
                    fail(f"sitemap missing {loc}")
                lastmod = node.findtext("sm:lastmod", namespaces=namespace)
                if not lastmod:
                    fail(f"sitemap missing lastmod for {loc}")
                try:
                    date.fromisoformat(lastmod)
                except ValueError:
                    fail(f"sitemap lastmod for {loc} is not ISO: {lastmod}")
                alternates = {
                    link.attrib.get("hreflang", ""): link.attrib.get("href", "")
                    for link in node.findall("xhtml:link", namespace)
                }
                if alternates != expected:
                    fail(f"sitemap alternates for {loc}: {alternates}")
    print("PASS sitemap lesson/reference matrix")


def main() -> int:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--locale", choices=("en", "fr", "zh"))
    argument_parser.add_argument("--kind", choices=("lessons", "references", "all"), default="all")
    args = argument_parser.parse_args()

    kinds = ("lessons", "references") if args.kind == "all" else (args.kind,)
    locales = (args.locale,) if args.locale else tuple(LANGUAGES)
    for locale in locales:
        for kind in kinds:
            check_kind(locale, kind)
    if args.kind == "all" and args.locale is None:
        check_sitemap()
    print("PASS standalone RAG Formation lesson/reference checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
