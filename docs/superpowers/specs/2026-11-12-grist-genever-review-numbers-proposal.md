# Proposal: numbers for the pending points in the Windmill Grist and Oude Genever intoxication-law reviews

**APPROVED (author, 2026-11-12, Eurobound Desk eb8-q1): "Approve as proposed".** The values below are ruled and recorded in the two item docs' Intoxication Law Reviews.

**Bead:** Eurobound-eb8. **Status:** APPROVED (author, 2026-11-12, Production Desk `Eurobound-eb8-q1`, verbatim: "Approve as proposed"). No data file or code has changed.
**Author answer that ordered this (bead page, 2026-11-12), verbatim:** "Have a systems designer propose numbers for me to approve" / note: "didnt we change the name of windmill grist and oude genever".
**Serves:** the ⚠ PENDING points in the two 10-point reviews, `design/items/brewery_tour/beer_bottoms_down_item.md:24-36` (Oude Genever / The Shakes) and `design/items/brewery_tour/beer_wobbly_windmill_brewery_item.md:24-36` (Windmill Grist).
**Binding law:** `design/mechanics/intoxication_law.md` (§3, §7, §8) and `design/narrative/bros_choose_debauchery.md`.
**Built on the approved status model:** the item-side duration shape (Eurobound-sue-q1, `NEXT_WORK.md:771`) and the status runtime model (Production Desk Eurobound-1m4-q1, "Approve as proposed", 2026-11-12 21:17Z). The runtime model is in `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` §5 (lines 248-253):
- a status has two independent counters;
- battle turns tick only in battle, and overworld steps tick only on the overworld;
- the status ends when either counter reaches 0, or at rest when `ends_on_rest` is set;
- the remaining turns carry into a fight and are written back afterwards (engine bead Eurobound-d6yl).

Every value below is **APPROVED**. Ruled values are quoted, not changed:
- The Shakes is −15% Accuracy for 3 turns (`docs/superpowers/NEXT_WORK.md:682`).
- Windmill Grist is Set A: +40 HP / +20 Bravado / +15% Speed for 3 turns / −20% Navigation for 5 turns, not sold (`NEXT_WORK.md:680`).

---

## 1. The name question: canon has not renamed either drink

- **The drinks are not renamed.** Round v34 ruled that both need new parody names. The author's words: "the name needs work. This is too high brow and official.... Remember, this is *satire* and *parody*. It isn't supposed to read as serious". The ledger adds "Both need new parody names" (`docs/superpowers/NEXT_WORK.md:683`). Nobody has minted the names yet:
  - Bead Eurobound-jsc ("Writers' Room: rename Windmill Grist and Oude Genever as parody") is blocked. The author approved the OpenRouter top-up on 2026-11-12, and the room has not run: `WritingRoom/tasks/20261112_0816_shamsterdam_drink_renames_and_opener_gag/state.json` shows `"rounds_done": 0`, and `questions_for_author.md` is empty.
  - Both item docs still say "⚠ AUTHOR-REVIEW: rename pending (Writers' Room punch-up)" (`beer_bottoms_down_item.md:43`, `beer_wobbly_windmill_brewery_item.md:44`).
- **The breweries were renamed, not the drinks:**
  - Brouwerij de Molen → **The Wobbly Windmill Brewery** (`NEXT_WORK.md:113-115`, 2026-11-10).
  - Proeflokaal 't Kansen → **Bottoms Down**: "name only; Kees, the jenever bar and the no-hands bow all stay" (`NEXT_WORK.md:488-489`, round v23).
- **Only the files and item ids moved.** `beer_bottoms_down` and `beer_wobbly_windmill_brewery` use brewery stems because e3_slugs was approved (`NEXT_WORK.md:678`). The PNGs were renamed the same way (`beer_bottoms_down_item.md:21-22`, `beer_wobbly_windmill_brewery_item.md:21-22`).
- Canon is not ambiguous, so this doc keeps **Windmill Grist** and **Oude Genever** as working names. When Eurobound-jsc lands, the new names replace them; none of the numbers depend on the names.

---

## 2. Anchors (every number below traces to one of these)

