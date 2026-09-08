const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Sandra Vermaak";
pres.title = "Managing Financial Performance Across Repairs & Maintenance";

// ---- palette ----
const DARK   = "13453B"; // deep green, dominant
const MID    = "2E7D68"; // mid teal-green
const GOLD   = "C8892F"; // sharp accent
const PALE   = "F1F5F3"; // card tint
const INK    = "16211E";
const BODY   = "33423D";
const MUTED  = "6E7D78";
const WHITE  = "FFFFFF";

const HEAD = "Cambria";
const SANS = "Calibri";

const M = 0.6;              // side margin
const W = 13.333 - M * 2;   // 12.133 content width

// ---------- helpers ----------
function footer(slide, n) {
  slide.addText("Sandra Vermaak  ·  Codi Group  ·  Finance Business Partner interview", {
    x: M, y: 6.95, w: 9, h: 0.3, align: "left", isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 9, color: MUTED,
  });
  slide.addText(String(n), {
    x: 12.25, y: 6.95, w: 0.5, h: 0.3, align: "right", isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 9, color: MUTED,
  });
}

function title(slide, text, kicker) {
  if (kicker) {
    slide.addText(kicker.toUpperCase(), {
      x: M, y: 0.42, w: W, h: 0.26, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 10, bold: true, color: GOLD, charSpacing: 2.2,
    });
  }
  slide.addText(text, {
    x: M, y: kicker ? 0.72 : 0.5, w: W, h: 0.62, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 30, bold: true, color: DARK,
  });
}

function numCircle(slide, x, y, label, fill) {
  slide.addShape(pres.ShapeType.ellipse, {
    x, y, w: 0.46, h: 0.46, fill: { color: fill || DARK },
  });
  slide.addText(label, {
    x, y, w: 0.46, h: 0.46, align: "center", valign: "middle", isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 12, bold: true, color: WHITE,
  });
}

function card(slide, x, y, w, h, fill) {
  slide.addShape(pres.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: fill || PALE }, line: { color: fill || PALE, width: 0 },
  });
}

// =====================================================================
// SLIDE 1 — title (dark)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: DARK };

  s.addText("CODI GROUP  ·  INTERVIEW PRESENTATION", {
    x: M, y: 0.6, w: W, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 11, bold: true, color: "8FBFAE", charSpacing: 2.4,
  });

  s.addText("Managing Financial Performance\nAcross Repairs & Maintenance", {
    x: M, y: 2.0, w: 11.6, h: 1.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 40, bold: true, color: WHITE, lineSpacing: 46,
  });

  s.addText("Size it.  Explain it.  Own it together.  Protect the home.", {
    x: M, y: 4.15, w: 11.6, h: 0.45, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 17, italic: true, color: GOLD,
  });

  s.addShape(pres.ShapeType.line, {
    x: M, y: 5.35, w: 3.0, h: 0, line: { color: "2E7D68", width: 1.5 },
  });

  s.addText("Sandra Vermaak", {
    x: M, y: 5.6, w: 6, h: 0.34, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 15, bold: true, color: WHITE,
  });
  s.addText("Candidate  ·  Finance Business Partner, Repairs & Maintenance  ·  September 2026", {
    x: M, y: 5.98, w: 9, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 11.5, color: "8FBFAE",
  });

  s.addNotes(
`PACE 0:45  ·  Seven slides, ten minutes.

Thank you. Ten minutes, five questions, one thread: a hundred-million-pound budget under pressure is a decision problem, not a reporting problem. My job is to get people arguing about the decision, not about whose number is right.

I'll cover scoping the number, the three hypotheses I'd arrive with, rebuilding the forecast with budget holders, what I'd do about it, how I'd escalate, and what I'd measure.

One caveat. This is my recommended approach, not a claim about how Codi works today. Figures are either published or clearly illustrative, and I'll say which.`);
}

