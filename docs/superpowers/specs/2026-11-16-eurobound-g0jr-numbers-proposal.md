# First Signature Moves: Numbers Proposal (Eurobound-g0jr)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-g0jr-q2`).
> Author's route, verbatim (bead page, 2026-11-16): "An agent proposes numbers for each bro's first
> signature move from battle_system.md, for my approval".
> Method and format copy the round v26 battle numbers (`design/mechanics/Battle/battle_numbers_proposal.md`).
> Nothing in `game/` or `design/` was changed. No move names or battle text were written: every
> name below is already in `design/mechanics/Battle/battle_system.md`.

## 1. Already decided (used as written)

| Rule | Source |
|---|---|
| Base Damage = (ATK + Bravado Modifier) − DEF, ×move multiplier, ±2 spread, minimum 1 | battle_system.md:36, round v26 |
| Bravado tiers: Low below 1/3 of max, High at 2/3 or more. Modifier: High + half max, Mid + a quarter, Low −2 | round v26 (BattleRules) |
| SMAAAASH crit: Luck %, +10 at High, − half target Grit, at least 1%; doubles damage | round v26 |
| Damage words: light ×0.7, standard ×1.0, moderate ×1.2, heavy ×1.5. Base hit 95% | round v27 (BattleRulings) |
| Gains Bro = +20% ATK. Stun = lose the next turn, does not stack. Embarrassed locks every Bravado-cost move | round v27 |
| Roast Line (Lord Pilsner): 4 Bravado, ×1.8, spoken | round v26, Eurobound-uwrw-q1 |
| Each ability is tagged spoken or not, one by one | Eurobound-64vo-q5 |
| XP levels raise stats; Clout rungs open moves | Eurobound-028k-q1 |
| Bros: Pilsner HP 45, Brav 12, Off 8, Def 6, Spd 5, Luck 4. Chadwick HP 35, Brav 20, Off 6, Def 3, Spd 7, Luck 6. Bradley HP 30, Brav 14, Off 12, Def 2, Spd 8, Luck 5 | `game/assets/data/party/party_members.json` (v26) |

**Engine fact that sets the costs:** `BattleCore.use_skill` takes the Bravado cost *before* the hit
(`game/battle/battle_core.gd:434`), so the damage uses the tier the bro is in *after* paying. Every
figure below accounts for that.

## 2. Which move is "first"

The first Core Ability listed for each bro in battle_system.md:

| Bro | First Core Ability | battle_system.md | Doc's description |
|---|---|---|---|
| Bradley | Keg Smash | :224 | "Single target, huge damage, drains Bravado." |
| Chadwick | Like & Hype | :243 | "Buff ally attack; viral chance gives crit bonus." |
| Lord Pilsner | Beer Belly Bash | :261 | "Stuns enemies with belly slam." |

Pilsner already starts with Roast Line. Beer Belly Bash is included because the author asked for
*each* bro; strike row P if Pilsner should start with Roast Line only.

## 3. Proposed values

