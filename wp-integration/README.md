# Crown Movers — WordPress integration

**Superseded 2026-09-24.** The PHP registration files that used to live here
(`01-post-types-and-taxonomies.php`, `02-acf-field-groups.php`) registered `location` /
`region` / `service_category` — post types and taxonomies that do not exist on staging and
were never activated there (confirmed via `docs/audit/exports/ssh/cpt-registration-grep.txt`
and `post-types.csv`, v1.4). They were based on `Crown_Movers_Content_Architecture_Spec_v2.md`,
a proposed spec that was never signed off (§14 sign-off table unticked) and never implemented.

**What's actually live and canonical now:** `services` and `service-areas` post types plus the
`service-region` taxonomy, registered through ACF's own UI + local JSON sync — confirmed by
diffing `post-types.csv` / `taxonomies.csv` (real REST output) field-for-field against the
registration source (see `docs/audit/01-staging-build-provenance.md`, v1.5). The canonical
registration now lives at **`acf-json/`** (repo root), one file per group/post-type/taxonomy/
options-page, named by ACF key — this is ACF's own local-JSON-sync format: drop this folder at
`wp-content/themes/<active-theme>/acf-json/` (or point ACF's `acf/settings/save_json` /
`load_json` filters at it) and ACF picks it up automatically, no PHP required.

Do not re-add PHP-based CPT/taxonomy registration for `services`/`service-areas` — it would
create a second, conflicting registration path for post types ACF's local JSON already owns.

If a genuinely new CPT is needed later, add it as ACF JSON in `acf-json/`, not as PHP here,
to keep one registration mechanism for the whole project.

The removed files are still in git history (`git log --follow -- wp-integration/`) if the old
spec's `location`/`region` model is ever revived — it hasn't been decided against, just not
what's built.
