# Round v43 design proposals (2026-11-12)

Status: PROPOSALS ONLY. Nothing here is canon until the author picks. No game code or canon doc was changed.
Author asks answered here: `taproom_numbers = propose`, `fs_embarrassed = propose`, `bp_keychain_passives = gather, then draft` (NEXT_WORK.md:757, 748, 764).

Path keys (all repo-relative): **TT** = `design/World Design/Debaucheryville/the_absinthium_taproom.md` | **NW** = `docs/superpowers/NEXT_WORK.md` | **EN** = `game/assets/data/enemies/debaucheryville_enemies.json` | **AB** = `game/assets/data/enemies/debaucheryville_arcade_battle.json` | **PM** = `game/assets/data/party/party_members.json` | **FS** = `game/core/field_status.gd` | **KC** = `design/items/bottle_opener_keychain_item.md` | **AD** = `Assets/Data/items/Bottle Opener Keychain.md` | **BT** = `design/quests/general_quests/brewerytour.md` | **PB** = `design/items/brewery_passport_book_item.md`.

---

## 0. Canon contradictions found (read first)

1. **Mirror Chad is listed as KILLED.** NW:23 ("Killed by author ruling: Mirror Chad"). Later rulings put him back: NW:732 (v41-42, "build ... Mirror Chad") and NW:757 (v43, "Mirror Chad and Wisp numbers are proposed"). Treated here as superseded by the later rulings; please confirm (Q1.1).
2. **Can the Taproom opener be bought?** TT:28 and TT:35 say complete the maze OR pay 22 SOVS. NW:732 says "The opener must be earned, cannot be bought"; `design/items/brewery_tour/opener_absinthium_taproom_item.md:6-7` and BT:64-65 agree (openers never sold). The 22 SOVS path and the "opener check" speech need rewriting (not done here).
3. **What does Dr. Vanek check?** TT:23,30-31,35 check a "Blarney Trap Bottle Opener"; TT:211 asks for "Debaucheryville Bottle Opener Keychain" (implies per-city keychains, dead per legacy). v43 ruling (NW:763): the ONE keychain from The Blarney Trap is the gate for collecting any opener. TT should check the keychain only.
4. **12 vs 16 breweries.** KC:13,26,269 say 12 (4 x 3 cities); BT:40,90,124 and PB:214-217 say 16 (4 x 4). The author flagged this (NW:764) and it is unresolved. Section 3 is written to work for either.
5. **Keychain: preloaded or new?** AD:8 and BT:38 say "pre-loaded" with spring-break openers; KC:29,44 say new, clean, empty. KC:5 says nothing labelled PROPOSED is canon. NW:764 says author copy was written into the item docs; the working-tree KC may or may not be that copy.
6. **How the keychain is obtained.** KC:16,30,272-273 "TBD"; BT:36-41 (order the special beer at the first Publandia brewery, handed over with first opener and Passport); AD:11 (conflict-marker text) "MUST be purchased in Dublin"; legacy docs "15 Sovs". NW:763 only fixes The Blarney Trap as the source. AD:9-12 is an unresolved Git conflict block.
7. **"Bartender Recognition" appears nowhere in the repo** (full-text search, excluding .git/.beads). Nearest canon: AD:6,29 (bartenders give better prices/exclusive brews) and KC:227 (NPC reaction "Professional recognition"). I use it as a working name only.
8. **Three different "Embarrassed" definitions:** battle = -20% ATK, -2 Bravado/turn, 2 turns (NW:569,583); hostel = -10 Bravado for 4 hours (`design/worlds/publandia/the_bunk_and_blunder.md:186-187`); closet = a gate with no stated effect (`design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md:102-117`).
9. **Real place names in canon copy:** AD:8,11,34-37 (Cancun, Daytona, Dublin, Prague, Munich, Belgium). Player-facing text may not use them (`.claude/CLAUDE.md`). Also raised at NW:764.

---

