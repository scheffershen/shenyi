---
version: alpha
name: "Shen Yi — Full-Stack & AI Portfolio"
description: "Light-only freelance developer portfolio. Emerald-led, evidence-focused, frosted-glass surfaces, one self-contained dark terminal component."
colors:
  bg: "#f7f9fc"
  bg-deep: "#eef1f6"
  surface: "rgba(15, 23, 42, 0.035)"
  surface-2: "rgba(15, 23, 42, 0.06)"
  border: "rgba(15, 23, 42, 0.10)"
  border-strong: "rgba(15, 23, 42, 0.18)"
  text: "#0f172a"
  text-dim: "#45536b"
  text-faint: "#5b6b84"
  primary: "#047857"
  primary-bright: "#34d399"
  primary-deep: "#10b981"
  on-primary: "#052b1e"
  secondary: "#0e7490"
  secondary-bright: "#22d3ee"
  tertiary: "#b45309"
  tertiary-bright: "#fbbf24"
  on-tertiary: "#3a2708"
  tag-fill: "rgba(255, 255, 255, 0.028)"
  metric-tint: "rgba(52, 211, 153, 0.055)"
  icon-tint: "rgba(52, 211, 153, 0.09)"
  icon-tint-amber: "rgba(251, 191, 36, 0.1)"
  availability-tint: "rgba(52, 211, 153, 0.07)"
  header-bg: "rgba(247, 249, 252, 0.72)"
  menu-bg: "rgba(255, 255, 255, 0.97)"
  drawer-bg: "rgba(255, 255, 255, 0.985)"
  field-bg: "#ffffff"
  on-skip: "#06281c"
  globe-emerald: "rgba(52, 211, 153, 0.07)"
  globe-cyan: "rgba(34, 211, 238, 0.09)"
  terminal-surface-top: "rgba(19, 29, 51, 0.95)"
  terminal-surface-bottom: "rgba(12, 20, 37, 0.95)"
  terminal-text: "#e8eefa"
  terminal-dim: "#93a4bf"
  terminal-faint: "#6b7d99"
typography:
  display:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 3rem
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.035em
  headline:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 2.25rem
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.02em
  title-card:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 1.2rem
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.02em
  body-lg:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 1.125rem
    fontWeight: "400"
    lineHeight: 1.65
  body:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 1rem
    fontWeight: "400"
    lineHeight: 1.65
  body-sm:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 0.95rem
    fontWeight: "400"
    lineHeight: 1.55
  label-eyebrow:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
    fontSize: 0.78rem
    fontWeight: "500"
    letterSpacing: 0.14em
  label-mono:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
    fontSize: 0.72rem
    fontWeight: "600"
    letterSpacing: 0.1em
  tag:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
    fontSize: 0.71rem
    fontWeight: "400"
  price:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
    fontSize: 1.02rem
    fontWeight: "600"
  metric-number:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
    fontSize: 1.5rem
    fontWeight: "600"
    letterSpacing: -0.02em
  button:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 1rem
    fontWeight: "600"
  form-label:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    fontSize: 0.83rem
    fontWeight: "600"
    letterSpacing: 0.01em
  font-sans:
    fontFamily: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
  font-cjk:
    fontFamily: '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif'
  font-mono:
    fontFamily: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
rounded:
  sm: 10px
  DEFAULT: 16px
  chip: 6px
  tile: 12px
  full: 999px
spacing:
  unit: 8px
  gap: 1.15rem
  wrap-max: 1200px
  section-y: 7.5rem
  card-padding: 1.9rem
  tap-target: 48px
  header-height: 4.5rem
  section-head-max: 46rem
