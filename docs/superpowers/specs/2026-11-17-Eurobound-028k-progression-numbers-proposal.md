# How the Bros Grow: Numbers Proposal (Eurobound-028k)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-028k-q2`).
> Author's direction, verbatim (Eurobound Desk `Eurobound-028k-q1`, 2026-11-16): "Both: XP levels for stats, Clout for moves".
> Ledger: `docs/superpowers/NEXT_WORK.md:919` (commit d7bda677).
> Method and format copy the 2026-11-16 battle rounds (`2026-11-16-eurobound-g0jr-numbers-proposal.md`, `-rl4c-`, `-wuyu-`).
> Nothing in `game/` or `design/` was changed. No move, rung or combo names were written: every name below already
> exists in `design/mechanics/Battle/battle_system.md` or `design/mechanics/Progression/skilltrees_cloutspells.md`.
> **Every number in this file is PROPOSED.** Each one carries a one-line reason and a sim table (§10 explains the sim).

Audience check: younger Gen X, xennial and millennial women. Levels make the bros sturdier; Clout makes them louder.
Nothing here makes them admirable or self-aware. The bigger-ego-bigger-crash rule (§7) keeps the joke on them.

## 1. Already decided (used as written)

| Rule | Source |
|---|---|
| XP levels raise stats; Clout rungs open moves | 028k-q1, `NEXT_WORK.md:919` |
| `skilltrees_cloutspells.md` is not approved as written (its rungs, its 45 moves) | `NEXT_WORK.md:919` |
| Canon Ultimates: Fratocalypse Now (Bradley), Going Viral (Chadwick), Final Round's On Me (Pilsner); no numbers yet | Eurobound-40ym, `NEXT_WORK.md:927` |
| Starting kit, no rung: Roast Line, Beer Belly Bash (Pilsner); Like & Hype (Chadwick); Keg Smash, Bro, Do You Even Lift? (Bradley) | g0jr, wuyu (`NEXT_WORK.md:942`, `:944`) |
| Ultimates are not in the Debaucheryville slice; they open on Clout rungs | g0jr (`NEXT_WORK.md:942`) |
| Starter combos open from the start: Beeramid, Like & Subscribe, Who Flexed Harder?; later combos open on Clout rungs | rl4c (`NEXT_WORK.md:943`) |
| Embarrassed (flat): −20% ATK, −2 Bravado a turn, locks Bravado-cost moves, Ultimates and Taunt; 2 turns; an Embarrassed bro cannot start or join a combo | v27 (`NEXT_WORK.md:569`), v28 (`:583`), rl4c, g0jr-q3 (`:948`) |
| Debaucheryville villain stats and XP are approved (the `xp_reward` values in `debaucheryville_enemies.json`) | `NEXT_WORK.md:434-436` |
| City order for a first playthrough: Publandia → Debaucheryville → Sinfonia → Shamsterdam; every city stays open | `design/worlds/city_progression_order.md:9` |
| Losing a street fight keeps XP; auto-win compares party level with enemy level, gap still open | skjd (`NEXT_WORK.md:932`) |
| Party stats today (v26): Pilsner HP 45, Brav 12, Off 8, Def 6, Spd 5, Charm 9, Luck 4, Grit 3. Chadwick 35, 20, 6, 3, 7, 10, 6, 2. Bradley 30, 14, 12, 2, 8, 4, 5, 3 | `game/assets/data/party/party_members.json` |
| Star ratings per bro (HP, Attack, Defense, Speed, Bravado pool) | `battle_system.md:218-222`, `:237-241`, `:256-260` |

## 2. The one framing choice: Debaucheryville is the second city

The v26 stats and every approved Debaucheryville villain were tuned against the bros at `level: 1`
(`party_members.json:6`). But Publandia comes first (`city_progression_order.md:9`). A player who clears
Publandia arrives in Debaucheryville several levels up and finds the approved villains soft.

