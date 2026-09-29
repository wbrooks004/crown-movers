# Hero
The page opener: real photography under the hero overlay and grain, one H1, one primary action and the phone number.

- Photo surface + `overlay--hero` + `overlay--grain`; the bottom edge slants by 3x `--notch` (the crown angle).
- The text column is at most 36rem and sits on the dark side of the overlay.
- The image is usually the LCP element: `fetchpriority="high"`, `srcset`, AVIF/WebP, never lazy-loaded, 180 KB or less at mobile width.
- Proof line: amber stars on ink (8.5:1) plus a text rating; the rating stays [VERIFY] until confirmed.
