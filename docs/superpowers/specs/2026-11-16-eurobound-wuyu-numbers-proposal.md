# Taunt, Counter-Brags and Venue Turn Order: Numbers Proposal (Eurobound-wuyu)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-wuyu-q2`).
> Author's route, verbatim (bead page, 2026-11-16): "An agent proposes numbers for all three for my
> approval".
> Method and format copy round v26 (`design/mechanics/Battle/battle_numbers_proposal.md`).
> Nothing in `game/` or `design/` was changed. No names or lines were written.

## 1. Already decided by the docs (used as written)

| Rule | Source |
|---|---|
| Minor actions: Item use, **Taunt**, Bravado Flex. One minor action a turn | battle_system.md:9, v26 §1 |
| Wingman Shout "taunts enemies, forcing them to attack Chad": a taunt pulls attacks onto the taunter | battle_system.md:245 |
| **Counter-brags:** "Certain Bravado Styles unlock counter-brags. If an enemy tries to taunt Bradley, he can interrupt with 'Bro, Do You Even Lift?' to gain Bravado instead of losing it." | battle_system.md:10 |
| Embarrassed **disables Taunt** | game_design_document.md:14 |
| Turn order: Speed, with High/Low Bravado ±2 Speed | battle_system.md:3-4, v26 ef3_bravado_speed |
| **Venue turn order:** "In regions with strong cultural vibes (Publandia tavern chants, Sinfonia rave basslines), turn order may temporarily sync to NPC/environment beats. Example: all actions in Sinfonia drop in rhythm with the nightclub track." | battle_system.md:5 |
| Enemy "taunts" already in the data (moves with `bravado_drain`): Is This My Taunt or His? (3), They ALL Remember (3), Honk If You've Peaked (2, v27), The Truth (5) | `game/assets/data/enemies/debaucheryville_arcade_battle.json` |
| Social contest = Charm against Grit | v27 ef4_social_damage |

## 2. Taunt (minor action)

| Id | Gap | Proposed value | Anchored to |
|---|---|---|---|
| wuyu_taunt_effect | What a Taunt does | The bro taunts **one enemy**. If it lands, that enemy's **next move that targets a single bro must target the taunter**. Moves that hit everyone, moves on its own side, and moves written to always hit one named bro (Buy the Dip on Chadwick) are not changed | battle_system.md:245 (taunt = forcing attacks onto the taunter) |
| wuyu_taunt_chance | Chance it lands | **50%, +5% for each point the taunter's Charm beats the enemy's Grit, clamped 10%-90%** | The v26 Run formula's shape (50% ± 5% a point, 10-90); Charm vs Grit is the v27 social contest |
| wuyu_taunt_length | How long | **Until the end of that enemy's next turn** | Shortest length that does anything; a Taunt is a minor action |
| wuyu_taunt_stack | Two taunts on one enemy | **The latest Taunt wins** | No stacking, like Stun (v27) |
| wuyu_taunt_cost | Cost | **No Bravado.** It uses the minor action, so the bro gives up that turn's Flex (+3) or Item | v26: one minor action a turn |
| wuyu_taunt_embarrassed | Embarrassed | **An Embarrassed bro cannot Taunt.** He keeps his other minor actions (Flex, Item) | game_design_document.md:14. See §5 for the clash with battle_system.md:12 |

Taunt chances against current villains (Charm: Pilsner 9, Chadwick 10, Bradley 4):

| Enemy (Grit) | Pilsner | Chadwick | Bradley |
|---|---|---|---|
| Croc Monsieur (6) | 65% | 70% | 40% |
| Accounts Receivable (7) | 60% | 65% | 35% |
| Shish Kahn, Vratislav (8) | 55% | 60% | 30% |
| Hatchback, Ninja, Wisp (2) | 85% | 90% | 60% |

Reading: Chadwick is the best taunter, which matches Wingman Shout. Pilsner (HP 45, Def 6) is the one
who should take the hits, and he lands it well enough. Bradley taunting is a bad idea, which is his
character.

## 3. Counter-brags (reaction)

