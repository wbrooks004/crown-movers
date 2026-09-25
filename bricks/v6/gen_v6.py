#!/usr/bin/env python3
"""Crown Movers v6.0 — component library generator.
Emits Bricks 2.4.1 clipboard JSON (paste into the builder). Every style lives on a
global BEM class and references ACSS variables only. Element nodes carry content,
tags, links, attributes and ACSS utility classes (plain _cssClasses) — never style keys.
"""
import json, hashlib, os, re

OUT = "/mnt/user-data/outputs/bricks-v6"
os.makedirs(OUT, exist_ok=True)
SRC = "https://staging.crownmovers.ca"
VER = "2.4.1"

def bid(seed):
    """Deterministic 6-char id (letters+digits) so re-generation keeps ids stable."""
    h = hashlib.md5(seed.encode()).hexdigest()
    s = "".join(c for c in h if c.isalnum())[:6]
    return s if s[0].isalpha() else "c" + s[1:]

# ---------- global classes (the design system) ----------
CLASSES = {}
def cls(name, settings):
    CLASSES[name] = {"id": bid("cls:" + name), "name": name, "settings": settings, "category": None}
    return CLASSES[name]["id"]

def raw(v): return {"raw": v}
def sides(v): return {"top": v, "right": v, "bottom": v, "left": v}
CARD_BORDER = {"width": sides("1px"), "style": "solid", "color": raw("var(--neutral-light)"), "radius": sides("var(--radius)")}
CARD_HOVER_CSS = ("%s:hover, %s:focus-within { box-shadow: var(--box-shadow-1); border-color: var(--primary); }\n"
                  "@media (prefers-reduced-motion: reduce) { %s { transition: none; } }")

# shared
cls("eyebrow", {"_typography": {"font-size": "var(--text-xs)", "font-weight": "700", "letter-spacing": "0.08em",
                                "text-transform": "uppercase", "color": raw("var(--primary)")}})
# section-header
cls("section-header", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)", "_widthMax": "62ch",
                       "_margin": {"bottom": "var(--space-l)"}})
cls("section-header--center", {"_alignItems": "center", "_typography": {"text-align": "center"},
                               "_margin": {"left": "auto", "right": "auto"}})
cls("section-header__intro", {"_typography": {"font-size": "var(--text-l)", "color": raw("var(--text-dark-muted)")}})
# service-card
cls("service-card", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-s)", "_padding": sides("var(--space-m)"),
                     "_background": {"color": raw("var(--white)")}, "_border": CARD_BORDER, "_position": "relative",
                     "_cssTransition": "border-color var(--transition), box-shadow var(--transition)",
                     "_cssCustom": CARD_HOVER_CSS % (".service-card", ".service-card", ".service-card")})
cls("service-card--featured", {"_background": {"color": raw("var(--neutral-ultra-light)")},
                               "_border": {"color": raw("var(--primary)")}})
cls("service-card__icon", {"_cssCustom": ".service-card__icon { font-size: var(--icon-size-m); color: var(--primary); line-height: 1; }"})
cls("service-card__title", {"_typography": {"font-size": "var(--h4)", "font-weight": "700", "line-height": "1.2"}})
cls("service-card__body", {"_typography": {"color": raw("var(--text-dark-muted)")}, "_flexGrow": "1"})
cls("service-card__link", {"_typography": {"font-weight": "600", "color": raw("var(--primary)"), "text-decoration": "none"},
                           "_background": {"color": raw("transparent")}, "_padding": sides("0"),
                           "_typography:hover": {"text-decoration": "underline"},
                           "_cssCustom": ".service-card__link::after { content: \" \\2192\"; }\n"
                                         ".service-card__link:focus-visible { outline: var(--focus-width) solid var(--focus-color); outline-offset: var(--focus-offset); }"})
# location-card
cls("location-card", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)", "_padding": sides("var(--space-s)"),
                      "_background": {"color": raw("var(--neutral-ultra-light)")}, "_border": CARD_BORDER, "_position": "relative",
                      "_cssTransition": "border-color var(--transition), box-shadow var(--transition)",
                      "_cssCustom": CARD_HOVER_CSS % (".location-card", ".location-card", ".location-card") +
                                    "\n.location-card__title a::after { content: \"\"; position: absolute; inset: 0; }"
                                    "\n.location-card:focus-within { outline: var(--focus-width) solid var(--focus-color); outline-offset: var(--focus-offset); }"})
