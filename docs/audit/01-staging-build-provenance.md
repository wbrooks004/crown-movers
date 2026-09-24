VERSION: Crown Movers v1.5

# Crown Movers v1.5 — Staging Build Provenance

Read-only, repo + HTTPS only. Nothing changed on staging or on any other branch. Executor:
Claude Code (remote cloud container).

## STAGING BUILD SOURCE — NOT FOUND in this repo's history. The provenance hypothesis is REFUTED, not confirmed.

A prior pass hypothesized that `claude/ssh-server-access-99xi0g`'s `bricks-json/home.json`
produced the live homepage, citing its commit `f80ea2c "Fix rendering bugs found in first real
Bricks render"`. Direct comparison rules this out.

**Method:** extracted every distinct `class="..."` token from three fresh, cache-busted
(`?nocache=1`) staging fetches — home (123 classes), `/montreal-movers/` (47), `/junk-removal/`
(46) — and searched for them, plus the three unique 6-character Bricks element IDs captured in
the v1.0 pass (`mmctxe`, `vctqsz`, `wfpxfu`), across all Bricks JSON in all three known
branches (`main`, `claude/zealous-rubin-9ngbym`, `claude/ssh-server-access-99xi0g`).

**Result: zero matches, in either direction, against all three sources.**

The live homepage uses an extensive, clearly deliberate BEM system under a `crown-` prefix —
90 distinct classes (`crown-hero__badge-icon`, `crown-topbar__group`, `crown-rating__stars`,
`crown-proof__inner`, `crown-stat__value`, `crown-testimonial__mark`, `crown-final__actions`,
etc., full list below) covering a topbar, header, hero with a Google-rating badge, a stats
strip, a "why us" section, a process section, a quote panel, testimonials, and a final CTA.
None of it — not one class name, not one element ID — appears anywhere in this repo's git
history across the three branches checked.

**Conclusion: the live staging build has a fourth, still-unidentified source.** It is not the
current repo's `bricks/*.json` pack, not `zealous-rubin`'s templates, and not
`ssh-server-access`'s `bricks-json/*.json`. Whoever built it did so directly in the Bricks
editor on staging, or from a JSON file that was never pushed to any branch in this GitHub
repository. Settling this needs the SSH half (v1.4): `wp post list --post_type=bricks_template`
plus the `bricks_global_classes` option would show whether it's stored as templates/components
(recoverable) or hand-built page-by-page (harder to reconstruct from outside the builder).

Full class list from staging home, for future comparison:
```
crown-btn, crown-btn--primary, crown-checklist, crown-container, crown-copy, crown-display,
crown-eyebrow, crown-final, crown-final__actions, crown-final__content, crown-final__inner,
crown-final__media, crown-final__phone, crown-final__title, crown-footer, crown-footer__bottom,
crown-footer__brand, crown-footer__col, crown-footer__heading, crown-footer__inner,
crown-footer__link, crown-footer__logo, crown-footer__text, crown-header, crown-header__cta,
crown-header__inner, crown-header__logo, crown-hero, crown-hero__actions, crown-hero__badge,
crown-hero__badge-copy, crown-hero__badge-icon, crown-hero__badge-label, crown-hero__badge-value,
crown-hero__content, crown-hero__copy, crown-hero__image, crown-hero__inner, crown-hero__media,
crown-hero__title, crown-map, crown-nav, crown-nav__link, crown-phone, crown-process,
crown-process__inner, crown-process__steps, crown-process__title, crown-proof,
crown-proof__inner, crown-quote, crown-quote__content, crown-quote__copy, crown-quote__features,
crown-quote__inner, crown-quote__title, crown-rating, crown-rating__g, crown-rating__label,
crown-rating__stars, crown-services, crown-services__copy, crown-services__grid,
crown-services__inner, crown-services__intro, crown-services__title, crown-stat,
crown-stat__icon, crown-stat__label, crown-stat__stars, crown-stat__value, crown-stats,
crown-stats__inner, crown-style-scope, crown-testimonial, crown-testimonial__mark,
crown-testimonial__meta, crown-testimonial__quote, crown-testimonial__stars, crown-topbar,
crown-topbar__group, crown-topbar__icon, crown-topbar__inner, crown-topbar__text, crown-why,
crown-why__content, crown-why__image, crown-why__inner, crown-why__link, crown-why__media,
crown-why__title
```

## ACSS CONFIG PROVENANCE — imported, then changed

Compared every key in `claude/ssh-server-access-99xi0g`'s `crown-movers-acss-settings.json`
against what `automatic.css` actually serves on staging (`docs/audit/exports/automatic.css`,
captured in v1.0):

| | Settings JSON | Live `automatic.css` | |
|---|---|---|---|
| `--primary` hue + chroma | `h=36.4737, c=0.2239` | `oklch(0.65 0.2239 36.4737)` | **Exact match to 4 decimals** on hue and chroma; lightness differs by 0.004 (0.6641 vs 0.65 — a display-rounding artifact, not a different colour) |
| `--accent`, `--secondary`, `--tertiary` | Defined (accent `oklch(0.78 0.165 73.7)`, secondary, tertiary all present) | **Absent entirely** — not disabled, not zeroed, not in the file at all | |
| `--base` | `L=0.9741` (near-white) | `L=0.65` (`#978D87`, taupe) | Different |

