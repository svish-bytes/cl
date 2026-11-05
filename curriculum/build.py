"""Builds The Operator's Curriculum (akitsuu edition) as HTML; render.js prints it to PDF."""
import pathlib, re
from data import BUSINESS, STRATEGY, CD, MODELS
from figs import FIGS, RECALL, loop, ak_lockup, ak_mark

HERE = pathlib.Path(__file__).parent
OUT = HERE / "operators-curriculum.html"

def one_highlight(html):
    """akitsuu rule: one highlighted (Garamond italic) word or phrase per layout."""
    seen = [False]
    def sub(m):
        if not seen[0]:
            seen[0] = True
            return f'<span class="hl">{m.group(1)}</span>'
        return f'<strong class="hl2">{m.group(1)}</strong>'
    return re.sub(r"<em>(.*?)</em>", sub, html, flags=re.S)

page_no = [0]
def page(body, label="", cls=""):
    page_no[0] += 1
    n = page_no[0]
    foot = "" if "cover" in cls else (
        f'<footer class="pf">{ak_mark()}<span class="cap">{label}</span><span class="pf-n">{n:02d}</span></footer>')
    return f'<div class="page {cls}">{one_highlight(body)}{foot}</div>'

TRACK = {"biz": "Track C · Business acumen", "brand": "Track B · Brand strategy"}

def module(m):
    chips = [f'<span class="chip">{TRACK[m["track"]]}</span>']
    if m.get("star"):
        chips.append('<span class="chip">★ Shared skill</span>')
    if m.get("needs"):
        chips.append(f'<span class="chip">Needs {m["needs"]}</span>')
    if m["unlocks"] not in ("—", ""):
        chips.append(f'<span class="chip">Leads to {m["unlocks"]}</span>')
    fig_fn, caption = FIGS[m["code"]]
    pl = plate(m["code"])
    fig_svg = fig_fn()
    if pl:  # the plate carries this page's one red; the diagram drops to brown
        fig_svg = fig_svg.replace("var(--red)", "var(--brown)")
    mem = "".join(f"<li>{x}</li>" for x in m["mem"])
    ex = "".join(
        f'<li><p class="ex-t">{t}</p><p class="ex-d">{d}</p><p class="ex-m"><span>Output · {o}</span><span>{tm}</span></p></li>'
        for t, d, o, tm in m["ex"])
    q1, q2 = RECALL[m["code"]]
    return f"""
<div class="chips">{''.join(chips)}</div>
<header class="mod-h">
  <p class="code">{m['code']}</p>
  <div class="mod-tt"><h2>{m['title']}</h2><p class="why">{m['why']}</p></div>
</header>
<figure class="fig">{fig_svg}<figcaption><b>See it.</b> {caption}</figcaption></figure>
<div class="mod-b">
  <div class="mem"><h3>Memorise</h3><ol>{mem}</ol></div>
  <div class="apply"><h3>Apply</h3><ol>{ex}</ol>
    <p class="done"><span class="box"></span>Done when {m['done']}</p></div>
</div>
{pl}
<div class="recall"><p class="cap">Test yourself<br>tomorrow</p>
  <p class="q">{q1}<span></span></p><p class="q">{q2}<span></span></p></div>"""

def plate(code):
    """Botanical plate slot: drop plates/<code>.png (or .jpg) in and rebuild."""
    for ext in ("png", "jpg", "webp"):
        f = HERE / "plates" / f"{code}.{ext}"
        if f.exists():
            return f'<figure class="plate"><img src="plates/{code}.{ext}" alt=""></figure>'
    return ""

def lines(n):
    return "".join('<span class="ln"></span>' for _ in range(n))

P = []

