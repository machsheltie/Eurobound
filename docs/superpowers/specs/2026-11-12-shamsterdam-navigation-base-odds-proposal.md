# Proposal: base odds for Shamsterdam's Navigation roll

**Status: PROPOSED, awaiting the author (Eurobound Desk `Eurobound-76gz-q1`).** No canon doc, data file or code has changed.
**Bead:** Eurobound-76gz. **Engine follow-on:** Eurobound-eggq (blocked on this ruling).
**Author answer that ordered this (bead page, 2026-11-12), verbatim:** "Have a systems designer propose base odds for my approval".
**Already ruled (eb8, Eurobound Desk eb8-q1, "Approve as proposed"), not reopened here:**
- Modifiers add as percentage points on the correct-exit chance.
- The chance is clamped to **10%-90%**.
- Sober (+20) ends with the party's first `alcohol: true` drink and returns at the next rest.

Sources: `design/worlds/shamsterdam/voetgangerstunnel.md:120-137` (the check) and `docs/superpowers/specs/2026-11-12-grist-genever-review-numbers-proposal.md` §5 (A12 clamp precedent, A16 table).

---

## 1. What canon already has

**The check (`voetgangerstunnel.md:122-126`):** at each intersection the player picks a direction from the signage, and a probability roll decides where the party actually ends up.

**The exit table (`voetgangerstunnel.md:46-56`)** already gives unmodified odds for each sign:

| Sign followed | Correct exit | Wrong exits |
|---|---|---|
| "Centraal Station" | Centraal Chaos **40%** | Roodelicht Row 35%, Coffeeshop Quarter 15%, Where you started 10% |
| "Museum Plein" | Museum Mile **50%** | Frietomat 30%, Canal (surface) 20% |

The modifier table (L129-137) never refers back to this exit table. That is why the bead found no base: the base is already sitting in the exit table, but nothing links the two.

**Every modifier in canon** (additive points; clamp 10-90):

| Modifier | Points | Source |
|---|---|---|
| Sober | +20 | `voetgangerstunnel.md:131` (eb8) |
| Map item equipped (e.g. Survival Map) | +15 | `:135`; `bicycle_warfare_accessories.md:154` |
| Local Guide NPC (10 SOVS) | +40 | `:136` |
| Each earlier success | +5, cumulative | `:137` |
| Opa Cees's Blessing | +5 | `shamsterdam_bike_rental.md:379`, `:408` |
| Tunnel Vision (perfect run, 1 hour) | +10 | `voetgangerstunnel.md:438-441` |
| Underground Navigator (5 successes, permanent, tunnels) | +5 | `voetgangerstunnel.md:443-445` |
| Contact High | −15 | `:132` |
| Tunnel Confusion | −15 | `:424-427` |
| Windmill Grist | −20 | `NEXT_WORK.md:680` |
| Canal Confusion | −25 | `:134` |
| Space Cake Gamble | −30 | `:133` |

---

## 2. Proposal (every value PROPOSED)

| Id | Rule | PROPOSED value | Anchor / reason |
|---|---|---|---|
| N1 | **Base correct-exit chance** | **The correct row of the sign's exit table: 40% for "Centraal Station", 50% for "Museum Plein".** | It uses odds the author already approved in the location doc instead of adding a number that would contradict them. Both sit at or just under the approved Run base of 50% (`design/mechanics/Battle/battle_numbers_proposal.md:35`), the only other approved coin-flip in the game. A tunnel designed to filter out tourists (`voetgangerstunnel.md:20`) should not be kinder than running from a fight |
| N2 | **Wrong exits** | **The remaining chance (100 − correct) is shared among that sign's wrong exits in their listed proportions**, rounded to whole percents by largest remainder (ties go to the higher row in the table). Roodelicht Row stays the likeliest wrong exit at every level | It keeps the exit table's comedy weighting at every modifier level (§4) |
| N3 | **Order** | base + every active modifier → clamp to 10-90 → roll | eb8 |
| N4 | **"Each earlier success" (+5)** | **Counts successes within the current tunnel visit and resets when the party leaves the tunnel.** Underground Navigator (+5, permanent) is the lifetime reward | The doc does not say which it is. A lifetime count would push every roll to the 90 cap after about 8-10 successes and make Underground Navigator pointless. The other option, a lifetime count, is shown in §3 row 9 |
| N5 | **Scope** | This base covers the Voetgangerstunnel roll, the only Navigation roll canon defines. Opa Cees's Blessing and Tunnel Confusion say "in Shamsterdam", but no other roll exists. Any future roll gets its base from its own exit table or from the author | No invention of new rolls |

**The rejected alternatives:**
- **(B) Flat 50% for every sign:** simple, and it matches the Run base. But it overwrites the authored Centraal row (40%), and Centraal is where the Roodelicht Row joke lives.
- **(C) Flat 40%:** harsher. Space Cake Gamble alone then hits the floor on every sign, so the floor stops meaning anything special.

---

## 3. Resulting odds in each modifier case (N1, clamp 10-90)

"Drunk" means Sober is gone (any alcoholic drink since the last rest). Unclamped values are in brackets.