components:
  page:
    backgroundColor: "linear-gradient(180deg, {colors.bg} 0%, {colors.bg-deep} 100%)"
  header:
    backgroundColor: "{colors.header-bg}"
    height: 4.5rem
  brand-mark:
    backgroundColor: "linear-gradient(135deg, {colors.primary-bright} 0%, {colors.secondary-bright} 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.font-mono}"
    rounded: "{rounded.sm}"
    size: 2.15rem
  nav-link:
    textColor: "{colors.text-dim}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0.6rem 0.85rem
  lang-menu:
    backgroundColor: "{colors.menu-bg}"
    rounded: "{rounded.sm}"
    padding: 0.4rem
  drawer:
    backgroundColor: "{colors.drawer-bg}"
  btn-primary:
    backgroundColor: "linear-gradient(135deg, {colors.primary-bright} 0%, {colors.primary-deep} 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0.85rem 1.5rem
    height: 48px
  btn-ghost:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0.85rem 1.5rem
    height: 48px
  btn-ghost-hover:
    backgroundColor: "{colors.surface-2}"
  btn-block:
    width: 100%
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.DEFAULT}"
    padding: 1.9rem
  card-hover:
    backgroundColor: "{colors.surface-2}"
  card-featured:
    backgroundColor: "linear-gradient(180deg, rgba(251, 191, 36, 0.055), {colors.surface})"
    rounded: "{rounded.DEFAULT}"
    padding: 1.9rem
  card-flag:
    backgroundColor: "{colors.tertiary-bright}"
    textColor: "{colors.on-tertiary}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.full}"
    padding: 0.2rem 0.65rem
  card-icon:
    backgroundColor: "{colors.icon-tint}"
    textColor: "{colors.primary}"
    rounded: "{rounded.tile}"
    size: 2.85rem
  card-icon-featured:
    backgroundColor: "{colors.icon-tint-amber}"
    textColor: "{colors.tertiary}"
  card-price:
    textColor: "{colors.primary}"
    typography: "{typography.price}"
  card-price-featured:
    textColor: "{colors.tertiary}"
  card-index:
    textColor: "{colors.text-faint}"
    typography: "{typography.label-mono}"
  tag:
    backgroundColor: "{colors.tag-fill}"
    textColor: "{colors.text-dim}"
    typography: "{typography.tag}"
    rounded: "{rounded.chip}"
    padding: 0.3rem 0.62rem
  metric-callout:
    backgroundColor: "{colors.metric-tint}"
    textColor: "{colors.text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0.9rem 1rem
  eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.label-eyebrow}"
  section-title:
    typography: "{typography.headline}"
  section-sub:
    textColor: "{colors.text-dim}"
    typography: "{typography.body}"
  hero-display:
    typography: "{typography.display}"
  hero-sub:
    textColor: "{colors.text-dim}"
    typography: "{typography.body-lg}"
  hero-proof-number:
    textColor: "{colors.primary}"
    typography: "{typography.metric-number}"
  hero-availability:
    backgroundColor: "{colors.availability-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.full}"
    padding: 0.45rem 0.9rem
  skip-link:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-skip}"
    typography: "{typography.button}"
    padding: 0.75rem 1.25rem
  form-field:
    backgroundColor: "{colors.field-bg}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 0.8rem 0.95rem
    height: 48px
  form-label:
    textColor: "{colors.text-dim}"
    typography: "{typography.form-label}"
  form-note:
    textColor: "{colors.text-faint}"
    typography: "{typography.body-sm}"
  direct-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    rounded: "{rounded.sm}"
    padding: 1rem 1.15rem
  footer-link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-dim}"
    rounded: "{rounded.sm}"
    size: 48px
  stack-group-heading:
    textColor: "{colors.secondary}"
    typography: "{typography.label-mono}"
  globe:
    backgroundColor: "radial-gradient(34rem 20rem at 88% 12%, {colors.globe-cyan}, transparent 65%), linear-gradient(135deg, {colors.globe-emerald}, {colors.surface})"
  terminal:
    backgroundColor: "linear-gradient(180deg, {colors.terminal-surface-top} 0%, {colors.terminal-surface-bottom} 100%)"
    textColor: "{colors.terminal-text}"
    typography: "{typography.font-mono}"
    rounded: "{rounded.DEFAULT}"
  terminal-body:
    textColor: "{colors.terminal-dim}"
  terminal-prompt:
    textColor: "{colors.primary-bright}"
  terminal-key:
    textColor: "{colors.secondary-bright}"
  terminal-num:
    textColor: "{colors.tertiary-bright}"
  terminal-faint:
    textColor: "{colors.terminal-faint}"
