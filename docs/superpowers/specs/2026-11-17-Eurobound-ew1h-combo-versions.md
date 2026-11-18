# Bros Before Heroes, Wingman Protocol, Double Chug, Selfie Block: The Versions Side by Side (Eurobound-ew1h)

> **Status: COMPARISON ONLY, waiting on the author** (Eurobound Desk `Eurobound-ew1h-q1`).
> Nothing here merges, rewrites or recommends. Every quote is verbatim from
> `design/mechanics/Battle/battle_system.md` (not edited) unless another file is named. Where a field is missing in a version, it says "(not stated)".
> Rulings checked: `docs/superpowers/NEXT_WORK.md:943` (rl4c, combos starter set), `:948` (g0jr-q3),
> `:927` (40ym, Ultimates), `:570` (v27, Stun and Confused), `:569` (Embarrassed). Spec: `docs/superpowers/specs/2026-11-16-eurobound-rl4c-numbers-proposal.md`.
> Proposal (not ruled): `docs/superpowers/specs/2026-11-17-Eurobound-028k-progression-numbers-proposal.md` §6 and §8.
> Model: `docs/superpowers/specs/2026-11-17-Eurobound-397r-combo-versions.md`.

The early sections (Party Dynamics :52-114, Combo Codex :115-197, Combo Bible table :198-212) and the later
"EuroBound Party Synergies & Combos System" (:306-446) each describe these four combos. Inside the early sections the
Codex and the Bible table agree with each other; Party Dynamics sometimes differs in detail.

Facts used throughout:
- **Ruled backfire types** are self-damage, Bravado drain and Embarrassed (battle_system.md:25-28), sized by rl4c: "backfire sizes 5 HP, 3 Bravado, Embarrassed 2 turns" (`NEXT_WORK.md:943`).
- **Ruled combo roll**: "one success roll on the participants combined Bravado tier (High 80%, Mid 60%, Low 40%); a failed roll is the backfire; no Bravado cost, no separate to-hit roll; Embarrassed bros cannot start or join" (`NEXT_WORK.md:943`). A combo starts from "A **Combo** entry in the main-action menu" (rl4c spec `2026-11-16-eurobound-rl4c-numbers-proposal.md:29`).
- **Real Bravado maxima** (`game/assets/data/party/party_members.json`): Lord Pilsner 12, Chadwick 20, Bradley 14 (46 together). None of the four combos, in any version, sets a Bravado total, so none is off the scale.
- **Statuses that exist.** `game/assets/data/skills/status_effects.json` has 42 ids, among them `embarrassed`, `sloppy`, `liquid_confidence`. Stun and Confused are ruled (`NEXT_WORK.md:570`: "Stun: lose the next turn, does not stack. Confused: each action targets someone at random, never the actor.") and built in `game/battle/battle_core.gd:20` (not in status_effects.json). **No status exists anywhere for** charmed, distracted, Protected, Heroic, Rejected, blind or "humiliation".

## 1. Bros Before Heroes

Two versions in battle_system.md, with different partners, triggers and effects, plus gear-set and ladder mentions (§1b).

| Field | Party Dynamics (:85-88) | Combo Codex (:169-174) and Combo Bible (:206) | Synergies section (:359-363) |
|---|---|---|---|
| Who | "(Bradley + Chadwick)" (:85) | "(Bradley + Chadwick)" (:169); "Bradley + Chadwick" (:206) | "(Bradley + Anyone)" (:359) |
| Trigger / setup | "They drop all defense to boost attack." (:86) | "They fist-bump, swearing loyalty." (:170); "Fist-bump loyalty oath." (:206) | "Bradley takes massive damage to protect ally" (:360); Requirements: "Ally at <25% HP, Bradley >50% HP" (:360) |
| Cost | (not stated) | (not stated) | "Bradley loses 25% current HP immediately" (:363) |
| Effect | "+50% ATK, +25% Bravado regen, −DEF for both." (:87) | "Sacrifice DEF → boost each other’s Bravado and DMG." (:171); "Sacrifice DEF → boost Bravado & DMG." (:206) | "Bradley intercepts all damage for ally for 2 turns" (:361); "Ally gets \"Protected\" status (+50% damage, immunity to status effects)" (:362); "Bradley gains \"Heroic\" status (+1 Guts permanently)" (:363) |
| Backfire | (not stated) | "RNG: they actually fight over spotlight, buffs cancel." (:172); "RNG: buffs cancel if egos clash." (:206) | (not stated) |
| Other | "Trigger line: “No man left behind—except defense stats.”" (:88) | Audience: "Crowd chants “BRO-S! BRO-S!”" (:173). Spotlight: "Spotlight swings between them." (:206). Flair: "Unlocks extra in Full Frat Bro gear → “Bros Before Heroes: Deluxe.”" (:174); "Full Frat Bro Set: Unlocks deluxe finisher." (:206) | Flavor: "\"No bro left behind... except my health bar.\"" (:363) |