| Id | Proposed value | Reason |
|---|---|---|
| **028k_anchor** | **The v26 stats become the Level 8 row.** The bros arrive in Debaucheryville at about Level 8 (§3 sim). Levels 1-7 sit below v26, for Publandia | Keeps every approved Debaucheryville number exactly as approved; the other way (v26 = Level 1) means re-tuning every Debaucheryville villain once Publandia exists |
| **028k_slice_start** | The Debaucheryville slice starts the bros at **Level 8, 333 XP, 100 Clout (rung Active)**, as if Publandia were done | Same stats the slice already uses; only `level`, `xp` and the new Clout field change |
| **028k_arcade_band** | The Arcade's level band (Palette Swap 3-spawn, `player_two_palette_swap.md:152`) is **Levels 8-11**: the third Swap appears at party Level 12+ | Level 12 comes after about 16 Debaucheryville fights (§3), roughly when the Arcade stops being new |

Alternative for the note box: "v26 = Level 1". Then the slice is unchanged and Debaucheryville villains are re-tuned
upward when Publandia is built.

## 3. XP and levels

| Id | Proposed value | Reason |
|---|---|---|
| **028k_cap** | **Level cap 40** | Four cities at about 8 levels each put the end of the story near Level 32. The last 8 levels are for backtracking and grinding, the way EarthBound finishes well short of its cap |
| **028k_curve** | XP from Level L to L+1 = **round(34 × 1.11^(L−1))**, stored as a 39-row table (below). Total to cap: 17,793 | Each new city levels the bros every ~3 fights on arrival and every ~7 by the time they leave. EarthBound pacing: fast in a new area, slower as you outlevel it |
| **028k_city_xp** | Guide for future enemy docs: a typical fight pays about **10 XP in Publandia, 22 in Debaucheryville (approved data), 52 in Sinfonia, 121 in Shamsterdam** (×2.33 a city) | 2.33 is the curve's growth over 8 levels (1.11^8), so every city has the same rhythm. A guide only: enemy XP still gets ruled doc by doc |
| **028k_payout** | **Every bro gets the fight's full XP**, downed bros included (they leave a won fight at 1 HP, `NEXT_WORK.md:572`) | Three fixed party members and no bench. Splitting XP among standing bros would starve Bradley, the glass cannon who goes down most |
| **028k_levelup** | A level-up raises max HP and max Bravado and **raises current HP and Bravado by the same amount** (no full heal). Several level-ups from one fight all apply. XP stops counting at the cap | Keeps the rest rules from 8snp meaningful (`NEXT_WORK.md:920`) |
| **028k_rounding** | Growth is **fixed, not random**: stat at level L = v26 value + gain × (L − 8), rounded half up, minimum 1 | EarthBound rolls growth, but on this small scale one lucky +2 moves a fight by 15%. Fixed growth is testable in GUT. Random growth is the alternative for the note box |

**The curve** (XP to next level; each `#` ≈ 40 XP):

```
L 1->2     34 cum      0 |#
L 4->5     46 cum    114 |#
L 7->8     64 cum    269 |##
L 8->9     71 cum    333 |##          <- Debaucheryville slice starts here
L12->13   107 cum    666 |###
L16->17   163 cum   1171 |####        <- leaving Debaucheryville
L20->21   247 cum   1937 |######
L24->25   375 cum   3100 |#########   <- leaving Sinfonia
L28->29   569 cum   4866 |##############
L32->33   864 cum   7546 |######################  <- end of the story
L36->37  1312 cum  11615 |#################################
L39->40  1794 cum  15999 |#############################################
                 cap 40 at 17,793
```

**Fights per level-up** at each city's typical fight XP:

| Level | Publandia (10) | Debaucheryville (22) | Sinfonia (52) | Shamsterdam (121) |
|---|---|---|---|---|
| 1 | 3.6 | | | |
| 8 | 7.4 | **3.2** | | |
| 16 | | 7.3 | **3.1** | |
| 24 | | | 7.2 | **3.1** |
| 32 | | | | 7.1 |

**Monte Carlo, level on leaving each city** (4,000 runs; Debaucheryville fights drawn from the approved
Arcade tables and Feral Segway Tourist street fights; other cities scaled by 028k_city_xp; p10 / mean / p90):

| Player | Publandia | Debaucheryville | Sinfonia | Shamsterdam |
|---|---|---|---|---|
| Rusher, ~28 fights a city | 5 / 6.4 / 8 | 12 / 13.3 / 15 | 19 / 20.8 / 23 | 27 / 28.8 / 31 |
| **Main path, ~40 fights a city** | 7 / **8.1** / 9 | 15 / **16.0** / 17 | 23 / **24.0** / 25 | 31 / **32.1** / 33 |
| Thorough, ~60 fights a city | 10 / 10.5 / 11 | 18 / 19.3 / 20 | 27 / 27.7 / 29 | 35 / 35.9 / 37 |