# ---------------------------------------------------------------- cover
emerge = '<div class="cv-texbox">' + (HERE / "tex-emerge.svg").read_text().replace("#2B2321", "#F5F0E8").replace("<svg ", '<svg class="cv-tex" ', 1) + '</div>'
P.append(page(f"""
<div class="cv">
  {emerge}
  <div class="cv-top">{ak_lockup()}<p class="cv-for">Prepared for Svish<br>Trivandrum<br>November 2026</p></div>
  <div class="cv-mid">
    <h1>The <em>Operator’s</em><br>Curriculum</h1>
    <p class="cv-sub">Creative direction, brand strategy and business judgement. A 12 month workbook: what to memorise, what to practise on real clients, and what to prove by the end of each quarter.</p>
  </div>
  <div class="cv-tracks">
    <div><b>C</b><p>Business acumen<br>7 skills · start here</p></div>
    <div><b>B</b><p>Brand strategy<br>9 skills</p></div>
    <div><b>A</b><p>Creative direction<br>9 skills · refine</p></div>
  </div>
  <p class="cv-note">Indian tax and legal points are from memory and marked <i>verify</i>. Confirm them with a CA or lawyer before you act.</p>
</div>""", cls="cover"))

# ---------------------------------------------------------------- orientation
P.append(page(f"""
<h1 class="ph">Built around <em>where you are</em></h1>
<p class="lede">You have the eye. What decides whether the work lasts is pricing, cash, client choice and contracts. So business acumen comes first, brand strategy second, and creative direction is refined alongside. Strategy and business acumen are one skill seen from two sides: your client’s business, and your own.</p>
<div class="two">
  <div>
    <h3 class="sh">Your starting position</h3>
    <table class="pos">
      <tr><td>Visual and concept judgement</td><td class="lv">Strong</td><td>5+ years of film and animation concept work</td></tr>
      <tr><td>Audience psychology</td><td class="lv">Raw edge</td><td>BA psychology, not yet turned into written deliverables</td></tr>
      <tr><td>Content strategy</td><td class="lv">Partial</td><td>Tactical, one step below brand strategy</td></tr>
      <tr><td>Positioning and platforms</td><td class="lv">Gap</td><td>Track B builds this</td></tr>
      <tr><td>Financial command</td><td class="lv">Gap</td><td>Track C builds this</td></tr>
      <tr><td>Proof of effectiveness</td><td class="lv lv1">Biggest gap</td><td>One anchor client, and no case study with numbers yet</td></tr>
    </table>
  </div>
  <div>
    <h3 class="sh">Rules for the way your mind works</h3>
    <ol class="rules">
      <li><b>Output beats input.</b> For every hour of reading, spend two applying it to a live client. Reading feels like progress, but it isn’t.</li>
      <li><b>Work on two skills at a time:</b> one business skill and one strategy skill.</li>
      <li><b>A skill is done when its output exists.</b> Tick the box, not the chapter.</li>
      <li><b>When a week collapses,</b> protect two habits only: the receivables check and one practice session.</li>
      <li><b>When you’re blocked,</b> walk, game or sleep first, and come back after.</li>
      <li><b>Teach it back.</b> After each skill, write 200 words in your own voice. That is retrieval practice, and it doubles as LinkedIn content.</li>
    </ol>
  </div>
</div>
<figure class="fig"><h3 class="sh">The mastery loop: run it on every exercise</h3>{loop()}</figure>
<div class="wk1">
  <h3 class="sh">Your first seven days</h3>
  <ol>
    <li><span class="box"></span><p><b>Day 1</b> List every unpaid invoice with its age in days (C4).</p></li>
    <li><span class="box"></span><p><b>Day 2</b> Pull 3 months of statements and build a rough P&amp;L (C1).</p></li>
    <li><span class="box"></span><p><b>Day 3</b> Work out AIME’s share of your revenue (C2).</p></li>
    <li><span class="box"></span><p><b>Day 4</b> Book the CA session and send the agenda from C6.</p></li>
    <li><span class="box"></span><p><b>Day 5</b> Start the decision journal with one open decision (C7).</p></li>
    <li><span class="box"></span><p><b>Day 6</b> Ask AIME for enquiry and enrolment numbers for the last two seasons (B1).</p></li>
    <li><span class="box"></span><p><b>Day 7</b> Rest. Take a walk and let it settle.</p></li>
  </ol>
</div>""", label="Orientation"))

# ---------------------------------------------------------------- tree
def node(code, name, star=False, note="", start=False):
    s = '<i class="nst">★</i>' if star else ""
    n = f'<small>{note}</small>' if note else ""
    st = ' <span class="start">start here</span>' if start else ""
    return f'<div class="nd"><b>{code}</b><span>{name}{s}{st}</span>{n}</div>'