## 1. Taproom battle numbers

### 1.1 Benchmarks (approved or shipped numbers)

| Fight | HP | Off | Def | Spd | XP | Pays | Source |
|---|---|---|---|---|---|---|---|
| Feral Segway Tourist (street grunt) | 28 | 6 | 3 | 6 | 12 | 8 SOVS | EN:8-16 |
| Palette Swap | 16 | 5 | 2 | 8 | 6 | 4 tickets | EN:102-114 |
| Croc Monsieur (heavy) | 52 | 9 | 6 | 3 | 22 | 15 tickets | EN:18-30 |
| Two-Seventy Vratislav (heavy) | 54 | 9 | 6 | 2 | 28 | 15 tickets | EN:130-142 |
| Shish Kahn (cabinet boss) | 72 | 10 | 6 | 3 | 30 | 20 tickets | EN:88-100 |
| Accounts Receivable (x2, toughest fight) | 46 each (92) | 9 | 7 | 3 | 22 each | 0 | EN:144-155; `design/worlds/debaucheryville/villains/absinthe_arcade/accounts_receivable.md:116-123` |

- **Party:** Pilsner HP 45 / Off 8 / Def 6 / Spd 5 / Charm 9 / Grit 3 (PM:8-15); Bradley HP 30 / Off 12 / Def 2 / Spd 8; Chadwick HP 35 / Off 6 / Def 3 / Spd 7 / Charm 10 / Grit 2 (NW:554). Party pool 110 HP.
- **Cabinet villains get +50% HP** (NW:582; `game/worlds/debaucheryville/absinthe_arcade/arcade_battle.gd:131-134`). Taproom foes are NOT cabinet villains, so the EN figures are their real HP. Cabinet equivalents: Croc 78, Vratislav 81, Shish 108.
- **Rules reused:** damage words x0.7/1.0/1.2/1.5, spread +-2, min 1, social = (Charm + Bravado mod) - Grit (NW:566-568); Bravado mod +half max at High, +quarter at Mid, -2 at Low (NW:549); Embarrassed and Confused as in NW:569-570; Stun and statuses last 2 turns unless a doc says otherwise (NW:583).

Formula (stat/reward scaling used below):

`HP_new = round(HP_ref x k)`   `XP = round(0.45 x HP_new)`

| Symbol | Type | Range | Description |
|---|---|---|---|
| HP_ref | int | 28-92 | Benchmark HP from the table |
| k | float | 0.75-1.25 | Tier multiplier chosen per option |
| XP | int | 1-60 | XP reward; 0.45 is the benchmark average (Croc .42, Vratislav .52, Shish .42, AR .48, Segway .43) |

Unbounded above, but all options stay under the Shish Kahn x1.5 ceiling (108) so no Taproom foe outclasses the Arcade's top fight. Example: HP_ref 54 (Vratislav), k 1.0 -> HP 54, XP 24.

Kill-speed check (ASSUMES physical = Off + Bravado mod - Def, as social does at NW:568; no crits): vs Def 5 at Mid Bravado the party deals Bradley 10.5 + Pilsner 6 + Chadwick 6 = about 22 per round; at Low Bravado about 7. 3 rounds therefore kill 54 HP only if Bravado is kept up.

### 1.2 Mirror Chad (mini-boss)

Fixed by TT: dies in 3 turns or applies Confused (TT:156); three barks (TT:158-160); per-bro mirror lines (TT:163-165); drop `cracked_mirror_shard` (TT:372); "Mirror, Mirror" = defeat without taking damage (TT:299).

