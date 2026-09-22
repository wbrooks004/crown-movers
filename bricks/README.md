# Crown Movers — Bricks Builder component pack

Paste-ready Bricks 2.3.6 JSON. Built with the `anthropic-skills:bricks` skill against your confirmed conventions: **1rem = 10px** (62.5% reset) and **native ACSS 4.x variables** (`--primary`, `--base`, `--accent`, `--neutral` + light/dark steps) — no invented parallel variable namespace.

This file was rewritten after a full review against `Crown_Movers_Content_Architecture_Spec_v2.md` (Drive) and the docx design-system brief, which surfaced two structural bugs in the previous version of this pack (see **Architecture correction** below) and a fuller list of missing components than previously tracked. Cite the continuation brief this session ran from, and this README, as the source for anything below.

## Files

| File | Format | Import via |
|---|---|---|
| `00-setup-acss-and-theme-styles.md` | reference | read first |
| `00-theme-styles.json` | theme styles | Bricks Settings → Theme Styles (hand-enter; see table in the setup doc) |
| `01-header.json` | template (header) | Bricks → Templates → Import — now includes a real "Services" dropdown (service_category terms) |
| `02-hero-home.json` | clipboard | paste — **homepage only.** Full split hero with photo, dual CTA, trust line |
| `02b-hero-inner.json` | clipboard | paste — standalone copy of the inner-page hero band (also embedded directly in every single/archive template below) |
| `03-trust-strip.json` | clipboard | paste, directly under the home hero |
| `04-service-card.json` | clipboard | paste — **static** 3-card grid (Residential/Commercial/Long-distance) for the homepage |
| `05-quote-form.json` | clipboard | paste — native Bricks `form` element, single-step quick quote |
| `06-faq.json` | clipboard | paste — `accordion-nested` with `faqSchema: true` (FAQ JSON-LD for SEO; spec §8.2 — display-value only, not a ranking play) |
| `07-footer-mobile-actions.json` | template (footer) | Bricks → Templates → Import — includes the fixed mobile call/quote bar |
| `08-page-home.json` | clipboard | paste onto the homepage — `02` + `03` + `04` + `05` + `06` already assembled |
| `09-page-quote.json` | clipboard | paste onto `/quote/` — `02b` + `05` already assembled |
| `10-section-services-listing.json` | clipboard | paste onto a designed Page — dynamic query loop over `page` posts tagged with any `service_category` term. See **Architecture correction**. |
| `11-section-locations-listing.json` | clipboard | paste onto a designed Page — dynamic query loop over the `location` CPT, own `location-card__*` class family. See **Architecture correction**. |
| `12-single-service.json` | template (single) | Bricks → Templates → Import — targets Pages via `terms: ["service_category::all"]`, not a CPT. See **Architecture correction**. |
| `13-single-location.json` | template (single) | Bricks → Templates → Import — targets the `location` CPT; eyebrow now reads the real `area_type` ACF field |
| `14-section-blog-listing.json` | clipboard | paste onto a designed Blog Page — dynamic query loop over native WP `post`, with real pagination. See **Architecture correction**. |
| `15-single-post.json` | template (single) | Bricks → Templates → Import — native WP `post` type |
| `16-page-contact.json` | clipboard | paste onto `/contact/` — hero + phone/email/hours + a short contact form |
| `17-announcement-bar.json` | template (content, hook) | Bricks → Templates → Import — optional desktop-only utility bar (`bricks_before_header` hook), phone/hours/real Google rating |
| `18-stats-strip.json` | clipboard | paste — real Google rating (5.0★/593), real years-in-business, real regions-served, one placeholder slot |
| `19-testimonial-cards.json` | clipboard | paste — grid (not a slider), 3× placeholder testimonial |
| `20-team-cards.json` | clipboard | paste — placeholder team/leadership cards |
| `21-partner-logo-row.json` | clipboard | paste — static row (not a carousel), 4× placeholder logo, held behind partner-permission sign-off |
| `22-phone-panel.json` | clipboard | paste anywhere — reusable phone CTA module, distinct from the header's phone button |
| `23-icon-list.json` | clipboard | paste — generic icon+label repeating row (covers "Benefit lists" and "Icon lists") |
| `24-quote-estimate-form.json` | clipboard | paste onto a dedicated estimate page — 8-step moving-estimate experience. **Read its root label before use — real limitation on step validation, see below.** |
| `25-page-privacy-policy.json` | clipboard | paste onto `/privacy-policy/` (existing live URL) — real Law 25 structure. **Needs legal review before publishing**, see its root label |
| `26-page-terms.json` | clipboard | paste onto `/terms-of-use/` (existing live URL) — **needs legal review before publishing**, see its root label |
| `27-cookie-consent.json` | template (content, hook) | Bricks → Templates → Import — site-wide banner (`bricks_before_footer` hook), functional accept/reject + localStorage, does not gate analytics scripts (see its root label) |