// =====================================================================
// SLIDE 2 — scope the number
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Scope the number before you explain it", "01  ·  Investigate");

  // left stat block
  card(s, M, 1.75, 4.5, 2.35, DARK);
  s.addText("£4,000", {
    x: M + 0.35, y: 2.0, w: 3.8, h: 0.95, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 46, bold: true, color: WHITE,
  });
  s.addText("per home, per year", {
    x: M + 0.35, y: 2.95, w: 3.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 13, color: "9CC7B8",
  });
  s.addText("c.£100m across c.25,000 homes", {
    x: M + 0.35, y: 3.42, w: 3.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 11.5, italic: true, color: "8FBFAE",
  });

  s.addText(
    "At that level this is not a responsive repairs budget. It spans several services with different cost behaviours — and it straddles the revenue and capital boundary.",
    { x: M, y: 4.3, w: 4.5, h: 1.0, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 13, color: BODY, lineSpacing: 19 });

  card(s, M, 5.4, 4.5, 1.28, PALE);
  s.addText(
    [{ text: "First question I'd ask.  ", options: { bold: true, color: DARK } },
     { text: "Where is the revenue/capital line drawn — and is it applied the same way across both legacy policies?", options: { color: BODY } }],
    { x: M + 0.28, y: 5.4, w: 3.94, h: 1.28, valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 12, lineSpacing: 17 });

  // right: composition rows
  const rows = [
    ["Responsive repairs & voids", "Demand-led, volatile, hardest to forecast", "Revenue"],
    ["Cyclical & compliance", "Servicing and the big six — protected spend", "Revenue"],
    ["Planned & major works", "Component replacement, WHQS, retrofit", "Largely capital"],
  ];
  let y = 1.75;
  rows.forEach(([h1, h2, tag]) => {
    card(s, 5.5, y, 7.23, 1.12);
    s.addText(h1, {
      x: 5.8, y: y + 0.16, w: 4.6, h: 0.32, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 14, bold: true, color: INK,
    });
    s.addText(h2, {
      x: 5.8, y: y + 0.52, w: 5.2, h: 0.4, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 11.5, color: MUTED,
    });
    s.addText(tag, {
      x: 10.9, y: y + 0.16, w: 1.6, h: 0.3, align: "right", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 10.5, bold: true, color: tag === "Largely capital" ? GOLD : MID,
    });
    y += 1.28;
  });

  s.addText(
    [{ text: "One budget, three very different cost behaviours. ", options: { bold: true, color: INK } },
     { text: "You cannot forecast the total — you forecast the drivers underneath it.", options: { color: BODY } }],
    { x: 5.5, y: 5.65, w: 7.23, h: 0.45, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13.5 });

  s.addText("Illustrative categories, to show how I would cut the budget — not Codi's actual structure.", {
    x: 5.5, y: 6.2, w: 7.23, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 10, italic: true, color: MUTED,
  });

  s.addNotes(
`PACE 1:20  ·  Running total 2:05.

Before explaining a variance I'd want to know what sits inside the number. A hundred million across roughly twenty-five thousand homes is about four thousand pounds per home, which is well above a pure responsive repairs budget. So it must span responsive and voids, cyclical and compliance, and planned or major works including WHQS and retrofit.

That matters twice. First, these behave differently: responsive is demand-led and volatile, compliance is effectively fixed, planned work is programme-driven. Averaging them hides the story. Second, they sit on different sides of the revenue and capital boundary, and only the revenue side hits operating surplus.

So my first question would be where that line is drawn and how consistently it is applied, particularly post-merger where two legacy capitalisation policies may still be in use. Reclassifying spend is not a saving, and I'd want to be sure no part of the position depends on it.

[Source] Homes figure from public reporting on the merger. The £100m is the interview scenario. Category split is illustrative.`);
  footer(s, 2);
}

