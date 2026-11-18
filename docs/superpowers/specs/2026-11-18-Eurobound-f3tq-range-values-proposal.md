# Drunk Rules: One Value per Range (Eurobound-f3tq)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-f3tq-q16`).
> Author's direction, verbatim (Eurobound Desk `Eurobound-f3tq-q15`, 2026-11-18): "An agent proposes one value for each in a single table, for my approval".
> **Every value in this file is PROPOSED.** Each sits inside the range the proposal gave
> (`docs/superpowers/proposals/2026-11-13-drunk-judgment-and-folklore-proposal.md`, cited by line below).
> Nothing in `game/` or `design/` was changed.
> **Not on this card:** how a drink raises the tier and how the tier wears off (bead Eurobound-p0j). The rulings these values
> build on are in `docs/superpowers/NEXT_WORK.md:955-957` ("Drunk rules, part 1 of 3" to "part 3 of 3").

Audience: younger Gen X, xennial and millennial women. The joke is watching the bros lose the wheel, so the numbers keep the
loss of control frequent enough to land as a running gag and short enough never to stop the game.

## The table

Law column: the RULING points of the 10-point review (`design/mechanics/intoxication_law.md` §8; the proposal's review at
`:240-247` leaves points 3, 6, 9 and 10 at RULING). Every row touches point 10 ("requires further author approval"); this
card is that approval, so point 10 is not repeated per row.

