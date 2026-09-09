const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Sandra Vermaak";
pres.title = "Managing Financial Performance Across Repairs & Maintenance";

// ---- palette ----
const DARK   = "13453B";
const MID    = "2E7D68";
const GOLD   = "C8892F";
const PALE   = "F1F5F3";
const INK    = "16211E";
const BODY   = "33423D";
const MUTED  = "6E7D78";
const WHITE  = "FFFFFF";

const HEAD = "Cambria";
const SANS = "Calibri";

const M = 0.6;
const W = 13.333 - M * 2;

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
// SLIDE 1 — title
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: DARK };

  s.addText("CODI GROUP  ·  INTERVIEW PRESENTATION", {
    x: M, y: 0.6, w: W, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 11, bold: true, color: "8FBFAE", charSpacing: 2.4,
  });

  s.addText("Managing Financial Performance\nAcross Repairs & Maintenance", {
    x: M, y: 2.4, w: 11.6, h: 1.9, isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 40, bold: true, color: WHITE, lineSpacing: 46,
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

Thank you for seeing me. I've got ten minutes, so I'll take your five questions in order: how I'd work out what's driving the overspend, how I'd rebuild the forecast with the budget holders, what I'd actually do about it, how I'd tell senior leaders, and what I'd track afterwards.

One thing up front. I don't know your systems or your numbers yet, so this is how I'd approach it rather than a view on how things work here. Where I've used a figure it's illustrative, and I'll say so.`);
  footer(s, 1);
}

// =====================================================================
// SLIDE 2 — scope the number  (Sandra's edits, spacing corrected)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Scope the number", "01  ·  Investigate");

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
    "At that level this is not only a responsive repairs budget. It spans several services with different cost behaviours — and it straddles both Revenue (operational expenditure) and Capital.",
    { x: M, y: 4.3, w: 4.5, h: 1.3, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 13, color: BODY, lineSpacing: 19 });

  const rows = [
    ["Responsive / reactive repairs", "Demand-led, volatile, difficult to forecast", "Revenue"],
    ["Cyclical", "Servicing, decoration – predictable", "Revenue"],
    ["Compliance", "Non-negotiable spend", "Revenue"],
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

  s.addNotes(
`PACE 1:20  ·  Running total 2:05.

Before I can explain a variance I need to know what is actually in the budget. A hundred million across about twenty-five thousand homes is roughly four thousand pounds a home. That is more than responsive repairs alone would cost, so the budget must also be carrying cyclical work, compliance and planned or major works.

That matters for two reasons. These things behave differently. Responsive is demand-led and hard to predict, compliance is effectively fixed, planned work is programme-driven. An average across all of them hides what is going on. And they sit on different sides of the revenue and capital line, and only the revenue side hits the surplus.

So the first thing I would do is agree with the team exactly what sits in the number, and where that line is drawn. Reclassifying spend is not a saving, and I would want to be sure that none of the reported position depends on it.

[Note] The £100m is the scenario you gave me; the per-home figure is my own arithmetic. The categories are illustrative.`);
  footer(s, 2);
}

