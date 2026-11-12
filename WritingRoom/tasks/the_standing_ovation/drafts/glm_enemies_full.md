# GLM — The Five Sinfonia Enemies, Consolidated Production Sheets

**Phase 5 REVISION — Editor Rulings #3 applied.** Changes this round: §0 contract corrected against shipped `battle_manager.gd`; new reward-path verification (§1); Supernumerary trigger contradiction resolved per `supernumerary_dispute` (§3); Keeper re-specced after survivability math killed the old block (§5); Keg-Acolyte damage tiers quantified (§6); **new §8 turn-by-turn survivability tables using the shipped damage formula**; new §9 first-clear reward rules; eleven-field schema count corrected. Flags ⚑ = corrections awaiting concept-writer sign-off (Gemini: Critic drop + Keeper re-spec; Aion: Supernumerary stance + Bassoonist prose).

---

## §0 DATA CONTRACT (corrected against shipped code this round)

**Schema: ELEVEN fields per enemy** — `display_name`, `battle_intro`, `max_hp`, `offense`, `defense`, `speed`, `luck`, `xp_reward`, `gold_reward`, `item_drop`, `drop_chance`. (Phase 4 said eight; the editor was right, the count is eleven. My §7 JSON block already carried all eleven.)

**Drop resolution — Phase 4 claim corrected ⚑:** Phase 4 stated `grant_rewards()` applies `item_drop` unconditionally, sourced from the vertical-slice review docs. The **shipped** `game/battle/battle_manager.gd` (`_win()`) ROLLS it: `if _rng.randf() < float(_enemy.get("drop_chance", 0.0)): drop = String(_enemy.get("item_drop", ""))`. Consequences:
- Authored `drop_chance: 1.0` everywhere still behaves as intended (always drops, name displays).
- **Tympanist droplessness is double-safe and now engine-true:** `drop_chance: 0.0` can never pass the roll, and even a spurious `item_drop: ""` is skipped by `grant_rewards()` (`if item_id != ""`). Verified. (Editor request "check `item_drop: ""` against the reward code" — done, it is safe.)
- Reward display calls `DataRepo.get_item(drop).get("display_name", drop)` — **the drop ID must exist in the item table or the victory summary prints the raw ID.** See §1.

`data_repo.gd` hardcodes the Debaucheryville enemy path; `sinfonia_enemies.json` is confirmed empty (`"enemies": {}`) — insertion order is ours and all five names are unique. Note for the implementer: `load_all()` fails loud on an *empty* enemy table (`not _enemies.is_empty()`), so when the path generalizes, world files must get the same treatment as `key_items.json` — present-but-empty is legal, absent is not.

## §0b REWARD-PATH VERIFICATION (new — affects every drop in this roster)

Verified against `game/core/data_repo.gd` + `game_state.gd` this round:

1. `DataRepo.get_item()` reads **`items/consumables.json` only**. Key items and equipment are separate tables (`get_key_item` / `get_equipment`) that the battle win path never consults. → **All five drops must land in `consumables.json`** or their names won't display.
2. `grant_rewards()` → `add_item()` puts the drop into generic inventory regardless of table — the grant works; only the *display and usability* depend on the consumables entry.
3. **`use_item()` consumes what it accepts:** it decrements and erases the item while applying `heal_hp`/`heal_bravado`. A zero-effect consumable is therefore *destroyed by use* — the exact "unusable clutter" the editor's `critic_drop` ruling prohibits. **Required PROPOSED engine guard:** a `usable: false` field honored by `use_item` (one line). Until it lands, joke drops should not be selected as items.
4. **No sell mechanic exists in the engine** — no shop, no gold-for-items path. Every "Sell X SOVS" value in this roster is design prose for a future shop system with **no current reader**. Kept as flavor, labeled PROPOSED.

Landing plan (Dependency 8, §12): one shared `items/consumables.json` is a **cross-world canonical file** — adding Sinfonia entries is an implementation-time author sign-off, not a room-level write. Proposed entries in §7.

---

## §1 THE AXED CRITIC — common / period-reference slot

