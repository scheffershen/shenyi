# AI Lab section for French and Chinese homepages

## Goal

Expose the existing AI Engineering Lab from the French (`/fr/`) and Chinese (`/zh/`) homepages with localized navigation and section copy. The English homepage and the existing AI Lab detail pages remain unchanged.

## Design

- Add an AI Lab anchor to each homepage's desktop and mobile navigation.
- Insert a localized `<section id="ai-lab">` after the portfolio and before the global hubs/locations section, matching the English section's structure and existing CSS classes.
- Keep the existing project names and destination URLs:
  - `../ai-lab/rag-engineer/` from `/fr/` and `/zh/`
  - `../ai-lab/rag-evaluation/`
  - `../ai-lab/rag-formation/`
- Translate all user-facing section text, status labels, card descriptions, calls to action, and image alternative text into French and Simplified Chinese.
- Reuse the existing AI Lab imagery, `.ai-lab-*` styles, reveal behavior, and featured course treatment; no CSS changes are expected.

## Content direction

French uses “Laboratoire d’ingénierie IA”, with concise professional copy around building reliable RAG systems, evidence-based evaluation, and a 30-day learning path. Chinese uses “AI 工程实验室”, with equivalent terminology familiar to technical Chinese readers. Proper project names and technical names such as RAG, MCP, and LightRAG remain unchanged.

## Verification

- Confirm each localized page has desktop and mobile AI Lab links targeting `#ai-lab`.
- Confirm each localized page has one `id="ai-lab"` section with three cards and correct relative links.
- Confirm the English homepage and stylesheet are unchanged by this feature.
- Run available repository checks and inspect the diff for accidental edits.
