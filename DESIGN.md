---
name: Shen Yi — Full-Stack & AI Portfolio
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
  terminal-surface-top: "rgba(19, 29, 51, 0.95)"
  terminal-surface-bottom: "rgba(12, 20, 37, 0.95)"
  terminal-text: "#e8eefa"
  terminal-dim: "#93a4bf"
  terminal-faint: "#6b7d99"
  terminal-accent: "{colors.primary-bright}"
  terminal-secondary: "{colors.secondary-bright}"
  terminal-tertiary: "{colors.tertiary-bright}"
typography:
  display:
    fontFamily: "{typography.font-sans}"
    fontSize: clamp(2.15rem, 1.15rem + 4.4vw, 4rem)
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.035em
  headline:
    fontFamily: "{typography.font-sans}"
    fontSize: clamp(1.85rem, 1.2rem + 2.6vw, 2.9rem)
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.02em
  title-card:
    fontFamily: "{typography.font-sans}"
    fontSize: clamp(1.12rem, 1.05rem + 0.35vw, 1.3rem)
    fontWeight: "700"
    lineHeight: 1.15
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "{typography.font-sans}"
    fontSize: clamp(1.05rem, 1rem + 0.32vw, 1.22rem)
    fontWeight: "400"
    lineHeight: 1.65
  body:
    fontFamily: "{typography.font-sans}"
    fontSize: clamp(1rem, 0.97rem + 0.15vw, 1.075rem)
    fontWeight: "400"
    lineHeight: 1.65
  body-sm:
    fontFamily: "{typography.font-sans}"
    fontSize: 0.95rem
    fontWeight: "400"
    lineHeight: 1.55
  label-eyebrow:
    fontFamily: "{typography.font-mono}"
    fontSize: 0.78rem
    fontWeight: "500"
    letterSpacing: 0.14em
    textTransform: uppercase
  label-mono:
    fontFamily: "{typography.font-mono}"
    fontSize: 0.72rem
    fontWeight: "600"
    letterSpacing: 0.1em
  tag:
    fontFamily: "{typography.font-mono}"
    fontSize: 0.71rem
    fontWeight: "400"
  button:
    fontFamily: "{typography.font-sans}"
    fontSize: 1rem
    fontWeight: "600"
  font-sans: '"Inter", "Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
  font-cjk: '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif'
  font-mono: '"JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
rounded:
  sm: 10px
  DEFAULT: 16px
  chip: 6px
  tile: 12px
  full: 999px
spacing:
  unit: 8px
  wrap-max: 1200px
  section-y: clamp(4rem, 9vw, 7.5rem)
  card-padding: clamp(1.4rem, 3.5vw, 1.9rem)
  tap-target: 48px
components:
  btn-primary:
    backgroundColor: "linear-gradient(135deg, {colors.primary-bright} 0%, {colors.primary-deep} 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 0.85rem 1.5rem
    boxShadow: 0 8px 26px rgba(16, 185, 129, 0.28)
  btn-primary-hover:
    boxShadow: 0 14px 34px rgba(16, 185, 129, 0.38)
  btn-ghost:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.text}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
    rounded: "{rounded.DEFAULT}"
    padding: "{spacing.card-padding}"
    backdropBlur: 8px
  card-hover:
    backgroundColor: "{colors.surface-2}"
    borderColor: rgba(16, 185, 129, 0.34)
    boxShadow: 0 22px 48px -22px rgba(15, 23, 42, 0.18)
  card-featured:
    borderColor: rgba(251, 191, 36, 0.34)
    backgroundColor: "linear-gradient(180deg, rgba(251, 191, 36, 0.055), {colors.surface})"
  card-icon-tile:
    backgroundColor: rgba(52, 211, 153, 0.09)
    textColor: "{colors.primary}"
    borderColor: "{colors.border}"
    rounded: "{rounded.tile}"
  tag:
    backgroundColor: rgba(255, 255, 255, 0.028)
    borderColor: "{colors.border}"
    textColor: "{colors.text-dim}"
    typography: "{typography.tag}"
    rounded: "{rounded.chip}"
  metric-callout:
    backgroundColor: rgba(52, 211, 153, 0.055)
    borderColor: rgba(52, 211, 153, 0.2)
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.label-eyebrow}"
  header:
    backgroundColor: rgba(247, 249, 252, 0.72)
    backdropBlur: 14px
  terminal:
    backgroundColor: "linear-gradient(180deg, {colors.terminal-surface-top}, {colors.terminal-surface-bottom})"
    textColor: "{colors.terminal-text}"
    typography: "{typography.font-mono}"
    rounded: "{rounded.DEFAULT}"
    boxShadow: 0 30px 70px -20px rgba(15, 23, 42, 0.35)
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

## Typography

Latin copy uses **Inter** (with Plus Jakarta Sans / system-ui fallbacks); pages under `/zh/` switch the entire body to a **CJK-first stack** (PingFang SC, Microsoft YaHei, Noto Sans SC — system fonts, no webfont download) and drop the `-0.02em` heading letter-spacing, which reads as tightness/kerning artifacts in Chinese type. **JetBrains Mono** is the deliberate "data" voice: eyebrow labels, tags, metric numbers, the terminal widget, and anything meant to read as a technical/measured fact rather than prose.

