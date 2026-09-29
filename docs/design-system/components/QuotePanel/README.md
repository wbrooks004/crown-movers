# QuotePanel
The conversion block: pitch and trust list on ink, the quote form in a white card with the crown-angle notch.

- On the site the form is WS Form (Quick Quote: id 4 EN, id 5 FR), styled by ACSS form tokens; the preview fields only approximate it.
- Field borders must be `--neutral` (4.16:1, meets 3:1). ACSS currently draws them with `--border-color-dark` (1.46:1); follow-up in v2.3.
- Trust items use amber triangles on ink (8.5:1). Claims stay [VERIFY] until confirmed.
- The notch is a `clip-path` corner (20px). No shadow: clip-path would cut it, and shadows vanish on ink anyway.