### 1b. Other versions (third and fourth shapes)

- **Gear unlock, in battle_system.md itself**: "Bradley’s “Full Frat Bro” set unlocks “Bros Before Heroes” as a finishing move." (:112); "Full Frat Bro Set: Unlocks “Bros Before Heroes: Team Finisher.”" (:196); plus the Deluxe lines above (:174, :206).
- **A Bradley-alone Ultimate** in `design/mechanics/Battle/bravado.md`: "Bradley + Full Frat Bro Set → Unlocks hidden ultimate: Bros Before Heroes (party-wide shield, drains his Bravado)." (`bravado.md:78`). This is a third rule set: one bro, a party-wide shield, a Bravado drain.
- **Any two bros** in the ladder doc: "Bros Before Heroes (Any Two) - Sacrifice mechanics" (`design/mechanics/Progression/skilltrees_cloutspells.md:93`), under "Legacy Level (600+ Clout Each)" (`skilltrees_cloutspells.md:91`).

So the partners differ in four places: Bradley + Chadwick (:85, :169, :206), Bradley + Anyone (:359), Any Two (`skilltrees_cloutspells.md:93`) and Bradley alone with a gear set (`bravado.md:78`).

### What each version runs into in the approved rulings

**Party Dynamics, :85-88**
- No backfire is stated. Under rl4c "a failed roll is the backfire", so a failed roll has nothing to resolve.
- "−DEF for both": defense is a real stat (`party_members.json` `defense`); "+25% Bravado regen" has no ruled Bravado regen to scale (the ruled per-turn Bravado changes are Flex +3 and Embarrassed −2, `NEXT_WORK.md:552`, `:569`).

**Codex / Bible, :169-174 / :206**
- "RNG: they actually fight over spotlight, buffs cancel." (:172) is its own random roll. rl4c has one roll, and its failure is the backfire; "buffs cancel" is not one of the three ruled backfire types (self-damage, Bravado drain, Embarrassed).
- No sizes are given ("boost each other’s Bravado and DMG").

**Synergies section, :359-363**
- No backfire is stated (same gap as :85-88 under rl4c).
- "Bradley loses 25% current HP immediately": an HP cost. rl4c rules "no Bravado cost"; it says nothing on HP costs.
- "\"Protected\"" and "\"Heroic\"": neither status exists (see the facts above).
- "+1 Guts permanently": the engine stat is `grit` (`party_members.json`); `party.md:116` calls the stat Guts. A permanent stat gain from a combo meets the 2026-11-16 direction "XP levels for stats, Clout for moves" (`NEXT_WORK.md:919`), under which XP levels raise stats.
- "Ally at <25% HP, Bradley >50% HP": possible with the real HP pools; no impossible condition.