cls("location-card__title", {"_typography": {"font-size": "var(--h5)", "font-weight": "700", "line-height": "1.2"},
                             "_cssCustom": ".location-card__title a { color: inherit; text-decoration: none; }"})
cls("location-card__meta", {"_typography": {"font-size": "var(--text-s)", "color": raw("var(--text-dark-muted)")}})
# testimonial-card
cls("testimonial-card", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)", "_padding": sides("var(--space-m)"),
                         "_background": {"color": raw("var(--white)")}, "_border": CARD_BORDER, "_margin": sides("0"),
                         "_cssCustom": ".testimonial-card { border-inline-start: 4px solid var(--primary); } /* EXCEPTION: 4px accent rule, no ACSS token for a thick rule */"})
cls("testimonial-card__stars", {"_typography": {"color": raw("var(--accent)"), "letter-spacing": "0.1em", "line-height": "1"}})
cls("testimonial-card__quote", {"_typography": {"font-size": "var(--text-m)"}, "_flexGrow": "1"})
cls("testimonial-card__author", {"_typography": {"font-weight": "700"}})
cls("testimonial-card__meta", {"_typography": {"font-size": "var(--text-xs)", "color": raw("var(--text-dark-muted)")}})
# faq
cls("faq", {"_widthMax": "72ch", "_margin": {"left": "auto", "right": "auto"}})
cls("faq__item", {"_border": {"width": {"bottom": "var(--divider-size)"}, "style": "solid", "color": raw("var(--divider-color-dark)")},
                  "_padding": {"top": "var(--space-xs)", "bottom": "var(--space-xs)"}})
cls("faq__question", {"_typography": {"font-size": "var(--text-l)", "font-weight": "600", "line-height": "1.3"}})
cls("faq__answer", {"_typography": {"color": raw("var(--text-dark-muted)")}, "_padding": {"top": "var(--space-xs)"}})
# grids
cls("card-grid", {"_display": "grid", "_gridTemplateColumns": "var(--grid-auto-3)", "_gridGap": "var(--grid-gap)"})
cls("card-grid--4", {"_gridTemplateColumns": "var(--grid-auto-4)"})
# process
cls("process", {"_display": "grid", "_gridTemplateColumns": "var(--grid-auto-3)", "_gridGap": "var(--grid-gap)"})
cls("process-step", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)"})
cls("process-step__number", {"_typography": {"font-size": "var(--h2)", "font-weight": "800", "line-height": "1", "color": raw("var(--primary)")}})
cls("process-step__title", {"_typography": {"font-size": "var(--h5)", "font-weight": "700"}})
cls("process-step__text", {"_typography": {"color": raw("var(--text-dark-muted)")}})
# stats
cls("stats", {"_display": "grid", "_gridTemplateColumns": "var(--grid-auto-4)", "_gridGap": "var(--grid-gap)"})
cls("stat-item", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)", "_alignItems": "flex-start"})
cls("stat-item__value", {"_typography": {"font-size": "var(--h1)", "font-weight": "800", "line-height": "1", "color": raw("var(--primary)")}})
cls("stat-item__label", {"_typography": {"font-size": "var(--text-s)", "font-weight": "600", "letter-spacing": "0.06em",
                                         "text-transform": "uppercase", "color": raw("var(--text-dark-muted)")}})
# quote-panel
cls("quote-panel", {"_display": "grid", "_gridTemplateColumns": "var(--grid-2)", "_gridGap": "var(--space-l)", "_alignItemsGrid": "center",
                    "_gridTemplateColumns:tablet_portrait": "var(--grid-1)"})
cls("quote-panel__content", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-s)"})
cls("quote-panel__trust", {"_display": "flex", "_direction": "column", "_rowGap": "var(--space-xs)", "_padding": sides("0"), "_margin": sides("0")})
cls("quote-panel__trust-item", {"_typography": {"font-size": "var(--text-s)"},
                                "_cssCustom": ".quote-panel__trust-item::before { content: \"\\2713  \"; color: var(--accent); font-weight: 700; }"})