**Slice check** (start Level 8, Debaucheryville fights only): Level 9 after 3.8 fights, 10 after 7.3, 12 after 15.6,
14 after 25.8, 16 after 38.3.

## 4. Stat growth per level

Gains follow the star ratings in `battle_system.md` (★1 ≈ 0.2-0.25, ★5 ≈ 0.8 a level for Off/Def/Spd; HP ★2 2.0, ★3 2.5,
★5 3.5). Charm, Luck and Grit have no stars, so their gains keep today's order between the bros.

| Id | Bro | HP | Bravado | Offense | Defense | Speed | Charm | Luck | Grit |
|---|---|---|---|---|---|---|---|---|---|
| **028k_growth_P** | Lord Pilsner (tank) | **3.5** | **0.2** | **0.55** | **0.5** | **0.25** | **0.4** | **0.15** | **0.3** |
| **028k_growth_C** | Chadwick (support) | **2.5** | **0.5** | **0.4** | **0.35** | **0.4** | **0.5** | **0.25** | **0.2** |
| **028k_growth_B** | Bradley (cannon) | **2.0** | **0.3** | **0.8** | **0.2** | **0.5** | **0.2** | **0.2** | **0.2** |

Reasons in one line each: Pilsner has the ★5 HP and ★4 Defense and stays the one who takes hits; Chadwick has the ★5
Bravado pool, so his grows fastest; Bradley has the ★5 Attack and ★1 Defense, so he hits harder every level and never
learns to block.

**Resulting stats** (HP / Brav / Off / Def / Spd / Charm / Luck / Grit):

| Level | Lord Pilsner | Chadwick | Bradley |
|---|---|---|---|
| 1 | 21 / 11 / 4 / 3 / 3 / 6 / 3 / 1 | 18 / 17 / 3 / 1 / 4 / 7 / 4 / 1 | 16 / 12 / 6 / 1 / 5 / 3 / 4 / 2 |
| 4 | 31 / 11 / 6 / 4 / 4 / 7 / 3 / 2 | 25 / 18 / 4 / 2 / 5 / 8 / 5 / 1 | 22 / 13 / 9 / 1 / 6 / 3 / 4 / 2 |
| **8 (v26)** | **45 / 12 / 8 / 6 / 5 / 9 / 4 / 3** | **35 / 20 / 6 / 3 / 7 / 10 / 6 / 2** | **30 / 14 / 12 / 2 / 8 / 4 / 5 / 3** |
| 12 | 59 / 13 / 10 / 8 / 6 / 11 / 5 / 4 | 45 / 22 / 8 / 4 / 9 / 12 / 7 / 3 | 38 / 15 / 15 / 3 / 10 / 5 / 6 / 4 |
| 16 | 73 / 14 / 12 / 10 / 7 / 12 / 5 / 5 | 55 / 24 / 9 / 6 / 10 / 14 / 8 / 4 | 46 / 16 / 18 / 4 / 12 / 6 / 7 / 5 |
| 24 | 101 / 15 / 17 / 14 / 9 / 15 / 6 / 8 | 75 / 28 / 12 / 9 / 13 / 18 / 10 / 5 | 62 / 19 / 25 / 5 / 16 / 7 / 8 / 6 |
| 32 | 129 / 17 / 21 / 18 / 11 / 19 / 8 / 10 | 95 / 32 / 16 / 11 / 17 / 22 / 12 / 7 | 78 / 21 / 31 / 7 / 20 / 9 / 10 / 8 |
| 40 | 157 / 18 / 26 / 22 / 13 / 22 / 9 / 13 | 115 / 36 / 19 / 14 / 20 / 26 / 14 / 8 | 94 / 24 / 38 / 8 / 24 / 10 / 11 / 9 |

**Role check, every level 1-40:** Bradley always has the most Offense, Pilsner the most HP and Defense, Chadwick the
biggest Bravado pool, and the Speed order Bradley > Chadwick > Pilsner holds everywhere except Level 2 (Bradley and
Chadwick tie at 5, in Publandia only).

