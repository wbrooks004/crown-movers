# Crown Movers Homepage — Build Notes (v5, full redesign to your reference image)

Fifth pass, and a different kind of change from v2→v3→v4: you sent a complete reference image
of the new design and said "I want it to look like this." This isn't a content-binding pass on
top of the old structure — it's a from-scratch rebuild to that reference, using the same BEM +
ACSS-variable discipline v3/v4 established, now extended to the header and footer (previously
deferred as separate, not-yet-started work).

## v5.1 — fixes from your real render (the first actual empirical test in this project)

You pasted `home.json` into the real builder and sent a screenshot — the first time anything
in this project has been checked against an actual render instead of just JSON review. It
surfaced real bugs, root-caused and fixed rather than guessed at:

- **Dark sections (stats bar, quote-CTA) rendered blank/white with invisible white-on-white
  text; button text/gradient didn't apply.** All traced to one cause: I'd used `_cssCustom`
  (raw CSS injection) for backgrounds/gradients/shadows in several places, and it wasn't
  reliably beating Bricks' own compiled class rules. Converted all 7 such usages to Bricks'
  native structured settings instead — `_gradient` for backgrounds (confirmed exact shape from
  the bricks skill's own reference docs), `_boxShadow` for shadows (decomposed into
  offsetX/offsetY/blur/spread using the literal numbers from your own
  `crown-movers-acss-settings.json` box-shadow tokens, not re-guessed), plain `_typography.color`
  for button text. The gradient-hover-sweep effect on primary buttons now uses a native
  `_gradient:hover` (swapped color-stop order) instead of a hand-rolled CSS transition — this
  one's a slightly newer technique for this project, worth a quick look once you re-test.
- **The "Why Crown" and closing-CTA photos rendered as a broken oval blob; the hero's "3,000+"
  badge escaped to the very bottom of the page instead of sitting on the hero photo.** Same root
  cause for both: I'd combined `_height:"100%"` with `_aspectRatio` on the image, which the
  skill's own docs describe as alternatives, not a pair — the conflict was almost certainly
  collapsing the image's container, which cascades into the hero badge's positioning context
  too. Fixed by dropping the redundant `_height` and keeping only `_aspectRatio` + `_width:100%`.
- **Services-band icons looked oversized and boxy against a pink tint**, not the clean minimal
  line-icon style in your reference. Dropped the padded/tinted chip wrapper — bare icon now,
  matching the reference.

I can't render Bricks myself from here, so this loop — you test in the real builder, send what's
actually wrong, I root-cause against your evidence rather than re-guessing — is the real
verification path for this project from here on. Worth another look and another screenshot
after this push.

## Three files now, two different delivery mechanisms

| File | Format | How you use it |
|---|---|---|
| `bricks-json/home.json` | Clipboard format (`bricksCopiedElements`) | Same as before — paste into the page canvas (Ctrl/Cmd+V in the structure panel) |
| `bricks-json/header.json` | **Template export format** | New for this project: **Bricks → Templates → Import**, not paste. Creates a template post with Type = Header, sitewide condition. |
| `bricks-json/footer.json` | **Template export format** | Same — **Bricks → Templates → Import**, Type = Footer. |

Header/footer use a different JSON shape than every other file I've given you in this project
(top-level `header`/`footer` array instead of `content`, `global_classes` instead of
`globalClasses`, plus `templateSettings`) — that's not a mistake, it's what Bricks' own
Template Import feature actually expects. Import (not paste) regenerates element IDs, merges
global classes, and pulls the remote image URLs into your media library automatically.

**One thing worth knowing before you paste `home.json`:** if any earlier version (v1–v4) of
this homepage was ever actually pasted into your real Bricks site, some global class *names*
here match names from those versions (`hero`, `btn`, `cta`...) with different definitions.
Bricks' paste-merge rule is "same name → use the local (existing) class" — so a same-named
leftover class from an old paste could silently keep its old styling instead of picking up v5's
definitions. If you haven't pasted anything into the real builder yet (sounded like you hadn't,
last we spoke), this doesn't apply. If you have, delete the old global classes first, or paste
this into a fresh, never-used page.

## Section-by-section (home.json, 154 nodes / 86 BEM classes)

1. **Hero** — eyebrow, `h1`, subtext, primary CTA button + phone link, 5-star Google rating
   line, photo with a "3,000+ moves handled every year" badge overlay.
2. **Stats bar** (dark) — 5.0 Google rating, animated 3,000+ counter, "No Hidden Fees" (the one
   real, previously-sourced line in this bar).
3. **Services band** — 4 curated category links (Residential / Long-Distance / Commercial /
   Packing & Storage) with icons, replacing the old photo-card grid of all 6 services.
4. **Why Crown** (split photo + checklist) — new section, replaces the old 3-column "keys to a
   perfect moving day."
5. **Quote CTA** (dark) — heading, 3 trust badges, and your **real, live quote form embedded**
   via `[ws_form id="20"]` (see below) — not a fake duplicate form.
6. **Process** — 3 numbered steps, new section.
7. **Testimonial + map** — one testimonial (query loop, 1 post) in a red panel, next to a
   decorative pinned-region graphic. New section.
