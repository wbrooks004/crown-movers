# Crown Movers — Bricks Builder component pack

Paste-ready Bricks 2.3.6 JSON for the components approved to build against placeholder content, plus the token/theme setup they depend on. Built with the `anthropic-skills:bricks` skill against your confirmed conventions: **1rem = 10px** (62.5% reset) and **native ACSS 4.x variables** (`--primary`, `--base`, `--accent`, `--neutral` + light/dark steps) — no invented parallel variable namespace.

## Files

| File | Format | Import via |
|---|---|---|
| `00-setup-acss-and-theme-styles.md` | reference | read first |
| `00-theme-styles.json` | theme styles | Bricks Settings → Theme Styles (hand-enter; see table in the setup doc) |
| `01-header.json` | template (header) | Bricks → Templates → Import |
| `02-hero-home.json` | clipboard | paste — **homepage only.** Full split hero with photo, dual CTA, trust line |
| `02b-hero-inner.json` | clipboard | paste — standalone copy of the inner-page hero band (also embedded directly in every single/archive template below, so you don't need to paste this separately except onto a one-off page) |
| `03-trust-strip.json` | clipboard | paste, directly under the home hero |
| `04-service-card.json` | clipboard | paste — **static** 3-card grid (Residential/Commercial/Long-distance) for the homepage. For a real "all services" listing use `10-archive-service.json` instead, which is dynamic |
| `05-quote-form.json` | clipboard | paste — native Bricks `form` element |
| `06-faq.json` | clipboard | paste — `accordion-nested` with `faqSchema: true` (FAQ JSON-LD for SEO) |
| `07-footer-mobile-actions.json` | template (footer) | Bricks → Templates → Import — includes the fixed mobile call/quote bar |
| `08-page-home.json` | clipboard | paste onto the homepage — `02-hero-home` + `03` + `04` + `05` + `06` already assembled in order |
| `09-page-quote.json` | clipboard | paste onto a dedicated `/quote/` page — `02b-hero-inner` + `05-quote-form` already assembled |
| `10-archive-service.json` | template (archive) | Bricks → Templates → Import — **dynamic**, real query loop over the `service` post type |
| `11-archive-location.json` | template (archive) | Bricks → Templates → Import — same pattern, `location` post type |
| `12-single-service.json` | template (single) | Bricks → Templates → Import — hero + `{post_content}` body + aside quote panel + process steps + dark CTA |
| `13-single-location.json` | template (single) | Bricks → Templates → Import — same as single-service, plus a "nearby locations" loop (excludes the current post) |
| `14-archive-blog.json` | template (archive) | Bricks → Templates → Import — native WP `post` type, no CPT needed |
| `15-single-post.json` | template (single) | Bricks → Templates → Import — native WP `post` type |
| `16-page-contact.json` | clipboard | paste onto a `/contact/` page — hero band + phone/email/hours + a short name/email/message form (distinct from the move-specific quote form) |

Every file passes `python3 -m json.tool` and a parent/child tree-integrity check (flat array, every id resolves, no orphans, no duplicates, every referenced class is embedded).

## Custom post types this pack assumes exist

`10`–`13` target post types with slugs `service` and `location` in their `templateConditions`. **Nothing here registers those post types** — set them up first (ACF's "Post Types" UI, or CPT UI) with exactly those slugs, or edit `postType`/`archivePostTypes` in the two archive and two single files to match whatever slugs you actually use. Until the CPTs exist, these four templates have nothing to attach to.

## Styling discipline — classes only, no inline styles

Every element carries content and a `_cssGlobalClasses` reference — nothing else. All visual/layout CSS (`_typography`, `_background`, `_border`, `_boxShadow`, `_padding`, gaps, flex/grid direction, hover states) lives in named global classes, never inline on an element. Verified by scanning every generated file for stray `_`-prefixed style keys outside `_cssGlobalClasses` — zero found.

Two class tiers, mirroring how ACSS itself works (utility classes you stack, plus named components):

- **Utility classes** (`u-*`) — atomic, reused everywhere: `u-gap-2xs` … `u-gap-xl` (map to the `--space-*` scale), `u-row`/`u-row-center`/`u-row-between`/`u-row-wrap-center`, `u-max-xs/s/m/l` (width caps), `u-pad-2xl-y` (section spacing), `u-bg-white`/`u-bg-warm`, `u-text-center`, `u-img-cover-fill`.
- **Component classes** — named, composite: `btn-primary`/`btn-outline`/`btn-dark`/`btn-phone-header`, `card-surface`/`card-hover-lift` (stack both for a hoverable card, just the first for a static one), `eyebrow`/`intro-text`/`body-text`/`text-muted-sm`, `service-card__*`, `footer-*`, `trust-item-*`, `hero-*`, `nav-link`/`nav-link-strong`.

The only settings that stay on an element itself: content (`text`/`tag`/`link`/`icon`/`image`), behavior config that has no CSS equivalent (`fields`/`actions` on forms, `faqSchema`/`expandFirstItem` on the accordion, `ariaLabel`/`mobileMenu` on nav, `logoText`/`logoHeight`), identity (`_cssId`, `_attributes`), and per-instance breakpoint visibility (`_display:mobile_landscape: "none"`) — none of these have a sensible class-based equivalent.

Classes are regenerated by a single script (not committed — every output file is already self-contained and paste-ready) that defines the library once and builds every file from it, so the same class name always carries the exact same settings everywhere it's used. Bricks merges same-named classes by name on paste, so pasting multiple files from this pack into one site converges correctly rather than duplicating.

Building a new template? Reuse the existing class names before inventing new ones — check this list first.

## What's still placeholder — search each file for `[VERIFY]`

None of this is wired to real business facts yet. Every `[VERIFY]` label marks a spot that needs one of the items from the earlier gap-analysis before this goes live:

- Phone number (`tel:+10000000000` everywhere)
- Real photography (image elements are left empty, pointing at `07-existing-site-photo-manifest.csv` for candidates — nothing hotlinks crownmovers.ca)
- Service-area/location list, reviews/ratings/stats, FAQ answers, pricing/insurance policy copy
- Quote form destination (`05-quote-form.json` + `09`/`16` defaults to Bricks' native email action; swap to a webhook once an n8n endpoint exists)
- Privacy Policy / Terms pages (footer links to `#` — also needed for Quebec Law 25 disclosures)
- Official colour/dark-variant logo file (header currently falls back to `logoText`)
- Contact email/hours (`16-page-contact.json`)

`12`/`13`/`14`/`15` are the least placeholder-dependent files here: their H1, body copy, excerpt, author, date, and featured image all come from `{post_title}`/`{post_content}`/`{post_excerpt}`/`{featured_image}` — real WordPress fields, correct the moment a post exists, zero ACF required. Only the eyebrow category label and phone number on those four are hand-typed.

## Two things to verify once pasted in (not blocking, just unverified)

1. **`--space-*` variable names** — assumed to match ACSS 4.x's native fluid spacing scale. If your panel uses different step names, it's a find-replace across `bricks/*.json`, not a rebuild.
2. **Quote-form submit button text color** — relies on the Theme Styles `button` group rendering dark ink, not white, on the coral background. The accessibility rule (`#151515` on `#F04836` ≈ 4.94:1; white fails AA) is non-negotiable — confirm it once pasted in.

## Template coverage

All 9 template types from the original site-structure list now exist:

| Template | File | Dynamic? |
|---|---|---|
| Header / Footer | `01`, `07` | — |
| Homepage | `08-page-home.json` | No — hand-typed, by design (one page, not a repeated post type) |
| Service archive / Single service | `10`, `12` | **Yes** — real query loop / real post fields |
| Location archive / Single location | `11`, `13` | **Yes** |
| Blog archive / Single post | `14`, `15` | **Yes** — native `post` type, no CPT setup needed |
| Quote page | `09-page-quote.json` | No — one page |
| Contact page | `16-page-contact.json` | No — one page |

## Not built yet (from the original 43-component docx spec)

This pack covers roughly 15 of 43 named components (breadcrumbs, post-meta, and post-content all use Bricks' native elements rather than hand-built markup). Still open: announcement bar, rating/stats strip, location cards as a *distinct* pattern from service cards, multi-step estimate form + calculator, date picker/radio-card form inputs, testimonial cards, team cards, partner logo row, popups, and the ACF field groups (category labels, verified excerpts, custom pricing/insurance fields) that would replace the remaining hand-typed `[VERIFY]` text with real dynamic data. Build these next once the business-fact gaps above are closed.