P.append(page(f"""
<h1 class="ph">The skill <em>tree</em></h1>
<p class="lede">Read it from the bottom up. The roots feed everything above them. A ★ shared skill builds two or more tracks with one round of practice, so do those first. The small notes show where a skill depends on another track.</p>
<div class="tree">
  <div class="tcol"><p class="tch">C · Business acumen</p>
    {node("C7","Decision quality",note="capstone · uses C1 to C6")}
    {node("C5","Sales and negotiation",True,"feeds A5")}
    {node("C3","Pricing and value",True,"feeds A5")}
    {node("C6","Contracts and tax",True,"feeds A8")}
    {node("C4","Cash and collections")}
    {node("C2","Unit economics",True,"feeds B1 · A6")}
    {node("C1","Financial literacy",note="opens most of the tree",start=True)}
  </div>
  <div class="tcol"><p class="tch">B · Brand strategy</p>
    {node("B9","Case studies",True,"proof for all tracks")}
    {node("B8","Effectiveness",note="needs C1")}
    {node("B6","Architecture and naming")}
    {node("B5","Brand platform")}
    {node("B7","Creative brief",True,"feeds A1 · A2")}
    {node("B4","Positioning")}
    {node("B3","Insight",True,"feeds A1")}
    {node("B2","Research",note="needs R2")}
    {node("B1","Client business read",note="needs C1 · C2")}
  </div>
  <div class="tcol"><p class="tch">A · Creative direction</p>
    {node("A5","Selling the work",note="needs C3 · C5")}
    {node("A8","Rights and legal",note="needs C6")}
    {node("A6","Production economics",note="needs C2")}
    {node("A7","Systems and guidelines")}
    {node("A4","Killing work")}
    {node("A3","Feedback language")}
    {node("A2","Briefing others",note="needs B7")}
    {node("A1","Idea vs execution",note="needs B3 · B7")}
    {node("A9","Taste calibration",note="daily, all year")}
  </div>
</div>
<div class="roots"><p class="cap">Roots</p>
  <div class="nd"><b>R1</b><span>Clear writing: one page thinking</span></div>
  <div class="nd"><b>R2</b><span>People psychology: you have this</span></div>
  <div class="nd"><b>R3</b><span>Numbers literacy</span></div>
</div>""", label="Map"))

# ---------------------------------------------------------------- critical path
steps = [("Wk 1 to 3", "C1", "Financial literacy"), ("Wk 3 to 5", "C2 ★", "Unit economics on your own studio"),
 ("Wk 5 to 10", "B1 to B3", "AIME read, interviews, insight"), ("Wk 10 to 14", "B4 · B7 ★", "Positioning and the one page brief"),
 ("Wk 14 to 20", "C3 ★ · C5 ★", "Pricing and sales, which open A5"), ("Wk 20 to 26", "C4 · C6 ★", "Cash and contracts, which cover A8"),
 ("Mo 7 to 9", "B5 · B6 · B8", "Platforms, naming, effectiveness"), ("Mo 9 to 12", "B9 ★ · C7", "Case studies and decision quality")]