cls("quote-panel__form", {"_background": {"color": raw("var(--white)")}, "_padding": sides("var(--space-m)"),
                          "_border": {"radius": sides("var(--radius)")},
                          "_cssCustom": ".quote-panel__form { box-shadow: var(--box-shadow-2); }"})
# mobile-actions
cls("mobile-actions", {"_display": "none", "_display:mobile_landscape": "flex", "_columnGap": "var(--space-xs)",
                       "_position": "fixed", "_bottom": "0", "_left": "0", "_right": "0", "_zIndex": "100",
                       "_padding": sides("var(--space-xs)"), "_background": {"color": raw("var(--white)")},
                       "_cssCustom": ".mobile-actions { border-top: var(--border); padding-bottom: calc(var(--space-xs) + env(safe-area-inset-bottom)); }\n"
                                     "@media (max-width: 767px) { body { padding-bottom: calc(var(--space-xxl)); } }"})
cls("mobile-actions__btn", {"_flexGrow": "1", "_typography": {"text-align": "center"}})

# ---------- element helpers ----------
def gc(*names): return [CLASSES[n]["id"] for n in names]
class Tree:
    def __init__(self, slug): self.slug, self.nodes, self.n = slug, [], 0
    def add(self, name, parent, settings=None, label=None):
        self.n += 1
        node = {"id": bid(f"{self.slug}:{self.n}:{name}"), "name": name, "parent": parent, "children": [], "settings": settings or {}}
        if label: node["label"] = label
        if parent != 0: next(x for x in self.nodes if x["id"] == parent)["children"].append(node["id"])
        self.nodes.append(node); return node["id"]
    def used_classes(self):
        ids = {i for x in self.nodes for i in x["settings"].get("_cssGlobalClasses", [])}
        return [c for c in CLASSES.values() if c["id"] in ids]
    def write(self, filename):
        # integrity checks
        ids = [x["id"] for x in self.nodes]; assert len(ids) == len(set(ids)), "dup ids"
        byid = {x["id"]: x for x in self.nodes}
        for x in self.nodes:
            assert x["parent"] == 0 or x["parent"] in byid, "orphan " + x["id"]
            for c in x["children"]: assert byid[c]["parent"] == x["id"]
            for k in x["settings"]:
                assert not (k.startswith("_") and k not in ("_cssClasses", "_cssGlobalClasses", "_attributes", "_cssId", "_hidden")), \
                    f"element-level style key {k} on {x['name']}"  # the §6 rule, enforced
        doc = {"content": self.nodes, "source": "bricksCopiedElements", "sourceUrl": SRC, "version": VER,
               "globalClasses": self.used_classes(), "globalElements": []}
        s = json.dumps(doc, indent=1, ensure_ascii=False)
        assert not re.search(r'"(hex|rgb)"\s*:', s), "raw colour value found"
        assert not re.search(r'"\d+(\.\d+)?px"', s.replace('"1px"', "").replace('"0"', "")), "hard-coded px value found"
        open(os.path.join(OUT, filename), "w").write(s); print("wrote", filename, len(self.nodes), "elements,", len(doc["globalClasses"]), "classes")

def section(t, label, extra_classes=""):
    sec = t.add("section", 0, {"tag": "section", "_cssClasses": ("section--m " + extra_classes).strip()}, label)
    con = t.add("container", sec, {}, label + " container")
    return sec, con

def header(t, parent, eyebrow, title, intro, center=False):
    h = t.add("block", parent, {"_cssGlobalClasses": gc("section-header", *(["section-header--center"] if center else []))}, "Section header")
    t.add("text-basic", h, {"text": eyebrow, "tag": "span", "_cssGlobalClasses": gc("eyebrow")})
    t.add("heading", h, {"text": title, "tag": "h2"})
    if intro: t.add("text-basic", h, {"text": intro, "tag": "p", "_cssGlobalClasses": gc("section-header__intro")})
    return h

