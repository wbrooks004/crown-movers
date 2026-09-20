# Crown Movers — WordPress integration code

PHP that the `bricks/` template pack depends on but that isn't Bricks JSON: post type,
taxonomy, and ACF field group registration. Nothing in `bricks/` will render correctly
until this (or your own equivalent) is active.

Source of truth for every setting here: `Crown_Movers_Content_Architecture_Spec_v2.md`
(Drive — most recently modified copy as of this writing, 2026-07-30T21:37 UTC; diffed
against the other saved copy from the same day, content identical on every point these
files implement). That spec is marked **PROPOSED — not approved** with a sign-off table
at its §14; nothing here should go to production before that sign-off happens.

## Install

Both files are plain PHP with no plugin header — drop them in `wp-content/mu-plugins/`
(must-use, loads automatically, can't be accidentally deactivated) or wrap them in a
one-file custom plugin. Load order matters: `01-` before `02-` (the ACF field groups'
location rules reference the CPT and page template `01-` registers).

Requires ACF Pro (Repeater field type) for `02-acf-field-groups.php`.

## What's deliberately NOT here

- **A `service` CPT.** The spec lists it under "post types deliberately not created" in
  Phase 1 (§3.5) — it's gated behind the service-URL decision (§6.3) and a translated
  URL base, which needs Polylang Pro. Services stay Pages + the Service field group
  until that gate opens. See `bricks/README.md` for how `10-archive-service.json` and
  `12-single-service.json` were rebuilt around that.
- **Branch Details (§5.2) and Route Details (§5.4) field groups**, and a branch CPT/page
  template. The spec calls for /montreal-movers/ and /fr/demenagement-montreal/ to get
  "their own Bricks template" (§3.2) with `LocalBusiness` schema — that template doesn't
  exist yet anywhere in `bricks/`, so its field group isn't registered here either. Real
  NAP is already available (Crown Movers Info.xlsx) if this gets picked up next.
- **Global ACF Options (§5.5)** — company-wide phone/email/social/CTA defaults. Same
  reason: nothing in the current pack reads from an Options page yet.
- **Polylang's per-CPT/taxonomy translation toggle.** UI-only (Languages → Settings →
  Custom Post Types and Taxonomies) — enable it for `location` and `service_category`
  after activating these files, there's no clean filter-based equivalent.

## Before this goes live

Run the staging test matrix in the spec, §10.4, in full — it's written as a checklist
specifically for the rewrite/query-var change in `01-post-types-and-taxonomies.php`
(the `pre_get_posts` filter). Nothing in this repo has been tested against a real
WordPress install; treat every `[VERIFICATION REQUIRED]` note inline in the PHP as
exactly that.

## How the "Service" page template actually gets used

`crown-service-template.php` is registered but the file itself doesn't exist — that's
intentional (see the comment in `01-post-types-and-taxonomies.php`). It does two jobs:

1. Gives editors a labeled "Service" choice in Page Attributes.
2. Lets the ACF Service field group auto-appear when that template is selected.

It does **not** control which Bricks template renders the page — Bricks 2.3.6 has no
"Page Template" template condition. `bricks/12-single-service.json` instead targets the
`service_category` taxonomy. **A service page needs both set:** the page template (admin
marker + field visibility) and a `service_category` term (what Bricks and the services
listing actually key off). Tagging one without the other means either the fields don't
show up in the editor, or the page won't render with the Service template on the front
end / won't appear in the services listing.