st = "".join(f'<li><p class="cp-w">{w}</p><p class="cp-c">{c}</p><p class="cp-n">{n}</p></li>' for w, c, n in steps)
P.append(page(f"""
<h1 class="ph">The <em>critical path</em></h1>
<p class="lede">This is the fastest route through the tree. Each step opens the next. A9, taste calibration, runs underneath the whole year at 15 minutes a day.</p>
<ol class="cp">{st}</ol>
<div class="cp-under"><b>A9</b>Taste calibration: write 5 lines on one great piece of work every day, all year.</div>
<h3 class="sh" style="margin-top:10mm">Operating rhythm</h3>
<table class="rhythm">
  <tr><th>When</th><th>Time</th><th>What</th></tr>
  <tr><td>Daily</td><td>15 min</td><td>One breakdown (A9) and one insight worked backwards (B3)</td></tr>
  <tr><td>Weekly</td><td>30 min</td><td>Receivables check, pipeline review, decision journal entries</td></tr>
  <tr><td>Weekly</td><td>2 to 3 hrs</td><td>Applied practice on one live client</td></tr>
  <tr><td>Monthly</td><td>1 hr</td><td>Money review (template on page PG_MONEY) and journal review</td></tr>
  <tr><td>Monthly</td><td>1 hr</td><td>Outside critique with AD PROPHETS or a senior strategist</td></tr>
  <tr><td>Quarterly</td><td>Half day</td><td>Strategy review, scorecard, one finished case study</td></tr>
</table>
<div class="howto" style="margin-top:8mm"><h3 class="sh">How each skill page works</h3>
<dl>
  <dt>See it</dt><dd>An illustration of the idea. Redraw it from memory once before you move on.</dd>
  <dt>Memorise</dt><dd>Five or six points to know cold. Read them aloud once a day while the skill is active.</dd>
  <dt>Apply</dt><dd>Exercises on your real clients, each with an output and a time box. The output is your proof.</dd>
  <dt>Test yourself</dt><dd>Two questions to answer the next day, without looking. Spaced recall is what makes it stick.</dd>
</dl></div>
<p class="minimum"><b>Minimum week:</b> the receivables check and one practice session. Everything else can slip. Those two stay.</p>""", label="Map"))

# ---------------------------------------------------------------- business
for m in BUSINESS:
    P.append(page(module(m), label="Track C · Business acumen"))

rows = "".join(f'<li><p class="mm-n">{n}</p><p class="mm-q">{q}</p><p class="mm-u">{u}</p></li>' for n, q, u in MODELS)
P.append(page(f"""
<h1 class="ph">Twelve models to <em>memorise</em></h1>
<p class="lede">These are the thinking tools behind C7. Cover the right side and quiz yourself. Then name one live decision each model applies to this week.</p>
<ol class="mm-l">{rows}</ol>""", label="Track C · Business acumen"))

# ---------------------------------------------------------------- strategy
for m in STRATEGY:
    P.append(page(module(m), label="Track B · Brand strategy"))

P.append(page("""
<h1 class="ph">Strategy formulas, and your <em>unfair edge</em></h1>
<p class="lede">Learn the formulas word for word. The table below maps the psychology you already know to where it does work in this curriculum.</p>
<div class="formulas"><h3 class="sh">Formulas to learn by heart</h3>
<dl>
 <dt>Insight</dt><dd>[Audience] wants [X], but [tension], because [deeper why].</dd>
 <dt>Positioning</dt><dd>For [target] who [need], [brand] is the [frame] that [difference] because [proof].</dd>
 <dt>Proposition</dt><dd>One thing. If it contains an “and”, cut it in half.</dd>
 <dt>Personality</dt><dd>Adjective, but not [its excess]. Three times.</dd>
 <dt>Case study</dt><dd>Problem, insight, idea, execution, results, learning.</dd>
 <dt>Funnel</dt><dd>Awareness, enquiry, conversion, retention, referral. Work on the narrowest stage.</dd>
 <dt>Interview opener</dt><dd>“Tell me about the last time you…”</dd>
</dl></div>
<div class="psy"><h3 class="sh">Psychology you already own, mapped to the work</h3>
<table>
 <tr><td class="pn">Anchoring</td><td>The first number sets the frame. Show the top tier first.</td><td class="pm">C3</td></tr>
 <tr><td class="pn">Loss aversion</td><td>Frame the cost of doing nothing (empty seats, a missed season) before your price.</td><td class="pm">C5</td></tr>
 <tr><td class="pn">Social desirability</td><td>Parents say what sounds right. Ask what they did.</td><td class="pm">B2</td></tr>
 <tr><td class="pn">Availability heuristic</td><td>What comes to mind first gets chosen. That is mental availability.</td><td class="pm">B8</td></tr>
 <tr><td class="pn">Social proof</td><td>Case studies and named results do the selling for you.</td><td class="pm">B9</td></tr>
 <tr><td class="pn">Confirmation bias</td><td>Yours. Look for the interview that breaks your favourite insight.</td><td class="pm">B3 · C7</td></tr>
 <tr><td class="pn">Planning fallacy</td><td>Yours too. Add 50% to time and cost estimates by default.</td><td class="pm">C7</td></tr>
</table></div>""", label="Track B · Brand strategy"))

