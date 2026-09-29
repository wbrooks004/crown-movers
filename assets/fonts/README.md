# Self-hosted fonts

Variable WOFF2 builds, Latin subset (covers French diacritics), pulled from the official
Fontsource CDN mirror (source: Google Fonts).

| File | Source URL | Date pulled | Licence |
|---|---|---|---|
| `archivo-latin-wght-normal.woff2` | https://cdn.jsdelivr.net/fontsource/fonts/archivo:vf@latest/latin-wght-normal.woff2 | 2026-09-29 | SIL Open Font License 1.1 |
| `inter-latin-wght-normal.woff2` | https://cdn.jsdelivr.net/fontsource/fonts/inter:vf@latest/latin-wght-normal.woff2 | 2026-09-29 | SIL Open Font License 1.1 |

Both are variable-weight fonts (`font-weight: 100 900`) replacing the previous static TTF
files (652 KB + 875 KB) served from a single fixed weight with an invalid `@font-face`
weight-list declaration.
