# Crown Movers — Content Seed (real content, ready to enter)

Everything below is either real, already-published Crown Movers content pulled directly from
the live site, or content you confirmed directly as accurate when I asked (marked "per your
confirmation" below) — nothing else is invented. Use it to populate the CPTs in `acf-json/` and
to fill in the homepage. Source noted per item so it's traceable.

## Testimonials (→ `testimonial` post type, 2 items)

The v5 homepage design features **one** testimonial (in the red quote panel next to the
service-area map) — set it first via the post's `menu_order` (or lowest-order) so the query
loop picks it up. Bruce Rickerd's review is still real, sourced content — keep it as a second
post for use elsewhere (a dedicated testimonials/reviews page, a future carousel, etc.), just
not on the homepage in this design.

**Featured on the v5 homepage — per your confirmation:**

| Field | Value |
|---|---|
| Title (name) | Karen L. |
| Role (repurposed as route) | Westmount to Vaudreuil |
| Pull quote | The quote was spot on. The team took the stress away. |
| Rating | 5 |

No photo/excerpt supplied for this one — add them if you have them, both are optional on this
CPT.

**Not used on the v5 homepage, real, sourced from crownmovers.ca:**

| Field | Value |
|---|---|
| Title (name) | Bruce Rickerd |
| Role | Musician - Cirque du Soleil |
| Pull quote | They Worked Their Butt Off! |
| Rating | 5 |
| Excerpt (review) | "Crown Movers and Storage were a great bunch of people to deal with. They were super careful handling all of my belongings just as if they were their own. Everyone was extremely nice and friendly. They worked their butt off and showed pride in their work. I can't thank all of you enough for your help. You're great!." |
| Photo | `https://www.crownmovers.ca/wp-content/uploads/2022/07/brucerickerd-movers-review-crown-movers-Montreal-1.webp` |

Source: crownmovers.ca homepage. (There may be more testimonials collected elsewhere, e.g. via
the NotificationX plugin already installed on the live site — worth checking.)

## Services (→ `services` post type, 6 items)

**v5 homepage note:** the homepage no longer shows a full grid of every service — it shows 4
fixed, curated category links instead (Residential Moving, Long-Distance, Commercial Moving,
Packing & Storage — see the build notes). These 6 posts are still needed: they're what
`/services/` and each `/services/{slug}/` page will show once those templates are built, and
"Packing & Storage" links straight to the `/services/` archive.

The `services` CPT has no separate "short description" field — the homepage card loop reads
the native WordPress **Excerpt** box, so enter the description text there (not in a custom
field). `related_services` and `service_faqs` (both on this CPT) aren't sourced from the live
site — leave them empty until there's real cross-sell/FAQ content to put in them.

| Title | Excerpt | Photo (re-upload, don't hotlink) |
|---|---|---|
| Crown Movers and Packers | Our packing and organizing experts will have you ready to move in no time. Keeping you organized throughout the entire moving experience. | `.../2022/07/Packing-And-Organizing.webp` |
| Furniture Assembly | Let us handle the disassembly and assembly of your furniture. We handle it, so that you don't have to worry about any missing screws! | `.../2022/07/Furniture-Disassembly-Assembly.webp` |
| Furniture Movers | Your furniture will be wrapped and protected in clean furniture blankets. We make sure that your belongings are safely transported to you. | `.../2022/07/furniture-movers.webp` |
| Free Movers Insurance | We include free basic liability coverage for your peace of mind. Added protection in case your possessions are damaged or lost during your move. | `.../2022/07/movers-insurance.webp` |
| Unpacking & Cleaning | Moving can be a long process. Allow Crown Movers to handle all unpacking and cleaning after the moving process, so you can relax and get settled in. | `.../2022/07/unpacking-cleaning.webp` |
| Storage Solutions | We go the extra step to set you up with 1 month of free storage at any local storage facility near you! We are more than just a moving company. | `.../2022/07/storage.webp` |

(All URLs share the host `https://www.crownmovers.ca/wp-content/uploads/`.)

Source: crownmovers.ca homepage, "Complete Moving Service" section.

Note: these 6 are the general services shown on the homepage. "Long Distance Moving" and
"Commercial Moving" are referenced elsewhere (the homepage quicklinks strip) as if they're
their own service pages too — if they are, add them here as additional `services` posts at
slugs `long-distance-moving` and `commercial-moving` so the quicklink URLs
(`/services/long-distance-moving/`, `/services/commercial-moving/`) resolve; if not, those two
quicklinks need re-pointing once you confirm what they should actually link to.

## Trusted Partners (→ `partner` post type, 18 items)

Real logos currently live on the homepage's "Our Network of Trusted Partners" section:

Boulevard Real Estate Agency · COSCO Shipping · Hydro-Québec (EIN) · English Montreal School
Board · Gold's Gym · Hellenic Community of the Greater Montreal · M Immobilier · Montreal Mini
Storage · Myra's Kids Foundation · PA Marché · PEYO · Holland · Café Olimpico · Canadian
Border Services · Lululemon · Revenu Québec · Satay Brothers · Ville de Montréal · Pandora
Mini-Entrepôts

Logo files are already on the live site under `/wp-content/uploads/2020/08/` and
`/wp-content/uploads/2026/01/` and `/wp-content/uploads/2026/04/` — re-download and re-upload
per the no-hotlinking rule, don't build this list from memory of the filenames since a couple
have inconsistent casing/naming; check the live page directly when uploading.

## FAQ (→ page-level `faq_items` repeater — real content from `/montreal-movers/`)

Use as-is on the Montreal Movers page; homepage doesn't need to duplicate all 6 — 3-4 of the
most general ones (cost, calculator accuracy, quote details) work fine there too, or skip FAQ
on the homepage and keep it page-specific.

1. **How much does a local move cost in Montreal?** — The price depends on the home size,
   access, stairs, elevator, walking distance, number of boxes, furniture, trucks, date, and
   travel time. Use the calculator for a starting range, then ask our team to review the
   details.
2. **Is the instant moving calculator a final quote?** — No. The calculator gives a starting
   estimate. Crown Movers reviews the details before confirming the final service, rate, crew,
   trucks, and availability.
3. **Do elevators add time to a Montreal move?** — Yes, they can. Elevator service needs
   reservations, loading time, and sometimes a longer walk from the truck. A small or busy
   elevator can also slow the move.
4. **Do you handle small moving jobs?** — Yes. Crown Movers handles small jobs, furniture
   delivery, storage service, single-item moves, apartment moves, condo moves, and full home
   moves. A small move still needs the right plan.
5. **Can I ask for packing help before moving day?** — Yes. Ask for packing services before
   the move. We can review boxes, fragile items, supplies, timing, furniture protection, and
   storage if needed.
6. **What details should I send before asking for a quote?** — Send the moving date, pickup
   address, drop-off address, access details, stairs, elevator information, walking distance,
   boxes, photos, inventory, and any heavy or fragile items.

## Homepage stats — v5 design (hero badge + dark stats bar)

**Per your confirmation**, not from `group_homepage_stats.json`:

- **3,000+** moves handled every year (hero photo badge + dark stats bar counter)
- **5.0 ★★★★★** on Google (hero rating line + dark stats bar)
- **No Hidden Fees** (dark stats bar — this one *is* real, sourced live-site copy, previously
  used in the old "keys to a perfect moving day" section, reused here)

`group_homepage_stats.json`'s original fields (`acf_stat_one_*`/`acf_stat_two_*` — the real,
live-sourced 1,000+ services/year and 29% savings numbers) aren't read anywhere in the v5
homepage JSON. I left the field group in `acf-json/` rather than deleting it — it's still real,
verified content, useful if you want it on another page or a future homepage revision. Let me
know if you'd rather I remove it.

## Hero / "Why Crown" copy (static content, not a CPT — goes straight in the homepage JSON)

The v5 design's hero and "Why Crown" split section replaced the old hero tagline and the old
3-item "keys to a perfect moving day" section. Current copy:

- Hero: "Your move, handled with care." / "Local, long-distance and commercial moving across
  Montreal and beyond." (adapted — reflects the three real, confirmed service lines)
- **Why Crown** — "Clear plan. Careful hands. A smoother move." / "We plan every detail so your
  move is efficient, protected and stress-free from start to finish." Checklist: Accurate
  estimates · Furniture protection included · Experienced, trained crews · Assembly &
  disassembly (all four map to real, previously-sourced service copy — furniture protection,
  assembly/disassembly, and experienced crews all come from the live site's own service
  descriptions).
- The old "You Are Our Priority" / "Experienced Movers" / "No Hidden Fees" 3-column section
  doesn't exist as its own section in v5 — "No Hidden Fees" moved to the stats bar (above),
  the other two ideas are folded into the Why Crown checklist instead.

## Business Info (→ Options Page `business-info`, single source of truth sitewide)

The homepage's primary/secondary CTA buttons (hero + closing CTA section) now pull from
`primary_cta`/`secondary_cta` here — **fill these in before launch**, the buttons render
fallback text but a dead link until you do.

| Field | Value | Source |
|---|---|---|
| `business_name` | Crown Movers | — |
| `legal_business_name` | *(leave blank unless the registered legal entity name differs from "Crown Movers")* | — |
| `primary_phone` | (514) 606-4030 | live site |
| `primary_email` | info@crownmovers.ca | live site |
| `office_address` | 4030 Blvd. Cote-Vertu Ouest, Suite 111, Montreal, QC H4R 1V4 | live site |
| `business_hours` | Monday–Sunday: 9:00 AM–5:00 PM | live site's own schema.org markup (`openingHours`) |
| `facebook_url` | `https://facebook.com/www.crownmovers.ca` | live site — this exact URL is what's currently published (the `www.crownmovers.ca` segment in a Facebook path looks like a live-site mistake, not something I introduced; worth a sanity check/fix on Facebook's end before reusing it) |
| `instagram_url` | `https://www.instagram.com/CrownMovers.ca` | live site |
| `linkedin_url` | `https://www.linkedin.com/company/crown-movers/` | live site |
| `youtube_url` | `https://www.youtube.com/channel/UCTWHXW2iyL45LgdYyN7Zpfg` | live site |
| `google_business_profile_url` | `https://g.page/Crown-Movers?share` | live site |
| `primary_cta` (link) | Text: "Get a Free Quote" → URL: `/free-quote/` | recommended — matches the live site's existing free-quote page and the homepage's own fallback copy |
| `secondary_cta` (link) | Text: "Call Crown Movers" (or "Call Us — (514) 606-4030") → URL: `tel:+15146064030` | recommended — the field's own instructions name "Call Crown Movers" as the expected default |