# ---------- 01 section-header + service cards ----------
t = Tree("service-cards")
sec, con = section(t, "Services")
header(t, con, "Moving services", "Everything the move needs, one crew", "Residential, commercial, long-distance, storage and specialty moving from one accountable team. [VERIFY copy]")
grid = t.add("div", con, {"_cssGlobalClasses": gc("card-grid")}, "Card grid")
for i, (icon, title, body, featured) in enumerate([
    ("fas fa-home", "Residential moving", "Apartments, condos and houses across Greater Montreal. Packing, protection and setup included. [VERIFY copy]", True),
    ("fas fa-building", "Commercial & office moving", "After-hours and weekend moves that keep your team working. [VERIFY copy]", False),
    ("fas fa-route", "Long-distance moving", "Montreal to Toronto, Ottawa and beyond with one crew door to door. [VERIFY copy]", False)]):
    card = t.add("block", grid, {"tag": "article", "_cssGlobalClasses": gc("service-card", *(["service-card--featured"] if featured else []))}, f"Service card {i+1}")
    t.add("icon", card, {"icon": {"library": "fontawesomeSolid", "icon": icon}, "_cssGlobalClasses": gc("service-card__icon")})
    t.add("heading", card, {"text": title, "tag": "h3", "_cssGlobalClasses": gc("service-card__title")})
    t.add("text-basic", card, {"text": body, "tag": "p", "_cssGlobalClasses": gc("service-card__body")})
    t.add("button", card, {"text": "Learn more", "tag": "a", "link": {"type": "external", "url": "#", "ariaLabel": f"Learn more about {title.lower()}"},
                           "_cssGlobalClasses": gc("service-card__link")})
t.write("01-section-header-and-service-cards.json")

# ---------- 02 location cards ----------
t = Tree("location-cards")
sec, con = section(t, "Service areas", "bg--ultra-light")
header(t, con, "Where we move", "Movers across the West Island, South Shore and beyond", None)
grid = t.add("div", con, {"_cssGlobalClasses": gc("card-grid", "card-grid--4")}, "Location grid")
for i, (region, city, meta) in enumerate([("West Island", "Pointe-Claire", "Served from the Montreal branch"),
                                          ("West Island", "Kirkland", "Served from the Montreal branch"),
                                          ("South Shore", "Brossard", "Served from the Montreal branch"),
                                          ("Laval", "Laval", "Served from the Montreal branch")]):
    card = t.add("block", grid, {"tag": "article", "_cssGlobalClasses": gc("location-card")}, f"Location card {i+1}")
    t.add("text-basic", card, {"text": region, "tag": "span", "_cssGlobalClasses": gc("eyebrow")})
    t.add("heading", card, {"text": f"{city} movers", "tag": "h3", "link": {"type": "external", "url": "#"}, "_cssGlobalClasses": gc("location-card__title")})
    t.add("text-basic", card, {"text": meta + " [VERIFY]", "tag": "p", "_cssGlobalClasses": gc("location-card__meta")})
t.write("02-location-cards.json")

# ---------- 03 testimonials ----------
t = Tree("testimonials")
sec, con = section(t, "Testimonials")
header(t, con, "Reviews", "What Montreal customers say", None, center=True)
grid = t.add("div", con, {"_cssGlobalClasses": gc("card-grid")}, "Testimonial grid")
for i in range(3):
    card = t.add("block", grid, {"tag": "figure", "_cssGlobalClasses": gc("testimonial-card")}, f"Testimonial {i+1}")
    t.add("text-basic", card, {"text": "★★★★★", "tag": "span", "_cssGlobalClasses": gc("testimonial-card__stars"),
                               "_attributes": [{"id": bid(f"stars{i}"), "name": "aria-label", "value": "5 out of 5 stars"}]})
    t.add("text-basic", card, {"text": "“Quote text — real review to be supplied by the client. Do not publish placeholder.” [VERIFY]", "tag": "blockquote",
                               "_cssGlobalClasses": gc("testimonial-card__quote")})
    t.add("text-basic", card, {"text": "Reviewer name [VERIFY]", "tag": "figcaption", "_cssGlobalClasses": gc("testimonial-card__author")})
    t.add("text-basic", card, {"text": "Google review · Montreal [VERIFY]", "tag": "span", "_cssGlobalClasses": gc("testimonial-card__meta")})
t.write("03-testimonial-cards.json")

# ---------- 04 FAQ (accordion-nested) ----------
t = Tree("faq")
sec, con = section(t, "FAQ")
header(t, con, "FAQ", "Questions before you book", None, center=True)
acc = t.add("accordion-nested", con, {"expandFirstItem": False, "independentToggle": True, "faqSchema": False,
                                      "_cssGlobalClasses": gc("faq")}, "FAQ accordion")
