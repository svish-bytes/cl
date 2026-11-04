"""Builds the Operator's Curriculum HTML; render.js turns it into PDF."""
import html, pathlib

OUT = pathlib.Path(__file__).parent / "operators-curriculum.html"

def e(s):  # allow inline <b>/<i>/<em> markup written by hand
    return s

# ---------------------------------------------------------------- data
BUSINESS = [
 dict(code="C1", title="Financial literacy", track="biz",
  why="Every other skill on this page needs numbers to stand on. You can’t price, choose clients or judge a bet you can’t measure.",
  unlocks="C2 · C4 · C6 · B1 · B8",
  mem=[
   "Revenue is vanity, profit is sanity, <em>cash is reality.</em>",
   "Profit = revenue − all costs, <b>including a fair salary for you.</b> If you don’t pay yourself, the profit isn’t real.",
   "Gross margin = (revenue − direct project costs) ÷ revenue. Direct costs are tool credits, freelancers, vendors and partner shares.",
   "Break-even = monthly fixed costs ÷ gross margin %.",
   "Runway = cash in bank ÷ monthly burn.",
   "GST you collect is <b>not your money.</b> Keep it separate the day it arrives."],
  ex=[
   ("Build the Elswheir P&amp;L", "Last 3 months, every rupee in and out: Higgsfield and AI subscriptions, freelancers, partner splits with AD PROPHETS and AEVORO, internet, equipment.", "One-sheet P&amp;L", "2 hrs"),
   ("Find your break-even", "Fixed monthly costs plus your minimum salary, divided by your margin. Write the number on a card above your desk.", "One number", "30 min"),
   ("Set up a tax account", "Open a separate account for GST and tax. Move a fixed % of every receipt into it. Ask your CA what the % should be.", "Standing instruction", "1 hr")],
  done="you can state last month’s revenue, margin, cash, receivables and break-even from memory."),
 dict(code="C2", title="Unit economics", track="biz", star=True,
  why="This tells you which work actually makes you money. The same lens becomes client diagnosis (B1) and production economics (A6).",
  unlocks="C3 · B1 · A6",
  mem=[
   "Effective rate = fee ÷ actual hours. <b>Use it to diagnose, never to price.</b>",
   "Chase <em>margin</em> per project, not revenue per project.",
   "CAC is the time and money it takes to win a client. LTV is the margin earned over the whole relationship.",
   "Healthy LTV is roughly 3× CAC or more. This is a SaaS rule of thumb; use it as a rough guide.",
   "If one client is over ~40% of revenue, losing them is an existential risk (rough threshold).",
   "Revisions silently eat your margin."],
  ex=[
   ("Review your last 5 projects", "AIME, C0C0N promo, Bodhini and two more. For each: quoted vs actual hours, tool credits, revision rounds, final margin. Rank them by margin.", "Ranked table", "3 hrs"),
   ("Check your AIME dependence", "What share of the last 12 months’ revenue came from AIME? If it’s over 40%, set a 90-day target to land one more retainer.", "% plus target", "45 min"),
   ("Cost per finished second", "Total production cost of your AI video pipeline ÷ seconds delivered. This is your internal floor for any quote.", "Floor rate", "1 hr")],
  done="you know your three most and least profitable kinds of work, and why."),
 dict(code="C3", title="Pricing &amp; value", track="biz", star=True,
  why="Value-based pricing is your stated model. This module turns it from a belief into a method you can defend in front of a client.",
  unlocks="C5 · A5",
  mem=[
   "Price to the <em>value of the outcome,</em> not your effort.",
   "Value = what the result is worth in the <b>client’s currency:</b> enrolments, sales, price premium.",
   "Always offer three options. The middle is your target and the top sets the anchor.",
   "Never cut price without removing scope.",
   "Write your walk-away number <b>before</b> the call.",
   "If you win more than ~70% of pitches, you are probably underpriced (rough heuristic)."],
  ex=[
   ("Do the AIME value maths", "Fee per student × the extra enrolments a campaign could plausibly drive = the value at stake. Decide the share of it you can defend, and write down your reasoning.", "Value sheet", "1 hr"),
   ("Price the Dubai client in three tiers", "Essential / Signature / Atelier, priced in AED, with the top tier as the anchor. Check the AED–INR rate on the day.", "3-tier proposal", "2 hrs"),
   ("Retire the rate card", "Rewrite your services as packages, each with scope, number of revisions, usage rights and timeline.", "Package sheet", "2 hrs")],
  done="every proposal states the client’s value before your price."),
 dict(code="C4", title="Cash &amp; collections", track="biz",
  why="Profitable studios still die of empty bank accounts. This module is mostly habit, not theory.",
  unlocks="C7",
  mem=[
   "Work never runs <b>ahead of payment.</b>",
   "Take a 40–50% advance on project work and bill the rest by milestone.",
   "Invoice the day a milestone is hit. Follow up on fixed days.",
   "Money owed to you above one month of revenue is a red flag.",
   "Put a late-payment clause in every contract.",
   "Keep a 3–6 month buffer covering personal and studio costs (rough guide)."],
  ex=[
   ("List what you’re owed", "Every unpaid invoice today, with its age in days. Chase anything over 30 days this week.", "Receivables list", "30 min"),
   ("Write three follow-up templates", "A friendly one for day 3, a firm one for day 15, a final notice for day 30. Write them once and reuse them.", "3 templates", "45 min"),
   ("Calculate your runway", "Cash in bank ÷ (studio plus personal monthly costs). If it’s under 3 months, that becomes priority one.", "Months of runway", "20 min")],
  done="receivables stay under one month of revenue for a full quarter."),
 dict(code="C5", title="Sales &amp; negotiation", track="biz", star=True,
  why="You already read people well. This module turns that into a repeatable process, and covers your partner deals.",
  unlocks="A5",
  mem=[
   "Ask before you pitch: <b>problem, impact, budget, decision-maker, timeline.</b>",
   "Know your BATNA, your best alternative if the deal dies. The stronger it is, the calmer you negotiate.",
   "<em>Trade, don’t give.</em> Every concession should get you something back.",
   "Silence is a tool. Let the client fill it.",
   "Name the emotion: “It sounds like timing is the real concern.”",
   "For every partnership, write down what each side gives and what each side gets."],
  ex=[
   ("Script your discovery call", "Run the five questions on the next lead and log the answers in a sales sheet with a dated next step.", "Sales log row", "Each call"),
   ("Map partner economics", "AD PROPHETS, AEVORO, and the Bodhini alliance: who brings leads, who delivers, the % splits, who owns the client relationship. Mark any imbalance.", "One-page map", "1.5 hrs"),
   ("Prepare objections for Girl Rising", "Write the three objections they are most likely to raise to your producer pitch, with your answer to each.", "Objection sheet", "45 min")],
  done="you never end a sales call without knowing the budget signal and who decides."),
 dict(code="C6", title="Contracts, tax &amp; compliance", track="biz", star=True,
  why="Mistakes here are expensive and hard to undo. This module also covers creative usage rights (A8). Verify every point below with a CA or lawyer.",
  unlocks="A8 · C7",
  mem=[
   "No work starts without <b>signed scope plus advance.</b>",
   "IP transfers only on <em>full payment.</em>",
   "Price usage rights separately by medium, territory and term. Cap your liability at the fee.",
   "GST: registration is generally required above ₹20 lakh aggregate turnover for services. <i>From memory, verify.</i>",
   "Exports such as the Dubai work may be zero-rated under a LUT if they meet the export conditions. Keep the FIRC/FIRA. <i>Verify.</i>",
   "Reconcile TDS against Form 26AS/AIS every quarter, or you lose the credit."],
  ex=[
   ("Book a CA session", "Agenda: GST status, whether 44ADA applies to your work, which TDS sections clients use, the LUT for Dubai, export paperwork.", "Written answers", "1 hr"),
   ("Get a master contract", "One master service agreement plus a SOW template, drafted by a lawyer. Do it once and reuse it.", "Templates", "Lawyer fee"),
   ("Find what isn’t written down", "Check the AIME and Dubai arrangements: is any scope, payment term or rights clause only verbal?", "Gap list", "1 hr")],
  done="you know your quarterly tax dates and every active client has a signed agreement."),
 dict(code="C7", title="Decision quality", track="biz",
  why="This is the capstone, and it’s what being a “grounded but successful” businessman comes down to: deciding well on incomplete information, again and again.",
  unlocks="Everything",
  mem=[
   "Judge a decision by its <b>process,</b> not its outcome. Good calls can still lose.",
   "One-way doors go slow, two-way doors go fast.",
   "Assume 1.5× the cost and 2× the time. Plan cash around that.",
   "Grounded means protecting the downside. Successful means taking <em>sized</em> bets on the upside.",
   "Make many small, survivable bets rather than a few large ones.",
   "Write down what you expect <b>before</b> you know the result."],
  ex=[
   ("Pre-mortem the backup model", "Kerala healthcare institute: “It’s 2028 and it failed. Why?” List 10 reasons, rank the top 3, and design the cheapest test for the riskiest one.", "Pre-mortem sheet", "1.5 hrs"),
   ("Keep a decision journal", "Log every decision above ₹50,000 or longer than 3 months, using the template at the back. Review it monthly.", "Journal", "10 min each"),
   ("Run a quarterly review", "Where did revenue come from? What should you stop, start, continue? What is the single biggest risk?", "One page", "Half day")],
  done="you have 12 months of journal entries and can name your three most common mistakes in judgement."),
]

