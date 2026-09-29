# Surfaces
The five Crown surfaces and three overlays; each maps to one ACSS Surface or Overlay slot, so a texture changes once, in the ACSS dashboard.

| Surface | Class here | ACSS slot | Background | Text | Use |
|---|---|---|---|---|---|
| Paper | `surface--paper` | Surface 1 | `--bg-ultra-light` + grain-on-light | `--text-dark` | Alternate content sections |
| Ink | `surface--ink` | Surface 2 | `--bg-ultra-dark` + grain-on-dark + route-lines | `--text-light` | Quote panel, CTA, footer |
| Photo | `surface--photo` + `overlay--hero` + `overlay--grain` | Surface 3 + Overlays 1, 3 | Crown photography | `--text-light` | Heroes |
| Brand | `surface--brand` | Surface 4 | `--primary` to `--accent` at 115deg + grain | `--base` | Stats band or quote strip; **once per page** |
| Map | `surface--map` | Surface 5 | `--bg-ultra-light` + island-contours | `--text-dark` | Location and route pages |

Rules
- At most one textured or photo surface per screen height; plain white or paper between them.
- On Photo, text sits on the left half, where the overlay is at least 72% ink (white text 6.8:1 even over a white pixel).
- Textures never animate. Under `prefers-contrast: more` every texture drops to its flat colour.
- Consumer provides: the section content, and for Photo an `img.surface__media` with `srcset`, real `alt` (or empty if decorative) and `fetchpriority="high"` when it is the LCP image.