Type scale is fluid throughout via `clamp()` rather than fixed breakpoint jumps — `display` (hero H1) down to `body-sm` all scale continuously with viewport width. Headings are tight (`-0.02em` to `-0.035em` letter-spacing, weight 700); body copy is loose (`line-height: 1.65`) for long-form readability. The hero headline uses a two-color `background-clip: text` gradient (`primary → secondary`) on a `<span>` for its emphasis word — the only place text itself carries a gradient.

## Layout

Content is capped at a **1200px** `wrap` max-width, centered, with fluid inline padding (`clamp(1.15rem, 4vw, 2.5rem)`). Vertical rhythm between sections is a single fluid token (`section-y: clamp(4rem, 9vw, 7.5rem)`) rather than per-section overrides, so spacing stays proportional across the whole page at any viewport. The portfolio grid is `grid-2` (two columns, single column below the mobile breakpoint) — cards are allowed to end a row unpaired rather than forcing an artificial even count. Every interactive target respects a `48px` minimum tap size (`--tap`), enforced even inside dense header/nav elements.

## Elevation & Depth

Depth comes from **translucency and blur**, not shadow stacking. Cards, the sticky header, and dropdown menus are `background: rgba(15,23,42,low-alpha)` panels with `backdrop-filter: blur()` (8px for cards, 14–18px for header/drawer/dropdown) — they read as frosted glass over the ambient gradient, not opaque painted surfaces. Box-shadow is reserved for **interactive/hover states only**: cards and primary buttons are flat at rest and gain a soft, diffused, negative-spread shadow (`box-shadow: 0 22px 48px -22px …`) plus a `translateY(-2px to -4px)` lift on hover — nothing casts a shadow while idle.

The one deliberately "heavier" surface is `.terminal`: a genuinely dark, high-contrast panel with its own self-contained color tokens (`terminal-*`, not the page's light-theme variables) and a real resting shadow, styled like an embedded code block/screenshot rather than a UI panel that must match the surrounding chrome.

## Shapes

Two structural radii cover almost everything: `rounded.sm` (10px) for anything interactive or input-like (buttons, form fields, dropdown items, nav links), and `rounded.DEFAULT` (16px) for containers (cards, the terminal, the globe/stack panels). Below that, small ad hoc radii exist for specific chip-like elements — `chip` (6px, tags) and `tile` (12px, the card icon square) — and above it, `full` (999px) produces pills (badges, the hubs badge, availability indicator) while `50%` produces true circles (avatar, status dot, traffic-light dots in the terminal bar). There is no radius scale beyond these five values — do not introduce a new one-off radius for a new component.

## Components

**Buttons** — `btn-primary` is a solid emerald gradient fill with dark ink text (`on-primary`) and a colored ambient shadow that intensifies on hover; `btn-ghost` is a translucent `surface` fill with a `border-strong` outline, used for secondary actions. Both share the same size, radius, and weight-600 label so they read as one family at different emphasis levels.

**Cards** — the base unit for services and portfolio items: frosted `surface` panel, `border`, `rounded.DEFAULT`, lifting on hover. `card-featured` is the *only* variant, swapping the accent from emerald to amber (border, icon tile, price color) and adding a subtle amber-tinted top gradient — reserved for a single highlighted offer, never used decoratively.

**Tags** — mono-font, low-contrast chips (`rgba(255,255,255,.028)` fill, `text-dim`) used for tech-stack lists; deliberately quiet so they don't compete with card copy.

**Metric callouts** — the signature "proof" element on portfolio cards: an emerald-tinted inset box pairing an icon with a bolded, ink-safe-emerald number/fact. This is the only place body text is allowed to carry heavy inline color emphasis (`<b>` → `primary`).

**Eyebrow labels** — mono, uppercase, letter-spaced, emerald, prefixed by a short horizontal rule — the section-kicker pattern used above every `section-title`.

**Terminal** — the self-contained dark-console widget described under Elevation & Depth; its own semantic color roles (`t-prompt`, `t-cmd`, `t-key`, `t-val`, `t-num`, `t-ok`) map directly to `terminal-accent` / `terminal-text` / `terminal-secondary` / `terminal-tertiary`, mirroring the page's primary/secondary/tertiary hues one level down.

## Do's and Don'ts

- **Do** use the ink-safe shade (`primary`/`secondary`/`tertiary`) for any foreground use — text, icons, borders-with-meaning. **Don't** use the bright shades for text; they fail contrast on the light background by design.
- **Do** keep `tertiary`/amber exclusive to the "featured" flag and its card variant. **Don't** spend amber on anything else — its entire value is signaling "this one is different."
- **Do** treat `secondary`/cyan as a rare second note (gradient stops, brand mark) — never a standalone CTA or link color. **Don't** promote it to a primary action color.
- **Do** build elevation with translucency + `backdrop-filter` blur, reserving box-shadow for hover/interactive states. **Don't** add resting drop-shadows to cards, buttons, or panels — it breaks the flat/frosted language.
- **Do** use `font-mono` for anything data-like (numbers, tags, labels, terminal). **Don't** set prose or headings in mono — it's a data/label signal, not a display font.
- **Do** reuse `rounded.sm` (interactive) / `rounded.DEFAULT` (containers) for any new component. **Don't** invent a new one-off border-radius value.
- **Do** let the CJK stack (`/zh/` pages) take over the whole body font and drop heading letter-spacing. **Don't** force the Latin `font-sans` stack or negative letter-spacing onto Chinese copy — it degrades legibility and kerns oddly.
- **Do** keep the site light-only, with `.terminal` as the sole self-contained dark exception. **Don't** add a site-wide dark-mode toggle or theme new components with a second, separate dark palette.