// =====================================================================
// SLIDE 3 — three hypotheses
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Three hypotheses I would arrive with", "01  ·  Investigate");

  s.addText("Each is a question with a data test attached — not a conclusion.", {
    x: M, y: 1.42, w: W, h: 0.32, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 13.5, italic: true, color: MID,
  });

  const hyps = [
    ["01", "Delivery mix", "Pobl expanded its in-house trades team by c.50% — 34 roles — in 2024, alongside an 11-lot framework for responsive repairs, voids and out-of-hours.",
     "Has external spend stepped down in proportion to the capacity we insourced, or are we carrying both?"],
    ["02", "Regulation", "WHQS hazard response took effect 1 April 2026: investigate and remedy within 24 hours each where harm is imminent; 10 then 5 working days otherwise.",
     "What has that done to job volume, out-of-hours and premium call-off, and to how densely we can schedule?"],
    ["03", "Price", "Sector surveys put expected responsive repairs cost increases at c.23% this year, against c.10% in the regulator's global accounts.",
     "On like-for-like jobs, how much of our movement is rate and materials rather than volume?"],
  ];

  const cw = (W - 0.7) / 3;
  hyps.forEach(([n, head, evidence, test], i) => {
    const x = M + i * (cw + 0.35);
    card(s, x, 2.0, cw, 4.15);
    numCircle(s, x + 0.3, 2.28, n, i === 1 ? GOLD : DARK);
    s.addText(head, {
      x: x + 0.3, y: 2.88, w: cw - 0.6, h: 0.36, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 19, bold: true, color: DARK,
    });
    s.addText(evidence, {
      x: x + 0.3, y: 3.32, w: cw - 0.6, h: 1.55, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 12, color: BODY, lineSpacing: 17,
    });
    s.addText("THE TEST", {
      x: x + 0.3, y: 4.92, w: cw - 0.6, h: 0.24, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 9, bold: true, color: GOLD, charSpacing: 1.8,
    });
    s.addText(test, {
      x: x + 0.3, y: 5.18, w: cw - 0.6, h: 0.85, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 11.5, italic: true, color: INK, lineSpacing: 16,
    });
  });

  s.addText("Sources: Codi/Pobl published announcements and tender notices; Welsh Government WHQS hazard-response statement; UK sector cost surveys.", {
    x: M, y: 6.32, w: W, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 9.5, italic: true, color: MUTED,
  });

  s.addNotes(
`PACE 2:05  ·  Running total 4:10.

I wouldn't arrive with an open mind and no shape. I'd bring three hypotheses and the data to kill or confirm each quickly.

First, delivery mix. Publicly, Pobl expanded its in-house trades team by about fifty per cent in 2024, thirty-four roles, while running an eleven-lot framework for responsive repairs, voids and out-of-hours to support the internal team. Sensible model, but it is exactly where double-running appears. The test: has contractor spend fallen in proportion to the capacity brought in-house, or are we paying for both? I'd compare contractor call-off value per month against internal jobs completed and operative hours.

Second, regulation. The WHQS hazard response requirements took effect on the first of April this year. Where harm is judged imminent you investigate within twenty-four hours and remedy within a further twenty-four; otherwise ten working days, then five. Compressed timescales push work out of hours and into premium call-off, and make it harder to batch jobs, so cost per job rises even when volume doesn't. Response times also have to be published and reported, so this is not a place to look for savings.

Third, price. Sector surveys put expected responsive repairs increases around twenty-three per cent this year, well ahead of the ten per cent implied by the regulator's global accounts. That is UK-wide and indicative rather than Welsh, but it tells me to separate rate from volume before concluding anything about efficiency.

If I'm wrong on all three I've still narrowed the search quickly. I'd rather be corrected in week one than confirm a number in month six.

[Source] Pobl in-house trades announcement (2024); Pobl responsive repairs and voids framework notice, 11 lots (Dec 2023); Welsh Government WHQS responding-to-hazards statement (Dec 2025), in force 1 April 2026; UK repairs cost survey commentary. Context, not claims about Codi's position.`);
  footer(s, 3);
}