for i, q in enumerate(["How far in advance should I book my move?", "Is there a minimum charge?", "Are my belongings insured during the move?"]):
    item = t.add("block", acc, {"_cssGlobalClasses": gc("faq__item")}, f"FAQ item {i+1}")
    tw = t.add("block", item, {"_hidden": {"_cssClasses": "accordion-title-wrapper"}, "_cssClasses": ""}, "Title wrapper")
    t.add("heading", tw, {"text": q, "tag": "h3", "_cssGlobalClasses": gc("faq__question")})
    t.add("icon", tw, {"icon": {"library": "fontawesomeSolid", "icon": "fas fa-plus"}, "isAccordionIcon": True})
    cw = t.add("block", item, {"_hidden": {"_cssClasses": "accordion-content-wrapper"}}, "Content wrapper")
    t.add("text-basic", cw, {"text": "Answer to be supplied by the client. [VERIFY]", "tag": "p", "_cssGlobalClasses": gc("faq__answer")})
t.write("04-faq.json")

# ---------- 05 process steps ----------
t = Tree("process")
sec, con = section(t, "Process", "bg--ultra-light")
header(t, con, "How it works", "Three steps to moving day", None)
grid = t.add("div", con, {"_cssGlobalClasses": gc("process")}, "Steps")
for i, (title, text) in enumerate([("Get a quote", "Tell us what you're moving and when. Written quote, no surprises. [VERIFY copy]"),
                                    ("We plan the move", "Crew, truck and materials matched to your home and building rules. [VERIFY copy]"),
                                    ("Moving day", "Wrapped, loaded, delivered and set up. [VERIFY copy]")]):
    step = t.add("block", grid, {"_cssGlobalClasses": gc("process-step")}, f"Step {i+1}")
    t.add("text-basic", step, {"text": f"0{i+1}", "tag": "span", "_cssGlobalClasses": gc("process-step__number"),
                               "_attributes": [{"id": bid(f"stepno{i}"), "name": "aria-hidden", "value": "true"}]})
    t.add("heading", step, {"text": title, "tag": "h3", "_cssGlobalClasses": gc("process-step__title")})
    t.add("text-basic", step, {"text": text, "tag": "p", "_cssGlobalClasses": gc("process-step__text")})
t.write("05-process-steps.json")

# ---------- 06 stats ----------
t = Tree("stats")
sec, con = section(t, "Stats")
grid = t.add("div", con, {"_cssGlobalClasses": gc("stats")}, "Stats")
for i, (v, l) in enumerate([("[VERIFY]", "Google rating"), ("[VERIFY]", "Moves per year"), ("[VERIFY]", "Years in business"), ("2", "Branches")]):
    item = t.add("block", grid, {"_cssGlobalClasses": gc("stat-item")}, f"Stat {i+1}")
    t.add("text-basic", item, {"text": v, "tag": "span", "_cssGlobalClasses": gc("stat-item__value")})
    t.add("text-basic", item, {"text": l, "tag": "span", "_cssGlobalClasses": gc("stat-item__label")})
t.write("06-stats.json")

# ---------- 07 quote panel (WS Form) ----------
t = Tree("quote-panel")
sec, con = section(t, "Quote panel", "bg--ultra-dark")
panel = t.add("block", con, {"_cssGlobalClasses": gc("quote-panel")}, "Quote panel")
content = t.add("block", panel, {"_cssGlobalClasses": gc("quote-panel__content")}, "Content")
t.add("text-basic", content, {"text": "Free quote", "tag": "span", "_cssGlobalClasses": gc("eyebrow")})
t.add("heading", content, {"text": "Get your moving quote in 24 hours", "tag": "h2"})
t.add("text-basic", content, {"text": "Tell us where and when. A coordinator calls you back with a written price. [VERIFY copy]", "tag": "p"})
trust = t.add("block", content, {"tag": "ul", "_cssGlobalClasses": gc("quote-panel__trust")}, "Trust list")
for s in ["Licensed and insured [VERIFY]", "No hidden fees [VERIFY]", "Local and long-distance"]:
    t.add("text-basic", trust, {"text": s, "tag": "li", "_cssGlobalClasses": gc("quote-panel__trust-item")})