| Id | Gap | Proposed value | Anchored to |
|---|---|---|---|
| wuyu_cb_who | Who has one | **Bradley only: "Bro, Do You Even Lift?"**, from the start. Chadwick and Pilsner have no counter-brag in the docs, so none is proposed | battle_system.md:10. Starting kit like Roast Line (v26). The alternative is a Clout rung (028k), whose threshold would be the author's number |
| wuyu_cb_trigger | What sets it off | **Any enemy move with a Bravado drain that hits Bradley**, single-target or all (the four moves in §1) | battle_system.md:10 ("if an enemy tries to taunt Bradley"). In the data, enemy taunts are the Bravado drains |
| wuyu_cb_chance | Chance | By Bradley's Bravado tier: **High 40%, Mid 30%, Low 20%** | Half the combo success rate for the same tier (battle_system.md:315-317: 80/60/40), because a counter-brag costs no action |
| wuyu_cb_effect | Effect | Bradley **gains the Bravado he would have lost** (up to his max). Any damage the move deals still lands (The Truth) | battle_system.md:10 ("gain Bravado instead of losing it") |
| wuyu_cb_input | Button or automatic | **Automatic**, no prompt | The engine has no reaction prompts; EarthBound-style battles do not stop for input mid-enemy-turn |
| wuyu_cb_blocks | When it cannot fire | **Not while Embarrassed or Stunned** | Same rule as Taunt (game_design_document.md:14); a Stunned bro is not acting |

Expected value: against Is This My Taunt or His? (3) at Mid, Bradley's average swing is
0.3 × (+3) + 0.7 × (−3) = −1.2 Bravado instead of −3. It softens taunts; it does not cancel them.

## 4. Venue turn order (Environmental Overrides)

| Id | Gap | Proposed value | Anchored to |
|---|---|---|---|
| wuyu_beat_reading | What "sync to the beat" means | **Timing, not order.** In a venue marked as a beat venue, each action's animation waits for the next beat of the venue's track. **Who acts when stays Speed + Bravado (v26)**, so no balance number moves | battle_system.md:5's own example: "all actions in Sinfonia drop in rhythm with the nightclub track" |
| wuyu_beat_wait | Longest wait | **One beat** (0.5 s at 120 BPM). The tempo comes from the venue's track | Keeps fights from feeling slower than the rolling HP meter (10 HP a second, v26) |
| wuyu_beat_where | Which venues | **None in Debaucheryville**, so nothing is built for the first slice. The flag goes on Publandia tavern and Sinfonia club battles when they are built | battle_system.md:5 names only Publandia and Sinfonia |

If the author wants the beat to change **who acts first**, the note box should say how, and an agent
will number that reading. This proposal does not invent one.

## 5. Conflicts and gaps (author picks)

- **What Embarrassed takes away:** battle_system.md:12 says "Embarrassed: lose minor action".
  game_design_document.md:14 says it "disables Taunt". v27 approved the villain-doc Embarrassed (−20% ATK,
  −2 Bravado a turn, locks Bravado-cost moves), which takes no minor action. This proposal uses the GDD
  (Taunt only), because it is the smallest change to what is built.
- **Liquid Confidence "+Taunt"** (bravado.md:22, party.md:114): Liquid Confidence is not in the status
  data, and any number on it needs the intoxication_law.md 10-point review. Not proposed.
- **Cottonmouth and Taunt:** Cottonmouth locks spoken *Bravado* skills; Taunt costs no Bravado. Whether
  a Taunt is blocked when the bro has Cottonmouth needs its own tag (64vo-q5). Not proposed.
- **"Dance/rhythm moves deal more if timed to the beat"** (battle_system.md:46): no such moves exist yet.
  Out of scope.
- **Battle text:** the counter-brag's line and Taunt lines are not written; they go to the Writers' Room
  after approval.
- **Build:** a Taunt minor action, a taunt redirect in enemy targeting (`battle_core.gd` `_move_targets`),
  and the counter-brag check when a `bravado_drain` resolves. A build bead follows the ruling.
