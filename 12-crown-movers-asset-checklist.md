# Crown Movers — Asset Checklist (fonts, icons, images)

What you actually need to gather or upload before/during the Bricks build. Split by how
urgent/blocking each one is.

## Fonts — 1 decision, then optionally upload files

Montserrat and Roboto are both free Google Fonts (Open Font License) — nothing to buy. One
decision first:

**Google-hosted vs. self-hosted?** Loading fonts straight from Google's CDN (the simplest ACSS
setup — what `font-1-type`/`font-2-type: "google"` in `crown-movers-acss-settings.json`
currently assumes) sends visitor IPs to Google at page load. Many Quebec/Canadian businesses
now self-host instead, both for performance and to sidestep that third-party data transfer
under Quebec's Law 25 — this isn't a hard legal requirement here, but it's a common, cheap
precaution worth a decision either way rather than a default.

- **If Google-hosted:** nothing to upload — confirm the two font entries in ACSS's Typography
  panel resolve correctly after import (flagged as needing a manual check in `08`).
- **If self-hosted:** download WOFF2 files and upload them via ACSS's font manager
  ("Upload" type instead of "Google"):
  - **Montserrat** — weights 400, 600, 700, 800, 900
  - **Roboto** — weights 400, 500, 600, 700
  - Get them free from fonts.google.com (each family's download gives you TTF; convert to
    WOFF2 with a tool like Font Squirrel's webfont generator, or pull pre-built WOFF2 via
    google-webfonts-helper).

## Icons — likely nothing to upload

Bricks ships Font Awesome (Regular/Solid/Brands), Ionicons, and Themify built in — no upload
needed for standard UI/social icons. The icons currently live on the site (heart, star,
map-marker, chevron-down, menu, cross, quote-left, and the Twitter/Facebook/LinkedIn/YouTube/
Instagram social set) all map cleanly to Font Awesome, which is already available natively.

**One exception worth a decision:** the Montreal Movers page has a custom hand-coded, animated
truck/route illustration (inline SVG with its own `crown-route-divider` animation — not a
stock icon). If you want that exact illustration preserved in the Bricks rebuild, that's a
custom SVG asset to carry over, not something from an icon library — let me know if you want
me to pull the actual SVG markup out of the live page (I only extracted its CSS so far, not
the SVG paths themselves).

If you want a fully custom Crown icon (e.g., a simplified version of the angular crown mark
for UI use, distinct from the wordmark logo), that would need to be commissioned/designed and
uploaded as SVG — the brief flags this as optional ("avoid repeating crown icons as
decoration"), so treat it as nice-to-have, not blocking.

## Images — the real work is here

**Rule from the brief, worth restating:** don't hotlink the old site's images in production —
download and re-upload every one you're keeping into the new WordPress media library.

### Logo — a real gap, get this first

Only a **white** logo (`crown-logo-white.webp`, for dark backgrounds) is in the upload pack.
Given the confirmed light-dominant background direction, **most placements now need a dark or
full-color version** — a white logo will be invisible on white/warm-tint backgrounds. Two
options, in priority order:
1. Ask whoever has the original logo files for a vector **SVG** (ideal — scales crisply,
   tiny file size, and Bricks/web best practice for logos generally). A colored or dark
   wordmark version, transparent background.
2. If no SVG exists, a high-resolution transparent **PNG** works as a fallback — the pack
   already flags `Color20logo20-20no20background_edited-1.png` on the old site as a possible
   source, but says explicitly to get the "official" high-res version if possible rather than
   rely on that one.

### Photos already identified (from `07-existing-site-photo-manifest.csv`) — re-download + re-upload

| Asset | Use |
|---|---|
| Family moving photo | Customer-care / residential section |
| Experienced movers | Experience / process section |
| No hidden fees | Transparent-pricing section |
| Packing and organizing | Packing service card/page |
| Furniture assembly | Assembly service card/page |
| Furniture movers | Furniture-protection section |
| Unpacking and cleaning | Post-move section — **confirm this service still exists before publishing** |
| Storage | Storage-related section — **confirm current storage relationship before publishing** |
| Free quote trucks (wide + portrait) | Quote-page hero/banner |
| About-page company photo | Company story — older image, check quality |

### Photos I found live that aren't in that manifest — add these too

These are newer (2026/06 uploads) and already in production on the two audited pages, so
they're proven, on-brand, and worth carrying forward:
- `montreal-commercial-movers-crown-truck-business-building.webp`
- `montreal-long-distance-moving-truck-crown-movers-quebec.webp`
- `montreal-packing-services-white-glove-crown-movers.webp`
- `montreal-residential-movers-crown-moving-truck-home.webp` (+ a 1200×900 crop variant)
- `Demenageurs-Professionel-2-1` (410×512 portrait crop)
- A candid team photo (`WhatsApp-Image-2021-05-13...`) — verify this is one you want to keep
  using; it reads as an informal/unposed shot rather than curated photography.

### New/missing, not covered by either list

- **Favicon** — not addressed anywhere in the existing brief or reference pack. Needs a small
  square mark (the crown symbol likely works well here) in the usual sizes WordPress expects.
- **Social share image (OG image)** — same, not addressed yet. A 1200×630 image for link
  previews when pages are shared.
- Service-page photos for the sub-pages not yet covered by the manifest — residential-moving,
  packing-services, furniture-assembly, small-movers, delivery-services, long-distance-moving
  each need at least one representative photo; check what's already live on those specific
  URLs before assuming new photography is needed.

## What doesn't need anything from you

Colors, type scale, radius, shadows, gradients, and button states are all specified in
`crown-movers-acss-settings.json` and `09-crown-movers-live-brand-tokens.css` — nothing to
gather there, just import and go.
