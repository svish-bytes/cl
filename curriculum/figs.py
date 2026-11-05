"""Inline SVG teaching illustrations + akitsuu logo. Colours come from CSS vars."""

INK = "var(--ink)"; INK2 = "var(--ink-2)"; RULE = "var(--rule)"; STOCK = "var(--stock)"
T = {"biz": "var(--brown)", "brand": "var(--brown)", "cd": "var(--brown)"}
R = "var(--red)"; IV = "var(--ivory)"

def svg(body, h=200, w=600):
    return (f'<svg class="fig-svg" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Lexend, sans-serif" font-size="11" fill="{INK}">{body.replace("url(#dots)", IV)}</svg>')

def tx(x, y, s, size=11, w=500, anchor="start", fill=INK, italic=False, serif=False):
    fam = ""
    st = ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}"{fam}{st}>{s}</text>'

def arrow_defs(c):
    return (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            f'<marker id="ahk" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<pattern id="dots" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.05" fill="{c}"/></pattern></defs>')

# ------------------------------------------------------------------ logo (supplied path, unchanged)
import pathlib as _p, re as _re
_LOCK = (_p.Path(__file__).parent / "akitsuu-lockup.svg").read_text()
_MARK_PATH = _re.search(r'<path fill-rule="evenodd" d="[^"]+"/>', _LOCK).group(0)
def ak_lockup(cls=""):
    return _LOCK.replace('<svg ', f'<svg class="ak-lockup {cls}" ', 1)
def ak_mark(cls=""):
    # the supplied path, unchanged; viewBox crops to the mark with one eye-width of clear space
    return f'<svg class="ak-mark {cls}" xmlns="http://www.w3.org/2000/svg" viewBox="33 255 1193 920" role="img" aria-label="akitsuu"><g fill="currentColor">{_MARK_PATH}</g></svg>'

def mark(size=28, acc="var(--logo-acc)", ink="currentColor"):
    return f'''<svg class="mark" width="{size}" height="{size}" viewBox="0 0 48 48" aria-hidden="true">
<ellipse cx="13.5" cy="17" rx="11" ry="3.3" transform="rotate(-14 13.5 17)" fill="{acc}"/>
<ellipse cx="34.5" cy="17" rx="11" ry="3.3" transform="rotate(14 34.5 17)" fill="{acc}"/>
<ellipse cx="14.5" cy="24" rx="9.6" ry="2.7" transform="rotate(12 14.5 24)" fill="none" stroke="{acc}" stroke-width="1.3"/>
<ellipse cx="33.5" cy="24" rx="9.6" ry="2.7" transform="rotate(-12 33.5 24)" fill="none" stroke="{acc}" stroke-width="1.3"/>
<rect x="23.1" y="12.5" width="1.8" height="31" rx=".9" fill="{ink}"/>
<circle cx="24" cy="9.2" r="2.7" fill="{ink}"/></svg>'''

def lockup(size=28, cls=""):
    return f'<span class="akl {cls}">{mark(size)}<span class="akw">akitsu<span class="aku">u</span></span></span>'