**Gear and ladder mentions (§1b)**
- `bravado.md:78` calls it a "hidden ultimate". 40ym ruled the canon Ultimates as Fratocalypse Now, Going Viral and Final Round's On Me (`NEXT_WORK.md:927`); nothing ruled covers gear-set hidden Ultimates. Embarrassed locks Ultimates (`NEXT_WORK.md:569`).
- 028k proposal §6 (not ruled) places "Bros Before Heroes (:169 / :359)" at Alumni (300) (`2026-11-17-Eurobound-028k-progression-numbers-proposal.md:230`) and lists "Bros Before Heroes: Deluxe / Team Finisher" as a gear combo off the ladder (`:235-236`). The ladder doc puts it at Legacy (`skilltrees_cloutspells.md:91-93`).
- rl4c spec §5 already flagged it: "**Bros Before Heroes**: two different versions (:86-88 and :359-363)." (`2026-11-16-eurobound-rl4c-numbers-proposal.md:78`).

## 2. Wingman Protocol

Same name and same pair in every version; the target, the status and the rewards differ.

| Field | Party Dynamics (:81-84) | Combo Codex (:163-168) and Combo Bible (:205) | Synergies section (:354-358) |
|---|---|---|---|
| Who | "(Chadwick + Pilsner)" (:81) | "(Chadwick + Pilsner)" (:163); "Chadwick + Pilsner" (:205) | "(Chadwick + Lord Pilsner)" (:354) |
| Trigger / setup | "Chad hypes Pilsner to distract NPC." (:82) | "Chad hypes Pilsner to an NPC." (:164); "Chad hypes Pilsner to NPC." (:205) | "Chad hypes up Pilsner to distract/charm enemies" (:355); Requirements: "Facing humanoid enemies, Chad not \"Embarrassed\"" (:355) |
| Cost | (not stated) | (not stated) | (not stated) |
| Effect | "Enemy charmed/confused for 2 turns." (:83); "Success restores both bros’ Bravado" (:84) | "Target is charmed/distracted. 50% chance of full ally buff if they “buy it.”" (:165); "Target charmed/distracted; 50% chance full ally buff." (:205) | "One enemy charmed for 2 turns" (:356); "Pilsner gains confidence boost (+2 Attack)" (:357); "50% chance of bonus party Bravado" (:358) |
| Backfire | "fail = NPC rolls eyes, Bravado drain." (:84) | "NPC rejects → both lose Bravado." (:166, :205) | "Target immune to charm → both lose Bravado, gain \"Rejected\"" (:358) |
| Other | (none) | Audience: "“One bro’s cringe is another bro’s gain.”" (:167). Spotlight: "If successful, Pilsner hogs spotlight; Chad sulks." (:168). Flair: "Varies per region → rejection harsher in Sinfonia." (:205) | "Enemy Types: Works best on club bouncers, barmaids; fails on robots, animals" (:358) |

### What each version runs into in the approved rulings

**All versions**
- **"charmed"**: no charmed status exists in `status_effects.json` or `battle_core.gd`. rl4c spec §5 left the combo out for this reason: "needs a \"charmed\" status and humanoid enemy tags, which are not in the data." (`2026-11-16-eurobound-rl4c-numbers-proposal.md:77`).
- The backfire "both lose Bravado" fits the ruled Bravado-drain type (3 Bravado).
- rl4c "no Bravado cost": no version states a cost, so none conflicts here.

**Party Dynamics, :81-84**
- "charmed/confused": Confused is ruled and built (`NEXT_WORK.md:570`); charmed is not. The line does not say which of the two applies.

**Codex / Bible, :163-168 / :205**
- "charmed/distracted": no distracted status exists. (Two Arcade villain docs use a "Distracted" skip "per PRD §6.8", e.g. `design/worlds/debaucheryville/villains/absinthe_arcade/street_fighter_identity_crisis/player_two_palette_swap.md:137`; that PRD is the dead branch, see §5.)
- "50% chance of full ally buff": an extra chance inside a success, like the ruled 25% viral share of Like & Subscribe. "full ally buff" has no size or status.

