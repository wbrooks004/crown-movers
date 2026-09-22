# Frontend Development Doctrine

This file is the constitution: what I believe, what has authority, how I expect you to work.
The checks and decision procedures are in `.claude/rules/`. Bricks and ACSS execution is in
the `bricks-acss-frontend` skill.

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

- Current web-platform knowledge comes from the `modern-web-guidance` skill. Consult it before
  frontend work, however small the task looks.
- Build in the main context. Research with the `css-researcher` agent. Audit with the
  `frontend-auditor` agent. Keep browsing and checklists out of the build context.
- Follow the checks in `.claude/rules/frontend-doctrine.md` before writing frontend code.
- Report contradictions between requirements, exports, and docs. Do not merge them silently.
- New information updates the one canonical rule it affects. Never append dated update logs.
