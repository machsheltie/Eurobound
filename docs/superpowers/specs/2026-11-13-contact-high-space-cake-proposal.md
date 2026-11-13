# Proposal: Contact High and Space Cake Gamble (sources, lengths, teleport rules)

**Status: PROPOSED, waiting on the author (Eurobound Desk `Eurobound-vt7k-q2`).** Nothing here is canon until the author approves it. Every number is PROPOSED.
**Bead:** Eurobound-vt7k. **Author answer that ordered this (Eurobound Desk `Eurobound-vt7k-q1`), verbatim:** "Have a systems designer propose sources, lengths and teleport rules".
**Already ruled, not reopened here:**
- Contact High −15 and Space Cake Gamble −30 on the Navigation roll (`design/worlds/shamsterdam/voetgangerstunnel.md:132-133`). They count once while any bro or the party has the status (`game/core/navigation_roll.gd`, Eurobound-1esc).
- Points add, then the chance is clamped to 10%-90%, then the roll happens (Eurobound-eb8; N3 at `voetgangerstunnel.md:146`).
- Sober (+20) ends only with the party's first **alcoholic** drink (`voetgangerstunnel.md:131`). Drugs don't count as "a drink" (`docs/superpowers/NEXT_WORK.md:713`).
- Lengths are stored in `default_duration.clock_minutes` (Eurobound-zcdf, author zcdf-q1; `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md`, note under §3).
- The game clock moves only when the bros act: a screen change costs 10 min, a fight or minigame 20, buying or drinking a drink 10, and talking is free. Rest jumps to 10:00 (`NEXT_WORK.md:666-671`, `:685`).

---

## 1. What canon already says

