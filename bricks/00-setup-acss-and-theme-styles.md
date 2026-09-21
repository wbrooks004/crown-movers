# Setup — do this before pasting any component

Two manual steps in ACSS's own admin UI, then one Bricks import. None of this is guesswork — the naming below is exactly what you confirmed for your ACSS 4.x setup, and everything downstream references these same variable names.

## 1. ACSS → Colors panel

Enter these as your brand colors. Component JSON references them by variable name (`var(--primary)` etc.), not by hex, so if you ever rebrand, change it once here.

| ACSS variable | Hex | Used for |
|---|---|---|
| `--primary` | `#F04836` (Crown Coral) | Buttons, links-as-actions, CTAs |
| `--base` | `#151515` (Crown Ink) | Headings, dark sections, button text-on-coral |
| `--accent` | `#F89C3E` (Crown Amber) | Supporting accent only — never large text blocks, never buttons |
| `--neutral` (+ light/dark steps) | `#777D83` (mid) / `#D9D5CF` (light) / `#555B61` (dark) | See mapping below |

**Neutral steps** — set the base `--neutral` swatch, then check what your light/dark variants actually render as and adjust so they land close to:
- `--neutral-light` ≈ `#D9D5CF` → borders, dividers, card outlines
- `--neutral` ≈ `#777D83` → muted/secondary text
- `--neutral-dark` ≈ `#555B61` → primary body text

**Not overridden — using ACSS defaults, per your call:** `--success`, `--danger`, `--focus`. Components reference these variable names for form validation states and focus rings; whatever ACSS ships by default is what renders. If your ACSS build uses different names for these three (e.g. `--error` instead of `--danger`), it's a find-replace across `bricks/*.json` — flagged here so it's a 2-minute fix, not a rebuild.

**Not a brand/neutral role — literal hex, no variable:** the warm off-white section background (`#F7F5F1`) and white surface (`#FFFFFF`) are used as plain hex values in the JSON. They're fixed brand constants, not systemic colors, so there's no naming dependency to get wrong.

## 2. ACSS → Spacing panel (assumption — verify)

Components reference `var(--space-xs)` through `var(--space-2xl)`, assuming ACSS 4.x's native fluid spacing scale uses that naming. **This is the one unverified assumption in this build** — I haven't confirmed the exact step names against your ACSS version. If your panel uses different names (numbered steps, different words), find-replace `--space-` across `bricks/*.json`.

Target px ranges (min viewport → max viewport) to dial your ACSS scale to, so the fluid growth matches what the design tokens were tuned for:

| Step | Min | Max | Used for |
|---|---|---|---|
| `space-2xs` | 4.8px | 7.2px | Tight internal gaps (icon-to-label) |
| `space-xs` | 8.8px | 12.8px | Form field gaps, badge padding |
| `space-s` | 12.8px | 18.4px | Button padding, small card gaps |
| `space-m` | 19.2px | 28.8px | Card padding, stack gaps |
| `space-l` | 28.8px | 44.8px | Grid gaps, section sub-spacing |
| `space-xl` | 44.8px | 76.8px | Hero column gap, large card padding |
| `space-2xl` | 67.2px | 115.2px | Section top/bottom padding |

## 3. Bricks Theme Styles import

`00-theme-styles.json` in this folder sets container width (1280px), section padding, and the h1–h4 + body type scale (Archivo headings / Inter body, fluid `clamp()` sizes, correct colors). This is 100% native Bricks — no ACSS dependency, no naming risk.

Bricks Settings → Theme Styles doesn't have a raw-JSON import in the UI; either hand-enter these values into the Theme Styles panel using the table below, or have a developer merge this JSON into the `bricks_theme_styles` option directly (WP-CLI or a one-off migration script).

| Element | Font | Size (fluid) | Weight | Color |
|---|---|---|---|---|
| H1 | Archivo | 40.8px → 74.4px | 750 | `--base` |
| H2 | Archivo | 32px → 49.6px | 750 | `--base` |
| H3 | Archivo | 24.8px → 35.2px | 750 | `--base` |
| H4 | Archivo | 20px → 26.4px | 750 | `--base` |
| Body | Inter | 16px → 18px | 400 | `--neutral-dark` |

Theme Styles also sets the default button background to `--primary` (coral) with an 8px radius. **Not verified:** whether Bricks' theme-style button text-color path renders dark ink or white by default — every hand-built button in `01-header.json`/`02-hero.json` sets its own text color explicitly (safe), but the native submit button in `05-quote-form.json` relies on the theme-style default. Check it renders `--base` (dark ink) text, not white, once pasted in — the accessibility rule (`#151515` on `#F04836` ≈ 4.94:1; white fails AA) is non-negotiable per the brief.

Rem base confirmed at **1rem = 10px** (62.5% reset) — every clamp() value in this build was computed against that. If that ever changes, every clamp() in `bricks/*.json` needs recomputing (px targets ÷ new root size), not just theme styles.

## 4. Fonts

Archivo and Inter are both Google Fonts — Bricks enqueues them automatically once `font-family` is set (confirm Settings → Performance doesn't have "Disable Google Fonts" on for GDPR reasons; if it does, self-host both as the fallback, per the earlier note on Quebec's privacy posture).

## Build order

1. This setup (colors, spacing, theme styles)
2. `01-header.json` (template import → Header)
3. `02-hero.json`, `03-trust-strip.json`, `04-service-card.json`, `05-quote-form.json`, `06-faq.json` (clipboard paste onto a page)
4. `07-footer-mobile-actions.json` (template import → Footer)

All component files use placeholder content (marked `[VERIFY]` inline) — see the earlier gap-analysis for the business facts (phone number, service-area list, reviews) that still need to land before this goes live.