STRATEGY = [
 dict(code="B1", title="Client business diagnosis", track="brand",
  why="Most marketing problems are business problems in disguise. Find the real one before you touch a brief.",
  unlocks="B2", needs="C1 · C2",
  mem=[
   "Ask: how do they make money, and <b>where does it leak?</b>",
   "Map the funnel: awareness → enquiry → conversion → retention → referral.",
   "Find the <em>constraint,</em> the one stage that limits growth. Work there.",
   "Seasonality decides timing. For NEET/JEE that means results season and admission windows.",
   "A client asking for “more reels” rarely needs more reels."],
  ex=[
   ("AIME on one page", "Fee structure, cost per enquiry, enquiry-to-enrolment conversion, competitor fees, seasonal calendar. Circle the constraint.", "Diagnosis page", "3 hrs"),
   ("Bodhini on one page", "Channels, repeat-purchase rate, margin per bottle, who buys vs who uses. Ask AD PROPHETS for the data.", "Diagnosis page", "2 hrs")],
  done="you can explain each client’s growth constraint in one sentence."),
 dict(code="B2", title="Research", track="brand",
  why="Your psychology degree is a real advantage here. This is where it starts showing up in client deliverables.",
  unlocks="B3", needs="R2 · B1",
  mem=[
   "Ask about <b>past behaviour,</b> not future intentions.",
   "Open with: <em>“Tell me about the last time you…”</em>",
   "5–8 interviews usually surface most patterns (common qualitative practice).",
   "Keep what people <b>say, do and feel</b> separate.",
   "Don’t lead and don’t pitch. Watch for social-desirability bias, especially with parents."],
  ex=[
   ("Interview six AIME families", "Students and parents, in Malayalam, Tamil or English, recorded with consent. Synthesise into patterns, tensions and verbatim quotes.", "Synthesis board", "1 week"),
   ("Audit five competitors", "Five coaching institutes’ ads: claims, tone, visual codes. Plot them on two axes and find the empty space.", "Competitor map", "3 hrs")],
  done="you’ve produced a synthesis a stranger could act on."),
 dict(code="B3", title="Insight", track="brand", star=True,
  why="This is the hinge between strategy and creative. A sharp insight makes your ideas (A1) sharper at the same time.",
  unlocks="B4 · A1", needs="B2",
  mem=[
   "An observation is not an insight.",
   "Insight = a truth + a <b>tension</b> + the reaction “huh, that’s true”.",
   "Formula: <em>[Audience] wants [X], but [tension], because [deeper why].</em>",
   "Test every one: is it true, non-obvious, and something the brand can act on?",
   "The best insights live in the <b>contradictions</b> in your research."],
  ex=[
   ("Write 20, keep 3", "From the AIME interviews, write 20 candidate insights in the formula. Cut to 3 and test each against the three questions.", "3 insights", "2 hrs"),
   ("Daily reverse-engineering", "For one ad you see each day, write the insight behind it in the formula. Five minutes.", "Insight log", "5 min/day")],
  done="your insights make clients pause before they nod."),
 dict(code="B4", title="Positioning", track="brand",
  why="Positioning is deciding what to give up. It applies to every client, and to Elswheir itself.",
  unlocks="B5 · B7", needs="B3",
  mem=[
   "<em>For</em> [target] <em>who</em> [need], [brand] <em>is the</em> [frame of reference] <em>that</em> [difference] <em>because</em> [proof].",
   "Positioning is sacrifice: choosing <b>who you’re not for.</b>",
   "The frame of reference sets what you get compared against.",
   "The difference must matter to the customer and be defensible.",
   "Proof beats claims."],
  ex=[
   ("Position Elswheir", "Write the statement, then a “we are not” list. For example: not an AI content mill, not a cheap reel factory.", "Statement + not-list", "1.5 hrs"),
   ("Position AIME and the Dubai house", "One statement each. For the couture house, map it against three other Dubai couture labels first.", "2 statements", "2 hrs")],
  done="each statement fits in one breath and excludes someone."),
 dict(code="B5", title="Brand platform", track="brand",
  why="The platform is the single page that keeps every future asset consistent, including work that isn’t made by you.",
  unlocks="B6", needs="B4",
  mem=[
   "Purpose: <b>only if it’s true.</b> No purpose is better than a fake one.",
   "Write values as behaviours: “We show the cost before the work”, not “Transparency”.",
   "Personality: three adjectives, each with a <em>“but not”</em> (bold, but not loud).",
   "Messages: one core message, three supporting, proof for each.",
   "If it doesn’t fit on one page, the choices haven’t been made yet."],
  ex=[
   ("Three platforms", "One page each for AIME, Bodhini and Elswheir. Use “this, not that” pairs for personality and voice.", "3 pages", "1 day"),
   ("Pressure test", "Give a platform to a freelancer with no other briefing. Does what they produce feel on-brand?", "Test result", "1 week")],
  done="someone else can make on-brand work from your page alone."),
 dict(code="B6", title="Architecture &amp; naming", track="brand",
  why="You have a live naming project right now. Set the criteria first and generate names second.",
  unlocks="—", needs="B5",
  mem=[
   "Three architectures: branded house, house of brands, endorsed.",
   "Name types: descriptive, invented, metaphor, founder, acronym.",
   "Criteria: distinct, easy to say, ownable (trademark and domain), clean in every target language, room to grow.",
   "<b>Write the criteria before you generate names.</b>",
   "Test names out loud with people from the target market, not with friends."],
  ex=[
   ("Dragonfly agency names", "Criteria first, including <em>must not read as India or MENA.</em> Generate 50, screen against the criteria, check trademark and domain, then test pronunciation with 5 people in the target markets.", "Shortlist of 3", "1 week"),
   ("Map AIME × Arcane", "Is Arcane a sub-brand, endorsed, or separate? Draw it, and write the rule for when the AIME name appears.", "Architecture map", "1 hr")],
  done="the shortlist passes every criterion on paper."),
 dict(code="B7", title="The creative brief", track="brand", star=True,
  why="The brief is where strategy turns into creative work. Writing better briefs also makes you a better director (A1, A2).",
  unlocks="A1 · A2", needs="B4 · R1",
  mem=[
   "One page, always.",
   "Single-minded proposition = <b>one thing.</b> Not two.",
   "A brief is a <em>springboard, not a fence.</em>",
   "If you can’t say it in one line, the strategy isn’t finished.",
   "Always include what success looks like: a metric."],
  ex=[
   ("Rewrite one brief", "Rewrite the next AIME or C0C0N brief on one page. Hand it to a partner and count the revision rounds.", "Brief + count", "1.5 hrs"),
   ("The stranger test", "Give a brief to someone with no context. Can they explain the job back to you in 30 seconds?", "Pass / fail", "15 min")],
  done="your briefs average two revision rounds or fewer."),
 dict(code="B8", title="Growth &amp; effectiveness", track="brand",
  why="This is how you prove your work moves the business, and it’s what justifies value-based pricing.",
  unlocks="B9", needs="C1",
  mem=[
   "Brands grow mainly by reaching <b>more buyers,</b> including light buyers (Sharp).",
   "Build mental availability (easy to think of) and physical availability (easy to buy).",
   "Distinctive assets such as colours, characters and sounds only work if you keep them <em>consistent.</em>",
   "Balance long-term brand building with short-term activation. Binet &amp; Field’s ~60:40 is an average that varies by category. <i>From memory.</i>",
   "Agree the metrics <b>before</b> the work starts."],
  ex=[
   ("Set AIME’s metrics", "Before the next campaign, agree on three: enquiries, cost per enquiry, enrolments. Build a simple tracker you both see.", "Metric sheet", "1 hr"),
   ("Audit Bodhini’s assets", "What is consistent across every touchpoint? What keeps changing? Recommend the 2–3 assets to lock in.", "Asset audit", "2 hrs")],
  done="every active client has agreed metrics on paper."),
 dict(code="B9", title="Case-study writing", track="brand", star=True,
  why="Case studies are the proof for all three tracks. They are what your next client, partner or investor will judge you on.",
  unlocks="Proof", needs="B8",
  mem=[
   "Structure: problem → insight → idea → execution → <b>results</b> → learning.",
   "<em>Numbers, or it didn’t happen.</em>",
   "A short client quote adds trust that design can’t.",
   "Write for the client you want next, not the one you had.",
   "Check the NDA before naming anyone."],
  ex=[
   ("The AIME case", "Done by Q3. One page plus a 60-second film cut. Get the enrolment and enquiry numbers from AIME in writing.", "Case study", "1 day"),
   ("The Dubai case", "Ask permission early. If you can’t name them, write an anonymised version with the numbers kept.", "Case study", "1 day")],
  done="you have two cases with numbers you can send without explanation."),
]