| # | Anchor | Value | Source |
|---|---|---|---|
| A1 | Item duration shape (approved) | `intoxicant.duration {battle_turns, field_steps, ends_on_rest}`; `stack_rule: extend` means "re-hit adds the duration again" | `docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md:22-23`; approved at `NEXT_WORK.md:771` |
| A2 | Status runtime model (approved) | two independent counters (turns in battle, steps on the overworld); ends when either reaches 0 or at rest; remaining turns carry into the fight and are written back | `status-effect-data-shape-proposal.md:250-253`; Production Desk Eurobound-1m4-q1 "Approve as proposed" |
| A3 | Listing (approved review, round v24) | **5 turns in battle ↔ 60 s on the overworld**, cleared by rest; "counts toward Buzzed → Beer Goggles escalation once the alcohol tiers have numbers" | `design/worlds/shamsterdam/the_hoisted_pint.md:237-250` |
| A4 | Overworld walk speed | 3.2 m/s; the bros walk 0.75 m apart | `game/characters/player/player_controller.gd:19`, `:22` |
| A5 | Embarrassed (approved) | 2 battle turns ↔ 60 game-minutes on the field | `NEXT_WORK.md:583`, `:783` |
| A6 | Clock costs | screen change 10 min, fight 20 min, drink 10 min | `NEXT_WORK.md:685` (round v35) |
| A7 | One built screen | Arcade main hall about 15 x 12 m | `design/worlds/debaucheryville/absinthearcade_interior_3d_asset_manifest.md:23` |
| A8 | Drink tag | every alcoholic drink counts as "a drink"; food, drugs and vapes don't | `NEXT_WORK.md:713` (round v37) |
| A9 | Rest | "Morning" is the next rest; the clock jumps to 10:00 | `NEXT_WORK.md:670` |
| A10 | Accuracy | 95% base, −9% per step; Sloppy −3 and Grease Fingers −2 steps, and they add together | `NEXT_WORK.md:567`; `game/battle/battle_core.gd:393-398` |
| A11 | Speed and the size of a Speed shift | Pilsner 5, Chadwick 7, Bradley 8; High/Low Bravado moves Speed ±2 | `design/mechanics/Battle/battle_numbers_proposal.md:36`, `:32` (approved v26) |
| A12 | Clamp precedent | Run chance is held between 10% and 90% | `battle_numbers_proposal.md:35` |
| A13 | The Shakes canon | stacks in duration, not magnitude; cure: time, food or sleep | `design/worlds/shamsterdam/bottoms_down.md:241`, `:243` |
| A14 | Gauntlet | four rounds, "accumulating Shakes stacks on failure" | `design/worlds/shamsterdam/PNG_Assets/bottoms_down_png_assets.md:482` |
| A15 | Food against The Shakes | Frietomat "Reduces debuff duration"; Stroopwafel Cart "Reduced debuff duration"; De Zilte Waarheid "Mild improvement" | `frietomat.md:271`, `stroopwafel_cart.md:254`, `de_zilte_waarheid.md:298` (all `design/worlds/shamsterdam/`) |
| A16 | Navigation factors | additive points on the correct-exit chance: Sober +20, Contact High −15, Space Cake Gamble −30, Canal Confusion −25, map +15, Local Guide +40, each earlier success +5 | `design/worlds/shamsterdam/voetgangerstunnel.md:129-137` |
| A17 | Tunnel Confusion | −15% Navigation; 2 hours or until a successful navigation | `voetgangerstunnel.md:424-427` |
| A18 | Shakes presentation (existing asset spec) | status bar "3-turn duration with stack indicator"; explicit "-15% Accuracy" readout; reduced-motion keeps the sprite still | `bottoms_down_png_assets.md:404-405`, `:504`, `:533` |
| A19 | Spin Meter presentation | vignette corner texture; vignette-only on Low LOD; off in reduced-motion mode | `design/worlds/shamsterdam/PNG_Assets/wobbly_windmill_brewery_png_assets.md:371`, `:376` |

---

## 3. Shared rules (both drinks)

