# Crown Movers — ACF Structure

Registers 4 Custom Post Types, 1 taxonomy, 5 field groups, 1 Options Page, plus 2 page-scoped
field groups for content that varies per page. Designed so the homepage — and later, other
pages — pull real content via Bricks query loops and dynamic-data tags instead of hardcoded
text baked into page JSON.

## Setup

Drop this whole `acf-json/` folder inside your active theme (or a custom plugin) as
`your-theme/acf-json/`. ACF's Local JSON auto-sync picks it up — check **Custom Fields →
Field Groups**, each group should show a "Sync available" prompt (or already be synced,
depending on ACF version). Post types, the taxonomy, and the Options Page appear once synced
too, under **Custom Fields → Post Types / Taxonomies / Options Pages**.

If you'd rather import by hand: **Custom Fields → Tools → Import Field Groups / Post Types**,
one file at a time.

## What's here

| File | Registers | Notes |
|---|---|---|
| `post_type_testimonial.json` | CPT `testimonial` | Title = customer name, Excerpt = the review quote, Featured Image = customer photo (optional) |
| `group_testimonial_details.json` | Fields on `testimonial` | `role`, `pull_quote`, `rating` |
| `post_type_services.json` | CPT `services` | Title = service name, Excerpt = card summary, Featured Image = real service photo. Rewrite slug `services` (`/services/{post-slug}/`) |
| `group_service_details.json` | Fields on `services` | `related_services` (relationship), `service_faqs` (repeater: `question`/`answer`) |
| `post_type_service_areas.json` | CPT `service-areas` | Title = area/city name, Excerpt = intro copy, Featured Image = area photo. Rewrite slug `locations` (`/locations/{post-slug}/`) — this is the city/region landing-page system |
| `group_service_area_details.json` | Fields on `service-areas` | `province` (select), `service_region` (taxonomy: `service-region`), `services_available` (relationship → `services`), `area_faqs` (repeater: `question`/`answer`) |
| `taxonomy_service_region.json` | Taxonomy `service-region` | Hierarchical, attached to `service-areas` only, not publicly queryable (`public: false`) — an internal grouping term, not a front-end archive |
| `post_type_partner.json` | CPT `partner` | Title = company name, Featured Image = logo |
| `group_partner_details.json` | Fields on `partner` | `website_url` |
| `options_page_business_info.json` | Options Page **Business Info** (`business-info`) | Sitewide singletons — see below |
| `group_business_info.json` | Fields on the Business Info Options Page | `business_name`, `legal_business_name`, `primary_phone`, `primary_email`, `office_address`, `business_hours`, `facebook_url`, `instagram_url`, `linkedin_url`, `youtube_url`, `google_business_profile_url`, `primary_cta` (link), `secondary_cta` (link) |
| `group_faq_items.json` | Repeater on **any Page** | `faq_items` → `question` / `answer`. Page-scoped on purpose — Montreal Movers and the homepage have different real FAQ content. Empty by default; a page with 0 rows should hide its FAQ section. |
| `group_homepage_stats.json` | Fields on the **front page only** | The two animated-counter stats — pre-filled with the real live numbers (1,000+ moves/year, 29% savings) so the homepage isn't blank on first import |

## Business Info Options Page — single source of truth

`primary_cta` and `secondary_cta` are ACF **link** fields (title + URL + target), each holding
the one global button used everywhere on the site — per the fields' own instructions:
"the one global primary/secondary CTA used throughout the site, normally Get a Free Quote /
Call Crown Movers." Every primary button on the homepage (hero + closing CTA section) is bound
to the same `primary_cta` field, and every "call us" button to the same `secondary_cta` field —
so they render identical text and href everywhere by design. Change the button copy or
destination once here, and it updates sitewide.

**Fill these in before launch** — until `primary_cta`/`secondary_cta` are set, those buttons
fall back to placeholder text (`@fallback` in the dynamic tag) but the `href` itself resolves
empty, so the buttons won't go anywhere. This is a launch blocker, not a nice-to-have.

`primary_phone` is separate plain text (no enforced format) for places that need just the raw
number rather than a full CTA button — nothing in the current homepage JSON reads it directly,
since both "Call us" buttons pull the full `secondary_cta` link instead; it's available for
header/footer templates later.

## The `services` / `service-areas` system

This is a proper locations + services structure, not flat pages:

- **`services`** (`/services/{slug}/`) — one post per service offered (residential moving,
  commercial moving, long-distance, storage, packing, etc.). The homepage services grid loops
  this CPT directly (`post_type: ["services"]`), links each card to `{post_url}`, and pulls
  the card blurb from `{post_excerpt}` — there's no separate "short description" field, the
  native WordPress excerpt is the summary field.
- **`service-areas`** (`/locations/{slug}/`) — one post per city/region served (Montreal,
  Laval, South Shore, etc.), each optionally grouped under a `service-region` term and linked
  to the specific `services` it offers there via the `services_available` relationship field.
  Nothing in `bricks-json/home.json` builds these pages yet — that's the next phase now that
  the CPT/taxonomy exist (see `11-crown-movers-redesign-plan.md`).
- Both CPTs carry their own FAQ repeater (`service_faqs` / `area_faqs`) separate from the
  generic page-level `faq_items` — a service or area page's FAQ section should loop its own
  post's repeater, not the page-level one.

## Dynamic-data tags used in the homepage JSON

```
{acf_role}                     - testimonial CPT loop
{acf_pull_quote}
{acf_rating}
{post_excerpt}                 - services CPT loop (card blurb — native excerpt, not ACF)
{post_url}                     - services CPT loop (card link target)
{acf_website_url}              - partner CPT loop
{acf_faq_items_question}       - FAQ repeater loop (objectType: "acf_faq_items")
{acf_faq_items_answer}
{acf_stat_one_value}           - front-page fields, no loop needed
{acf_stat_one_suffix}
{acf_stat_one_label}
{acf_stat_one_description}
{acf_stat_two_value}
{acf_stat_two_suffix}
{acf_stat_two_label}
{acf_stat_two_description}
{acf_primary_cta}              - Business Info options page (resolves to the link's title in
                                  text settings; bound as a full link via useDynamicData on the
                                  button's link setting)
{acf_secondary_cta}            - same, options page secondary_cta
```

## Two things worth a manual check

1. The FAQ repeater loop's `objectType: "acf_faq_items"` binding is the one piece Bricks' own
   docs flag as version-sensitive for hand-authored JSON (vs. built through the query-loop UI).
   It's the standard, documented fallback pattern, but worth a 10-second confirm: open that
   loop's query settings in the builder once and check the type dropdown resolved to
   "ACF: faq_items" rather than showing an error. Testimonial/services/partner loops use plain
   `post_type` queries instead — no such caveat there.
2. `primary_cta`/`secondary_cta` bind through `"link": {"type": "meta", "useDynamicData":
   "{acf_field}"}` — documented in Bricks' own ACF provider reference as the correct shape for
   an ACF link field. Worth a quick spot-check in the builder once real values are entered,
   same as any first-time dynamic binding.

## Content

Real content already gathered from the live site (testimonial, all 6 service descriptions,
partner list, FAQ, stats, business contact info) is in `13-crown-movers-content-seed.md` at the
repo root — ready to copy into wp-admin once these post types and the Options Page exist.
Nothing here is placeholder/lorem text.