CD = [
 ("A1", "Idea vs execution", "If it can’t be said in one sentence, <em>it isn’t an idea yet.</em>",
  "Before any frames for Els Prophecy or C0C0N, write the idea as one line. Keep the line pinned above the edit timeline.", "B3 · B7"),
 ("A2", "Briefing others", "Revision rounds measure <em>your brief,</em> not their talent.",
  "Track revisions per brief and aim for two or fewer. Keep a reusable prompt-brief template for Nano Banana via Higgsfield.", "B7"),
 ("A3", "Feedback language", "Name the problem and the goal. <em>Let them find the fix.</em>",
  "Rewrite your last 10 feedback notes as “X doesn’t yet feel Y, because Z.”", "—"),
 ("A4", "Killing work", "Your loyalty is to the brief, <em>not the frame.</em>",
  "Log one thing you cut per project and why. Review the log quarterly.", "—"),
 ("A5", "Selling the work", "Problem → insight → idea → execution. <em>Never open with visuals.</em>",
  "Before every presentation, write the three objections you expect. Afterwards, note which ones actually came up.", "C3 · C5"),
 ("A6", "Production economics", "Know your <em>cost per finished second.</em>",
  "Keep a cost log per project: hours, credits, vendors, revisions. Compare it with the quote.", "C2"),
 ("A7", "Systems &amp; guidelines", "Work nobody else can extend <em>stops growing when you step away.</em>",
  "Ship a two-page mini guideline with every identity or campaign project.", "—"),
 ("A8", "Rights &amp; legal", "Price usage separately: <em>medium, territory, term.</em>",
  "Add a rights clause to every quote. Ask a lawyer about AI-output copyright in India, music and font licences, and talent releases.", "C6"),
 ("A9", "Taste calibration", "Taste is <em>judgement you can put into words.</em>",
  "Every day, write 5 lines on one piece of award-winning work: insight, idea, craft choice, the emotion it targets, and the bias it uses.", "R2"),
]

