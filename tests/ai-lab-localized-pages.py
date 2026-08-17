#!/usr/bin/env python3
"""Verify the complete EN/FR/ZH AI Lab page and sitemap matrix."""
from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://shenyi.dev"
GA_ID = "G-S0YRBQKHLZ"

ROUTES = {
    "overview": {
        "en": "ai-lab/",
        "fr": "fr/ai-lab/",
        "zh": "zh/ai-lab/",
        "types": {"CollectionPage"},
        "project_names": {"RAG Engineer", "RAG Evaluation", "RAG Formation"},
        "asset": "assets/img/ai-lab/rag-engineer-social.png",
    },
    "engineer": {
        "en": "ai-lab/rag-engineer/",
        "fr": "fr/ai-lab/rag-engineer/",
        "zh": "zh/ai-lab/rag-engineer/",
        "types": {"TechArticle"},
        "project_names": {"RAG Engineer"},
        "asset": "assets/img/ai-lab/rag-engineer-social.png",
    },
    "evaluation": {
        "en": "ai-lab/rag-evaluation/",
        "fr": "fr/ai-lab/rag-evaluation/",
        "zh": "zh/ai-lab/rag-evaluation/",
        "types": {"TechArticle"},
        "project_names": {"RAG Evaluation"},
        "asset": "assets/img/ai-lab/rag-evaluation-social.png",
    },
    "formation": {
        "en": "ai-lab/rag-formation/",
        "fr": "fr/ai-lab/rag-formation/",
        "zh": "zh/ai-lab/rag-formation/",
        "types": {"Course"},
        "project_names": {"RAG Formation"},
        "asset": "assets/img/og-image.png",
    },
}

EXPECTED_LANG = {"en": "en", "fr": "fr", "zh": "zh-CN"}
DEVELOPMENT_MARKERS = {"en": "development", "fr": "développement", "zh": "开发"}
PAGE_METADATA: list[dict[str, str]] = []


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.attrs: dict[str, list[str]] = {}
        self.meta_tags: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.link_tags: list[dict[str, str]] = []
        self.images: list[str] = []
        self.image_tags: list[dict[str, str]] = []
        self.json_ld: list[str] = []
        self.title_text = ""
        self.visible_text_parts: list[str] = []
        self._in_title = False
        self._in_json_ld = False
        self._json_ld_parts: list[str] = []
        self._in_body = False
        self._ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        for key in ("lang", "title", "name", "content", "rel", "href", "property", "src", "type"):
            if key in values:
                self.attrs.setdefault(f"{tag}.{key}", []).append(values[key])
        if tag == "meta":
            self.meta_tags.append(values)
        if tag == "title":
            self._in_title = True
        if tag == "a":
            self.links.append(values)
        if tag == "link":
            self.link_tags.append(values)
        if tag == "img" and "src" in values:
            self.images.append(values["src"])
            self.image_tags.append(values)
        if tag == "body":
            self._in_body = True
        if tag in ("script", "style"):
            self._ignored_depth += 1
        if tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text += data
        if self._in_json_ld:
            self._json_ld_parts.append(data)
        if self._in_body and self._ignored_depth == 0:
            self.visible_text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_ld_parts))
            self._in_json_ld = False
        if tag in ("script", "style") and self._ignored_depth:
            self._ignored_depth -= 1
        if tag == "body":
            self._in_body = False

    def values(self, tag: str, attr: str) -> list[str]:
        return self.attrs.get(f"{tag}.{attr}", [])

    @property
    def visible_text(self) -> str:
        return "".join(self.visible_text_parts)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def get_route(path: str) -> str:
    normalized = path.removeprefix("/")
    for route in ROUTES.values():
        for language in ("en", "fr", "zh"):
            if route[language] == normalized:
                return normalized
    fail(f"unknown route {path}")


def expected_alternates(route: dict[str, object]) -> dict[str, str]:
    return {
        "en": BASE + "/" + route["en"],
        "fr": BASE + "/" + route["fr"],
        "zh": BASE + "/" + route["zh"],
        "x-default": BASE + "/" + route["en"],
    }


def parse_json_ld(parser: PageParser) -> list[dict[str, object]]:
    values = []
    for raw in parser.json_ld:
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as error:
            fail(f"invalid JSON-LD: {error}")
        values.append(value)
    return values


def meta_content(parser: PageParser, attribute: str, value: str) -> list[str]:
    return [tag.get("content", "") for tag in parser.meta_tags if tag.get(attribute) == value]


