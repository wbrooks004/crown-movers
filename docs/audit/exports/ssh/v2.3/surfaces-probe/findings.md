# ACSS Surfaces/Overlays -- source findings (read-only probe)

Source: `wp-content/plugins/automatic-css/` on staging, ACSS 4.0.1. All paths below are
relative to that plugin root. Full 80-line grep of `surface-1-`/`overlay-1-` is in
`grep.txt`; the answers below required reading beyond those first 80 hits into the
actual module files (`assets/scss/modules/surfaces/` and `.../overlays/`), which the
precompiled cache file only references indirectly.

## 1. Which selector/class does ACSS generate for a surface?

`.surface-#{$index}` (numeric position, 1-5) and `.surface-#{$name}` (the surface's
custom name), applied together as a single combined selector.

- `assets/scss/modules/surfaces/_classes.scss:7-8` -- animation-only surfaces:
  `.surface-#{$name}, .surface-#{$index} { animation: $animation; }`
- `assets/scss/modules/surfaces/_classes.scss:11-13` -- asset-bearing surfaces:
  `.surface-#{$name}, .surface-#{$index} { @include surface($index); }`

A surface class only appears in the generated CSS once it has an asset or an
animation (`classes/Model/Config/Framework.php:162-163` -- comment confirms this is
enforced by inspecting the generated stylesheets, not the config alone).

## 2. Which selector/class does ACSS generate for an overlay?

Two unrelated overlay systems exist under the same word:

- **Basic overlays** (a generic utility, gated by `option-basic-overlays`): class
  `.overlay` or any `[class*="overlay--"]`, using a `::before` pseudo-element by
  default (`$basic-overlay-pseudo-element: "before"`).
  `assets/scss/modules/overlays/_classes.scss:2,7` .
- **Numbered overlay presets** (`overlay-1` .. `overlay-5`, the ones this unit asked
  about) get **no selector/class of their own at all**. They only ever exist as CSS
  custom properties `--overlay-{N}-{prop}` (name, bg-color, type, background,
  background-image, opacity, etc.) emitted into `:root`:
  `assets/scss/modules/overlays/custom/_tokens.scss:2-12`. They become visible only
  through whichever surface links to them via `surface-N-overlay` (see Q5).

## 3. Does a surface support more than one background image?

**No.** A surface's asset is a single scalar value, not a list:

- `assets/scss/modules/surfaces/_vars.scss:7-8` -- `$surface-1-asset: null !default;`
  paired with a single boolean `$surface-1-asset-is-url: on !default;` (one value, one
  is-it-a-url flag -- no array/list structure).
- `assets/scss/modules/surfaces/_mixins.scss:3` -- the `surface()` mixin emits exactly
  one `background-image` declaration from one `--surface-#{$name}-asset` variable.

## 4. Does an overlay support a gradient?

**Yes**, by convention rather than by computed transformation. `overlay-N-background-type`
defaults to `"gradient"` (`assets/scss/modules/overlays/custom/_vars.scss:8`), and
gates whether any `--overlay-{N}-*` custom properties are emitted at all --
`assets/scss/modules/overlays/custom/_tokens.scss:8`: tokens only emit when
`$background_type != "none"`. The token emitter itself does not construct a gradient
string; it emits whatever raw value `overlay-N-background` already holds, verbatim
(`_tokens.scss:9`: `--overlay-#{$overlay}-#{$prop}: #{$value};`). So "gradient" support
means: the user/dashboard is expected to put a literal `linear-gradient(...)` (or
similar) CSS value into `overlay-N-background` when `background-type` is `"gradient"`.
UNVERIFIED: whether the ACSS dashboard UI validates/constrains that value to a well-
formed gradient syntax -- that layer wasn't reached by this source read (would be in
the plugin's admin JS bundle, not the CSS-generation SCSS/PHP this probe covered).

## 5. How does `surface-N-overlay` link an overlay to a surface?

`surface-N-overlay` is a plain per-surface settings variable (default `null`):
`assets/scss/modules/surfaces/_vars.scss:16` (`$surface-1-overlay: null !default;`),
included as the `"overlay"` key in the `$surfaces` map (`_vars.scss:103,117,131,145,159`
for surfaces 1-5).

`surfaces/_tokens.scss:13` emits this value directly and generically (it isn't given
special handling the way `"asset"` and `"animation"` are):
`--#{$surface}-#{$prop}: #{$value};` -- i.e. whatever string `surface-N-overlay` holds
becomes the literal value of `--surface-{name}-overlay`.

`surfaces/_mixins.scss:9` then consumes it in the `surface()` mixin:
`border-image: fill 1 var(--surface-overlay, var(--surface-#{$name}-overlay));` --
using the `border-image: fill` technique to paint the overlay over the surface's own
background, rather than a separate pseudo-element.

Structurally, this means the link is a plain CSS custom-property reference: setting
`surface-1-overlay` to something like `var(--overlay-1-background)` would make the
surface's border-image resolve to whatever `overlay-1-background` was set to. This is
the only mechanism the source supports (there is no PHP glue code connecting the two
numbered systems -- confirmed by the absence of any PHP file matching `overlay-1` or
`background-type`, see `grep.txt`). UNVERIFIED (empirically): the exact string format
the ACSS dashboard actually writes into `surface-N-overlay` when a user links the two
in the UI, since neither `surface-1-overlay` nor any overlay preset is currently
configured on this site (see `current.txt`) -- there is no live value to confirm
against.

## 6. What does `surface-N-color-relationship` do?

Links a surface into the same generated-selector group as a specific ACSS palette
color name (e.g. `"primary"`, `"base"`), so that color-relationship rules written for
`.bg--{color}` (text color, link color, button styling, heading color, all computed
for contrast against that color) also apply to any surface sharing that relationship.

- `assets/scss/modules/surfaces/_functions.scss:6-17` -- `get_surface_selectors($color)`
  loops the `$surfaces` map; for every surface whose `"relationship"` equals the given
  color, appends `.surface-#{$i}, .surface-#{$custom-name}` to a selector string.
- Called from 4 modules, each building a combined selector
  `'.bg--#{$color}' + get_surface_selectors($color)`:
  `assets/scss/modules/color-relationships/_buttons.scss:4`,
  `assets/scss/modules/color-relationships/_text.scss:4`,
  `assets/scss/modules/color-relationships/_links.scss:5` and `:25`,
  `assets/scss/modules/color-relationships/_headings.scss:4` and `:12`.

So `surface-1-color-relationship: "primary"` would make anything inside `.surface-1`
receive exactly the same text/link/button/heading color treatment ACSS already
computes for `.bg--primary`, without needing to add the `.bg--primary` class itself.
Default value is `"none"` (`_vars.scss:14`), which never matches any real color name,
so no relationship is applied by default.