MODELS = [
 ("Opportunity cost", "What am I not doing if I say yes?", "A low-fee project vs time spent on the Dubai wedge."),
 ("Base rates", "How does this usually go for people like me?", "A new revenue line: assume it is slower and smaller."),
 ("Second-order effects", "And then what?", "A discount for one client becomes the price everyone expects."),
 ("Inversion", "How would I guarantee this fails?", "Then avoid exactly that."),
 ("Pre-mortem", "It’s a year later and it failed. Why?", "Run it before any big commitment."),
 ("Expected value", "Probability × payoff, compared across options.", "Which pitches deserve your week."),
 ("Reversibility", "Is this a one-way or a two-way door?", "Hiring, equity and long contracts are one-way doors."),
 ("Margin of safety", "What if it costs 1.5× and takes 2× as long?", "Cash planning, launch timing."),
 ("Concentration", "What breaks if one thing fails?", "One client, one partner, one platform."),
 ("Incentives", "What does each party actually gain?", "Partner splits, client stakeholders."),
 ("Sunk cost", "Would I start this today, knowing what I know?", "Long pitches going nowhere."),
 ("Circle of competence", "Do I actually know this, or do I just feel confident?", "Healthcare, trading, new markets."),
]

# ---------------------------------------------------------------- render helpers
def module(m):
    star = '<span class="star" title="Shared node">★ shared</span>' if m.get("star") else ""
    needs = f'<span>Needs <b>{m["needs"]}</b></span>' if m.get("needs") else ""
    mem = "".join(f"<li>{x}</li>" for x in m["mem"])
    ex = "".join(
        f'<li><p class="ex-t">{t}</p><p class="ex-d">{d}</p><p class="ex-m"><span>Output · {o}</span><span>{tm}</span></p></li>'
        for t, d, o, tm in m["ex"])
    return f"""
<section class="mod t-{m['track']}">
  <header class="mod-h">
    <p class="code">{m['code']}</p>
    <div class="mod-tt">
      <h2>{m['title']} {star}</h2>
      <p class="why">{m['why']}</p>
    </div>
    <p class="deps">{needs}<span>Unlocks <b>{m['unlocks']}</b></span></p>
  </header>
  <div class="mod-b">
    <div class="mem"><h3>Memorise</h3><ol>{mem}</ol></div>
    <div class="apply"><h3>Apply</h3><ol>{ex}</ol>
      <p class="done"><span class="box"></span>Done when {m['done']}</p></div>
  </div>
</section>"""

