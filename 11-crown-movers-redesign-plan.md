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
| Button accessibility | Done — every button color pairing (60 combinations) checked against WCAG AA directly, 16 corrected; see §4.1 |
| Gradients | Done — a small gradient system (`--gradient-action`/`-hover`/`-wash`/`-ink`/`-gold`) in `09-...css`, meant to be used broadly (buttons, CTA panels, hover states, section washes), not just the one button |
| Hover treatment | Done — buttons deepen toward a richer gradient + lift + stronger glow on hover, spec'd in `09-...css` |
| Asset checklist | Done — `12-crown-movers-asset-checklist.md`: fonts, icons, images you need to gather/upload before build |
| Component reference | `crown-movers-frontend-reference.zip` already has header/footer/hero/ quote-form/service-card/trust-strip/FAQ HTML+CSS scaffolds — use as the Bricks component starting point, restyled with the corrected tokens above, not the zip's own placeholder colors |

## 3. Confirmed direction: light-dominant backgrounds

You confirmed: pages should read **light/white-dominant overall**; dark sections are fine, used
deliberately rather than as the default canvas.

This matches what's already live, not a change to it — across the 9 audited sections, every
full-width section background is white or the warm `#FFF4EE` tint; dark ink only ever appears
on specific panels/cards *within* a light section (the quote-form's left info panel, the FAQ's
closing CTA card, photo-card overlays), never as back-to-back full dark sections. The token
mapping already reflects this and doesn't need to change:

- `base` / `body-bg-color` → white / warm tint (the page canvas, stays light)
- `secondary` (ink `#111111`) → reserved for panels, dark buttons, footer, CTA cards — an
  accent surface, not the default one

Carrying this rule forward into Phase 3 template work: budget dark sections deliberately (a
closing CTA band, the footer, maybe one contrast section per page) rather than defaulting to
them for visual variety — reach for the warm tint first.

## 4. Decisions

### 4.1 Resolved

1. **Button text color on orange — resolved: accessibility-first, not size-conditional.**
   Rather than the size-dependent rule this plan originally proposed (white for large CTAs
   only), every `btn-{role}-*-bg`/`*-text` pairing that ships in the ACSS template was checked
   against the WCAG contrast formula directly — 60 pairs across all 10 color roles × 6 button
   states. 16 failed and were corrected to whichever of crown-ink/white actually passes 4.5:1
   against that specific background (mostly ink on the lighter/mid oranges and golds, white on
   the darker hover/dark shades). Every button in `crown-movers-acss-settings.json` now clears
   normal-text AA unconditionally — nothing depends on a component author judging text size
   correctly at build time.
2. **Energy level of motion — resolved: energetic, professional, friendly.** Supersedes the
   original brief's "calm, controlled" framing. Live motion (shine-sweep buttons, pulsing
   glows, animated truck) stays, and the new button hover treatment in `09-...css` leans into
   it further — see the "night hover" spec below.
3. **Gradients — resolved: use broadly, not just on the one button.** A small gradient system
   is now in `09-crown-movers-live-brand-tokens.css` (`--gradient-action`, `-hover`, `-wash`,
   `-ink`, `-gold`) built from the same two brand hues so it reads as one family rather than
   decoration — meant for buttons, CTA panels, hover states, and section-background washes
   (the live "radial-glow over warm-white" pattern already found in 6 of the 9 audited
   sections is now a named, reusable token: `--gradient-wash`).
4. **Orange/gray consolidation — resolved: proceed.** Standardized on `#FE4B03` and `#444444`
   as documented in §6 of `08-crown-movers-live-brand-audit.md`; already applied throughout
   `crown-movers-acss-settings.json`.
5. **Warning/info colors — resolved: use ACSS's own stock defaults.** No live precedent
   exists for either (see audit), so rather than inventing a brand-adjacent color, both are
   kept at whatever ACSS ships with by default — `#FFC10A` (warning) and `#18A2B8` (info),
   which is what your original settings file already had for these two roles, unedited. Every
   button pairing using them was re-checked against WCAG after the change (see §4.1's process
   — 2 more corrections came out of this, `crown-movers-acss-settings.json` already has them).

**Button hover ("night hover") spec** — read literally as a darkening/deepening treatment
rather than a flat color swap: on hover, the button's gradient shifts to a darker, richer pair
of stops (`--gradient-action-hover`, `#CD3A00 → #FE4B03` — moving *into* the color rather than
just swapping it), the glow shadow intensifies (`--shadow-brand-glow-hover`), and the button
lifts 3px. Full CSS is in `09-...css` under "Button hover treatment," with a
`prefers-reduced-motion` fallback. **Flag if "night" meant something else — I read it as the
gradient deepening toward a richer/darker tone, not a literal dark-mode toggle; easy to adjust
if that's not what you meant.**

### 4.2 Still open

Nothing — all decisions from the first pass are resolved as of this update.

## 5. Rollout phases

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
radius consolidation, resolved button accessibility, and gradient/hover system from §4.1, plus
the light-dominant rule from §3, actually get applied.

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
Re-run the WCAG contrast check from §4.1 against final rendered buttons/badges. Confirm the
generated ACSS hover states read correctly. Cross-browser check the animated route/truck
divider and shine-sweep buttons (motion-heavy, worth a `prefers-reduced-motion` audit —
several of the live keyframes already respect it, confirm the rest do too when ported).

## 6. What I did not do

- Did not touch the live site — this is all local reference material in this repo.
- Did not render the two pages visually (headless Chromium in this sandbox can't complete a
  TLS handshake through the environment's network proxy; I didn't force past that by disabling
  certificate verification). Everything above is sourced from the actual shipped HTML/CSS
  text, not a screenshot — see confidence notes in `08`.
- Did not invent business claims, review counts, or service details — none were needed for
  this pass, but flagging per the existing brief's rule.