# ------------------------------------------------------------------ figures
def c1():
    c = T["biz"]; b = arrow_defs(c); base = 170; k = 1.35
    bars = [("Revenue", 0, 100, INK, "100"), ("Direct costs", 100, 70, "url(#dots)", "−30"),
            ("Gross margin", 70, 0, c, "70"), ("Fixed + your salary", 70, 25, "url(#dots)", "−45"),
            ("Profit", 25, 0, R, "25")]
    for i, (lab, top, bot, fill, val) in enumerate(bars):
        x = 30 + i * 92
        y1 = base - top * k; y2 = base - bot * k
        b += f'<rect x="{x}" y="{min(y1,y2)}" width="66" height="{abs(y2-y1)}" fill="{fill}" stroke="{c if "dots" in fill else "none"}" stroke-width=".8"/>'
        b += tx(x + 33, min(y1, y2) - 6, val, 12, 700, "middle")
        b += tx(x + 33, base + 16, lab, 9.5, 600, "middle", INK2)
        if i < 4:
            yy = base - (bot if i in (0, 2) else bot) * k if False else (base - (100 if i == 0 else 70 if i in (1, 2) else 25) * k)
            b += f'<line x1="{x+66}" y1="{yy}" x2="{x+92}" y2="{yy}" stroke="{INK2}" stroke-dasharray="2 2"/>'
    b += f'<line x1="20" y1="{base}" x2="490" y2="{base}" stroke="{INK}"/>'
    b += tx(549, 66, "Cash", 18, 600, "middle")
    b += tx(549, 86, "is what", 10, 500, "middle")
    b += tx(549, 100, "actually landed", 10, 500, "middle")
    b += tx(549, 114, "in the bank.", 10, 500, "middle")
    b += tx(549, 138, "≠ profit", 11, 700, "middle", c)
    return svg(b, 196)

def c2():
    c = T["biz"]; b = arrow_defs(c)
    rows = [("Big retainer", 90, 14), ("Brand film", 62, 31), ("Reel pack", 40, 21), ("Promo film", 55, 9), ("Rush job", 34, 3)]
    b += tx(0, 14, "REVENUE vs MARGIN, BY PROJECT", 9, 700, "start", INK2)
    for i, (n, rv, m) in enumerate(rows):
        y = 30 + i * 30
        b += tx(0, y + 13, n, 10.5, 600)
        b += f'<rect x="96" y="{y}" width="{rv*3.2}" height="18" fill="none" stroke="{INK}" stroke-width=".8"/>'
        b += f'<rect x="96" y="{y}" width="{m*3.2}" height="18" fill="{c}"/>'
        b += tx(96 + rv * 3.2 + 6, y + 13, f"{m}% margin" if True else "", 9.5, 600, "start", INK2)
    b += f'<rect x="96" y="186" width="10" height="8" fill="{c}"/>' + tx(110, 194, "margin", 9, 600, "start", INK2)
    b += f'<rect x="160" y="186" width="10" height="8" fill="none" stroke="{INK}"/>' + tx(174, 194, "revenue", 9, 600, "start", INK2)
    # donut
    cx, cy, r = 520, 98, 52; circ = 2 * 3.14159 * r; share = .55
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{RULE}" stroke-width="20"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{R}" stroke-width="20" stroke-dasharray="{circ*share} {circ}" transform="rotate(-90 {cx} {cy})"/>'
    # 40% tick
    import math
    a = -math.pi / 2 + 2 * math.pi * .40
    b += f'<line x1="{cx+(r-14)*math.cos(a)}" y1="{cy+(r-14)*math.sin(a)}" x2="{cx+(r+16)*math.cos(a)}" y2="{cy+(r+16)*math.sin(a)}" stroke="{INK}" stroke-width="1.6"/>'
    b += tx(cx + (r + 20) * math.cos(a), cy + (r + 26) * math.sin(a), "40% line", 9, 700, "middle")
    b += tx(cx, cy - 2, "55%", 18, 600, "middle")
    b += tx(cx, cy + 14, "one client", 9, 600, "middle", INK2)
    b += tx(cx, 186, "Concentration risk", 10, 700, "middle")
    return svg(b, 200)