LOGO = '<span class="logo"><span class="l1">Els</span><span class="l2">wheir</span></span>'

page_no = [0]
def page(body, track="", label="", cls=""):
    page_no[0] += 1
    n = page_no[0]
    foot = "" if "cover" in cls else f"""
  <footer class="pf"><span class="pf-l">{LOGO}</span><span class="pf-t {track}">{label}</span><span class="pf-n">{n:02d}</span></footer>"""
    return f'<div class="page {cls}">{body}{foot}</div>'

def track_head(name, color, sub):
    return f'<div class="trk {color}"><p class="trk-n">{name}</p><p class="trk-s">{sub}</p></div>'

# ---------------------------------------------------------------- pages
P = []

# Cover
P.append(page(f"""
<div class="cv">
  <div class="cv-top">{LOGO.replace('logo','logo logo-xl')}<p class="cv-for">Prepared for Svish · Trivandrum · November 2026</p></div>
  <div class="cv-mid">
    <h1>The <em>Operator’s</em><br>Curriculum</h1>
    <p class="cv-sub">Creative direction, brand strategy and business judgement. A 12-month workbook with what to memorise, what to practise, and what to prove.</p>
  </div>
  <div class="cv-bands">
    <div class="cvb biz"><span>C</span><p>Business<br>Acumen</p></div>
    <div class="cvb brand"><span>B</span><p>Brand<br>Strategy</p></div>
    <div class="cvb cd"><span>A</span><p>Creative<br>Direction</p></div>
  </div>
  <p class="cv-note">Indian tax and legal points in this workbook are from memory and are marked <i>verify</i>. Confirm them with a CA or lawyer before you act.</p>
</div>""", cls="cover"))

# How it's built for you
P.append(page(f"""
<h1 class="ph">Built around <em>where you are</em></h1>
<p class="lede">You have the eye. What decides whether Elswheir lasts is pricing, cash, client choice and contracts. So the order is <b>business acumen first, brand strategy second,</b> and creative direction refined alongside. Strategy and business acumen are one skill seen from two sides: thinking about your client’s business, and thinking about your own.</p>

<div class="two">
  <div>
    <h3 class="sh">Your starting position</h3>
    <table class="pos">
      <tr><td>Visual &amp; concept judgement</td><td class="lv lv5">Strong</td><td>5+ years film and animation concept work</td></tr>
      <tr><td>Audience psychology</td><td class="lv lv4">Raw edge</td><td>BA psychology, not yet turned into written deliverables</td></tr>
      <tr><td>Content strategy</td><td class="lv lv3">Partial</td><td>Tactical level, one step below brand strategy</td></tr>
      <tr><td>Positioning &amp; platforms</td><td class="lv lv2">Gap</td><td>Track B builds this</td></tr>
      <tr><td>Financial command</td><td class="lv lv2">Gap</td><td>Track C builds this</td></tr>
      <tr><td>Proof of effectiveness</td><td class="lv lv1">Biggest gap</td><td>One anchor client and no case studies with numbers yet</td></tr>
    </table>
  </div>
  <div>
    <h3 class="sh">Rules for the way your mind works</h3>
    <ol class="rules">
      <li><b>Output, not input.</b> For every hour of reading, spend two hours applying it to a live client. Reading feels like progress. It isn’t.</li>
      <li><b>Work on two skills at a time, no more:</b> one business skill and one strategy skill.</li>
      <li><b>A skill counts as done only when its output exists.</b> Tick the box, not the chapter.</li>
      <li><b>When a week collapses,</b> protect just two habits: the receivables check and one practice session.</li>
      <li><b>When you’re blocked,</b> walk, game or sleep first. Come back after. Don’t force output.</li>
      <li><b>Teach it back.</b> After each skill, write a 200-word post in your own words. It’s retrieval practice, and it doubles as Elswheir LinkedIn content.</li>
    </ol>
  </div>
</div>

<h3 class="sh">The mastery loop: run it on every exercise</h3>
<div class="loop">
  <div><span>1</span><b>Predict</b><p>Write what you expect and how confident you are.</p></div>
  <div><span>2</span><b>Do</b><p>Ship it to a real client with real stakes.</p></div>
  <div><span>3</span><b>Measure</b><p>Record what actually happened, in numbers.</p></div>
  <div><span>4</span><b>Review</b><p>Where was your model wrong? Write the rule.</p></div>
  <div><span>5</span><b>Critique</b><p>Monthly, with someone more senior than you.</p></div>
</div>

<div class="wk1">
  <h3 class="sh">Your first seven days</h3>
  <ol>
    <li><span class="box"></span><p><b>Day 1.</b> List every unpaid invoice with its age in days (C4).</p></li>
    <li><span class="box"></span><p><b>Day 2.</b> Pull 3 months of bank statements and build the rough P&amp;L (C1).</p></li>
    <li><span class="box"></span><p><b>Day 3.</b> Work out AIME’s share of your revenue (C2).</p></li>
    <li><span class="box"></span><p><b>Day 4.</b> Book the CA session and send the agenda from C6.</p></li>
    <li><span class="box"></span><p><b>Day 5.</b> Start the decision journal with one open decision (C7).</p></li>
    <li><span class="box"></span><p><b>Day 6.</b> Ask AIME for enquiry and enrolment numbers for the last two seasons (B1).</p></li>
    <li><span class="box"></span><p><b>Day 7.</b> Rest. Walk. Let it settle.</p></li>
  </ol>
</div>
""", label="Orientation"))

