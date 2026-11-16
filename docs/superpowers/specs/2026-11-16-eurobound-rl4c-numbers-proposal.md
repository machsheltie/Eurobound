# Combos Starter Set: Numbers Proposal (Eurobound-rl4c)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-rl4c-q2`).
> Author's route, verbatim (bead page, 2026-11-16): "An agent proposes numbers for a small starter
> set from battle_system.md, the way the v26 battle numbers were done, for my approval".
> Method and format copy round v26 (`design/mechanics/Battle/battle_numbers_proposal.md`).
> Nothing in `game/` or `design/` was changed. Every combo name below is already in
> `design/mechanics/Battle/battle_system.md`; no names or lines were written.

## 1. Already decided by the docs (used as written)

| Rule | Source |
|---|---|
| A Combo is a **main action** (Attack, Skill or Combo) | battle_system.md:8, v26 §1 |
| Triggers: same target, compatible skills, gear | battle_system.md:16-19 |
| Resolves in turn order, like Chrono Trigger dual and triple techs | battle_system.md:22 |
| Success rate by Bravado: **High 80%, Medium 60%, Low 40%** | battle_system.md:315-317 |
| Backfires: self-damage, Bravado drain, Embarrassed | battle_system.md:25-28 |
| Beeramid: needs Pilsner at High Bravado, **3× damage to all enemies**, **all enemies Stunned 1 turn**, **+2 Bravado to both**; backfire: both hurt and Embarrassed | battle_system.md:320-324 |
| Like & Subscribe: Bradley's hit **2× damage**, **25% "viral crit"**; backfire "0 viewers", Bradley loses Bravado | battle_system.md:128-130, :201 |
| Viral crit size: **4× damage** | battle_system.md:331 (Viral Moment) |
| Who Flexed Harder?: both roll crit checks, winner deals extra damage, loser loses Bravado; crowd boos → both Embarrassed | battle_system.md:91-94, :177-179 |
| v26/v27 numbers: damage formula, thirds, ±2 spread, SMAAAASH, Flex +3, Stun does not stack, Embarrassed 2 turns, Embarrassed locks Bravado-cost moves and Ultimates | NEXT_WORK.md rounds v26-v28 |

## 2. Rules every combo uses (the gaps)

| Id | Gap | Proposed value | Anchored to |
|---|---|---|---|
| rl4c_start | How a combo starts. The engine plays one fighter's turn at a time and has no declare phase (`game/battle/battle_core.gd:8`, `_new_round`), so "both bros declare, system prompts" cannot happen as written | A **Combo** entry in the main-action menu. It lists the combos whose partners are alive, not Stunned, not Embarrassed, and have not taken their main action this round. Choosing one spends **every participant's turn** this round and resolves at once | battle_system.md:22 (dual techs need every participant ready). The menu entry is the "prompt" |
| rl4c_roll | How success is rolled | **One roll per combo.** The tier is the participants' *combined* Bravado (sum of current over sum of max) on the v26 thirds: High 80%, Mid 60%, Low 40% | battle_system.md:315-317; v26 thirds apply game-wide (v27) |
| rl4c_fail | What a failed roll does | **A failed roll is that combo's backfire**, at every tier. No separate fizzle | battle_system.md:39 (Low Bravado "increase backfire odds") and :25 |
| rl4c_cost | Bravado cost | **None.** The doc names none; Bravado works through the success roll and the damage formula | battle_system.md:23 ("synergy bonuses scale with current Bravado") |
| rl4c_embarrassed | Embarrassed bros | **Cannot start or join a combo** (greyed out) | v27: Embarrassed locks Bravado-cost moves and Ultimates; battle_system.md:68 (an Embarrassed bro makes the chant fall apart) |
| rl4c_damage | Damage | The named striker's **normal formula** (ATK + Bravado Mod − DEF) × the combo multiplier, ±2, minimum 1. **No separate 95% to-hit roll** (the success roll replaces it). SMAAAASH applies as usual except where a combo has its own crit | v26 formula; avoids failing twice for one action |
| rl4c_self_damage | Size of backfire self-damage | **5 HP** to each participant who is hurt | A light hit from Croc Monsieur on Bradley: (9 − 2) × 0.7 = 4.9 |
| rl4c_drain | Size of a backfire Bravado loss | **3 Bravado** | One Flex (v26 ef3_flex) |
| rl4c_embarrassed_len | Backfire Embarrassed length | **2 turns** | v28 default |
| rl4c_slice | Are Combos in the first slice? | **Yes, the three below, open from the start**, so the Combo command can be tested in Debaucheryville. Later combos open on Clout rungs (Eurobound-028k), at thresholds the author sets | 028k ("Clout for moves") |

## 3. The starter set (three combos)

None of the three needs a move that does not exist yet: they all use Attack.