| | **A. Words Only (Recommended)** | **B. Hybrid** | **C. True Mirror** |
|---|---|---|---|
| HP | 54 (Vratislav, k 1.0) | 42 (k 0.78, between Segway and Croc) | 1.2 x the mirrored bro: 54 / 36 / 42 |
| Off / Def / Spd | 9 / 5 / 4 | 8 / 4 / 5 | copies that bro |
| Charm / Grit / Luck | 8 / 3 / 3 | 8 / 3 / 3 | copies that bro |
| Round 1 bark | "Maybe you're the problem": Embarrassed 40%, one target, 2 turns, no HP damage | same | that bro's own Attack |
| Round 2 bark | "They ALL remember": drains 3 Bravado from one bro (Taunt precedent, AB:511-514) | social low x0.7 + Embarrassed 40% (Hatchback move, AB:121-132) | that bro's own Attack |
| Round 3 bark | "Exactly like your father": if he is alive, applies Confused to one bro, 2 turns (AB:57-69), then repeats rounds 1-3 | same | same |
| "Mirror, Mirror" | Reachable (he never damages) | Only by killing him before round 2 | Practically not |
| Why | The 3-turn clock is the threat: Embarrassed (-20% ATK) makes the kill slower. Theme matches TT: every move is a line | Mix of words and a hit | Literal "your own sprite" |

Shared: immune to Embarrassed and Confused (he applies them; same pattern as AB:783-785). Needs 18 dmg/round average to beat the clock at HP 54 (A) or 14 (B): comfortable at Mid, failed at Low.

Rewards (all options): XP 24 (A) / 19 (B) / 0.45 x HP (C); drop `cracked_mirror_shard` 100% (every shipped mini-boss drops at 1.0, EN:29,99,141); tickets 0 (the Taproom is not a cabinet; Q1.3).
SOVS drop: **12** (recommended: one Absinthe Lager; per-HP the Segway pays 0.29 SOVS/HP, so 54 HP is about 15, rounded down) / 0 / 20.

### 1.3 Green Fairy Wisp (optional boss)

Fixed by TT: phases at 66% and 33% (TT:170-179); Confusion Breath 40% Confused (TT:171); splits into 3, 2 illusions and 1 real (TT:175); Phase 3 "control reversal possible" and final attack "The Truth" (TT:179-180); rewards Green Fairy Essence (consumable, guaranteed Confusion, +30 Bravado) and stamp eligibility (TT:183-184); "Defeat OR survive" (TT:209); Reality Anchor now a 10% chance to block Confusion (NW:750).

| | A. Single Heavy | **B. Pair Parity (Recommended)** | C. Cabinet-Equivalent |
|---|---|---|---|
| HP | 72 (= Shish Kahn) | 90 (about AR pair 92, the toughest base fight) | 108 (Shish x1.5 effective) |
| XP | 32 | 40 | 49 |
| Expected length at Mid Bravado | 3 rounds | 4-5 (illusions eat actions) | 5-6 |

Shared stats: Off 9 (heavy parity) / Def 4 / Spd 8 / Charm 10 / Grit 2 / Luck 5. Immune: Confused. Her damage is deliberately low (Off 9 vs party Def 2-6 is about 3-7 per hit, 110-HP party); the threat is statuses, as the docs frame her.

| Phase | Moves (only doc-named skills plus the universal Attack, NW:555) | Numbers |
|---|---|---|
| 1 (100-66%) | Attack; Confusion Breath | Breath weight 40, Confused 40%, one target, 2 turns. With Reality Anchor: 0.40 x 0.90 = 36% |
| 2 (66-33%) | Splits into 3: the real Wisp plus 2 illusions using the Palette Swap block (16 HP, Off 5, Def 2, Spd 8; EN:102-114), no rewards. Attack; Confusion Breath | Illusions pop on any hit; the real Wisp holds the rest of the HP pool; no visual tell unless Q1.4 |
| 3 (33-0%) | Attack; Confusion Breath now hits all (weight 35); **The Truth**, once, at HP under 20% (`hp_below_once` pattern, AB:218,698), one round of telegraph (AB:77-80) | The Truth: social moderate x1.2 to all, -5 Bravado each (drain precedent 2-3, NW:571, AB:513), and Saw Yourself on each bro hit (field status: -5 Bravado, 1 h, TT:285; per-bro per NW:749). It is the final attack |

