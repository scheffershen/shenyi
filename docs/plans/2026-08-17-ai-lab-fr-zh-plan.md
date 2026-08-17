# Localized AI Lab Homepage Sections Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add localized AI Engineering Lab navigation and homepage sections to `/fr/` and `/zh/`, linking to the existing AI Lab project pages without changing the English homepage.

**Architecture:** Modify only the two localized static HTML entrypoints. Reuse the English homepage section structure, existing `.ai-lab-*` CSS classes, existing images, and relative links from each language directory. Add a small repository-local verification script so the required navigation, section, localized copy, image references, and destination links are checked deterministically.

**Tech Stack:** Static HTML, existing CSS/JavaScript, PowerShell verification script.

---

### Task 1: Add a failing localization verification test

**Files:**
- Create: `tests/ai-lab-localization.ps1`

**Step 1: Write the failing test**

Create assertions for both `fr/index.html` and `zh/index.html` that require:
- an `href="#ai-lab"` desktop navigation link;
- an `href="#ai-lab"` mobile navigation link;
- exactly one `id="ai-lab"` section;
- all three existing AI Lab route links under the localized pages;
- all three AI Lab image paths;
- localized section headings/status text.

**Step 2: Run the test to verify it fails**

Run:
```powershell
pwsh -File tests/ai-lab-localization.ps1
```

Expected: FAIL because the localized pages do not yet contain the AI Lab navigation and section.

### Task 2: Add localized AI Lab navigation

**Files:**
- Modify: `fr/index.html`
- Modify: `zh/index.html`

**Step 1: Add the desktop navigation entry**

Insert an AI Lab link between portfolio and tech stack, targeting `#ai-lab`, with localized labels:
- French: `Laboratoire d’ingénierie IA`
- Chinese: `AI 工程实验室`

**Step 2: Add the mobile navigation entry**

Insert the matching link in each drawer and keep numbering sequential.

### Task 3: Add the French homepage section

**Files:**
- Modify: `fr/index.html`

**Step 1: Insert the section after the portfolio section**

Reuse the English section’s `section`, `section-head`, `ai-lab-method`, `ai-lab-grid`, `card`, `ai-lab-card`, and `card-featured` structure with `id="ai-lab"`.

**Step 2: Localize the content**

Use French copy for:
- the eyebrow, heading, and supporting paragraph;
- BUILD / MESURER / APPRENDRE methodology labels;
- card statuses, titles, descriptions, alt text, and calls to action;
- the future-course label, without implying the course is currently available.

Keep project names `RAG Engineer`, `RAG Evaluation`, and `RAG Formation`, plus technical product names, unchanged.

**Step 3: Set correct relative links**

Use:
- `../ai-lab/rag-engineer/`
- `../ai-lab/rag-evaluation/`
- `../ai-lab/rag-formation/`

### Task 4: Add the Chinese homepage section

**Files:**
- Modify: `zh/index.html`

**Step 1: Insert the section after the portfolio section**

Use the same structure and existing CSS classes as the English and French sections.

**Step 2: Localize the content**

Use Simplified Chinese copy for the eyebrow, heading, supporting text, methodology labels, card statuses, titles, descriptions, alt text, and calls to action. Keep project names and technical names unchanged.

**Step 3: Set correct relative links**

Use the same three `../ai-lab/.../` routes relative to `/zh/`.

### Task 5: Run verification and inspect the diff

**Files:**
- Verify: `fr/index.html`, `zh/index.html`, `tests/ai-lab-localization.ps1`

**Step 1: Run the localization test**

Run:
```powershell
pwsh -File tests/ai-lab-localization.ps1
```

Expected: PASS for both localized pages.

**Step 2: Check the changed-file scope**

Run:
```bash
git diff --stat -- fr/index.html zh/index.html tests/ai-lab-localization.ps1
```

Confirm no English homepage, CSS, image, or unrelated file changes were introduced.

**Step 3: Validate route references**

Run:
```bash
rg -n 'ai-lab|rag-engineer|rag-evaluation|rag-formation' fr/index.html zh/index.html
```

Confirm each language has two `#ai-lab` nav targets, one section, three cards, and three image/link destinations.
