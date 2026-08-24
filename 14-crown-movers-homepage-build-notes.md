# Crown Movers Homepage — Build Notes (v2, rebuilt on ACSS)

The first pass of `bricks-json/home.json` hand-rolled Bricks-native inline styling —
per-element pixel padding/radius/shadow, manually specified grid breakpoints — instead of
using the ACSS design system already built this session. That was wrong; this version fixes
it. Same real content, completely different construction.

## What changed

- **No magic-number pixels for structure.** Spacing, radius, and shadows come from ACSS's own
  generated variables — confirmed live in `crown-movers-acss-settings.json`
  (`option-space-variables`, `option-radius-variables`, `option-auto-grid-variables` are all
  `"on"`; `section-padding-block` already maps to `var(--section-space-m)`) — not a parallel
  hand-rolled scale. `var(--space-s/m/l/xl)`, `var(--radius)`/`var(--radius-s)`/`var(--radius-l)`,
  `var(--box-shadow-1/2/3)` throughout instead of `"22px"`, `"18px"` etc.
- **No bespoke per-element CSS for structure.** `section`, `container`, `grid`/`grid--2`/
  `grid--3` are applied as plain ACSS utility classes (`_cssClasses: "grid grid--3"`) — ACSS's
  own compiled stylesheet defines these once the settings are imported; Bricks doesn't
  redefine them. Same for the auto-grid responsive collapse (mobile/tablet column counts) —
  that's what `option-auto-grid-variables` is for, so there's no hand-written
  `_gridTemplateColumns:tablet_portrait` override anywhere in this version.
- **Buttons use ACSS's own button classes** (`_cssClasses: "btn primary"`,
  `"btn outline primary"`) instead of hand-rolled gradient/shadow/padding per button. This
  means the 18-fix accessibility pass from earlier — every `btn-{role}-*-text` color checked
  against WCAG and corrected — now actually applies to every button on the page automatically,
  which it didn't in the first version.
- **A small, disciplined set of custom global classes** for the few things ACSS doesn't
  natively provide (`option-cards` is `"off"` in your settings, so there's no native `.card`) —
  `card`, `eyebrow`, `stack`, `cluster`, `icon-circle`, `logo-item`, plus background variants
  `section--warm`/`section--dark`. 11 classes total, defined once in the JSON's
  `globalClasses` array, reused everywhere via `_cssGlobalClasses` — not invented per-section.
  Names match the project's own `class-map.csv` (from `crown-movers-frontend-reference.zip`)
  where that taxonomy applies.
- Result: 44.9KB vs. the first version's 56.9KB, despite doing more (reusable classes vs.
  duplicated inline settings on every element).

## One thing genuinely worth a 30-second check

The exact class strings ACSS compiles to (`.btn.primary` vs. some other convention,
`.grid--3`, `--radius-l`) are my best-confidence read of ACSS's own settings-key naming
(`btn-primary-*` implies `.btn` + a bare `primary` class; the `s/m/l/xl` suffix convention is
directly confirmed elsewhere in your settings — `text-s-max`, `contextual-content-gap: var(
--space-m)`, etc.) and the project's own `class-map.csv` for the grid/section names — not
something I've inspected in ACSS's actual compiled output from this environment, since I don't
have a working connection to the Bricks builder itself. After import: open one button in the
builder and confirm `.btn.primary` picks up the orange. If a string is slightly off, it's a
find-and-replace on that one class name in the JSON, not a rebuild.

## Everything from the first version's notes still applies

- rem base confirmed at 16px from your own `root-font-size: 100` setting.
- Nothing renders until the CPT posts exist — see `13-crown-movers-content-seed.md` and
  `acf-json/README.md`.
- `/commercial-moving/` is a guessed slug — verify or send me the real one.
- The FAQ loop's `objectType: "acf_faq_items"` binding is the one query worth a spot-check in
  the builder (vs. the 3 CPT loops, which use the more robust `post_type` form).
- Stat counter numbers (1,000 / 29) are hardcoded literals, not ACF-bound — Bricks' `counter`
  element needs a real number to animate from/to, and I didn't want to bet that on an unverified
  dynamic-tag binding for a purely decorative animation.
- Image URLs point at the live site as placeholders — swap for your new media-library URLs
  before production, don't hotlink. See `12-crown-movers-asset-checklist.md`.
- Header/footer aren't in this JSON — separate Bricks templates, not page content.