| Id | Rule | APPROVED value | Anchor |
|---|---|---|---|
| R1 | **What a step is** | **1 step = 1 metre walked by the party leader.** The engine has no step yet; Eurobound-d6yl adds the unit, so this definition is offered for it. | A4: movement is continuous. A metre is countable from the leader's travel and sits close to the 0.75 m spacing between the bros |
| R2 | **Steps per battle turn** | **40 steps per turn** | A3: Listing, the approved pair for a brewery-tour drink, is 5 turns ↔ 60 s, so 12 s per turn. At 3.2 m/s (A4) that is 38.4 m, rounded to 40. **Cross-check:** Embarrassed (A5) is 30 game-minutes per turn, which is 3 screen changes (A6). The one built screen is about 12-15 m across (A7), so 36-45 m. The two approved pairs agree |
| R3 | **Counting** | As approved (A2): turns tick in battle, steps tick on the overworld, and the status ends when either counter reaches 0. **One addition:** a status with no battle effect (Navigation) has no battle counter, so a fight never ends it | A2. Without the addition, Grist's "5 turns" would run out inside the fight it was drunk in and never touch the overworld |
| R4 | **Rest** | Both statuses end at the next rest (`ends_on_rest: true`) | A9; A13 ("sleep"); A3 (Listing "cleared by rest") |
| R5 | **Per-serving stacking** | Each serving adds one serving's worth to both counters. Magnitude never grows (`stack_rule: extend`) | A13 (Shakes canon); A1 (approved meaning of `extend`). Grist uses the same rule so the brewery tour has one rule |
| R6 | **Cap** | 4 servings' worth | A14: the gauntlet's four rounds are the only authored count of servings in one sitting |
| R7 | **Alcohol ladder** | Each serving counts as **1 drink** toward Buzzed → Beer Goggles → Shitfaced → Catastrophe. No ABV weighting. The tier thresholds are not proposed here; they stay with Eurobound-p0j (deferred) | A8 (each one is "a drink"); A3 (Listing counts, approved) |

---

## 4. Oude Genever / The Shakes: points 3, 6 and 8

Oude Genever cannot be drunk in combat (`bottoms_down.md:234`), so The Shakes always starts on the overworld and reaches battle by the carry in A2.

| Point | Question | APPROVED value | Anchor |
|---|---|---|---|
| 3 | One serving | **3 turns / 120 steps** | ruled 3 turns; R2 |
| 3 | Extra serving | **+3 turns / +120 steps**; still −15% | R5, A13 |
| 3 | Zeer Oude Jenever ("The Shakes x2") | +6 turns / +240 steps | `bottoms_down.md:219`, R5 |
| 3 | Gauntlet failure | +3 turns / +120 steps per failed round | A14, R5 |
| 3 | Cap | **12 turns / 480 steps** | R6 |
| 3 | Alcohol ladder | 1 drink per serving | R7 |
| 6 | Overworld behaviour | No mechanical effect on the overworld. Walking spends the step counter ("time"). If a fight starts first, the turns carry in | A2; accuracy only matters in battle (A10), and the docs give the Shakes no field effect, so none is added |
| 6 | Couchsurf morning (`bottoms_down.md:367`) | Applied after the rest: one serving | A9, R4 |
| 6 | Frietomat | **−2 turns / −80 steps** per meal | A15 "reduces" |
| 6 | Stroopwafel Cart | **−2 turns / −80 steps** | A15 "reduced" (same word, same cut) |
| 6 | De Zilte Waarheid herring | **−1 turn / −40 steps** | A15 "mild": the smallest unit (R2) |
| 6 | Sleep | Ends it | R4 |
| 8 | Size in the hit roll | **−15 percentage points (95% → 80%)**. Not rounded to 9-point steps, which would change the ruled 15 to 9 or 18 | ruled −15%; A10 |
| 8 | Stacks with Beer Goggles' −Accuracy? | **Yes, they add**, the way Sloppy and Grease Fingers already do in the hit roll. Beer Goggles' own size stays unruled: today it is an enemy debuff from Pilsner's Vintage Ultimate (`design/characters/LordPilsner/lordpilsner.md:32`) and the alcohol-tier version waits on Eurobound-p0j | A10 |
| 8 | Hit floor | None added. The battle has none today, and the Shakes cannot exceed −15 | A10, R5 |
| 4 (addition) | Overworld cue | The existing Shakes status bar with stack indicator and the "-15% Accuracy" readout on the bro's Status card. The stack indicator shows `ceil(turns left / 3)`. The 2px offset-frame tremor goes on the walk sprite too, and in reduced-motion mode the sprite holds still. These are existing assets, and no new text is written. | A18 |