// =====================================================================
// SLIDE 3 — where an overspend comes from  (general method)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Where an overspend usually comes from", "01  ·  Investigate");

  s.addText("First check it is real — phasing, accruals and coding. Then split the variance three ways.", {
    x: M, y: 1.42, w: W, h: 0.32, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 13.5, italic: true, color: MID,
  });

  const cols = [
    ["01", "Volume", "We are doing more jobs than the budget assumed.",
     "Job numbers by type against budget and last year. Backlog, seasonality, and any change in demand."],
    ["02", "Price", "Each job is costing more than we assumed.",
     "Cost per job on like-for-like work. Labour and material rates, and the split between in-house and contractor."],
    ["03", "Mix", "The work is different, or harder, than planned.",
     "Job types and complexity. Emergency against planned. Which properties or areas are driving it."],
  ];

  const cw = (W - 0.7) / 3;
  cols.forEach(([n, head, what, look], i) => {
    const x = M + i * (cw + 0.35);
    card(s, x, 2.0, cw, 3.95);
    numCircle(s, x + 0.3, 2.28, n, i === 1 ? GOLD : DARK);
    s.addText(head, {
      x: x + 0.3, y: 2.88, w: cw - 0.6, h: 0.36, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 19, bold: true, color: DARK,
    });
    s.addText(what, {
      x: x + 0.3, y: 3.32, w: cw - 0.6, h: 1.1, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 12.5, color: BODY, lineSpacing: 18,
    });
    s.addText("WHAT I'D LOOK AT", {
      x: x + 0.3, y: 4.22, w: cw - 0.6, h: 0.24, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 9, bold: true, color: GOLD, charSpacing: 1.8,
    });
    s.addText(look, {
      x: x + 0.3, y: 4.5, w: cw - 0.6, h: 1.1, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 11.5, color: INK, lineSpacing: 16,
    });
  });

  s.addText("Then I'd walk through real jobs with supervisors and planners, so the financial explanation matches what is happening on the ground.", {
    x: M, y: 6.15, w: W, h: 0.3, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 11, italic: true, color: MUTED,
  });

  s.addNotes(
`PACE 2:05  ·  Running total 4:10.

Before deciding anything I would want to know what is actually driving it, and I would work through it in a set order.

First, is it real? A lot of apparent overspends turn out to be timing. Work done but not yet invoiced, accruals in the wrong period, jobs coded to the wrong budget, or a programme simply running ahead of its phasing. I would rule that out before raising an alarm, because getting that wrong once costs you credibility for the rest of the year.

Once I am satisfied it is real, I would split it three ways. Volume: are we doing more jobs than we planned for? Price: is each job costing more than we assumed, and is that labour, materials, or more work going to contractors? Mix: is the work different — more emergencies, more complex jobs, or particular property types and areas driving it?

That split matters because each one leads somewhere different. A volume problem is a demand and capacity conversation. A price problem is a procurement and rates conversation. A mix problem usually means the assumptions in the budget were wrong, and that affects next year as well as this one.

And I would not do this from a spreadsheet on its own. I would go through real jobs with the supervisors and planners, so that whatever I end up telling the board matches what is actually happening on the ground.`);
  footer(s, 3);
}

// =====================================================================
// SLIDE 4 — rebuild the forecast  (Sandra's FYF retained)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Rebuild the forecast with the people who own it", "02  ·  Forecast");

  card(s, M, 1.72, W, 0.78, DARK);
  s.addText("Actuals  +  committed cost  +  ( remaining demand  ×  evidenced unit cost )  =  FYF", {
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
      x: x + 0.04, y: 3.45, w: cw - 0.1, h: 1.85, valign: "top", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 12, color: BODY, paraSpaceAfter: 7, lineSpacing: 16,
    });
  });

  card(s, M, 5.55, W, 0.95, PALE);
  s.addText(
    [{ text: "Show the forecast before mitigation. ", options: { bold: true, color: DARK } },
     { text: "Only owned, dated, achievable actions come off it — everything else is listed as an opportunity. A savings target is not a forecast.", options: { color: BODY } }],
    { x: M + 0.35, y: 5.55, w: W - 0.7, h: 0.95, valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13.5, lineSpacing: 19 });

  s.addNotes(
`PACE 1:35  ·  Running total 5:45.

The forecast has to be built with the budget holders, not sent to them. I bring the structure and the challenge; they own the assumptions about demand, capacity and what they can realistically deliver. If they have not helped shape it they will not stand behind it, and a forecast nobody stands behind gets ignored.

The mechanics are actuals, plus what we are already committed to, plus the remaining work at a realistic cost per job. For responsive that is expected job numbers by type against an evidenced unit cost, allowing for seasonality and backlog. For planned work it is what is left at contract rates, against dates the team actually believes. I would be careful with open commitments so nothing is counted twice — that is the easiest mistake to make.

I would write down who owns each significant assumption and how confident they are, and run a downside as well as a base case, so we can see the range and which two or three things really move the answer.

One thing I would hold firmly. Show the forecast before mitigation. Only actions that are owned, dated and realistic come off it, and everything else is listed separately as an opportunity. A savings target is not a forecast.`);
  footer(s, 4);
}