# Skill tree
def node(code, name, cls, star=False, note=""):
    s = '<i class="nst">★</i>' if star else ""
    n = f'<small>{note}</small>' if note else ""
    return f'<div class="nd {cls}"><b>{code}</b><span>{name}{s}</span>{n}</div>'

P.append(page(f"""
<h1 class="ph">The skill <em>tree</em></h1>
<p class="lede">Read it from the bottom up. Roots feed everything above them. A <b>★ shared skill</b> builds two or more tracks with one round of practice, so do those first. The small notes show where a skill depends on another track.</p>

<div class="tree">
  <div class="tcol">
    <p class="tch biz">C · Business acumen</p>
    {node("C7","Decision quality","biz",note="capstone · uses C1–C6")}
    {node("C5","Sales &amp; negotiation","biz",True,"→ A5")}
    {node("C3","Pricing &amp; value","biz",True,"→ A5")}
    {node("C6","Contracts &amp; tax","biz",True,"→ A8")}
    {node("C4","Cash &amp; collections","biz")}
    {node("C2","Unit economics","biz",True,"→ B1 · A6")}
    {node("C1","Financial literacy","biz",note="unlocks most of the tree")}
  </div>
  <div class="tcol">
    <p class="tch brand">B · Brand strategy</p>
    {node("B9","Case studies","brand",True,"proof for all tracks")}
    {node("B8","Effectiveness","brand",note="needs C1")}
    {node("B6","Architecture &amp; naming","brand")}
    {node("B5","Brand platform","brand")}
    {node("B7","Creative brief","brand",True,"→ A1 · A2")}
    {node("B4","Positioning","brand")}
    {node("B3","Insight","brand",True,"→ A1")}
    {node("B2","Research","brand",note="needs R2")}
    {node("B1","Client diagnosis","brand",note="needs C1 · C2")}
  </div>
  <div class="tcol">
    <p class="tch cd">A · Creative direction</p>
    {node("A5","Selling the work","cd",note="needs C3 · C5")}
    {node("A8","Rights &amp; legal","cd",note="needs C6")}
    {node("A6","Production economics","cd",note="needs C2")}
    {node("A7","Systems &amp; guidelines","cd")}
    {node("A4","Killing work","cd")}
    {node("A3","Feedback language","cd")}
    {node("A2","Briefing others","cd",note="needs B7")}
    {node("A1","Idea vs execution","cd",note="needs B3 · B7")}
    {node("A9","Taste calibration","cd",note="daily, throughout")}
  </div>
</div>
<div class="roots">
  <p class="roots-l">Roots</p>
  <div class="nd root"><b>R1</b><span>Clear writing: one-page thinking</span></div>
  <div class="nd root"><b>R2</b><span>People psychology: you have this</span></div>
  <div class="nd root"><b>R3</b><span>Numbers literacy</span></div>
</div>
""", label="Map"))

# Critical path + rhythm
steps = [
 ("Wk 1–3", "C1", "Financial literacy", "biz"),
 ("Wk 3–5", "C2★", "Unit economics on Elswheir", "biz"),
 ("Wk 5–10", "B1–B3", "AIME diagnosis, interviews, insight", "brand"),
 ("Wk 10–14", "B4 B7★", "Positioning and the one-page brief", "brand"),
 ("Wk 14–20", "C3★ C5★", "Pricing and sales; unlocks A5", "biz"),
 ("Wk 20–26", "C4 C6★", "Cash, contracts; covers A8", "biz"),
 ("Mo 7–9", "B5 B6 B8", "Platforms, naming, effectiveness", "brand"),
 ("Mo 9–12", "B9★ C7", "Case studies and decision quality", "brand"),
]
st = "".join(f'<li class="{c}"><p class="cp-w">{w}</p><p class="cp-c">{code}</p><p class="cp-n">{n}</p></li>' for w, code, n, c in steps)
P.append(page(f"""
<h1 class="ph">The <em>critical path</em></h1>
<p class="lede">This is the fastest route through the tree. Each step unlocks the next. <b>A9 taste calibration</b> runs underneath the whole time, at 15 minutes a day.</p>
<ol class="cp">{st}</ol>
<div class="cp-under cd"><b>A9</b> Taste calibration: a 5-line breakdown of one great piece of work every day, all year</div>

<h3 class="sh" style="margin-top:12mm">Operating rhythm</h3>
<table class="rhythm">
  <tr><th>When</th><th>Time</th><th>What</th></tr>
  <tr><td>Daily</td><td>15 min</td><td>One breakdown (A9) and one insight reverse-engineered (B3)</td></tr>
  <tr><td>Weekly</td><td>30 min</td><td>Receivables check, pipeline review, decision-journal entries</td></tr>
  <tr><td>Weekly</td><td>2–3 hrs</td><td>Applied practice on one live client</td></tr>
  <tr><td>Monthly</td><td>1 hr</td><td>Money review (template p. 17) and journal review</td></tr>
  <tr><td>Monthly</td><td>1 hr</td><td>Outside critique with AD PROPHETS or a senior strategist</td></tr>
  <tr><td>Quarterly</td><td>Half day</td><td>Strategy review, scorecard, one finished case study</td></tr>
</table>
<div class="howto">
  <h3 class="sh">How to read a module</h3>
  <dl>
    <dt>Memorise</dt><dd>Five or six points to know cold. Read them aloud once a day while the skill is active. Quiz yourself with the right side covered.</dd>
    <dt>Apply</dt><dd>Exercises on your real clients, each with an output and a time box. The output is the proof the skill is learned.</dd>
    <dt>Done when</dt><dd>The test for moving on. Tick it only when it’s true, not when the reading is finished.</dd>
    <dt>Needs / Unlocks</dt><dd>Where the skill sits in the tree. Don’t start a skill before the ones it needs.</dd>
  </dl>
</div>
<p class="minimum"><b>Minimum viable week:</b> receivables check and one practice session. Everything else can slip. These two can’t.</p>
""", label="Map"))

