# RAG Formation Continue — 01: design

## Goal

Publish the supplied production-RAG tutorial as the first supplementary
lesson in a distinct **RAG Formation Continue** series. It must sit beside,
not inside, the completed 16-lesson RAG Formation curriculum. The initial
release is text-first; video integration is explicitly deferred.

## Routes

Create one equivalent route per language:

- `/ai-lab/rag-formation/continue/01-improve-your-rag.html`
- `/fr/ai-lab/rag-formation/continue/01-improve-your-rag.html`
- `/zh/ai-lab/rag-formation/continue/01-improve-your-rag.html`

Each page will use a self-canonical URL and the reciprocal `en`, `fr`, `zh`,
and `x-default` alternates. `x-default` points to English.

## Page design and content

Follow the existing RAG Formation lesson shell: shared header, language
switcher, hero terminal, lesson sections, an interactive browser exercise,
and footer. The copy is localized per page and presents the same claims:

1. Capture reproducible interaction logs and user feedback first.
2. Explain the complementary roles of chunk-vector, summary-vector,
   keyword, and graph retrieval.
3. Triage production failures into retrieval, ranking, grounding/refusal,
   and follow-up failures before changing the system.
4. Scope a fix to one measured failure class, add a regression test, then
   rerun triage to verify the improvement.
5. Give an ordered baseline build plan for a four-channel, cited RAG.

The pages will not embed or link the supplied videos in this release. Any
meaningful visual material added later will carry localized alt text.

## Discovery and navigation

Add a dedicated RAG Formation Continue card below the existing 16-lesson
library on each localized RAG Formation roadmap. It will identify the lesson
as a supplementary field lesson, keeping the course’s "16 lessons complete"
claim intact. The lesson itself links back to the roadmap and treats this as
the first entry in the Continue series.

## Metadata, structured data, and sitemap

Each page will contain localized title, description, Open Graph, Twitter, and
`TechArticle` JSON-LD metadata; the series is a continuation lesson, not a
promise of enrollment or certification. The existing consent-aware GA4 block
will be retained verbatim. Add all three routes to `sitemap.xml` with a
2026-09-12 `lastmod` and matching four-way alternates.

## Verification

Run `python tests/ai-lab-localized-pages.py`, then extend or manually inspect
the localized Continue pages for language, reciprocal routes, metadata,
navigation, local assets, sitemap entries, and valid HTML links. Run the
static-server smoke test for the three new URLs.
