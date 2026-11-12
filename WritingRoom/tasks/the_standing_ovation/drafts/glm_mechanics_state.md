# GLM — Combat Architecture, Economy & Quest State

**Phase 5 REVISION — Editor Rulings #3 applied.** Corrections this round: affordability claim tightened (§1); **state-lifetime audit — eight flags cut to two** (§2); **the +90 HP exploit killed** (§3); balance assumptions verified against shipped party data (§5); §7 rewritten after full re-verification (the Phase 4 version contained one wrong engine claim — §0 of the enemies file records which). Reviewer: Gemini.

---

## §0 ENGINE VERIFICATION (re-verified this round)

1. `new_game()` starts **gold = 20**, scene `debaucheryville/clocktower_plaza`. No documented Sinfonia arrival balance. Confirms the 20-SOVS anchor and the editor's figure.
2. Shipped `battle_manager.gd` `_win()` **rolls** `drop_chance` before granting; `grant_rewards()` grants an existing item_id unconditionally and skips `""`. (Phase 4's "unconditional grant" claim came from the vertical-slice review docs, which predate the shipped roll. Corrected; enemies file §0 carries the full note.)
3. Reward display calls `DataRepo.get_item(drop)` — **consumables table only**. All five drops need `items/consumables.json` entries (enemies file §0b/§7).
4. `use_item()` heals **party[0] only**, and **consumes what it accepts** — a zero-effect consumable is destroyed by use (the exact clutter the `critic_drop` ruling prohibits). One-line `usable: false` guard proposed (Dependency 8).
5. `flags` is a plain boolean Dictionary; `SAVE_VERSION := 2`; new flags are absorbed with no migration, absent = valid default. Unchanged from Phase 4.
6. `data_repo.gd` hardcodes the Debaucheryville enemy path; `sinfonia_enemies.json` is empty. When the path generalizes, world files must accept present-but-empty tables (the `key_items.json` precedent) or a fresh world boots into a load failure.
7. **No Bravado regen exists in the shipped battle loop**; the only Bravado restore in data is `absinthe_shot` (+8). Pilsner ships with 12 max. District-wide Roast Line budget math is in enemies file §8 — the integrator must not stage multiple mandatory Roast Line checks in one evening.

## §1 ECONOMY — Producer's Circle (sb correction 1, affordability tightened)

**Working value 36 SOVS (24 pours + 12 acknowledgment), reserved table 0 — approved as a Phase 5 working price, explicitly NOT permanent economy canon (editor `economy_circle`).**

**Affordability claim, corrected:** the phrase "reachable through play" in Phase 4 oversold the evidence. What is actually true:
- Hard anchor: 20 gold at new game; nothing else documented.
- The three District fights pay **6–14 SOVS each** (6+14+16 gold = 36 max, once each) — so closing a 16-SOVS gap is *arithmetically possible* from the roster's own gold, but that calculation assumes Sinfonia ambient encounters are the venue's neighbors and the player found them. It is a plausibility case, **not a proven curve**.
- The player can also just not have 36: **the menu entry is grayed at <36, never hidden** (Phase 4, unchanged), and `economy_circle` explicitly authorizes that: the purchase may be visibly unavailable, the quest must not require grinding or invented wealth, and the decline path (D1B) loses zero show content — the Wing table keeps its clean diagonal (verified staged in Kimi's spine §1).
- **Documented for the balance pass:** expected accessibility = "36 is reachable within the quest's own ambient economy if the player takes any fights; never required; a broke player misses exactly one vanity purchase." If Sinfonia's economy pass lands richer, ceiling 48 / floor 24 stand (acknowledgment must remain a real fraction of the bill). If the price changes again, Bradley's line and the receipt recompute together.

**D3B, the quest's only other spend:** three Encores = 30 SOVS at canon price (10 / +30 HP / staff standing ovation). The threshold question stays with the author (§3). **D1B is the legitimized branch at any price.**

**Parked (recorded, not adopted, no ask filed):** the 8–10 SOVS "Acknowledgment à la carte" tier — would answer "why is Jenna rewarding Pilsner?" at the root; changes D1's approved binary shape, so it waits.

## §2 QUEST STATE — the state-lifetime audit (editor `flags` + `glm_mechanics_state` applied)

The editor's audit question — *"do these need persistent storage if their only consumers are within the same evening?"* — was asked and answered honestly, and the honest answer removed **six** of my eight proposed flags. **New registered-flag count: 2.** A flag registers only if it has a **reader outside its own evening/scene**. Everything else is scene-local state in the dialogue runner (the Phase 4 principle), inventory (which is its own persistence), or derivable.

| Surviving flag | Set when | Reader outside its own scene |
|---|---|---|
| `sinfonia.ovation.footage_release_planned` | D4 release | A LATER venue/city interaction (none this quest) + the Axed Critic's Eager state anywhere in the district — both are *different scenes* |
| `sinfonia.ovation.footage_vaulted` | D4 vault | Mutual exclusion with release; prevents any later "you promised us the tape" continuity error |

Audit trail for the six cuts:

1. **`sinfonia.ovation.tape` → cut.** Source of truth: `add_item("chadwick_tape")` — inventory persists across scenes and saves, and "does a tape object exist" is *what a tape is*. Readers switch from `has_flag` to `inventory.get("chadwick_tape", 0) > 0`. PROPOSED item registration for the tape object (see §2.2).
2. **`circle` → cut.** Source of truth: `add_item(receipt_producers_circle)`. Readers: Max's approach variant and the receipt joke check the receipt's existence — the receipt IS the memento; a duplicate boolean is bookkeeping that can desync from the inventory (spend-tracking flags always do). PROPOSED key-item-style entry with `usable: false` semantics under Dependency 8.
3. **`coping_drink` → cut.** One reader: the D3B suppression staging *inside the same scene, after the third glass*. Scene-local variable in the dialogue runner. Durable state it once pretended to provide (the suppression state) is itself presentation-only (§3) and does not survive the scene per the editor's intoxication ruling.
4. **The three `reset_*` flags → cut.** Their ONLY consumer is the one taped frame, selected immediately. Scene-local enum (`reset_method` ∈ {press, wallsit, wedge}, default none), consumed at selection, gone at scene exit. Exactly what the editor's `flags` ruling said the three Biomechanical flags should be.
5. **`rope_resolved` / `palate_respected` (new this round, enemies file §9) → registered.** These are the first-clear gates — persistent by definition, real permanent readers (repeat-encounter behavior), mutual exclusion n/a.

Save/load: both surviving flags are plain booleans absorbed by `SAVE_VERSION 2`, absent = valid default. Replay of the encounter cannot retain stale branch state because **no branch state is persistent anymore** — the scene rebuilds it from inventory + the two flags every time. That is the stale-state proof, structurally, not procedurally.

### §2.2 Proposed item registrations (companion to the flag cuts)

| Item | Table | Class | Reader |
|---|---|---|---|
| `chadwick_tape` | key_items.json | permanent (key) | D4 menu condition; chain-yank; payload table |
| `receipt_producers_circle` | consumables.json (`usable:false`) | souvenir | Max approach variant; receipt joke |
| `relic_claim_ticket` (Jenna's "ONE (1) RELIC — CLAIM BY 2004") | consumables.json (`usable:false`) | souvenir, per `economy_understudy` | none — flavor prop; cut if the author doesn't want inventory clutter |

### §2.3 Per-decision engine notes (updated to the audit)

- **D1A:** gold check (grayed at <36), gold −36, add receipt item. No flag.
- **D1B:** nothing. Absence of the receipt is the state.
- **D2:** three-option menu; only the D2B branch persists state (the tape item). Chain-yank during Event 10 reads inventory. D3's payload table reads inventory + scene-local `reset_method`.
- **D3A:** zero cost, zero items, no state beyond the scene.
- **D3B:** gold −30; **no item grants** (§3 — the HP exploit); suppression presentation swap staged after the third glass.
- **D3C:** scene-local enum; exactly one value; template's write-once contract holds at the enum level.
- **D4:** menu condition = tape item present → Release/Vault (the two persistent flags); otherwise **Reenactment is the exit scene, not a failure state** (sb correction 3). `footage_posted` is NOT set by this quest (q8): no upload, no views, no attention mechanics, anywhere.

## §3 TROUSER SNAKE — implementation spec (f1-compliant, exploit closed)

**Player-facing text is canon and untouched:** +10 Confidence / −25 Concentration / dialogue options temporarily compromised / persists for the remainder of the evening unless suppressed by substantial alcohol. No new numbers.

**Numeric layer:** the two deltas are quest-scoped presentation (Kimi's banner). No engine stat keys exist; the banner does the work. Exact compliance with "no new numbers."

**Compromised-dialogue layer (shipped capability: dialogue-option replacement):**
1. **Post-status (all branches, on contact with service staff):** the full Aion set — *"Yes." / "Yes, please." / "You have a very symmetrical mustache."* (Kimi's `kimi_five_fixes`: these are Bradley's, not Chadwick's.)
2. **During D3:** branch-shaped.
3. **Suppressed (D3B, after the third Encore):** what the player selects is never what Bradley delivers — the compromises get **louder**:

| Player selects | Bradley delivers |
|---|---|
| "Shake it off." | "No. That's still in there. I can feel it going up my spine." |
| "Be normal." | "I'm completely normal. Ask anyone. Ask them normally." |
| "Order water." | "WATER. And none of the— none of the production." |

**Cost audit — three Encores = 30 SOVS — with the exploit fix:**
- Encore is canon **10 SOVS / +30 HP** (venue menu; verified Phase 4, re-verified this round). The venue's separate **Encore! buff** (+5 Bravado, Bravo Challenge) stays uncoupled — no coupling proposed.
- **The +90 HP problem (editor `economy_drinks`, now solved in spec):** if D3B went through the item system as three `the_encore` consumables, `use_item()` would stack **+90 HP** on top of the drink's narrative purpose — free full healing disguised as a coping mechanism, and it would make the optional 30-SOVS spend the single best combat purchase in the game. Fix: **D3B grants no items and calls no `use_item`** — it is a scripted gold deduction (30) plus the presentation swap. The canonic HP value survives untouched in the menu for anyone who *legitimately* orders Encores as drinks; the coping branch simply is not an item loop. Consequence accepted: the branch heals nothing. Which is correct — the joke is that it doesn't fix anything.
- **No ABV is documented for any venue drink.** The suppression trigger therefore stays exactly as the editor ruled: a proposed quest-local threshold (three Encores, after an evening of drinking — the Circle receipt's 24-SOVS pour line is the "prior drinks" evidence), **explicitly not** an established intoxication mechanic, and the author decision (Beer Goggles vs. quest-local vs. new subsystem) is recorded in §9 as THE open question. My editorial note for the author, unchanged: investigate reusing Eurobound's existing Beer Goggles design before creating a new alcohol subsystem.
- **Framing for the medical claim (f1):** Bradley's "It's medical" line stays; **the world visibly declines to agree** — table mockery, Pilsner's toast ("To whatever you took for the thing we don't discuss"), no narrator, no PSA, status not cured, presentation only, duration unchanged. Kimi's cut: make the world's rejection one beat louder without moralizing anyone.

## §4 ENCOUNTER DESIGN LAW (unchanged in substance)

Party combat doesn't exist; `use_item` heals party[0]; battle is Bash / Roast Line / Item / Run against one enemy — **and the shipped party is Pilsner alone** (`party_members.json` contains one member; the solo contract is the shipped state, not an assumption). Every encounter is specified solo-winnable with real math (enemies file §8). Timers are the comedy engine, written to the venue's own cue language (*cue: toast_performance_ui, trigger: Siphon Tier 3*). Distress attacks mirror the approved status DSL.

## §5 SHARED BALANCE ASSUMPTIONS (verified)

- **Pilsner solo anchor is now a verified fact, not my band: HP 45, offense 8, defense 6, luck 4, bravado 12/12, Roast Line ×1.8 / cost 4** — all shipped values. Shipped formula: (off×2 − def) × mult ±2, floor 1, crit = luck%. Baselines and five encounter tables: enemies file §8.
- Fights pay 3–16 SOVS, 5–40 XP. Plausibility case for the Circle gap, not a proven curve (§1).
- Cross-review flags carried: party scaling undefined until party combat lands; Critic's Eager cannot be party-triggered (it isn't — Act IV flag, district-roaming Critic); **Bravado scarcity** (§0.7) is a new district-wide constraint every writer's counterplay must respect.

## §6 FIXED-EVENT ZERO-MENU CONTRACT (unchanged)

Zero player menus between Event 3 and Event 11; the D2B chain-yank is stage business over verbatim lines; the whole runway is one scripted dialogue-runner sequence (`cue: max_enters` → `cue: max_leaves`), no input bound between boundary cues. Verbatim record with the corrected speaker attribution: enemies file §11.

## §7 SOURCE VERIFICATION (this round, files named)

- `game/core/game_state.gd` — gold 20, `grant_rewards` (skips ""), `use_item` (party[0], consumes-and-erases), flags API, `SAVE_VERSION 2`. **Read in full this round.**
- `game/battle/battle_manager.gd` — drop roll, reward display via `DataRepo.get_item`, menu (Bash/Roast/Item/Run), Run 50%, lose → HP 1 + return. **Read in full this round.**
- `game/core/data_repo.gd` — table paths (consumables only for `get_item`), empty-table load behavior. **Read in full this round.**
- `game/assets/data/` — `party_members.json` (Pilsner stats), `party_abilities.json` (roast_line 4 / ×1.8), `consumables.json` (kebab 20 / goulash 40 / absinthe 8 Bravado — no Bravado regen mechanic exists in battle), `key_items.json` (student_id — the precedent for a `permanent` class with no shop economy), `sinfonia_enemies.json` (empty), `debaucheryville_enemies.json` (schema reference, eleven fields).
- Damage formula: `docs/superpowers/plans/2026-07-30-vertical-slice.md` Task 10 (the plan-of-record the shipped calculator implements).
- Venue prices: `the_standing_ovation.md` menu table (Encore 10 / Understudy 4 / Copper 8).
- **Phase 4 correction for the record:** my claim that `grant_rewards` applied drops unconditionally came from the vertical-slice review docs, which predate the shipped roll. The shipped code rolls. Where my Phase 4 file and shipped code disagreed, shipped code wins — recorded in enemies file §0.

## §8 ENGINE DEPENDENCIES (consolidated; new entries from this round)

| # | Dependency | Blocks | Priority |
|---|---|---|---|
| 1 | Generalize `data_repo.gd` enemy/item path loading (allow present-but-empty world tables) | All five enemies summonable | High |
| 2 | `the_encore` real item spec in the venue's item lane — **for menu purchases only, NOT for D3B** (§3) | Legitimate Encore ordering through the item system | Medium |
| 4 | Present-tense stage version of the post-status dialogue set | Post-status scene | Medium |
| 5 | ~~Suppressed presentation flag~~ **scene-local presentation state** (audit result — no register entry needed) | §3 staging | Medium |
| 6 | Lint task for the verbatim runway | Speaker-swap regressions | Low |
| 7 | Party combat scaling (project-wide) | Rebalancing the five sheets post-party | Deferred |
| 8 | `usable: false` honored by `use_item` | Joke drops + receipts as safe inventory | Medium |
| 9 | Consumables entries for the five drops (enemies §7) — cross-world file, author sign-off | Drop display | Medium |
| 10 | Fifth battle action **Wait** + contextual actions (enemies §10) | Ignore/lecture/Break Pose routes in full design | Medium |

## §9 OPEN AUTHOR DECISIONS (unchanged in scope; none blocking drafting)

1. **Intoxication system** — Beer Goggles vs. quest-local threshold vs. new subsystem. Blocks final D3B mechanics only; the scene drafts today.
2. **Circle price 36** — working value with recorded ceiling/floor; final number is the author's at economy balancing.
3. **Parked:** à-la-carte acknowledgment tier (§1) — recorded, not asked.
4. **Suppressed-presentation register entry** — withdrawn this round: the audit made it scene-local; nothing to register.


---

## §10 PHASE 6 SYNCHRONIZATION ADDENDUM (Rulings #4 applied; supersedes conflicting statements above)

Editor `glm_mechanics_state` items 1–7, applied. Where a statement above disagrees with this section, this section wins.

### §10.1 q9/q10 incorporated (ruling item 1)

Both are resolved author rulings; neither is an open question anywhere in this file's §9 anymore.

- **q9: B** — alcohol still dulls TROUSER SNAKE as written; the pill and the performer route fully defeat it. §3's framing line ("the author decision … is recorded in §9 as THE open question") is **superseded**: the question is closed by the author's Intoxication Law + Appendix A; the mechanic now lives in `drafts/glm_intoxication_spec.md` (the ten-point review). D3B's three-Encore threshold is now a **staged dulling beat inside the quest-authored tier curve**, not a competing subsystem proposal.
- **q10: A** — MoonCum696969 is added to the coin pool and spendable with Tony420 (CryptoBro69 and the Shadow Exchange take crypto too; most money in the game is still SOVS). The pill costs **50 MoonCum696969**; no SOVS alternative exists at the ICQ window.

### §10.2 Crypto exception entered in the quest ledger (ruling item 6)

The phrase "the quest's only other spend" (§1) is **superseded**. Quest spends are now: Producer's Circle 36 SOVS (working price), D3B 30 SOVS, and the **ICQ purchase: 50 MoonCum696969** — a crypto debit at Tony420's window, the explicitly authorized exception to junk-coin restrictions (editor `mooncum_economy`). No gold is deducted at the ICQ window and no item grant occurs at purchase; `add_item("flintstone_vitamins")` follows payment. Coin availability ≠ vendor access: if the player holds no MoonCum or never opened Bagholder Assets (`has_inspected_first_crypto_trash`, the AD-04 prerequisite), the pill route is closed **and the performer and decline routes remain fully available** — the vitamin is never a progression gate. The existing airdrop, if collected, makes the 50 deliberately trivial; the break must not represent it as a sacrifice (editor note, already honored in break §9).

### §10.3 Persistent-flag count reconciled (ruling item 4)

The §2 header count ("New registered-flag count: 2") is **superseded**. Pre-overnight persistent flags: **4** — the two footage flags (§2 table) + `rope_resolved` / `palate_respected` (§2 audit item 5, the first-clear gates). Overnight adds **5** (§10.4). **Quest total: 9 persistent entries.**

### §10.4 The overnight's additional persistence (ruling item 5)

From Kimi's break §8; readers audited; my synch findings (`drafts/glm_s5_synch_findings.md` S7/S8) propose two placement refinements Kimi should apply in the break:

| Entry | Set when | Readers | Clear condition |
|---|---|---|---|
| `sinfonia.ovation.flintstone_xanax_active` | Bradley consumes the pill (consumption IS the trigger; item is `usable: true`, zero-heal — see findings S4) | D6 staging; morning Bradley staging; TROUSER SNAKE recurrence/performance suppression | **Next in-game morning only** — never scene exit, dialogue end, hostel arrival, or the decline path (a decline player who ate the pill still carries it to their own next morning; the joke does not require the afterparty) |
| `sinfonia.ovation.afterparty_completed` | V3 cut to black | Morning scene availability; decline exclusion; next-day callbacks | Not cleared (one-shot evening marker) |
| `sinfonia.ovation.campaign_buttons_awarded` | V5 grant | Duplicate-award guard | Not cleared |
| `sinfonia.ovation.inauguration_held` | The single Catastrophe override | Fridge decree + pillowcase sash at **V4** (findings S7: place at V4 so any save ≥V3 still renders them) | Retained through the apartment morning; cleared by the morning scene's exit |
| Evening tier + D5/D6 selections | Authored beats (spec Points 3/5) | Act II / afterparty staging; the morning transition is the only clear point | Serialized with the evening chain; absent = Buzzed default; absorbed by `SAVE_VERSION 2` |

Coupling note (findings S8, recommendation (b) adopted): `afterparty_completed` carries scene availability AND callbacks in one boolean. Two-job coupling recorded as accepted risk in favor of the editor's flag-count discipline.

### §10.5 Per-decision map completion (ruling item 5, xanax correction 4)

**New §2.3 row:**

> **ICQ window (after TROUSER SNAKE lands, before D5):** reachable after **any** D3 outcome (D3A zero-cost, D3B drinks, D3C reset) — the pill route is not gated on the paid drink branch. Engine contract: requires MoonCum balance + `has_inspected_first_crypto_trash`; purchase = crypto debit −50 MoonCum696969, no gold, no item grant at purchase; `add_item("flintstone_vitamins")`; consumption on use sets `flintstone_xanax_active` (until next in-game morning). D5 waits for the player; the window never auto-advances the evening.

### §10.6 Affordability discussion re-audited (ruling item 7)

§1's post-Phase-5 language already states the plausibility-case/not-proven-curve position and that a broke player misses exactly one vanity purchase; re-verified against the ruling. No further edit. Standing correction, unchanged: the intended free solutions (Keeper bypass, Acolyte weathering) award XP/drop, **not** gold — they never fund the Circle.

### §10.7 Encounter-affordability + solo-math caveat (ruling `glm_enemies_full` item 5)

Recorded here as well as in the enemies file: all five encounter tables are computed against the **shipped solo-Pilsner build** (HP 45 / off 8 / def 6 / luck 4 / bravado 12, Roast Line ×1.8 cost 4). When three-character party combat lands, every sheet rebalances (Dependency 7). The enemies file's §8 tables and this file's §4/§5 are synchronized on that caveat.

### §10.8 Open-author-decisions register updated (ruling item 1)

§9 item 1 (intoxication system question) is **RESOLVED** — author's Intoxication Law + Appendix A + this round's `glm_intoxication_spec.md`. §9 items 2 (Circle price at economy balancing) and 3 (parked à-la-carte tier) stand. Item 4 remains withdrawn.