| Subject | Canon | Where |
|---|---|---|
| Contact High, effect | "Confused state from secondhand exposure (+Relaxed, −Coordination)" | `design/worlds/shamsterdam/shamsterdam.md:276` |
| Contact High, De Groene Gids | "Environmental AoE effect, applies mild Confusion to all party members while inside" | `design/worlds/shamsterdam/de_groene_gids.md:214`; `npcs/De_Groene_Gids/npc_budtender_bas.md:248` ("While inside") |
| Contact High, tunnel | Coffeeshop Quarter wrong exit: "'Contact High' debuff risk from ambient atmosphere", plus a "confusion cure" at tourist prices | `voetgangerstunnel.md:162-166` |
| Contact High, tunnel data | `debuff_risk_check`, `contact_high`, `chance: 0.3`, then an `offer` of `confusion_cure` at `tourist_markup` | `design/worlds/shamsterdam/events/voetgangerstunnel_events.json:96-97` |
| Contact High, couchsurf | A possible negative payoff | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:36` |
| Contact High, cue | Contact High Indicator, 48x48, "Ambient AoE affecting the whole party while inside" | `design/worlds/shamsterdam/PNG_Assets/De_Groene_Gids_PNG_Assets.md:355` |
| Space Cake Gamble | "Delayed effect (nothing for 2 hours, then EVERYTHING)" | `shamsterdam.md:278` |
| Space Cake Gamble, tunnel | "−30% accuracy, random teleportation"; data `"random_teleport": true` | `voetgangerstunnel.md:133`; `design/worlds/shamsterdam/core/voetgangerstunnel_core.json:65` |
| Space Cake (item) | 8 SOVS; "+40 Bravado after 2 hours game time"; "It's Not Working" dialogue | `de_groene_gids.md:113`; `npc_budtender_bas.md:237` |
| The timer | "Purchases trigger 2-hour countdown"; "Delayed status effects hit all at once when timer completes"; on landing: "−Navigation, +Confusion, +Bravado burst" | `de_groene_gids.md:126-130` |
| The timer | "2-hour game-time countdown with a visible UI counter. All delayed effects land simultaneously at expiry" | `npc_budtender_bas.md:249`, `:332` |
| The timer, art | Timer UI; the timer "persists across location changes"; on landing, 3 distortion rings over 2.0 s, a warp vignette, and the trio's "OH." frame; the music bed pitch-bends 4% down "and stays there" | `De_Groene_Gids_PNG_Assets.md:345`, `:497-502` |
| Delayed strain | "Shamsterdam Dream": "+20 Bravado, −Speed, Delayed 'Space Cake Effect'" | `de_groene_gids.md:110` |
| Lost time | The Space Cake Incident: "Wake up in location you don't remember entering" | `shamsterdam.md:362-366` |
| After the high | The Munchies: "Triggers after Bravado boost wears off" | `de_groene_gids.md:216`; `npc_budtender_bas.md:250` |

Nothing in canon gives Contact High a length outside the shop. Nothing gives Space Cake Gamble a length after it lands, and nothing says how a teleport works.

**One reading this proposal relies on (PROPOSED):** "Space Cake Gamble" is the status the Space Cake Timer applies when it lands. The landing's "−Navigation, +Confusion" (`de_groene_gids.md:130`) is the Gamble's −30 Navigation and its teleport, and the "+Bravado burst" is the item's +40 Bravado. The "Space Cake Effect" food rows in other docs (`frietomat.md:273`, `stroopwafel_cart.md:255`, `de_zilte_waarheid.md:299`) read the same active status.

---

## 2. Contact High (every value PROPOSED)

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| CH1 | **Source A: inside De Groene Gids** | Every screen of De Groene Gids applies Contact High to the whole party (`FieldStatus.PARTY`), refreshed to its full length on each screen. In effect, it lasts while the party is inside and for **30 clock minutes** after they leave | `de_groene_gids.md:214`; `npc_budtender_bas.md:248`. "While inside" alone would never reach the tunnel, which is the only place the −15 does anything (N5). The 30 minutes carry the haze out the door |
| CH2 | **Source B: Coffeeshop Quarter tunnel exit** | On emerging there, **30%** chance that the party gets Contact High for 30 clock minutes | `voetgangerstunnel.md:166`; the 30% is already in `voetgangerstunnel_events.json:96`. Adopting it adds no new number |
| CH3 | **Source C: Couchsurfing Chronicles** | When that quest rolls Contact High as a negative payoff, it uses the same default: party, 30 clock minutes | `couchsurfingchroniclesshamsterdam.md:36` |
| CH4 | **Not sources** | (a) The "Contact High Cloud" enemy (`shamsterdam.md:399`) inflicts battle Confusion in its own doc, not this status. (b) "Nicotine Contact High" in Debaucheryville (`design/worlds/debaucheryville/cyberspacekavarna.md:110`) is a different status. (c) "Green Guide Special" gives +Confused (`de_groene_gids.md:111`), not Contact High | Keeps one meaning per name |
| CH5 | **Effect** | The ruled −15 Navigation, and nothing else mechanical. **"Mild Confusion" means this penalty.** It does not apply the reversed-controls Confusion (`game/core/field_status.gd` GREEN_FAIRY_CONFUSION), the battle `confused` status, or a stat change. "+Relaxed, −Coordination" (`shamsterdam.md:276`) is shown, not counted: the cue, plus whatever lines the author approves | "Mild" (`de_groene_gids.md:214`) sits below the Green Fairy's reversed controls. Coordination is not an engine stat |
| CH6 | **Scope / bearer** | `scope: ["field"]`, applied to the party. It is not carried into battle | Canon gives it no battle use. A fight costs 20 clock minutes, so a fight burns two-thirds of it |
| CH7 | **Length** | `clock_minutes: 30`, `ends_on_rest: true`, `until_cured: false` | 30 minutes = 3 screen changes: enough to walk from the haze into the tunnel and pay for it, short enough to stay "mild". It matches Red Light Shame's 30 minutes on the sister exit (`voetgangerstunnel.md:158`) |
| CH8 | **Stacking** | `stack_rule: "refresh"`: a new exposure resets it to 30 and never adds. It never counts twice on the roll | Secondhand smoke doesn't add up |
| CH9 | **Cures** | Rest; waiting it out; the Coffeeshop Quarter's "confusion cure" (`voetgangerstunnel.md:165`, `voetgangerstunnel_events.json:97`) **if the author rules that item**. The item has no doc, name or price, so it is filed as its own bead (§6) and nothing here defines it | The cure is sold in the same room that gave you the haze, at tourist prices |
| CH10 | **Sober** | Contact High does **not** end Sober (drugs are not "a drink", `NEXT_WORK.md:713`). A Sober party with Contact High nets +5 | Settled ruling; stated so nobody "fixes" it |

---

## 3. Space Cake Gamble (every value PROPOSED)

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| SC1 | **Source: the Space Cake** | Buying a Space Cake at De Groene Gids (8 SOVS) means a bro eats it at the counter and starts the **Space Cake Timer** on that bro | `de_groene_gids.md:113`, `:126` ("Purchases trigger"); `npc_budtender_bas.md:139-142` (Bas states the two hours at purchase) |
| SC2 | **Source: "Shamsterdam Dream"** | That strain also starts the Space Cake Timer, in addition to its own +20 Bravado and −Speed | `de_groene_gids.md:110` ("Delayed 'Space Cake Effect'") |
| SC3 | **Not sources (yet)** | "Space Cake Roulette" (`shamsterdam.md:261`), Schrödinger's Souvenir "Healing Edibles" (`shamsterdam.md:218`) and "Space Cake Mix" (`schrodingers_souvenir.md:170`). None has an item doc. Each becomes a source only when its own doc says so | No invention |
| SC4 | **The timer** | A status row `space_cake_timer` ("Space Cake Timer", the name canon already uses at `npc_budtender_bas.md:249`): `section: "neutral"`, `scope: ["field"]`, `clock_minutes: 120`, no effect of its own, `then: {status: "space_cake_gamble"}`. Its cue is the Timer UI (`De_Groene_Gids_PNG_Assets.md:345`). It persists across locations (`:500`). "It's Not Working" lines unlock at 30/60/90 minutes (`de_groene_gids.md:219-240`) | Uses the approved shape's `then` chain instead of inventing a delay field |
| SC5 | **Landing ("then EVERYTHING")** | When the timer reaches 0, all of these happen together (`npc_budtender_bas.md:332`): (a) the bro gets **+40 Bravado** (`heal_bravado`, capped at max as usual); (b) the bro gets **Space Cake Gamble**; (c) the onset cue plays (rings, warp vignette, "OH." frame, the audio ramp: `De_Groene_Gids_PNG_Assets.md:497-502`; `de_groene_gids.md:279`) | All canon. Only the order is proposed |
| SC6 | **Onset wobble** (separable; drop it if you prefer) | At landing, **15 real seconds** of reversed movement, using the existing reversed-controls field row (as Trap Mirror does for 30 s, `field_status.gd` TRAP_MIRROR). Dialogue choices are not shuffled | "WHY IS THE FLOOR MOVING" (`de_groene_gids.md:247`). This is the "+Confusion". Law §3 allows a short, bounded loss of control |
| SC7 | **Effect while active** | The ruled −30 Navigation, plus **random teleportation** (§4). No stat changes, no battle effect. The 4% pitch-bent music bed holds while the status is active (`De_Groene_Gids_PNG_Assets.md:502`, "and stays there") | Canon effects only |
| SC8 | **Scope / bearer** | `section: "negative"`, `scope: ["field"]`, bearer = the bro who ate it. The Navigation penalty already counts once while any bro has it | As Tunnel Confusion and Grist |
| SC9 | **Length** | `clock_minutes: 90` after landing, `ends_on_rest: true` | 90 minutes is the "ninety minutes later" Bas's customers reach the munchies counters (`npc_budtender_bas.md:269`, `:276`). In clock terms it is about 9 screen changes, or 4 fights. It runs longer than Contact High (30) and Canal Confusion (45) and shorter than Tunnel Confusion (120), since it is the harshest penalty and the bros paid and waited two hours for it. Alternatives for the author: 60 or 120 |
| SC10 | **Stacking** | **Before landing:** a second cake joins the running timer; the timer does not restart. When it lands, each cake's +40 Bravado lands, and the Gamble lasts 90 min per cake, **capped at 180**. **After landing:** a new cake starts a new timer; when that lands, it adds 90, again capped at 180 remaining. The penalty stays −30 | Chadwick: "Should we get another one?" (`de_groene_gids.md:222`). The cap keeps it bounded (Law §7). The shape has no cap field yet; Grist has the same gap (Eurobound-cvkq) |
| SC11 | **Rest** | Rest ends Space Cake Gamble **and clears a timer that has not landed yet**: the bros slept through it, and no Bravado lands | Rest is the universal reset (`NEXT_WORK.md:670`). It stops the timer being banked overnight for a free morning burst |
| SC12 | **Cures** | Only rest or waiting it out. No item cures it. The "confusion cure" (CH9) does not touch it | "Two. Hours." Bas never shortens anything (`npc_budtender_bas.md:72`, `:419`) |
| SC13 | **Afterwards** | When it ends **by time** (not by rest), The Munchies follows: canon fires it "after Bravado boost wears off" (`de_groene_gids.md:216`). The Munchies has no status entry or numbers, so it is filed as its own bead (§6). Until it is ruled, nothing follows | Law §5 (delayed consequence) |
| SC14 | **Sober** | Space Cake does not end Sober (`NEXT_WORK.md:713`). A Sober bro with Space Cake Gamble nets −10 | Settled ruling; stated, not reopened |

---

## 4. Random teleportation (every value PROPOSED)

The "Gamble": the roll decides **whether** the bros get it right, and the cake decides **where** they get it wrong.

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| T1 | **When** | Only on the Voetgangerstunnel Navigation roll, while any bro has Space Cake Gamble | `voetgangerstunnel.md:133`; N5 (`:148`): the only Navigation roll |
| T2 | **Order** | Roll as ruled (base + modifiers → clamp 10-90 → roll). **If the roll is correct, nothing changes.** If it is wrong, a second roll: **50%** chance the wrong exit is replaced by a teleport | The approved 10% floor (eb8) stays exact: a teleport can never take away a correct exit. 50% is the coin flip in "Gamble" |
| T3 | **Where to** | Uniformly among **every tunnel exit except the followed sign's correct one**: the other sign's exits, the other wrong exits, and "Where you started". That is 6 destinations, each 1/6. Example: heading for Centraal, the bros can come up at Museum Mile, Frietomat or the canal | Uses only the 7 exits the doc already authors (`voetgangerstunnel.md:47-56`), so it needs no new map and cannot softlock |
| T4 | **What it counts as** | A wrong turn, for Tunnel Confusion's count (3) and Tunnel Vision (lost). The exit's own consequences apply in full: Red Light Shame, no re-entry from Roodelicht Row, the Coffeeshop Quarter's 30% Contact High, and so on (`voetgangerstunnel.md:155-178`) | One rule for every exit |
| T5 | **Lost time** (separable) | A teleport costs **30 extra clock minutes** on top of the screen change | "Wake up in location you don't remember entering" (`shamsterdam.md:364`). Because the Gamble runs on the clock, lost time also eats the high, so a run of teleports burns it out faster: self-limiting |
| T6 | **Cues** | The landing's warp vignette (`De_Groene_Gids_PNG_Assets.md:498`) covers a hard cut to the new exit, with no walking animation. With reduced motion: a plain cut. The bros' lines on arrival come from a writing round with the author; none are proposed here | Law §7 (readable, with an accessibility option) |
| T7 | **Map readout** | The map readout (Display, `voetgangerstunnel.md:149`) still shows only the correct-exit chance. A teleport doesn't change that number | The approved readout is unchanged |

**What the player sees** (Centraal, drunk, Space Cake only: 10% correct). Without teleport, the wrong exits are Roodelicht 53 / Coffeeshop 22 / Start 15 (proposal §4 of the base-odds spec). With T2-T3, 45 points are spread evenly over 6 destinations (7.5 each):

| Exit | Chance |
|---|---|
| Centraal Chaos (correct) | 10% |
| Roodelicht Row | 34% (26.5 + 7.5) |
| Coffeeshop Quarter | 18.5% (11 + 7.5) |
| Where you started | 15% (7.5 + 7.5) |
| Museum Mile, Frietomat, Canal (surface) | 7.5% each |

Museum Plein at 20% correct: Frietomat 31 / Canal 23, and 6.7% for each of the four Centraal-side exits. **Roodelicht Row (or Frietomat on the Museum sign) stays the likeliest wrong exit**, as N2 requires (`voetgangerstunnel.md:145`).

**Rejected alternatives:**
- **(B) Teleport replaces the roll outright, e.g. 25% before rolling.** This breaks the 10% floor: Centraal falls to 7.5%.
- **(C) Teleport to a random intersection inside the tunnel.** This needs an intersection graph nobody has built, and it can loop.
- **(D) Teleport anywhere in Shamsterdam.** This leaves N5's scope and risks dropping the party into gated or unbuilt locations.

**Expected clock cost per intersection with T2-T5** (Centraal, Space Cake only): 10 + 0.9 × 0.5 × 30 ≈ 23.5 min. A 90-minute Gamble therefore covers about 4 intersections after the walk to the tunnel.

---

## 5. Proposed data (for `game/assets/data/skills/status_effects.json`, after approval)

```json
"contact_high":     {"section": "negative", "scope": ["field"], "bearer": "bro",
                     "default_duration": {"clock_minutes": 30, "ends_on_rest": true, "until_cured": false},
                     "stack_rule": "refresh", "cured_by": [{"kind": "rest"}]},