**Synergies section, :354-358**
- "Chad not \"Embarrassed\"": already covered by rl4c ("Embarrassed bros cannot start or join"), and it names only Chad.
- "Facing humanoid enemies": enemy entries have no type or tag field (`game/assets/data/enemies/debaucheryville_enemies.json` keys: display_name, battle_intro, max_hp, offense, defense, speed, luck, xp_reward, sovs_reward, item_drop, drop_chance).
- "\"Rejected\"": no such status; it is a fourth backfire effect beside the three ruled types.
- "+2 Attack": the stat is `offense` in the data; it exists.
- One live villain doc already leans on this version: "The Wingman Protocol charm fails into her rejection bark but still counts as a \"humanoid\" target per PRD §6.7" (`design/worlds/debaucheryville/villains/absinthe_arcade/street_fighter_identity_crisis/super_turbo_hyper_jarmila.md:137`). "PRD §6.7" is the dead-branch PRD (`design/legacy/EUROBOUND_PRD.md`).

**Placement**
- 028k proposal §6 (not ruled) places "Wingman Protocol (:163 / :354)" at Alumni (300) (`2026-11-17-Eurobound-028k-progression-numbers-proposal.md:230`); the ladder doc also lists it under Alumni (`skilltrees_cloutspells.md:87-90`).
- Name neighbour (for awareness, not a conflict): Chadwick's skill "Wingman Shout — Taunts enemies, forcing them to attack Chad." (:245).

## 3. Double Chug / Double Chug Disaster

Same pair and same setup; the later version names the statuses and splits failure into two grades.

| Field | Double Chug, Party Dynamics (:75-78) | Double Chug, Codex (:154-160) and Bible (:204) | Double Chug Disaster (:342-346) |
|---|---|---|---|
| Who | "(Pilsner + Bradley)" (:75) | "(Pilsner + Bradley)" (:154); "Pilsner + Bradley" (:204) | "(Pilsner + Bradley)" (:342) |
| Trigger / setup | "They attempt simultaneous chugs to buff." (:76) | "Both try to out-chug." (:155); "Compete to out-chug." (:204) | "Both try to out-drink each other mid-battle" (:343); Trigger: "Both use consumable alcohol same turn" (:343) |
| Cost | (not stated) | (not stated) | (not stated; the trigger spends a consumable each) |
| Effect | "RNG: Buff OR both puke → Stun all allies." (:77) | "Temporary buff if success; if fail, they puke mid-fight." (:156); "Buff if success." (:204) | "Temporary \"Liquid Confidence\" buff OR" (:344) |
| Backfire | "both puke → Stun all allies." (:77) | "AoE stun on party." (:157); "Fail: puke → AoE stun allies." (:204) | "Both gain \"Sloppy\" debuff and puke on each other" (:345); "AoE stun to entire party on critical failure" (:346) |
| Other | "If in Publandia, locals cheer the puke → allies regen small Bravado despite stun." (:78) | Audience: "the crowd audibly loses interest — “A true showing of masculine fortitude… and intestinal weakness.”" (:158). Spotlight: "Neither gains spotlight → crowd jeers." (:159). Flair: "Publandia barmaids mop up, lowering enemy speed." (:160); "Publandia: Barmaids mop up → enemy speed −." (:204) | "In Publandia, crowd cheers the puke → small Bravado gain despite failure" (:346) |

### What each version runs into in the approved rulings

**All versions**
- **Intoxication law.** rl4c spec §5: "built on drinking. It needs the 10-point review in `design/mechanics/intoxication_law.md` first (no intoxicant gives a free advantage)." (`2026-11-16-eurobound-rl4c-numbers-proposal.md:73-74`). No review has been done for this combo. Whether a combo chug counts as a drink on the Buzzed → Catastrophe ladder is not ruled (the sogp review asks the same for Chug & Shrug, `docs/superpowers/specs/2026-11-17-Eurobound-sogp-intoxication-review.md:81`).
- **Party-wide Stun as the backfire.** Stun is ruled ("lose the next turn, does not stack", `NEXT_WORK.md:570`) and built, but it is not one of the three ruled backfire types (self-damage, Bravado drain, Embarrassed). Beeramid uses Stun only on enemies (rl4c).
- **Publandia Bravado on a failure** ("allies regen small Bravado despite stun", :78; "small Bravado gain despite failure", :346): no size; regional modifiers are not ruled for any combo.
- **No Bravado cost** in any version (fits rl4c).

