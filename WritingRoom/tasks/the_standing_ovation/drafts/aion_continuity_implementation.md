# Aion — Continuity Register & Implementation Dependencies

**ROUND 6 REVISION — full synchronization to the moderator's CURRENT DECISION REGISTER and Editor Ruling #4 (`aion_continuity_implementation`, `remaining_continuity_errors`).** The register now carries ONE current value per live item and treats every author answer as settled. Retired alternatives live in the decision history, not here.

**Reviewer: GLM.**

---

## 1. FACT-CHECK LEDGER (updated rows; carried canon unchanged unless noted)

| Claim | Source checked | Status |
|---|---|---|
| Producer's Circle **36 SOVS** (24 pours + 12 acknowledgment, table 0) | Editor `economy_circle`; GLM mechanics §1 | **WORKING VALUE**, not permanent canon, not "proven affordable." Ceiling 48 / floor 24 recorded. Menu grayed at <36, never hidden; D1B loses zero show content. Receipt + Bradley's arithmetic recompute together if the price moves. |
| Encore: 10 SOVS, +30 HP, staff standing ovation | Venue menu table | **CANON.** D3B routes three Encores as a **scripted gold deduction (−30), no item grants, no `use_item`** (GLM §3 — the +90 HP exploit stays closed). |
| Encore **buff** (+5 Bravado, Bravo Challenge) vs. the Encore drink | Venue docs; GLM §3 | **UNCOUPLED — binding.** No wiring, ever, between the drink and the buff. |
| Three Encores = suppression? | Author q9: B | **RESOLVED.** Alcohol DULLS TROUSER SNAKE (status text stands); the Encores are coping that fixes nothing. The two full defeat routes: Flintstone Xanax and the performer encounter. |
| The Understudy comp (D2A) | Editor `economy_understudy` | **STRUCK.** Replaced by Jenna's no-effect `relic_claim_ticket` ("ONE (1) RELIC — CLAIM BY 2004"). |
| Drop resolution | Shipped `battle_manager.gd` `_win()` | **CANON:** the engine ROLLS `drop_chance`; `grant_rewards()` skips `""`. Drops must exist in `consumables.json` or names print as raw IDs (GLM §0b). |
| Tony420 | Project planning docs + live `.claude` domain notes | **PRE-EXISTING PROJECT CHARACTER** with a completed working profile at `drafts/kimi_tony420_profile.md` (editor-approved as a consolidation; expanded details are ordinary canon proposals). ICQ purchases are **crypto-only**; older dollar/SOVS ad copy is historical pitch. |
| Real public figures in political parody | AUTHOR NOTE 2026-11-09 | **BINDING:** Chelsea Clinton, the Bush twins, Bush, Gore, Katherine Harris et al. stay in player-facing dialogue. Real PLACE names remain banned. "Florida's still counting" stays (locked historical reference). |
| Event 10 speaker order; fixed events 3–11; verbatim record | Dossier + `max_vex.md` + GLM §11 | **BINDING.** Max asks; Chadwick answers. Zero player menus on the runway. |
| Camcorder with chain | `chadwicksweapons.md` | **CANON.** Seven-character title-generator limit: PROPOSED device detail. |
| `sinfonia_enemies.json` empty; eleven-field schema | `game/assets/data/enemies/` | **CANON.** All five names unique; GLM's consolidated sheets are the review candidate. |
| MoonCum696969 spendability | Author q10: A | **RESOLVED.** Spendable with Tony420 only; **added to the coin pool** (my proposed pool-format entry in `canon_proposals.md`; the moderator applies the `design/economy/` edits only with the author's OK). The price is **50 MoonCum696969**. |
| Overnight chronology | Author + Editor `overnight_story_break`/`overnight_timing` | **BINDING:** catcalling escalates DURING Act II → fixed Max encounter → D3 coping/optional ICQ → D4 at the threshold → Jenna's stage-door invitation → **D5 before departure** → Green Room → afterparty at the unnamed apartment (`sinfonia_firstdaughters_apartment_01`, provisional) → cut to black → morning reveal. Venue closes 01:00. |

---

## 2. PROPOSED CONTENT AND MECHANICS REGISTER (f2 — one current definition per item)

### Prices
- Producer's Circle: **36 SOVS** (working; D1A only). D3B: **30 SOVS** (scene only, scripted deduction). Tony420 ICQ purchase: **50 MoonCum696969** (author-ruled; crypto, never SOVS). Every other beat in the quest: **0 SOVS.**

### Items (all PROPOSED unless marked CANON)
| ID | Class | Readers |
|---|---|---|
| `press_napkin` | key item, no effect | 5A envelope beat ("Credentials stay with the journalist."); Keeper of the Rope nonviolent resolution |
| `chadwick_tape` | key item | D4 menu condition; chain-yank; D3 payload table |
| `receipt_producers_circle` | consumables, `usable:false` souvenir | Max approach variant; receipt joke; D1 branch state |
| `relic_claim_ticket` | consumables, `usable:false` souvenir | none — flavor prop; cut if the author dislikes clutter (`economy_understudy`) |
| `condescending_review` | consumables, `usable:false` | Critic fixed drop |
| `crumpled_headshot` | consumables, `usable:false` | Supernumerary fixed drop |
| `spare_reed` | consumables, `usable:false` (Embarrassed-cure effect PROPOSED, ships inert if status system isn't ready) | Bassoonist + Oboist drop |
| `decorative_brass_stanchion_clip` | consumables, `usable:false` | Keeper fixed drop |
| `dramatisch_dunkel` | consumables, **usable**, heal 40 | Keg-Acolyte fixed drop (first-clear gated; `palate_respected` now also fires on burst KO per GLM §13.4) |
| `flintstone_vitamins` | **consumable, `usable:true`, zero-heal; consumption IS the trigger** for `flintstone_xanax_active` (GLM findings S4). Display name **Flintstone Xanax**; price **50 MoonCum696969** from Tony420 via ICQ. **Effect (author-ruled):** ends TROUSER SNAKE and prevents recurrence AND Bradley's sexual performance until the next in-game morning — reliable, no roll, save/load-safe, cleared only by the next-morning transition. | D6 variant staging; morning Bradley staging; TROUSER SNAKE suppression. **Flintstone Fentanyl is a SEPARATE product with no assigned effect — do not merge.** |
| `campaign_button_chelsea_morning` / `_jenna_talia` / `_barbara_bushed` | permanent equippable cosmetic accessories, zero stats, **never consumable**; fallback class: permanent key items | Found together on the bathroom counter at V5; first-award gated by reaching the morning continuation (`afterparty_completed` + `campaign_buttons_awarded`) |

- All five enemy drops land in the **shared cross-world** `items/consumables.json` — implementation-time author sign-off (Dependency 9). `usable: false` requires the one-line `use_item` guard (Dependency 8). The three campaign buttons are equipment/key items, NOT consumables — a separate registration row from the drop items.

### Quest flags (persistent)
**Four pre-overnight + five overnight = nine total**, each with a named reader:

| Flag | Set on | Reader |
|---|---|---|
| `sinfonia.ovation.footage_release_planned` | D4 RELEASE | Axed Critic's Eager state (district-wide); next-day metrics narration (predictions only). Rumor, never publication (q8). |
| `sinfonia.ovation.footage_vaulted` | D4 VAULT | Mutual exclusion with release; blocks later "you promised us the tape" continuity errors. No other reader — by design. |
| `sinfonia.ovation.rope_resolved` | any first Keeper resolution | Foyer trigger; Keeper becomes one-line NPC. First-clear gate. |
| `sinfonia.ovation.palate_respected` | first Acolyte lecture/weathering OR burst KO (GLM §13.4) | Alley trigger; no repeat drop. First-clear gate. |
| `sinfonia.ovation.flintstone_xanax_active` | Pill consumed | D6 variant; morning Bradley staging; TS recurrence/performance suppression. Survives save/load and scene changes; clears only on next in-game morning. |
| `sinfonia.ovation.afterparty_completed` | V3 cut to black | Morning scene availability; decline exclusion; next-day callbacks |
| `sinfonia.ovation.campaign_buttons_awarded` | V5 grant | Mirror interaction; prevents duplicate awards |
| `sinfonia.ovation.inauguration_held` | Catastrophe override | Fridge decree and pillowcase sash at V4/V5; retained until the morning scene has read it |
| *(evening tier + D5/D6 selections)* | Quest beats | Serialize with the evening chain on mid-chain save; no scene-end reset; clears at the next-morning transition |

- **`footage_posted`: NOT SET by this quest** (q8). Reserved for a future, properly established resolution interaction.
- **Scene-local (no flags):** `reset_method` enum (press/wallsit/wedge, consumed at selection); D1 branch via receipt presence; D2 branch via `chadwick_tape` presence; D3B suppression staging. Stale-state proof is structural: no branch state persists.

### Statuses
- **TROUSER SNAKE** — canon text/numbers (+10 Confidence / −25 Concentration / compromised dialogue / rest of evening). **Defeat routes (author-ruled, q9: B):** (1) `flintstone_vitamins` — full defeat plus until-morning recurrence/performance block; (2) sleeping with one of the revue's performers — offscreen, never shown, no new relationship canon. **Alcohol DULLS it** (banner dims, compromise lines lose volume; presentation only) and never defeats it. No character explains why the vitamins work (§17 / author logic note).
- **Intoxication tiers — CANON names (Buzzed → Beer Goggles → Shitfaced → Catastrophe), no numeric thresholds.** Quest implementation per GLM's ten-point spec (`drafts/glm_intoxication_spec.md`): authored-beat escalation during Act II; one bounded Catastrophe substitution at the afterparty ("PILSNER IS MAKING AN EXECUTIVE DECISION." → "Assume the presidency."); D5 and D6 never overridden; all mechanics PROPOSED engineering.
- **Stage Fright** (Supernumerary): 35% freeze on next 2 attacks, ordinary attack against the COMPLETED pose only. PROPOSED.
- **Sharp** (Bassoonist self-debuff): offense −2, 3 turns. PROPOSED.
- **Corpsing** ×2: damage multiplier on prep-interrupt, not a status. PROPOSED.
- **NO `presidential_soreness` status** (editor `presidential_soreness`): morning soreness plays as animation, posture, props, and dialogue only.

### New NPC information
- **Tony420** — pre-existing character; working profile `drafts/kimi_tony420_profile.md` (editor-approved consolidation; expanded details are canon proposals). All-lowercase, no punctuation, chronically online, crypto-only for actual ICQ purchases. `shared_npc_tony420_01` remains a proposed ID pending registry check; the documented hostel-lobby hotspot is the valid fallback to the proposed venue-door hotspot.
- **Performers** — Chelsea Morning, Jenna Talia, Barbara Bushed: profiles in `drafts/gemini_npc_profiles.md`; quest ID standardized to `sinfonia_sidequest_standing_ovation_01`. Post-overnight appearances (apartment, morning) still need adding to those profiles per the editor's note.
- Supernumerary, Bassoonist, Tympanist, Oboist: combat enemies, no profile templates; names registered unique.

---

## 3. CONTINUITY NOTES FOR KIMI'S INTEGRATION

1. **Fixed events 3–11:** zero menus, speaker-by-speaker fidelity. The D2B chain-yank is stage business over verbatim lines only.
2. **5C is a two-option player choice** (Reenactment vs. the Official Version) — the spine's §11 marker should read "**AION 5C — the two records**," not "REENACTMENT as the full no-tape exit."
3. **The two TROUSER SNAKE defeat routes now have player-facing entry points:** the ICQ window is reachable after ANY D3 outcome (GLM mechanics §2.3), never auto-closes the evening, and D5 waits for the player; the performer route runs through D6. The pill is an optional route, never a progression gate.
4. **Do not "correct" the reenactment's misordered exchange** — "That's not the order." / "Director's cut." is the joke (ruling `kimi_five_fixes` NOTE).
5. **The anointing exchange in 5C-2 is cut** (Editor Ruling #4): Pilsner's "Nobody fact-checks a legend, Chadwick." runs straight into Chadwick's silent backward performance.
6. **VAULT = "the footage is never publicly distributed"** (Editor Ruling #4) — the Act III camera-review beat shows the player some of the recording; the vault claim is about distribution, not player blindness.
7. **D4 plays at the marquee/threshold, before departure; D5 follows immediately at the stage door.** The old street ending plays only on the decline path. Do not splice a completed street walk between D4 and Jenna's invitation.
8. **Chronology:** pre-overnight content sits inside 16:00–01:00; the afterparty and morning are offsite at the provisional apartment ID.

---

## 4. ENGINE DEPENDENCIES

Carried unchanged from GLM's consolidated list (#1–#10, mechanics file §8 / enemies file §12), plus the overnight's proposed dependencies (GLM spec §9, #11–#16). Nothing new from my lane this round.

---

## 5. OPEN AUTHOR DECISIONS (none blocking drafting)

1. Performer-route eligibility: whether "one of the drag show 'ladies'" includes Max Vex or only the First Daughters cast — flagged in `canon_proposals.md`, not invented. The break's D6 staging (Barbara default, Jenna alternate) slots in under either answer.
2. Producer's Circle final price (economy balancing pass).
3. Title-generator seven-character limit as device canon (proposed detail).
4. Xanax availability dependency: implementation must confirm a deterministic existing MoonCum acquisition route reachable before D5 (Kimi canon_proposals §4); the room does not invent one.
