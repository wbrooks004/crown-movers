# ServiceCard
A service summary whose whole surface links to the service page; `service-card--featured` sits on paper.

- The only link is the service name (`service-card__link`); its `::after` stretches over the card, so there is one tab stop and no "Learn more" ambiguity.
- The icon well is `--primary-ultra-light` with a coral icon (3.2:1, meets 3:1 for graphics). Icons are decorative (`aria-hidden`).
- Hover and focus-within: border to `--primary` plus `--box-shadow-1`. No movement.
- Body in `--text-dark-muted`. Copy is placeholder until supplied ([VERIFY]).