Every file passes `python3 -m json.tool` and a parent/child tree-integrity check (flat array, every id resolves, no orphans, no duplicates, every referenced class is embedded) — 29/29 files clean as of this rewrite.

## Architecture correction — read this before building anything else on `10`/`11`/`12`

The previous version of this pack built `10`, `11`, and `12` against a `service` custom post type and a CPT-archive template for `location`. Both were wrong against the actual, approved project spec:

- **`service` CPT never existed in the approved spec.** `Crown_Movers_Content_Architecture_Spec_v2.md` §3.5 explicitly lists "service CPT (Phase 1)" under "Post types deliberately **not** created" — it's gated behind an unapproved URL-consolidation decision (§6.3) and a Polylang Pro requirement neither of which is signed off (checked all 4 copies of the related `Crown_Movers_ACF_Approval_Sheet.md` in Drive — every version has its approval checkboxes unticked). §2's content model states plainly: "Services | Pages + Service field group (Phase 1) → CPT in Phase 2, gated." `10` and `12` now target Pages, not a CPT.
- **`location`'s own spec (§3.1) sets `has_archive: false` on purpose** — "the 'areas we serve' hub is a designed Page, not a CPT archive." The previous `11-archive-location.json` was built as a real Bricks CPT-archive-type template, which has nothing to attach to under that setting (no archive route exists to bind it to). `11` is now a plain Page-embeddable section instead.

