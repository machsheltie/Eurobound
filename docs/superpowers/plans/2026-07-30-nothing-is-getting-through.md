# "Nothing Is Getting Through" Implementation Plan (Agent-Team Edition)

> **For agentic workers:** This plan is executed by an **agent team** (agent-teams plugin): one orchestrator (session lead), five implementer lanes with strict file ownership, and one canon/tone reviewer. Each implementer receives ONLY its own lane section plus the Global Constraints. Source of truth for design intent: `docs/superpowers/specs/2026-07-30-nothing-is-getting-through-design.md` (~200 lines — implementers should read it in full).

**Goal:** Ship the "Nothing Is Getting Through" questline (The Herp / Gold Circle Coin), six full lady-NPC profiles, item/status/location wiring, and the Beatdown deferral batch — ~10 new files, ~10 surgical edits.

**Architecture:** Five parallel lanes with disjoint file ownership. Lane B1 (Renata) completes before Lane A starts (Lane A quotes her). Lanes B2, C, D run fully parallel. Reviewer sweeps the whole batch at the end; one fix wave; re-review.

**Tech Stack:** Markdown design docs against repo templates; JSON data files validated with PowerShell `ConvertFrom-Json`.

## Global Constraints

- **Templates are mandatory and complete:** sidequests use every section of `Templates/sidequest_template.md`; NPC profiles use all 16 H2 sections of `Templates/NPC_Profile_Template.md`; permanent items use all 12 H2 sections of `Templates/permanent_item_template.md`. No section skipped, no "N/A" without a one-line justification.
- **Tone (binding):** Bros are NEVER self-aware; players laugh AT them; they are delusional pushing-40 dad-bods, not studs — every "conquest" is a misread. Satire targets frat-bro/tourist psychology, reality TV, and luxury-retail gatekeeping — never Czech/Austrian people, never women's bodies. Renata, Věra, Aiguille, and all six ladies keep their dignity: winners, operators, or unbothered.
- **Renata is not the joke.** The comedy lands 100% on the bros' beer goggles and morning horror.
- **Miss Morphine's is-she-real ambiguity is NEVER resolved.** Not in her profile, not in the quest, not in a footnote.
- **No new crypto content** (CryptoBro69's existing gags may be referenced; add nothing new). No Aaron / "She Thinks My Tractor's Sexy" NFT content anywhere (parked for a future round).
- **Never "spring break"** — it is a summer vacation trip. World names only: Debaucheryville, Sinfonia, Publandia, The Bacchanus — never Prague/Vienna/Dublin/Vltava. Y2K-era cringe (ICQ, VHS, 1990 latex).
- **No graphic sexual content** — implication, cutaway, and morning-after wreckage only.
- **Canonical IDs (use verbatim, everywhere):**
  - Quest: `debaucheryville_sidequest_nothing_is_getting_through_01`
  - Status effect: `the_herp`
  - Item: `item_gold_circle_coin`
  - NPCs: `debaucheryville_npc_queen_riviera_renata_01`, `debaucheryville_npc_vape_witch_vanessa_01`, `debaucheryville_npc_backpack_girl_01`, `debaucheryville_npc_cryptobro69s_ex_01`, `debaucheryville_npc_polina_01`, `debaucheryville_npc_paulina_01`, `debaucheryville_npc_miss_morphine_01`
- **Canonical verbatim quotes (copy exactly):**
  - Renata: **"That's QUEEN Riviéra Renata to you!"** and **"You're such nice boys!"**
  - Locals at the party: "Renata's here somewhere tonight—"
  - Thong discovery: "Bro. Whose is this." / "...Mine now?"
  - Bradley: **"Bro it itches so bad it looks like we got CRABS."**
  - Věra: **"European strains require cinematic-grade containment."**
  - Hamstradamus prophecy: **"ONLY THE GOLD CIRCLE SHALL STAY THE BURNING. SEEK THE HOUSE OF NEEDLES. REPENT."**
  - Vitrine placard: "Molded 1990. A piece of cinema history. **It is not for sale. It is for aspiration.**"
  - Pretty Woman canon: "the condom of champions, the one and only… nothin' is gettin' through this sucker."
  - Narrator, post-exit: "Nobody said it out loud."
- **Git discipline (concurrent-session hazard):** a second Claude session shares this checkout committing Godot engine work. Implementers do **NOT** run any git commands. The orchestrator commits each lane on completion using explicit file paths only (never `git add -A`/`-u`), with the session's required commit trailers.
- **Surgical edits only** on existing files: add the specified content where it belongs; never rewrite, reformat, or "improve" untouched sections.

## File Ownership Map

| Lane | Owns (create) | Owns (edit) |
|---|---|---|
| B1 | `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md` | — |
| B2 | 5 lady profiles (paths in Lane B2) | — |
| A | `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md` | `Design/Quests/couchsurfingchronicles.md`, `Design/Quests/Location Specific/Debaucheryville/couchsurfingchroniclesdebaucheryville.md` |
| C | `Design/Inventory/items/gold_circle_coin_item.md` | `Design/Mechanics/Battle/status_effects.md`, `Design/World Design/Sinfonia/haute_couture_haberdashery.md`, `Design/World Design/Debaucheryville/bohemian_riviera.md`, Riviera JSONs (`core/`, `environment/`, `interactions/`, `npcs/Bohemian_Riviera/` × `bohemian_riviera_*.json`) |
| D | — | `Design/World Design/Debaucheryville/the_participation_trophy.md`, `Design/World Design/Debaucheryville/mysterymeatcart.md`, `Design/World Design/Debaucheryville/items/bohemian_riviera_items.json`, `Design/Inventory/items/summer_vacay_stein_item.md`, `Design/Inventory/items/trivia_champ_badge_item.md`, `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md` |

No lane touches another lane's files, ever. Cross-lane needs are satisfied by the Canonical IDs/Quotes above.

---

### Lane B1: Queen Riviéra Renata (FIRST — blocks Lane A)

**Files:**
- Create: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md`
- Read first: `Templates/NPC_Profile_Template.md`, spec §2–§3, `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/janek_sykora.md` (house style + the "dignity intact" treatment to emulate)

**Interfaces — Produces:** her NPC ID, her two verbatim lines, and the outbreak-scene beats Lane A will stage.

- [ ] **Step 1: Write the profile** — all 16 template sections. Required content:
  - Mid-50s Bohemian Riviera institution; decades of devoted sun worship (sun-worn, and completely at peace with it); ridiculously high libido; loves a good party; "spreads the love amongst all beachgoers equally — it's only fair." Locals speak of her with genuine respect and mild awe.
  - The beer-goggles mechanic: through the bros' goggles her sprite renders as a 22-year-old knockout; sprite sheet table must list BOTH sprites (true self + goggles-render) with the goggles version marked as a bros-POV-only filter, not her actual appearance.
  - Outbreak-scene beats from her side: gets exactly what she came for, has the sense to redress fully and sensibly, sunglasses on; maternal cheek-pats for the two standing bros; arms around thong-bro's neck, big kiss on the mouth; jogs off calling "You're such nice boys!"; the mid-exit "That's QUEEN Riviéra Renata to you!" beat (wink, pride, serious swagger) when the bros finally connect the name.
  - Her "rejection scene" for the quest's rejection system: cheerful unavailability — she has already moved on to the next party; nothing cruel, she simply has better things to do. Post-cure callback line included.
  - Dialogue section must carry all her verbatim canon lines from Global Constraints.
- [ ] **Step 2: Validate** — `(Get-Content <file> | Select-String '^## ').Count` equals the template's H2 count (16). Fix if not.
- [ ] **Step 3: Report DONE** to the orchestrator (who commits).

### Lane B2: The Five Harvested Ladies

**Files (create all 5):**
- `Design/Character Profiles/DebaucheryvilleNPCs/Velvet Curtain Club/vape_witch_vanessa.md`
- `Design/Character Profiles/DebaucheryvilleNPCs/Absinthe Arcade/backpack_girl_who_never_left.md` (new folder)
- `Design/Character Profiles/DebaucheryvilleNPCs/Shadow Exchange/cryptobro69s_ex.md` (new folder)
- `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/suspicious_twins_polina_paulina.md` (one file, two NPC IDs)
- `Design/Character Profiles/DebaucheryvilleNPCs/miss_morphine.md`
- Read first: `Templates/NPC_Profile_Template.md`, spec §6, `Design/Quests/Location Specific/Debaucheryville/couchsurfingchroniclesdebaucheryville.md` (their established canon — morning scenes, results, satire angles are BINDING; harvest, don't reinvent), one existing profile for house style.

**Interfaces — Consumes:** status id `the_herp`; NPC IDs from Global Constraints. **Produces:** each lady's Herp-rejection scene + post-cure callback line (self-contained; Lane A references them by pointer, not by quote).

- [ ] **Step 1: Write the five profiles** — all 16 sections each. Every established fact from the Chronicles file carries over (meet locations, morning scenes, result payloads, ICQ integrations, satire angles). Each profile adds two NEW quest hooks:
  - **Herp-rejection scene** (triggered when an infected bro attempts a couchsurf/romance): Vanessa consults her crystals and recoils — "your aura is... contagious"; Backpack Girl writes and performs a hostel ballad about it on the spot; the Ex laughs, screenshots, sends it to CryptoBro69 (his ICQ gloating follows — reuse his voice, add no new crypto schemes); the Twins update the American Tourist Bingo card ("herpes" was already a square); Miss Morphine's rejection is only an ICQ auto-reply.
  - **Post-cure callback line** for the re-attempt once the Coin is equipped — each in her own voice, never letting the bros off the hook.
  - Ladies stay put: Twins at the Cirque, Ex at the Shadow Exchange. Nobody relocates.
- [ ] **Step 2: Validate** — H2 section count = 16 for each of the five files.
- [ ] **Step 3: Report DONE.**

### Lane A: Quest File + Chronicles Updates (starts after B1)

**Files:**
- Create: `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`
- Edit: `Design/Quests/couchsurfingchronicles.md`, `Design/Quests/Location Specific/Debaucheryville/couchsurfingchroniclesdebaucheryville.md`
- Read first: `Templates/sidequest_template.md`, spec §1–§7, `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md` (B1's output — quote her exactly), `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md` (house style for a flagship quest), `Design/World Design/Sinfonia/haute_couture_haberdashery.md` (the shop's Assessment Protocol and Valued Client tier you'll build the two paths on — reference, do not edit).

**Interfaces — Consumes:** Renata's profile (B1); IDs/quotes from Global Constraints. **Produces:** the quest structure Lane C's location wiring points at (quest ID + scene event names below).

- [ ] **Step 1: Write the quest file** — full sidequest template. Required beats, in order (spec §3–§4):
  1. **Outbreak scene** (event id `night_event_outbreak_01`, staged at the Bohemian Riviera `night_party_zone`): party montage with literal beer-goggles rendering (three separate through-the-goggles moments, three oblivious bros, each unaware of the others); locals' background name-drops; morning seagulls; the thong discovery exchange; Renata's exit exactly per her profile (maternal cheek-pats, kiss, "You're such nice boys!", the QUEEN correction mid-exit); narrator: "Nobody said it out loud."; all three bros itching in unison; poison-ivy self-diagnosis ("there was DEFINITELY foliage at that beach party") and Bradley's CRABS line. All three infected — scripted, guaranteed.
  2. **Věra refusal** at Midnight Munchies General Store — judgment-free single glance; no poison ivy, no plants, no real sand at that beach; her verbatim containment line; `the_herp` locks in.
  3. **Prophecy** at Hamstradamus's tent — verbatim prophecy; the House of Needles = Haute Couture Haberdashery (Aiguille = French for "needle" — state the pun in the design notes).
  4. **The Limp to Sinfonia** — Herp active throughout; NO temporary suppressant exists anywhere; rejection scenes trigger per lady (pointer list to the six profiles — do not duplicate their scene text).
  5. **The Haberdashery**: vitrine discovery (verbatim placard), then **PATH A — "Become Someone Who Belongs Here"** (Valued Client at 500 Sovs via the shop's existing tier + an absurd errand for Monsieur Aiguille, who opens the vitrine with genuine ceremony) and **PATH B — "Big. Huge. Mistake."** (after-hours infiltration in formal wear bought from the same shop; mannequin poses in opera capes while the night porter passes).
  6. **Prize:** `item_gold_circle_coin` — party-wide suppression while ANY bro has it equipped.
  7. **The Return:** revisitable cities, per-lady re-attempts with post-cure callbacks; Chronicles completion stays fully achievable.
  8. **Post-credits:** months later — the Coin framed on a wall like a championship belt; one bro still absentmindedly scratching.
- [ ] **Step 2: Edit the two Chronicles files** — add (a) Renata as a scripted/mandatory Chronicles entry (the outbreak IS a Chronicles event; full completion now REQUIRES catching The Herp — "Slept Around, Found Out" becomes literal), (b) a note that infected couchsurf attempts route to each lady's Herp-rejection scene, (c) pointers to the six official profiles. Surgical additions only.
- [ ] **Step 3: Validate** — every H2 of `Templates/sidequest_template.md` present in the quest file, in order.
- [ ] **Step 4: Report DONE.**

### Lane C: Items & Systems Wiring

**Files:**
- Create: `Design/Inventory/items/gold_circle_coin_item.md`
- Edit: `Design/Mechanics/Battle/status_effects.md`, `Design/World Design/Sinfonia/haute_couture_haberdashery.md`, `Design/World Design/Debaucheryville/bohemian_riviera.md`, `Design/World Design/Debaucheryville/core/bohemian_riviera_core.json`, `Design/World Design/Debaucheryville/environment/bohemian_riviera_environment.json`, `Design/World Design/Debaucheryville/interactions/bohemian_riviera_interactions.json`, `Design/World Design/Debaucheryville/npcs/Bohemian_Riviera/bohemian_riviera_npcs.json`
- Read first: `Templates/permanent_item_template.md`, spec §5, §7, and the §4/§3 scene summary; `Design/Inventory/items/vip_wristband_item.md` or the Beatdown items for house style; the Port-O-Cologne entry in `status_effects.md` (format to match).

**Interfaces — Consumes:** quest ID + outbreak event id `night_event_outbreak_01` (Lane A; fixed here so C never waits on A). **Produces:** `item_gold_circle_coin`, `the_herp`.

- [ ] **Step 1: Gold Circle Coin item file** — all 12 template sections. Key item / equippable accessory; The Deception inverted — for once the item actually IS what the legend claims, the one item in the game that fully delivers; party-wide Herp suppression ("aura of champions") while equipped by any bro; unequip → the shimmer returns; one and only — cannot be sold, dropped, or traded ("It is not for sale. It is for aspiration." — the bros finally agree with Aiguille on something); Pretty Woman quote verbatim; Molded 1990.
- [ ] **Step 2: `the_herp` status entry** in `status_effects.md`, beside Port-O-Cologne, matching its format exactly: permanent, never cured, suppressed only while `item_gold_circle_coin` equipped (any bro → whole party); −2 Charm (all NPCs); romance/couchsurf attempts auto-trigger rejection scenes; **Groin Blurts** rare involuntary interruptions ("DOES ANYONE HAVE A BAG OF FROZEN PEAS?!", "IT'S JUST A RASH, I SWEAR!"); subtle waist-level heat-shimmer particle REUSING the Riviera PNG doc's existing `heat_shimmer` asset; NPCs visibly step back. All three bros carry it simultaneously.
- [ ] **Step 3: Haberdashery surgical edit** — add to the Accessories Alcove: the locked vitrine under *Objets d'Héritage* with the verbatim placard; quest-integration note (first-visit Assessment Protocol snub = the Pretty Woman snub; PATH A rides the existing 500-Sov Valued Client tier; PATH B after-hours beats staged here); Aiguille's ceremony beat (he respects the Coin more than they do). Do NOT rewrite any existing section.
- [ ] **Step 4: Riviera outbreak wiring** — `bohemian_riviera.md`: add the outbreak event to the location's events/quest-hooks section (event id `night_event_outbreak_01`, quest `debaucheryville_sidequest_nothing_is_getting_through_01`, staged at `night_party_zone`, one line on Renata's presence with pointer to her profile). Mirror minimally in the three JSONs: `core` (quest hook registration), `environment` (night-party state note if the file's schema has one), `interactions` (the scripted outbreak trigger), `npcs` (register Renata: id `debaucheryville_npc_queen_riviera_renata_01`, name, night_party_zone presence, pointer to her profile file — nothing more; her design lives in B1's profile). Follow each JSON's existing schema — add entries in the same shape as neighbors, invent no new top-level keys.
- [ ] **Step 5: Validate** — 12 H2s in the item file; every edited JSON passes `Get-Content <file> -Raw | ConvertFrom-Json`.
- [ ] **Step 6: Report DONE.**

### Lane D: Deferral Cleanup Batch

**Files (edit only):** `the_participation_trophy.md`, `mysterymeatcart.md`, `items/bohemian_riviera_items.json`, `summer_vacay_stein_item.md`, `trivia_champ_badge_item.md`, `bacchanusbeachbeatdown.md` (paths in File Ownership Map)
- Read first: spec §9; `Design/World Design/Debaucheryville/items/cirque_du_shady_items.json` (the existing-sheet pointer style to copy).

- [ ] **Step 1: NPC ID backfill** — formal NPC ID blocks: Yolanda → `debaucheryville_npc_yolanda_kovarik_01` in `the_participation_trophy.md`; Chef Chuckles → `debaucheryville_npc_chef_chuckles_01` in `mysterymeatcart.md`. Match the ID-block format used by the Beatdown NPC profiles.
- [ ] **Step 2: Icon fixes** — in `bohemian_riviera_items.json`, convert the 5 icon refs pointing at unspecced PNGs to the existing-sheet pointer style used by `cirque_du_shady_items.json`; unify the currency field wording with that file. JSON must still parse.
- [ ] **Step 3: Polish edits** — (a) stein rarity-line reworded to stop duplicating the badge's; (b) replace the flat "random tourist kid" NPC reaction row in `trivia_champ_badge_item.md` with a characterized one; (c) add one line to the Beatdown quest's minigame turn-structure row stating launched bros leave the round-robin; (d) add a one-line spec note in the stein file acknowledging Glitter Gullet as a deliberate deviation from the spec's "brief Nausea."
- [ ] **Step 4: Skip** the optional Rosťa/Standa/Zdenka compact profiles (deferred again — out of capacity by default; orchestrator may re-add).
- [ ] **Step 5: Validate** — `bohemian_riviera_items.json` parses; report DONE.

---

## Review & Landing (orchestrator)

- [ ] Commit each lane on its DONE report (explicit paths only, required trailers).
- [ ] Dispatch the canon/tone reviewer over the whole batch diff with the reviewer dimensions from spec §10: canon fidelity (verbatim quotes), tone (satire targets the bros; the ladies keep their dignity), template compliance (16/12/full-sidequest section counts), no lane-crossing edits, no parked-Aaron content, no "spring break," no real-world city names.
- [ ] One fix wave (resume the owning lane's implementer per finding), scoped re-review, then land: merge/push main per the finishing-a-development-branch skill (fetch origin first; concurrent-session commits excluded from review scope).
