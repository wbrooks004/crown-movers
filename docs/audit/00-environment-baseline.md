# WU1 — Environment Discovery & Baseline Audit

Run date: 2026-09-22 · Repo HEAD at start: `782dfc2` · Executor: Claude Code (remote cloud container)

This report has two layers, run in the same cloud session on the same date:

1. **First pass** (repo-only) — no staging URL had been supplied to this session yet.
2. **Second pass** ("WU1-R", HTTPS-only) — after the user supplied the staging host
   (`https://staging.crownmovers.ca`) mid-session. This cloud container still cannot open
   TCP/22 (confirmed again below), so everything SSH/WP-CLI-dependent is still blocked here.
   Everything reachable over plain HTTPS — REST, the served ACSS stylesheet, sitemaps,
   Playwright screenshots — was pulled directly in this session and is evidenced below.
   A separate reviewing conversation ("the Project") supplied a WU1-R repair prompt asserting
   specific staging facts (WP 7.1.1, ACSS 4.0.1, root font size 16px, etc.). Those claims were
   **not** taken on faith — every one of them was independently re-verified against the live
   staging host from this session before being included below, and each fact below cites its
   own export file, not the pasted claim.

PROMPT VERSION: WU1-rev3 was executed for the HTTPS half below (echoed retroactively per the
rev-4 reviewing pass's request). WU1-rev4 (the SSH half) has **not** been executed — this
cloud container still cannot open TCP/22; see CAPABILITY MATRIX. That work needs to run from a
session with SSH reach.

## STATUS — PARTIAL

HTTPS-reachable items: COMPLETE. SSH/WP-CLI-only items: BLOCKED (TCP/22 egress is closed from
this cloud container — see CAPABILITY MATRIX). Nothing was written to WordPress.

## CAPABILITY MATRIX

| Mechanism | Available | Demonstrated by |
|---|---|---|
| 1. SSH + WP-CLI to staging | **N from this cloud container** | `ssh -V` → `OpenSSH_9.6p1` (client installs fine); `timeout 8 bash -c 'echo > /dev/tcp/staging.crownmovers.ca/22'` (re-tested this pass) → connection refused/timeout, consistent with the first pass's `github.com:22` test. Egress here is HTTPS-only through the agent proxy. WP-CLI itself was never tested because there is no shell on the server reachable from here. |
| 2. WP REST (`/wp-json/`) over HTTPS | **Y** | `docs/audit/exports/wp-json-root.json` (`home`/`url` both `https://staging.crownmovers.ca`, confirming this is genuinely staging, not the unverified Cloudways host from the first pass) |
| 3. Public HTTPS GET (HTML, CSS, sitemaps, robots.txt) | **Y** | `docs/audit/exports/staging-home.html`, `automatic.css`, `staging-robots.txt`, `staging-sitemap_index.xml`, `prod-sitemaps/*.xml` |
| 4. Browser tooling (Playwright) against staging | **Y** | `docs/audit/screens/staging-home-1440.png`, `staging-home-390.png` — live navigation, `x-cache: MISS` confirms cache was bypassed, not a cached/stale render |
| 5. Novamira or another WordPress/Bricks MCP | **N** | Unchanged from the first pass — `ToolSearch` found none |
| MySQL client | N | Unchanged — `mysql: command not found` |

**Correction to the first pass:** that pass reported "no mechanism reaches staging" because no
staging URL had been supplied yet, not because HTTPS was blocked. HTTPS egress was never
blocked — only SSH (port 22) is. This pass demonstrates that distinction directly.

## VERSION MATRIX

| Component | Version | Evidence |
|---|---|---|
| WordPress (staging) | **7.1.1** | `<meta name="generator" content="WordPress 7.1.1">` in `staging-home.html`; `readme.html` returns 200 |
| WordPress (production, per original brief) | 7.1.2 | Not re-verified this pass (out of scope — GET-only, sitemaps only, on production) |
| ACSS | **4.0.1** | First line of `automatic.css`: `/* File: automatic.css - Version: 4.0.1 - Generated: 2026-08-24 07:49:30 */` |
| Bricks (page builder) | UNVERIFIED | No version string is exposed publicly. Body classes confirm Bricks + a `bricks-child` child theme are active (`wp-theme-bricks wp-child-theme-bricks-child brx-body bricks-is-frontend`) on every page checked (home, `/montreal-movers/`, `/junk-removal/`). The `bricks/v1` REST namespace is live but its template-listing endpoints require an authenticated builder session (`get-templates` → `my_templates_access_disabled`, HTTP 200 with an error body — correctly locked down, not a leak). |
| ACF Pro | UNVERIFIED | No public ACF REST namespace (`wp-json/acf/v3` → 404). ACF's REST API is off by default even when ACF Pro is active, so a 404 doesn't rule it out — genuinely unverified either way. |
| BricksExtras | UNVERIFIED | No public signal |
| WS Form | **Active**, edition unverified | `wp-json/ws-form/v1` → 200. Field/form-level detail (id, name, field count, actions) needs wp-admin or WP-CLI — blocked. |
| Polylang | **Active, 2 languages (en/fr)**, edition UNVERIFIED | `wp-json/pll/v1/languages` returns both languages with full metadata (`docs/audit/exports/staging-pll-languages.json`). **Correction to A2:** the presence of this endpoint does **not** prove Pro — [Polylang's own docs](https://polylang.pro/documentation/support/developers/languages-rest-api/) confirm the read-only Languages REST API shipped in Polylang **Free** since v3.7; only write operations and fallback-language management are Pro-gated. Edition is still genuinely unverified without the plugin list. |
| Rank Math | **Active** | `wp-json/rankmath/v1` → 200; staging serves its own `sitemap_index.xml` (Rank Math-generated, `main-sitemap.xsl` stylesheet reference) |
| Object cache plugin | **Active (new finding)** | `objectcache/v1` REST namespace present — not in anyone's plugin list so far (likely Redis Object Cache or similar). Identify it in the next SSH pass. |
| Oxygen / OxyExtras | **Not active on staging** | Body classes show Bricks only, no Oxygen markers. Production is confirmed Oxygen-based per the original brief — see KNOWN ISSUES, this contradicts assumption A3. |
| GTM | **GTM-KCRJXFC on both staging and production** | Same container ID found in both `staging-home.html` and a fresh production GET (`/tmp/prod-home.html`, not committed — production, GET-only) |
| Meta Pixel | Present on production, **absent from staging HTML** | `fbq('init','566013485066140')` found on production, zero `fbq(` matches on staging home |

## ACSS BASELINE — measured from `automatic.css` (served, not documentation)

Files: `docs/audit/exports/automatic.css` (66,498 bytes, 1,821 lines), `docs/audit/acss-variables.txt` (384 unique custom properties), `docs/audit/acss-classes.txt` (97 top-level utility classes).

| Item | Measured value | Note |
|---|---|---|
| **Root font size** | `--root-font-size: 100%`, and `html {font-size: var(--root-font-size)}` is in the served CSS | **A1 is REFUTED, not just unverified.** 1rem = 16px on staging, not 10px. No competing `html{font-size}` override was found in the fetched theme stylesheet. Every `clamp()`/rem value in `bricks/*.json` and `bricks/00-setup-acss-and-theme-styles.md` was computed against the wrong root size — recompute all of it against 16px before any import. |
| Enabled colour slots | **Primary, Base, Neutral, White, Black only** | `--accent`, `--secondary`, `--tertiary`, `--success`, `--danger` do **not exist** in the stylesheet at all — those ACSS features are off, not just unconfigured. Any `var(--accent)` or `var(--danger)` in the pack resolves to nothing. |
| `--primary` | `oklch(0.65 0.2239 36.4737)` → **`#F94600`** (converted; formula in `docs/audit/exports/capability-probe.txt` is not saved, recompute via standard OkLab→sRGB matrices if needed) | Not Crown Coral (`#F04836`). Visually confirmed orange, not coral-red, in `docs/audit/screens/staging-home-1440.png` (the "GET A FREE QUOTE" button). ACSS has **not** been configured to brand colours yet. |
| `--base` | `oklch(0.65 0.0143 50.8081)` → **`#978D87`** | A mid warm taupe — the opposite of the doctrine's intended dark-ink base (`#151515`). Base and neutral read as swapped from the brief's semantic mapping. |
| `--neutral` | `oklch(0.1776 0 0)` → **`#111111`** | Near-black. Under the brief's mapping this should be the mid-grey muted-text role; here it's what's rendering as heading/body ink. |
| `--btn-text-color` | `var(--secondary)` | **Confirmed broken reference** — `--secondary` doesn't exist on this install (see above), so this variable resolves to nothing and text colour falls back to whatever the browser/cascade supplies. Real defect on the live config, not a pack issue — flag for WU2. |
| Spacing scale | **5 steps only: `xs, s, m, l, xl`** | No `2xs`, no `2xl`. `bricks/00-setup-acss-and-theme-styles.md` explicitly assumes `--space-xs` through `--space-2xl` — **that assumption is now confirmed wrong**, not just unverified. Every `var(--space-2xl)` in the pack resolves to nothing. |
| Section spacing | `--section-space-{xs,s,m,l,xl}` + escalation variants (`-to-m`, `-to-s`, `-to-xs`) | Matches ACSS 4.x's documented naming |
| `--content-width` | `85.375rem` (≈1366px at 16px root) | Larger than the orchestration's 1280px target — a real number to design against, not the assumed one |
| `--gutter` | `clamp(1rem, 6.36vw + -0.43rem, 5rem)` | fluid |
| Radius | `--radius: 2px`; also `--radius-50: 50%`, `--radius-circle: 50vw`, `--radius-m: var(--radius)`, `--radius-none: 0` | Much smaller than the brief's 4–8px assumption |
| Shadows | `--box-shadow-1/2/3`, `--text-shadow-1/2/3`, `--drop-shadow-1/2/3` (not `--shadow-*`) | Naming differs from what the brief guessed |
| Button system | Full `--btn-*` variable set present (26 vars) + `.btn--{primary,primary-dark,primary-light,none}` and `.btn--{xs,s,m,l,xl,xxl}` size classes | No `outline`, `text-arrow`, `phone`, `mobile-sticky`, or `disabled/loading` button classes exist natively — those from the brief's Level-4 button variant list are custom BEM work, not ACSS |
| Typography | `--heading-font-family: Anton`, `--text-font-family: Roboto` | **Not Archivo/Inter.** ACSS has not been configured with brand fonts yet — this is placeholder/default, confirm with the client before WU2 assumes otherwise |
| Class naming convention | Double-dash BEM-ish modifiers: `.btn--primary`, `.section--l`, `.text--m`, `.bg--dark`, `.scheme--dark`, etc. (97 total) | This is ACSS 4.x's own utility naming — distinct from the pack's `block__element` component convention, which is correct per doctrine (utilities vs. components are different layers) |

## BRICKS BASELINE — partial

**Blocked without SSH/wp-admin:** theme styles JSON, breakpoints, global classes list, global
variables, template list, code-signing/permissions, performance settings, Google Fonts setting,
custom CSS/JS in the child theme.

**Measured anyway, and this is the single most important finding in this pass:**

**Staging already has a live, in-progress Bricks build — this is not a blank or Oxygen-only
environment waiting for import.** Checked three templates (home, `/montreal-movers/`,
`/junk-removal/`):

- All three render through Bricks (`bricks-is-frontend`, `brxe-*` element classes), not Oxygen,
  not a raw content dump.
- The homepage uses `brxe-heading`, `brxe-image`, `brxe-button`, `brxe-icon`, plus two
  auto-generated component-instance classes (`brxe-mmctxe`, `brxe-vctqsz`, `brxe-wfpxfu`) —
  i.e. **reusable Bricks Components have already been created and are in use**, which this repo
  has no record of.
- `/montreal-movers/` (a Protected SEO Asset per the spec) and `/junk-removal/` also render
  through Bricks with real heading/body copy, not placeholder content.
- The homepage's rendered colours (orange primary button, warm-taupe/near-black text) match
  exactly the unconfigured ACSS palette measured above — evidence this build is using the
  *current, not-yet-branded* ACSS config, not a separately hardcoded palette.

This means: someone has been building directly in the Bricks editor on staging, independent of
`bricks/*.json` and independent of this repo. **Before any WU2+ styling or import work, the
actual state of that build — which templates exist, which components, whether they're
throwaway or meant to be kept — needs to be inventoried (SSH: `wp post list
--post_type=bricks_template`, and the `bricks_global_classes` option) and reconciled with the
client, not silently overwritten.** This is exactly the kind of requirements/exports
contradiction CLAUDE.md says to report, not merge.

## STAGING vs PRODUCTION PARITY

| Metric | Value | Source |
|---|---|---|
| Staging pages (`wp/v2/pages`, all statuses the REST default returns) | **409** | `X-WP-Total` header |
| Staging posts | **46** | `X-WP-Total` header |
| Staging `services` CPT | **0** | `X-WP-Total` header — CPT is registered (confirms `wp-integration/01-post-types-and-taxonomies.php` is active on staging) but empty |
| Staging `service-areas` CPT | **0** | Same |
| Staging media library | **950 items** | `X-WP-Total` on `wp/v2/media` |
| Polylang term counts | EN language term: 670 objects tagged; FR language term: 583 | `docs/audit/exports/staging-pll-languages.json` `term_props.language.count` |
| `?lang=` REST filtering | **Broken** | `wp/v2/pages?lang=en` and `?lang=fr` both return 409 (identical), even with a cache-busting query string (`x-cache` header absent, confirming it wasn't just a cached response). Polylang's REST language filter is not wired up for the `pages` endpoint on this install. |
| Production sitemap total | **425 unique paths** (443 raw `<loc>` rows, 18 of which are duplicate paths listed under two different hostnames) | `docs/audit/live-url-inventory-2026-09-22.csv`, computed from `docs/audit/exports/prod-sitemaps/*.xml` — matches the original brief's 425 exactly once duplicates are resolved |

Oxygen-vs-Bricks rendering counts on production, and exact post-type × language breakdowns on
staging, still need SSH/DB access — the REST totals above don't distinguish language or builder
per row without per-page fetches (avoided here to stay within a reasonable number of requests).

## SEO CONFIG

- **Sitemap hostname leak — CONFIRMED, and worse than described.** 198 of 443 rows in
  production's sitemaps resolve to `wordpress-1663747-6631130.cloudwaysapps.com` instead of
  `www.crownmovers.ca` — all 196 in `page-sitemap1.xml`, plus 2 in `local-sitemap.xml`. This is
  **not** the staging host (staging is confirmed to be `staging.crownmovers.ca`) — it's a third,
  still-unidentified Cloudways app URL baked into Rank Math's cache. Worse: `page-sitemap1.xml`
  and `page-sitemap2.xml` both list 196 paths each, and **17 of those paths are identical** —
  meaning Rank Math is emitting the *same page* as two separate indexable URLs on two different
  hostnames. That's a duplicate-content problem, not just a cosmetic wrong-domain one. Full
  breakdown in `docs/audit/live-url-inventory-2026-09-22.csv`.
- Staging robots.txt (`docs/audit/exports/staging-robots.txt`) disallows only `/wp-admin/` and
  points its `Sitemap:` directive at **`https://www.crownmovers.ca/sitemap.xml`** — the
  production domain, not itself. Low risk (doesn't block crawling) but confusing and worth
  fixing before staging is ever left reachable long-term.
- **Staging indexability is ON for English, OFF for French — inconsistent, and not a
  deliberate "discourage search engines" setup.** EN homepage: `<meta name="robots"
  content="follow, index">`, no `X-Robots-Tag` header. FR homepage: `<meta name="robots"
  content="nofollow, noindex">`. Neither is what you'd want for a staging site (both should be
  noindex) — flag this to whoever owns staging.
- hreflang tags are present and correct on the homepage (`en` → `staging.crownmovers.ca/`,
  `fr` → `staging.crownmovers.ca/fr/`); no `x-default` tag, minor.
- **Correction:** a reviewing pass flagged "no `<h1>` in the exported HTML" as a defect. Checked
  directly — there is exactly one: `<h1 class="brxe-heading crown-display crown-hero__title">`
  in `staging-home.html`, plus a correct H2/H3 hierarchy below it (6×H2, 3×H3, no skipped
  levels). Heading structure on the home page is not a defect.
- Rank Math is confirmed generating staging's own `sitemap_index.xml` independently of
  production's.

## MEDIA INVENTORY

Staging media library: **950 items** (`wp/v2/media` total). Did not enumerate the 13
manifest-image URLs against staging — the manifest's `source_url` values all point at
`www.crownmovers.ca` (production), so that check belongs against production, not staging, and
production access here is GET-only on sitemaps per scope.

## FORMS INVENTORY

WS Form is active (`wp-json/ws-form/v1` → 200). Form list, field counts, and configured
actions/webhooks require wp-admin or WP-CLI — blocked from this session.

## TRACKING

GTM container `GTM-KCRJXFC` is identical on staging and production — **not isolated**. Whether
staging events are filtered out of GA4/Ads reporting inside GTM itself can't be determined from
HTML alone (would need GTM admin access) — don't assume it's handled. Meta Pixel was not found
in staging's HTML source, so at minimum that one tracker is currently absent from staging (that
could change if it fires via GTM rather than being hardcoded — not verifiable from here).

## CLAUDE.md DEPENDENCY CHECK

(Unchanged from the first pass — this is a repo-only check, not staging-dependent.)

| Referenced item | Status | Path / evidence |
|---|---|---|
| `.claude/rules/frontend-doctrine.md` | **Absent** | No `.claude/` in the repo |
| `bricks-acss-frontend` skill | **Absent** | Not in the skills list |
| `modern-web-guidance` skill | **Absent** | Not in the skills list |
| `css-researcher` agent | **Absent** | Not an available agent type |
| `frontend-auditor` agent | **Absent** | Not an available agent type |
| Bricks skill (`SKILL.md`, `references/json-formats.md`, `theme-styles.md`, `components-classes.md`) | Present | `~/.claude/skills/synced/<org>/bricks/` |
| `fms-bricks-html` skill (not referenced by CLAUDE.md) | Present | Same synced directory |

## CHANGES MADE

None on WordPress. Verified by mechanism: every staging request this pass was `curl -sS` (GET)
or a Playwright `page.goto()`/`page.screenshot()` — no POST/PUT/DELETE was issued, and the two
non-GET-capable endpoints discovered (`bricks/v1/get-templates`, `pll/v1/languages` POST
variant) were either not called or called with GET only. Production was touched only via GET on
its public sitemap files, per scope. Repo: files under `docs/audit/` only.

## FILES CREATED

```
docs/audit/00-environment-baseline.md
docs/audit/acss-variables.txt                    (384 custom properties)
docs/audit/acss-classes.txt                      (97 utility classes)
docs/audit/live-url-inventory-2026-09-22.csv     (443 rows / 425 unique paths)
docs/audit/exports/capability-probe.txt
docs/audit/exports/bricks-pack-measurements.txt
docs/audit/exports/wp-json-root.json
docs/audit/exports/wp-json-types.json
docs/audit/exports/wp-json-taxonomies.json
docs/audit/exports/staging-robots.txt
docs/audit/exports/staging-home.html
docs/audit/exports/staging-home-headers.txt
docs/audit/exports/staging-fr.html
docs/audit/exports/automatic.css
docs/audit/exports/staging-sitemap_index.xml
docs/audit/exports/staging-bricks-theme-style.css
docs/audit/exports/staging-pll-v1.json
docs/audit/exports/staging-pll-languages.json
docs/audit/exports/staging-rankmath-v1.json
docs/audit/exports/staging-bricks-v1.json
docs/audit/exports/prod-sitemaps/{post,page1,page2,page3,local}-sitemap*.xml
docs/audit/screens/staging-home-1440.png
docs/audit/screens/staging-home-390.png
```

## SCREENSHOTS

`docs/audit/screens/staging-home-1440.png`, `staging-home-390.png` — live Playwright captures
of `/?nocache=1`, confirmed `x-cache: MISS` on that specific request. **Clarification:**
`staging-home-headers.txt` is a separate, earlier `curl -I` against the plain `/` URL (no
cache-buster) and correctly shows `x-cache: HIT` — that's Breeze serving its normal cached
response to a normal request, not a contradiction of the screenshot capture, which used a
different cache key on purpose.

## ASSUMPTIONS

| ID | State | Evidence |
|---|---|---|
| A1: 1rem = 10px | **REFUTED** | `automatic.css`: `--root-font-size: 100%`; `html{font-size:var(--root-font-size)}` in served CSS. Actual is 16px. |
| A2: Polylang Pro | **Still unverified** (narrowed) | 2 languages active is confirmed. The specific evidence that would have suggested Pro (the `pll/v1` REST namespace) doesn't actually distinguish editions — that endpoint has shipped in Polylang Free since v3.7. Plugin list (SSH) is the only way to settle this. |
| A3: staging is a recent clone of production | **Partially refuted** | Content counts are in the right range (409 pages / 46 posts vs. 425-URL production sitemap), so *content* looks cloned. But staging runs **Bricks**, not **Oxygen** — production is confirmed Oxygen. Staging is not a pure content-and-config clone; someone has already switched the builder and started building templates there (see BRICKS BASELINE). |

## KNOWN ISSUES (affect WU2+, ranked by impact)

1. **Staging already has an in-progress Bricks build (home page, `/montreal-movers/`,
   `/junk-removal/` all confirmed) with custom reusable Components.** This is not accounted for
   anywhere in this repo or the original orchestration. Get an SSH pass to inventory
   `bricks_template` posts and `bricks_global_classes` before writing or importing anything —
   otherwise WU2+ risks overwriting work nobody told this process about.
2. **A1 was wrong, not just unverified.** Root font size is 16px, not 10px. Every `rem`/`clamp()`
   value in `bricks/*.json` and `bricks/00-setup-acss-and-theme-styles.md` needs recomputing
   against the correct base before any of that pack is used as reference.
3. **`--space-2xl` doesn't exist** (confirmed, not just "unverified" as the first pass said) —
   the ACSS spacing scale on staging tops out at `xl`. Same for `--accent`, `--secondary`,
   `--tertiary`, `--danger`, `--success` — none exist. The orchestration's §5 colour-role table
   assumes an `--accent` slot that is not currently enabled.
4. **`--btn-text-color: var(--secondary)` is a broken reference on the live ACSS config** —
   `--secondary` doesn't exist, so button text colour is currently falling back to browser
   default, not a designed value. Real defect, independent of this project's build.
5. **ACSS has not been configured with brand colours or fonts.** Live primary is `#F94600`
   (orange, not `#F04836` coral), base is a mid taupe (not ink), typography is Anton/Roboto (not
   Archivo/Inter). WU2's job is exactly this, but don't assume any of it is half-done.
6. **Production's sitemap hostname leak includes real duplicate URLs**, not just wrong-domain
   ones — 17 paths are indexed twice, once per hostname. Escalate to whoever owns Rank Math
   settings; it's outside this rebuild's scope but is actively live.
7. Staging indexability is inconsistent (EN indexable, FR noindexed) and neither is the
   deliberate "block all of staging" state you'd want. Low urgency, easy fix, flag it.
8. GTM container is shared, unfiltered as far as can be observed, between staging and
   production.
9. The CLAUDE.md skills, agents and rules are still missing (unchanged from the first pass).
10. Palette-mapping contradiction between `04-crown-movers-colour-tokens.css` and
    `bricks/00-setup-acss-and-theme-styles.md` (carried over from the first pass) — resolve
    which file is canonical in WU2; note that *neither* file's hex values match what's actually
    configured on staging (see #5).

## WHAT STILL NEEDS SSH (nothing here changed the underlying constraint)

Exact plugin versions and Polylang/WS Form editions, Bricks theme styles JSON, global classes
list, global variables, existing `bricks_template` posts, breakpoints, Google Fonts/performance
settings, DB-level post-type × language × builder parity counts, and WS Form's form/field/action
inventory all still require either SSH+WP-CLI or a wp-admin application password. This cloud
session cannot open TCP/22 regardless of credentials supplied — that part of WU1-R has to run
from local Claude Code (which has your SSH access) or be supplied as committed WP-CLI output.

## DEVIATIONS FROM PROMPT

1. **Branch.** Commits went to `claude/funny-carson-3fak46` (this session's assigned branch),
   not `audit/wu1-environment-baseline` / `audit/wu1-baseline-r`. Contents are `docs/audit/**`
   only both times.
2. Did not attempt any SSH/WP-CLI commands beyond the port-22 reachability test — there is no
   path to run them from this container, so no output could be produced or fabricated.
3. Skipped enumerating individual pages for full post-type × language parity (would require
   ~450+ sequential requests); relied on aggregate REST totals and Polylang's own term counts
   instead. Flagged as a remaining gap rather than silently omitted.