// =====================================================================
// SLIDE 4 — rebuild the forecast
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Rebuild the forecast with the people who own it", "02  ·  Forecast");

  card(s, M, 1.72, W, 0.78, DARK);
  s.addText("Actuals  +  committed cost  +  ( remaining demand  ×  evidenced unit cost )  =  year-end position", {
    x: M, y: 1.72, w: W, h: 0.78, align: "center", valign: "middle", isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 16, bold: true, color: WHITE,
  });

  const cols = [
    ["01", "Agree the assumptions", ["Demand, backlog and seasonality", "Capacity and productivity", "Work mix and complexity", "Contract rates and variations"]],
    ["02", "Cost the work honestly", ["Open jobs and commitments once, not twice", "Evidenced cost per job by type", "Realistic delivery dates for planned work", "Base case and a downside"]],
    ["03", "Make it theirs", ["A named owner for every material assumption", "Confidence level recorded, not implied", "Monthly sign-off with the service lead", "Quantify disagreement rather than settle it"]],
  ];

  const cw = (W - 0.7) / 3;
  cols.forEach(([n, head, items], i) => {
    const x = M + i * (cw + 0.35);
    numCircle(s, x, 2.82, n, DARK);
    s.addText(head, {
      x: x + 0.62, y: 2.86, w: cw - 0.62, h: 0.4, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 17, bold: true, color: DARK,
    });
    s.addText(items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== items.length - 1 } })), {
      x: x + 0.04, y: 3.45, w: cw - 0.1, h: 1.85, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 12, color: BODY, paraSpaceAfter: 7, lineSpacing: 16,
    });
  });

  card(s, M, 5.55, W, 0.95, PALE);
  s.addText(
    [{ text: "Show the delivery forecast before mitigation. ", options: { bold: true, color: DARK } },
     { text: "Only owned, time-phased, achievable actions come off it — everything else is listed as an opportunity. A savings target is not a forecast.", options: { color: BODY } }],
    { x: M + 0.35, y: 5.55, w: W - 0.7, h: 0.95, valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13.5, lineSpacing: 19 });

  s.addNotes(
`PACE 1:35  ·  Running total 5:45.

The forecast has to be built with budget holders, not sent to them. My role is structure and challenge; theirs is demand, capacity and programme. If they haven't shaped it they won't defend it, and a forecast nobody defends gets ignored.

Mechanically it is actuals, plus committed cost, plus remaining demand times an evidenced unit cost. For responsive work that means remaining jobs by type against a cost per job reflecting the current mix, allowing for seasonality and backlog. For planned work, remaining quantities at contract rates against realistic dates. I'd reconcile open commitments carefully so nothing is counted twice, which is the most common error I see.

I'd record the owner and confidence level of every material assumption, and run a base case and a downside, such as sustained contractor reliance or a harder winter. The point is to show the range and identify which two or three assumptions actually move the answer.

One discipline I'd hold firmly. The delivery forecast stays visible before mitigation. Only owned, time-phased, achievable actions come off it; anything less certain is shown separately as an opportunity. A savings target is not a forecast, and the moment those blend the number stops being useful.`);
  footer(s, 4);
}

// =====================================================================
// SLIDE 5 — act
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Act in order: protect first, then choose", "03  ·  Manage the risk");

  const acts = [
    ["01", "Protect", "Safety, compliance and WHQS hazard response times.", "Now published and reported. Not a place to save.", DARK],
    ["02", "Convert existing capacity", "Productivity, first-time fix and scheduling density across the in-house team.", "The cheapest saving is the one you have already paid for.", MID],
    ["03", "Challenge external spend", "Call-off discipline, variation validation, rates tested on like-for-like work.", "Only counts if it reduces paid hours or contractor spend.", MID],
    ["04", "Rephase selectively", "Discretionary planned work only, with asset and service leads.", "Last resort — and never quietly.", GOLD],
  ];

  let y = 1.78;
  acts.forEach(([n, head, detail, note, col]) => {
    numCircle(s, M, y + 0.16, n, col);
    s.addText(head, {
      x: M + 0.62, y: y + 0.02, w: 3.5, h: 0.34, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 17, bold: true, color: DARK,
    });
    s.addText(detail, {
      x: M + 0.62, y: y + 0.4, w: 5.5, h: 0.42, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 12, color: BODY,
    });
    s.addText(note, {
      x: 7.5, y: y + 0.16, w: 5.23, h: 0.4, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 12, italic: true, color: col === GOLD ? GOLD : MID,
    });
    y += 1.02;
  });

  card(s, M, 5.92, W, 0.8, "FBF3E6");
  s.addText(
    [{ text: "Watch the second-order effect.  ", options: { bold: true, color: "8A5A12" } },
     { text: "Deferring planned work usually raises responsive cost later and shifts capitalised spend into revenue — that hits operating surplus, not just timing.", options: { color: "6B4A18" } }],
    { x: M + 0.35, y: 5.92, w: W - 0.7, h: 0.8, valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13, lineSpacing: 18 });

  s.addNotes(
`PACE 1:35  ·  Running total 7:20.

I'd work the actions in a deliberate order, because the order is the argument.

First, protect. Urgent, safety-critical and compliance work is ring-fenced, and I'd put WHQS hazard response in that category. Those response times are published and reported, so slowing them is not a saving; it is a regulatory and human risk that comes back as disrepair cost.

Second, convert capacity we have already bought. If the in-house team has grown, the cheapest saving is making it productive: better diagnosis, right trade first time, materials on the van, appointments that hold. But I'd only call it a cash saving if it reduces paid hours or displaces contractor spend. Otherwise it is released capacity or avoided future cost, and I'd report it as exactly that.

Third, challenge external spend with procurement: call-off discipline, validating variations, testing rates on genuinely comparable work.

Fourth, and only then, rephasing discretionary planned work with asset and service leads.

And I'd be explicit about the second-order effect. Deferring planned work tends to increase responsive demand later, and moves spend that would have been capitalised into revenue. That lands on operating surplus, not just between years. Every action needs an owner, a date, a cost and an evidenced benefit.`);
  footer(s, 5);
}