def c3():
    c = T["biz"]; b = arrow_defs(c)
    x = 60; w = 110
    b += f'<rect x="{x}" y="20" width="{w}" height="50" fill="url(#dots)" stroke="{c}"/>'
    b += f'<rect x="{x}" y="70" width="{w}" height="60" fill="{R}"/>'
    b += f'<rect x="{x}" y="130" width="{w}" height="50" fill="none" stroke="{INK}"/>'
    for y, l in [(20, "Value to client"), (70, "Your price"), (130, "Your cost floor")]:
        b += f'<line x1="{x+w}" y1="{y}" x2="{x+w+40}" y2="{y}" stroke="{INK}"/>' + tx(x + w + 46, y + 4, l, 11, 700)
    b += tx(x + w / 2, 49, "client’s gain", 10, 700, "middle")
    b += tx(x + w / 2, 104, "your margin", 10, 700, "middle", STOCK)
    b += tx(x + w / 2, 160, "cost", 10, 600, "middle", INK2)
    b += tx(x - 10, 102, "VALUE-BASED", 8.5, 700, "end", INK2) if False else ""
    # tiers
    tx0 = 380
    b += tx(tx0, 22, "THREE OPTIONS", 9, 700, "start", INK2)
    tiers = [("Atelier", 40, "anchor"), ("Signature", 78, "target"), ("Essential", 116, "entry")]
    for n, y, role in tiers:
        hl = role == "target"
        b += f'<rect x="{tx0}" y="{y}" width="200" height="30" fill="{c if hl else "none"}" stroke="{c if hl else INK}"/>'
        b += tx(tx0 + 12, y + 20, n, 12, 400, "start", STOCK if hl else INK, True, True)
        b += tx(tx0 + 188, y + 19, role.upper(), 8.5, 700, "end", STOCK if hl else INK2)
    b += tx(tx0, 168, "Show the top first. It sets the frame.", 10, 500, "start", INK2)
    b += tx(tx0, 184, "Most buyers choose the middle.", 10, 500, "start", INK2)
    return svg(b, 196)

def c4():
    c = T["biz"]; b = arrow_defs(c)
    x0, x1 = 120, 580; wk = (x1 - x0) / 10
    for i in range(11):
        b += f'<line x1="{x0+i*wk}" y1="186" x2="{x0+i*wk}" y2="190" stroke="{INK2}"/>' + (tx(x0 + i * wk, 200, f"wk {i}", 8.5, 500, "middle", INK2) if i % 2 == 0 else "")
    b += f'<line x1="{x0}" y1="186" x2="{x1}" y2="186" stroke="{INK2}"/>'
    def row(y, label, sub, pays):
        s = tx(0, y + 10, label, 11, 700) + tx(0, y + 25, sub, 9, 500, "start", INK2)
        s += f'<rect x="{x0}" y="{y}" width="{wk*6}" height="16" fill="{INK}"/>' + tx(x0 + 6, y + 12, "WORK", 8.5, 700, "start", STOCK)
        for wkk, pct in pays:
            px = x0 + wkk * wk
            s += f'<line x1="{px}" y1="{y+56}" x2="{px}" y2="{y+24}" stroke="{c}" stroke-width="2" marker-end="url(#ah)"/>'
            s += tx(px, y + 68, pct, 10, 700, "middle", c)
        return s
    b += row(14, "Risky", "you fund the client", [(10, "100%")]).replace(c, R)
    b += f'<rect x="{x0+wk*6}" y="14" width="{wk*4}" height="16" fill="url(#dots)" stroke="{c}" stroke-width=".6"/>' + tx(x0 + wk * 8, 26, "gap", 9, 700, "middle")
    b += row(100, "Safe", "work never runs ahead", [(0, "50%"), (3, "25%"), (6, "25%")])
    return svg(b, 204)

def c5():
    c = T["biz"]; b = arrow_defs(c)
    y = 96; x0, x1 = 30, 570
    b += f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="1.4" marker-end="url(#ahk)"/>'
    b += tx(x1, y + 22, "price →", 9, 600, "end", INK2)
    b += f'<rect x="210" y="{y-26}" width="210" height="52" fill="url(#dots)" stroke="{c}"/>'
    b += tx(315, y + 4, "deal zone", 13, 600, "middle")
    def mk(x, top, l1, l2, col):
        yy = y - 40 if top else y + 40
        return (f'<line x1="{x}" y1="{y-30 if top else y+30}" x2="{x}" y2="{y}" stroke="{col}" stroke-width="2"/>'
                + tx(x, yy - (6 if top else -6), l1, 10.5, 700, "middle", col) + tx(x, yy + (8 if top else 20), l2, 9, 500, "middle", INK2))
    b += mk(210, True, "Your walk-away", "set before the call", R)
    b += mk(420, True, "Their maximum", "find it in discovery", INK)
    b += mk(500, False, "Your anchor", "open here", c)
    b += mk(110, False, "Weak BATNA", "you cave down here", INK2)
    return svg(b, 196)

