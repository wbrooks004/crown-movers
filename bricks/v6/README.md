# Crown Movers v6.0 — component library (draft)

Format: Bricks clipboard JSON, `version` 2.4.1, generated 2026-09-24 from `gen_v6.py`.
Import: Bricks builder → right-click canvas → *Paste* (Ctrl/Cmd+V after copying the file contents). Global classes ride with each file and merge by name.

## Gates before import
1. **v2.0 saved** — classes reference `--accent`, `.btn--neutral`, `--radius` ≥ 6px; on the current dashboard those render missing/tiny.
2. **v3.0 done** — the stale `hero__*`, `section-header*`, `eyebrow`, `faq__*`, `stats*`, `process*`, `testimonial*`, `pit-*`, `u-*` global classes must be deleted first. Bricks merges pasted classes **by name onto the existing class** and keeps the existing (Montserrat/`--secondary`) settings, so a paste over stale classes silently loses these styles.

## Rules these files obey
- Zero element-level style keys (generator asserts it). Zero hex/rgb. Zero px except the 1px ACSS `--border-size` equivalent on cards and one documented 4px exception.
- Every colour, size, gap, radius, shadow, transition is an ACSS variable verified in `docs/audit/acss-variables.txt`.
- ACSS utilities attached as plain classes: `section--m`, `bg--ultra-light`, `bg--ultra-dark`, `btn--primary`, `btn--neutral`, `btn--m`.
- Layout grids use ACSS grid variables (`--grid-auto-3`, `--grid-auto-4`, `--grid-2`) — ACSS 4 registers no grid utility classes on this install.

## Documented exceptions
- `section-header` / `faq` max-width `62ch` / `72ch` — typographic measure; ACSS has no measure token.
- `testimonial-card` 4px accent rule — no ACSS token for a thick rule; single occurrence in `_cssCustom`.
- `mobile-actions` sets `body { padding-bottom }` under 767px so the fixed bar never covers content.

## Content placeholders
Every `[VERIFY]` string is unsupported by project evidence and must not ship. Form id 4 = *Quick Quote Form EN*, 5 = FR (from `wsform-forms.tsv`). Phone 514-606-4030 is the number on the live site header.

## Class ledger
| Class | id | ACSS tokens used |
|---|---|---|
| `eyebrow` | `be8b21` | `--primary`, `--text-xs` |
| `section-header` | `c2f53d` | `--space-l`, `--space-xs` |
| `section-header--center` | `c0ea7e` | — |
| `section-header__intro` | `ace57d` | `--text-dark-muted`, `--text-l` |
| `service-card` | `c8b6fc` | `--box-shadow-1`, `--neutral-light`, `--primary`, `--radius`, `--space-m`, `--space-s`, `--transition`, `--white` |
| `service-card--featured` | `ce9d85` | `--neutral-ultra-light`, `--primary` |
| `service-card__icon` | `e17573` | `--icon-size-m`, `--primary` |
| `service-card__title` | `d232c0` | `--h4` |
| `service-card__body` | `e8c23c` | `--text-dark-muted` |
| `service-card__link` | `e9d797` | `--focus-color`, `--focus-offset`, `--focus-width`, `--primary` |
| `location-card` | `cdc267` | `--box-shadow-1`, `--focus-color`, `--focus-offset`, `--focus-width`, `--neutral-light`, `--neutral-ultra-light`, `--primary`, `--radius`, `--space-s`, `--space-xs`, `--transition` |
| `location-card__title` | `cc5216` | `--h5` |
| `location-card__meta` | `c79ff4` | `--text-dark-muted`, `--text-s` |
| `testimonial-card` | `cc5ede` | `--neutral-light`, `--primary`, `--radius`, `--space-m`, `--space-xs`, `--white` |
| `testimonial-card__stars` | `cb2bfc` | `--accent` |
| `testimonial-card__quote` | `cebadc` | `--text-m` |
| `testimonial-card__author` | `c93627` | — |
| `testimonial-card__meta` | `ccbbbc` | `--text-dark-muted`, `--text-xs` |
| `faq` | `a572e0` | — |
| `faq__item` | `fd783a` | `--divider-color-dark`, `--divider-size`, `--space-xs` |
| `faq__question` | `a72874` | `--text-l` |
| `faq__answer` | `c2ac85` | `--space-xs`, `--text-dark-muted` |
| `card-grid` | `a6b0dc` | `--grid-auto-3`, `--grid-gap` |
| `card-grid--4` | `fc064f` | `--grid-auto-4` |
| `process` | `c009f2` | `--grid-auto-3`, `--grid-gap` |
| `process-step` | `d261df` | `--space-xs` |
| `process-step__number` | `cdde6b` | `--h2`, `--primary` |
| `process-step__title` | `c1d152` | `--h5` |
| `process-step__text` | `df8074` | `--text-dark-muted` |
| `stats` | `cbae62` | `--grid-auto-4`, `--grid-gap` |
| `stat-item` | `c68c21` | `--space-xs` |
| `stat-item__value` | `cc8aae` | `--h1`, `--primary` |
| `stat-item__label` | `a441d2` | `--text-dark-muted`, `--text-s` |
| `quote-panel` | `b4c3c6` | `--grid-1`, `--grid-2`, `--space-l` |
| `quote-panel__content` | `c0057d` | `--space-s` |
| `quote-panel__trust` | `c17658` | `--space-xs` |
| `quote-panel__trust-item` | `cd1aad` | `--accent`, `--text-s` |
| `quote-panel__form` | `c4153f` | `--box-shadow-2`, `--radius`, `--space-m`, `--white` |
| `mobile-actions` | `da3d25` | `--border`, `--space-xs`, `--space-xxl`, `--white` |
| `mobile-actions__btn` | `d7618c` | — |