**Concept: Gemini (integrated).** Bitter print journalist fired in the 2002 dot-com ad collapse, still roasting street life in late-90s/early-00s entertainment-column register. To him the bros are a derivative boy-band reunion that deserves a career-ending pan. Shabby tweed, ink-stained fingers, cracked bifocals on a chain, clutching a 2001 issue of Sinfonia Arts Weekly like a riot shield. (Distinct from the Bassline's in-house Opera Critic: this one is unemployed, outside, and reviews YOU. Aion's ledger, verified.)

**Battle intro:** *An Axed Critic intercepts you with an unprompted retrospective!*

**Kit (Gemini, GLM corrections — Eager gate reviewed by Gemini this round per f3):**
1. **Pan the Production** — single-target takedown in syndicated register (*"Derivative styling, unearned swagger, zero third-act development!"*), ego damage, chance of Embarrassed.
2. **2001 Retrospective** — AoE taunt at the party's cultural relevance (*"You look like the clearance rack of an untelevised VMAs pre-show!"*), Existential Crisis flavored as a defense-debuff window.
3. **Ink-Stained Slander** — fountain-pen swipe, low damage, Grease Fingers-style accuracy-debuff flavor (indelible gall-nut ink).
4. **The Eager Turn ⚑ (unchanged from Phase 4; Gemini sign-off pending):** fires on battle start **only** if `sinfonia.ovation.footage_release_planned` is true. The party cannot cause it mid-fight — the one-turn-kill exploit is closed by construction (the flag is set in Act IV, the Critic roams the district). While Eager: he opens by begging Chadwick for syndication rights to tape nobody has seen (*"I heard rumors of unedited tape! Give me the exclusive!"*), defense halved (a critic approaching a source forgets to defend himself), party crit chance up. He is easier because he is desperate; the player did nothing but tell the truth to a camcorder. **Rumor, not publication** — the flag never means anything was uploaded (q8; editor `gemini_enemies` ruling).
5. **Deadline Distress** (GLM, f2 status-DSL mirror) — on `player_hp < 25%`: *"The Critic is OUT OF TIME and has remembered he is journalists' future."* Defense drop, forfeited next action. The momentum of humiliation is a timer, and the log tells you so.