Rewards: Green Fairy Essence 100%; stamp eligibility; achievement "Fairy Slayer" (TT:306); XP per option row; SOVS **25** (about two Lagers) / 0 / 40 (the Accounts Receivable tab, AR doc:199). "Survive" route (stamp, no Essence/XP/Fairy Slayer): the Wisp leaves after round 6 (Q1.2).

### 1.4 Absinthe Lager price

TT:225 lists 12 SOVS, and NW:732 repeats "(12 SOVS)" in the v41-42 build list, but v43 did not separately confirm it. Interactions: signature beers can be bought only after earning that brewery's opener (NW:761); the Lager carries Bravado +15 and 30% Green Fairy Confusion to the drinker (TT:222-224); the Essence is the Lager doubled (+30, 100%). I recommend **confirming 12 SOVS**. Beat 40 SOVS tab (AR doc:199) and 4+40 Croc bill (AB:21-24): a Lager is cheap, as a Taproom drink should be.

### Questions for the author (Section 1)
- **Q1.1 Mirror Chad un-killed?** (a) Yes, NW:732/757 supersede NW:23 (Recommended) / (b) No, drop him, Wisp only.
- **Q1.2 Mirror Chad package:** A Words Only (Recommended) / B Hybrid / C True Mirror. **Wisp HP:** A 72 / B 90 (Recommended) / C 108.
- **Q1.3 Rewards:** SOVS 12 + 25 (Recommended) / SOVS 0, items and XP only / SOVS 20 + 40. Tickets in the Taproom: none (Recommended) / pay tickets like cabinets.
- **Q1.4 "Survive the Wisp" and the Lager:** Wisp leaves after round 6, no tell for the real one + Lager 12 SOVS confirmed (Recommended) / real Wisp has a shimmer tell + Lager 12 / change the Lager price (type it).

---

## 2. Embarrassed in the field

### 2.1 What exists
- Field layer: `FieldStatus` stores either game-clock minutes (`UNIT_CLOCK`) or real seconds (`UNIT_REAL`), per bro or party; `has(state, id)` with no target means "any bro" (FS:17-18,41-49,59-67). Embarrassed is "a gate ... no field effect of its own" (FS:12-13).
- Sibling field durations: Saw Yourself 60 min, Existentially Rested 120 min, Confusion 30-180 real seconds (FS:26-30; TT:284-287).
- Checks: graffiti joystick glows only while Embarrassed (closet doc:115); reading graffiti while Embarrassed unlocks the "Combo'd by Love" lore (closet doc:110); "Joysticks & Shame" needs the whole graffiti tour done while still Embarrassed (closet doc:111,117); an Embarrassed-only sticker waits on this system (NW:733).
- Sources in canon: failing a QTE in front of an NPC (closet doc:103); the closet's 30-second shame timer (NW:733), which fires an announcer line once per visit when you stay in the room 30 s (`game/assets/data/locations/debaucheryville/debaucheryville_environmental.json:438-443`); hostel roommate witnesses (Bunk and Blunder doc:176-184).
- "Field statuses carry into battle" (NW:746); battle Embarrassed lasts 2 turns (NW:583).

### 2.2 Proposal: duration

`T_field = base x (1 - 0.10 x R)` (minutes of game clock)

| Symbol | Type | Range | Description |
|---|---|---|---|
| base | int | 30-240 | Option value below |
| R | int | 0-3 | Embarrassed Resistance points (closet doc:103 grants +1); the -10% per point copies Photogenic Drinker's -10% (BT:79-80) |
| T_field | int | 27-240 | Minutes until it expires; clamped to min 1; refreshing re-applies and never stacks |