# Business modules: 2 per page
biz_pages = [BUSINESS[0:2], BUSINESS[2:4], BUSINESS[4:6], BUSINESS[6:7]]
for i, grp in enumerate(biz_pages):
    head = track_head("Track C · Business acumen", "biz", "Thinking about your own business: money, pricing, deals, risk. Start here.") if i == 0 else ""
    P.append(page(head + "".join(module(m) for m in grp) + ("" if i < 3 else '<div class="spacer"></div>'), track="biz", label="C · Business acumen"))

# Models (flash list)
rows = "".join(f'<li><p class="mm-n">{n}</p><p class="mm-q">{q}</p><p class="mm-u">{u}</p></li>' for n, q, u in MODELS)
P[-1] = P[-1].replace('<div class="spacer"></div>', f"""
<div class="mm"><h3 class="sh">C7 · The twelve models to memorise</h3>
<p class="mm-i">Cover the right two columns and quiz yourself. Then name one live decision each model applies to this week.</p>
<ol class="mm-l">{rows}</ol></div>""")

# Strategy modules
st_pages = [STRATEGY[0:2], STRATEGY[2:4], STRATEGY[4:6], STRATEGY[6:8], STRATEGY[8:9]]
for i, grp in enumerate(st_pages):
    head = track_head("Track B · Brand strategy", "brand", "Thinking about your client’s business: finding the truth, defining the brand, proving it worked.") if i == 0 else ""
    extra = ""
    if i == 4:
        extra = """
<div class="formulas"><h3 class="sh">Strategy formulas: learn them by heart</h3>
<dl>
 <dt>Insight</dt><dd>[Audience] wants [X], but [tension], because [deeper why].</dd>
 <dt>Positioning</dt><dd>For [target] who [need], [brand] is the [frame] that [difference] because [proof].</dd>
 <dt>Proposition</dt><dd>One thing. If it has an “and”, cut it in half.</dd>
 <dt>Personality</dt><dd>Adjective, but not [its excess]. ×3.</dd>
 <dt>Case study</dt><dd>Problem → insight → idea → execution → results → learning.</dd>
 <dt>Funnel</dt><dd>Awareness → enquiry → conversion → retention → referral. Work on the constraint.</dd>
 <dt>Interview opener</dt><dd>“Tell me about the last time you…”</dd>
</dl></div>
<div class="psy"><h3 class="sh">Your unfair edge: psychology you already own, mapped to the work</h3>
<table>
 <tr><td class="pn">Anchoring</td><td>The first number sets the frame. Show the top tier first.</td><td class="pm">C3</td></tr>
 <tr><td class="pn">Loss aversion</td><td>Frame the cost of inaction (empty seats, missed season) before your price.</td><td class="pm">C5</td></tr>
 <tr><td class="pn">Social desirability</td><td>Parents say what sounds right. Ask what they <em>did.</em></td><td class="pm">B2</td></tr>
 <tr><td class="pn">Availability heuristic</td><td>What comes to mind first gets chosen. That is mental availability.</td><td class="pm">B8</td></tr>
 <tr><td class="pn">Social proof</td><td>Case studies and named results do the selling for you.</td><td class="pm">B9</td></tr>
 <tr><td class="pn">Confirmation bias</td><td>Yours. Look for the interview that breaks your favourite insight.</td><td class="pm">B3 · C7</td></tr>
 <tr><td class="pn">Planning fallacy</td><td>Yours too. Add 50% to time and cost estimates by default.</td><td class="pm">C7</td></tr>
</table></div>"""
    P.append(page(head + "".join(module(m) for m in grp) + extra, track="brand", label="B · Brand strategy"))

# CD pages
def cdrow(r):
    code, name, mem, ex, needs = r
    return f'<li><p class="cd-c">{code}</p><div><p class="cd-n">{name}</p><p class="cd-m">{mem}</p></div><div><p class="cd-e"><b>Apply</b> {ex}</p>{'' if needs=='—' else f'<p class="cd-d">Needs {needs}</p>'}</div><span class="box"></span></li>'
P.append(page(track_head("Track A · Creative direction", "cd", "You already have the craft. These are the unglamorous skills that separate a senior CD from a strong artist. Rate yourself 1–5 on each and work on anything 3 or below.")
 + f'<ol class="cdl">{"".join(cdrow(r) for r in CD)}</ol>', track="cd", label="A · Creative direction"))