def c6():
    c = T["biz"]; b = arrow_defs(c)
    steps = ["Signed scope", "Advance in", "Work", "Milestones", "Full payment", "IP transfers"]
    w = 92
    for i, s in enumerate(steps):
        x = 4 + i * (w + 6); last = i == len(steps) - 1
        b += f'<path d="M{x},16 h{w-12} l12,22 l-12,22 h-{w-12} l{12 if i else 0},-22 z" fill="{R if last else "none"}" stroke="{R if last else INK}"/>'
        b += tx(x + w / 2 + 3, 42, s, 9.5, 700, "middle", STOCK if last else INK)
    ox, oy = 330, 186
    b += tx(0, 112, "Usage rights are priced on three axes", 11, 700)
    b += tx(0, 128, "Widen any axis, raise the fee.", 10, 500, "start", INK2)
    b += f'<path d="M{ox},{oy} h110 l40,-26 v-46 h-110 l-40,26 z" fill="{IV}" stroke="{c}" stroke-width=".8"/>'
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox+190}" y2="{oy}" stroke="{INK}" marker-end="url(#ahk)"/>' + tx(ox + 196, oy + 4, "Territory", 10, 700)
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-92}" stroke="{INK}" marker-end="url(#ahk)"/>' + tx(ox - 8, oy - 84, "Medium", 10, 700, "end")
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox+92}" y2="{oy-60}" stroke="{c}" stroke-width="1.6" marker-end="url(#ah)"/>' + tx(ox + 98, oy - 62, "Term", 10, 700, "start", c)
    return svg(b, 196)

def c7():
    c = T["biz"]; b = arrow_defs(c)
    x0, y0, W, H = 70, 14, 400, 168
    b += f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="none" stroke="{INK}"/>'
    b += f'<rect x="{x0+W/2}" y="{y0}" width="{W/2}" height="{H/2}" fill="url(#dots)"/>'
    b += f'<line x1="{x0+W/2}" y1="{y0}" x2="{x0+W/2}" y2="{y0+H}" stroke="{INK}"/><line x1="{x0}" y1="{y0+H/2}" x2="{x0+W}" y2="{y0+H/2}" stroke="{INK}"/>'
    q = [(x0 + 12, y0 + 22, "Decide fast, then review", "Pricing test on one proposal", INK),
         (x0 + W / 2 + 12, y0 + 22, "Slow down: pre-mortem", "Hiring, equity, long contract", R),
         (x0 + 12, y0 + H / 2 + 22, "Just decide", "A new reel format", INK),
         (x0 + W / 2 + 12, y0 + H / 2 + 22, "Decide, but write it down", "A small annual subscription", INK)]
    for x, y, h, e, col in q:
        b += tx(x, y, h, 11.5, 700, "start", col) + tx(x, y + 16, e, 9.5, 500, "start", INK2)
    b += tx(x0 + W / 2, y0 + H + 16, "two-way door ←   REVERSIBILITY   → one-way door", 9, 700, "middle", INK2)
    b += f'<text x="{x0-12}" y="{y0+H/2}" font-size="9" font-weight="700" fill="{INK2}" text-anchor="middle" transform="rotate(-90 {x0-12} {y0+H/2})">low ←  STAKES  → high</text>'
    b += tx(490, 60, "Most decisions", 11, 700) + tx(490, 76, "are two-way doors.", 11, 700) + tx(490, 100, "Treat them that way", 10, 500, "start", INK2) + tx(490, 114, "and save your care for", 10, 500, "start", INK2) + tx(490, 128, "the top-right box.", 10, 500, "start", INK2)
    return svg(b, 200)

def b1():
    c = T["brand"]; b = arrow_defs(c)
    stages = [("Awareness", 70), ("Enquiry", 56), ("Conversion", 18), ("Retention", 40), ("Referral", 30)]
    x = 10; w = 112; cy = 80
    for i, (n, h) in enumerate(stages):
        nh = stages[i + 1][1] if i + 1 < len(stages) else h
        con = n == "Conversion"
        b += f'<path d="M{x},{cy-h} L{x+w},{cy-h} L{x+w},{cy+h} L{x},{cy+h} z" fill="{"url(#dots)" if con else "none"}" stroke="{R if con else INK}" stroke-width="{1.6 if con else 1}"/>'
        b += tx(x + w / 2, cy + 4, n, 10.5, 700, "middle", R if con else INK)
        x += w + 4
    b += tx(10 + 2 * 116 + 56, 128, "the constraint", 12, 600, "middle", R)
    b += f'<line x1="{10+2*116+56}" y1="132" x2="{10+2*116+56}" y2="104" stroke="{R}"/>'
    b += tx(10, 172, "Fix the narrowest stage first. More awareness poured into a blocked conversion stage is wasted spend.", 10, 500, "start", INK2)
    return svg(b, 186)

def b2():
    c = T["brand"]; b = arrow_defs(c)
    for cx, cy, l in [(150, 82, "SAY"), (230, 82, "DO"), (190, 146, "FEEL")]:
        b += f'<circle cx="{cx}" cy="{cy}" r="62" fill="none" stroke="{INK}"/>'
    b += f'<circle cx="190" cy="104" r="16" fill="{R}"/>'
    b += tx(118, 66, "SAY", 11, 700, "middle") + tx(262, 66, "DO", 11, 700, "middle") + tx(190, 186, "FEEL", 11, 700, "middle")
    b += f'<line x1="206" y1="104" x2="330" y2="104" stroke="{c}" marker-end="url(#ah)"/>'
    b += tx(338, 100, "Insight lives in the gaps", 13, 600, "start")
    b += tx(338, 118, "“I want him to choose freely” (say)", 10, 500, "start", INK2)
    b += tx(338, 133, "… but she picked his subjects (do)", 10, 500, "start", INK2)
    b += tx(338, 150, "Illustrative example", 8.5, 600, "start", INK2, True)
    return svg(b, 196)

def b3():
    c = T["brand"]; b = arrow_defs(c)
    boxes = [(10, "Truth", "something real about them", "none", INK), (200, "Tension", "what gets in the way", "url(#dots)", c), (410, "Insight", "“huh, that’s true”", R, STOCK)]
    for x, h, s, f, col in boxes:
        b += f'<rect x="{x}" y="40" width="170" height="78" fill="{f}" stroke="{(R if f==R else c) if f!="none" else INK}"/>'
        b += tx(x + 85, 78, h, 18, 600, "middle", col) + tx(x + 85, 98, s, 9.5, 600, "middle", col if col == STOCK else INK2)
    b += tx(190, 86, "+", 24, 300, "middle") + tx(395, 86, "=", 24, 300, "middle")
    b += tx(10, 160, "Observation: “Students want good marks.”  True, but no tension, so it isn’t an insight.", 10, 500, "start", INK2)
    return svg(b, 180)

def b4():
    c = T["brand"]; b = arrow_defs(c)
    cx, cy = 190, 96
    b += f'<line x1="30" y1="{cy}" x2="350" y2="{cy}" stroke="{INK}" marker-end="url(#ahk)" marker-start="url(#ahk)"/>'
    b += f'<line x1="{cx}" y1="10" x2="{cx}" y2="182" stroke="{INK}" marker-end="url(#ahk)" marker-start="url(#ahk)"/>'
    b += tx(30, cy - 8, "Mass", 9.5, 700, "start", INK2) + tx(350, cy - 8, "Premium", 9.5, 700, "end", INK2)
    b += tx(cx + 8, 20, "Mentor", 9.5, 700, "start", INK2) + tx(cx + 8, 180, "Exam factory", 9.5, 700, "start", INK2)
    for x, y in [(80, 140), (110, 160), (70, 120), (240, 150), (270, 135), (130, 60), (300, 160)]:
        b += f'<circle cx="{x}" cy="{y}" r="7" fill="{INK2}" opacity=".55"/>'
    b += f'<circle cx="290" cy="42" r="26" fill="url(#dots)" stroke="{c}" stroke-dasharray="3 3"/><circle cx="290" cy="42" r="8" fill="{R}"/>'
    b += f'<line x1="318" y1="42" x2="380" y2="42" stroke="{c}" marker-start="url(#ah)"/>'
    b += tx(388, 40, "Own the empty space", 13, 600, "start")
    b += tx(388, 58, "Grey dots: competitors.", 10, 500, "start", INK2)
    b += tx(388, 73, "Pick axes that customers", 10, 500, "start", INK2)
    b += tx(388, 87, "actually care about.", 10, 500, "start", INK2)
    b += tx(388, 112, "Illustrative axes", 8.5, 600, "start", INK2, True)
    return svg(b, 192)

def b5():
    c = T["brand"]; b = arrow_defs(c)
    layers = [("Purpose", "only if true", 120), ("Values", "as behaviours", 180), ("Personality", "3 × “but not”", 240), ("Messages", "1 core + 3 supporting", 300), ("Proof", "evidence under every claim", 360)]
    for i, (n, s, w) in enumerate(layers):
        y = 8 + i * 36; x = 200 - w / 2
        f = R if i == 4 else ("url(#dots)" if i == 0 else "none")
        b += f'<rect x="{x}" y="{y}" width="{w}" height="31" fill="{f}" stroke="{R if i == 4 else (c if i == 0 else INK)}"/>'
        b += tx(200, y + 20, n, 11.5, 600, "middle", STOCK if i == 4 else INK)
        b += f'<line x1="{x+w+6}" y1="{y+16}" x2="420" y2="{y+16}" stroke="{RULE}"/>' + tx(426, y + 20, s, 10, 600, "start", INK2)
    return svg(b, 192)

def b6():
    c = T["brand"]; b = arrow_defs(c)
    def grp(x, title, sub, mode):
        s = tx(x + 80, 186, title, 11, 700, "middle") + tx(x + 80, 200, sub, 9, 500, "middle", INK2)
        if mode == 0:
            s += f'<circle cx="{x+80}" cy="80" r="56" fill="url(#dots)" stroke="{c}"/>'
            for dx, dy in [(-24, -10), (0, 18), (24, -10), (0, -30)]:
                s += f'<circle cx="{x+80+dx}" cy="{80+dy}" r="11" fill="{c}"/>'
        elif mode == 1:
            for dx, dy in [(-40, 90), (0, 110), (40, 90)]:
                s += f'<circle cx="{x+80+dx}" cy="{dy}" r="20" fill="none" stroke="{INK}"/><circle cx="{x+80+dx+14}" cy="{dy-14}" r="7" fill="{c}"/>'
            s += f'<circle cx="{x+80}" cy="38" r="14" fill="{R}"/>'
            for dx, dy in [(-40, 90), (0, 110), (40, 90)]:
                s += f'<line x1="{x+80}" y1="52" x2="{x+80+dx}" y2="{dy-20}" stroke="{RULE}"/>'
        else:
            for dx, dy, r in [(-45, 60, 22), (30, 50, 16), (-20, 120, 18), (45, 115, 24)]:
                s += f'<circle cx="{x+80+dx}" cy="{dy}" r="{r}" fill="none" stroke="{INK}"/>'
        return s
    b += grp(10, "Branded house", "one name carries all", 0)
    b += grp(215, "Endorsed", "sub-brands, master signs off", 1)
    b += grp(420, "House of brands", "each stands alone", 2)
    return svg(b, 206)

def b7():
    c = T["brand"]; b = arrow_defs(c)
    b += f'<path d="M20,20 L260,90 L260,110 L20,180 z" fill="none" stroke="{INK}"/>'
    b += f'<path d="M340,90 L580,20 L580,180 L340,110 z" fill="none" stroke="{INK}"/>'
    b += f'<rect x="260" y="84" width="80" height="32" fill="{R}"/>' + tx(300, 105, "ONE thing", 11, 700, "middle", STOCK)
    for i, l in enumerate(["research", "data", "insights", "mandatories", "client wishes"]):
        b += tx(30, 56 + i * 24, l, 10, 600, "start", INK2)
    for i, l in enumerate(["film", "posts", "print", "site", "events"]):
        b += tx(570, 56 + i * 24, l, 10, 600, "end", INK2)
    b += tx(300, 140, "single-minded", 11, 600, "middle", c) + tx(300, 156, "proposition", 11, 600, "middle", c)
    return svg(b, 196)

def b8():
    c = T["brand"]; b = arrow_defs(c)
    x0, y0 = 40, 170
    b += f'<line x1="{x0}" y1="{y0}" x2="560" y2="{y0}" stroke="{INK}" marker-end="url(#ahk)"/><line x1="{x0}" y1="{y0}" x2="{x0}" y2="14" stroke="{INK}" marker-end="url(#ahk)"/>'
    b += tx(560, y0 + 16, "time", 9, 600, "end", INK2)
    b += f'<text x="{x0-12}" y="92" font-size="9" font-weight="600" fill="{INK2}" text-anchor="middle" transform="rotate(-90 {x0-12} 92)">sales effect</text>'
    d = f"M{x0},{y0-6}"
    for k in range(5):
        sx = x0 + 20 + k * 100
        d += f" L{sx},{y0-6} L{sx+8},{y0-70} L{sx+40},{y0-12} L{sx+100},{y0-8}"
    b += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    b += f'<path d="M{x0},{y0-4} C200,{y0-20} 380,{y0-90} 545,{y0-136}" fill="none" stroke="{R}" stroke-width="2.6"/>'
    b += tx(430, 40, "Brand building", 12, 600, "start") + tx(430, 55, "slow, compounding", 9.5, 600, "start", INK2)
    b += tx(70, 88, "Activation", 12, 600, "start") + tx(70, 103, "fast spikes, fade quickly", 9.5, 600, "start", INK2)
    b += tx(300, 194, "Illustrative shape, after Binet &amp; Field", 8.5, 600, "middle", INK2, True)
    return svg(b, 200)

def b9():
    c = T["brand"]; b = arrow_defs(c)
    pts = [(30, 150, "Problem"), (140, 128, "Insight"), (250, 104, "Idea"), (360, 92, "Execution"), (470, 40, "Results"), (570, 60, "Learning")]
    d = "M" + " L".join(f"{x},{y}" for x, y, _ in pts)
    b += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    for x, y, l in pts:
        hl = l == "Results"
        b += f'<circle cx="{x}" cy="{y}" r="{9 if hl else 5}" fill="{R if hl else STOCK}" stroke="{R if hl else INK}" stroke-width="1.4"/>'
        b += tx(x, y + (26 if not hl else -16), l, 10.5 if not hl else 12, 700, "middle")
    b += tx(470, 74, "numbers here", 9.5, 600, "middle", INK2)
    b += tx(30, 192, "Most portfolios stop at Execution. The client is paying for Results.", 10, 500, "start", INK2)
    return svg(b, 200)

def loop():
    c = "var(--brown)"; b = arrow_defs(c)
    names = [("Predict", "write expectation + confidence"), ("Do", "ship it, real stakes"), ("Measure", "what happened, in numbers"), ("Review", "where was I wrong?"), ("Critique", "monthly, someone senior")]
    for i, (n, s) in enumerate(names):
        x = 10 + i * 120
        b += f'<circle cx="{x+16}" cy="24" r="14" fill="{c if i==0 else "none"}" stroke="{c}"/>' + tx(x + 16, 29, str(i + 1), 12, 600, "middle", STOCK if i == 0 else c)
        b += tx(x, 58, n, 11, 700) + tx(x, 73, s, 9, 500, "start", INK2)
        if i < 4:
            b += f'<line x1="{x+34}" y1="24" x2="{x+116}" y2="24" stroke="{INK}" marker-end="url(#ahk)"/>'
    b += f'<path d="M{10+4*120+16},40 C{10+4*120+40},96 40,96 26,44" fill="none" stroke="{c}" stroke-dasharray="3 3" marker-end="url(#ah)"/>'
    b += tx(300, 98, "repeat: every loop makes the next prediction better", 9.5, 600, "middle", c)
    return svg(b, 104)

FIGS = {
 "C1": (c1, "Profit is what’s left after you pay yourself. Cash is the only one that pays bills. Illustrative numbers."),
 "C2": (c2, "Big revenue can hide thin margin. And when one client passes the 40% line, your studio’s fate is in their hands. Illustrative."),
 "C3": (c3, "Price between your cost and their value. Show three options, anchored by the top one."),
 "C4": (c4, "Same project, two payment plans. In the first, you are a bank lending to your client for free."),
 "C5": (c5, "Know your walk-away before you talk. A strong alternative (BATNA) keeps you out of the cave-in zone."),
 "C6": (c6, "The order that protects you: rights move only after the money does."),
 "C7": (c7, "Sort decisions by how reversible they are and how much is at stake. Spend your care where both are high."),
 "B1": (b1, "Every funnel has one narrowest point. That is the brief."),
 "B2": (b2, "Research isn’t transcription. Look for where saying, doing and feeling disagree."),
 "B3": (b3, "An insight needs tension. Without it you only have an observation."),
 "B4": (b4, "Map the category on two axes customers care about, then claim space no one owns."),
 "B5": (b5, "Build the platform bottom-up from proof. Purpose sits on top only if it’s true."),
 "B6": (b6, "Three ways to organise a family of brands. Choose deliberately."),
 "B7": (b7, "A brief narrows everything to one idea, so the work can open up again."),
 "B8": (b8, "Activation spikes and fades. Brand building compounds. You need both."),
 "B9": (b9, "The arc of a case study. Results are the peak the reader is looking for."),
}

RECALL = {
 "C1": ["Write the break-even formula from memory.", "Why is GST in your account not your money?"],
 "C2": ["Why is the effective hourly rate never your price?", "What concentration level is a red flag?"],
 "C3": ["Which tier do you present first, and why?", "What must you remove before you lower a price?"],
 "C4": ["What advance % do you ask for on project work?", "When is your receivables total a red flag?"],
 "C5": ["Name the five discovery questions.", "What is a BATNA, and why does it calm you?"],
 "C6": ["What are the three axes of usage rights?", "When does IP transfer to the client?"],
 "C7": ["Process or outcome: which do you judge a decision by?", "What do you assume about cost and time?"],
 "B1": ["Name the five funnel stages.", "What is the constraint, and why work there?"],
 "B2": ["Why ask about the past, not the future?", "Which bias distorts parents’ answers?"],
 "B3": ["Say the insight formula.", "What three tests must an insight pass?"],
 "B4": ["Say the positioning statement template.", "Why is positioning a sacrifice?"],
 "B5": ["How do you write a value so it’s usable?", "What does “but not” do for personality?"],
 "B6": ["Name the three brand architectures.", "What do you write before generating names?"],
 "B7": ["How long is a brief?", "What does single-minded mean in practice?"],
 "B8": ["What two kinds of availability make brands grow?", "When are metrics agreed?"],
 "B9": ["List the six parts of a case study.", "What does a client quote add?"],
}