---

## Overview

This is the design system for **shenyi.dev**, a freelance developer portfolio positioned as production-engineering credibility rather than agency marketing gloss. The tone is technical and evidence-led: real numbers, source-cited claims, terminal-style data readouts, and NDA-anonymized case studies presented like production postmortems, not sales copy.

The system is deliberately **light-only** — no dark-mode toggle. The one intentional exception is the `.terminal` component, which stays a dark console regardless of page theme, the same way a code block stays dark in an otherwise light-themed documentation site. A faint, fixed radial-gradient "ambient glow" (emerald + cyan, near-transparent) sits behind all content to keep the flat light background from feeling sterile, without competing with foreground content.

Visual restraint is the operating principle: one structural accent hue (emerald), one secondary hue (cyan) used sparingly, and one tertiary hue (amber) reserved exclusively for "featured/highlighted" flags. No gratuitous color, no heavy resting shadows, no dark-mode variants to maintain.

## Colors

Every hue in this system exists as **two shades**, and the split is deliberate:

- An **ink-safe shade** (`primary` `#047857`, `secondary` `#0e7490`, `tertiary` `#b45309`) — AA-contrast-safe on the light background. This is what nearly every *foreground* use (body text, icons, links, eyebrow labels, metric highlights) resolves to.
- A **bright/saturated shade** (`primary-bright` `#34d399`, `secondary-bright` `#22d3ee`, `tertiary-bright` `#fbbf24`) — used only for *solid fills* where vividness matters more than text contrast: button backgrounds, badges, status dots, the brand mark, the ambient glow.

`primary` (emerald) is the workhorse accent: CTAs, focus rings, section eyebrows, link color, hero headline gradient, metric-callout highlights. `secondary` (cyan) appears sparingly, mainly as the second stop in the hero headline gradient and the brand-mark gradient — never as a standalone CTA color. `tertiary` (amber) is reserved exclusively for the "featured" card variant and its flag; introducing amber anywhere else dilutes its signal value.

Neutrals are cool-toned and layered by opacity rather than by distinct hex steps: `surface`/`surface-2` are near-transparent dark overlays (`rgba(15,23,42,·)`) over the `bg`/`bg-deep` gradient, so every "card" is really the background showing through a frosted layer, not a separately-painted panel. Text has three steps only — `text` (near-black ink), `text-dim`, `text-faint` — and a `prefers-contrast: more` media query darkens `text-dim`/`text-faint`/`border` for users who need it.

> **On lint findings:** every translucent token in this palette (all `rgba(15,23,42,·)` surfaces, every `*-tint`, the terminal gradient stops) is composited over the light `bg` `#f7f9fc` before reaching the eye — a `surface` card renders as ≈`#f7f8fa` with `text` `#0f172a` ink (~15.9:1 contrast). A contrast checker that treats the raw `rgba` as opaque will under-report these. The same goes for colors referenced only inside gradient strings (`page`, `btn-primary`, `globe`, `terminal`): they resolve correctly but appear "orphaned" to naive token scanners. None of these warnings indicate a real contrast or usage defect.

## Typography

Latin copy uses **Inter** (with Plus Jakarta Sans / system-ui fallbacks); pages under `/zh/` switch the entire body to a **CJK-first stack** (`font-cjk`: PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans SC — system fonts, no webfont download) and drop the `-0.02em` heading letter-spacing, which reads as tightness/kerning artifacts in Chinese type. **JetBrains Mono** (`font-mono`) is the deliberate "data" voice: eyebrow labels, tags, metric numbers, the terminal widget, and anything meant to read as a technical/measured fact rather than prose.

The type scale is **fluid** throughout via `clamp()` — the token values above are the representative desktop sizes, while the exact CSS expressions are:

