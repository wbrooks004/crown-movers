# WU1 — Environment Discovery & Baseline Audit

Run date: 2026-09-22 · Repo HEAD at start: `782dfc2` · Executor: Claude Code (remote cloud container)

## STATUS — BLOCKED (staging) / COMPLETE (repo-only items)

No staging URL, SSH key, WP-CLI, application password, or WordPress MCP exists in this
execution environment. Every staging item is unverified. The repo-only items are complete.
The Cloudways hostname (`wordpress-1663747-6631130.cloudwaysapps.com`) was **not** contacted:
nobody has confirmed whether it is production or staging, and the prompt forbids any access
to production.

## CAPABILITY MATRIX

Verbatim output: `docs/audit/exports/capability-probe.txt`.

| Mechanism | Available | Demonstrated by |
|---|---|---|
| 1. SSH + WP-CLI to staging | **N from this cloud container** | The SSH client installs (`OpenSSH_9.6p1`), but outbound TCP port 22 is blocked (`tcp/22 egress: blocked`); egress is HTTPS-only through the agent proxy. `wp` is not installed locally, which is expected because WP-CLI would run on the server. The user reports that SSH works from their side, so the mechanism exists but must run from a local Claude Code session or their terminal. |
| 2. WP REST (`/wp-json/`) | **N** | No staging URL supplied and no credentials in env. General outbound HTTPS works through the agent proxy, so REST becomes Y as soon as a URL and an application password are supplied. |
| 3. Browser tooling (Playwright) | **Y, local only** | `playwright 1.56.1 chromium 141.0.7390.37 screenshot ok` (probe of a local page at 390px). No staging target, so no staging screenshots were taken. |
| 4. Novamira or another WordPress/Bricks MCP | **N** | ToolSearch `wordpress bricks novamira` → `No matching deferred tools found`. The connected MCPs are GitHub, Drive, Gmail, Calendar, ClickUp, Canva, Figma, Context7 and Claude Docs. None of them touches WordPress. |
| MySQL client | N | `mysql: command not found` |

## VERSION MATRIX

| Component | Staging version | Source |
|---|---|---|
| WordPress, PHP, Bricks, ACSS, ACF Pro, BricksExtras, WS Form, Polylang (edition), Rank Math, Oxygen, OxyExtras, NotificationX, GS Logo Slider, Breeze, others | **UNVERIFIED** | Blocked: no mechanism reaches staging |
| Bricks schema the repo pack targets | 2.3.6 | `"version": "2.3.6"` in 21 of 29 `bricks/*.json` (the other 8 have no `version` key) |
| Bricks schema the installed skill targets | 2.3.6 | `bricks/SKILL.md`: "Verified against Bricks 2.3.6 source" |

## ACSS BASELINE — UNVERIFIED (blocked)

Not produced: the settings export, `acss-variables.txt` and `acss-classes.txt`. Per the DoD they
must come from the stylesheet staging serves, and I did not reconstruct them from docs or memory.
The root font size, palette slots, shades, spacing and section spacing, content width, gutter,
radius, shadows, button system, typography scale and option groups are all unmeasured.

## BRICKS BASELINE — UNVERIFIED (blocked)

Nothing was measured on staging: theme styles, breakpoints, global classes and variables,
templates, code signing, performance and Google Fonts settings, and custom CSS/JS.
The known-good schema sample (`_bricks_page_content_2`, `_bricks_template_settings`,
`bricks_global_classes`, `bricks_global_variables`) was not exported.

**Repo-side measurements** (`docs/audit/exports/bricks-pack-measurements.txt`). These correct
some figures in the orchestration verdict:

| Metric | Verdict said | Measured |
|---|---|---|
| JSON files in `bricks/` | 27 | **29** (00-theme-styles + 01–27 + 02b) |
| Global classes | 140 | **107 unique names** / 310 definitions incl. cross-file duplicates |
| `u-*` utility classes | layer present | 16 (`u-gap-*`, `u-max-*`, `u-bg-*`, `u-pad-2xl-y`, `u-row-wrap-center`, `u-text-center`, `u-mt-2xs`, `u-img-cover-fill`) |
| `8px` / `12px` / `14px` / `22px` | 135 / 72 / 48 / 46 | 137 / 72 / 48 / 46 |
| `760px` / `560px` / `999px` | present | 17 / 7 / 24 |
| Hex literals | `#FFFFFF`, `#F7F5F1` | `#FFFFFF` ×56, `#F7F5F1` ×16, **`#D93E2E` ×14** (coral hover, not flagged before), `#FFF4EE` ×2 |
| `clamp()` | theme styles | 11 |
| Native Bricks `form` elements | present | 5 |

These numbers support the verdict: the pack is not usable as a styling foundation.

## STAGING vs PRODUCTION PARITY — UNVERIFIED (blocked)

I did not compute these: counts by post type and language, Oxygen vs Bricks rendering counts,
the discourage-indexing and server-level noindex state, and the hostname/search-replace state.
`docs/audit/live-url-inventory-2026-09-22.csv` is **absent** from the repo, so the production side
of the table has no committed source either.