---

## 5. Windmill Grist: points 1, 3, 4, 6 and 8

| Point | Question | APPROVED value | Anchor |
|---|---|---|---|
| 1 | "Not sold" vs the opener-gated purchase | **Not proposed here.** It is a content conflict, not a number; bead Eurobound-8gg owns it | `NEXT_WORK.md:680`; `wobbly_windmill_brewery.md:217` |
| 6 | Navigation −20% duration | **200 steps** (5 turns × R2). It is overworld-only: no battle counter, so it waits out any fight (R3) | R2, R3 |
| 6 | Speed +15% duration | **3 turns / 120 steps.** Drunk in battle, it runs 3 turns. Drunk on the overworld, it lasts 120 steps and carries into a fight that starts first | ruled 3 turns; R2, A2 |
| 6 | Speed +15% size | 15% of Speed, rounded to the nearest whole point, at least +1. That gives **+1** for all three bros (5/7/8). High Bravado gives +2 | A11 |
| 6 | Benefit vs drawback timing | On the overworld the Speed buff (120 steps) ends before the Navigation penalty (200 steps). Drunk in battle, the Speed buff is used up in the fight and the whole penalty is still waiting outside | bros_choose_debauchery.md:16 |
| 6 | Cure besides waiting | **Rest only.** Food gets no cure: the three food tables list The Shakes, not Navigation, and adding one would be new content | R4; A15 |
| 3 | Second Grist | Navigation **+200 steps**, still −20%. The Speed buff **refreshes** to 3 turns / 120 steps and does not extend or grow. HP and Bravado restore again as normal | R5 |
| 3 | Cap | **800 steps**, 4 servings' worth, and rest ends it sooner | R6, R4 |
| 3 | Alcohol ladder | 1 drink per Grist | R7 |
| 3 | Whose Navigation | Navigation is the party's direction roll. The penalty applies while **any** bro has it. Two bros' Grists don't add: the most is −20%, each bro has his own counter, and the penalty lasts until the last counter ends | A16; `FieldStatus.has()` with no target = anyone (`game/core/field_status.gd:96-97`) |
| 8 | Stacks with the Navigation table | **Additive percentage points** with every A16 factor and Tunnel Confusion (−15, A17) | A16 is written as additive points |
| 8 | Floor | The correct-exit chance is clamped to **10%-90%**, so a heavy stack never makes the right exit impossible (Law §3: no softlocks) | A12 |
| 8 | Does drinking cancel Sober +20%? | **Yes.** Sober ends with the party's first `alcohol: true` drink and returns at the next rest. The first Grist therefore costs 40 points (Sober +20 lost, Grist −20 taken). The other option is that Sober ends only at Buzzed, which waits on the ladder (Eurobound-p0j) | A16, A8, R4 |
| 8 | Listing | Independent: Listing drifts walking, and Grist moves the intersection roll, so both apply | A3 |
| 4 | Cue outside the brewery | (a) A Grist status row on the bro's Status card with an explicit "-20% Navigation" readout, like the Shakes' explicit readout. (b) At each Navigation intersection, the Spin Meter's corner vignette at its first-beer level for that decision only: vignette-only on Low LOD, off in reduced-motion mode, where (a) stands alone. (c) It needs one new small status icon (a spin motif) for the readout row. No new dialogue or narration | A18, A19 |

---

## 6. Worked examples (APPROVED values)

- **One Genever, then a fight 60 m away.** 60 of the 120 steps are spent on the way and all 3 turns are left, so the bro fights at 80% hit for 3 turns and The Shakes ends there.
- **One Genever, then a long walk.** After 120 m of walking the step counter runs out and The Shakes ends before any fight. That walk is about 37 seconds at walking speed.
- **Three Genevers, then fries.** 9 turns / 360 steps → Frietomat → 7 turns / 280 steps.
- **Pilsner drinks one Grist at the Couchsurf breakfast.** He gets +40 HP and +20 Bravado. The Speed buff (+1) lasts 120 steps unless a fight comes first. Navigation is −20 for 200 steps, and Sober's +20 is gone until the next rest. The party's correct-exit chance drops 40 points, with a 10% floor.

