# Proposal: Legendary Hangovers, the unit of their after-battle length and a rescale of "+N all stats"

**Status: APPROVED by the author, 2026-11-14 (Eurobound Desk `Eurobound-picf-q1`), verbatim: "Approve as proposed" (no note).** U1-U6 and S1-S5 are canon, U6 included. Read every "PROPOSED" below as approved. Ledger: `docs/superpowers/NEXT_WORK.md`, entry Eurobound-picf-q1.
**Bead:** Eurobound-picf. **Blocks:** Eurobound-90vn (Canal Courage item doc and engine entry).
**Author answer that ordered this (bead page, 2026-11-13), verbatim:** "Have a systems designer propose a unit and a rescale for my approval".
**Already ruled, not reopened here:**
- The four Legendary Hangovers are consumables, one per city, unlocked by that city's 4 stamps (`design/Quests/general_quests/brewerytour.md:86-98`).
- The three older cities' details stand as written (Eurobound Desk c24-q1: "Use the legacy/current details as written"). Canal Courage's effects are approved (Eurobound Desk c24-q3; `docs/superpowers/NEXT_WORK.md:849`).
- Their battle specials, status extras, cures, prices, repurchase rules and flavor text. This proposal touches only two things: what "minutes" means, and how big "+N / −N all stats" is.
- The game clock moves only when the bros act: a screen change is 10 minutes, a fight or minigame 20, buying or drinking a drink 10, and talking is free. Rest jumps to 10:00 (`NEXT_WORK.md:667`, `:670`, `:685`).
- A status can store its length in game-clock minutes: `default_duration.clock_minutes` (Eurobound Desk zcdf-q1; `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md:82`). Canal Confusion's 45 minutes is already stored that way.

**Binding law:** `design/mechanics/intoxication_law.md` and `design/narrative/bros_choose_debauchery.md`.

---

## 1. What canon says today

| | Publandia: The Full Irish Experience | Debaucheryville: The Neon Nightmare | Sinfonia: The Imperial Concerto | Shamsterdam: Canal Courage |
|---|---|---|---|---|
| Source | `design/Quests/publandia/brewerytourpublandia.md:312-322` | `design/Quests/debaucheryville/brewerytourdebaucheryville.md:340-353` | `design/Quests/sinfonia/brewerytoursinfonia.md:122-137` | `design/Quests/general_quests/brewerytour.md:100-121` |
| Battle buff | +15 all stats (`:316`) | +20 all stats (`:344`) | +18 all stats (`:126`) | +20 all stats |
| Hangover penalty | −10 all stats (`:318`) | −15 all stats (`:348`) | −12 all stats (`:130`) | −15 all stats (`:113`) |
| Hangover length | 30 minutes | 45 minutes | 40 minutes | 45 minutes |
| Price | 50 SOVS | 75 SOVS | 60 SOVS | 75 SOVS |

**The battle stat scale these numbers meet** (approved round v26, built in `game/assets/data/party/party_members.json`):

| Bro | Offense | Defense | Speed | Charm | Luck | Grit | Max Bravado |
|---|---|---|---|---|---|---|---|
| Lord Pilsner | 8 | 6 | 5 | 9 | 4 | 3 | 12 |
| Chadwick | 6 | 3 | 7 | 10 | 6 | 2 | 20 |
| Bradley | 12 | 2 | 8 | 4 | 5 | 3 | 14 |

- Damage is (Offense + Bravado Modifier) − Defense, ±2, at least 1 (`design/mechanics/Battle/battle_numbers_proposal.md:14`, `:30`).
- The largest approved swings are the Bravado Modifier (High: + half max Bravado, so +6 for Pilsner; Low: −2; `:29`) and Bravado's ±2 Speed (`:32`).
- The master status list works in ones, twos and threes: Hungover −2 all stats, Crash −3 all stats, Liquid Confidence +3 Charm (`design/mechanics/Battle/status_effects.md:36`, `:107`, `:4`). The only other "all stats" buff in the battle docs is +1 ("Legendary" status, `design/mechanics/Battle/battle_system.md:337`).
- The first boss-sized enemy is Croc Monsieur: 52 HP, Offense 9, Defense 6 (`battle_numbers_proposal.md:39`).