## FORMS INVENTORY — UNVERIFIED (blocked)
## SEO CONFIG — UNVERIFIED (blocked)
## MEDIA INVENTORY — UNVERIFIED (blocked)

Repo side only: `07-existing-site-photo-manifest.csv` has a header and **13 data rows**. All 13
`source_url` values point at `www.crownmovers.ca` (production), so I did not fetch them for pixel
dimensions.

## CLAUDE.md DEPENDENCY CHECK

| Referenced item | Status | Path / evidence |
|---|---|---|
| `.claude/rules/frontend-doctrine.md` | **Absent** | No `.claude/` in the repo. Filesystem-wide `find` found nothing. |
| `bricks-acss-frontend` skill | **Absent** | Not in the skills list. `find` found nothing. |
| `modern-web-guidance` skill | **Absent** | Not in the skills list. `find` found nothing. |
| `css-researcher` agent | **Absent** | `~/.claude/agents` does not exist, and it is not an available agent type |
| `frontend-auditor` agent | **Absent** | Same as `css-researcher` |
| Bricks skill (`SKILL.md`, `references/json-formats.md`, `theme-styles.md`, `components-classes.md`) | Present | `~/.claude/skills/synced/<org>/bricks/` |
| `fms-bricks-html` skill (not referenced by CLAUDE.md) | Present | Same synced directory |

CLAUDE.md's "How I expect you to work" section is not executable as written in this environment.

## CHANGES MADE

None on WordPress: no mechanism in this environment can reach it (see capability matrix).
Repo: files under `docs/audit/` only.

## FILES CREATED

- `docs/audit/00-environment-baseline.md`
- `docs/audit/exports/capability-probe.txt`
- `docs/audit/exports/bricks-pack-measurements.txt`

## ELEMENT-LEVEL STYLING AUDIT — N/A (no build)
## INLINE CSS AUDIT — N/A (no build)
## HARD-CODED DESIGN VALUE AUDIT — N/A (no build)

## SCREENSHOTS

None of staging. The Playwright probe screenshot was a local test page and is not committed.

## ASSUMPTIONS

| ID | State | Evidence |
|---|---|---|
| A1: 1rem = 10px | **Still unverified** | Only source is `bricks/README.md` ("confirmed"), which is a repo claim, not a measurement |
| A2: Polylang Pro | **Still unverified** | `docs/crown-context.md:163` and `docs/crown-bricks-acss.md:15` state the intent. The installed edition is unknown. |
| A3: staging is a recent clone of production | **Still unverified** | No staging access |

## KNOWN ISSUES (affect WU2+)

1. **Palette-mapping contradiction, unresolved in the repo.** `04-crown-movers-colour-tokens.css:27–32`
   maps `--primary: ink`, `--action: coral`, `--base: #F7F5F1`. `bricks/00-setup-acss-and-theme-styles.md`
   maps `--primary: #F04836`, `--base: #151515`. ACSS 4.x has no `--action` slot. The orchestration's
   §5 resolves this in favour of the setup doc, but the token files still carry the other mapping.
   Decide which file is canonical and retire the other in WU2.
2. `--space-*`, `--danger`, `--success` and `--focus` names in the pack are self-declared assumptions
   (`bricks/00-setup…md` §1–2). They can't be checked until the ACSS stylesheet is extracted.
3. The pack contains 5 native Bricks form elements. They conflict with the WS Form-only rule.
4. The CLAUDE.md skills, agents and rules are missing (see table above).
5. `live-url-inventory-2026-09-22.csv` was never committed.
6. The designated push branch differs from the prompt (see DEVIATIONS).

## WHAT UNBLOCKS THE REST (in order of value)

| # | Supply | Unblocks | Effort (you) |
|---|---|---|---|
| 1 | Written confirmation of which Cloudways app is staging, plus its URL | Everything below. Also resolves whether the sitemap leak is a staging host. | 2 min |
| 2 | WP application password for a staging admin, supplied as env vars on this cloud environment (not pasted into chat) | REST: versions (`/wp-json/wp/v2/plugins`), post types, page counts per language, template list. Unauthenticated reads also give the frontend ACSS stylesheet → `acss-variables.txt` / `acss-classes.txt` | 5 min |
| 3 | Re-run WU1 from **local** Claude Code, which has your SSH access, or run the WP-CLI commands yourself and commit the output to `docs/audit/exports/`. This cloud container cannot open port 22. | Option dumps (ACSS settings, `bricks_global_*`, theme styles, Polylang, Rank Math), meta parity counts, WS Form actions | 10–20 min |
| 4 | Staging basic-auth credentials, if the site sits behind it | Playwright screenshots at 1440/390 | 2 min |

Items 1 and 2 cover roughly 70% of the checklist. Only item 3 yields raw option exports.

## DEVIATIONS FROM PROMPT

1. **Branch.** The prompt specifies `audit/wu1-environment-baseline`. This session is restricted to
   pushing `claude/funny-carson-3fak46`, so the commit went there. Contents are `docs/audit/**` only.
   Rename or cherry-pick into `audit/wu1-environment-baseline` if the name matters.
2. Status is BLOCKED/PARTIAL rather than COMPLETE, for the reasons above.