| Id | Move | Proposed value | Anchored to |
|---|---|---|---|
| g0jr_B_cost | Keg Smash (`keg_smash`), Bradley | **5 Bravado** | Just over 1/3 of his 14 bar, so one cast from a full bar drops him from High to Mid: "drains Bravado" (battle_system.md:224) and "burns Bravado for massive spikes" (:216). Roast Line costs 4 of Pilsner's 12 |
| g0jr_B_mult | Keg Smash | **×2.5**, physical, one enemy, no extra effect | Above Roast Line ×1.8 and "heavy" ×1.5, because the doc says "huge". It gives Bradley the same lift over his own best Attack that Roast Line gives Pilsner (×1.77 vs ×1.75, see §4) |
| g0jr_B_spoken | Keg Smash | **not spoken** (Cottonmouth does not block it) | It is a smash, not a line. Needs the author's tag under 64vo-q5 |
| g0jr_C_cost | Like & Hype (`like_and_hype`), Chadwick | **4 Bravado** | Same as Roast Line. 4 of 20 is the cheapest share in the party, matching "Bravado Pool High, regenerates easily" (:241) |
| g0jr_C_effect | Like & Hype | **One other bro gets Gains Bro (+20% ATK) for 3 of his turns.** No damage. Recasting resets it to 3; it does not stack | Gains Bro is the existing +20% ATK status (v27, `BattleRulings.GAINS_BRO_ATK`, already applied to bros in `battle_unit.gd:159`). 3 turns matches the other timed party buffs in the doc (Influence Aura "for 3 turns", :287) |
| g0jr_C_viral | Like & Hype, "viral chance" | **25% chance** the buffed bro also gets **+10 crit %** for the same 3 turns | 25% is the doc's own viral chance (Like & Subscribe, :129 and :201). +10 is the size of the High-Bravado crit bonus (v26 ef3_crit) |
| g0jr_C_target | Like & Hype | **Any living bro except Chadwick** | The doc says "ally" (:243); "his buffs are strongest when someone else is in spotlight" (:250) |
| g0jr_C_spoken | Like & Hype | **spoken** (Cottonmouth blocks it) | Bro-Mancy is "motivational yelling" (:235). Needs the author's tag under 64vo-q5 |
| g0jr_P_cost | Beer Belly Bash (`beer_belly_bash`), Pilsner (optional, row P) | **3 Bravado** | Below Roast Line's 4: "Pilsner: Low Bravado use" (:304) |
| g0jr_P_mult | Beer Belly Bash | **×1.0** (standard), physical, one enemy | It is a control move, not his damage move (Roast Line is) |
| g0jr_P_stun | Beer Belly Bash | **40% chance of Stun (1 turn)**, then a **3-turn cooldown** | 40% is the status chance the villain docs already use most (Is This Your Lane, EXTRA CRISPY!, Maybe You're the Problem, Confusion Breath: all 0.4). The cooldown copies GET IN THE PITA's 3 (Condiment Clan Ninja). Without it, Pilsner could Flex (+3) and Bash (−3) every turn and stun-lock a villain. Shish Kahn's and Vratislav's 50% stun resist still applies |
| g0jr_P_spoken | Beer Belly Bash | **not spoken** | A belly slam. Needs the author's tag under 64vo-q5 |
| g0jr_unlock | All three | **Starting kit**, like Roast Line (v26 ef3_starting_moves), so no Clout rung | Clout rungs open *later* moves (028k). Their thresholds are the author's numbers and are not proposed here |
| g0jr_ultimates | When Ultimates arrive | **Not in the Debaucheryville slice.** Each bro's Ultimate opens on a Clout rung, and its numbers come in a later round, once the Clout rungs are ruled | 028k: Clout opens moves. ability_template.md already requires Mid Bravado or more for an Ultimate. See §5 for the name conflict that must be settled first |

## 4. Sanity check (Croc Monsieur: 52 HP, Off 9, Def 6; v26 reference fight)

All figures are expected values before the spread and the crit. In the cabinet fight the Croc has
78 HP (+50%) and 25% physical resist, which takes a quarter off every row below.

| Action | Bravado before → after | Tier used | Damage |
|---|---|---|---|
| Bradley Attack | 14 | High (+7) | (12+7−6) = **13** |
| Bradley Keg Smash | 14 → 9 | Mid (+3) | (12+3−6)×2.5 = **23** (×1.77 his best Attack) |
| Bradley 2nd Keg Smash | 9 → 4 | Low (−2) | (12−2−6)×2.5 = **10** |
| Pilsner Attack | 12 | High (+6) | (8+6−6) = **8** |
| Pilsner Roast Line (for comparison) | 12 → 8 | High (+6) | 8×1.8 = **14** (×1.75 his best Attack) |
| Pilsner Beer Belly Bash | 12 → 9 | High (+6) | **8**, 40% Stun |
| Bradley Attack with Like & Hype | 14 | High (+7) | (14+7−6) = **15** (+2 a hit for 3 turns) |
| Bradley Keg Smash with Like & Hype | 14 → 9 | Mid (+3) | (14+3−6)×2.5 = **28** (+5) |
| Chadwick Attack (what Like & Hype costs him) | 20 | High (+10) | (6+10−6) = **10** |

Reading: Bradley can land about three strong Keg Smashes with a Flex each turn (net −2 Bravado a
turn), then he is at Low and slapping for 10. That is the "burn then slump" the doc describes. Like &
Hype on Bradley returns about 6-15 damage over three turns, against the 10 Chadwick would have done
himself, so it pays only when he buffs the cannon. Buffing Pilsner returns about +6. Nothing here
outdamages Bradley.

## 5. Conflicts between docs (author picks)

- **g0jr_conflict_ultimates.** battle_system.md:283/:291/:299 names the Ultimates Fratocalypse Now
  (Bradley), Going Viral (Chadwick) and Final Round's On Me (Pilsner). party.md and bravado.md:52/:57/:62
  name them Bouncer Breaker, Viral Meltdown and Mid-Life Crisis. No Ultimate can be numbered until the
  author picks a list. Filed as its own bead (see the session report).
- **Beer Belly Bash.** battle_system.md:261 says it stuns; bravado.md:51 says "damage + knockback".
  This proposal follows battle_system.md, as the author asked. The engine has no knockback.

## 6. Gaps this proposal cannot fill

- **Battle text.** `party_abilities.json` needs a `battle_text` line for each move, and the ability
  template needs success and failure lines. None exist and none were written. They go to the Writers' Room
  once the numbers are approved.
- **Failure states.** battle_system.md gives these three moves no fail case, so none is proposed.
- **Build needs** (for the build bead after approval): skills that target an ally, apply a status
  with a chance, carry a cooldown, and grant a crit bonus to the user's side. Today `use_skill` only
  deals damage (`battle_core.gd:430-438`).