**Why the written numbers don't fit.** +20 takes Pilsner's Offense from 8 to 28 and his Defense from 6 to 26. Croc Monsieur, Offense 9, could not scratch him. −15 takes every stat on every bro below zero, and the engine has no rule for a negative stat (`game/battle/battle_unit.gd:137-175`).

**Why "minutes" is unclear.** The same file that gives The Neon Nightmare its 45 minutes also says "1 in-game hour (real-time = 5 min)" (`brewerytourdebaucheryville.md:332`), a real-time clock the game no longer has. The approved battle model counts turns and steps (`status-effect-data-shape-proposal.md:254-257`). By the approved Embarrassed pair (60 game-minutes = 2 turns, `NEXT_WORK.md:783`) and 40 steps a turn, 45 minutes would be 1.5 turns, or 60 metres of walking: under 20 seconds. A hangover that is over before the bros leave the room is not a hangover.

---

## 2. Proposed unit (every value PROPOSED)

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| U1 | **Unit** | The four lengths are **game-clock minutes**, stored in `default_duration.clock_minutes`. The numbers stay as written: **30 / 45 / 40 / 45** | The author already put Canal Confusion's 45 minutes on the game clock by name (zcdf-q1), and Canal Confusion runs alongside Canal Courage Hungover for "the same 45 minutes" (`brewerytour.md:113`). One hangover cannot run on two units. No ruled number changes |
| U2 | **What that buys** | 30 minutes = 3 screen changes, or a fight plus a screen change; a second fight that starts before minute 30 is covered too (U3). 40 = 4 screen changes, or 2 fights. 45 = 2 fights back to back with 5 minutes left, enough to catch a third. In normal play, with walking between fights: 1 to 2 fights for Publandia and Sinfonia, 2 to 3 for the two 45-minute hangovers | Clock costs, `NEXT_WORK.md:685` |
| U3 | **In battle** | If the hangover is live when a fight starts, the penalty holds for **the whole fight**. The fight costs its usual 20 clock minutes; the hangover does not expire in the middle of it | The existing carry: a field status enters battle as "until the fight ends" (`game/core/field_status.gd:86-89`, `:126-134`; shape doc `:25`). No battle-turn counter is added, so no minutes-to-turns conversion is needed |
| U4 | **Rest and cures** | As written: the city's cure item, sleep, or waiting it out. Rest ends it (`ends_on_rest: true`) | `brewerytourpublandia.md:319`; `brewerytourdebaucheryville.md:352`; `brewerytoursinfonia.md:134`; `brewerytour.md` Canal Courage block |
| U5 | **Stacking** | As written: one instance of a given city's hangover at a time. Drinking the same city's again while hungover refreshes it to its full length and never adds | `brewerytourpublandia.md:326-331` |
| U6 | **The hangover always gets its fight** (separable; drop it if you prefer) | Waiting it out cannot end the hangover until the bro has **started one fight** with it. Until then the clock holds it at its last 10 minutes. The cure item and sleep still end it at any time | Without this, three screen changes with no fight wipe a 30-minute hangover and the bro never pays in battle. `bros_choose_debauchery.md:16`: no consequence-free advantage. It never traps the player: the cure and a bed always work (Law §7) |

**Rejected alternative: convert to turns and steps.** By the approved pairs that is 1 to 1.5 turns, or 40 to 60 steps (§1). To make it bite, every length would have to be re-invented (say 6 turns / 240 steps), which changes four ruled numbers instead of none.

**Rejected alternative: real minutes.** The game clock ruling says time never moves while the player stands still (`NEXT_WORK.md:667`). A real-time hangover could be waited out by standing still.

---

## 3. Proposed rescale (every value PROPOSED)

