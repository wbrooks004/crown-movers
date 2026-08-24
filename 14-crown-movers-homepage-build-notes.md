# Crown Movers Homepage — Build Notes

`bricks-json/home.json` — 9 sections, 111 nodes, validated (unique ids, no orphaned parent/child
references, JSON parses clean). Paste into the empty section Bricks gave you (select it in the
structure panel, Cmd/Ctrl+V) or replace it outright.

## rem base

Confirmed as **16px**, not assumed — your own `crown-movers-acss-settings.json` has
`"root-font-size": 100` (ACSS's root-font-size setting is a percentage; 100% of the browser
default 16px = 16px, i.e. no override). All `clamp()`/rem values in the homepage JSON are built
on that basis.

## Sections, in order

1. **Hero** — split layout, real tagline, dual CTA (Free Quote / Call), real branded-truck photo
2. **Stats** — the 2 real live counters (1,000+ moves/year, 29% savings), sourced from
   `group_homepage_stats.json`
3. **Quick links** — Moving in Montreal / Long Distance / Commercial (see caveat below)
4. **Keys to a perfect moving day** — the 3 real cards (Priority / Experienced / No Hidden Fees)
5. **Complete service grid** — dynamic, loops the `service` CPT (6 real entries once you add them
   per `13-crown-movers-content-seed.md`)
6. **Testimonials** — dynamic, loops the `testimonial` CPT (1 real entry — Bruce Rickerd — ready
   to add; layout supports up to 3 without changes)
7. **Trusted partners** — dynamic, loops the `partner` CPT (18 real names ready to add)
8. **FAQ** — dynamic, loops the page-level `faq_items` ACF repeater; `faqSchema: true` outputs
   FAQ JSON-LD automatically (useful with Rank Math already in your stack)
9. **Final CTA** — dark gradient panel, real heading, quote + call buttons

All colors reference your actual design tokens (`{"raw": "var(--primary)"}` etc.), not
hardcoded hex — they'll stay in sync if the ACSS settings change later.

## Things worth knowing, not silently decided

- **Nothing renders until the CPT posts exist.** The loops are correctly wired but there's no
  content in `service`/`testimonial`/`partner` until you (or I) create those posts — see
  `13-crown-movers-content-seed.md` for the exact real content to enter, and the acf-json setup
  first (`acf-json/README.md`).
- **`/commercial-moving/` is a guess.** Nav on the live site shows "Commercial" but I never
  confirmed the exact slug — check it before publishing, or tell me the real URL and I'll fix it.
- **The FAQ loop's `objectType: "acf_faq_items"`** is the one binding Bricks' own docs flag as
  worth a manual spot-check (vs. the 3 CPT loops, which use the more robust `post_type` query
  form) — open its query settings once in the builder and confirm it resolved to "ACF:
  faq_items". Full explanation in `acf-json/README.md`.
- **Stat counter numbers (1,000 / 29) are hardcoded literals**, not ACF-bound, even though the
  label/description text around them is dynamic. Bricks' `counter` element needs a real number
  to animate from/to; I didn't want to bet that on an uncertain dynamic-tag binding for a purely
  decorative animation. If these ever change, edit them directly in the JSON/builder (rare —
  redesign-level edit, not routine content).
- **All image URLs point at the live site** (`www.crownmovers.ca/wp-content/uploads/...`) as
  placeholders so the page isn't blank on first paste. Per the brief's own rule, swap these for
  your new media-library URLs before this goes to production — don't hotlink. `12-crown-movers-
  asset-checklist.md` has the full list.
- Header and footer aren't part of this JSON — those are separate Bricks templates (Phase 1 in
  `11-crown-movers-redesign-plan.md`), not page content. Say the word if you want those built
  next, same real-content approach.