**Battle check** (simplified Monte Carlo, 3,000 fights each: bros Attack with Flex, Bradley Keg Smashes, Pilsner Roast
Lines; the enemy uses plain attacks). The reference enemy is Croc Monsieur at Level 8, scaled by the guide curve in the
last table. Columns: win %, rounds, party HP left.

| Fight | Win | Rounds | HP left |
|---|---|---|---|
| v26 reference: Level 8 party vs Croc Monsieur | 100% | 1.7 | 97% |
| Level 12 party vs Croc (mid-Debaucheryville) | 100% | 1.0 | 100% |
| Level 8 vs 2 Crocs | 100% | 3.1 | 87% |
| Matched Level 24 vs 2 reference enemies | 100% | 3.7 | 88% |
| Matched Level 16 / 24 / 32 / 40, one enemy | 100% | 1.6 / 1.8 / 1.9 / 2.3 | 98% / 97% / 97% / 96% |
| 4 levels under (20 vs 24) / 4 over (28 vs 24) | 100% | 1.9 / 1.4 | 96% / 99% |

Reading: at a matched level, fights stay the same length from Level 8 to Level 32 and stretch slightly at the cap.
Outlevelling an area makes it quick, which is what EarthBound's auto-win is for (skjd). This sim leaves out enemy
moves, statuses and resistances, so it checks the growth rates, not any one fight.

| Id | Proposed value | Reason |
|---|---|---|
| **028k_enemy_guide** | Guide for future enemy docs: per level above 8, an enemy gains **×1.045 HP, +0.55 Offense, +0.45 Defense** from its Debaucheryville equivalent. Reference enemy: L16 HP 74 / Off 13 / Def 10; L24 105 / 18 / 13; L32 150 / 22 / 17 | This is the rate that keeps matched fights flat in the table above. A guide only: every enemy still gets ruled in its own doc |

**Bravado drift.** Move costs are fixed numbers, so as the pool grows each move takes a smaller share. One cast from
a full bar drops a tier only while the cost is over a third of the pool:

| Level | Keg Smash (5) | Roast Line (4) | Beer Belly Bash (3) | Like & Hype (4) |
|---|---|---|---|---|
| 8 | 5/14 = 36% | 4/12 = 33% | 25% | 20% |
| 16 | 31% | 29% | 21% | 17% |
| 32 | 24% | 24% | 18% | 12% |
| 40 | 21% | 22% | 17% | 11% |

Keg Smash stops dropping Bradley from High to Mid after Level 9. That is proposed as fine: the moves that open later
(§6) cost more. The alternative for the note box: **max Bravado does not grow with level** (all Bravado gains 0).

## 5. Clout: thresholds, what earns it, payouts

| Id | Proposed value | Reason |
|---|---|---|
| **028k_clout_pool** | **One Clout total for the party**; the three bros share the rung | EarthBound opens moves at fixed points with no point-spending menu. One number, one rung, and combos need no "each bro at 300" check (`skilltrees_cloutspells.md:87`) |
| **028k_rungs** | Rung names and floors as in the ladder doc: **Pledge 0, Active 100, Alumni 300, Legacy 600, Living Legend 1,000** (`skilltrees_cloutspells.md:11-15`) | Gaps of 100 / 200 / 300 / 400 grow by one step a city, so the main story pays one rung per city (table below) |
| **028k_clout_no_fights** | **Ordinary and repeatable fights pay no Clout.** The villain docs' "Clout (XP)" rows are XP | If fights paid both, the two bars would be one bar. XP is for grinding; Clout is for deeds |
| **028k_clout_main** | The main story pays each city's rung gap: **Publandia 100, Debaucheryville 200, Sinfonia 300, Shamsterdam 400.** The city boss pays half; the city's main-story beats share the other half | A player who skips every side quest still reaches the next rung at each city's boss. Side quests are optional and must not gate moves |
| **028k_clout_side** | Each side quest pays **5 Clout in Publandia, 10 in Debaucheryville, 15 in Sinfonia, 20 in Shamsterdam**, in the template's Clout field (`design/templates/sidequest_template.md:85`). Same on a return visit | 10% of the rung gap per quest: a completionist reaches each rung about mid-city, never a whole rung early |
| **028k_clout_nft** | Each NFT found pays **3 / 5 / 8 / 10 Clout** (same city order) | The NFT hunts run on the bros believing NFTs are clout (`design/Quests/debaucheryville/nfthuntdebaucheryville.md:2`). Smaller than a quest: 3-4 per city (`game_design_document.md:80`, `:141`, `:169`) |
| **028k_clout_never_lost** | **Clout never goes down**; nothing un-learns a move | Losing standing already exists as regional reputation (trl3, `NEXT_WORK.md:949`). Embarrassment stays in battle (§7) |