A hue+chroma match this precise across 2,563 keys is not a coincidence. **Verdict: this settings
file (or one producing near-identical values) was imported into ACSS at some point, and the
config was changed afterward** — accent/secondary/tertiary were removed or reset, and base was
recalculated. This is "imported-then-changed," not "never imported" and not "unknown." It does
not, however, make this file a current source of truth — it describes a config state that no
longer exists.

## CPT REGISTRATION SOURCE — CONFIRMED (not just consistent)

Compared `claude/ssh-server-access-99xi0g`'s `acf-json/post_type_services.json`,
`post_type_service_areas.json`, and `taxonomy_service_region.json` field-by-field against the
live `wp-json-types.json` / `wp-json-taxonomies.json` from v1.0:

| Field | ACF JSON | Live REST | Match |
|---|---|---|---|
| `services` post_type slug | `services` | `services` (rest_base) | ✓ |
| `services` hierarchical | `false` | `false` | ✓ |
| `service-areas` post_type slug | `service-areas` | `service-areas` (rest_base) | ✓ |
| `service-areas` hierarchical | `false` | `false` | ✓ |
| `service-region` taxonomy slug | `service-region` | `service-region` (rest_base) | ✓ |
| `service-region` object_type | `['service-areas']` | `types: ['service-areas']` | ✓ |
| `service-region` hierarchical | `true` | `true` | ✓ |

Every field matches. **And critically, this repo's own alternative registration mechanism —
`wp-integration/01-post-types-and-taxonomies.php` on `main`/`claude/funny-carson-3fak46` —
registers entirely different slugs**: `location` (not `services`/`service-areas`) with
taxonomies `region` and `service_category` (not `service-region`). That PHP file is
**definitively ruled out** as the source of what's live — it can't be, the slugs don't exist on
staging at all. The ACF JSON on `ssh-server-access-99xi0g` is the only candidate that matches,
on every field checked. Confidence: high, pending only the trivial confirmation that this exact
file (not a look-alike) is what's active in `wp-content/plugins` or `mu-plugins` on staging —
that's a one-line `grep`/`diff` for v1.4, not a real doubt.

## BRANCH STATUS TABLE

| Branch | Last commit | Merged to `main`? | Contents | Disposition |
|---|---|---|---|---|
| `main` | `782dfc2` (2026-09-22) | — | Governing docs, `bricks/*.json` (27-file pack, rejected in v1.0), `wp-integration/*.php` (registers `location`/`region`/`service_category` — confirmed NOT what's live) | Base branch |
| `claude/funny-carson-3fak46` | `960a034` (2026-09-23) | No (PR #4 open) | v1.0–v1.5 audit trail | **Active** |
| `claude/ssh-server-access-99xi0g` | `5e4660a` (2026-08-24) | No | `bricks-json/{header,footer,home}.json`, `crown-movers-acss-settings.json`, `acf-json/*` | **Evidence-only.** Confirmed source of the live CPT/taxonomy registration and of the ACSS config's original palette hue. **Not** the source of the live Bricks page build. Do not modify; do not merge as-is (would delete the entire `docs/audit/` trail, `docs/crown-*.md`, and the current `bricks/`/`wp-integration/`). |
| `claude/zealous-rubin-9ngbym` | `b72d2b2` (2026-09-20) | No | Adds `10-archive-service.json`, `11-archive-location.json`, `14-archive-blog.json` + singles, on top of the same rejected 27-file pack | **Dead.** Its three archive templates directly contradict the recorded owner decision "no archive templates" (see `bricks/README.md` on `main`: "archive templates are not used anywhere on this site... confirmed by Saleem 2026-09-21"). Its Bricks pack is the same one v1.0 rejected. No reason to merge or build on it. |

## KNOWN CONFLICTS

1. **The live staging build's source is still open.** This is the one item v1.5 didn't close —
   it narrowed the field from "could be any of three branches" to "is none of the three
   branches," which is a real answer but not the one hoped for. v1.4 (SSH: `wp post list
   --post_type=bricks_template`, `bricks_global_classes` option) is the only way to find where
   this content actually lives (template posts vs. page-level content vs. something outside
   this repo entirely).
2. `zealous-rubin`'s three archive templates contradict the recorded no-archive-templates
   decision — flagged, not actioned (branch is dead, no merge is proposed).
3. The ACSS settings file's `--primary` still isn't Crown Coral (`#F04836`) — it's the same
   off-brand orange live on staging now, imported from this exact file. Confirms v2.0's palette
   work is a real reconfiguration, not a restore-from-file.

## DEVIATIONS FROM PROMPT

None. All five branches read-only; only `docs/audit/01-staging-build-provenance.md` written, on
`claude/funny-carson-3fak46`.
