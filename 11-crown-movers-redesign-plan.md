# Crown Movers Redesign Plan (Bricks + Automatic CSS)

Status: draft plan, first pass. Built from a live audit of `crownmovers.ca` (see
`08-crown-movers-live-brand-audit.md`) plus the corrected token set in `09`/`10` and
`crown-movers-acss-settings.json`.

## 1. Where things actually stand

- The **new** stack (WordPress + Bricks Builder + Automatic CSS + Frames + ACF + Polylang +
  Rank Math) hasn't been stood up yet — the live site is still on Oxygen Builder.
- The visual direction for the new site already exists in production, though: **8 hand-built
  sections on `/montreal-movers/`** and a dedicated quote layout on `/free-quote/`, injected as
  custom code blocks on top of the old Oxygen theme. That's a real, validated design language
  — bold orange (`#FE4B03`), near-black ink, warm off-white sections, big rounded cards,
  Montserrat/Roboto, soft brand-tinted glow shadows, confident hover/shine motion.
- Your `color-primary`/`color-secondary` etc. in the pasted ACSS settings were still the
  plugin's stock demo colors (teal/navy/olive) — not a stale version of anything real, just
  never set. `crown-movers-acss-settings.json` replaces them with the live-verified palette.

**In short: this is less "invent a new look" and more "formalize the look that already exists
across 9 sections, fix its inconsistencies, and roll it out to the rest of the site in Bricks."**

## 2. Foundation (ready now)

| Piece | Status |
|---|---|
| Color tokens | Done — `crown-movers-acss-settings.json`, ready to import into ACSS |
| Typography | Done — Montserrat/Roboto registered, heading weight/tracking set |
| Radius scale | Done — `base-radius: 14px` × `radius-scale: 1.5` ramp matches live spread |
| Shadow tokens | Done — soft neutral + brand-glow shadow added to `box-shadow-1/2/3` |
| Button treatment | Done — uppercase, `0.06em` tracking, `800` weight (matches live CTAs) |
| Component reference | `crown-movers-frontend-reference.zip` already has header/footer/hero/ quote-form/service-card/trust-strip/FAQ HTML+CSS scaffolds — use as the Bricks component starting point, restyled with the corrected tokens above, not the zip's own placeholder colors |

## 3. Open decisions — need your sign-off before build

1. **Button text color on orange.** Live ships white-on-orange, which only passes WCAG AA for
   large/bold text (3.38:1) and fails for anything smaller (needs 4.5:1). Recommendation: keep
   white for large CTA buttons (matches current brand feel, passes AA there), switch to
   crown-ink (`#111111`) text anywhere orange backs smaller text (badges, inline tags, small
   links) — ink-on-orange hits 5.59:1 either way. Confirm before this goes live sitewide.
2. **Energy level of motion.** The original design brief (`02`) asked for "calm, controlled."
   What's actually live is more energetic — shine-sweep buttons, pulsing badge glows, an
   animated route/truck illustration. This plan preserves the live energy level by default
   (per your "match the current site" instruction). Say the word if you'd rather dial it back
   toward "calm" for the full rollout.
3. **Warning/info colors.** No live precedent exists for either (see audit). Flagged defaults
   are in place; fine to leave until a real use case (e.g., "limited availability" badge)
   comes up.
4. **Orange/gray consolidation.** Production currently has 3 near-duplicate oranges and 4
   near-duplicate body grays (see audit §"Inconsistencies"). This plan standardizes on one of
   each (`#FE4B03`, `#444444`). Flag if any of the specific existing usages were intentional
   variation rather than drift.

## 4. Rollout phases

**Phase 0 — Bricks/ACSS environment**
Stand up Bricks + ACSS + Frames + ACF + Polylang + Rank Math on a staging copy. Import
`crown-movers-acss-settings.json`. Re-check the two `font-1`/`font-2` custom-font entries in
the ACSS Typography panel directly (see confidence note in `08`) and the generated hover
shades in the ACSS color picker.

**Phase 1 — Global components** (per `bricks-exports/class-map.csv` in the reference pack)
Header/nav + language switcher, footer, mobile sticky conversion bar, button set
(primary/dark/outline), form field styling for the ACF-driven quote flow. These touch every
page, so get them right once.

**Phase 2 — Rebuild the 2 pages that already exist, natively in Bricks**
Port the 9 already-validated custom sections from Oxygen code blocks into real Bricks
elements/components using the corrected tokens — not a re-design, a re-platform. This is the
lowest-risk phase since the content and layout are already proven; it's also where the color/
radius consolidation from §3.4 actually gets applied.

**Phase 3 — Template-ize for the rest of the site**
Sitemap shows this IA to cover, matching the brief's "service-page" and "location-page"
patterns:
- `/montreal-movers/` sub-pages: residential-moving, packing-services, furniture-assembly,
  small-movers, delivery-services
- `/long-distance-moving/`
- `/contact/`
- Homepage
- French (`/fr/...`) equivalents via Polylang — same visual system, no separate design pass;
  budget extra width for French labels per the brief's "15–30% longer" note.

Build ACF field groups for services/locations/reviews/FAQs (per
`bricks-exports/README.md`'s recommended build order) so these become dynamic templates rather
than one-off pages — the two existing pages are the pattern library for this.

**Phase 4 — QA pass**
Re-run the WCAG contrast check from §3.1 against final rendered buttons/badges. Confirm the
generated ACSS hover states read correctly. Cross-browser check the animated route/truck
divider and shine-sweep buttons (motion-heavy, worth a `prefers-reduced-motion` audit —
several of the live keyframes already respect it, confirm the rest do too when ported).

## 5. What I did not do

- Did not touch the live site — this is all local reference material in this repo.
- Did not render the two pages visually (headless Chromium in this sandbox can't complete a
  TLS handshake through the environment's network proxy; I didn't force past that by disabling
  certificate verification). Everything above is sourced from the actual shipped HTML/CSS
  text, not a screenshot — see confidence notes in `08`.
- Did not invent business claims, review counts, or service details — none were needed for
  this pass, but flagging per the existing brief's rule.
