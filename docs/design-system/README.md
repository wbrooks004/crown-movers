# Crown Movers
The design system for the crownmovers.ca rebuild: warm ink, Crown Coral and real photography, on Automatic.css and Bricks.

## How to read this system
- **Source of truth.** Every colour, size and space here was read from the ACSS 4.0.1 stylesheet that staging.crownmovers.ca serves (2026-09-29). Token names **are** the ACSS variable names (`--primary`, `--base`, `--text-m`, `--space-m`, `--radius`), so component CSS moves into Bricks global classes unchanged.
- **Hierarchy.** An ACSS variable first; an ACSS utility class second; the ACSS dashboard third; a BEM class from this system fourth; a documented exception last. No inline styles and no Bricks element-level styling, ever.
- **Placeholders.** Anything marked `[VERIFY]` is not a fact yet: ratings, move counts, years, reviews, insurance and pricing claims. It does not ship until the client confirms it.

## Brand foundations
Crown Movers moves homes and businesses in Greater Montreal and beyond, in English and French. The site has one job: turn a worried person into a booked move. The look is calm, specific and well-made, which is what a careful mover looks like. It is not loud.

**Voice.** Plain and specific. Say what happens ("A coordinator calls you back with a written price"), not how great it is. No superlatives without a source. Same message in EN and FR; French is written for Quebec and proofread by a native speaker before it ships. Calls to action are verbs: "Get a free quote", "Call 514-606-4030".

## Colour
| Role | Token | Hex | Where |
|---|---|---|---|
| Crown Coral | `--primary` | #F04836 | Primary buttons, big numerals, focus ring, route marks |
| Coral hover | `--primary-hover` | #FF6B56 | Primary button hover |
| Warm ink | `--base` | #161513 | Text, headings, ink sections, ink button |
| Ink 2 | `--base-dark` | #222222 | Ink hover, second dark band |
| Paper | `--base-ultra-light` | #F7F5F1 | Alternate sections (`.bg--ultra-light`) |
| Warm border | `--base-light` | #D8D5CF | Card borders, dividers |
| Grey | `--neutral` | #777D83 | Icons, form-field borders |
| Amber | `--accent` | #F89C3E | Gradient partner; marks on ink |

**Contrast rules (measured).**
| Pair | Ratio | Verdict |
|---|---|---|
| ink on white / paper | 18.3 / 16.8 | any text |
| white on ink | 18.3 | any text |
| **ink on coral** | 4.94 | primary button text |
| white on coral | 3.69 | **never** |
| coral on white / paper | 3.69 / 3.39 | large text (24px+, or 18.7px bold) and graphics only |
| coral on ink | 4.94 | any text, including the eyebrow |
| amber on white | 2.14 | **never** text or meaningful graphics |
| amber on ink | 8.5 | marks, stars, small text |
| grey on white / paper | 4.16 / 3.82 | icons, borders, large text; not body copy |
| muted text (80% ink) on white / paper | 9.7 / 9.2 | body copy in cards |

Links in running text are ink with a 2px coral underline, never coral text.

## Typography
- **Archivo** for display (headings, numerals), **Inter** for text. Both are self-hosted variable WOFF2 files (Latin subset, 35 KB + 48 KB, all French accents present), weight axis 100-900, `font-display: swap`. Never load them from Google.
- Scale (ACSS, fluid): `--h1` 31-47px at 700, 1.05, -0.02em · `--h2` 26-36px at 700 · `--h3` 22-27px at 600 · `--h4` 18-20px at 700 · body `--text-m` 16-18px · lead `--text-l` 19-24px · small `--text-s` 14-15px.
- One H1 per page. Headings balance-wrap. Eyebrows are the only uppercase text.

## Surfaces and texture
Five surfaces, three overlays, all configured once in the ACSS Surfaces panel (see the Surfaces component for the table). The rules are what keep texture premium rather than decorative:
1. At most one textured or photo surface per screen height, with plain white or paper between.
2. The brand gradient (coral to amber, from the logo) appears once per page, at most.
3. Text on photos sits only where the hero overlay is at least 72% ink.
4. Textures are static SVG under 30 KB combined, and they drop out under `prefers-contrast: more`.
5. Motifs mean something: route lines are journeys (long-distance, quote), island contours are place (locations), grain unifies the photography.

## Shape
- `--radius` 8px on buttons, cards and inputs. No pill buttons. `--radius-circle` only for avatars and dots.
- **The crown angle:** one 20px diagonal cut (`--notch`) taken from the logo's crown. It appears on the quote card's corner and, at 3x, as the hero's slanted bottom edge. One per section at most; never on buttons or cards in a grid.
- Borders are 1px `--border-color-dark`. Shadows are for hover lift (`--box-shadow-1`) and floating panels (`--box-shadow-2`) only.

## Spacing and layout
- Content width `--content-width` 1280px; gutter `--gutter` 16-80px; section padding `--section-space-m` (48-90px), heroes `--section-space-l`.
- Gaps and padding use `--space-*` only. Grids use `auto-fit` columns so they reflow without breakpoint patches.

## Motion
- 0.3s ease-in-out (ACSS `--transition`) on colour, border and shadow; the only movement is a 3px arrow nudge on buttons.
- Hover and `:focus-visible` always get the same treatment. Everything stops under `prefers-reduced-motion`.
- Entrance animation: at most one per section header; none on content text.

## Iconography
One icon style: 24px line icons, 1.75 stroke, round caps (the service icons here). Icons are decorative (`aria-hidden`) and never the only label. Coral in icon wells, ink elsewhere.

## Photography
Real Crown crews, trucks, packing and Montreal streets only; no stock people and no AI-generated people or trucks. Heroes use cover crops under the hero overlay; cards use 4:3. Serve AVIF/WebP with `srcset`; the hero image is `fetchpriority="high"` and is never lazy-loaded.

## Accessibility
- Every text pair above has a measured ratio; nothing below 4.5:1 carries small text.
- Focus: 2px `--focus-color` outline at 2px offset on every interactive element (3.4:1 or better on every surface).
- Targets 44px or larger. Rating stars are decorative; the rating is also written as text.
- Form fields: visible labels, and `--neutral` borders (3:1 or better).

## ACSS follow-ups found while building this system
| Setting | Now | Should be | Why |
|---|---|---|---|
| `link-color` | `var(--primary)` | `var(--base)` + coral 2px underline | coral text on white is 3.69:1 |
| `f-field-border-color` | `--border-color-dark` (#D8D5CF) | `--neutral` | input borders need 3:1; now 1.46:1 |
| `f-field-color-placeholder` | `--neutral-light` | `--neutral` | placeholder legibility |
| Surfaces 1-5 / Overlays 1-3 | empty | as in Surfaces | textures under global control |

## Inventory status
Built: tokens, fonts, 8 assets, and the components Surfaces, Button, SectionHeader, ServiceCard, LocationCard, TestimonialCard, ProcessSteps, StatsBand, QuotePanel, Hero.
Not built yet: header and navigation, footer, mobile action bar, FAQ, route card, breadcrumbs, blog card, form states (error and success). Missing from the client: the SVG logo master, real reviews, and confirmed numbers.
