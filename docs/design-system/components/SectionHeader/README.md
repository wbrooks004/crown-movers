# SectionHeader
Eyebrow, title and intro that open a section; left-aligned by default, `section-header--center` for CTAs.

- `eyebrow`: 14px, 700, uppercase, 0.08em tracking. **Ink text with a 2px coral bar on light surfaces; coral text only on ink; white on photo.** Coral small text on white is 3.69:1 and fails AA; the v6.0 library draft did this and v6.2 corrects it.
- Title is the section's `h2`. Intro is `--text-l` in `--text-dark-muted` (9.7:1), max 62ch.
- Consumer provides: the heading level, if not h2.
