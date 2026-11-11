# Battle Numbers (APPROVED, round v26, 2026-11-11)

> **Status: APPROVED.** The author approved every ef3_ item in round v26 (2026-11-11) and picked
> battle_system.md for ef3_roles (Lord Pilsner is the tank, Bradley the glass cannon). Round v27
> (ef4_) then approved the values the villain docs needed on top of these: damage words, accuracy,
> Social damage, status definitions, Stun/Confused, the Honk drain, short weight tables, the Full
> Crossing lock, summed tickets, 1 HP after a won fight, the Street Fighter level band, the thirds
> as Bravado bands game-wide, lasting statuses, the soggy-pile refund, and Jarmila's defeat counter.
> Built in `game/battle/` (BattleRules = v26, BattleRulings = v27).

## 1. Already decided by the docs (built as written)

| Rule | Source |
|---|---|
| Turn order by Speed (standard JRPG initiative); Bravado can push Speed up (high) or down (low) | battle_system.md, Turn Order |
| Each bro gets **one main action** (Attack, Skill, Combo) and **one minor action** (Item, Taunt, Bravado Flex) per turn | battle_system.md, Action Economy |
| **Base Damage = (ATK + Bravado Modifier) − DEF**. High Bravado = bonus damage and a big crit chance; low Bravado = a penalty | battle_system.md, Damage & Effect Formulas |
| Crits are **SMAAAASH**; Luck raises crit chance; Grit resists crits | game_design_document.md, villain docs |
| **Rolling HP meter** (EarthBound): damage rolls the meter down over time, so a bro hit for lethal damage can still act if the fight ends first | game_design_document.md, Synopsis.md |
| Zero Bravado: no collapse; signature moves and Ultimates lock out, basic attacks only | bravado.md |
| Villain AI: data-driven weighted-random moves, telegraphed big moves, vulnerability windows (each villain's move table gives the multipliers and weights) | villain_template.md, the nine Arcade villain docs |
| Lose an Arcade cabinet fight: back at that cabinet, 1 HP, tokens spent | ruling ef_arcade_loss |

## 2. Gaps: the docs name the rule but give no number

| Id | Gap | Proposed value |
|---|---|---|
| ef3_bravado_tiers | Where Low / Mid / High Bravado start | Low below 1/3 of max Bravado, High at 2/3 and above, Mid between |
| ef3_bravado_modifier | Size of the Bravado Modifier in the damage formula | High: + half max Bravado. Mid: + a quarter of max Bravado. Low: −2. (Pilsner, max 12: +6 / +3 / −2) |
| ef3_damage_floor_spread | Random spread and minimum hit | ±2 spread, a hit always does at least 1 |
| ef3_crit | Crit chance and SMAAAASH size | Crit % = Luck + 10 at High Bravado − half the target's Grit, at least 1%. SMAAAASH doubles the damage |
| ef3_bravado_speed | How much Bravado moves Speed | High +2 Speed, Low −2 Speed |
| ef3_flex | Bravado Flex (minor action) | Restores 3 Bravado |
| ef3_rolling_hp | How fast the HP meter rolls | 10 HP a second |
| ef3_run | Run chance (the docs have none) | 50%, +5% for each point the party's average Speed beats the enemies' (10% to 90%). Running from a cabinet fight: tokens stay spent, HP kept, bros back at the cabinet |
| ef3_party_stats | Chadwick and Bradley have no numbers (only stars). Pilsner's current data: HP 45, Bravado 12, Offense 8, Defense 6, Speed 5, Charm 9, Luck 4, Grit 3 | Stars to numbers, anchored on Pilsner: HP 25/30/35/40/45, Offense 5/6/8/10/12, Defense 2/3/4/6/7, Speed 5/6/7/8/9, Bravado 8/12/14/16/20 for 1-5 stars. **Bradley**: HP 30, Bravado 14, Off 12, Def 2, Spd 8, Charm 4, Luck 5, Grit 3. **Chadwick**: HP 35, Bravado 20, Off 6, Def 3, Spd 7, Charm 10, Luck 6, Grit 2 |
| ef3_starting_moves | Which moves each bro has in the first fights (only Roast Line has numbers: 4 Bravado, ×1.8) | Everyone: Attack, Item, Flex, Run. Pilsner: Roast Line. Chadwick's and Bradley's first signature moves get numbers in a later round |

Sanity check against Croc Monsieur (52 HP, Off 9, Def 6), all three at High Bravado: Pilsner hits
for about 8, Bradley 13, Chadwick 10, so about two rounds. At Low Bravado the party does about 1 / 4 /
1, which is the point of the system. The croc hits Bradley for about 7 of his 30 HP.

## 3. Conflict between docs (author picks)

**ef3_roles:** `party.md` says Lord Pilsner is the leader/all-rounder and **Bradley is the
tank**. `battle_system.md` says **Lord Pilsner is the tank** (HP and Defense high, Speed lowest) and
Bradley is the glass cannon. Pilsner's current data (HP 45, Speed 5) matches battle_system.md. The
§2 stats assume battle_system.md.