**Double Chug, :75-78 and :154-160 / :204**
- "Buff" has no status or size. The success / fail split fits the rl4c shape (one roll; the failure is the backfire).

**Double Chug Disaster, :342-346**
- **Trigger.** "Both use consumable alcohol same turn" (:343) starts the combo from Item use, which is a minor action (battle_system.md:9). rl4c starts every combo from the Combo main-action entry (rl4c spec `2026-11-16-eurobound-rl4c-numbers-proposal.md:29`).
- **Embarrassed.** An Embarrassed bro can still use Items (g0jr-q3: "Embarrassed blocks Taunt on top of its v27 effects, not Flex or Item" (`NEXT_WORK.md:948`)) but "cannot start or join" a combo (rl4c, `NEXT_WORK.md:943`). The two rules meet under this trigger.
- **Two failure grades.** Sloppy on a failure, party Stun "on critical failure" (:346). rl4c has one roll and no critical-failure tier.
- **Statuses.** `liquid_confidence` and `sloppy` both exist in `status_effects.json`, each with `battle_turns: null` (lengths still flagged as ranges). g0jr-q3 ruled "Liquid Confidence has no Taunt bonus" (`NEXT_WORK.md:948`). Sloppy as a backfire is not one of the three ruled backfire types.
- **Success branch.** "Temporary \"Liquid Confidence\" buff OR" (:344) is an intoxicant buff on success. The standing law: "Intoxicants do not provide uncomplicated, consequence-free advantages." (`design/narrative/bros_choose_debauchery.md:16`).

**Placement**
- 028k proposal §6 (not ruled) keeps "Double Chug, Double Chug Disaster" off the ladder with the backfire combos, "which rl4c left open as \"chosen or happens to them\"" (`2026-11-17-Eurobound-028k-progression-numbers-proposal.md:236-237`).

## 4. Selfie Block / Selfie Sabotage

Different names, different partners and a different mechanism; both are listed as Backfire Combos.

| Field | Selfie Block, Party Dynamics (:72-74) | Selfie Block, Codex (:146-153) and Bible (:203) | Selfie Sabotage (:338-342) |
|---|---|---|---|
| Who | "(Chadwick + Pilsner)" (:72) | "(Chadwick + Pilsner)" (:146); "Chadwick + Pilsner" (:203) | "(Chadwick + Anyone)" (:338) |
| Trigger / setup | "Pilsner swings, Chad selfie-sticks for clout." (:73) | "Pilsner swings paddle; Chad jumps in with selfie stick." (:147, :203) | "Chad tries to film ally's attack for content" (:339); Trigger: "Chad uses \"Selfie Smite\" same turn as ally special" (:339) |
| Cost | (not stated) | (not stated) | (not stated) |
| Effect | "Pilsner smacks Chad, party laughs, Chad loses Bravado." (:74) | "Misses enemy → hits Chad. Self-damage, −Bravado." (:148); "Misses enemy → hits Chad. Self-damage & −Bravado." (:203) | "Chad's ring light blinds ally instead of enemy" (:340); "Ally misses completely, loses Bravado" (:341); "Chad gains \"Embarrassed\" status" (:342) |
| Backfire | (not stated; under the heading "B. Backfire Combos (Ego Ruins It)", :70) | "N/A (backfire is core)." (:203) | (not stated; under "B. BACKFIRE COMBOS", :337) |
| Other | (none) | Audience: "“Truly, a Kodak moment. Shame it cracked his jaw instead of the enemy’s.”" (:149). Spotlight: "Spotlight wasted on Chad’s pain." (:150). Flair: "Sinfonia: Selfie projected on club walls, permanent humiliation debuff." (:152); "Debaucheryville: Pickpockets steal their wallets during the selfie." (:153) | (none) |

### What each version runs into in the approved rulings

