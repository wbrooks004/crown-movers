# Crown Movers — Live Site Brand Audit (supersedes the color/type choices in 02–05)

## Why this file exists

Files `02`–`07` in this repo describe a **proposed** design system ("Crown Coral" `#F04836` /
"Crown Amber" `#F89C3E` / Archivo + Inter) that was explicitly built **not** to copy the
current website. That direction has not been implemented anywhere live.

You asked the redesign to match the current site instead, using the Montreal Movers page and
the Free Quote page as the reference for "the styling and direction of the entire new site."
This file documents what is **actually live** on those two pages today, and the corrected
token set derived from it. Use this file — not `04`/`05` — as the color/type source of truth
going forward. `04`/`05` are kept for history, not deleted.

## What's actually running today

`crownmovers.ca` is currently built on **Oxygen Builder** (WS Form Pro, NotificationX, a
logo‑slider plugin) — not Bricks/ACSS yet. The Bricks + Automatic CSS build is the *new* site
you're planning. Both `/montreal-movers/` and `/free-quote/` carry the same sitewide Oxygen
theme **plus** a set of hand-built, custom-coded sections (injected as Oxygen "Code Block"
elements, class-prefixed `crown-*`/`cm-*`) that are visibly more recent and more deliberate
than the rest of the site — dated images from `2026/06`, consistent BEM naming, real
micro-interactions. There are **8 of these bespoke sections on `/montreal-movers/` alone**
(trust-stat strip, hero CTA pair, an embedded quote widget, an animated route/truck divider,
a service-story photo grid, a "care" section, a residential-move split hero, a calculator CTA
banner, a moving/storage section, and a final FAQ+CTA section) plus one dedicated quote layout
on `/free-quote/`. That's the real, already-in-production design language — this audit
canonicalizes it.

## Corrected brand tokens (live-verified)

| Role | Hex | Source / confidence |
|---|---|---|
| **Primary** (brand action orange) | `#FE4B03` | Live. Dominant color on every button, icon, badge, link across both pages — used far more than any other single value. |
| **Secondary** ("ink" — dark panels/buttons) | `#111111` | Live. Used consistently instead of pure black for text and every dark surface (quote-form dark panel, dark CTA buttons, feature-card overlays). |
| **Tertiary** (warm gradient partner) | `#FF7530` | Live. The lighter stop in every primary-button gradient (`linear-gradient(135deg, #fe4b03, #ff7530)`) and hover glow. |
| **Accent** (gold highlight) | `#F5A400` | Live. The one other hue found in production — used for the star-rating number on the trust strip. |
| **Base** (warm section tint) | `#FFF4EE` | Live family. Sections alternate pure white with a warm off-white wash (`#fff7f2`/`#fff1e8`/`#fff4ee` cluster) — this is the canonical value, and matches what `04-...css` already guessed almost exactly. |
| **Neutral** (grayscale ramp) | `#111111` → white | Live. Same ink anchor as Secondary, zero chroma. |
| **Success** | `#16713B` | Live. Real value from the quote form's validation states. |
| **Danger** | `#B42318` | Live. Real value from the quote form's validation states (also happens to be an exact match to `05-...json`'s guess). |
| **Warning** | `#B7791F` | **Not found live** — no warning/caution UI exists on either page today. Brand-adjacent amber, safe default. Revisit if/when a real warning state is designed. |
| **Info** | `#2E6FD1` | **Not found live** — the only blue on either page is a Google "G" review-badge icon, not a UI color. Conventional default. |

**Typography:** Montserrat (headings — very heavy weights, 800–950, tight negative tracking
down to `-0.06em`, aggressive `clamp()` fluid sizing) + Roboto (body/UI/forms). Not
Archivo/Inter as `02` proposed — Montserrat/Roboto are what's actually enqueued and used on
both live pages.

**Radius:** live sections use a bold, two-tier system, not the small 4/8/12px scale `05`
proposed — cards/panels/photos run **20–34px**, buttons/inputs run **7–14px**, and badges/tags/
some primary CTAs are full pill (`999px`).

**Shadows:** soft, large-blur, frequently brand-tinted glows (`0 16px 35px rgba(254,75,3,.35)`
on primary buttons) rather than flat/hard shadows.

**Motion:** live sections are genuinely energetic — hover-lift, shine-sweep button
animations, a pulsing-glow animated route/truck illustration. Worth flagging: this reads more
"confident and dynamic" than the "calm, controlled" positioning in `02`'s brief. Since you
asked to match the current site, this audit preserves the live energy level; see the redesign
plan (`11`) for the explicit call-out.

## Inconsistencies found in production (cleanup input for the redesign)

The current custom sections were clearly built across multiple sessions and have drifted:

- **Brand orange has 3 near-duplicate values in production**: `#fe4b03` (dominant), `#ff4b00`
  (free-quote page's own quote section), `#ff5a1f` (the embedded quote widget on
  montreal-movers). All three read as "the same orange" to a viewer but aren't literally the
  same value. **Recommendation: standardize on `#FE4B03` everywhere** (used in this audit).
- Body-copy gray has 4 close variants (`#3f3f3f`/`#444444`/`#4a4a4a`/`#555555`) with no clear
  rule for which is used where.
- Button radius is inconsistent: 7px, 14px, and 999px pill all appear as "the primary CTA"
  treatment in different sections, without an obvious rule.

These are exactly the kind of drift a real token system (below) is meant to fix.

## Confidence notes / what to double-check

- Colors, fonts, radius, shadow, and spacing values above are extracted directly from CSS
  actually shipped to the browser on both live pages — high confidence.
- I could not render the pages visually in this sandbox (headless Chromium here can't
  complete a TLS handshake through this environment's network proxy, and I did not disable
  certificate verification to force it) — everything above is from the shipped markup/CSS
  text itself, not a screenshot.
- The generated ACSS *custom font registration* fields (`font-1-*`/`font-2-*` in the JSON
  import) are a best-effort guess at Automatic CSS's internal shape — re-check those two font
  entries in the ACSS Typography panel UI directly after import.
- The per-role **hover** lightness in the generated JSON is an approximation (base lightness
  darkened ~10%, gamut-clamped) since ACSS Pro's exact internal hover formula isn't public.
  It'll look right, but nudge it in the ACSS color picker if you want pixel-exact control.