| # | Range (proposal line) | Range | Value | Reason | Law flag |
|---|---|---|---|---|---|
| 1 | Beer Goggles: chance a `judgment_gate` choice is overridden (`:66`) | 10-20% | **15%** PROPOSED | "Occasionally" (f3tq-q1). With the cap in row 3, a two-gate talk is overridden about 28% of the time: a recurring gag, not every conversation (law §3: "comedic payoff rather than constant frustration"). | **Point 3**: how often a bro sits at Beer Goggles depends on escalation (p0j). |
| 2 | Shitfaced: override chance (`:67`); Catastrophe uses the same ("everything from T3", `:68`) | 30-50% | **40%** PROPOSED | The sensible option is already gone at Shitfaced, so the roll only picks between bold and stupid. 40% makes the stupid pick close to a coin flip, a visible step up from row 1 (law §2 progression) while the menu still matters. | **Point 3** (as row 1). |
| 3 | Overrides per conversation (`:66` gives 1 at Beer Goggles; no cap is stated for Shitfaced or Catastrophe) | 1 | **1 at every tier** PROPOSED | Fills the gap: one executive decision per conversation keeps every talk bounded (law §7: "bounded durations and predictable recovery"). | **Point 6** (bounded control). |
| 4 | "PILSNER IS MAKING AN EXECUTIVE DECISION" banner (`:75`) | 1.0-1.5 s | **1.5 s** PROPOSED | The banner is the only telegraph and no text explains it, so it must be readable: 39 capitals plus the auto-picked line need the long end (law §3 "understandable", §7 "readable"). | none |
| 5 | Beats in one embarrassment event (`:76`) | 1-3 | **3 at most** PROPOSED | Setup, escalation, punchline. EarthBound-style gags run a few text boxes; a fourth beat starts to feel like a cutscene. Each event's own count (1-3) is set when its content is written with the author (Eurobound-3iwg). | **Point 6** (duration). |
| 6 | Whole event, after which the timeout auto-advances (`:77`) | 20-40 s | **30 s** PROPOSED | About 10 s a beat for three beats. It also matches the shortest ruled loss of control in the field, Green Fairy Confusion's "random 30 s to 3 min" (`NEXT_WORK.md:753`). | **Point 6** (duration). |
| 7 | Nights before the same event can fire again (`:92`) | 2-3 | **2 nights** PROPOSED | The event pool is not written yet (Eurobound-3iwg). With up to two events a night (f3tq-q13), a 2-night lock holds back at most four events, so a small first pool rarely drops to the fallback. Raise it once the pool is big. Counted with `GameClock.day()` (`game/core/game_clock.gd:38`), which exists. | none |
| 8 | Default initiator base B per bro per event (`:116`) | 0-3 | **1 for every bro** PROPOSED | With every B at 1, the drunkest bro is likeliest to start the event (the proposal's own worked example, `:123`). Exceptions (0 = this bro cannot start it; up to 3 = the event is written around him) are set per event with the author, as content. | **Point 3**: the weight is B x tier, so it scales with escalation (p0j). |
| 9 | Cab moon: each other bro's base chance to join, J (`:129`); Pilsner's "always, once he's at Beer Goggles or worse" is ruled (f3tq-q11), so J only covers Chadwick, Bradley, and Pilsner while Buzzed | 20-50% | **30%** PROPOSED | With +15% a tier (row 10), a bro joins at 30% Buzzed, 45% Beer Goggles, 60% Shitfaced. Pilsner already guarantees a duo from Beer Goggles up. When he starts it, the three-bro moon (which hits the shared regional standing, `:131`) lands on 20% of rides with the others at Beer Goggles and 36% with them Shitfaced: a big night, not the default. | **Point 3** (scales with tier); **point 9**: no cab or taxi context exists in `game/` (grep for cab/taxi finds only arcade cabinets). |
| 10 | Join chance added per tier above Buzzed; join cap (`:129`) | single values already | **+15% a tier, cap 90%** PROPOSED (unchanged) | Listed so this approval covers every number on the card. The 90% cap means even a Catastrophe bro can sit one out. | **Point 3**. |
| 11 | Morning cone: chance each Catastrophe morning (`:174`, `:183`; flat chance ruled, f3tq-q9) | 30-50% | **40%** PROPOSED | "It happens sometimes" (author, f3tq-q2). 40% is the proposal's own worked example (`:187`). With a four-slot pool drawn once per save (`:199`), the pool lasts about ten Catastrophe mornings. | **Point 9**: the wake-up hook exists (`GameClock.rest`, `game_clock.gd:64`); the roll is not built (Eurobound-p1jn). |
| 12 | Evidence items per morning (`:187`) | single value already | **1** PROPOSED (unchanged) | One plain toast keeps the joke clean: the bros just have a cone now. | none |
| 13 | Drunk purchase payoff delay (`:162`) | 2-4 days | **3 in-game days** PROPOSED, for every payoff | The author's own example ("Idiotic purchase, useful three days later", proposal `:151`; "Author's example is 3 in-game days", `:162`). Counted with `GameClock.day()`; delivered at the wake-up of the due day (`:163`). | none |
| 14 | Open payoffs at once (`:166`) | single value already | **3** PROPOSED | Equal to the delay, so one drunk purchase a night, every night, never hits the cap; it only stops farming several in one night. **Flag:** f3tq-q8 rules the purchase "Always" pays off, so the cap must work by **not offering** a drunk purchase while three are open, never by dropping a record that was already paid for. | **Ruled f3tq-q8** must hold (see flag). |

## Notes for the build beads

- Eurobound-diot takes rows 1-4; Eurobound-9m69 rows 5-8; Eurobound-evsl rows 9-10; Eurobound-p1jn rows 11-12;
  Eurobound-gn7i rows 13-14. Each bead still runs its own 10-point review before building.
- Point 6 stays RULING after this card: the event lengths are bounded here, but tier decay belongs to Eurobound-p0j.
- Point 9 stays RULING for the cab moon until a cab context exists (Eurobound-evsl already flags it).
- Not in the ranges, so not proposed here: how long the morning Hungover lasts in the field. The status master list gives
  only battle turns (`design/mechanics/Battle/status_effects.md:35-38`, "3-5 turns"), and nothing in `game/core/` applies it
  yet. Filed as its own bead, Eurobound-pzei (author-ruling; it blocks Eurobound-p1jn).
