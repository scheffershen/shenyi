# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static, zero-build personal/freelance portfolio site for **SHEN YI** (shenyi.dev) — no framework, no bundler, no package.json. Plain HTML, one CSS file, one JS file, deployed as-is (GitHub Pages style, note `.nojekyll`).

## Commands

There is no build step. To preview locally:

```bash
python -m http.server 8123 --directory .
```

(A pre-configured launch entry named `static` already does this — see `.claude/launch.json` — point the preview browser tool at it instead of starting your own server.)

There is no automated test runner wired into CI. Verification is done with small **repository-local PowerShell assertion scripts** that regex/string-match against the built HTML files (see `tests/portfolio-project-08.ps1` for the pattern: assert a marker string appears exactly once, required tags exist, and forbidden identifiers are absent). Run one with:

```bash
pwsh -File tests/<script>.ps1
```

When adding a new page section or localized page, follow this repo's existing convention (see `docs/plans/2026-08-17-ai-lab-fr-zh-plan.md`) of writing a small assertion script *first* that checks nav links, section ids, required copy, and image/link destinations across all three locales, then implementing until it passes.

**Important:** `tests/` and `docs/` are listed in `.gitignore`, but files already inside them are tracked (gitignore only blocks *new* untracked files from being picked up by a bare `git add`). If you add a new file under `tests/` or `docs/`, you must `git add -f` it or it will silently stay untracked.

## Architecture

### Trilingual static mirror, not an i18n framework

There is no templating or string-extraction system. Each locale is a **fully self-contained HTML file** that must be edited independently:

- `index.html` — English (canonical, at the site root)
- `fr/index.html` — French
- `zh/index.html` — Simplified Chinese

All three share the same DOM structure, section order, and CSS classes (`section`, `card`, `ai-lab-card`, `hero-grid`, etc.) — only text content, `hreflang`/`lang` attributes, and relative paths differ (root pages use `assets/...`; `fr/`/`zh/` use `../assets/...`). When changing one locale's markup/behavior, **mirror the structural change into the other two** unless the task is explicitly locale-scoped (e.g. a French-only copy fix). English-only content changes are the norm for net-new features until they're explicitly localized (see the AI Lab section's rollout: added to `index.html` first, localized into `fr/`/`zh/` in a later commit).

`zh/` pages switch the whole body to the CJK font stack (`font-cjk` in `DESIGN.md`) and drop heading letter-spacing — don't force the Latin `font-sans` stack onto Chinese copy.

Each locale's `<head>` carries the full set of `hreflang` alternates (`en`/`fr`/`zh`/`x-default`) and per-locale Open Graph/Twitter meta — keep these in sync (canonical URL, og:locale, og:locale:alternate) when adding a page.

### Standalone sub-pages

`ai-lab/index.html` and its three children (`ai-lab/rag-engineer/`, `ai-lab/rag-evaluation/`, `ai-lab/rag-formation/`) are separate pages linked from (not templated by) the homepage's `#ai-lab` section. They reuse the same header/drawer/footer chrome and CSS classes as the homepage, hand-copied rather than shared via includes. `privacy/index.html` (and its `fr/privacy/`, `zh/privacy/` counterparts) follow the same standalone-but-consistent-chrome pattern.

### One CSS file, organized by component

`assets/css/style.css` (~1260 lines) is a single stylesheet with no preprocessor, sectioned by comment headers in this order: Tokens (`:root`) → Utilities → Section furniture → Header → Language switcher → Mobile drawer → Buttons → Hero → Terminal → Cards → AI Engineering Lab → Global hubs banner → Tech stack → Contact → Footer → Cookie consent banner → Policy/legal content → Scroll reveal → Motion/contrast preferences → Print. Responsive breakpoints are mobile-first `min-width` queries (480/680/900/1024/1280px) grouped near the bottom, not interleaved per-component. Follow this same layout when adding a new component's styles: define tokens (if new) at the top, add the component's rules in a clearly commented section near related components, add breakpoint overrides in the shared media-query blocks.

**Design system is documented in `DESIGN.md`** — read it before touching colors, spacing, radii, or typography. Key constraints: light-only (no dark-mode toggle, `.terminal` is the sole intentional dark exception), fluid type via `clamp()` (don't freeze sizes at fixed breakpoints), only two border-radius tokens for almost everything (`rounded.sm` interactive, `rounded.DEFAULT` containers), amber (`tertiary`) reserved exclusively for the "featured" card variant, elevation via translucency/blur rather than resting box-shadows.

### JS is a single deferred, dependency-free enhancement script

`assets/js/main.js` is intentionally unbundled vanilla JS covering: sticky header shadow, mobile drawer, language-switcher dropdown, terminal line-reveal animation, IntersectionObserver-based scroll reveal (with a 2s failsafe that force-shows content if the observer never fires — treat "observer breaks" as "show the content," never "hide it"), GA4 Consent Mode cookie banner, and footer year. The site must remain fully readable/navigable with this script absent — it only ever adds classes/behavior, never renders required content. If you add JS-dependent UI, follow this same progressive-enhancement contract and mirror any new listener setup across all three locale pages if the feature is homepage-wide.

### Privacy/anonymization constraint

Some portfolio case studies (e.g. the "Internal Enterprise Platform" project) describe work done for the site owner's employer under an NDA-style constraint: **never introduce the employer's real name or identifying strings** (see the `$forbiddenIdentifiers` check in `tests/portfolio-project-08.ps1` — currently `Universal Medica`, `UMP`, `universalmedica.com`). If asked to add or edit anonymized case-study content, keep it generic/anonymized and check it doesn't reintroduce a real employer identifier, consistent with existing assertion scripts.

### Analytics/consent

Google Analytics (gtag.js, `G-S0YRBQKHLZ`) is loaded with **Consent Mode default-denied**; the cookie banner (`#consentBanner`) only flips `analytics_storage` to `granted` on explicit user action, persisted in `localStorage` under `consent_analytics`. Don't change consent defaults to granted-by-default, and keep the "manage preferences" footer reopen affordance (`[data-consent-manage]`) working if you touch this flow.