form = t.add("block", panel, {"_cssGlobalClasses": gc("quote-panel__form")}, "Form card")
t.add("shortcode", form, {"shortcode": '[ws_form id="4"]'})   # WS Form 4 = "Quick Quote Form EN" (staging export); FR = id 5
t.write("07-quote-panel.json")

# ---------- 08 mobile actions ----------
t = Tree("mobile-actions")
nav = t.add("block", 0, {"tag": "nav", "_cssGlobalClasses": gc("mobile-actions"),
                         "_attributes": [{"id": bid("navlabel"), "name": "aria-label", "value": "Quick actions"}]}, "Mobile actions")
t.add("button", nav, {"text": "Call 514-606-4030", "tag": "a", "link": {"type": "external", "url": "tel:+15146064030"},
                      "_cssClasses": "btn--neutral btn--m", "_cssGlobalClasses": gc("mobile-actions__btn")})  # btn--neutral exists after v2.0
t.add("button", nav, {"text": "Free quote", "tag": "a", "link": {"type": "external", "url": "/free-quote/"},
                      "_cssClasses": "btn--primary btn--m", "_cssGlobalClasses": gc("mobile-actions__btn")})
t.write("08-mobile-actions.json")

# ---------- ledger ----------
rows = []
for c in CLASSES.values():
    toks = sorted(set(re.findall(r"var\((--[a-z0-9-]+)\)", json.dumps(c["settings"]))))
    rows.append(f"| `{c['name']}` | `{c['id']}` | {', '.join(f'`{x}`' for x in toks) or '—'} |")
open(os.path.join(OUT, "README.md"), "w").write("\n".join([
    "# Crown Movers v6.0 — component library (draft)", "",
    f"Format: Bricks clipboard JSON, `version` {VER}, generated {os.popen('date -u +%Y-%m-%d').read().strip()} from `gen_v6.py`.",
    "Import: Bricks builder → right-click canvas → *Paste* (Ctrl/Cmd+V after copying the file contents). Global classes ride with each file and merge by name.", "",
    "## Gates before import",
    "1. **v2.0 saved** — classes reference `--accent`, `.btn--neutral`, `--radius` ≥ 6px; on the current dashboard those render missing/tiny.",
    "2. **v3.0 done** — the stale `hero__*`, `section-header*`, `eyebrow`, `faq__*`, `stats*`, `process*`, `testimonial*`, `pit-*`, `u-*` global classes must be deleted first. Bricks merges pasted classes **by name onto the existing class** and keeps the existing (Montserrat/`--secondary`) settings, so a paste over stale classes silently loses these styles.", "",
    "## Rules these files obey",
    "- Zero element-level style keys (generator asserts it). Zero hex/rgb. Zero px except the 1px ACSS `--border-size` equivalent on cards and one documented 4px exception.",
    "- Every colour, size, gap, radius, shadow, transition is an ACSS variable verified in `docs/audit/acss-variables.txt`.",
    "- ACSS utilities attached as plain classes: `section--m`, `bg--ultra-light`, `bg--ultra-dark`, `btn--primary`, `btn--neutral`, `btn--m`.",
    "- Layout grids use ACSS grid variables (`--grid-auto-3`, `--grid-auto-4`, `--grid-2`) — ACSS 4 registers no grid utility classes on this install.", "",
    "## Documented exceptions",
    "- `section-header` / `faq` max-width `62ch` / `72ch` — typographic measure; ACSS has no measure token.",
    "- `testimonial-card` 4px accent rule — no ACSS token for a thick rule; single occurrence in `_cssCustom`.",
    "- `mobile-actions` sets `body { padding-bottom }` under 767px so the fixed bar never covers content; `767px` is the Bricks `mobile_landscape` breakpoint literal (Bricks cannot use a variable inside a media query).", "",
    "## Content placeholders", "Every `[VERIFY]` string is unsupported by project evidence and must not ship. Form id 4 = *Quick Quote Form EN*, 5 = FR (from `wsform-forms.tsv`). Phone 514-606-4030 is the number on the live site header.", "",
    "## Class ledger", "| Class | id | ACSS tokens used |", "|---|---|---|", *rows, ""]))
print("classes:", len(CLASSES))