| Token | Fluid expression |
|:--|:--|
| `display` (hero H1) | `clamp(2.15rem, 1.15rem + 4.4vw, 4rem)` |
| `headline` (section H2) | `clamp(1.85rem, 1.2rem + 2.6vw, 2.9rem)` |
| `title-card` (card H3) | `clamp(1.12rem, 1.05rem + 0.35vw, 1.3rem)` |
| `body-lg` (hero sub) | `clamp(1.05rem, 1rem + 0.32vw, 1.22rem)` |
| `body` (page text) | `clamp(1rem, 0.97rem + 0.15vw, 1.075rem)` |
| terminal body | `clamp(0.72rem, 0.63rem + 0.42vw, 0.86rem)` |
| hero proof numbers | `clamp(1.25rem, 1rem + 1vw, 1.75rem)` |

Headings are tight (`-0.02em` to `-0.035em` letter-spacing, weight 700); body copy is loose (`line-height: 1.65`) for long-form readability. The hero headline uses a two-color `background-clip: text` gradient (`primary → secondary`) on a `<span>` for its emphasis word — the only place text itself carries a gradient.

## Layout

Content is capped at a **1200px** `wrap` max-width, centered, with fluid inline padding (`clamp(1.15rem, 4vw, 2.5rem)`). Vertical rhythm between sections is a single fluid token (`section-y: clamp(4rem, 9vw, 7.5rem)` — the YAML value is the upper bound) rather than per-section overrides, so spacing stays proportional across the whole page at any viewport. Card padding is likewise fluid (`clamp(1.4rem, 3.5vw, 1.9rem)`).

Grids are mobile-first and only ever *add* columns at breakpoints: the portfolio grid is `grid-2` (two columns at 680px+, single column below); `grid-4` (services) and `stack-grid` (3 columns) and the hero / contact split appear at 1024px+; the globe splits into two columns at 900px+. Cards are allowed to end a row unpaired rather than forcing an artificial even count. Every interactive target respects a `48px` minimum tap size (`tap-target`), enforced even inside dense header/nav elements, and the sticky header reserves `scroll-padding-top: 5.5rem` so anchor jumps clear it.

## Elevation & Depth

Depth comes from **translucency and blur**, not shadow stacking. Cards, the sticky header, and dropdown menus are `rgba(15,23,42,low-alpha)` panels with `backdrop-filter: blur()` (8px for cards, 14–18px for header/drawer/dropdown) — they read as frosted glass over the ambient gradient, not opaque painted surfaces. Box-shadow is reserved for **interactive/hover states only**: cards and primary buttons are flat at rest and gain a soft, diffused, negative-spread shadow (`box-shadow: 0 22px 48px -22px rgba(15,23,42,0.18)` cards / `0 14px 34px rgba(16,185,129,0.38)` primary button) plus a `translateY(-2px to -4px)` lift on hover — nothing casts a shadow while idle. Floating overlays that must separate themselves (language menu `0 18px 44px rgba(15,23,42,0.16)`) are the one exception.