| # | Case | Centraal (base 40) | Museum Plein (base 50) |
|---|---|---|---|
| 1 | Drunk, nothing else | **40%** | **50%** |
| 2 | Sober | 60% | 70% |
| 3 | Drunk + map | 55% | 65% |
| 4 | Sober + map | 75% | 85% |
| 5 | Sober + map + Opa Cees + Underground Navigator | 85% | **90%** (95) |
| 6 | Drunk + Local Guide | 80% | **90%** |
| 7 | Sober + Local Guide | **90%** (100) | **90%** (110) |
| 8 | Sober + Tunnel Vision | 70% | 80% |
| 9 | Sober + 2 earlier successes this visit | 70% | 80% |
| 9b | (lifetime-count reading) Sober + 6 lifetime successes + Underground Navigator | **90%** (95) | **90%** (105) |
| 10 | Contact High (drunk) | 25% | 35% |
| 11 | Tunnel Confusion (drunk) | 25% | 35% |
| 12 | One Windmill Grist (drunk) | 20% | 30% |
| 13 | Sober party drinks one Grist (eb8 example: −40 swing) | 60% → 20% | 70% → 30% |
| 14 | Canal Confusion (drunk) | 15% | 25% |
| 15 | Canal Courage Hungover, if Eurobound-c24-q3 is approved (Sober lost + Canal Confusion) | 15% | 25% |
| 16 | Space Cake Gamble (drunk) | **10%** | 20% |
| 17 | Grist + Tunnel Confusion | **10%** (5) | 15% |
| 18 | Canal Confusion + Tunnel Confusion | **10%** (0) | **10%** (10) |
| 19 | Space Cake + Contact High | **10%** (−5) | **10%** (5) |
| 20 | Grist + Canal Confusion + Tunnel Confusion + Space Cake | **10%** (−50) | **10%** (−40) |
| 21 | Hungover party pays the Local Guide (Canal Confusion + Guide) | 55% | 65% |
| 22 | Same, with a map | 70% | 80% |

**Expected tries to reach the signed exit** (1/p): 40% → 2.5; 60% → 1.7; 90% → 1.1; 10% → 10. The tunnel is an optional shortcut (`voetgangerstunnel.md:27`: "Alternative route with trade-offs"), and the surface route always works, so even the floor is a joke, not a softlock.

### Why these odds keep the modifiers and the floor meaningful

- **The cap is earned, not given.** No single permanent bonus reaches 90. Only the paid Local Guide, or Sober stacked with three or more bonuses, gets there (rows 5-7).
- **Every penalty is felt from the most common state (drunk):** −15 to −30 moves a coin-flip into "probably Roodelicht Row".
- **The floor is reached only by Space Cake on the harsher sign, or by stacking two or more penalties** (rows 16-20). It is the rare, stacked-disaster outcome, not the normal drunk state, which is what a 10% floor is for (Law §3: bounded, never impossible).
- **Paying for help is a real choice:** a hungover party that buys the guide climbs from 15% to 55% (rows 14 and 21).

---

## 4. Wrong-exit split at sample levels (N2)

| Sign | Correct | Wrong exits |
|---|---|---|
| Centraal (35:15:10) | 40% (as written) | Roodelicht 35 / Coffeeshop 15 / Start 10 |
| | 60% | 23 / 10 / 7 |
| | 75% | 15 / 6 / 4 |
| | 90% | 6 / 2 / 2 |
| | 10% | 53 / 22 / 15 |
| Museum Plein (30:20) | 50% (as written) | Frietomat 30 / Canal 20 |
| | 70% | 18 / 12 |
| | 90% | 6 / 4 |
| | 10% | 54 / 36 |

---

## 5. Intoxication-law 10-point review (where it applies)

The roll is not an intoxicant. It is where several intoxicants pay off: Sober lost, Windmill Grist, Contact High, Space Cake Gamble, and Canal Courage's Canal Confusion if c24-q3 is approved. Points 1-3 belong to those items' own reviews; the rest apply here.

1. **Source:** none of its own. The inputs are the drinks and drugs listed in §1.
2. **Immediate effect:** none of its own. It turns their points into one chance.
3. **Escalation:** Penalties add (eb8). More intoxicants mean worse odds, down to 10%.
4. **Player-facing cues:** the existing ones: Grist's "−20% Navigation" readout and Spin Meter vignette at intersections (eb8 §5 point 4), and Tunnel Confusion's question marks (`voetgangerstunnel.md:428`). **Proposed engineering:** show the final correct-exit chance at each intersection only while the map item is equipped. That makes the map's +15 visible, and it needs no new text beyond a percentage. This is a proposal; drop it if you prefer the roll hidden.
5. **Player control:** The player always picks the direction. Only the outcome is rolled, and the right exit is never impossible (10% floor).
6. **Duration and recovery:** No state of its own. Each modifier keeps its own duration, and per-visit successes reset on leaving the tunnel (N4).
7. **Comedic consequence:** The drunker the bros, the likelier they come up between two red-lit windows. The Roodelicht weighting holds at every level (N2).
8. **Status interactions:** Every §1 modifier adds; the clamp applies last.
9. **Technical dependencies (proposed engineering, not built):**
   - a Navigation roll at intersection triggers;
   - a per-sign exit table in data;
   - a modifier sum that reads `FieldStatus` (Sober, Grist, Contact High, Space Cake, Canal Confusion, Tunnel Confusion, Tunnel Vision), equipment (map), flags (Opa Cees, Underground Navigator) and a per-visit success counter;
   - the clamp, then a weighted pick over the wrong exits.
   Filed as Eurobound-eggq.
10. **Further author approval:** N1-N5. After sign-off, the ruling goes into `voetgangerstunnel.md` (the Navigation Mechanics section) and the ledger, and the engine bead unblocks.
