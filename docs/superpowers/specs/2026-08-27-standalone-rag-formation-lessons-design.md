# Standalone RAG Formation Lessons

## Status

Approved design. Implementation begins only after the user reviews this written specification.

## Goal

Make every RAG Formation lesson self-contained on the SHEN YI website. A learner must be able to open any English, French, or Simplified Chinese lesson URL, read the complete lesson, complete browser-based checks, and continue through the course without visiting the GitHub repository.

## User decisions

- Use the existing website pages and URLs rather than introducing a separate course application.
- Port the full instructional content from `D:/Sandbox/4-rag-formation/lessons/`.
- Keep local reference cheat sheets from `D:/Sandbox/4-rag-formation/reference/`.
- Make exercises browser-based with immediate feedback.
- Do not persist answers or learner progress.
- Keep the lesson pages available in English, French, and Simplified Chinese.

## Scope

### In scope

- Update the existing 48 lesson pages: 16 lessons in each of EN, FR, and ZH.
- Preserve the current lesson URLs, language switchers, SEO metadata, analytics consent defaults, shared header/footer, and previous/next navigation.
- Replace overview-only lesson bodies with complete lesson content: outcomes, explanations, examples, tables, code snippets, deliverables, mission connections, and next actions.
- Remove GitHub lesson-source links and repository-dependent calls to action.
- Replace links to source-only files such as `MISSION.md` and `RESOURCES.md` with local website links or concise in-page explanations.
- Add local reference cheat sheets for each supported lesson language and update lesson links to use the matching locale.
- Add shared lesson styling to the existing stylesheet.
- Add a lesson-only JavaScript module for interactive checks.
- Add automated checks for lesson-page completeness, localization, local links, and GitHub-link absence.

### Out of scope

- Executing the Python RAG backend, Docker services, or live evaluation harness in the browser.
- Accounts, server-side learner progress, analytics for answers, or `localStorage` persistence.
- Introducing a new frontend framework or a build pipeline for the static site.
- Requiring external documentation to complete a lesson. Official external links may remain as optional further reading.

## Page architecture

Each page keeps the current site shell and uses the following lesson body structure:

1. Tangible outcome.
2. Core concept in plain language.
3. Guided engineering practice.
4. Examples, tables, and code snippets where useful.
5. Browser-based knowledge checks.
6. Deliverable or decision worksheet.
7. Mission connection and next lesson.

The source HTML lesson bodies are adapted into the existing SHEN YI visual system rather than embedded in an iframe or presented as a separate course site. The current course-in-development status remains visible and consistent with the RAG Formation page requirements.

## Interaction design

The new lesson script will use semantic quiz containers, buttons, and live feedback regions. Each quiz will:

- provide immediate correct/incorrect feedback;
- disable its choices after an answer;
- expose feedback through `aria-live`;
- reset naturally when the page is reloaded;
- avoid cookies, `localStorage`, accounts, and server calls.

Decision worksheets remain transient browser inputs. Learners can copy their notes manually, but the site does not save them.

Command examples such as `python3 eval.py ...` remain useful engineering documentation. They are not presented as browser-executable requirements; the required checks on the website are the interactive scenario and reasoning exercises.

## Localization

The English source material is the content reference. French and Simplified Chinese pages receive complete localized instructional copy rather than only translated headings. Technical names remain unchanged where appropriate, including RAG, Qdrant, Meilisearch, LightRAG, SOP, and MVP. Claims, course status, lesson numbering, and learning outcomes remain aligned across locales.

Reference pages use the same locale structure as the lessons. Relative links are calculated for their page depth and all meaningful images retain descriptive alternative text.

## File layout

- `assets/css/style.css` — shared lesson layout and interaction styles.
- `assets/js/lesson.js` — lesson-only quiz and transient worksheet behavior.
- `ai-lab/rag-formation/lessons/` — English lesson pages.
- `fr/ai-lab/rag-formation/lessons/` — French lesson pages.
- `zh/ai-lab/rag-formation/lessons/` — Simplified Chinese lesson pages.
- `ai-lab/rag-formation/reference/` — English reference pages.
- `fr/ai-lab/rag-formation/reference/` — French reference pages.
- `zh/ai-lab/rag-formation/reference/` — Simplified Chinese reference pages.
- `tests/ai-lab-lesson-pages.py` — automated lesson and reference validation.

Existing user changes in unrelated files, including the current sitemap and lesson assets, are preserved.

## Navigation and links

Lesson pages continue to link to:

- the course roadmap;
- the AI Lab overview;
- the previous lesson, when present;
- the next lesson, when present;
- the matching local reference page, when relevant.

No lesson page may contain a GitHub URL or depend on a repository-only Markdown file. Optional external primary-reading links can remain clearly secondary to the in-page lesson.

## Validation

Implementation is complete only when all of the following have fresh evidence:

- the lesson checker passes all 48 lesson pages and their local references;
- every lesson has the expected language, canonical URL, reciprocal alternates, development status, lesson navigation, and interactive exercise markup;
- no lesson page contains a GitHub URL;
- all local lesson/reference links resolve to files;
- `git diff --check` passes;
- the static HTTP smoke test returns HTTP 200 for every lesson and reference route;
- browser interaction checks confirm feedback appears and choices disable after selection;
- the existing `tests/ai-lab-localized-pages.py` command is run and any unrelated pre-existing failure is reported separately.

## Risks and mitigations

- **Large duplicated HTML surface:** Keep the lesson structure consistent and validate all locales with one checker.
- **Translation drift:** Use the English lesson as the content baseline and compare outcomes, phase labels, and claims across locales.
- **Broken relative links:** Validate every local `href` against the page’s filesystem location.
- **Static-site limitations:** Make browser exercises self-contained and label backend commands as optional local engineering practice.
- **Accessibility regressions:** Use semantic controls, keyboard-operable buttons, and `aria-live` feedback.
