# Phase 1 — GLM (combat/data/mechanics)

## 1. The enemy data contract (what "production-ready" actually means here)

### 1.1 State of the repo
- `game/assets/data/enemies/sinfonia_enemies.json` exists and is **EMPTY**: `{ "schema_version": "1.0", "world_name": "sinfonia", "enemies": {} }`. Our five are the **first Sinfonia enemies in the game**. No existing Sinfonia enemy names to collide with; debaucheryville has exactly one (`feral_segway_tourist`), Publandia is empty.
- **Schema is fixed by the one shipped enemy** (`debaucheryville_enemies.json`):
  `display_name`, `battle_intro`, `max_hp`, `offense`, `defense`, `speed`, `luck`, `xp_reward`, `gold_reward`, `item_drop`, `drop_chance`. Snake_case id, human display name. Note: the money field is called `gold_reward` — values are SOVS (project currency), only the JSON key is legacy.
- `game/tests/unit/test_data_repo.gd` asserts the shipped enemy's exact shape (`max_hp == 28`, `item_drop == "lukewarm_kebab"`). Extra keys won't break tests; **missing keys will crash the battle scene**: `battle_manager.gd` indexes `max_hp` and `display_name` directly (no defaults).

### 1.2 What the running engine can actually deliver (be honest in final.md)
- Battle is **one bro vs one enemy**: `_member = GameState.party[0]`. No three-bro turn economy, no combo menu, no Ego meter, no regional beat-sync. The `battle_system.md` +25% layer is design lore, **not implemented** — do not cite its features as working mechanics in final.md.
- Enemy turn = one plain attack via `DamageCalculator`. **There is no enemy status, attack-list, or AI system in code.** `enemyai.md` is literally the placeholder text "Temporary placeholder."
- Player options are: Bash, Roast Line (one scripted ability), Item (hardcoded: lukewarm_kebab / questionable_goulash / absinthe_shot), Run (50%).
- Consequence: **enemy personality must live entirely in `battle_intro`, stats, and the drop item** — that is what the engine renders today. A funny intro line IS the enemy's voice. Anything more (status attacks like *Embarrassed*, taunt AI, behavior scripts) is an engine extension and must be marked PROPOSED, never shipped as if supported.

### 1.3 Drop items are a hard dependency
`_win()` resolves the drop's display name via `DataRepo.get_item()`, and the Item menu hardcodes three consumables from `game/assets/data/items/consumables.json`. So each of our five enemies needs a matching consumables.json entry (`display_name`, `heal_hp`/`heal_bravado`, description) or the player sees a raw id and can't use the drop. Existing economy anchors: Lukewarm Kebab +20 HP / 8 Sovs-ish street food; Absinthe Shot +8 Bravado; Questionable Goulash +40 HP. Enemy drops should sit at or below those values.

### 1.4 Balance anchors (provisional bands, PROPOSED)
- Party reference: Lord Pilsner max_hp **45**, offense 8, defense 6, speed 5, bravado max **12**.
- Shipped enemy: HP 28 / off 6 / def 3 / spd 6 / luck 2 / **xp 12 / gold 8** / drop_chance 1.0.
- Starting wallet: **20 gold**. Venue menu runs 4–10 Sovs; the venue's collectibles run ~10–25 Sovs; audition bills run 216–388 SOVS.
- → Proposed Sinfonia Opera District bands: **HP 18–55, offense 5–9 (party DEF 6 = dangerous but survivable), speed 2–9, luck 2–7, xp 12–20, gold 5–12, drop_chance 1.0**. Enemies are pocket-change, not income — the money jokes belong to the venue, not the corpses.

### 1.5 Where encounters fire (needs author framing, see ask)
Engine battle flow is a single `pending_enemy_id` fired through SceneRouter. The revue itself is a scene, **not a combat space** — putting fights inside the show means new scripting plus interrupting the one scene the author has choreographed beat-by-beat. My recommendation: the five are **ambient Opera District night encounters** (alley, queue, ticket line, post-show street), available before/after the revue. Options logged in the ask.

### 1.6 Name-unique check (done)
No repo hits for Supernumerary / Woodwind / Keg-Acolyte / the five Gemini concepts. "Fermented" exists as a beer-buff term only. Gemini's five names are clear to adopt as proposals. Two notes: Gemini's #2 embeds Herr Dramatisch's name in an enemy id ("dramatisch_keg_acolyte") — playable as faction naming, flag if the author minds; "Feral Critic" reuses the word "Feral" from `feral_segway_tourist` (distinct name, fine, reads as a series).

## 2. Mechanics audit of the four auditions (choices, costs, statuses)

**Aion:** 2 real decision points of the required 3 — the "tribute act" menu converges to identical continuation (fake choice, brief §5), coping choice 2-way is real. **216 SOVS is unavoidable** (brief §4 violation: no escape from the itemized bill). Berlin Wall named verbatim — real place, needs a parody swap. His status-mapping caveat (TROUSER SNAKE as quest-local modifier block, not new global stats) is correct and matches code.

**Gemini:** the "three seating tiers" are three prices for the same bill — one decision wearing three hats (§5 failure). His five enemy concepts are the strongest creative base we have; each needs role/stats/drop/encounter-slot to reach the §7 bar.

**GLM (mine):** the deciding vote is one genuine 3-way branch; the N-Gage *sleeve* gag is the right shape (the purchase must be player-initiated); but **~388 SOVS of stacked mandatory fees violates §4** exactly like Aion's. Kimi's ordering note is correct: my draft puts Bradley's beat before "Beer Lord"; the dossier flow is Beer Lord → Chadwick non-nickname → Basketball Jersey → Trouser Snake. Reorder in round 2. Concede the velvet tip pouch stage direction — Max takes tips, Max sells nothing; keep the line, cut the prop business that makes them look like they're working a merch route.

**Kimi:** structure is the strongest; mechanics endorsement for the curtain call where **nothing is required** — the queens give tips unpurchased and the fees stay player-initiated. That's the brief §4 fix the whole room should converge on.

## 3. TROUSER SNAKE — production mapping (proposal, consistent across auditions)
- Code check: party members have no confidence/concentration keys; `bravado_state()` is percent-band-based. **Do not bolt the status onto Bravado.**
- Implement as a quest-scoped status struct: `CHA_MOD +10`, `FOCUS_MOD −25`, `DIALOGUE_COMPROMISED true`, `persists_until` end-of-evening; alcohol sets stage `TS_SUPPRESSED` (penalty swaps to a judgment penalty; it is a stage of the same status, not a new buff). Engine extension = PROPOSED; scene-level effect (dialogue option swaps) shippable now.

## 4. Carry-forward for round 2 (my lane)
1. Finalize the five enemies in the exact shipped schema + consumables.json drop entries; assign each a combat role, a counterplay, and an Opera District encounter slot; every stat marked PROPOSED.
2. Battle text pass: intro lines must be EarthBound-cruel and venue-specific; enemies are theater people, so the intros do the insult work the engine can't yet.
3. Rebuild the quest's cost architecture to brief §4/§5: ≥3 genuine decision points, ≥2 with game-state consequences, ≥1 free path, ≥1 non-spending escalation; no mandatory bill.
4. Resolve the device question (Kimi's q1) before drafting any Chadwick filming beat; one-phone canon says no N-Gage livestream.