8. **Closing CTA** — heading, primary + phone buttons, photo. Same idea as v4's, restyled.

**Dropped from the homepage** (not deleted — just not in this design): the old quicklinks strip,
the full 6-item services photo grid, the trusted-partners logo strip, and the FAQ accordion.
The `partner` CPT and the page-level `faq_items` repeater are untouched and still usable on
other pages; the `services` CPT still needs all 6 posts (services band links to them, and
they're the future `/services/{slug}/` detail pages).

## Header (20 nodes / 15 classes) + Footer (30 nodes / 13 classes)

- **Utility bar**: location text, phone (dynamic, `{acf_primary_phone}`), and an **FR** language
  link via `[polylang]` — Polylang's standard switcher shortcode. I didn't guess at its display
  options (flags/names/hide-current) — check it renders how you want in Polylang's own settings
  after import, adjust the shortcode's attributes there if needed.
- **Main header**: real logo (`Crown-Movers-Logo.png`, the non-white variant, pulled from your
  live site's own media library — not invented), `nav-nested` primary nav, dynamic primary CTA
  button. Sticky on scroll (`headerSticky: true`) — a reasonable default for a site whose main
  CTA should stay reachable while scrolling, not something visible in a static reference image,
  so say the word if you'd rather it not stick.
- **Footer**: white-logo variant (also a real asset), dynamic address/phone, 3 link columns,
  dynamic social icons (Facebook/Instagram/Google — see content-seed), dynamic copyright year.

## Real vs. placeholder, all in one place

**Confirmed real** (sourced from crownmovers.ca or your own ACF field definitions):
- Both logo files, the hero/why-crown/cta photos (placeholder *crops*, still real Crown Movers
  photography — swap for better-fitted shots before launch, same as earlier versions)
- `/montreal-movers/`, `/free-quote/` links
- "No Hidden Fees" stats-bar line
- Facebook/Instagram/LinkedIn/YouTube/Google Business URLs, business hours, address, phone
- The `services`/`service-areas` CPT rewrite base paths (`/services/`, `/locations/`)

**Per your confirmation this session** (not independently verified against the live site):
- 3,000+ moves/year, 5.0 Google rating, the Karen L. testimonial

**Still placeholder — flagged inline in the JSON `label` fields, not hidden:**
- Nav's "Resources" link and every footer Company/Resources column link (no such pages
  confirmed to exist yet)
- The exact post slugs for `long-distance-moving`/`commercial-moving` (the `/services/` base is
  now confirmed real; the specific slug per post isn't)
- Icon glyph names in the services band / why-crown checks / process arrows / trust badges —
  chosen from Bricks' bundled ionicons set by best-guess naming, same convention as the one
  already-confirmed-real name (`ion-ios-arrow-forward`) used since v3. A wrong guess just shows
  a blank icon, nothing breaks — spot-check each in the icon picker after import and swap any
  that don't render.
- The testimonial+map decorative graphic is exactly that — decorative, hand-positioned pins on
  a tinted panel, not an interactive map. Bricks does have real `map`/`map-leaflet` elements if
  you'd rather have an actual embedded map later.

## The quote form is real, not a duplicate

Your live `/free-quote/` page runs on **WS Form** (confirmed from its own markup —
`wp-json/ws-form/v1/submit`, form id `20`), not Bricks' native form element or any of the more
common plugins. Rather than guess at rebuilding its fields and validation by hand, the quote-CTA
section embeds the actual form via Bricks' `shortcode` element: `[ws_form id="20"]` — WS Form's
own standard embed shortcode. This is the same form, same backend, same submissions — not a
second thing to maintain. One real caveat: the *look* of the fields inside that card (input
borders, spacing, the submit button's exact color) is controlled by WS Form's own Style settings
in wp-admin, not by this JSON — open WS Form's styling once the form is embedded and align it
with the rest of the site if it doesn't already match.

## Still true from earlier passes

- rem base confirmed at 16px (`root-font-size: 100` in your ACSS settings).
- Nothing renders until the CPT posts and Options Page fields exist — `13-content-seed.md` +
  `acf-json/README.md`. The primary/secondary CTA buttons (4 of them now: hero, closing CTA,
  and the header) need `primary_cta`/`secondary_cta` filled in before they point anywhere.
- Every color value in every new class is an ACSS variable (`var(--primary)`, `var(--secondary)`,
  `var(--text-dark-muted)`-style `color-mix()` derivations, etc.) — none are hardcoded hex,
  including the gradients: `linear-gradient(135deg, var(--primary) 0%, var(--tertiary) 100%)`
  on buttons and a `color-mix()`-derived two-stop dark gradient on the stats bar / quote-CTA
  section, both built from your role colors rather than snapshotted hex, unlike v3's one
  disclosed exception on button colors (that workaround is no longer needed).
- Radius is uniformly `var(--radius)` (your ACSS settings already consolidate card/button/icon
  radius to this one token — confirmed directly from `crown-movers-acss-settings.json`, not
  assumed) — except pill shapes (badges), which use a literal `999px`, matching the one other
  pattern-file precedent for pills in this project.
