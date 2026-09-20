# Crown Movers — Bricks Builder component pack

Paste-ready Bricks 2.3.6 JSON for the components approved to build against placeholder content, plus the token/theme setup they depend on. Built with the `anthropic-skills:bricks` skill against your confirmed conventions: **1rem = 10px** (62.5% reset) and **native ACSS 4.x variables** (`--primary`, `--base`, `--accent`, `--neutral` + light/dark steps) — no invented parallel variable namespace.

## Files, in build order

| File | Format | Import via |
|---|---|---|
| `00-setup-acss-and-theme-styles.md` | reference | read first |
| `00-theme-styles.json` | theme styles | Bricks Settings → Theme Styles (hand-enter; see table in the setup doc) |
| `01-header.json` | template (header) | Bricks → Templates → Import |
| `02-hero-home.json` | clipboard | paste — **homepage only.** Full split hero with photo, dual CTA, trust line |
| `02b-hero-inner.json` | clipboard | paste — **every inner page** (service, location, quote, blog). Compact: breadcrumbs + eyebrow + dynamic `{post_title}` H1 + short intro + CTA row, no photo column. Home and inner pages don't share a hero — using the home hero everywhere was wrong, this replaces that |
| `03-trust-strip.json` | clipboard | paste, directly under the home hero |
| `04-service-card.json` | clipboard | paste — 3-card grid, duplicate the card pattern for more services once the service list is confirmed |
| `05-quote-form.json` | clipboard | paste — native Bricks `form` element |
| `06-faq.json` | clipboard | paste — `accordion-nested` with `faqSchema: true` (FAQ JSON-LD for SEO) |
| `07-footer-mobile-actions.json` | template (footer) | Bricks → Templates → Import — includes the fixed mobile call/quote bar |

Every file passes `python3 -m json.tool` and a parent/child tree-integrity check (flat array, every id resolves, no orphans, no duplicates).

## What's still placeholder — search each file for `[VERIFY]`

This was scoped as "build the existing 7 reference components with placeholder content" — it is **not** wired to real business facts yet. Every `[VERIFY]` label marks a spot that needs one of the items from the earlier gap-analysis before this goes live:

- Phone number (`tel:+10000000000` everywhere)
- Real photography (image elements are left empty, pointing at `07-existing-site-photo-manifest.csv` for candidates — nothing hotlinks crownmovers.ca)
- Service-area/location list, reviews/ratings/stats, FAQ answers, pricing/insurance policy copy
- Quote form destination (`05-quote-form.json` defaults to Bricks' native email action; swap to a webhook once an n8n endpoint exists)
- Privacy Policy / Terms pages (footer links to `#` — also needed for Quebec Law 25 disclosures)
- Official colour/dark-variant logo file (header currently falls back to `logoText`)

## Two things to verify once pasted in (not blocking, just unverified)

1. **`--space-*` variable names** — assumed to match ACSS 4.x's native fluid spacing scale. If your panel uses different step names, it's a find-replace across `bricks/*.json`, not a rebuild.
2. **Quote-form submit button text color** — relies on the Theme Styles `button` group rendering dark ink, not white, on the coral background. The accessibility rule (`#151515` on `#F04836` ≈ 4.94:1; white fails AA) is non-negotiable — confirm it once pasted in.

## Not built yet (from the original 43-component docx spec)

This pack covers 9 of 43 named components (breadcrumbs landed as part of `02b-hero-inner.json`, using Bricks' native `breadcrumbs` element rather than hand-built links). Still open: announcement bar, rating/stats strip, location cards, multi-step estimate form + calculator, date picker/radio-card form inputs, testimonial cards, team cards, partner logo row, popups, and the ACF field groups + query loops that would make services/locations dynamic instead of hand-typed. Build these next once the business-fact gaps above are closed — hand-typed content now would just need to be redone as dynamic data later.
