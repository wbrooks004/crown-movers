# Crown Movers — Content Seed (real content, ready to enter)

Everything below is real, already-published Crown Movers content pulled directly from the
live site — nothing invented. Use it to populate the CPTs in `acf-json/` and to fill in the
homepage. Source page noted per item so it's traceable.

## Testimonials (→ `testimonial` post type)

**1 real testimonial found on the homepage** (there may be more collected elsewhere, e.g. via
the NotificationX plugin already installed on the live site — worth checking before assuming
this is the only one you have).

| Field | Value |
|---|---|
| Title (name) | Bruce Rickerd |
| Role | Musician - Cirque du Soleil |
| Pull quote | They Worked Their Butt Off! |
| Rating | 5 |
| Excerpt (review) | "Crown Movers and Storage were a great bunch of people to deal with. They were super careful handling all of my belongings just as if they were their own. Everyone was extremely nice and friendly. They worked their butt off and showed pride in their work. I can't thank all of you enough for your help. You're great!." |
| Photo | `https://www.crownmovers.ca/wp-content/uploads/2022/07/brucerickerd-movers-review-crown-movers-Montreal-1.webp` |

Source: crownmovers.ca homepage.

## Services (→ `service` post type, 6 items — the homepage's "Complete Moving Service" grid)

| Title | Short description | Photo (re-upload, don't hotlink) |
|---|---|---|
| Crown Movers and Packers | Our packing and organizing experts will have you ready to move in no time. Keeping you organized throughout the entire moving experience. | `.../2022/07/Packing-And-Organizing.webp` |
| Furniture Assembly | Let us handle the disassembly and assembly of your furniture. We handle it, so that you don't have to worry about any missing screws! | `.../2022/07/Furniture-Disassembly-Assembly.webp` |
| Furniture Movers | Your furniture will be wrapped and protected in clean furniture blankets. We make sure that your belongings are safely transported to you. | `.../2022/07/furniture-movers.webp` |
| Free Movers Insurance | We include free basic liability coverage for your peace of mind. Added protection in case your possessions are damaged or lost during your move. | `.../2022/07/movers-insurance.webp` |
| Unpacking & Cleaning | Moving can be a long process. Allow Crown Movers to handle all unpacking and cleaning after the moving process, so you can relax and get settled in. | `.../2022/07/unpacking-cleaning.webp` |
| Storage Solutions | We go the extra step to set you up with 1 month of free storage at any local storage facility near you! We are more than just a moving company. | `.../2022/07/storage.webp` |

(All URLs share the host `https://www.crownmovers.ca/wp-content/uploads/`.)

Source: crownmovers.ca homepage, "Complete Moving Service" section.

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

## Homepage stats (already defaulted in `group_homepage_stats.json`, restated here for reference)

- **1,000+** Moving Services Per Year — "Our experience is unmatched! Our professional
  Montreal moving services guarantees a successful move every time."
- **29%** (SAVE) Affordable Moving Service — "Crown's affordable moving services save you time
  and money! Crown Movers is 29% less expensive than our competitors."

## Hero / "keys to a perfect moving day" copy (static content, not a CPT — goes straight in the homepage JSON)

- Hero: "Reliable Moving Services in Montreal" / "We truly care about your moving experience —
  from the first call to the last box unpacked." (adapted from the real live tagline)
- **You Are Our Priority** — From your first phone call to the last box we unpack, you are our
  priority. Your move is more than just a job. Our aim is to make your move memorable for all
  the right reasons. We value your moving experience and aim to have you pleasantly surprised
  with how fun and easy moving can be!
- **Experienced Movers** — The Rule of the 3 E's. Experience Equals Efficiency. Our
  experienced Montreal moving company has all the right moves and is equipped with the tools
  to have your move done in no time. Every moving service is planned out and organized in
  advance.
- **No Hidden Fees** — From the moment you call Crown Movers, we go through as many details as
  needed to assure an accurate quotation. We offer hourly rates so there are no hidden fees.

## Contact details (real, for footer / CTA sections)

- Phone: **(514) 606-4030**
- Email: info@crownmovers.ca
- Address: 4030 Blvd. Cote-Vertu Ouest, Suite 111, Montreal, QC H4R 1V4

## What I did *not* pull in

- The claim "highest-rated Montreal moving company on Google" / "#1 moving company in
  Montreal" appears on the live site in a few places. It's their own existing published claim,
  not something I added — carrying it forward is reusing their content, not me asserting a new
  fact. Still worth a sanity check on your end before it goes on the new homepage, same as any
  claim of this kind.
- The 40-city service-area list (Anjou, Beloeil, Blainville... down to Westmount) is real and
  live but is footer/SEO-link content, not homepage hero material — I condensed it in the
  homepage JSON rather than reproducing the full list; see the homepage build notes.