# ---------------------------------------------------------------- creative direction
def cdrow(r):
    code, name, mem, ex, needs = r
    nd = "" if needs == "—" else f'<p class="cd-d">Needs {needs}</p>'
    return (f'<li><p class="cd-c">{code}</p><div><p class="cd-n">{name}</p><p class="cd-m">{mem}</p></div>'
            f'<div><p class="cd-e"><b>Apply</b>{ex}</p>{nd}</div><span class="box"></span></li>')
P.append(page(f"""
<h1 class="ph">Track A · Creative <em>direction</em></h1>
<p class="trk-s">You already have the craft. These are the less visible skills that separate a senior creative director from a strong artist. Rate yourself 1 to 5 on each, and work on anything at 3 or below.</p>
<ol class="cdl">{''.join(cdrow(r) for r in CD)}</ol>""", label="Track A · Creative direction"))

# ---------------------------------------------------------------- roadmap
P.append(page("""
<h1 class="ph">Twelve months, <em>four proofs</em></h1>
<p class="lede">Each quarter ends with something you can show. If a quarter slips, move the dates, but keep the proof.</p>
<table class="road">
 <tr><th></th><th>Business</th><th>Strategy</th><th>Creative direction</th><th>Proof by quarter end</th></tr>
 <tr><td class="q">Q1<small>Nov to Jan</small></td><td>C1, C4. Money review habit. CA session on GST, TDS and tax regime.</td><td>B1 to B3. AIME read, interviews, insight.</td><td>Brief template. Feedback rewrite.</td><td><b>3 monthly P&amp;Ls. AIME research synthesis.</b></td></tr>
 <tr><td class="q">Q2<small>Feb to Apr</small></td><td>C2, C3. Unit economics. Pricing reset on new proposals.</td><td>B4, B5. Positioning and platforms for AIME, Bodhini, akitsuu and Elswheir.</td><td>Selling the work. Three objection drill.</td><td><b>Platforms done. New pricing used on 3 or more proposals.</b></td></tr>
 <tr><td class="q">Q3<small>May to Jul</small></td><td>C5, C6. Sales log. Master contract from a lawyer.</td><td>B6, B7. Service line naming. One page briefs.</td><td>Cost log. Rights clauses.</td><td><b>Signed master contract. AIME case study.</b></td></tr>
 <tr><td class="q">Q4<small>Aug to Oct</small></td><td>C7. Quarterly reviews. Pre-mortems on big bets.</td><td>B8, B9. Effectiveness metrics. Case writing.</td><td>50 or more taste breakdowns.</td><td><b>2 case studies. Annual review: revenue, margin, concentration, win rate.</b></td></tr>
</table>
<h3 class="sh" style="margin-top:10mm">Reading: one book at a time, only alongside its skill</h3>
<div class="read">
 <div><p class="rh">Business</p><p><em>The Personal MBA</em>, Kaufman · C1 to C7</p><p><em>Financial Intelligence for Entrepreneurs</em>, Berman and Knight · C1</p><p><em>Profit First</em>, Michalowicz · C4</p><p><em>The Win Without Pitching Manifesto</em>, Enns · C3</p><p><em>Never Split the Difference</em>, Voss · C5</p><p><em>Thinking in Bets</em>, Duke · C7</p></div>
 <div><p class="rh">Strategy</p><p><em>Strategy Is Your Words</em>, Pollard · B3 to B7</p><p><em>How Brands Grow</em>, Sharp · B8</p><p><em>The Long and the Short of It</em>, Binet and Field · B8</p><p><em>Positioning</em>, Ries and Trout · B4</p><p><em>Zag</em>, Neumeier · B4</p><p>Effie India, WARC and IPA cases · B9</p></div>
 <div><p class="rh">Creative direction</p><p><em>Hey Whipple, Squeeze This</em>, Sullivan · A1 to A5</p><p><em>A Technique for Producing Ideas</em>, Young · A1</p><p>Cannes Lions, D&amp;AD and One Show case films · A9</p></div>
</div>
<p class="fine">Titles are recommended from memory. Check editions and availability.</p>""".replace("<em>", "<cite>").replace("</em>", "</cite>").replace("Twelve months, <cite>four proofs</cite>", "Twelve months, <em>four proofs</em>"), label="Plan"))