**v5 footer note:** the new footer's social-icon row shows exactly 3 icons (Facebook,
Instagram, Google) to match the reference design — `facebook_url`/`instagram_url`/
`google_business_profile_url` power those. `linkedin_url`/`youtube_url` are still collected
here and available if you want a 4th/5th icon added later.

## What I did *not* pull in

- The claim "highest-rated Montreal moving company on Google" / "#1 moving company in
  Montreal" appears on the live site in a few places. It's their own existing published claim,
  not something I added — carrying it forward is reusing their content, not me asserting a new
  fact. Still worth a sanity check on your end before it goes on the new homepage, same as any
  claim of this kind.
- The 40-city service-area list (Anjou, Beloeil, Blainville... down to Westmount) is real and
  live but is footer/SEO-link content, not homepage hero material — I condensed it in the
  homepage JSON rather than reproducing the full list; see the homepage build notes. This list
  is now the real content source for the new `service-areas` CPT (`acf-json/`) — each city
  becomes its own post at `/locations/{slug}/` once that phase starts, rather than living only
  as flat footer links. I haven't pulled the per-city page content (if any exists beyond the
  name) — that's a future fetch, not done here.
- The v5 homepage's testimonial+map section shows 6 pinned regions (Laval, Montreal, West
  Island, South Shore, Quebec City, Toronto) — a simplified, decorative regional set, not the
  full 40-city list, and not pulled from a specific live-site source; it's a reasonable summary
  of the service area already established elsewhere in this project (Montreal & Greater
  Montreal, plus long-distance moving reaching Toronto/Quebec City). Sanity-check it names the
  regions you actually want to feature there.