"space_cake_timer": {"display_name": "Space Cake Timer", "section": "neutral", "scope": ["field"], "bearer": "bro",
                     "default_duration": {"clock_minutes": 120, "ends_on_rest": true, "until_cured": false},
                     "stack_rule": "none", "then": {"status": "space_cake_gamble", "stacks": true}},
"space_cake_gamble":{"section": "negative", "scope": ["field"], "bearer": "bro",
                     "default_duration": {"clock_minutes": 90, "ends_on_rest": true, "until_cured": false},
                     "stack_rule": "extend", "cured_by": [{"kind": "rest"}]}
```

Teleport numbers go in `game/assets/data/navigation/voetgangerstunnel.json`: `"teleport": {"status": "space_cake_gamble", "chance_on_wrong": 50, "lost_minutes": 30}`. The confusion-cure `item_id` joins Contact High's `cured_by` only once that item is ruled.

---

## 6. Intoxication law §8: 10-point review

| # | Point | Contact High | Space Cake Gamble |
|---|---|---|---|
| 1 | Source | De Groene Gids interior; Coffeeshop Quarter tunnel exit (30%); couchsurf payoff (CH1-CH3) | Space Cake (8 SOVS) and "Shamsterdam Dream", through the 120-minute Space Cake Timer (SC1-SC4) |
| 2 | Immediate effect | −15 Navigation, party-wide | Nothing for 120 minutes. Then +40 Bravado, the onset wobble, −30 Navigation and teleports |
| 3 | Escalation | None. It refreshes and never deepens (CH8). It adds with other penalties toward the 10% floor (base-odds spec §3 row 19) | More cakes mean a longer high (90 each, cap 180) and more Bravado, but never a deeper penalty (SC10) |
| 4 | Player-facing cues | Contact High Indicator icon (`De_Groene_Gids_PNG_Assets.md:355`); the shop haze | Timer UI and the "It's Not Working" unlocks; rings, warp vignette and "OH." frame; the pitch-bent music bed; warp-covered teleport cuts |
| 5 | Player control | None lost. The player still picks every direction | The player still picks the direction. 15 real seconds of reversed movement at onset (SC6, separable). Teleport changes only *where* a wrong turn lands; the 10% floor holds (T2) |
| 6 | Duration and recovery | 30 clock min after the last exposure; rest; the confusion cure if ruled | 120 min wait, then 90 min (cap 180); rest ends both and clears an unlanded timer. Saved in `FieldStatus` rows, so save/load is consistent |
| 7 | Comedic consequence | The bros walk out of the haze relaxed and convinced they know the way, and come up between two red windows | The bros decide it isn't working, buy another, and two hours later the tunnel spits them out at Frietomat with half an hour missing. What they think they get is +40 Bravado; what they get is the floor moving (bros_choose_debauchery.md:24) |
| 8 | Interactions | Adds with Space Cake, Grist, Canal/Tunnel Confusion; clamp last. Does not end Sober. Distinct from battle `confused`, Green Fairy Confusion, Nicotine Contact High | Same additive rule. Does not end Sober. Teleports count as wrong turns toward Tunnel Confusion (T4). Not carried into battle |
| 9 | Technical dependencies (proposed engineering) | `FieldStatus.apply_from_table` already applies clock rows. Needs: a per-screen apply hook for De Groene Gids (no scene exists yet); `stack_rule: refresh` honoured on clock rows; the 30% check on the Coffeeshop Quarter exit in `NavigationRoll` | Needs: the Space Cake purchase applying `space_cake_timer`; **clock rows firing `then` on expiry** (today `_fire_then` runs only for steps and battle expiry, `field_status.gd:269`, `:344`, and clock rows expire lazily); `then` read from the status table, not only from the row; a stack count on the timer for SC10, and a cap; the landing hook (Bravado, cue, wobble); `NavigationRoll` teleport step (T2-T5); rest clearing the timer. All belong to one gameplay-programmer bead after approval |
| 10 | Further author approval | CH1-CH10 | SC1-SC14, T1-T7. SC6 and T5 can be dropped on their own. Lines and flavor text come from a writing round, not this spec |

Neither status lectures, warns or explains. The bros eat the cake willingly, complain it isn't working, and take the consequence without being scared of it. That consequence is the satire.

---

## 7. Found work filed (not decided here)

- The Coffeeshop Quarter "confusion cure" has no item doc, name or price (CH9).
- The Munchies has no status entry or numbers (SC13).
- De Groene Gids UI sizes disagree: Timer UI is 128x32 at `de_groene_gids.md:370` but 192x64 at `De_Groene_Gids_PNG_Assets.md:345`; Munchies icon is 64x64 at `:374` but 48x48 at `:356`.

## 8. If approved

1. Record the ruling in `docs/superpowers/NEXT_WORK.md`, `voetgangerstunnel.md` (Navigation Mechanics and Coffeeshop Quarter Emergence) and `de_groene_gids.md` (Status Effect Application, "Is It Working Yet?" System).
2. Write the §5 entries and point the `_pending` notes at the ruling.
3. File the gameplay-programmer bead for §6 point 9, and the Navigation teleport tests.