// =====================================================================
// SLIDE 5 — act in order
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Act in order: protect first, then choose", "03  ·  Manage the risk");

  const acts = [
    ["01", "Protect", "Safety, compliance and statutory response times.", "Not a place to look for savings.", DARK],
    ["02", "Use the capacity we have", "Productivity, first-time fix and scheduling across the in-house team.", "The cheapest saving is one you have already paid for.", MID],
    ["03", "Challenge external spend", "Call-off discipline, checking variations, rates on like-for-like work.", "Only counts if it reduces hours or contractor spend.", MID],
    ["04", "Rephase selectively", "Discretionary planned work only, with asset and service leads.", "Last resort — and never quietly.", GOLD],
  ];

  let y = 1.78;
  acts.forEach(([n, head, detail, note, col]) => {
    numCircle(s, M, y + 0.16, n, col);
    s.addText(head, {
      x: M + 0.62, y: y + 0.02, w: 3.6, h: 0.34, isTextBox: true, margin: 0,
      fontFace: HEAD, fontSize: 17, bold: true, color: DARK,
    });
    s.addText(detail, {
      x: M + 0.62, y: y + 0.4, w: 5.6, h: 0.42, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 12, color: BODY,
    });
    s.addText(note, {
      x: 7.5, y: y + 0.16, w: 5.23, h: 0.4, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 12, italic: true, color: col === GOLD ? GOLD : MID,
    });
    y += 1.02;
  });

  card(s, M, 5.92, W, 0.8, "FBF3E6");
  s.addText(
    [{ text: "Watch the knock-on effect.  ", options: { bold: true, color: "8A5A12" } },
     { text: "Deferring planned work usually pushes up responsive costs later, and moves spend that would have been capital into revenue — that hits the surplus, not just the timing.", options: { color: "6B4A18" } }],
    { x: M + 0.35, y: 5.92, w: W - 0.7, h: 0.8, valign: "middle", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13, lineSpacing: 18 });

  s.addNotes(
`PACE 1:35  ·  Running total 7:20.

I would work through the options in a deliberate order.

First, protect. Safety, compliance and statutory response times are ring-fenced. Slowing those down is not a saving. It comes back as disrepair cost, and it is the wrong thing to do to somebody living in the home.

Second, get more out of the capacity we already have. Where there are in-house teams, the cheapest saving available is making them more productive: the right diagnosis, the right trade first time, materials on the van, appointments that stick. But I would only call that a cash saving if it actually reduces paid hours or takes work off a contractor. If it does not, it is spare capacity or cost avoided later, and I would report it that way.

Third, external spend. Working with procurement on call-off discipline, checking variations are valid, and testing rates on genuinely comparable work.

Fourth, and only then, rephasing discretionary planned work with the asset and service leads.

And I would be clear about the knock-on effect, because this is where in-year savings destroy value. Deferring planned work usually increases responsive demand later, and it moves spend that would have been capitalised into revenue, which hits the surplus rather than just moving between years. Every action needs an owner, a date, a cost to deliver it and a benefit we can evidence.`);
  footer(s, 5);
}

// =====================================================================
// SLIDE 6 — escalate  (generalised)
// =====================================================================
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  title(s, "Escalate early, and in the right terms", "04  ·  Communicate");

  const steps = ["Approved\nbudget", "Latest\nforecast", "Agreed\nmitigations", "Gap that\nremains"];
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

  s.addText("Why a repairs overspend is more than a budget variance", {
    x: M, y: 3.2, w: W, h: 0.36, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 14, bold: true, color: DARK,
  });

  const ctx = [
    ["It lands on the surplus", "Repairs is largely revenue spend, so an overspend comes off operating surplus — which feeds interest cover and covenant headroom. Finance leaders need it in those terms, not just as a variance."],
    ["It competes with the investment programme", "Money spent unplanned on reactive work is money not available for planned works and new homes. That is the trade-off leadership is actually being asked to make."],
  ];
  let y = 3.65;
  ctx.forEach(([h, d]) => {
    card(s, M, y, W, 1.05);
    s.addText(h, {
      x: M + 0.35, y: y + 0.14, w: 5.2, h: 0.32, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13, bold: true, color: GOLD,
    });
    s.addText(d, {
      x: M + 0.35, y: y + 0.48, w: W - 0.7, h: 0.48, isTextBox: true, margin: 0,
      valign: "top", fontFace: SANS, fontSize: 11.5, color: BODY,
    });
    y += 1.2;
  });

  s.addText(
    [{ text: "So the escalation says: ", options: { color: BODY } },
     { text: "here is the gap, here is what I recommend, here is the alternative, and here is what happens if we do nothing.", options: { bold: true, color: INK } }],
    { x: M, y: 6.15, w: W, h: 0.45, isTextBox: true, margin: 0, fontFace: SANS, fontSize: 13.5 });

  s.addNotes(
`PACE 1:25  ·  Running total 8:45.

I would tell senior leaders as soon as there is a credible sign of a material problem, and be clear about what I know as against what I am still checking. I would not wait for a tidy month-end pack, because the information loses value faster than it gains accuracy.

The report itself is a bridge. Approved budget, to the latest forecast, to the mitigations we have actually agreed, to the gap that is left, with a downside case and the movement since last time. One page. The decision I need, what I recommend, the alternative, and what happens if we do nothing.

What I would avoid is presenting it as just a budget variance. Repairs is mostly revenue spend, so an overspend comes straight off the operating surplus, and that feeds interest cover and covenant headroom. And in practical terms, money spent unplanned on reactive work is money that is not available for planned works or for new homes. That is the trade-off leadership is really being asked to make, so that is how I would frame it — and it is why I would want treasury and corporate finance in the conversation early rather than at the end.`);
  footer(s, 6);
}