**Owner decision, confirmed by Saleem 2026-09-21 — archive templates are not used anywhere on this site.** Listing/hub pages (services, locations, blog) are designed WordPress Pages containing a query-loop section; single items each get one Bricks single template. This applies even where the underlying post type has a perfectly normal native archive route (blog posts do) — it's a site-wide editorial choice, not just a fix for the `location`/`has_archive:false` bug above. `14-section-blog-listing.json` (previously `14-archive-blog.json`, a real Bricks archive template) was converted to match on 2026-09-22. Two traps specific to the blog conversion: don't set the target Page under Settings → Reading → "Posts page" (that routes it through the archive/home template hierarchy and ignores this section's own content); and the Page must land at the blog index's *current* URL (pull it from the Screaming Frog crawl — `internal_html` in Drive) since Phase 1 allows zero URL changes.

Fixed in this pass:
- `10-section-services-listing.json`, `11-section-locations-listing.json`, and `14-section-blog-listing.json` are no longer Bricks *templates* — they're clipboard sections meant to be pasted onto a normal, human-created Page (their `{archive_title}`/`{archive_description}` tags, which only resolve on a real archive route, were swapped for `{post_title}` and, on `10`/`11`, a hand-typed intro — matching how every other paste-once page in this pack works). The three files were also renamed to drop "archive" from the filename: the misleading name is what produced the original `location`/`has_archive:false` bug in the first place, so keeping "archive" in a filename that's now a plain Page section would just leave the same trap for the next person.
- `12-single-service.json`'s template condition changed from `postType: ["service"]` to `terms: ["service_category::all"]` — it now applies to any **Page** carrying a `service_category` term, confirmed against the actual Bricks 2.3.6 templateConditions schema (`includes/templates.php`), which has no "Page Template" condition type at all — don't reintroduce that assumption later.
- `11`'s loop cards now use their own `location-card__*` class family (pin icon, real `region` term) instead of a verbatim copy of `service-card__*` — the two were structurally identical in the previous build, which is exactly the pattern the spec's rule #3 says not to do ("Physical branches and service areas are different things and never share a content type, a template, or a schema block").
- `wp-integration/` (new top-level folder, sibling to `bricks/`) registers the `location` CPT with the exact §3.1 settings (empty rewrite slug, `has_archive: false`, the Option A rewrite-resolution filter), the `region` and `service_category` taxonomies, a virtual "Service" page template for ACF field-group targeting, and the Area Details / Service Details ACF field groups (§5.1/§5.3). **Nothing renders correctly until this (or your own equivalent) is active** — see its own README for what's deliberately left out (a branch CPT/template, Route/Branch field groups, Global ACF Options) and why.

One correction to the continuation brief itself: it described two near-duplicate copies of `Crown_Movers_ACF_Approval_Sheet.md`. There are actually **four** documents under that title in Drive — three are near-identical autosave-style copies of a 5-part "Structure Approval" doc, and the fourth (also the most recently modified, 2026-07-30T21:55) is a materially different, condensed "4 Decisions" rewrite. All four still show unticked approval checkboxes for the services-under-one-hub URL consolidation, so the conclusion doesn't change — but it's four documents, not two.

## Custom post types, taxonomies, and the `service` page template

`location` (CPT), `region` (taxonomy), and `service_category` (taxonomy) are registered by `wp-integration/01-post-types-and-taxonomies.php`. There is no `service` CPT — services stay Pages, tagged with a `service_category` term and (for ACF field visibility) the virtual "Service" page template. See that file and its README for exact settings and the manual Polylang step it can't do for you.

## Styling discipline — classes only, no inline styles

Every element carries content and a `_cssGlobalClasses` reference — nothing else, verified by scanning every file for stray `_`-prefixed style keys outside the documented exceptions (`_cssGlobalClasses`, `_cssId`, `_attributes`, per-instance `_display:breakpoint`, `_interactions`, `_conditions`, and `_cssCustom` used only as Bricks' own documented raw-CSS escape hatch — e.g. the backdrop-filter on the header, and the disabled/loading button state added in this pass, which needs it because Bricks' documented pseudo-state shorthands don't include `:disabled`). All other visual/layout CSS lives in named global classes, never inline on an element.

Two class tiers, mirroring how ACSS itself works:

- **Utility classes** (`u-*`) — atomic, reused everywhere: `u-gap-2xs` … `u-gap-xl`, `u-row`/`u-row-center`/`u-row-between`/`u-row-wrap-center`, `u-max-xs/s/m/l` (width caps), `u-pad-2xl-y`, `u-bg-white`/`u-bg-warm`, `u-text-center`, `u-img-cover-fill`, `u-justify-center`.
- **Component classes** — named, composite, BEM (`block__element`) where a class family has one: `btn-primary`/`btn-outline`/`btn-dark`/`btn-phone-header`, `card-surface`/`card-hover-lift`, `eyebrow`/`intro-text`/`body-text`/`text-muted-sm`, `service-card__*`, `location-card__*`, `testimonial-card__*`, `team-card__*`, `stat-*`, `phone-panel__*`, `hero__*`, `trust-item__*`, `faq__*`, `footer-*`, `nav-link`/`nav-link-strong`.

All non-BEM class names from the previous version (`hero-col-left`, `hero-bg-home`, `hero-row`, `hero-col-right`, `hero-media`, `hero-pad-home`, `trust-item-desc`, `trust-item-divider`, `trust-item-title`, `faq-item-border`, `faq-title-row` — three more than the continuation brief actually flagged, same flat-hyphen problem, fixed the same way) are now `block__element` throughout every file that defines or references them.

Classes are regenerated by throwaway scripts per session (not committed — every output file is already self-contained and paste-ready). Bricks merges same-named classes by name on paste, so pasting multiple files from this pack into one site converges correctly. Building something new? Check this list before inventing a class name.

## Real facts closed this pass

Pulled from `Crown Movers Info.xlsx` (Drive — the designated business-facts source) and `Crown_Movers_Content_Architecture_Spec_v2.md` §3.2 (verified GBP records):

- Phone: `514-606-4030` (was `tel:+10000000000` everywhere — now the real number, in every file, both the `tel:` link and the visible label)
- Hours: Mon–Fri 9am–7pm, Sat–Sun 9am–5pm (contact page, announcement bar, phone panel)
- Email: `info@crownmovers.ca` (contact page)
- Hero trust line: real, verified — 5.0★ / 593 Google reviews (Crown Movers, Montreal/English GBP listing)
- Founding date (Jan. 16, 2020) → "6+ years in business" stat
- Service areas (Montreal, Rive-Sud, Rive-Nord, Laval) → "4 regions served" stat, and the seed terms for the `region` taxonomy
- Privacy Policy / Terms of Use footer links now point at the real, existing live URLs (`/privacy-policy/`, `/terms-of-use/` — confirmed via the 7 Jul 2026 Screaming Frog crawl) instead of `#`

## What's still placeholder — search each file for `[VERIFY]`

Still open, because no verified source exists for it in the project files gathered so far:

- Real photography (image elements point at candidate rows in `07-existing-site-photo-manifest.csv` where one exists; a few placements — the commercial service card, in particular — have no matching candidate in the manifest at all, flagged as a possible real photography gap, not just a selection task)
- FAQ answers, pricing/insurance policy copy, a confirmed full service-area list
- Real testimonials, real team/leadership photos and names (the two verified owners — Jonathan Probonas, Carl Kortbaui — are available if this turns out to be a leadership section rather than a crew section; not assumed either way)
- Real partner names/logos and permission to display them
- Quote/estimate form destination (still defaults to Bricks' native email action — see **Blocked** below)
- Official colour/dark-variant logo file (header still falls back to `logoText`)
- Privacy Policy / Terms of Use: real content structure is drafted (Law 25-shaped), but every operational specific — the designated privacy officer, actual data retention period, which third-party processors are really in use, actual cookie categories — is a named `[VERIFY]`, and the whole draft needs legal review before publishing
- Nav dropdown / footer service links: still `#` anchors, now explicitly flagged where they weren't before, pending confirmed per-category URLs

## Blocked, not guessed

- **n8n endpoint for the quote/estimate forms.** `05-quote-form.json` and `24-quote-estimate-form.json` both default to Bricks' native `email` action. No n8n webhook URL exists yet in any project file gathered — don't invent one. Swap `actions: ["email"]` to `actions: ["webhook"]` + a real `webhookUrl` once it exists.
- **Worth flagging separately:** the architecture spec (§9) names **WS Form** as the project's actual forms plugin, with `form_variant` hidden fields for lead attribution. Every form in this pack, old and new, uses Bricks' own native `form` element instead. That's a real, unresolved tension — not something this pass tried to silently resolve either way.

## Two things to verify once pasted in (not blocking, just unverified)

1. **`--space-*` variable names** — assumed to match ACSS 4.x's native fluid spacing scale.
2. **Quote-form submit button text color** — dark ink (`#151515` on `#F04836` ≈ 4.94:1), not white.
3. **New this pass:** the estimate form's radio fields (`24-quote-estimate-form.json`) use Bricks' native `radio` field type, not a hand-styled "card" look — its own root label explains why and what a real card treatment would need.
4. **New this pass:** the cookie banner's show/hide and localStorage write are real and tested against documented Bricks interaction mechanics, but it does not gate any analytics/ad script from firing pre-consent — that needs separate consent-mode wiring if this site runs Google Analytics/Ads.

## Template coverage

| Template | File | Dynamic? |
|---|---|---|
| Header / Footer | `01`, `07` | — |
| Homepage | `08-page-home.json` | No — one page, by design |
| Services listing | `10-section-services-listing.json` | Yes — paste onto a Page; not a CPT archive, see **Architecture correction** |
| Single service | `12-single-service.json` | Yes — real Page fields, targets `service_category::all` |
| Locations listing | `11-section-locations-listing.json` | Yes — paste onto a Page; not a CPT archive |
| Single location | `13-single-location.json` | Yes — real `location` CPT fields |
| Blog listing | `14-section-blog-listing.json` | Yes — paste onto a Page; native `post` type, real pagination, not an archive template |
| Single post | `15-single-post.json` | Yes — native `post` type |
| Quote page | `09-page-quote.json` | No — one page |
| Contact page | `16-page-contact.json` | No — one page |
| Privacy Policy / Terms | `25`, `26` | No — one page each; needs legal review |

Site-wide add-ons (paste/import independently of any one page): `17` (announcement bar), `27` (cookie banner).

## Component coverage against the original 43-item spec

Full verbatim list and per-item detail extracted from `Crown Movers Design System Instructions.docx` this pass (that doc has 217 paragraphs, no tables/images — the extraction is complete, not a sample). Status:

**Built (28 of 43):** desktop/mobile header, desktop nav, dropdown nav, breadcrumbs, eyebrow labels, trust badges, primary/secondary/outline/dark buttons (now incl. disabled/loading state), Google review display, rating summary, statistics strip, service cards, location cards (own class family), process steps, benefit/icon lists, quote form, multi-step estimate form (see its own caveats), form inputs, select fields, date picker, radio inputs, checkboxes, testimonial cards, review grid (not a carousel, by design), team cards, partner logo row, FAQ accordion, image+copy split, dark CTA section, phone-call panel, blog cards, sticky mobile bar, footer, legal footer, cookie interface, utility announcement bar.

**Partial, disclosed:** language switcher (one static link, not wired to a real Polylang toggle — that needs live Polylang, can't be faked in static JSON); service-area link groups (each location card now shows its real region, but isn't yet grouped into per-region sections — deliberately not attempted as a nested query loop without a live site to test it against, see `11-section-locations-listing.json`'s label); validation states (disabled/loading covered; there's no error/danger color anywhere in the docx's palette — flagging that gap rather than inventing a color); author information (native byline, name only — no richer bio/credential component built).

**Not built, out of scope for this pass:** popups (zero mentions anywhere in the docx — building one would be inventing scope, not filling a gap), a branch page template + Branch/Route ACF field groups (required by the architecture spec §3.2 for the two physical office pages, but wasn't part of the original 18-file pack and touches real NAP/LocalBusiness schema — flagged as a real gap, not attempted here), full pricing/calculator logic (explicitly gated in the spec — "formulas come from Crown Movers in writing").

## The multi-step estimate form's real limitation

`24-quote-estimate-form.json` is one real Bricks `form` element (so it validates and submits correctly as a whole) with 8 step panels shown/hidden via button-click interactions — a real, working step-through UI. What it can't do: Bricks hides a field with `display:none`, and hidden required fields are excluded from native HTML5 validation in most browsers, so nothing here stops a visitor from clicking through to the last step without filling earlier ones. There's no documented Bricks mechanism for "validate this step, then advance." Two real fixes, neither attempted: custom JS per Next-button, or rebuild it in WS Form (the project's actual confirmed forms plugin), which has genuine native multi-step support. The field list, copy, and step design are the real, reusable deliverable regardless of which fix gets picked.
