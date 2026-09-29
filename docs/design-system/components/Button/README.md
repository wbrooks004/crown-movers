# Button
ACSS buttons in three roles: coral primary (one per view), ink base, and outline; plus the phone link.

- `btn--primary`: coral with **ink** text (4.94:1), hover `--primary-hover` (6.51:1). Never white text on coral (3.69:1).
- `btn--base`: ink with white text (18.3:1), hover `--base-dark`.
- `btn--outline`: ink border and text on light surfaces. `btn--outline-light`: white border and text on ink or photo. On the site this needs an ACSS light-outline variant or one BEM modifier (decided in v4).
- `phone-link`: ink (or white on dark) with a 2px coral underline. Coral is never the text colour on light grounds.
- 700 weight, sentence case, `--radius` (8px), min 44px tall. The arrow moves 3px on hover and focus-visible; no motion under reduced-motion.
- One primary per view. Labels are verbs: "Get a free quote", "Call 514-606-4030".