| | base | Why |
|---|---|---|
| A. Short, real-time | 90 real seconds (`UNIT_REAL`) | Cheap, but the closet shame timer fires at 30 s, leaving about 60 s to read graffiti. Too tight for a "complete the tour" gate |
| **B. One hour (Recommended)** | 60 game-min | Matches Saw Yourself (TT:285), long enough for the closet and the way out, gone by the next scene |
| C. Hostel-length | 240 game-min | Matches the existing hostel -10 Bravado for 4 h (Bunk doc:187); outlasts the Arcade visit and bleeds into other cities |

Example (B, R = 1): 60 x 0.9 = 54 minutes.

### 2.3 Proposal: what applies it and what checks it
- **Applied by (Recommended, all three):** (1) the closet shame timer's announcer line at 30 s in the room, once per visit (reuses the existing trigger, so a re-visit re-applies it and it cannot be farmed); (2) a failed QTE in front of an NPC (closet doc:103); (3) hostel roommate-witness events, replacing the separate -10 Bravado/4 h version (Contradiction 8) so there is one Embarrassed. Applied to the bro involved (lead bro for the shame timer), per-bro like the other two Taproom statuses (NW:749).
- **Checked by:** `FieldStatus.has(state, EMBARRASSED)` with target "any bro": glowing joystick, lore drop, "Joysticks & Shame" progress, the sticker.
- **In battle:** a bro who starts a fight Embarrassed gets the standard battle status for 2 turns (-20% ATK, -2 Bravado/turn, no Bravado-cost moves; NW:569,583); the field timer keeps running. That is the price of the closet reward, so no free advantage.
- **Not applied by any intoxicant**, in line with the standing intoxication law.

### Questions for the author (Section 2)
- **Q2.1 Duration:** A 90 real seconds / B 60 game-minutes (Recommended) / C 240 game-minutes.
- **Q2.2 Carry into battle:** 2 turns then gone (Recommended) / whole fight / does not carry.
- **Q2.3 Sources:** shame timer + failed QTE + hostel witness (Recommended) / shame timer + QTE only, hostel keeps its own -10 Bravado.
- **Q2.4 Resistance +1:** shortens duration 10% per point (Recommended) / blocks the status outright 10%.

---

## 3. Bottle Opener Keychain passives

### 3.1 Everything canon says, with contradictions

| Claim | Source | Status |
|---|---|---|
| "+3 Party Prep, +1 Bro Credibility, -1 Airport Security" | AD:4 | Removed as "unsupported flavor" at KC:158 ("may return as non-mechanical item-card jokes only after author approval"). Bravado spec: such one-off stats "stay in the design docs and never reach JSON" (`docs/superpowers/specs/2026-08-06-bravado-consolidation-design.md:130-133`) |
| "European bartenders offer better prices and exclusive local brews" | AD:6; AD:29 ("better prices or exclusive drinks because you 'clearly know your beer'") | KC:72,176 say NOT granted unless separately ruled |
| "Certain pub NPCs won't talk to you unless you have 'proper beer credentials'" | AD:30 | Same, KC:176 |
| "In Germany/Czech Republic areas, locals treat you with more respect"; city-by-city reactions | AD:31,34-37 | Real place names, KC:176 "cultural respect" struck |
| "Jangles loudly with every step" | AD:7-8,17 | Cosmetic: progressive jingle by tier, event-based only (KC:168,204,337) |
| Unlocks the Brewery Tour in each city | AD:5 | CONFIRMED (KC:164; BT:45-46 hard gate). Now also: "you have to have the keychain from the blarney trap to collect any opener. none can be gotten without it" (NW:763) |
| Collection tracking: each earned opener is added | BT:61; KC:165 | CONFIRMED |
| Regional beer unlock | BT:62; KC:166; NW:761 (beers buyable only after that opener/stamp) | CONFIRMED |
| Legendary Hangover per city; Continental Beer Master (+1 to all alcohol-based item effects) on full tour | BT:89-90; KC:283-284,291 | CONFIRMED rewards of the TOUR, not of the keychain |
| Photogenic Drinker (+1 Hungover resistance, -10% duration) | BT:79-80; PB:145 | Reward of the selfies |
| Bartenders react to album poses | BT:74-75 | Selfie layer, not the keychain |
| Openers carry no stats | `design/items/brewery_tour/opener_*.md` (cosmetic Special Features only, e.g. `opener_absinthium_taproom_item.md:13`) | Cosmetic |
| "Bartender Recognition" | no hit anywhere | Contradiction 7 |