**Rule S1: divide the written number by 3, round to the nearest whole point.** The order between the cities, and the gap between buff and penalty, stay exactly as ruled.

| City | Battle buff: written → PROPOSED | Hangover penalty: written → PROPOSED | Length (U1) |
|---|---|---|---|
| Publandia, The Full Irish Experience | +15 → **+5 all stats** | −10 → **−3 all stats** | 30 clock minutes |
| Sinfonia, The Imperial Concerto | +18 → **+6 all stats** | −12 → **−4 all stats** | 40 clock minutes |
| Debaucheryville, The Neon Nightmare | +20 → **+7 all stats** | −15 → **−5 all stats** | 45 clock minutes |
| Shamsterdam, Canal Courage | +20 → **+7 all stats** | −15 → **−5 all stats** | 45 clock minutes |

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| S1 | **Size** | Written ÷ 3, rounded | The buff lands at +5 to +7, the size of Pilsner's High Bravado bonus (+6, `battle_numbers_proposal.md:29`): a Legendary Hangover is "a second High Bravado on everything". The penalty lands at −3 to −5: from Crash (−3, `status_effects.md:107`) upward, above ordinary Hungover (−2, `:36`), which is what "Legendary" should mean |
| S2 | **Which stats "all" covers** | The six battle stats: **Offense, Defense, Speed, Charm, Luck, Grit**. Not max HP, not max Bravado, not accuracy | These are the six the status table reads (`game/battle/status_table.gd:11`). Max HP and max Bravado are meters, and moving them mid-fight has no rule. This is proposed for the four Legendary Hangovers only. The same question is open for Crash, Cottonmouth and Hungover (shape doc §8 Q1); the author may apply this answer there too, or not |
| S3 | **Floor** | A status penalty never takes a stat **below 1** | −5 on Bradley's Defense 2 or anyone's Grit would otherwise go negative. A hit always does at least 1 already (`battle_numbers_proposal.md:30`) |
| S4 | **Display** | The Status card shows the rescaled number: "+7 all stats", "−5 all stats" | Same explicit-readout rule as The Shakes (`design/items/brewery_tour/beer_bottoms_down_item.md:30`) |
| S5 | **Unchanged** | Confusion immunity, Embarrassment immunity, Canal Courage's −25% Bravado loss, Neon Nightmare's 10% input reversal, every other extra, every cure, every price | Ruled as written (c24-q1, c24-q3) |

**What the pattern keeps.** Canal Courage's approved proposal found the penalty is two-thirds to three-quarters of the buff (`docs/superpowers/specs/2026-11-12-canal-courage-legendary-hangover-proposal.md:32`). After S1 it is 3/5, 4/6 and 5/7: 60% to 71%. Price still follows length.

### 3.1 Worked example (PROPOSED values, Croc Monsieur: Offense 9, Defense 6)

| | Pilsner normal (High Bravado) | Pilsner on The Neon Nightmare (+7) | Pilsner Neon Nightmare Hungover (−5, Mid Bravado) |
|---|---|---|---|
| Offense / Defense / Speed | 8 / 6 / 5 | 15 / 13 / 12 | 3 / 1 / 1 |
| His hit on the croc | about 8 | about 15 | 1 (3 + 3 − 6 is 0; a hit does at least 1) |
| The croc's hit on him | about 3 | 1 | about 8 |

One fight where he hits twice as hard and barely feels it, then two or three fights where he tickles the enemy and takes nearly triple. Bradley on +7 hits for about 20 instead of 13; hungover at −5 his Defense 2 and Grit 3 both sit at the floor of 1.

### 3.2 Rejected alternatives