**Reward (GLM correction to Gemini's fixed drop ⚑ — Gemini to sign off or argue):** **`condescending_review`** — *"A laminated verdict: 'Two stars. One is for the cargo shorts.' It is about YOU. He will be reprinting it."* Fixed-drop economics preserved (engine-true); the joke changes target. Old `shredded_broadsheet` retired. Landing per §7: consumable-table entry, `usable: false`.

**Counterplay:** a single-turn Setup window between retrospective callouts (the search for a comparable — *"he checks his Rolodex for a worse example of you"*): burst it to interrupt a Pan. Withstand the retrospective without flinching (no action spent) and he loses his nerve instead of you. Turn 1 Roast Line on his posture (`illiterate fullback` register, Gemini's) takes 1.5× effect — the tradesman's opening weakness, once per fight. **Balance note (§8):** at shipped numbers he is the cleanest fight in the district — two Roast Lines kill him outright; the Bash route needs exactly one heal.

---

## §2 SUPERNUmerary AMBITIEUX — status-manipulation slot

**Concept: Aion (integrated).** An unpaid opera extra who treats spear-holding as Stanislavski-grade art. Mismatched Roman legionary armor, stage blood on his chin kept for continuity. The bros are his enemies because they NOTICED him — an audience of three cargo-shorted Americans is the review he has waited his whole unpaid life for.

**Battle intro:** *A Supernumerary Ambitieux assumes a ready position! He is already acting.*

### §2.1 THE TRIGGER TABLE (resolves `supernumerary_dispute` — editor-mandated design)

The dispute ruling requires prep / complete / break / challenge to be **distinguishable player-facing states and actions**, and demands the disrespect pun be separated from the de-pose benefit. Resolution — the distinction is **which action the player selects**, never a timing roll:

| Player action (vs. his state) | Result |
|---|---|
| Attack during **Build a Tableau** (the ONE prep turn, telegraphed: *"he strikes an agonized Grecian pose"*) | **Corpsing ×2 damage.** Pose cancelled, he restarts. **Stage Fright is structurally impossible here** — the ×2 bonus and the freeze are mutually exclusive by action type, stated in the move text itself. |
| Explicit **Break Pose** action against the completed pose (PROPOSED contextual menu action) | Removes the defensive stance. **No damage, no Stage Fright.** He deflates visibly (pauldron slips) and restarts next turn. |
| Ordinary attack (**Bash/Roast**) against the completed pose | Damage applies against posed defense, **and** 35% Stage Fright: the attacker forfeits their next 2 actions (*"You've been seen. God, you've been SEEN."*). Attacking his art while he holds it is the disrespectful choice, punished as disrespect — time and cringe, not death. |
| **Wait** through three complete-pose turns (PROPOSED fifth battle action, §10) | **Attention denial — he leaves.** *Note From the Director: "they weren't ready."* Zero risk, zero reward, the funniest outcome. Editor `supernumerary_dispute`: preserved, not lost in the state machine. |

Posed defense: base 5 → 9 while posed. Prototype fallback: with only the shipped four-button menu, the Wait route is unavailable (can't stand still, can't Break Pose); the fight still works — prep-interrupt (×2) or grind through posed defense — but the joke needs the full design. Both variants documented for the integrator.

**Party-combat fix (deferred per §0.4 Phase 4):** in a three-member party, damage across ALL members de-poses him — his art requires a single unbroken line of sight. Recorded for the party-combat dependency, not authored now.

**Reward:** **Gold 0** (unpaid; the empty wallet IS the premise — Gemini's sign-off held). XP 11. Fixed drop **`crumpled_headshot`** (Aion's) — laminated 8x10 in full legionary kit, autographed to nobody, printed email with "2007" in it. Landing per §7.

---

## §3 SECOND CHAIR BASSOONIST — group / reinforcement slot

**Concept: Aion (integrated), GLM corrections applied.** Twenty-two years of second chair; wrinkled white-tie tuxedo; colossal wooden bassoon braced like an anti-tank weapon; furious that a laptop now does his job and doesn't even have a chair. The bros are the century's current representatives, and one of them asked if the bassoon is "one of those big clarinet things."

**Battle intro:** *A Second Chair Bassoonist takes issue with you! Also with the century!*

**Kit:**
1. **Cracked Reed** (unchanged — Aion's do-not-smooth note stands): built-in 25% miss chance on his attacks, +10% per taunt.
2. **Low C** (unchanged): two visible inhale turns, then armor-piercing bottom-C; lands a quarter-tone sharp, self-debuff **Sharp** (offense −2 for 3 turns — he heard it). **The district's only two-turn telegraph** (Gemini's distribution ruling; the Supernumerary moved to one prep turn).
3. **Union Break — ONE USE PER ENCOUNTER** (editor-mandated): when he calls for backup, what arrives is **The Reed Section's Break** — a **Tympanist on Break** (half his HP, a thump that has a 30% chance to hit whoever was conducting — at solo table that is *himself*, the fight's best self-own; log names the victim, per Kimi) and an **Overworked Oboist** (weaker; her one lecture — *"real musicians don't crunch during the opera"* — inflicts Embarrassed, usable once, then only zero-effect breath-support criticism). **The summons are permanently weaker than he is.** Solidarity arrives on break, stays broken, and his own action economy pays for the phone call.
4. **Key-click** (Kimi's telegraph + cooldown, applied): whenever the party uses an item, he clicks his keys — the pit musician's decades-deep contempt reflex — for a token free hit. Telegraphed first time (*"He is watching your inventory. He has opinions."*), cooldown 2 turns so item healing can't be punished into a loop.

**Solo survivability — Phase 4 prose corrected with real math (§8, table B):** the fight is **three turns**, not the "4–5 turns" I wrote in Phase 4. With one taunt stacked (+10% reed miss) and his Sharp self-debuff after the first Low C, his effective damage averages ~4–6/turn against Pilsner's defense; total damage taken across a clean kill is under 20. No healing required. The wall is his HP; the adds are furniture that hits like pillows.

**Reward:** gold 14 (union scale — he has money, it's just never enough), XP 16, fixed drop **`spare_reed`** (Aion's; proposed Embarrassed-cure consumable — effect itself PROPOSED pending status review; ships as an inert collectible per §7 if the status system isn't ready). Tympanist dropless (§0). Oboist also drops `spare_reed` (1.0) — same item, so the table gains one ID, not two.

---

## §4 (reserved — numbering preserved from Phase 4)

---

## §5 KEEPER OF THE ROPE — rare / spatial-rule slot (RE-SPECCED after survivability math ⚑)

**Concept: Gemini; structure corrected by GLM. Phase 5: stats re-cut because the Phase 4 block (68 HP / 12 offense / 10 defense) is mathematically unwinnable solo — see §8, table D.** A bouncer whose entire identity rests on a four-foot decorative velvet rope not connected to any wall — the venue's own canon says its ropes are *decorative, not exclusive*. Ten feet of clear walking space on either side.

**Battle intro:** *The Keeper of the Rope bars an imaginary VIP boundary!*

**New stat block:** **HP 52 / offense 9 / defense 7 / speed 4 / luck 1.** Design law this encodes: brute-forcing a decorative rope is the most expensive option in the district — survivable only with real item investment or near-death — while every correct solution is free. The joke is now load-bearing in the numbers.

**Layer 1 — environmental bypass (unchanged):** observant players read the open flanks (examine text: *"A majestic velvet rope guarding three square feet of polished linoleum. You could easily walk three paces to the left."*) and walk around. The Keeper glares, adjusts his cuffs, combat never triggers. Restraint as literal counterplay.

**Layer 2 — combat, two tiers:**
1. **The written-rule tier (Gemini, kept):** *Redefine the Velvet* repositions the rope diagonally and declares zones off-limits (players caught inside lose physical attacks until they spend an action *Stepping Outside the Line* — PROPOSED repositioning action, §10). *Check the Clipboard* cancels an undeclared action (*"You're not on the manifest."*). *Stern Velvet Whip* — the RARE slot hits like the costume implies; damage up from Phase 4's draft, and the knockback feeds *Redefine the Velvet* (you're shoved INTO the declared zone). **No two-turn windup** — he owns spatial rules, not charge timers (editor `combat_rhythm`).
2. **The unwritten-rule tier (GLM):** CAN-DO polish, no other talent. **Roast Line ladder — exactly two rungs, in-battle, mechanical:**
   - **Roast #1:** he answers with better policy (*"Regulations state the boundary is conceptual!"*) and **forfeits his next action** re-pressing the rope's non-existent creases.
   - **Roast #2:** policy collapse. He abandons combat posture entirely to measure floor tiles with a clipboard (*"The floor plan is… aspirational."*) — **the encounter ends as a win with full rewards**: a man defending a boundary nobody signed, beaten by two sentences. Phase 4's separate defense-drop and floor-measuring fates were two endings for one joke; merged into this single escalation (⚑ Gemini to confirm).
   - Bravado check: two Roast Lines cost 8 of Pilsner's 12 — affordable from a fresh battle, tight after a district's worth of roasting (see §8 note on Bravado scarcity).

**Nonviolent resolution (unchanged, reward consequence explicit):** present Chadwick's `press_napkin` prop or Pilsner's expired license. He inspects the ink under a magnifying glass, murmurs *"Your accreditation is dangerously irregular, but the typography is confident,"* unhooks the brass latch with grand ceremony, and lets the party through. Full XP, full drop. The fictional credentials work because he cannot tell the difference between fiction and policy — the fight and the bribe are the same joke at two difficulty settings.

**Reward:** gold 15, XP 35, fixed drop **`decorative_brass_stanchion_clip`** — *"Regulation-grade. For a regulation that does not exist."* **First-clear gating: §9** (the nonviolent route is otherwise a three-second infinite XP/item farm — editor `missed_gameplay_defects` #3; fixed).

---

## §6 THE DRAMATISCH KEG-ACOLYTE — elite / mini-boss slot (GLM; Phase 5: damage tiers quantified)

**A parish of one** (editor ruling 01 honored). Rubber cellar apron, welder's goggles pushed up, brass CO2 manifold worn like a bandolier, the thousand-yard serenity of a man who has found the answer, and the answer is head retention.

**Battle intro:** *A Dramatisch Keg-Acolyte demands you appreciate The Head!*

**Phase 5 stat block:** **HP 48 / offense 11 / defense 6 / speed 3 / luck 2** (from 55/13/6 — the 13 made even the intended patient route mathematically fatal before the lecture; see §8, table E).

**Premise:** he is not hostile. He is EVANGELICAL. The bros asked for a beer without commenting on the head, and that is a pastoral emergency. The fight is his lecture. The comedy is that he is genuinely, technically right about everything, and cannot imagine why that doesn't end the conversation.

**Kit (numbers now explicit):**
1. **Siphon Spray** — pressurized jet. **Tier damage: 8 → 14 → 22**, escalating one tier per turn, holding at Tier 3. (Phase 4 said "moderate, escalating" with no numbers; the editor's survivability demand applies to tiers too.)
2. **The Head Foam Meter** — the tier counter lives on the ACOLYTE and on PILSNER'S OWN STEIN; the sprite's pour visibly thickens; the caption reads *"appreciation presumed."* HIS meter.
3. **The Lecture — available from ANY tier** (Phase 5 clarity fix): at Tier 3 — or after the party **Waits twice consecutively** — he stops attacking and delivers the head-retention lecture in three escalating couplets, telegraphed in the venue's own cue language: *"cue: toast_performance_ui, trigger: Siphon Tier 3"* / after the second consecutive Wait: *"The pressure gauge is near red. He draws breath for THE LECTURE."* **Weather it (three Waits, zero attacks) and he salutes the party's discerning palate and leaves mid-fight** — awarding his drop and the encounter's respect. **A mini-boss you can lose to politely.** Fleeing spares the damage but counts as a walkout: no drop, and the log tells you so (*"He pronounces your palate underdeveloped to the empty alley."*).
4. **Low Gear** (f2 contract, unchanged): the CO2 jet is raw low-pressure combat math, no fizz status. His real control tool is **Applause Forfeit** — while Acolyte-instigated applause is pending, the party's Bravado regen pauses (the room is busy clapping for beer).

**Counterplay, now numeric (§8, table E):** burst route = exactly three full-Bravado Roast Lines (survivable by ONE hit point at full HP, no crits taken — impatience is survivable only by your single best behavior); patient route = two Waits + three lecture Waits for ~22 total damage and the best drop in the quest; Run always available at 50%. Three exits, no optimal one, the funniest one is free.

**Reward:** gold 16, XP 40, fixed drop **`dramatisch_dunkel`** (Kimi's Phase-2 item: 12% cellar brew, **heal_hp 40**, *"Obliterates the faculty of regret."*) — the quest's best consumable, given for LISTENING. **First-clear gating: §9.**

---

## §7 PROPOSED ITEM ENTRIES (new — the consumables.json landing for every drop)

All five drops land in the shared `items/consumables.json` (§0b). `usable: false` requires the one-line `use_item` guard (Dependency 8) — until it ships, these must not be selectable as items. Sell values are future-shop flavor, no current reader.

```json
"condescending_review": {
  "display_name": "Condescending Review",
  "heal_hp": 0, "heal_bravado": 0, "usable": false,
  "description": "A laminated verdict: 'Two stars. One is for the cargo shorts.' It is about YOU. He will be reprinting it."
},
"crumpled_headshot": {
  "display_name": "Crumpled Headshot",
  "heal_hp": 0, "heal_bravado": 0, "usable": false,
  "description": "An 8x10 in full legionary kit, autographed to nobody. The printed email address contains the year 2007."
},
"spare_reed": {
  "display_name": "Spare Reed",
  "heal_hp": 0, "heal_bravado": 0, "usable": false,
  "description": "A reed for an instrument you have never played. Given with the contempt of a man parting with nothing."
},
"decorative_brass_stanchion_clip": {
  "display_name": "Decorative Brass Stanchion Clip",
  "heal_hp": 0, "heal_bravado": 0, "usable": false,
  "description": "Regulation-grade. For a regulation that does not exist."
},
"dramatisch_dunkel": {
  "display_name": "Dramatisch Dunkel",
  "heal_hp": 40, "heal_bravado": 0, "usable": true,
  "description": "The 12% cellar brew. Obliterates the faculty of regret. Restores 40 HP."
}
```

(`dramatisch_dunkel` is the one real consumable; +40 HP matches the goulash tier. The Encore/Encore! separation is unaffected — this is a different drink.)

---

## §8 SOLO SURVIVABILITY — DETERMINISTIC TABLES (new; editor `missed_gameplay_defects` #4)

**Shipped formula** (plan-of-record, `docs/superpowers/plans/2026-07-30-vertical-slice.md`, Task 10 — matches the calculator the shipped `battle_manager.gd` calls): `damage = (offense×2 − defense) × multiplier ± 2, floor 1; crit chance = attacker luck × 1%, crit ×2.`
**Pilsner (shipped `party_members.json`):** HP 45, offense 8, defense 6, luck 4, bravado 12/12, skills: roast_line (×1.8, cost 4). **The shipped party is Pilsner alone** — the solo contract is not an assumption, it is the shipped state.
Baseline: Bash 4–8 avg ~6.2 vs def 10; ~12.5 vs def 4; ~9.4 vs def 7; ~10.4 vs def 6. Roast Line ×1.8 on those bases: ~11.3 / ~22 / ~16.9 / ~18.7. Enemy crits add attacker luck ×1% — noise-level for luck ≤4; noted where it matters.

| # | Encounter | Enemy (HP/off/def) | Player route | Turns | Damage taken | Verdict |
|---|---|---|---|---|---|---|
| A | Axed Critic | 42/9/4 | 2× Roast Line | 2 | ~25 | **Wins, no heal.** (Bash route: 4 turns, ~50 — needs 1 kebab.) |
| B | Bassoonist + Break adds | 34+16+18/7/3 | Taunt T1, Bash ×3 | 3 | ~18 | **Wins, no heal.** Adds hit ~2/turn or each other. |
| C | Supernumerary | 26/5/5 (posed def 9) | Prep-interrupt ×2, then Bash | 3 | ~12 | **Wins, no heal.** Stage Fright route: +~2 forfeited turns, ~24 — survivable cringe. |
| D | Keeper of the Rope **(re-spec)** | 52/9/7 | Full Bravado: 3× Roast + 1 Bash | 4 | ~48 | **Needs ≥1 kebab or dies by a hair.** Brute force = the expensive option. |
| D′ | Keeper — correct routes | — | Walk around / 2× Roast ladder / credentials | 0–4 | 0–48 | **Free, free, free.** The design wants you here. |
| E | Keg-Acolyte **(re-spec)** | 48/11/6 | 3× Roast Line (full bar) | 3 | ~44 | **Survives by 1 HP, zero crits.** The impatience tax. |
| E′ | Keg-Acolyte — patient route | 48/11/6 | Wait, Wait, lecture ×3 | 5 | ~22 | **Wins with the best drop.** One kebab makes it comfortable; below ~60% HP it's a Run call. |
| F | Phase 4 Keeper block (68/12/10) | 68/12/10 | any | 11+ | ~200 vs 45 HP | **Mathematically unwinnable solo.** This is why §5 was re-specced. |

**Bravado scarcity (district-wide, affects everyone's Roast Line counterplay):** the shipped battle has **no Bravado regen** — it only decreases; the sole restore in data is `absinthe_shot` (+8). Pilsner carries 12. Demand across the roster if every route is taken: Critic 8 + Keeper ladder 8 + Acolyte burst 12 = 28 against 12 + absinthe. The routes are ALTERNATIVES by design — each encounter has at least one zero-Bravado exit (this is why the tables above lean on Bash routes too). Integrator: do not stage multiple mandatory Roast Line checks in one evening's sequence.

## §9 FIRST-CLEAR REWARD RULES (new; editor `missed_gameplay_defects` #3)

Shipped engine fact: enemies respawn on scene re-entry (`spawn_enemy` in `_ready()`) and death costs nothing but progress (`_lose()` sets HP to 1 and returns the player). Unlimited re-farming is therefore possible TODAY. The special-grant routes are the exploitable ones (bypass the Keeper = 35 XP + item in three seconds; weather the Acolyte = the best consumable, repeatedly). Fix — **scene-wrapped grants, gated by persistent flags** (battle manager can't do this; the quest scene around the trigger does):

| Flag | Set on | Read by | Repeat behavior |
|---|---|---|---|
| `sinfonia.ovation.rope_resolved` | ANY first Keeper resolution (bypass, ladder, bribe, or KO) | the foyer trigger | Afterwards the Keeper is a one-line NPC: *"The boundary is conceptual. Move along."* No repeat grant, no re-battle. |
| `sinfonia.ovation.palate_respected` | first Acolyte lecture/weathering | the alley trigger | Afterwards he nods from the cellar door and returns to his pour. No repeat drop. |

Ambient gold re-farming (Critic/Bassoonist respawn) is a general economy question, not this quest's blocker — noted for the Sinfonia economy pass (open item, §12).

## §10 BATTLE-ACTION CLARITY (new; editor `missed_gameplay_defects` #2)

The shipped menu is exactly four buttons: Bash / Roast Line / Item / Run (50% flee; failed Run = enemy turn). Three of this roster's best jokes need actions that don't exist. **PROPOSED full-design UI:** a fifth baseline action **Wait** (pass; enemy turn proceeds; per-encounter flavor line — the Supernumerary's ignore route, the Acolyte's lecture-weathering) and a **contextual action** that replaces Wait when the target's state allows it (**Break Pose** vs a completed tableau; **Step Outside the Line** while zoned; the Keeper's ladder needs no new button — Roast Line exists). **Prototype-shippable fallbacks, stated honestly:** without new buttons, the Supernumerary still works (prep-interrupt / grind; the ignore joke waits for full design), the Acolyte's patient route is unreachable (burst or Run — the tier table still holds), the Keeper is Bash-and-items or the overworld bribe. Documented so integration stages the right version against the right build.

## §11 FIXED-EVENT SOURCE VERIFICATION + VERBATIM RECORD

Three passes over the dossier encounter text and `max_vex.md`, comparing speakers against the dossier beat numbers, then against the ruling's quoted block, then against Kimi's spine — **Event 10 order confirmed: Max asks; Chadwick answers.** (Pass 1 found a dangling dossier attribution on the walk-away lines — the dossier text attributes them to CHADWICK; the ruling and `max_vex.md` say MAX. **Ruling and NPC profile win; dossier attribution is treated as a transcription artifact.** Recorded so the next verifier doesn't re-fight it. Flagged to Kimi for her final pass.) Runway record, zero quotation marks, bold-only attribution:

> **MAX:** Hey! It's Beer Lord, Trouser Snake and…
>
> *(Max looks at Chadwick.)*
>
> **MAX:** …what did you say your name was again?
>
> **CHADWICK:** Chadwick.
>
> **MAX:** Right.
>
> **CHADWICK:** You know my name.
>
> **MAX:** Do I?

## §12 REVIEW MATRIX, DEPENDENCIES, OPEN FLAGS

| Sheet | Concept | Mechanic corrections by | Full-sheet reviewer |
|---|---|---|---|
| Axed Critic | Gemini | GLM (reward, Eager gate) | Kimi |
| Supernumerary Ambitieux | Aion | Gemini + Kimi + GLM (§2.1) | Kimi |
| Second Chair Bassoonist | Aion | GLM (Union Break, Key-click, §8 correction) | Kimi |
| Keeper of the Rope | Gemini | GLM (§5 re-spec, ladder merge) | Kimi |
| Keg-Acolyte | GLM | — | Kimi + Aion |

**New dependencies this round:**

| # | Dependency | Blocks | Priority |
|---|---|---|---|
| 8 | `usable: false` honored by `use_item` (one line) | All four joke drops as safe inventory | Medium |
| 9 | Consumables entries (§7) in the **shared, cross-world** `items/consumables.json` | Drop display; author sign-off at implementation | Medium |
| 10 | Fifth battle action **Wait** + contextual actions (§10) | Ignore/lecture/Break Pose routes in full design | Medium |

(Carried from Phase 4: #1 data-path generalization — with the new note that empty-but-present world files must be legal, per the `key_items.json` precedent; #2–#7 unchanged.)

**Open flags:**
1. ⚑ Gemini sign-offs: Critic drop swap (§1), Keeper re-spec + ladder merge (§5). ⚑ Aion sign-offs: Supernumerary trigger table (§2.1), Bassoonist survivability correction (§3).
2. Default Critic battle text must carry the common slot alone for players who never arm the camera (Eager is a rare flavor state). Kimi, on review.
3. All enemy stats are PROPOSED; the §7 item entries are PROPOSED; nothing here is authorized to change game files.


---

## §13 PHASE 6 ADDENDUM — RULING `keg_acolyte_dispute` + `glm_enemies_full` ITEMS 1–5 APPLIED

Where this addendum disagrees with §6 above, this addendum wins.

### §13.1 Applause Forfeit is DEAD — replaced by the APPLAUSE LOCKOUT (ruling item 1; Kimi's proposal adopted by the editor)

**Delete §6.4's Applause Forfeit entirely.** There is no Bravado regeneration in the shipped loop; the mechanic paused nothing and taxed the wrong route.

**Replacement — the Applause Lockout (encounter-local, comedic, patient-route-safe):**

- **Trigger:** the moment a **Roast Line lands on the Acolyte**, the room erupts — the bros have jeered the one man the house actually loves, and the house answers with applause *for the beer*. Telegraph line on the landing turn: *"The room roars its approval. Of the beer. He bows."*
- **Effect:** on the party's NEXT turn, **Roast Line is locked** — the button grays with one line: *"Nobody can hear you. They're still clapping."*
- **Constraints (editor-mandated):** telegraphed (the landing-turn line above is the telegraph); fires **at most once per encounter** (the second Roast lands in ordinary silence); **never removes or disables Wait** — the patient route's action is untouchable by design, because the applause is *caused by Roasting*, and a party that never Roasts is never locked out.

**Burst-route math with the lockout (§8 table E updated, same verdict):** T1 Roast (18.7, lockout telegraphs) → T2 locked → Bash (~10.4) → T3 Roast (18.7) → T4 Roast (18.7). Cumulative ~66.5 vs 48 HP: dead at T4. Damage taken across T1–T3: 8 + 14 + 22 = **~44 vs 45 HP — survives by 1 HP, zero crits, four turns instead of three.** The impatience tax now includes one turn of shouting into applause. Patient route unchanged: no Roast, no lockout, 2 Waits + 3 lecture Waits, ~22 taken.

### §13.2 Wait counts, stated explicitly (ruling item 2)

**The lecture initiates after TWO consecutive Wait actions** (telegraph after the second: *"The pressure gauge is near red. He draws breath for THE LECTURE."*). **Weathering it requires THREE further Waits** (the three couplets). Five Waits total on the patient route; zero attacks; ~22 damage; the best drop in the quest. §6.3's prose already carries these numbers; this section is the verification the editor asked for. The `available from ANY tier` clause stands — Tier 3 also opens the lecture without any Waits.

### §13.3 FULL-DESIGN-ONLY label (ruling item 3)

**The shipped build is the four-button menu: Bash / Roast Line / Item / Run. The following do not exist in it and must not be staged against it:**

- The **Acolyte patient route** (Wait ×2 + lecture ×3) — no Wait button. Prototype reality: burst route (§13.1) or Run.
- The **Applause Lockout** — no contextual disable capability.
- The **Supernumerary's ignore route** (Wait ×3) and **Break Pose**.
- The **Keeper's Step Outside the Line** action.

§10 lists these with fallbacks; this is the prominent banner the editor required. Integration stages the right version against the right build — the four-button build ships the encounters with burst/grind/bribe routes only, and the log says nothing about missing jokes.

### §13.4 First-clear coverage extended (ruling item 4)

`rope_resolved` already covers **all** first Keeper resolutions (bypass, ladder, bribe, KO) — unchanged, verified against §9.

`palate_respected` is **extended: set on the FIRST Keg-Acolyte resolution that awards benefits — the lecture-weathering OR a burst-route KO (the KO pays gold + XP + the rolled `dramatisch_dunkel` at drop_chance 1.0, so it is exploitable exactly like the bypass was).** Repeat behavior splits on how it was first cleared:

- Cleared by **weathering**: the cellar-door nod, *"He returns to his pour."*
- Cleared by **KO**: he is simply back at his pour and pointedly does not acknowledge the party — no repeat drop, no nod, no comment.

Either way: one dunkel per save file, from one route, once.

### §13.5 Solo-build caveat (ruling item 5)

The §8 tables, the §13.1 burst math, and every stat block in this file are computed against the **shipped solo-Pilsner build** (HP 45 / off 8 / def 6 / luck 4 / bravado 12, Roast Line ×1.8 cost 4). They are NOT balanced for the future three-character party; when party combat lands, all five sheets rebalance (Dependency 7). The math is preserved as the design-law record of what each joke costs one man.
