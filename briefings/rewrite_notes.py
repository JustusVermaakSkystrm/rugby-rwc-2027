#!/usr/bin/env python3
"""Rewrite the speaker notes so they match the current slides.

The notes had drifted: they still described the earlier structure. These follow
the slides as they now stand, in Sandra's register and using her own terms
(GL deep dive, PY, FYF, run rate, causal, scope creep, safety stock, buy-in).

Usage: rewrite_notes.py <in.pptx> <out.pptx>
"""
import sys

from pptx import Presentation

NOTES = {

1: """[45 sec · 0:45 elapsed]

Thank you for seeing me. I've got ten minutes, so I'll take your five questions in order: how I'd work out what's driving the overspend, how I'd rebuild the forecast with the budget holders, what I'd actually do about it, how I'd communicate it, and what I'd track afterwards.

One thing up front. I don't know your systems or your numbers yet, so this is how I'd approach it rather than a view on how things work here. Where I've used a figure it's illustrative, and I'll say so.""",

2: """[1 min 15 · 2:00 elapsed]

Before I can explain a variance I need to know what's actually in the number. A hundred million across roughly twenty-five thousand homes is about four thousand pounds a home. That's more than responsive repairs alone would cost, so the budget must also be carrying cyclical work, compliance, and planned and major works.

That matters for two reasons. They behave differently. Responsive is demand-led and hard to forecast, cyclical is predictable, compliance is non-negotiable, and planned work is programme-driven. An average across all four hides what's going on.

And they sit on different sides of the revenue and capital line. Only the revenue side hits the surplus.

So the first thing I'd do is agree with the team exactly what sits in the number, and where the threshold between a repair and capex is drawn. Reclassifying spend isn't a saving, and I'd want to be sure none of the reported position depends on it.

[Note] The £100m is the scenario you gave me. The per-home figure is my own arithmetic and the categories are illustrative.""",

3: """[2 min · 4:00 elapsed]

Before I decide anything I want to know what's actually driving it, and I'd work through it in order.

First, is it real? A lot of apparent overspends turn out to be something else. Coding errors, phasing, accruals, adjustments, or the way costs have been allocated. I'd do a GL deep dive before raising any alarm, because getting that wrong once costs you credibility for the rest of the year.

Then, is it a one-off or an emerging trend? I'd compare actuals to prior year as well as to forecast, and ask whether the forecast assumptions themselves have changed. A single bad month is a different conversation from a run rate that has moved.

Once I'm satisfied it's real and it's a trend, I'd split the variance three ways.

Volume. Are we simply doing more jobs than the budget assumed? Job numbers by type against budget and against last year, the backlog, seasonality, and anything that's changed in demand.

Price. Is each job costing more? Cost per job on like-for-like work, labour and material rates, and how much more is going to contractors rather than our own teams.

Mix. Is the work different, or more complicated? Job types and complexity, emergency against planned, and which properties or areas are driving it. Productivity sits here too, because the same job taking longer is a mix and productivity problem, not a price one.

Each of those leads somewhere different, which is why I wouldn't lump them together. And I wouldn't do it from a spreadsheet alone. I'd walk through real jobs with the operational team, so what I end up telling the board matches what's happening on the ground.""",

4: """[1 min 35 · 5:35 elapsed]

The forecast has to be built with the people who own the budget, not sent to them.

Mechanically it's actuals, plus what we're already committed to, plus the remaining work at a realistic cost. That gives the full year forecast.

Three things make it credible. First, agree the plan. A realistic plan for the year with detailed timing, the capacity and manpower actually available, the work mix and complexity, and the contract rates and variations we already know about. A plan that assumes capacity we haven't got isn't a forecast, it's a wish.

Second, cost the work honestly. I'd use run rate as a guide rather than a rule, and agree one inflationary assumption applied consistently across all finance areas. Different teams quietly using different inflation is one of the easiest ways for a group position to stop adding up. I'd build the base case before adjustments, then set out the overall picture and get the actions identified and embedded in it.

Third, operational buy-in. Sign-off with the operations, and where we disagree I'd quantify the difference rather than argue it out. A number the operation hasn't signed won't survive its first challenge.""",

5: """[1 min 45 · 7:20 elapsed]

Then the actions. I'd work through them in a deliberate order, and raise the risks early rather than at year end.

Planning first. Properly understanding the nature, volume and complexity of the planned work, with predefined rates and a clear monetary threshold for what's a repair and what's capex. Most of the value is won here, before anything is spent.

One boundary before anything else, though. Safety issues, compliance and statutory response times can't be cut. That is not where savings come from.

Second, use the capacity we already have. Productivity, first-time fix, and scheduling across the in-house team, with a fixed scope of work to guard against scope creep. I'd also keep an eye on safety stock, because running materials too lean means paying over the odds the moment something runs out.

Third, challenge additional spend that isn't in the budget. Checking variations, testing rates on like-for-like work, and understanding variance to budget on a causal basis rather than just reporting the number. I'd also be watching for changes to the assumptions we built the forecast on.

Fourth, highlight risks. Identify any offsetting opportunities and raise them early, so actions can actually be agreed. A risk raised late leaves no options.

And only then, fifth, rephase. Discretionary planned work only. That's a timing benefit rather than a saving, and I'd say so rather than let it be counted as one.""",

6: """[1 min 25 · 8:45 elapsed]

Then communicating it, and for me that's partnering rather than reporting.

The report itself is a bridge. Approved budget, to the latest forecast, to the mitigations we've agreed, to the gap that remains.

But I wouldn't present it as just a budget variance, because it isn't one. Repairs is largely revenue spend, so an overspend comes off operating surplus, and that feeds interest cover and covenant headroom. And money spent unplanned on reactive work is money that isn't available for planned works and new homes. That's the trade-off leadership is really being asked to make, so that's how I'd frame it.

On how I'd do it. Be timely, because identifying risks late leaves little opportunity to correct course. Be honest, including when the news is bad or the number has moved against me. Be factual, so the conversation is about the decision rather than about whose figures are right. And be the partner, not the person who turns up at year end with a number and no options.

So: identify the gap, provide a recommendation and the alternative, and be clear on the consequence of doing nothing.""",

7: """[1 min 15 · 10:00 elapsed]

Finally, measurement. A short set agreed with the teams, each with a definition, a baseline, an owner and a point where we escalate. The test of a dashboard is whether it changes what somebody does on Monday morning.

On the money: the gap and how it's moved since last time, whether the savings we expected have actually landed, the split between capital and revenue, cost per job adjusted for the mix of work, and productivity. That mix adjustment matters, because an average cost can fall simply because the team did easier jobs that month, and I wouldn't let that be reported as efficiency.

On service and residents: outstanding safety and compliance work, first-time fix and repeat visits, jobs per operative, how old the backlog is, and satisfaction and repeat contact. Those tell you early if a saving is being taken out of the resident rather than out of the cost.

A weekly look at exceptions with the operational team, a monthly signed-off position, and anything safety-related goes straight up.

Thank you. I'm happy to take questions.""",
}


def main(src, dst):
    prs = Presentation(src)
    total = 0
    print(f"{'SLIDE':<7}{'WORDS':<8}{'SECONDS @135wpm':<18}FIRST LINE")
    for n, slide in enumerate(prs.slides, 1):
        text = NOTES[n]
        slide.notes_slide.notes_text_frame.text = text
        spoken = text.split("\n", 1)[1].split("[Note]")[0]
        w = len(spoken.split())
        total += w
        print(f"{n:<7}{w:<8}{w/135*60:<18.0f}{text.splitlines()[0]}")
    prs.save(dst)
    print(f"\nTOTAL {total} words  ->  {total/135:.1f} min at 135 wpm, "
          f"{total/125:.1f} min at a slow 125 wpm")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