# Roadmap
P.append(page("""
<h1 class="ph">Twelve months, <em>four proofs</em></h1>
<p class="lede">Each quarter ends with something you can show. If a quarter slips, move the dates, but don’t skip the proof.</p>
<table class="road">
 <tr><th></th><th class="biz">Business</th><th class="brand">Strategy</th><th class="cd">Creative direction</th><th>Proof by quarter end</th></tr>
 <tr><td class="q">Q1<small>Nov–Jan</small></td><td>C1, C4. Money review habit. CA session on GST, TDS and the tax regime.</td><td>B1–B3. AIME diagnosis, interviews, insight.</td><td>Brief template. Feedback rewrite.</td><td><b>3 monthly P&amp;Ls. AIME research synthesis.</b></td></tr>
 <tr><td class="q">Q2<small>Feb–Apr</small></td><td>C2, C3. Unit economics. Pricing reset on new proposals.</td><td>B4–B5. Positioning and platforms for AIME, Bodhini and Elswheir.</td><td>Selling the work. Three-objection drill.</td><td><b>3 platforms. New pricing used on 3+ proposals.</b></td></tr>
 <tr><td class="q">Q3<small>May–Jul</small></td><td>C5, C6. Sales log. Master contract from a lawyer.</td><td>B6–B7. Dragonfly naming. One-page briefs.</td><td>Cost log. Rights clauses.</td><td><b>Signed master contract. AIME case study.</b></td></tr>
 <tr><td class="q">Q4<small>Aug–Oct</small></td><td>C7. Quarterly reviews. Pre-mortems on big bets.</td><td>B8–B9. Effectiveness metrics. Case writing.</td><td>50+ taste breakdowns.</td><td><b>2 case studies. Annual review of revenue, margin, concentration, win rate.</b></td></tr>
</table>

<h3 class="sh" style="margin-top:10mm">Reading: one book at a time, only alongside its skill</h3>
<div class="read">
 <div class="biz"><p class="rh">Business</p><p><i>The Personal MBA</i>, Kaufman · C1–C7</p><p><i>Financial Intelligence for Entrepreneurs</i>, Berman &amp; Knight · C1</p><p><i>Profit First</i>, Michalowicz · C4</p><p><i>The Win Without Pitching Manifesto</i>, Enns · C3</p><p><i>Never Split the Difference</i>, Voss · C5</p><p><i>Thinking in Bets</i>, Duke · C7</p></div>
 <div class="brand"><p class="rh">Strategy</p><p><i>Strategy Is Your Words</i>, Pollard · B3–B7</p><p><i>How Brands Grow</i>, Sharp · B8</p><p><i>The Long and the Short of It</i>, Binet &amp; Field · B8</p><p><i>Positioning</i>, Ries &amp; Trout · B4</p><p><i>Zag</i>, Neumeier · B4</p><p>Effie India, WARC and IPA cases · B9</p></div>
 <div class="cd"><p class="rh">Creative direction</p><p><i>Hey Whipple, Squeeze This</i>, Sullivan · A1–A5</p><p><i>A Technique for Producing Ideas</i>, Young · A1</p><p>Cannes Lions, D&amp;AD and One Show case films · A9</p></div>
</div>
<p class="fine">Titles are recommended from memory. Check editions and availability.</p>
""", label="Plan"))

# Templates
lines = lambda n: "".join('<span class="ln"></span>' for _ in range(n))
P.append(page(f"""
<h1 class="ph">Templates <em>to copy</em></h1>
<div class="tpl">
 <h3 class="sh">Decision journal: one per decision over ₹50,000 or longer than 3 months</h3>
 <div class="frm">
  <p><b>Date</b>{lines(1)}</p><p><b>Decision</b>{lines(1)}</p>
  <p><b>Options considered</b>{lines(2)}</p>
  <p><b>What I expect will happen</b>{lines(2)}</p>
  <p class="row3"><span><b>Confidence</b> ____ %</span><span><b>One-way or two-way door?</b></span><span><b>Review on</b> ________</span></p>
  <p><b>What actually happened</b>{lines(2)}</p>
  <p><b>Rule learned</b>{lines(1)}</p>
 </div>
</div>
<div class="tpl">
 <h3 class="sh">Pre-mortem: “It’s 12 months later and this failed. Why?”</h3>
 <div class="frm">
  <p><b>The bet</b>{lines(1)}</p>
  <p><b>Ten reasons it failed</b>{lines(6)}</p>
  <p><b>Top 3, ranked by likelihood × damage</b>{lines(2)}</p>
  <p><b>Cheapest test of the riskiest assumption</b>{lines(1)}</p>
 </div>
</div>
""", label="Tools"))

P.append(page(f"""
<div class="tpl">
 <h3 class="sh">Monthly money review: first Monday, one hour</h3>
 <table class="mr">
  <tr><td>Revenue this month</td><td></td><td>Cash in bank</td><td></td></tr>
  <tr><td>Direct costs</td><td></td><td>Owed to me (total)</td><td></td></tr>
  <tr><td>Gross margin %</td><td></td><td>Oldest unpaid invoice (days)</td><td></td></tr>
  <tr><td>Fixed costs + my salary</td><td></td><td>Committed costs, next 3 months</td><td></td></tr>
  <tr><td>Profit</td><td></td><td>Runway (months)</td><td></td></tr>
  <tr><td>Top client share %</td><td></td><td>Tax &amp; GST account balance</td><td></td></tr>
 </table>
 <p class="frm-q"><b>One thing to change next month</b>{lines(1)}</p>
</div>
<div class="tpl">
 <h3 class="sh">Quarterly scorecard: rate 1–5</h3>
 <table class="sc">
  <tr><th>Skill</th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th></tr>
  <tr><td>I know my monthly numbers from memory</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Receivables under one month of revenue</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Price set on value; walk-away number defined</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Top client under 40% of revenue</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I write a one-page brief a stranger can use</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I build brand platforms from real research</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I state the idea in one sentence before visuals</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>I present problem → insight → idea → execution</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Decision journal kept and reviewed monthly</td><td></td><td></td><td></td><td></td></tr>
  <tr class="key"><td>Case studies with numbers (count)</td><td></td><td></td><td></td><td></td></tr>
 </table>
 <p class="fine">The last row matters most. Clients, partners and your own confidence all rest on it.</p>
</div>
""", label="Tools"))

# ---------------------------------------------------------------- css + doc
CSS = (pathlib.Path(__file__).parent / "style.css").read_text()
doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The Operator's Curriculum</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,200;1,300&display=block" rel="stylesheet">
<style>{CSS}</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter></svg>
{''.join(P)}
</body></html>"""
OUT.write_text(doc)
print("pages:", page_no[0])