**Clout by city** (side-quest counts from the `design/Quests/<city>/` folders: 5 / 13 / 5 / 4; Shamsterdam NFTs assumed 3):

| Player | Publandia | Debaucheryville | Sinfonia | Shamsterdam |
|---|---|---|---|---|
| Main path only | 0 → 100: **Active at the boss** | → 300: **Alumni at the boss** | → 600: **Legacy at the boss** | → 1,000: Living Legend at the final boss |
| Half the side quests and NFTs | → 118 | → 390 (Alumni at the boss) | → 740 (Legacy at the boss) | → 1,195 (995 before the boss) |
| Every side quest and NFT | → 137 (Active at the boss) | → 482 (**Alumni before the boss**) | → 881 (**Legacy before the boss**) | → 1,391 (**Living Legend before the boss**) |

Reading: nobody reaches Legacy (the Ultimates) in Debaucheryville, even doing everything, which keeps the g0jr ruling.
Living Legend is a rung for players who do the side quests or come back later.

## 6. What each rung opens

Every move below is from `battle_system.md` (line numbers given). Each bro has seven moves there besides his starting
kit, plus his Ultimate: eight slots, two per rung. Order: simple and cheap first, upgrades and room-clearers last.

**Lord Pilsner** (Keg-Fu, tank)

| Rung | Moves | Why there |
|---|---|---|
| Pledge (kit) | Roast Line, Beer Belly Bash | Approved |
| Active (100) | Keg Shield (:263), Stout Stagger (:298) | He soaks for others from the start; one heavy hit with a Speed drop |
| Alumni (300) | Bouncer Toss (:265), Chug & Shrug (:264) | First splash damage; first self-heal |
| Legacy (600) | Brew Shield (:295), **Final Round's On Me (Ultimate, :299)** | Brew Shield is the party-wide Keg Shield |
| Living Legend (1,000) | Barrel Roll (:296), Hop-Chi Heal (:297) | Hit-everyone knockdown; the heal that scales with missing Bravado |

**Chadwick** (Bro-Mancy, support)

| Rung | Moves | Why there |
|---|---|---|
| Pledge (kit) | Like & Hype | Approved |
| Active (100) | Bro Code Chant (:246), Hashtag Blessing (:289) | Embarrassed is everywhere in the Arcade, so the cure comes early; a crit buff pairs with Like & Hype |
| Alumni (300) | Clout Hex (:288), Wingman Shout (:245) | First enemy debuff; taunt-all for the support |
| Legacy (600) | Flex Cam (:244), **Going Viral (Ultimate, :291)** | Both stream an ally's move; Going Viral copies everyone's last move, so it wants a full moveset |
| Living Legend (1,000) | Influence Aura (:287), Cancel Smite (:290) | Party Bravado regen; the 50/50 cancel is endgame chaos |

**Bradley** (Frat-Sorcery, cannon)

| Rung | Moves | Why there |
|---|---|---|
| Pledge (kit) | Keg Smash, Bro, Do You Even Lift? | Approved |
| Active (100) | Pledge Hazing (:226), Natty Light Bolt (:279) | Set-up and pay-off: Hazing inflicts Embarrassed, the Bolt ignores armour on Embarrassed enemies |
| Alumni (300) | Frat Fury (:225), Shotgun Flex (:227) | Multi-hit, then the guaranteed crit for a third of his bar |
| Legacy (600) | Jaeger Meteor (:280), **Fratocalypse Now (Ultimate, :283)** | The ×2 heavy hit at high Bravado, then the whole-bar nuke |
| Living Legend (1,000) | Beer Pong Barrage (:281), Shotgun Ritual (:282) | Stacking multi-hit; Shotgun Ritual is Shotgun Flex with splash |