**Both**
- **Always a backfire.** battle_system.md:33: "Backfire Combos: guaranteed comedy when synergy collapses." Under rl4c "a failed roll is the backfire", so a combo whose only outcome is the backfire has no success result to roll for. rl4c spec §5: "always backfire. Whether the player chooses these or they happen to the bros is a design question for the author." (`2026-11-16-eurobound-rl4c-numbers-proposal.md:75-76`). Still open.
- **The effects fit the ruled backfire types**: self-damage (5 HP), Bravado loss (3), Embarrassed (2 turns).

**Selfie Block, :72-74 and :146-153 / :203**
- "Pilsner swings paddle": Lord Pilsner's starting weapon is the "Ceremonial Beer Paddle" (`design/mechanics/Battle/party.md:28`).
- "permanent humiliation debuff" (:152): no such status, and "permanent" has no ruled precedent for a combo debuff.
- Pickpocketed wallets (:153): no ruled money-loss effect in battle.

**Selfie Sabotage, :338-342**
- **Trigger.** "Chad uses \"Selfie Smite\" same turn as ally special" (:339) starts the combo from two separate actions, not from the Combo main-action entry (rl4c spec `2026-11-16-eurobound-rl4c-numbers-proposal.md:29`). Selfie Smite is canon: "Special: Selfie Smite — flash blinds foes, but 10% chance he trips while posting." (`design/mechanics/Battle/party.md:45`; ladder rung 100, `skilltrees_cloutspells.md:57`). "ally special" is not defined; party.md gives each bro one "Special" (`party.md:29` Pilsner, `:45` Chadwick, `:61` Bradley).
- **"blinds ally"**: no blind status exists. "Ally misses completely" matches the ruled miss ("a miss does 0 damage", v27, `NEXT_WORK.md:567`).
- **"Chad gains \"Embarrassed\""**: matches the ruled Embarrassed backfire (2 turns).
- **"(Chadwick + Anyone)"**: the ally can be Pilsner or Bradley; Selfie Block is Pilsner only.

**Placement**
- 028k proposal §6 (not ruled) keeps "Selfie Block, Selfie Sabotage" off the ladder with the backfire combos (`2026-11-17-Eurobound-028k-progression-numbers-proposal.md:236-237`).

## 5. Copies and citations outside battle_system.md (not separate canon)

- `design/legacy/Game Files/Markdown Files/combatsystem.md` (and the same file under `legacy setup/`) is an older copy of battle_system.md with the same entries, two to five lines lower (e.g. Bros Before Heroes at :87, :171, :208, :364). Not a different version.
- `design/legacy/EUROBOUND_PRD.md:308-310` (and its copy `EUROBOUND_PRD.md:314-316` at the repo root) has a merged table of Wingman Protocol, Double Chug and Bros Before Heroes. That PRD is the dead branch (`.claude/CLAUDE.md`: "Never treat it as canon"). It is listed here only because live villain docs cite it: `super_turbo_hyper_jarmila.md:137` ("PRD §6.7", humanoid target for Wingman Protocol), and "PRD §6.8" Distracted skips in `two_seventy_vratislav.md:145`, `:190` and `player_two_palette_swap.md:137`, `:193` (same folder). Filed as its own bead.
- 028k §8 (`:274-276`) lists the duplicate names Alpha Sigma Slam / Thunder, Beeramid / Beeramid Blast and Like & Subscribe / Viral Moment. It does not list these four pairs.

## 6. Already settled (not reopened)

- Beeramid and Beeramid Blast: merged by rl4c (`NEXT_WORK.md:943`).
- Alpha Sigma Slam / Thunder and Viral Moment: on the Desk as `Eurobound-397r-q1` (`docs/superpowers/specs/2026-11-17-Eurobound-397r-combo-versions.md`).
- The combo roll, the Embarrassed lock, backfire sizes and "no Bravado cost": rl4c (`NEXT_WORK.md:943`).

## 7. If the author rules

battle_system.md marks the losing entries superseded (no rewrite of the winners beyond what the author says), the ledger
records the ruling, and the 028k §6 combo table (`:229-237`) follows the surviving entries. Numbers, missing statuses
(charmed, Protected, Heroic, Rejected, blind) and the intoxication-law review for Double Chug are separate rounds.