- **Keep flat +15 to +20.** The buff makes every bro immune to the enemies the game has numbers for, and the penalty is below zero on every stat.
- **A percentage of each stat** (say +60% / −40%, the way Windmill Grist's Speed buff is 15% of Speed). It would track level-ups, but no level curve is ruled, most stats are so small that percentages round to 1 or 2 points and erase the difference between the cities, and "+60% all stats" reads worse on the Status card than "+7". If a level curve is ruled later and +7 falls behind, revisit S1 then.
- **Divide by 5** (+3 / +4 / +4, −2 / −2 / −3). Sinfonia and Debaucheryville collapse to the same buff, and the penalty is no worse than ordinary Hungover.

---

## 4. Intoxication law §8: 10-point review

| # | Point | Answer |
|---|---|---|
| 1 | Source | The four Legendary Hangover consumables, each unlocked by its city's 4 stamps and repurchasable at stamped locations. All `alcohol: true` |
| 2 | Immediate effect | PROPOSED +5 / +6 / +7 / +7 to the six battle stats for one whole battle, plus the ruled specials (unchanged) |
| 3 | Escalation | None added. One instance per city's hangover; a second drink refreshes the length (U5). Each counts as 1 drink on the alcohol ladder (approved R7, `2026-11-12-grist-genever-review-numbers-proposal.md` §3) |
| 4 | Player-facing cues | The hangover's Status-card row with the explicit "−N all stats" readout (S4). Each city's ruled sensory extras are unchanged. No new text |
| 5 | Player control | No new loss of control. Neon Nightmare's ruled 10% input reversal and Imperial's bows stay as written. U6 only stops the hangover expiring unpaid; the cure item and sleep always end it |
| 6 | Duration and recovery | 30 / 40 / 45 / 45 game-clock minutes; a live hangover lasts through the fight it enters (U3). Cure item, sleep, or waiting. It is a saved `FieldStatus` clock row, so save and load keep it |
| 7 | Comedic consequence | He drinks the city's trophy and has the fight of his life. Then he swings at the next enemy and does 1 damage, still certain he is on form |
| 8 | Interactions | Canal Confusion runs on the same clock beside Canal Courage Hungover (unchanged). Six O'Clock Wit postpones it like any Hungover (`design/worlds/shamsterdam/the_mad_monarchs_wit_tea_party.md:229-238`). Photogenic Drinker's "−10% Hungover duration" (`brewerytour.md:80`) on clock minutes is not ruled for any city and is not proposed here. Different cities' hangovers can be live together as written; their penalties add, down to the floor of 1 (S3) |
| 9 | Technical dependencies (proposed engineering, not built) | A battle-scoped "+N all stats" buff that ends with the fight; an after-battle hook that applies the hangover row; `stats.all` read as the six stats (today it is a deliberate no-op, `status_table.gd:7`, `:11`); a floor of 1 in `BattleUnit`'s stat functions (`battle_unit.gd:137-175`); the four hangover entries in `status_effects.json` with `clock_minutes`; U6's "has started a fight" mark on the row |
| 10 | Further author approval | U1-U6 and S1-S5. U6 can be dropped on its own. S2 can be extended to Crash, Cottonmouth and Hungover, or kept to these four |

## 5. `bros_choose_debauchery.md` check

- **No free advantage (l.16):** the best single fight in the game is paid for with one to three fights at Crash strength or worse, and U6 closes the walk-it-off dodge. The price (50 to 75 SOVS) is unchanged.
- **No lectures (l.18):** the only cue is a number on the Status card. Nothing warns, explains or comments.
- **Willing and delusional (l.28):** nothing stops him buying another one while hungover.

## 6. If approved

1. Record the ruling in `docs/superpowers/NEXT_WORK.md`.
2. Update the four hangover blocks to the ruled unit and sizes: `brewerytourpublandia.md:316-318`, `brewerytourdebaucheryville.md:344-348`, `brewerytoursinfonia.md:126-130`, `brewerytour.md` (Canal Courage block), plus `design/items/brewery_passport_book_item.md`.
3. Unblock Eurobound-90vn (Canal Courage item doc and engine entry) and file the engineering bead for §4 point 9.

## 7. Found work filed (not decided here)

- `brewerytourdebaucheryville.md:332` still says "1 in-game hour (real-time = 5 min)", a real-time clock that the round v34 game-clock ruling replaced. Bead: Eurobound-kh9g.