// =====================================================================
// SLIDE 6 — escalate
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Escalate early, in balance-sheet terms", "04  ·  Communicate");

  // bridge
  const steps = ["Approved\nbudget", "Delivery\nforecast", "Owned\nmitigations", "Residual gap\n+ downside"];
  const bw = 2.75, gap = 0.38;
  steps.forEach((t, i) => {
    const x = M + i * (bw + gap);
    card(s, x, 1.72, bw, 1.15, i === 3 ? DARK : PALE);
    s.addText(t, {
      x, y: 1.72, w: bw, h: 1.15, align: "center", valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13.5, bold: true, color: i === 3 ? WHITE : DARK, lineSpacing: 17,
    });
    if (i < 3) {
      s.addText("→", {
        x: x + bw, y: 1.72, w: gap, h: 1.15, align: "center", valign: "middle", isTextBox: true, margin: 0,
        fontFace: SANS, fontSize: 16, bold: true, color: MID,
      });
    }
  });

  s.addText("Why an R&M variance is not just a cost variance at Codi", {
    x: M, y: 3.2, w: W, h: 0.36, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 14, bold: true, color: DARK,
  });

  const ctx = [
    ["Viability graded Yellow", "The July 2026 regulatory judgement retained the governance grade and identified the effect of the development and planned maintenance programme on financial metrics."],
    ["£130m sustainability-linked facility", "Margin is tied to environmental and social targets. Retrofit and planned works delivery therefore carries a cost-of-debt consequence, not only a cost consequence."],
  ];
  let y = 3.65;
  ctx.forEach(([h, d]) => {
    card(s, M, y, W, 1.05);
    s.addText(h, {
      x: M + 0.35, y: y + 0.14, w: 4.3, h: 0.32, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13, bold: true, color: GOLD,
    });
    s.addText(d, {
      x: M + 0.35, y: y + 0.48, w: W - 0.7, h: 0.48, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 11.5, color: BODY,
    });
    y += 1.2;
  });

  s.addText(
    [{ text: "So the escalation says: ", options: { color: BODY } },
     { text: "here is the gap, here is what I recommend, here is the alternative, and here is what happens if we do nothing.", options: { bold: true, color: INK } }],
    { x: M, y: 6.15, w: W, h: 0.45, isTextBox: true, margin: 0, fontFace: SANS, fontSize: 13.5 });

  s.addNotes(
`PACE 1:25  ·  Running total 8:45.

I'd tell senior leaders as soon as there is a credible indication of material exposure, separating what is known from what is still being validated. I wouldn't wait for a clean month-end pack, because the value of the information falls faster than its accuracy improves.

The report is a bridge: approved budget, to delivery forecast, to owned mitigations, to the residual gap with a downside and the movement since last time. One page, with the decision required, my recommendation, the alternative, and the consequence of doing nothing.

What I wouldn't do is present it as purely a cost variance, because here it isn't. The July regulatory judgement rated financial viability Yellow while retaining the governance grade, and identified the effect of development and planned maintenance on financial metrics. Separately, the group has a hundred and thirty million pound sustainability-linked facility where the margin is tied to environmental and social targets, so retrofit and planned works delivery carries a cost-of-debt consequence too.

Put those together and a repairs overspend touches operating surplus, interest cover and potentially the cost of borrowing. That is the frame I'd use, and why I'd want treasury in the conversation early.

[Source] Codi Group regulatory judgement, published July 2026; reporting on Codi's £130m sustainability-linked facility.`);
  footer(s, 6);
}

