# Crown Movers — Bricks JSON (Stage: Home page + header/footer templates)

Generated 2026-09-24, against verified staging facts (`docs/audit/00-environment-baseline.md`,
`docs/audit/01-staging-build-provenance.md`, `docs/audit/exports/ssh/`). Built with the
`anthropic-skills:bricks` skill's verified JSON shapes. Not yet applied to staging — this repo
has no SSH/wp-admin access; import is a separate step (see below).

## What's here

| File | Format | Targets |
|---|---|---|
| `header-template.json` | Template export (`type: "header"`) | Existing empty `bricks_template` post **18545** ("Crown Movers — Header") — already carries sticky settings; this fills its content |
| `footer-template.json` | Template export (`type: "footer"`) | Existing empty `bricks_template` post **18531** ("Footer - EN") |
| `home-page.json` | Clipboard paste (`bricksCopiedElements`) | Page **28** (home) — replaces its current `_bricks_page_content_2`, which today is a single flat page with `_cssClasses` strings instead of registered global classes |

Header/footer are built as real templates, not embedded in the page content — the previous
state (flagged in `docs/audit/00-environment-baseline.md`) had both live inside page 28's own
JSON, with the six actual `bricks_template` posts left as empty shells.

## What every value is bound to

- **Design values** (spacing, color, radius, section spacing, content width, shadows) reference
  ACSS custom properties only (`var(--primary)`, `var(--space-l)`, `var(--section-space-l)`,
  `var(--content-width-safe)`, `var(--radius)`, etc.) — never a literal hex or px. This means
  the pending v2.0 ACSS dashboard reconfiguration (brand coral, ink base, Archivo/Inter, 6px
  radius) applies to this JSON automatically once saved; nothing here needs to change when that
  happens.
- **Two ACSS button classes are borrowed by name** (`btn--primary`, `btn--m`, `btn--l`,
  `btn--primary-light`) with empty `settings` — Bricks' class-merge-by-name behavior on import
  resolves these to the site's real, already-registered definitions
  (`docs/audit/exports/ssh/opt-bricks_global_classes.json`), not to anything invented here.
- **Every custom class is a real registered global class** (`crown-hero`, `crown-why__grid`,
  etc. — 53 total across the three files), not a loose `_cssClasses` string — this fixes the
  anti-pattern flagged in the baseline audit, where the live home page's `crown-*` classes were
  plain strings with no matching entry in `bricks_global_classes`.
- **All copy, images, and business facts are ACF dynamic tags**, bound to the already-registered
  `group_crown_homepage` and `group_crown_business_info` (options page) field groups —
  `{acf_home_hero_heading}`, `{acf_home_google_rating}`, `{acf_home_moves_year}`,
  `{acf_primary_phone}`, etc. **Nothing is hardcoded**, including the "3,000+ moves/year" and
  "5.0 Google rating" claims flagged `[VERIFY]` in the audit — they're now editable content
  fields, not baked-in copy, and won't render anything until those fields are populated.
- **The quote form is `{acf_home_quote_form_shortcode}`**, a plain text ACF field rendered
  through a `shortcode` element — not a hardcoded WS Form ID. There are 21 forms on staging
  including what look like two different "current" quote forms (`Free Moving Quote` id 1,
  `Crown Free Quote - English` id 20); which one is live is a content decision, not something to
  guess in JSON. Set the actual shortcode (e.g. `[ws_form id="1"]`) as that field's value.

## Query loops referenced, not fully specified

Three loops (`home_featured_services` relationship, `home_why_benefits` repeater,
`home_quote_features` repeater, `home_process_steps` repeater, and the footer's `services` CPT
loop) are marked `hasLoop: true` with a best-effort `query` object. Per the Bricks skill's own
reference, the exact `objectType` string for an ACF-sourced loop is what the **builder itself**
emits when you pick the field from its query-type dropdown — hand-authoring can get close but
should be confirmed by opening the loop settings in the builder once imported, not trusted
blind.

## Content still needed before this looks right

- Populate `group_crown_homepage` and `group_crown_business_info` (options page) with real
  values — hero copy, stat numbers (only once confirmed with the client, per the `[VERIFY]`
  flag), business hours/address/phone, social URLs, logo assets.
- Set `home_quote_form_shortcode` to the correct live WS Form shortcode.
- Populate the `services` CPT (currently 0 posts) so the featured-services relationship field
  and the footer loop have something to show.
- Nav links in the header are hardcoded paths (`/services/`, `/montreal-movers/`, etc.) matching
  the existing URL inventory — confirm against `docs/audit/live-url-inventory-2026-09-22.csv`
  before treating them as final; URL preservation is a hard requirement, not a suggestion.

## Applying this to staging

This repo has no SSH or wp-admin session. To land it:

1. **Templates** — Bricks admin → Templates → Import → `header-template.json` /
   `footer-template.json`. Bricks will ask to overwrite or create new; point it at posts 18545 /
   18531 if the UI offers that, otherwise import as new and re-point the template condition,
   then trash the old empty ones.
2. **Home page** — paste `home-page.json`'s `content` array into page 28 via the builder
   (Cmd/Ctrl+V in the structure panel), or use WP-CLI from a session with SSH access:
   `wp post meta update 28 _bricks_page_content_2 --format=json < <(python3 -c "import json;print(json.dumps(json.load(open('home-page.json'))['content']))")`
   — **take a backup of the current `_bricks_page_content_2` value first**, this overwrites it.
3. **ACF registration** — copy `acf-json/*.json` to wherever ACF's local JSON sync path points
   on staging (see `wp-integration/README.md`); it should already match what's live since these
   files came from the site's own `acf-export-2026-09-23.json`, but confirm no drift since that
   export was taken.

None of this has been applied yet. Screenshot/visual verification, WS Form ID confirmation, and
the ACSS v2.0 dashboard save are still open — see `docs/audit/00-environment-baseline.md`
KNOWN ISSUES for the full list.