| Id | Combo | Proposed value | Anchored to |
|---|---|---|---|
| rl4c_beeramid | **Beeramid** (Bradley + Pilsner). Needs Pilsner at **High** Bravado | Success: **Bradley's Attack ×3.0 on every enemy**, **every enemy Stunned 1 turn**, **+2 Bravado to both**. Backfire: **both take 5**, **both Embarrassed 2 turns** | All from battle_system.md:320-324, plus §2 sizes |
| rl4c_like_subscribe | **Like & Subscribe** (Chadwick + Bradley). One enemy | Success: **Bradley's Attack ×2.0**. **25% of successes go viral: ×4.0** instead, and that hit does not also roll SMAAAASH (no ×8). A viral hit gives **each living bro 1-3 Bravado** at random. Backfire ("0 viewers"): the attack fizzles, **Bradley loses 3 Bravado** | battle_system.md:63, :129-130, :201, :331. 1-3 averages the +2 crowd gain of Beeramid and is capped at one Flex |
| rl4c_flex_harder | **Who Flexed Harder?** (Bradley vs Chadwick). One enemy | Success: winner picked by the crit check, **chance in proportion to each bro's crit %** (Luck, +10 at High). **Winner: a hit at ×2.5 and +3 Bravado. Loser: −3 Bravado.** Backfire (crowd boos): **both Embarrassed 2 turns** | battle_system.md:91-94, :372-374 ("winner gets massive damage bonus and Bravado"). ×2.5 matches Keg Smash's proposed "huge" size (Eurobound-g0jr proposal) |

## 4. Sanity check (Croc Monsieur: 52 HP, Off 9, Def 6; v26 reference fight)

Expected values, before spread and crit. Bravado mods: Bradley High +7 / Mid +3; Chadwick High +10 /
Mid +5; Pilsner High +6. "Separate" is what the same bros do with two plain Attacks.

| Combo | Tier | Combo result | Expected (with success roll) | Separate Attacks |
|---|---|---|---|---|
| Beeramid | High | 13 × 3 = **39** to every enemy + Stun | 31 + Stun 80% of the time | 8 + 13 = 21 |
| Beeramid vs three Palette Swaps (16 HP, Def 2) | High | 17 × 3 = 51 each: clears the screen | | |
| Like & Subscribe | High | 26, viral 52 | 0.8 × 32.5 = **26** | 13 + 10 = 23 |
| Like & Subscribe | Mid | 18, viral 36 | 0.6 × 22.5 = **13.5** | 9 + 5 = 14 |
| Who Flexed Harder? | High | Bradley wins 48%: 33; Chadwick wins 52%: 25 | 0.8 × 28.9 = **23** | 23 |

Reading: Like & Subscribe pays a little at High and breaks even at Mid, so it rewards keeping Bravado
up. Who Flexed Harder? is a coin flip worth the same damage as attacking, plus a 6-point Bravado swing
between the two. **Beeramid is the strongest action in the game against groups**, as the doc says
("massive AoE nuke"). It is held back only by Pilsner needing High Bravado and by the 20% backfire. If
that is too strong, the note box can cut the multiplier for enemies other than the target.

## 5. Left out of the starter set, and why

- **Alpha Sigma Slam / Alpha Sigma Thunder** (all three): needs "combined Bravado > 150" (:334), off the
  current scale (the bros' maxes add up to 46), and full Bravado restore, which needs its own numbers.
- **Double Chug** (and Double Chug Disaster): built on drinking. It needs the 10-point review in
  `design/mechanics/intoxication_law.md` first (no intoxicant gives a free advantage).
- **Selfie Block / Selfie Sabotage**: always backfire. Whether the player chooses these or they happen
  to the bros is a design question for the author.
- **Wingman Protocol**: needs a "charmed" status and humanoid enemy tags, which are not in the data.
- **Bros Before Heroes**: two different versions (:86-88 and :359-363).
- **Toast vs. Post, Flex-Off, Who's The Alpha?, Tag Team Supreme, Spotlight Clash**, the regional and gear combos
  (Casino Royale needs boss enrage and spawn rules that do not exist), the Ego meter and the
  "Snap Out of It" recovery: later rounds.

## 6. Conflicts and gaps (author picks)

- **Like & Subscribe backfire:** battle_system.md:64 says Chadwick loses Bravado; :130 and the Combo
  Bible table at :201 say Bradley does. This proposal follows the table (Bradley).
- **Beeramid's two versions:** :58-59 ("High Bravado → massive AOE damage, bonus Bravado gain") and
  :320-324 (3× AoE, Stun all, +2 Bravado both). The second is used because it has numbers.
- **Battle text:** combo lines, the "0 viewers" overlay and the Insta poll overlay are not written.
  They go to the Writers' Room after approval.
- **Build:** the Combo command, partner checks, AoE party hits and the success roll are all new
  code (`battle_core.gd` has no combo action). A build bead follows the ruling.