// =====================================================================
// SLIDE 7 — measure (dark close)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: DARK };

  s.addText("05  ·  MEASURE", {
    x: M, y: 0.55, w: W, h: 0.26, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 10, bold: true, color: GOLD, charSpacing: 2.2,
  });
  s.addText("Measure the money and the home", {
    x: M, y: 0.85, w: W, h: 0.62, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 30, bold: true, color: WHITE,
  });
  s.addText("A short set, each with a definition, a baseline, an owner and a trigger.", {
    x: M, y: 1.5, w: W, h: 0.32, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 13.5, italic: true, color: "9CC7B8",
  });

  const groups = [
    ["Financial", ["Forecast gap, and movement since last forecast", "Net benefit delivered against the agreed action profile", "Share of spend capitalised versus revenue", "Cost per job, adjusted for work mix"]],
    ["Service and resident", ["WHQS hazard response compliance", "First-time fix and repeat visits", "Jobs per operative — is insourced capacity landing?", "Backlog age and overdue safety work", "Satisfaction and repeat contact"]],
  ];
  groups.forEach(([head, items], i) => {
    const x = M + i * 6.25;
    s.addText(head.toUpperCase(), {
      x, y: 2.15, w: 5.7, h: 0.3, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 11, bold: true, color: GOLD, charSpacing: 1.8,
    });
    s.addText(items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== items.length - 1 } })), {
      x: x + 0.04, y: 2.58, w: 5.66, h: 2.6, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 13, color: "DCEAE4", paraSpaceAfter: 9, lineSpacing: 18,
    });
  });

  s.addShape(pres.ShapeType.line, {
    x: M, y: 4.62, w: W, h: 0, line: { color: "2E7D68", width: 1 },
  });

  s.addText("Weekly operational exception review. Monthly signed-off financial position. Safety escalates immediately.", {
    x: M, y: 4.8, w: W, h: 0.32, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 12.5, color: "9CC7B8",
  });

  s.addText("What success looks like: a number the operation recognises, a forecast that stops moving, and a resident who does not have to ring twice.", {
    x: M, y: 5.5, w: 11.9, h: 1.1, valign: "top", isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 21, bold: true, italic: true, color: WHITE, lineSpacing: 30,
  });

  s.addNotes(
`PACE 1:05  ·  Running total 9:50.

Finally, measurement. A short set agreed with the teams, each with a definition, a baseline, an owner and an escalation trigger. The test of a dashboard is whether it changes what someone does on Monday.

Financially: the forecast gap and its movement, net benefit delivered against profile, the capitalised versus revenue split, and cost per job adjusted for mix. That adjustment matters, because an average cost can fall simply because the team completed easier jobs, and I wouldn't let that be reported as efficiency.

On service: WHQS hazard response compliance, first-time fix, jobs per operative to show whether insourced capacity is landing, backlog age and overdue safety work, and satisfaction or repeat contact. Those are the early warning that a saving is coming out of the resident rather than out of the cost.

A number the operation recognises, a forecast that stops moving, and a resident who does not have to ring twice. Thank you, and I'm happy to take questions.`);
  footer(s, 7);
}

pres.writeFile({ fileName: "/home/user/rugby-rwc-2027/briefings/Codi_Presentation_Sandra_Vermaak.pptx" })
  .then(f => console.log("written:", f));