---

## 7. Intoxication-law 10-point review of this proposal

1. **Source**: Oude Genever (Bottoms Down, Kees; plus Zeer Oude, gauntlet failure, Couchsurf morning) and Windmill Grist (Wobbly Windmill; Yeast Golem x3, Couchsurf +2). Both `alcohol: true`.
2. **Immediate effect**: Unchanged from the rulings. This proposal adds only durations, how statuses combine, and the hit-roll and Navigation arithmetic.
3. **Escalation**: More servings make it last longer, never hurt harder (R5), up to a cap of 4 servings (R6). Each serving is 1 drink on the alcohol ladder (R7).
4. **Player-facing cues**: Shakes: the existing bar, stack count, readout and tremor, now also on the overworld. Grist: a readout row and the intersection vignette. Every cue has a reduced-motion form. The interface shows the loss of control coming (Appendix A: "the interface communicates that they're getting less control").
5. **Player control**: Bounded and readable. Attacks miss more (80% hit). Wrong exits come more often, but the right exit is never impossible (10% floor). No dialogue or movement takeover is added.
6. **Duration and recovery**: Every effect has a turn count, a step count and a cap. It ends at rest, and The Shakes can also be cut with food. It is saved in `FieldStatus`, the existing save (`field_status.gd:3-4`).
7. **Comedic consequence**: Kept as the item docs have it. The bro chases fifteen years of Hendrik's life and gets lost faster. He proves his constitution and can't hold a weapon still. Fries are the cure.
8. **Status interactions**: The Shakes adds to Beer Goggles, Sloppy and Grease Fingers. Grist adds to the A16 table and Tunnel Confusion, clamped to 10-90%. The Sober interaction is approved. Listing is independent of Grist. Canal Courage is unchanged.
9. **Technical dependencies** (proposed engineering work, not built):
   - the steps unit and the turn carry, both already filed as Eurobound-d6yl; R1 offers d6yl its definition of a step;
   - the "no battle counter" case for overworld-only statuses (R3);
   - `extend` with a cap;
   - a flat-point accuracy modifier in `BattleCore._hit`, where steps are the only modifier today;
   - a Navigation stat and roll with the clamp: the roll's base odds are unruled and it has no engine code (Eurobound-76gz);
   - Sober as a flag cleared by `alcohol: true` and restored at rest;
   - one Grist status icon.
10. **Further author approval**: Everything above. After sign-off, the values go into both item docs' reviews and the ledger (eb8 acceptance), and then the engine sync of either drink can go ahead.

## 8. `bros_choose_debauchery.md` check

- **No free advantage (l.16):**
  - Genever: the +25 Bravado is paid for with 80% hit chance for 3 turns per serving, and it can't be drunk in a fight to rescue one.
  - Grist: the +40 HP, +20 Bravado and +1 Speed are paid for with up to a 40-point Navigation swing. The swing outlasts the Speed buff and is never spent inside a fight, and a second Grist buys no extra Speed.
  - Both benefits are front-loaded and both costs trail behind.
- **No moral lectures (l.18):** every cue is a UI readout, an existing sprite or a vignette. No text explains, warns or comments.
- **Willing and delusional (l.28):** nothing stops the bros drinking: no refusal, no cap on purchases. The cap limits only the penalty's length, so the joke can't turn into constant frustration (Law §3).

---

## 9. Not proposed here (owned elsewhere)

- New drink names: Eurobound-jsc (Writers' Room).
- Grist "not sold" vs the opener purchase: Eurobound-8gg.
- Alcohol tier thresholds and Beer Goggles' magnitude: Eurobound-p0j (deferred).
- The steps unit, the turn carry and the write-back: Eurobound-d6yl.
- Navigation base odds and engine stat: Eurobound-76gz (discovered-from Eurobound-eb8).
