# Frontend Development Doctrine

This file is the constitution: what I believe, what has authority, how I expect you to work.
Bricks JSON authoring uses the installed `anthropic-skills:bricks` skill (verified against
Bricks 2.3.6 source; the installed site runs 2.4.1 — treat any schema difference you find as a
real one to verify against a fresh export, not the skill's word alone). There is no
`.claude/rules/` directory and no `bricks-acss-frontend`, `modern-web-guidance`,
`css-researcher`, or `frontend-auditor` skill/agent in this environment — confirmed absent,
not just unused (`docs/audit/00-environment-baseline.md`, CLAUDE.md DEPENDENCY CHECK). Don't
assume they exist in a future session either; verify before relying on any of them again.

## What I believe

The platform comes first. Prefer native HTML and CSS over JavaScript when the platform provides
the capability. Use semantic HTML before making any styling decision.

Styling is class-first and low-specificity. Reusable patterns are BEM-style semantic component
classes. Utility-class soup and specificity escalation are defects.

Design decisions live in tokens. Never invent an arbitrary value when an existing design-system
token can express it. Never redefine framework tokens.

Related selectors, states, queries, and children are grouped with native CSS nesting, kept
shallow.

Responsive behaviour escalates: static, then intrinsic, then container query, then media query.
Use the lowest-complexity technique that correctly models the relationship. Breakpoints are
chosen where a layout actually breaks, never from a device list.

The default compatibility target is Baseline Widely Available. Newer features are welcome when
they improve the result and degrade gracefully.

## What has authority

On projects using Automatic.css, ACSS is the design-system authority. Never build another
design system on top of it. Extend it only when it genuinely lacks a semantic concept the site
requires.

The installed version decides which documentation applies. ACSS 3.x and 4.x are not
interchangeable; never mix their workflows.

In Bricks, reusable styling belongs on global classes at the smallest appropriate scope. Element
ID styling is the exception.

When guidance conflicts, use this order:

1. Current project requirements
2. Project ACSS export or settings
3. Project Bricks configuration and data
4. Current official Automatic.css documentation for the installed version
5. Current official Bricks documentation
6. Modern Web Guidance and current web-platform compatibility
7. This doctrine and `.claude/rules/`
8. Kevin Geary methodology where compatible
9. General model knowledge

The project export beats the docs. Never guess a framework token, recipe, utility, or API when
it can be verified.

## How I expect you to work

- Verify current web-platform behaviour against official sources when it matters; no dedicated
  skill for this is installed here.
- Build directly against the real project exports, not memory or a skill's built-in assumptions:
  `2026-09-23--acss-export.json` / `docs/audit/exports/ssh/opt-automatic_css_settings.json` for
  ACSS, `acf-json/` for CPT/taxonomy/field-group registration, `docs/audit/exports/ssh/` for
  every other measured fact about the staging install (plugin versions, global classes, Polylang
  edition, etc.). `docs/audit/00-environment-baseline.md` and
  `docs/audit/01-staging-build-provenance.md` are the canonical record of what's actually
  installed and what's actually live — read them before assuming anything about the environment.
- Report contradictions between requirements, exports, and docs. Do not merge them silently.
- New information updates the one canonical rule it affects. Never append dated update logs.
- `bricks-json/` holds paste/import-ready Bricks JSON built against verified ACSS variables and
  real global classes (`docs/audit/exports/ssh/opt-bricks_global_classes.json`) — never against
  guessed hex/px values. `bricks/` (root) is the original 27-file pack; it was rejected as a
  styling source (hardcoded values, a parallel `u-*` utility layer, native Bricks forms instead
  of WS Form) and kept only as structural/content reference.