// =====================================================================
// SLIDE 7 — measure
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
    ["Financial", ["The gap, and how it has moved since last time", "Whether agreed savings have actually landed", "Split between capital and revenue spend", "Cost per job, adjusted for the mix of work"]],
    ["Service and resident", ["Outstanding safety and compliance work", "First-time fix and repeat visits", "Jobs per operative", "Backlog, and how old it is", "Satisfaction and repeat contact"]],
  ];
  groups.forEach(([head, items], i) => {
    const x = M + i * 6.25;
    s.addText(head.toUpperCase(), {
      x, y: 2.15, w: 5.7, h: 0.3, isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 11, bold: true, color: GOLD, charSpacing: 1.8,
    });
    s.addText(items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j !== items.length - 1 } })), {
      x: x + 0.04, y: 2.58, w: 5.66, h: 2.6, valign: "top", isTextBox: true, margin: 0,
      fontFace: SANS, fontSize: 13, color: "DCEAE4", paraSpaceAfter: 9, lineSpacing: 18,
    });
  });

  s.addShape(pres.ShapeType.line, {
    x: M, y: 4.62, w: W, h: 0, line: { color: "2E7D68", width: 1 },
  });

  s.addText("Weekly look at exceptions with the operational team. Monthly signed-off position. Anything safety-related goes straight up.", {
    x: M, y: 4.8, w: W, h: 0.32, isTextBox: true, margin: 0,
    fontFace: SANS, fontSize: 12.5, color: "9CC7B8",
  });

  s.addText("What success looks like: a number the operation recognises, a forecast that stops moving, and a resident who does not have to ring twice.", {
    x: M, y: 5.5, w: 11.9, h: 1.1, valign: "top", isTextBox: true, margin: 0,
    fontFace: HEAD, fontSize: 21, bold: true, italic: true, color: WHITE, lineSpacing: 30,
  });

  s.addNotes(
`PACE 1:15  ·  Running total 10:00.

Last, measurement. I would agree a short set with the teams, each with a definition, a baseline, an owner and a point where we escalate. The test of a dashboard is whether it changes what somebody does on Monday morning.

On the money: the gap and how it has moved, whether the savings we agreed have actually landed, the capital and revenue split, and cost per job adjusted for the mix of work. That adjustment matters, because an average cost can fall simply because the team did easier jobs that month, and I would not let that be reported as efficiency.

On the service: outstanding safety and compliance work, first-time fix, jobs per operative, how old the backlog is, and repeat contact. Those tell you early if a saving is coming out of the resident rather than out of the cost.

What I would want a year in is a number the operation recognises as theirs, a forecast that stops moving, and a resident who does not have to ring twice. Thank you — happy to take questions.`);
  footer(s, 7);
}

pres.writeFile({ fileName: "/home/user/rugby-rwc-2027/briefings/Codi_Presentation_Sandra_Vermaak.pptx" })
  .then(f => console.log("written:", f));