def check_page(language: str, route_name: str, route: dict[str, object]) -> None:
    relative_path = route[language]
    page_path = ROOT / relative_path / "index.html"
    if not page_path.is_file():
        fail(f"missing page {page_path}")

    parser = PageParser()
    html = page_path.read_text(encoding="utf-8")
    parser.feed(html)

    if parser.values("html", "lang") != [EXPECTED_LANG[language]]:
        fail(f"{relative_path}: incorrect html lang")

    for meta_name in ("description", "author"):
        if meta_name not in parser.values("meta", "name"):
            fail(f"{relative_path}: missing meta name={meta_name}")
    title = parser.title_text
    description = meta_content(parser, "name", "description")
    if not title.strip():
        fail(f"{relative_path}: missing unique title")
    if len(description) != 1 or not description[0].strip():
        fail(f"{relative_path}: missing meta description")

    canonical = [link.get("href") for link in parser.link_tags if link.get("rel") == "canonical"]
    expected_url = BASE + "/" + relative_path
    if canonical != [expected_url]:
        fail(f"{relative_path}: canonical must be {expected_url}")

    alternates = {
        link.get("hreflang"): link.get("href")
        for link in parser.link_tags
        if link.get("rel") == "alternate" and link.get("hreflang")
    }
    if alternates != expected_alternates(route):
        fail(f"{relative_path}: hreflang set is {alternates}, expected {expected_alternates(route)}")

    for property_name in ("og:type", "og:site_name", "og:title", "og:description", "og:url", "og:image", "og:locale"):
        if not any(tag.get("property") == property_name and tag.get("content", "").strip() for tag in parser.meta_tags):
            fail(f"{relative_path}: missing {property_name}")
    for name in ("twitter:card", "twitter:title", "twitter:description", "twitter:image"):
        if not any(tag.get("name") == name and tag.get("content", "").strip() for tag in parser.meta_tags):
            fail(f"{relative_path}: missing {name}")

    for project_name in route["project_names"]:
        if project_name not in parser.visible_text:
            fail(f"{relative_path}: missing canonical project name {project_name}")

    if GA_ID not in html or "googletagmanager.com/gtag/js" not in html:
        fail(f"{relative_path}: missing Google Analytics snippet")
    for storage_name in ("ad_storage", "ad_user_data", "ad_personalization", "analytics_storage"):
        if f"'{storage_name}': 'denied'" not in html:
            fail(f"{relative_path}: {storage_name} consent is not denied by default")

    depth = len(Path(relative_path).parts)
    if route_name != "formation":
        expected_asset = (Path(*([".."] * depth)) / route["asset"]).as_posix()
        expected_asset_options = {
            expected_asset,
            (Path(*([".."] * depth)) / "assets/img/og-image.svg").as_posix(),
        }
        if not any(asset in parser.images for asset in expected_asset_options):
            fail(f"{relative_path}: missing expected image {expected_asset_options}")
    for image_tag in parser.image_tags:
        image = image_tag["src"]
        if image_tag.get("aria-hidden") != "true" and not image_tag.get("alt", "").strip():
            fail(f"{relative_path}: meaningful image is missing alt text {image}")
        if image.startswith("http"):
            continue
        if not (page_path.parent / image).resolve().is_file():
            fail(f"{relative_path}: missing local image {image}")

    json_ld = parse_json_ld(parser)
    found_types = set()
    for item in json_ld:
        item_type = item.get("@type") if isinstance(item, dict) else None
        if isinstance(item_type, str):
            found_types.add(item_type)
        elif isinstance(item_type, list):
            found_types.update(item_type)
    if not found_types.intersection(route["types"]):
        fail(f"{relative_path}: missing structured data type {route['types']}")
    if route_name == "formation":
        marker = DEVELOPMENT_MARKERS[language]
        if marker.lower() not in parser.visible_text.lower():
            fail(f"{relative_path}: Formation visible copy must remain clearly in development")
        course_descriptions = [
            item.get("description", "")
            for item in json_ld
            if isinstance(item, dict) and item.get("@type") == "Course"
        ]
        if not any(marker.lower() in str(description).lower() for description in course_descriptions):
            fail(f"{relative_path}: Formation Course description must remain clearly in development")

    expected_lab_href = "./" if route_name == "overview" else "../"
    if not any(link.get("href") == expected_lab_href for link in parser.links):
        fail(f"{relative_path}: missing local AI Lab overview navigation link")

    for link in parser.links:
        href = link.get("href", "")
        if not href or href.startswith(("#", "http:", "https:", "mailto:", "tel:")):
            continue
        clean_href = href.split("#", 1)[0]
        if not clean_href:
            continue
        target = (page_path.parent / clean_href).resolve()
        if clean_href.endswith("/"):
            target = target / "index.html"
        if not target.is_file():
            fail(f"{relative_path}: broken local link {href}")

    PAGE_METADATA.append({"route": route_name, "language": language, "title": title.strip(), "description": description[0].strip()})
    print(f"PASS page {relative_path}")


def check_localized_metadata() -> None:
    for route_name in ROUTES:
        pages = [page for page in PAGE_METADATA if page["route"] == route_name]
        if len({page["title"] for page in pages}) != 3:
            fail(f"{route_name}: titles must be unique across locales")
        if len({page["description"] for page in pages}) != 3:
            fail(f"{route_name}: descriptions must be unique across locales")


def check_sitemap() -> None:
    sitemap = ET.parse(ROOT / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9", "xhtml": "http://www.w3.org/1999/xhtml"}
    urls = sitemap.findall("sm:url", namespace)
    locs = {element.findtext("sm:loc", namespaces=namespace): element for element in urls}
    for route in ROUTES.values():
        expected = expected_alternates(route)
        for url in expected.values():
            if url not in locs:
                fail(f"sitemap missing {url}")
            lastmod = locs[url].findtext("sm:lastmod", namespaces=namespace)
            if not lastmod:
                fail(f"sitemap missing lastmod for {url}")
            try:
                date.fromisoformat(lastmod)
            except ValueError:
                fail(f"sitemap lastmod for {url} must be an ISO date: {lastmod}")
        for url in expected.values():
            alternate_links = {
                element.attrib.get("hreflang"): element.attrib.get("href")
                for element in locs[url].findall("xhtml:link", namespace)
            }
            if alternate_links != expected:
                fail(f"sitemap alternates for {url}: {alternate_links}")
    print("PASS sitemap AI Lab route matrix")


for route_name, route in ROUTES.items():
    for language in ("en", "fr", "zh"):
        check_page(language, route_name, route)
check_localized_metadata()
check_sitemap()
print("PASS all AI Lab localization checks")