Every move above still needs its own numbers round (cost, multiplier, chance, spoken tag), like g0jr. For the slice,
that means the six Active moves; the Alumni six can follow, since Alumni comes at the Debaucheryville boss.

**Combos** (all from `battle_system.md`):

| Rung | Combos | Note |
|---|---|---|
| Pledge (open) | Beeramid, Like & Subscribe, Who Flexed Harder? | Approved (rl4c) |
| Active (100) | Toast vs. Post (:182) | The other contest combo, twin of Who Flexed Harder? |
| Alumni (300) | Bros Before Heroes (:169 / :359), Wingman Protocol (:163 / :354), Flex-Off (:371) | The ladder doc opens cross-party combos at Alumni (`skilltrees_cloutspells.md:13`) |
| Legacy (600) | Alpha Sigma Slam (:137), Tag Team Supreme (:364), Who's The Alpha? (:379); Viral Moment (:328) also needs the Ring Light Mace equipped | The three-bro combos; Viral Moment rides on Bradley's Ultimate |
| Living Legend (1,000) | **Unassigned rung.** battle_system.md has no combo left for it | The ladder doc puts Legendary Douchebags, Rewrite Reality and Infinite Ego Loop here (`skilltrees_cloutspells.md:95-98`); battle_system.md makes Legendary Douchebags a gear combo (Full Frat Regalia, :387-388) |

**Not on the ladder** (they have their own gates): the region combos (Beer Brawl Combo, Casino Royale, Symphony of
Bros, Tavern Takeover, VIP Meltdown, Symphony of Destruction); the gear combos (LinkedIn Lament, Bros Before Heroes:
Deluxe / Team Finisher, Full Frat Regalia, Tech Bro Catastrophe); and the backfire combos (Selfie Block, Selfie Sabotage,
Double Chug, Double Chug Disaster, Spotlight Clash), which rl4c left open as "chosen or happens to them".

**Moves only in the ladder doc** (`skilltrees_cloutspells.md:17-84`): not placed. Of its 45 moves, Hashtag Blessing and
Influence Aura are also in battle_system.md and are placed above. The other 43 (Pint-Sized Rally through Immortal Bro)
are left for the author to keep or strike. Kept ones could fill Living Legend's empty combo slot or a later rung.

## 7. Does Embarrassed escalate by Clout rung?

The ladder doc says yes (`skilltrees_cloutspells.md:4-6`); the ruled Embarrassed is flat (§1). Raised by Eurobound-jsd0.

