# AI Lab maintenance guide

This repository is a hand-authored static website. AI Lab pages must remain available in English, French, and Simplified Chinese.

## URL matrix

Each route family has one page per language:

| Page | English | Français | 中文 |
|---|---|---|---|
| Overview | `/ai-lab/` | `/fr/ai-lab/` | `/zh/ai-lab/` |
| RAG Engineer | `/ai-lab/rag-engineer/` | `/fr/ai-lab/rag-engineer/` | `/zh/ai-lab/rag-engineer/` |
| RAG Evaluation | `/ai-lab/rag-evaluation/` | `/fr/ai-lab/rag-evaluation/` | `/zh/ai-lab/rag-evaluation/` |
| RAG Formation | `/ai-lab/rag-formation/` | `/fr/ai-lab/rag-formation/` | `/zh/ai-lab/rag-formation/` |

## Page requirements

When creating or modifying an AI Lab page:

- Keep the correct `<html lang>` value: `en`, `fr`, or `zh-CN`.
- Write a unique, localized `<title>` and `<meta name="description">`.
- Use a self-referencing `<link rel="canonical">`.
- Include exactly four reciprocal alternates for the route family: `en`, `fr`, `zh`, and `x-default`. The `x-default` URL is the English page.
- Keep Open Graph metadata localized: `og:type`, `og:site_name`, `og:locale`, `og:url`, `og:title`, `og:description`, and `og:image`.
- Keep Twitter metadata present: `twitter:card`, `twitter:title`, `twitter:description`, and `twitter:image`.
- Add descriptive `alt` text to all meaningful images. Decorative images must use `alt=""` or `aria-hidden="true"`.
- Include JSON-LD appropriate to the page:
  - `CollectionPage` for the overview;
  - `TechArticle` for RAG Engineer and RAG Evaluation;
  - `Course` for RAG Formation.
- RAG Formation is a future course. Never imply that enrollment, certification, or course delivery is currently available. Keep its “in development” status in the visible copy and structured-data description.

## Google Analytics

All AI Lab pages use Google Analytics 4 measurement ID `G-S0YRBQKHLZ`.

The existing consent-aware snippet must appear in each page `<head>`:

- Load `https://www.googletagmanager.com/gtag/js?id=G-S0YRBQKHLZ` asynchronously.
- Set `analytics_storage` to `denied` by default.
- Also preserve the existing denied defaults for ad storage, ad user data, and ad personalization.
- Initialize with `gtag('js', new Date())` and `gtag('config', 'G-S0YRBQKHLZ')`.

Do not add a second analytics provider or bypass the consent default.

## Links and assets

- Use relative links and asset paths appropriate to the page depth.
- Language switches must point to the equivalent route, not to a language homepage.
- Keep the existing shared stylesheet at `assets/css/style.css` and script at `assets/js/main.js`.
- Keep RAG Engineer and RAG Evaluation GitHub links canonical:
  - `https://github.com/scheffershen/rag-engineer-skill`
  - `https://github.com/scheffershen/rag-evaluation-skill`

## Sitemap

Every AI Lab route must appear in `sitemap.xml`. Each of the 12 URL entries must include the four matching `xhtml:link` alternates (`en`, `fr`, `zh`, `x-default`). Update `lastmod` when page content changes.

## Translation rules

- French pages use professional French and preserve technical names such as RAG, MCP, Qdrant, and LightRAG.
- Chinese pages use Simplified Chinese and preserve product/project names and technical names.
- Keep project names `RAG Engineer`, `RAG Evaluation`, and `RAG Formation` unchanged.
- Translate navigation, calls to action, metadata, image alt text, status labels, and visible explanatory copy.
- Keep claims aligned across languages; do not add availability, results, or credentials to one language only.

## Verification

From the repository root, run:

```bash
python3 tests/ai-lab-localized-pages.py
```

The check validates all 12 pages, metadata, reciprocal alternates, analytics, structured data, local links/assets, RAG Formation status, and sitemap coverage. Also serve the repository locally and request all 12 routes, expecting HTTP 200 responses.
