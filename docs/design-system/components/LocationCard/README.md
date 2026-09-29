# LocationCard
A compact link to one location page, grouped by region; deliberately different from ServiceCard.

- Region label: 14px uppercase in `--text-dark-muted` (not the grey neutral, which fails for small text).
- Title link text matches the page H1: "<City> movers". The meta line names the serving branch; location pages are not branches (no LocalBusiness schema on them).
- Shown on the Map surface; hover and focus as ServiceCard.