The one deliberately "heavier" surface is `.terminal`: a genuinely dark, high-contrast panel with its own self-contained color tokens (`terminal-*`, not the page's light-theme variables) and a real resting shadow (`0 30px 70px -20px rgba(15,23,42,0.35)`), styled like an embedded code block/screenshot rather than a UI panel that must match the surrounding chrome.

## Shapes

Two structural radii cover almost everything: `rounded.sm` (10px) for anything interactive or input-like (buttons, form fields, dropdown items, nav links), and `rounded.DEFAULT` (16px) for containers (cards, the terminal, the globe/stack panels). Below that, small ad hoc radii exist for specific chip-like elements — `chip` (6px, tags) and `tile` (12px, the card icon square) — and above it, `full` (999px) produces pills (badges, the hubs badge, availability indicator) while `50%` produces true circles (avatar, status dot, traffic-light dots in the terminal bar). There is no radius scale beyond these five values — do not introduce a new one-off radius for a new component.

## Components

**Buttons** — `btn-primary` is a solid emerald gradient fill (`primary-bright → primary-deep`) with dark ink text (`on-primary`) and a colored ambient shadow that intensifies on hover; `btn-ghost` is a translucent `surface` fill with a `border-strong` outline (`btn-ghost-hover` deepens to `surface-2`), used for secondary actions. Both share the same size, `rounded.sm` radius, `height: 48px`, and weight-600 label so they read as one family at different emphasis levels. `btn-block` stretches to full width for forms and drawers.

**Cards** — the base unit for services and portfolio items: frosted `surface` panel, `border`, `rounded.DEFAULT`, lifting on hover (`card-hover`). `card-featured` is the *only* variant, swapping the accent from emerald to amber (border, icon tile, price color) and adding a subtle amber-tinted top gradient — reserved for a single highlighted offer, never used decoratively. `card-flag` is the pill badge pinned to the featured card's top edge (`tertiary-bright` fill, `on-tertiary` text).

**Tags** — mono-font, low-contrast chips (`tag-fill` over the background, `text-dim`) used for tech-stack lists; deliberately quiet so they don't compete with card copy.

**Metric callouts** — the signature "proof" element on portfolio cards: an emerald-tinted inset box (`metric-callout`) pairing an icon with a bolded, ink-safe-emerald number/fact. This is the only place body text is allowed to carry heavy inline color emphasis (bold → `primary`).

**Eyebrow labels** — mono, uppercase, letter-spaced, emerald, prefixed by a short horizontal rule — the section-kicker pattern used above every `section-title`.

**Terminal** — the self-contained dark-console widget described under Elevation & Depth; its own semantic color roles (`terminal-prompt`, `terminal-key`, `terminal-num`, `terminal-body`, `terminal-faint`) map directly to `primary-bright` / `secondary-bright` / `tertiary-bright` / `terminal-dim` / `terminal-faint`, mirroring the page's primary/secondary/tertiary hues one level down.

**Forms** — `form-field` inputs are solid white (`field-bg`) with `border-strong` and a 3px emerald focus ring; `form-label` is small weight-600 text, required markers in `primary`. A honeypot `_gotcha` field is visually hidden from users *and* assistive tech (unlike `.sr-only`) to trap spam bots.

**Chrome** — `header` is a frosted sticky bar (`header-bg` at 72%, 14px blur) that gains a border when stuck; `brand-mark` is a `primary-bright → secondary-bright` gradient tile with mono initials; `lang-menu` / `drawer` are near-opaque white panels with heavy blur; `footer-link` and `direct-link` are quiet `surface` icon/contact tiles; `stack-group-heading` uses cyan (`secondary`) as its mono label color to differentiate the tech-stack section; `globe` carries the emerald→cyan ambient gradient inside its own panel; `skip-link` is the one `primary-bright` solid used for accessibility.

## Do's and Don'ts

- **Do** use the ink-safe shade (`primary`/`secondary`/`tertiary`) for any foreground use — text, icons, borders-with-meaning. **Don't** use the bright shades for text; they fail contrast on the light background by design.
- **Do** keep `tertiary`/amber exclusive to the "featured" flag and its card variant. **Don't** spend amber on anything else — its entire value is signaling "this one is different."
- **Do** treat `secondary`/cyan as a rare second note (gradient stops, brand mark) — never a standalone CTA or link color. **Don't** promote it to a primary action color.
- **Do** build elevation with translucency + `backdrop-filter` blur, reserving box-shadow for hover/interactive states. **Don't** add resting drop-shadows to cards, buttons, or panels — it breaks the flat/frosted language.
- **Do** use `font-mono` for anything data-like (numbers, tags, labels, terminal). **Don't** set prose or headings in mono — it's a data/label signal, not a display font.
- **Do** reuse `rounded.sm` (interactive) / `rounded.DEFAULT` (containers) for any new component. **Don't** invent a new one-off border-radius value.
- **Do** let the CJK stack (`font-cjk`, `/zh/` pages) take over the whole body font and drop heading letter-spacing. **Don't** force the Latin `font-sans` stack or negative letter-spacing onto Chinese copy — it degrades legibility and kerns oddly.
- **Do** keep the site light-only, with `.terminal` as the sole self-contained dark exception. **Don't** add a site-wide dark-mode toggle or theme new components with a second, separate dark palette.
- **Do** keep the type scale fluid via `clamp()` (see the Typography table for the canonical expressions). **Don't** freeze type or spacing at fixed breakpoint jumps — continuous fluid scaling is part of the system's identity.
