# Crown Movers Homepage — Build Notes (v4, ACF integration pass)

Fourth pass. v1 hand-rolled inline pixel styling; v2 moved to ACSS's own utility classes
(`.section`/`.container`/`.btn.primary`) but that meant guessing ACSS's exact compiled class
names; v3 followed your instruction directly: every element carries exactly one (or base +
modifier) purpose-built BEM global class, and every value inside those classes is an ACSS
variable — nothing else. v4 doesn't touch any of that BEM/ACSS work — it rewires *content
bindings* onto the more complete ACF structure you sent (Business Info Options Page, the real
`services`/`service-areas` CPT system), replacing the placeholder structure v3 was built
against. See `acf-json/README.md` for the full field reference.

## What changed in v4

- **Service loop**: `post_type` changed from the placeholder `service` to the real `services`
  CPT. Card body text changed from `{acf_short_description}` (a field that no longer exists) to
  `{post_excerpt}` — the new CPT has no separate short-description field, native WP Excerpt is
  the summary. The service card block itself is now a real link (`tag: "a"`, `link:
  {"type":"meta","useDynamicData":"{post_url}"}`) to its own post, and picked up the existing
  `card--hover` modifier class (already used by the quicklinks, so this is reusing an existing
  BEM component, not inventing a new one) — previously the cards weren't clickable at all,
  which only became fixable once `services` posts had real permalinks to link to.
- **Hero + closing CTA buttons are now sitewide-dynamic**, not hardcoded per instance. All four
  primary buttons (hero + CTA section) bind to the Business Info Options Page's `primary_cta`
  link field; both "call us" buttons bind to `secondary_cta`. Text uses the tag directly
  (`{acf_primary_cta}`, resolves to the link's title) with an `@fallback` matching the old
  hardcoded copy so the button isn't blank before the Options Page is filled in; the `link`
  setting binds the whole field via `{"type":"meta","useDynamicData":"{acf_primary_cta}"}` —
  documented in Bricks' own ACF provider reference as the correct shape for a link-type field.
  **Tradeoff worth naming**: the hero and CTA-section primary buttons previously had slightly
  different copy ("Free Quote" vs. "Get a Free Quote") — now they render identical text, since
  both fields are explicitly documented as "the one global CTA used throughout the site."
  That's the field's own stated intent, not a side effect I introduced quietly.
- **Quicklinks slugs**: `/long-distance-moving/` and `/commercial-moving/` both got a
  `/services/` prefix, since the real `services` CPT's registered rewrite slug is now known
  (`services`, confirmed from the CPT's own JSON, not a guess) — so the base path is correct
  even though the exact post slug per item is still unconfirmed (see below).

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
- Nothing renders until the CPT posts and Options Page fields exist —
  `13-crown-movers-content-seed.md` + `acf-json/README.md`. The hero/CTA buttons specifically
  need `primary_cta`/`secondary_cta` filled in on the Business Info Options Page before they
  point anywhere — see the README's "launch blocker" note.
- `/services/long-distance-moving/` and `/services/commercial-moving/` — the `/services/` base
  is now confirmed (it's the real CPT's registered rewrite slug), but whether posts actually
  exist at those exact two slugs is still unconfirmed — verify once the `services` posts are
  created, or send me the real slugs.
- The FAQ loop's `objectType: "acf_faq_items"` binding is worth a spot-check in the builder.
- Stat counter numbers (1,000 / 29) are literals, not ACF-bound — see earlier notes for why.
- Image URLs point at the live site as placeholders — swap before production.
- Header/footer are separate Bricks templates, not part of this page JSON. Now that Business
  Info exists as an Options Page, the footer template is the natural home for
  `office_address`/`business_hours`/social links/`primary_phone` — none of those are used on
  the homepage itself.
- `service-areas`/`service-region` (the locations system) and full `services` detail-page
  templates aren't built yet — the CPTs/field groups exist as of this pass, the pages don't.
