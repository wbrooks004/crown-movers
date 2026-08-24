# Crown Movers Homepage — Build Notes (v3, pure BEM + ACSS variables)

Third pass. v1 hand-rolled inline pixel styling; v2 moved to ACSS's own utility classes
(`.section`/`.container`/`.btn.primary`) but that meant guessing ACSS's exact compiled class
names. This version follows your instruction directly: every element carries exactly one (or
base + modifier) purpose-built BEM global class, and every value inside those classes is an
ACSS variable — nothing else.

## What's actually on each element now

Every one of the 107 nodes in `bricks-json/home.json` holds **only** content — `text`, `tag`,
`link`, `image`, `icon`, `hasLoop`/`query` — plus `_cssGlobalClasses` pointing at 1-2 BEM
classes. No inline `_padding`, `_typography`, `_background`, `_border`, anything. A validation
pass in the generator script asserts this for every node (checked: 0 elements have styling
settings outside a class reference) and asserts no element carries a plain `_cssClasses`
string at all — this fixes the earlier version's dependency on guessing ACSS's own compiled
selector names, since I'm no longer attaching ACSS's utility classes directly; I'm authoring
the BEM classes myself and pulling in ACSS's **variables** as values, which I have much higher
confidence in (they're literally the keys I set in `crown-movers-acss-settings.json`).

## Contextual spacing/sizing, not the raw scale

Per your note, spacing/sizing pulls from ACSS's *contextual* tokens rather than picking a
specific rung on the raw scale by hand:

- `var(--content-gap)` — gap between stacked content (paragraph-to-button, card padding).
  Confirmed real: `contextual-content-gap: var(--space-m)` in your settings.
- `var(--container-gap)` — horizontal gutter on the hero row. Confirmed:
  `contextual-container-gap: var(--space-xl)`.
- `var(--grid-gap)` — every card-grid gap. Confirmed: `contextual-grid-gap: var(--space-m)`.
- `var(--section-space-m)` — every section's vertical padding. Confirmed 1:1, it was already
  wired to `section-padding-block` in your settings.
- `var(--col-width-s/m/l)` (13/25/38rem, confirmed real settings) for content-width
  constraints — hero lead paragraph, section headers, FAQ/CTA column widths — instead of
  picking arbitrary rem numbers.
- `var(--h1)`/`var(--h2)`/`var(--h3)` and `var(--text-s)`/`var(--text-m)`/`var(--text-l)` for
  every font-size. These are the one part of this pass I haven't hand-verified against
  compiled output (no live connection to your builder from here) — but they're strongly
  implied by settings that are directly confirmed present and active: `heading-scale: 1.333`,
  `text-scale: 1.333`, `base-heading-desk/mob: 20/18`, `base-text-desk/mob: 18/16`. Font
  *family*/*weight*/*letter-spacing* stay explicit brand choices (Montserrat 800 etc.) — only
  the size value comes from the scale.

## Buttons carry the accessibility fix directly, not through an assumed selector

`btn--primary` sets `color: var(--secondary)` (ink) on the orange gradient — the exact
resolved pairing from the earlier WCAG pass (5.59:1), written directly into the class I
authored rather than trusted to an ACSS-generated `.btn.primary` selector whose exact string I
was never fully certain of. `btn--secondary` (ink bg, white text, 18.88:1) and
`btn--outline-primary` (transparent bg, white text, orange border — for the CTA section's dark
background, mirroring the live site's own `crown-simple-hero-button--dark` pattern) follow the
same logic. One minor tradeoff worth naming: this means the button colors now live in two
places (the ACSS settings file and these BEM classes) rather than one — if you ever change the
brand orange, both need updating. Everything else (spacing, sizing, other colors) still flows
from the ACSS variables live, so this is the one deliberate exception.

## 9 blocks, 77 BEM classes total

`hero`, `stats`/`stat`, `quicklinks`/`quicklink`, `keys`/`key`, `services`/`service`,
`testimonials`/`testimonial`, `partners`/`partner`, `faq`, `cta` — each section is its own BEM
block with `__element` children; `btn` and `card` are shared component blocks reused across
sections (e.g. `card` backs the stat/quicklink/key/service/testimonial/faq-item surfaces, so a
future change to card styling changes all of them at once).

## Still true from earlier passes

- rem base confirmed at 16px (`root-font-size: 100` in your ACSS settings).
- Nothing renders until the CPT posts exist — `13-crown-movers-content-seed.md` +
  `acf-json/README.md`.
- `/commercial-moving/` is a guessed slug — verify or send me the real one.
- The FAQ loop's `objectType: "acf_faq_items"` binding is worth a spot-check in the builder.
- Stat counter numbers (1,000 / 29) are literals, not ACF-bound — see earlier notes for why.
- Image URLs point at the live site as placeholders — swap before production.
- Header/footer are separate Bricks templates, not part of this page JSON.
