# Handoff: Beads Deployment Team, Eurobound-f3tq drunk rules (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned one task: Eurobound-f3tq (drunk judgment tiers, embarrassment events, morning evidence, cab mooning). **Done. This window can be cleared.** Nothing is running.

## What was done

1. **Ledger.** The author answered 14 Desk cards on 2026-11-13 (Eurobound-f3tq-q1 to q14). They were read from the Desk, and all 14 now sit in `docs/superpowers/NEXT_WORK.md`, quoted verbatim, as three entries: "Drunk rules, part 1 of 3" (tiers and control), "part 2 of 3" (embarrassment, cab mooning, standing) and "part 3 of 3" (mornings). They were added with `ledger_add.py`, so they are **staged, not committed**. The index also holds another window's staged entries ("Writers' Room answers, part three" and others). Whoever commits should look at the staged diff first.
2. **Status banner.** `docs/superpowers/proposals/2026-11-13-drunk-judgment-and-folklore-proposal.md` now opens with "SHAPE APPROVED, DETAILS RULED, NUMBERS OPEN", a rulings table that maps the proposal's Q1-Q10 to the cards, and a "Still open" list.
3. **Appendix A pointer.** Desk q5 asked to "Keep Appendix A as-is and record the new mapping as replacing it (traceable)". The text of Appendix A is unchanged. One italic note above it, in `design/mechanics/intoxication_law.md`, points to the ruled mapping.
4. **Gap posted to the Desk.** `Eurobound-f3tq-q15` went up under window "Beads Deployment Team" with `relayed: false`. It asks who sets the PROPOSED numbers: override chances, banner time, event beats and length, repeat window, initiator bases, cab-moon join odds, the morning-cone chance and the payoff delay and cap. The options are routes. Escalation thresholds and tier decay are left to Eurobound-p0j, which is deferred.
5. **Build beads.** These were filed with `bead_new.py` (found_by Eurobound-f3tq, discovered-from Eurobound-f3tq) after a duplicate search for intoxication, drunk, embarrassment, traffic cone, hungover, moon, grudge, Cautionary and Beer Goggles. Only Eurobound-p0j and Eurobound-jsd0 overlapped, and the new beads link to them rather than duplicate them.

| Bead | What | State |
|---|---|---|
| Eurobound-diot | Per-bro tier and its dialogue effects | Blocked: f3tq-q15, depends on p0j |
| Eurobound-9m69 | Embarrassment-event runner (q13 cadence) | Blocked: q15, depends on diot |
| Eurobound-evsl | Cab moon (q11) and Cautionary Tale standing (q14) | Blocked: q15, depends on 9m69. **Gap:** no cab context exists |
| Eurobound-3385 | Grudge and fan flags (q6) | Ready |
| Eurobound-p1jn | Morning Hungover (q10) and evidence roll with the plain toast (q2, q9, q12) | Blocked: q15, depends on diot |
| Eurobound-gn7i | Deferred-payoff queue (q8) | Blocked: q15, depends on 9m69 |
| Eurobound-xo6e | Stolen Traffic Cone item doc. The inspect line goes to the author on the Desk | Ready |
| Eurobound-3iwg | Writers' Room round with the author: event pool, payoffs, evidence items E2-E4 | Blocked: xnpg-wr1 (OpenRouter) |
| Eurobound-8hjb | Design doc and `design/registry/entities.yaml`. Asks the author for the doc format first (no template fits) | Ready |

6. **Intoxication-law review.** Each bead that adds an intoxication mechanic (diot, 9m69, evsl, p1jn, gn7i) carries the review note. Points 3, 6, 9 and 10 are still RULING. Points 4 and 8 are PASS-FLAG, and q5 settles point 5's flag. This is flagged, not decided.
7. **f3tq** is now **blocked** on Desk q15, with a summary comment. The canon index was rebuilt, and a search for "Cautionary Tale" finds the new ledger entry. The bead page was synced once.

## Uncommitted (this task)

- `docs/superpowers/NEXT_WORK.md`: three entries, staged.
- `docs/superpowers/proposals/2026-11-13-drunk-judgment-and-folklore-proposal.md`: the banner. Not staged.
- `design/mechanics/intoxication_law.md`: the Appendix A pointer. Not staged.
- This handoff.

## Next for whoever takes the name

When q15 is answered:
1. Relay it verbatim to f3tq and to the six beads that wait on it.
2. Record it in the ledger.
3. Set the beads back to open. diot also needs Eurobound-p0j.

Noticed in passing: the staged icon renames from Eurobound-952g include `velvet_wristband_vip_64/128.png` moving to `legacy_pixel/`. 952g's own comment says it held that twin back. The orchestrator should check that before anyone commits.
