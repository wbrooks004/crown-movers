# Crown Movers — ACF Structure

Registers 3 Custom Post Types (queryable content that repeats across the site) and 3 field
groups (extra structured fields on top), plus 2 page-scoped field groups for content that
varies per page. Designed so the homepage — and later, other pages — pull real content via
Bricks query loops and dynamic-data tags instead of hardcoded text baked into page JSON.

## Setup

Drop this whole `acf-json/` folder inside your active theme (or a custom plugin) as
`your-theme/acf-json/`. ACF's Local JSON auto-sync picks it up — check **Custom Fields →
Field Groups**, each group should show a "Sync available" prompt (or already be synced,
depending on ACF version). Post types appear once synced too, under **Custom Fields → Post
Types**.

If you'd rather import by hand: **Custom Fields → Tools → Import Field Groups / Post Types**,
one file at a time.

## What's here

| File | Registers | Notes |
|---|---|---|
| `post_type_testimonial.json` | CPT `testimonial` | Title = customer name, Excerpt = the review quote, Featured Image = customer photo (optional) |
| `group_testimonial_details.json` | Fields on `testimonial` | `role`, `pull_quote`, `rating` |
| `post_type_service.json` | CPT `service` | Title = service name, Featured Image = real service photo |
| `group_service_details.json` | Fields on `service` | `short_description`, optional `link_override` |
| `post_type_partner.json` | CPT `partner` | Title = company name, Featured Image = logo |
| `group_partner_details.json` | Fields on `partner` | `website_url` |
| `group_faq_items.json` | Repeater on **any Page** | `faq_items` → `question` / `answer`. Page-scoped on purpose — Montreal Movers and the homepage have different real FAQ content. Empty by default; a page with 0 rows should hide its FAQ section. |
| `group_homepage_stats.json` | Fields on the **front page only** | The two animated-counter stats — pre-filled with the real live numbers (1,000+ moves/year, 29% savings) so the homepage isn't blank on first import |

## Dynamic-data tags used in the homepage JSON

```
{acf_role}                 - testimonial CPT loop
{acf_pull_quote}
{acf_rating}
{acf_short_description}    - service CPT loop
{acf_website_url}          - partner CPT loop
{acf_faq_items_question}   - FAQ repeater loop (objectType: "acf_faq_items")
{acf_faq_items_answer}
{acf_stat_one_value}       - front-page fields, no loop needed
{acf_stat_one_suffix}
{acf_stat_one_label}
{acf_stat_one_description}
{acf_stat_two_value}
{acf_stat_two_suffix}
{acf_stat_two_label}
{acf_stat_two_description}
```

## One thing worth a manual check

The FAQ repeater loop's `objectType: "acf_faq_items"` binding is the one piece Bricks' own
docs flag as version-sensitive for hand-authored JSON (vs. built through the query-loop UI).
It's the standard, documented fallback pattern, but worth a 10-second confirm: open that
loop's query settings in the builder once and check the type dropdown resolved to
"ACF: faq_items" rather than showing an error. Testimonial/service/partner loops use plain
`post_type` queries instead — no such caveat there.

## Content

Real content already gathered from the live site (testimonial, all 6 service descriptions,
partner list, FAQ, stats) is in `13-crown-movers-content-seed.md` at the repo root — ready to
copy into wp-admin once these post types exist. Nothing here is placeholder/lorem text.