Net: only gating, collection, and cosmetic jingle are confirmed. Every mechanical passive is open. The keychain's job is already gate + counter; the 12/16 question changes only the count, so the draft keys off **C = cities completed (0-4)** and **O = openers held**, valid for either total.

### 3.2 Draft passive system, three options

Formula (Bartender Recognition, options B/C):

`Price = max(1, round(Base x (1 - 0.05 x C)))`

| Symbol | Type | Range | Description |
|---|---|---|---|
| Base | int | 1-99 | Listed bar price in SOVS (e.g. Absinthe Lager 12, TT:225) |
| C | int | 0-4 | Cities with all breweries completed (4 breweries each, BT:89) |
| Price | int | 1-99 | Bar price paid; applies to bar-served drinks only, never to openers (not for sale) or non-drinks |

Output clamped at 1 SOV (singular, per the money rule). Max discount is 20% at C = 4. Example: Lager 12 at C = 2: 12 x 0.90 = 10.8 -> 11 SOVS; at C = 4: 9.6 -> 10 SOVS.

| | A. Joke Card Only | **B. Credentials (Recommended)** | C. Credentials + Party Prep |
|---|---|---|---|
| Gate: keychain required for any opener, stamp, signature beer | yes (NW:763) | yes | yes |
| Collection counter, jingle tiers, tier art | yes (KC:168,337) | yes | yes |
| Item-card jokes "Party Prep / Bro Credibility / Airport Security" | text only, no numbers | text only | Airport + Credibility text only |
| Bartender Recognition (price break above) | none | yes, 5% per completed city | yes |
| Beer credentials (AD:30): pub NPCs unlock "proper credentials" lines/shops at O >= 1; extra "locals" line per completed city. No stat | no | yes (flag only) | yes |
| Party Prep as a real number | no | no | start of each battle: +C Bravado to each bro (max +4; pools are 12-20, PM:9, NW:554). A fight edge, not an intoxicant edge |
| Risk | Dead item between the gate and the finale | Small economy lever; stacks with Beer Master's +1 only on consumed drinks, not price | Combat lever; its "jangles" joke fits but nothing costs the player (could pair with Q3.3) |
| Matches existing rules | KC:158,176; Bravado spec | KC:176 is lifted by this ruling | Also lifts Bravado spec:130-133 for Party Prep (the spec says those jokes stay as text) |

Out of every option on purpose: exclusive local brews on possession alone (conflicts with NW:761), cultural-respect buffs and city-specific reactions (real place names), and airport mechanics (no airport in canon I found).

### Questions for the author (Section 3)
- **Q3.1 Passive tier:** A Joke Card Only / B Credentials (Recommended) / C Credentials + Party Prep.
- **Q3.2 Bartender discount:** 5% per completed city, max 20% (Recommended) / flat 1 SOV off per city / none, credentials lines only.
- **Q3.3 If Party Prep goes mechanical:** +1 Bravado per city at battle start (Recommended) / pair it with a cost: the keychain jangle gives enemies a first-strike chance / leave it as joke text.
- **Q3.4 Totals:** thresholds by cities (works for 12 or 16, Recommended) / commit to 12 / commit to 16. Also: scrub the real place names from AD copy (yes / no).

---

Cross-system facts to register if approved (not written; `design/registry/entities.yaml` untouched): Green Fairy Essence, `cracked_mirror_shard`, the Bartender Recognition formula, field Embarrassed duration. May I add them to the registry after your answers?