# ---------------------------------------------------------------- templates
P.append(page(f"""
<h1 class="ph">Templates <em>to copy</em></h1>
<div class="tpl"><h3 class="sh">Decision journal: one per decision over ₹50,000 or longer than 3 months</h3>
 <div class="frm">
  <p><b>Date</b>{lines(1)}</p><p><b>Decision</b>{lines(1)}</p>
  <p><b>Options considered</b>{lines(2)}</p><p><b>What I expect will happen</b>{lines(2)}</p>
  <p class="row3"><span><b>Confidence</b> ____ %</span><span><b>One-way or two-way door?</b></span><span><b>Review on</b> ________</span></p>
  <p><b>What actually happened</b>{lines(2)}</p><p><b>Rule learned</b>{lines(1)}</p>
 </div></div>
<div class="tpl"><h3 class="sh">Pre-mortem: it is 12 months later and this failed. Why?</h3>
 <div class="frm">
  <p><b>The bet</b>{lines(1)}</p><p><b>Ten reasons it failed</b>{lines(6)}</p>
  <p><b>Top 3, ranked by likelihood × damage</b>{lines(2)}</p><p><b>Cheapest test of the riskiest assumption</b>{lines(1)}</p>
 </div></div>""", label="Tools"))

P.append(page(f"""
<div class="tpl"><h3 class="sh">Monthly money review: first Monday, one hour</h3>
 <table class="mr">
  <tr><td>Revenue this month</td><td></td><td>Cash in bank</td><td></td></tr>
  <tr><td>Direct costs</td><td></td><td>Owed to me (total)</td><td></td></tr>
  <tr><td>Gross margin %</td><td></td><td>Oldest unpaid invoice (days)</td><td></td></tr>
  <tr><td>Fixed costs and my salary</td><td></td><td>Committed costs, next 3 months</td><td></td></tr>
  <tr><td>Profit</td><td></td><td>Runway (months)</td><td></td></tr>
  <tr><td>Top client share %</td><td></td><td>Tax and GST account balance</td><td></td></tr>
 </table>
 <p class="frm-q"><b>One thing to change next month</b>{lines(1)}</p></div>
<div class="tpl"><h3 class="sh">Quarterly scorecard: rate each 1 to 5</h3>
 <table class="sc">
  <tr><th>Skill</th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th></tr>
  <tr><td>I know my monthly numbers from memory</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Receivables under one month of revenue</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Price set on value, walk-away number defined</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Top client under 40% of revenue</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I write a one page brief a stranger can use</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I build brand platforms from real research</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I state the idea in one sentence before visuals</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I present problem, insight, idea, execution</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Decision journal kept and reviewed monthly</td><td></td><td></td><td></td><td></td></tr>
  <tr class="key"><td>Case studies with numbers (count)</td><td></td><td></td><td></td><td></td></tr>
 </table>
 <p class="fine">The last row matters most. Clients, partners and your own confidence all rest on it.</p></div>""", label="Tools"))

# ---------------------------------------------------------------- assemble + brand checks
money_page = page_no[0]
body = "".join(P).replace("PG_MONEY", str(money_page))
body = re.sub(r"(\w)\s?–\s?(\w)", r"\1 to \2", body)        # ranges: "10 to 14", never a dash
body = body.replace(" — ", ": ").replace("—", "")
assert "–" not in body and "—" not in body, "dash left in copy"
for word in ["unlock", "elevate", "seamless", "game-changing", "world-class", "guaranteed", "next-gen"]:
    assert word not in re.sub(r"<[^>]+>", " ", body).lower(), f"never-say word: {word}"
assert "AKITSUU" not in body and "Akitsuu" not in body

CSS = (HERE / "style.css").read_text()
doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The Operator's Curriculum · akitsuu</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=EB+Garamond:ital,wght@1,400;1,500&family=Lexend:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS} cite{{font-style:normal;font-weight:600;}}</style></head><body>
{body}
</body></html>"""
OUT.write_text(doc)
print("pages:", page_no[0], "· money review on page", money_page)