| Id | Proposed value | Reason |
|---|---|---|
| **028k_emb_low** | **Pledge, Active, Alumni: exactly the ruled Embarrassed.** The doc's Pledge "−1 Bravado a turn" is dropped | It would soften a ruled number, and every rung the slice uses stays as built |
| **028k_emb_legacy** | **Legacy: −3 Bravado a turn** instead of −2. Everything else as ruled | "The bigger the ego, the harder the crash" (`skilltrees_cloutspells.md:7`), at the rung where the Ultimates open |
| **028k_emb_legend** | **Living Legend: −3 a turn, and each other standing bro loses 1 Bravado a turn while he is Embarrassed** (the doc's "secondhand embarrassment", `:6`). The doc's "combos locked 2 turns" is dropped | An Embarrassed bro already cannot start or join a combo (rl4c); locking everyone's combos would stack a second penalty |
| **028k_emb_scope** | Only the bros' Embarrassed escalates. Enemies made Embarrassed (Pledge Hazing, Clout Hex) use the ruled version | Clout is the bros' ego, not the enemy's |

Bravado lost over the 2 turns of Embarrassed:

| Rung | The Embarrassed bro | Each other bro | Party | Per turn if he Flexes (+3) |
|---|---|---|---|---|
| Pledge to Alumni (ruled) | 4 | 0 | 4 | +1 |
| Legacy | 6 | 0 | 6 | 0 |
| Living Legend | 6 | 2 | 10 | 0 |

Reading: from Legacy on, Flexing only holds his bar level; it no longer climbs. That is the crash, without a lockout.
Alternative for the note box: no escalation at any rung (the flat rule everywhere).

## 8. Conflicts and gaps (author picks)

- **Level 1 or Level 8** (§2). Proposed: v26 = Level 8.
- **Quest "Recommended Level".** Ten quest docs carry a "Recommended Level" between 1 and 7 (e.g. `bacchanusbeachbeatdown.md:9`,
  3-5; `nothingisgettingthrough.md:9`, 5-7). The template calls it a 1-10 difficulty (`sidequest_template.md:12`), and the
  values don't follow the city order (Bicycle Thunderdome in Shamsterdam: 5). With real levels the field reads as a
  character level. Filed as its own bead; this proposal does not change them.
- **"Clout (XP)" label.** The villain template (`villain_template.md:148`) and ten Arcade villain docs label XP as
  "Clout (XP)"; `party.md:10`, `:100`, `:103` say XP is Clout. Under the ruling these are XP. Relabel after approval (same bead).
- **Duplicate combo names in battle_system.md.** Alpha Sigma Slam (:137, 10% argument) and Alpha Sigma Thunder (:333,
  15%, combined Bravado > 150); Beeramid and Beeramid Blast (:320); Like & Subscribe and Viral Moment (:328). The
  table in §6 uses the codex names. One of each pair needs striking before numbers.
- **Intoxication law.** Chug & Shrug, Hop-Chi Heal ("the drunker, the stronger", :297) and Final Round's On Me ("slams
  entire keg", :299) need the 10-point review in `design/mechanics/intoxication_law.md` before their numbers. Shotgun
  Flex and Shotgun Ritual should be checked too (the doc never says whether "shotgun" means a beer). Placing them on a
  rung is not a number, so they are placed.
- **Wingman Shout vs Taunt.** Every bro now has a Taunt minor action (wuyu). Wingman Shout is the main-action version
  that taunts all enemies (:245); its numbers round should keep the two apart.
- **The rest of the ladder doc** (Regional Mastery, Midlife Crisis Mode, Reality Check, Fake It Till You Make It,
  the NPC reaction ladder, `skilltrees_cloutspells.md:100-160`): not covered. They need their own rulings; the
  2026-11-15 proposal already flags "Perspective" / "Character Growth" (`:149-153`) as breaking "never self-aware".
- **Auto-win gap** (skjd) and **enemy level tags**: once this curve is approved, each enemy can carry the level it is
  tuned for (Debaucheryville: 8-12) and the auto-win gap can be ruled against it. Left to skjd's numbers round.

## 9. If approved: build and doc follow-ups (not done here)

1. Ledger entry and `design/mechanics/Progression/leveling.md`, `xpgain.md` rewritten from §3-§5 (placeholders today).
2. Eurobound-5aie: pay XP to every bro, apply the level table and growth, GUT tests; set the slice start (Level 8,
   333 XP, Clout 100); add a Clout total and rung to `GameState` and the menu.
3. A numbers round for the six Active moves (two per bro), then Alumni.
4. Rung-gated move lists in `party_abilities.json` / `combos.json` (an `unlock_rung` field).

## 10. How the sim was run

A scratch Python script (not in the repo). Fixed seed, 4,000 runs per row.

- **Fight XP**: the approved Debaucheryville tables. Frogger releases 18 / 21 / 34 / 43 XP (weights 40/35/15/10),
  Street Fighter 12 / 20 / 42 (50/30/20), Kebab Kombat rungs 20 / 34 / 44, street Feral Segway Tourist 12;
  a quarter of fights from each source. Mean 22.3 XP a fight. Other cities: the same draws × 0.43 / 2.33 / 5.43.
- **Fights per city**: normal around 28, 40 or 60, standard deviation 6.
- **Battles**: the v26 rules (Base = Off + Bravado mod − Def, ±2, minimum 1; 95% to hit; crit at Luck %, +10 at
  High, ×2; thirds tiers; Flex +3). Bros: Bradley Keg Smashes while it leaves him at Mid or above, Pilsner Roast Lines
  while it leaves him at High, otherwise Flex and Attack on the weakest enemy. Enemies attack a random standing bro.
  No enemy moves, statuses, resistances or the cabinet +50% HP.
- **Clout**: deterministic sums of §5's payouts; "before the boss" = the main-story beats' half plus side quests.
