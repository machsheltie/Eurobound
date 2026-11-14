# Eurobound — Next-Work Handoff (paused 2026-07-31 for folder reorganization)

## Current state (updated 2026-11-11, Eurobound-j50)

- The folder restructure is merged: `chore/folder-restructure` landed on main in 2003ee3
  (2026-08-04) and `_sorting/` no longer exists. The legacy-named trees (`design/World Design/`,
  `design/Character Profiles/` and others) still sit beside the snake_case ones (beads
  Eurobound-58a, Eurobound-bzi).
- All work happens on `main`. The Godot project lives in `game/` (Godot 4.7, `game/project.godot`).
- Round 5 (economy, wallet, crypto) was executed: Lanes E/C/V in 9952f7e, Lane R in 49f8345,
  Lane B in 45db6fb. `docs/superpowers/plans/2026-08-01-economy-round5.md` still shows 0 of 21
  boxes checked although `design/economy/{economy_system,wallet_ui,icq_airdrops,
  shitcoin_master_pool,legacy_vault_cards}.md` exist. Whether the spec's formal review ever
  happened is a question for the author.
- Open work is tracked in beads (`bd list`). Resolved work items from the sections below were
  moved verbatim to the end of this file.

## Standing rulings 2026-08-03 (CLAUDE.md / PRD-reclamation round — binding, do not relitigate)

- **The story belongs to the author alone.** The PRD branch's invented plot ("The Last Hurrah") is struck in full; the author-dictated story core is in EUROBOUND_PRD.md §4.2. No agent writes story without the author.
- **MA canon restated at full strength:** the ONLY content ceiling is no nudity — beyond that, anything goes. The seedy underbelly is shown, glorified, and ridiculed. No safe-build mechanism (`SATIRE_MODE`, `line_safe`, string swaps) may ever be created. Satire targets everything; there is no narrator; "never targets locals" is struck.
- **All tracked NPCs and locations as of 2026-08-03 are author-approved canon** — written by or with the author. This includes the full audit list (Cyberspace Kavarna, Internet History Museum, Mystery Meat Cart, The Participation Trophy, the four Debaucheryville breweries, Haute Couture Haberdashery, Bassline Opera House, Mozart's Last Rave, Café Existenz, Vape Witch Vanessa, Vlad the Validator, Suspicious Twins, Backpack Girl, CryptoBro69's Ex, Bartender Matrix, Slick Greg, the Black-Tie Backroom cast, Bohemian Riviera cast, and all Publandia/Sinfonia venues). None are agent-orphans; none get struck.
- **Killed by author ruling:** Mirror Chad; Fistø's alternate ending and any sincerity arc (Fistø survives ONLY as the graffiti-quest philosopher-janitor); Reality Check enemies/ending; the Perspective status; "The Legend" finale boss; all PRD act beats; the Holy Keg as MacGuffin (demoted back to Lord Pilsner's personal sidequest); per-city Rival Trio showdowns (Rival Trio appears ONCE, in the NFT sidequest).
- **Currency:** SOVS only — never euros, never the € display glyph, never koruna (supersedes the R5 spec §1.2 glyph rule; € price sweep COMPLETED 2026-08-04).
- **Platform:** Steam/desktop. The Apple-guidelines rationale for any content decision is void.
- **NFTs:** 16 total, 4 per city (Shamsterdam's #4 is Dennis's NFT), milestones 4/8/12/16; the 16/16 epilogue is the author-dictated CryptoBro69 press-conference arrest ("DIAMOND HANDS FOREVER!"); the 12 reward is pending author (author, 2026-11-11).
- **Shamsterdam is canon** — the author's fourth city, and the FINAL city of the trip (author ruling 2026-08-03): the crescendo before the airport; the finale happens there. **City order: Publandia → Debaucheryville → Sinfonia → Shamsterdam; visited cities stay open for backtracking.**
- **New author-dictated content:** Mom-call rework (Lord Pilsner secretly lives with his mom post-divorce); Bradley's wedding-ring extortion quest (player choice; DeLorean payoff); **The Weed Wraith** = minor villain in Shamsterdam; **The Schnitzel King** = minor boss of **The Golden Cutlet**, a Sinfonia dungeon (author-dictated: multi-level "authenticity" tourist-trap tavern, group-purchased VIP Cultural Heritage Pass — Chadwick's idea, basement Heritage Trial, trap doors, real combat per vault, hosts a Sinfonia NFT acquisition point; roster/boss details in development); Hot Kroger Guy stays, plus his scripted girlfriend's-phone call to Pilsner — see EUROBOUND_PRD.md §4.2–§4.4.
- **Villain template mandate:** every villain (minor villain, miniboss, city boss, finale) gets a completed `Templates/villain_template.md` profile AT CREATION — no exceptions.
- **Black-Tie Backroom Easter egg (author-dictated):** ambient entrance scene — a pretty brunette in a little black dress being chatted up by the security guards ("no way you're forty-four"); bros never notice, never explained, no name, no roster entry.
- **Risk-mitigation plans are shit-canned repo-wide** (author ruling): no risk registers, no mitigation sections, ever.
- **NO NARRATOR — swept repo-wide 2026-08-04, and no in-world substitute either.** The Aaron spec's "Narrator voice remains canon as dry stage description" carve-out is OVERRULED. Killed: the Narrator-as-Roastmaster design pillar (`party.md`), "Narrator Roast Mode" toggle (`battle_system.md`), sung "Narrator Verses" (`musicalbeats.md`), `narrator_commentary` blocks in the location template and shipped JSONs, `speaker: "narrator"` / `effect: "narrator_line"` data entries, and every `**Narrator:**` label in quest/venue docs. Prose that sat under those labels survives as **stage direction** (what is on screen, spoken by nobody). **Battle-log/UI flavor text is NOT a narrator** and stays — it is where the mechanical comedy lives ("Bradley flexes. Nobody cares. −2 Dignity"); docs that called it "the narrator's descriptions" now call it battle-log flavor text. Do not re-add a commentary section to any template.
- **Platform sweep 2026-08-03:** mobile/iOS/App Store references replaced repo-wide with Steam/desktop; App Store marketing docs banner-marked as stale history.
- The old PRD branch `claude/eurobound-jrpg-prd-uv5iog` is dead and must never be merged or treated as canon. The salvaged, author-corrected PRD lives on `claude/claude-md-game-guidelines-68oyd0`.

## Paused mid-interview 2026-08-04 (author researching — resume from here)

**Finale interview** (author chose "interview me"): Q1 answered — Shamsterdam is the final city. Q2 answered — order Publandia → Debaucheryville → Sinfonia → Shamsterdam, visited cities stay open for backtracking. **Q3 pending: what is the finale beat itself in Shamsterdam** (last blowout / final boss / money-runs-out / author's own shape). Author is thinking it through; do not invent. (bead Eurobound-3mz)

**Other open author decisions:**
- Publandia dungeon: author wants NON-food concept; pitches on the table: The Dead Poets' Lock-In (literary-heritage ghosts, recommended), The Craic Mines, The Eternal Students' Union, The Bookies' Labyrinth. Needs pick + its own boss (villain template mandatory). (bead Eurobound-anc)
- The Golden Cutlet: RULED 2026-11-12. Roster approved (bead page p1y "Approve both as proposed"; desk p1y-q2 "Approve all as drafted"), written into design/worlds/sinfonia/enemies/ and the_schnitzel_king.md. Heritage Pass fine-print QR is Route B to Holographic Charizard (counts once), written into the Charizard item doc, nfthuntsinfonia.md and Legacy Vault Card 5. Still open: QR scan timing (desk 2w7l-q1). (bead Eurobound-p1y)
- Rival Trio reconciliation awaiting confirm: the single game-wide appearance = the Craic Tax showdown awarding Pogs (per the author's FINAL Publandia NFT roster); Debaucheryville/Sinfonia showdowns stay dead. (bead Eurobound-pj5)
- NFT card copy (Tagline/Description/Collector's Thesis) for the seven replacement NFTs: AUTHOR WRITES ONLY, blocks are empty on purpose. (bead Eurobound-dio)
- Shamsterdam city boss + quest skeleton: undefined, author's to dictate. Steam price point: open. Deluxe Roast Pack DLC: open. macOS support: open. Golden Cutlet villain profile and enemy docs: written 2026-11-12 (p1y); venue doc: still to be written. (beads Eurobound-sbn, Eurobound-p22, Eurobound-p1y)

**State at pause:** Rounds 1–4 landed and pushed to `origin/main`. Round 5 (Economy/Wallet/Crypto)
spec is approved-in-substance and committed; its PLAN and EXECUTION have NOT started — paused by
author order pending the folder reorg. Branch: `feature/bacchanus-beach-beatdown` (same as main).
(updated 2026-11-11, Eurobound-j50: Round 5 has since been planned and executed, and all work
now happens on `main`; see Current state above.)

## ⚠️ CRITICAL WARNINGS FOR THE REORG WINDOW

(updated 2026-11-11, Eurobound-j50: the reorg window closed with merge 2003ee3; warning 1 moved to
Resolved, warnings 2-3 kept until verified.)

2. All specs/plans/briefs in `docs/superpowers/` reference current absolute/relative paths.
   After the reorg, the first work session must run a path-refresh pass before executing
   anything from them.
3. `Assets/` and `Scripts/` remain the engine (Godot) session's domain — its uncommitted
   changes were still in the working tree at pause (modified Assets/Data JSONs, deletions
   under Design/World Design/Debaucheryville/sprites/, .import files).
   (updated 2026-11-11, Eurobound-j50: the engine now lives in `game/`; root `Assets/` and `Scripts/`
   still hold 1641 tracked legacy files, see bead Eurobound-qfu.)

## 🔁 RESTRUCTURE RESUME CHECKLIST (added 2026-08-04, author-ordered — do not improvise)

When the folder restructure resumes on `chore/folder-restructure`, execute in this exact order:

3. **Re-run the platform/currency sweeps on moved files:** the SOVS-only retrofit (no euros, no
   koruna — standing ruling below, canon `currency.md` wherever it currently lives, originally
   `_sorting/Design/Economy/currency.md`) and the tracked world-names verification greps (small
   ledger, last bullet). Files have new paths since the sweeps last ran — sweep by content match,
   not by remembered path lists. (bead Eurobound-mb3)
4. **Continue the walkthrough** per `docs/superpowers/plans/2026-07-31-folder-restructure.md`
   (Tasks 4–7: author personally places files; `_sorting/` must reach ZERO files then be deleted;
   then Tasks 8–15 game batches). Session 1 (World Design cities) state: legacy PNG-spec merges
   done with 13 `> ⚠ CONFLICT:` callouts awaiting author rulings — grep `CONFLICT` under the
   Debaucheryville design docs to find them.
   (updated 2026-11-11, Eurobound-j50: `_sorting/` is gone and game batch F landed (466069a, 5ea6f70);
   the only `CONFLICT:` callouts left under `design/` are in
   `design/Quests/debaucheryville/club_flyers.md`, bead Eurobound-01x.)

## Next execution work (in priority order)

1. **Round 5: Economy, Wallet & Crypto Satire System** — spec at
   `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` (author-approved in
   substance; formal review of the transcription still open). Next: writing-plans → agent team
   (proposed lanes E system docs / C coin pool / V vault cards / R retrofit + reviewer).
   Includes the koruna elimination list (§1.3: Zdenka's ladder, badge kid, Riviera JSONs,
   SuperKoruna rename) and Legacy Vault cards for the 12 existing NFTs.
   (updated 2026-11-11, Eurobound-j50: executed. Lanes E/C/V 9952f7e, Lane R 49f8345 (koruna
   eliminated), Lane B 45db6fb. Formal review of the transcription is still an author question.)
2. **Engine coordination (Godot session):** rebuild the brewery-tracker roster from author
   canon — `Assets/Data/saves/brewery_tracker_full.json` + `Scripts/systems/breweries/brewery_tracker.gd`
   currently track AI-invented breweries (`vienna_noir_fermentarium`, `opernhaus_ale_stube`,
   `sachercraft_barrelworks`, `schnitzelbier_innovation_lab`, `liffy_lager_house`, and a
   `"deboucheryville"` key typo) instead of the author's named breweries (Sinfonia: The Standing
   Ovation, Crown & Cask, The Dancing Stein; see city files for all cities). Also carried
   engine notes: per-NPC `chronicles_entry_completed[<npc_id>]` flags (Herp quest dev notes),
   the Aaron encounter's fixed-stake/500-SOVS-collateral + one-time-scene flags (thekingswerehumming
   dev notes), Zdenka's cheapest-cure constraint vs the Port-O-Cologne vendor tax (zdenka.md
   dev notes).
   (updated 2026-11-11, Eurobound-j50: roster rebuilt from author canon in 45db6fb; the file is now
   `game/assets/data/saves/brewery_tracker_full.json` with none of the invented keys, but it
   still lacks Shamsterdam's four (bead Eurobound-akw). The carried engine notes are unverified.)
3. **Draft adoption rounds** (per-file formal review → commit of the ~240 drafts; each adoption
   applies full canon/tone/template review; hippo name + world names already cleaned on disk).

## Open author decisions (queued, with context)

- **Shamsterdam's 4 brewery names** (author to mint; ruled 2026-08-04 that every city has 4
  breweries): ~~rename "Brouwerij de Molen" (REAL Dutch brewery — brand liability, zero joke)~~
  **RESOLVED 2026-11-10: renamed The Wobbly Windmill Brewery; references swept.** Still open:
  rename "Proeflokaal 't Kansen" (generic Dutch, no satire; keep Kees + jenever-distillery
  character, name only), plus invent 2 new establishments. Sweep references after minting.
  (updated 2026-11-11, Eurobound-j50: all names minted in Round v23/v24 (Bottoms Down, The Hoisted Pint,
  The Mad Monarch's Wit-tea Party); item docs 6cb91d1, bead Eurobound-290 closed. "Proeflokaal"
  still appears in 5 design docs, so the reference sweep is unverified.)

## Brewery Tour — RULED 2026-08-04 (canonical spec: design/quests/general_quests/brewerytour.md)

**Decomposition round PHASES 1-5 EXECUTED 2026-08-05** (spec: docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md; all phase-2 rulings live in
docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md §Rulings — binding, do
not relitigate). Headlines: **Trinity of Pints fully redesigned by author** (four-course
drinking-game curriculum — Pub 115 / Song 220 / Greek 330 / Thesis Defense 401 — magnet-cheat
Dean finale, "NOBODY GRADUATES! SECURE THE QUAD!" boss battle vs Dean + 3 professors,
security-guard alley knockout, then the author-dictated Brenda speakerphone scene; grading
system DEAD). **One-phone canon recorded** (phones confiscated on arrival in Euromemeia;
one shared speakerphone-only phone w/ ICQ; Brenda knows she's on speaker — WHY lands in the
author's other window; "Euromemeia" = author-minted continent name, add to world-name canon).
Iron Gut Tripel = next-turn only; beer price band demoted to guideline (Blockchain Bock 18
±5 stays); +5% Confused res = selfie badge only; PNG names = full brewery stems; 28
gatekeeper quotes salvaged as ambient flavor (gating dead); Key Collector achievement dead.
Creative gaps + referee/brewmaster NPCs: Claude drafts, ⚠ AUTHOR-REVIEW batches.
All files written and legacy docs retired; pending: author batch review of ⚠-flagged drafts, then Shamsterdam follow-on when names are minted.

All five design forks resolved by author: (1) keychain = ONE item, openers = one per brewery
EARNED on challenge completion (vendor sales + ICQ opener sales DEAD); (2) 16 breweries
(4×4); (3) Legendary Hangovers = named CONSUMABLES (Full Irish Experience / Neon Nightmare /
Imperial Concerto / Canal Courage — the last is a consumable, not a passive); (4) stamps
earned on challenge completion + brewmaster selfie honor; selfie/scrapbook layer KEPT, Chadwick
posts to his feed; (5) Publandia special-beer order = the one-time trigger granting keychain +
first opener + passport book. **Queued content round:** decompose into per-item .md files
(keychain, 16 stamps, 16 openers, 16 beers, passport book) + merge the six legacy brewery
docs (all six stay until then; master spec overrides on conflict). Merge map is in the five
analyst reports from this session; contradictions list included.

## Standing rulings recorded this round (so no future pass relitigates them)

- **No mascots, ever** (R5 spec §0a rule 1); **story/lore/satire changes require author ruling
  first**; sanitizing/softening = highest-severity defect (§0a rule 2).
- **Dutch cultural-heritage gag cluster** (Pancake House / Klompen shop / herring vendor /
  Condomerie, ~90 lines in Shamsterdam drafts): **KEEP AS-IS, premise treatment** — real-culture
  satire is the spine, same protection as the döner vendors' Turkish heritage. No sweep touches it.
- **Hippo:** one-off Kinder-egg deflation gag + mute junk trinket "Tiny Plastic Hippo"
  (+1 Luck/−1 Int, "It was inside the egg."). No name, no adoption, no evolution, no side
  content, no cameos. Applied on disk in `fabergeegghunt.MD` + both shamsterdam.md copies.
- **Blade Dubbel** and the **beer-style vocabulary exemption** (style terms incl. national-style
  adjectives in descriptions are exempt; item/place NAMES stay strict): author-confirmed.
- **Premise-cluster exemption** (American identity, Europe frame, language names, heritage) and
  **ban-all world names** with minted canon: The Craic Tax, Quay of Last Resort, Publandian,
  Blarney Trap Receipt JPG, Astronomical Cock-Up Square (unified spelling), Bohemian (language),
  the Emperors, Shamsterdammer, Canal Courage, The Old Master Collection, The Inventor's Cut,
  Sinfonian Wheel, Twenty-One Sinfonian.
- **QR ARG pages** (Round 5) are framed as the real internet → exempt from ban-all.
- **SUPERSEDED 2026-08-01:** the euro display-glyph rule is dead by author ruling. The whole game is SOVS; **neither euros nor koruna exist**. Repo-wide retrofit already executed. Canon: `_sorting/Design/Economy/currency.md`.

## Standing ruling 2026-08-06: key_items.json schema (author)

First entry shape for `game/assets/data/items/key_items.json`, author-approved — the standing
schema for all permanent/curse/quest items from now on (do not relitigate): bare snake_case
key (consumables convention), fields `display_name`, `item_class` ("permanent"|"curse"|
"quest"), optional `stat_modifiers` object, optional `per_bro_variants` bool, `source`,
`description` (must carry the item's voice, never flattened). First entry: `student_id`
(Trinity Student ID — design/items/publandia_items/student_id_item.md; its creative fields
remain ⚠-flagged for the batch review; critic-pass sharpenings applied by author order).
GUT baseline note: suite grew 27→36 tests (engine window); all 36 pass.

**Amendment 2026-11-09 (author ruling `prize_fields = "both"`):** the key_items schema gains two
fields. `ticket_price` (int): price in tickets at the Absinthe Arcade Prize Redemption counter;
present only on ticket-bought prizes. `effect` (string or null): the item's gameplay effect in
plain words, `null` when it has none; required on every Absinthe Arcade prize (`aa_prize_*`).
Neither field is required on other key items (`student_id` carries its mechanics in
`stat_modifiers` and was left untouched).
**Amendment 2026-11-09 (author ruling `worn_prizes = "key_cosmetic"`):** worn prizes live in
key_items.json for now with `"wearable": "cosmetic"` (Fangs for Nothing, Sixty-Minute Emerald,
Two-Grand Tie-Dye Tee). They move to equipment.json once an equipment schema is ruled.

## Small ledger (mechanical, any future round)

- Shamsterdam untracked city-file pair (byte-identical flat + folder copies): reorg window
  consolidates (folder copy canonical, matching the other three cities). (bead Eurobound-58a)
- `Design/Quests/Location Specific/Amsterdam/` folder name (real city in a path) — reorg
  window's call. (bead Eurobound-nda)
- `npcs/Old_Town-Square/` folder name (legacy zone name in a path) — reorg window's call.
- Bassline Opera House two-way ID references from older files (ledgered in Round 3 review).
- Post-reorg: re-run the tracked world-names verification greps once paths settle. (bead Eurobound-mb3)

## Merge notes 2026-08-04 (restructure -> main; flags for author/engine windows)

- **Platform re-sweep: DONE 2026-08-04** (four mechanical passes repo-wide over design/,
  legacy/ excluded: Mobile Optimization headings -> Performance & Assets, iOS/Android compression
  bullets -> Desktop S3TC/BPTC with per-file descriptors preserved, ASTC-4x4 exception lists ->
  uncompressed-texture exception lists, iPhone baselines -> min-spec; euro sweep also DONE - one
  real usage fixed, remaining hits are exempt rule-statements). Original note: the legacy-content merges (author-approved)
  ported "Mobile Optimization Requirements" sections (iOS/PVRTC etc.) into the Dec-generation
  specs BEFORE the Steam/desktop ruling landed. Main's platform sweep only hit the old
  superseded copies. One mechanical pass over design/worlds/*/PNG_Assets/ to retitle/trim
  mobile-era content per the platform ruling.
- **theabsinthiumtaproom.md clobber: VERIFIED CLOSED 2026-08-05.** The misfiled paste was a
  strict textual subset of canonical shadowexchange.md (every NPC, mechanic, number, and
  checklist verbatim; its only deltas were STALE — oldtown IDs, "gold" currency). Nothing
  stranded; no action. Side-findings: chat-scaffolding tail stripped from shadowexchange.md
  (per the standing strip-scaffolding cleanup ruling); RESOLVED 2026-08-05 by
  the game-wide ruling below.

## Standing ruling 2026-10-27: the Absinthe Arcade window cat (author)

**The black cat on the Absinthe Arcade facade stays.** It is ambient set dressing, not a
mascot, pet or party companion, so the no-mascots rule does not remove it. It is its own 3D
prop (`aa_prop_window_cat`) sitting on the OUTSIDE of the left first-floor window's stone
sill, and that window is modeled OPEN. Do not strip it in future mascot/pet sweeps. Do not
relitigate.

## Standing ruling 2026-08-05: 60 FPS (author)

**The game-wide performance target is 60 FPS on min-spec hardware — single standard, no
dual floor.** All straggler location targets (35/40/45/50, incl. the shadowexchange 50-vs-60
conflict and every "45 FPS min-spec" line from the platform sweep) normalized to 60 in one
mechanical pass (68 files). Animation frame rates (8/10/12/30 fps etc.) are NOT performance
targets and were untouched. Draw-call/memory budgets unchanged. Do not relitigate.

**Also executed 2026-08-05:** LoadingStrategy.md re-deleted per author ruling (the author's
original Session-3 triage call stands; main's platform-sweep update of it was unaware of the
deletion; recoverable from git history).
- **debaucheryville data JSONs repaired during merge:** interactions/environmental/
  sprite_mapping suffered container corruption on BOTH lines (main: line-sorted wreck with
  fragment blob; branch: records appended outside the object). Rebuilt via record extraction +
  union (branch structure + main-only records e.g. locations_core, crypto-kebab sheets),
  gilded_square sweep applied. Engine window should sanity-check record contents.
- **LoadingStrategy.md**: author deleted it in Session-3 triage; main's window had updated it
  meanwhile. Merge kept main's newer version at game/assets/data/npcs/LoadingStrategy.md -
  author may re-delete if the triage call stands.
- club_flyers.md: main's scrub-round rework won all hunks (Path-B 100-SOVS payment line and
  dev-notes section from the older draft dropped with it - in git history if wanted).

## Engine data sanity-check 2026-08-04 (post-repair verification — PASSED with notes)

All five debaucheryville data JSONs parse; zero oldtown residue; shadow_exchange salvage and
kebab union (crypto vendor sheet + animation sequences + rotisserie) verified intact;
environmental & sprite_mapping are complete supersets of the pre-corruption base. Two
interaction records (kebab_alley_restroom_01, velvet_alley_kebab_01) were transcribed
2026-08-05 from the author-recovered pre-corruption copy (commit 4cf1a75) and enriched the
same day in the recovery-closure round (section below). Their line-soup remains preserved in
commit e0a18a4's fragment blob and in design/legacy/. NOTE: the 4cf1a75 session intended to
record its unplaced-lines list here, but its str.replace targeted stale text and failed
silently ("ledger updated" printed, nothing changed, commit touched only the JSON) — repaired
in the closure section below with the list restored from the session archive. For the engine window: (a) locations.json (16 recs)
vs locations_core.json (6-rec subset) relationship is yours to formalize; (b) AUTHOR RULING 2026-08-05 (supersedes
the 08-04 standalone note, which was based on my misread of the author's question): **the
Clocktower Plaza cellar IS canon** — the venue doc is the author's own year-old rough draft.
Canonical ID stays `debaucheryville_clocktower_tapdatvault_brewery_02`; the three stray
spellings were unified to it mechanically. **Brewery visit order is UNIMPORTANT (author
ruling)** — only the Publandia trigger brewery matters; numeric suffixes in brewery IDs are
identifiers, not a visit sequence, and the passport "slot order" conflict is void; (c) sprite_mapping
carries a separate `..._kebab_01_character_animations` record — verify intended.
**ID clarification (author asked):** `velvet_alley_kebab_01` IS the Late-Night Kebab Stand's
canonical ID (declared in its .md and PNG spec; "velvet alley" = its spot by the Velvet
Curtain alley exit) and `kebab_alley_restroom_01` is the data files' ID for the Grease Trap
Shrine restroom — though its PNG spec declares `kebaballey_greasetrapshrine_restroom_01`
instead: one location, two IDs, needs unification. Only their INTERACTION records were lost
to corruption; the locations themselves are intact everywhere else.

## Recovery closure round 2026-08-05 (unplaced lines placed + stub records enriched)

The deferred later-round (old Task #13) is DONE. The three remaining stub records in
`debaucheryville_interactions.json` were rebuilt verbatim from
`design/legacy/debaucheryville_interactions_precorruption_recovery.json`, attribution per
design-doc cross-reference (absinthearcade.md, clawmachinemaintenanceclosetrestroom.md,
mysterymeatcart.md, Late-Night Kebab Stand.md, greatdonerdebate.md). Boot clean, GUT 27/27.

**The 11 ledgered unplaced lines — final disposition** (list restored from the 4cf1a75
session archive after its silent ledger-write failure):

1. CRT market monitors (kebab prices + meme-coin candles) — RESOLVED: duplicate of the
   intact shadow-exchange record's `crt_monitor_wall_live_markets`; already placed.
2. Eldritch-meat-glyph cracked mirror cluster — PLACED: Grease Trap Shrine restroom
   (its PNG spec lists the glyphs incl. the sheltie-paper-crown; the greasy-prophet tracking
   line "…haiku_pixel_kebab_mirror_glyphs…" requires it there).
3. chili_sauce_trail_investigation — PLACED: restroom (3AM crawlspace guidance per PNG spec).
4. beer_pong_saint_relic NFT target (claw `prizes` block) — PLACED: arcade claw machine.
5. kebab_coins_to_tokens 1:5 — PLACED: arcade token_exchange_machine.
6. vip_wristband_png_acquisition — RESOLVED: duplicate; both copies live in the intact
   shadow-exchange record.
7. "emotional_impact" line — PLACED: closet's Tekken-virginity haiku (crude-subject match).
8. pop_rocks_relish — PLACED: cart's Clown Dog Deluxe™ (menu doc).
9. Hand-dryer hygiene gag — PLACED: closet's used_socks_prize_chute.
10. NFT_4_LYFE wall scrawl — PLACED: Late-Night Kebab Stand street details (its .md and
    greatdonerdebate.md both put the scrawled wall at Chadz's cart).
11. ai_particle_system circuit-under-meat — PLACED: cart's Glizzénstein's Brain Brat.

**Corrections to earlier best-effort content (all doc-evidenced, all values preserved):**

- Mr. Chadz's dialogue: "Mystery meat builds character…" and "One bite and you'll see God…"
  are Chef Chuckles catchphrases (mysterymeatcart.md) — moved to the cart record; "This
  place accepted crypto before it was a currency…" is an arcade original line
  (absinthearcade.md) — moved to Backpack Girl. Chadz gained his own doc-listed lines
  ("intestinal roulette", FDA-2019); "Meats mostly legal…" stays his.
- `fluorescent_meat_skewer_light` + `pixel_kebab_googly_eyes` moved kebab-stand → restroom
  (Grease Trap Shrine PNG spec places both; a ceiling tile also only exists indoors).
- Engine-stub arcade record: Backpack Girl's couchsurf block had the SE ex's morning scene —
  replaced with her recovered ukulele-6am block; the hackers' dialogue_samples were verbatim
  duplicates of the ex's SE lines — dropped (they live at the SE record); the "12-hour
  session" line moved to the speedrunners (foot-soak decompression).
- **CryptoBro69's-Ex couchsurf block does NOT belong to the cart.** The 4cf1a75 session's
  parenthetical was wrong: a full census of the soup's 10 NPC blocks vs 10 zone lines shows
  `behind_mystery_meat_cart` is Chef Chuckles's own vendor zone; the ex's single couchsurf
  block is fully accounted for at the shadow exchange. Nothing is missing from the cart.

**Held back, NOT transcribed (still safe in the recovery file), author's call someday:**

- ~~"This'll put hair on your chest! And possibly remove it too."~~ — **KILLED by author
  ruling 2026-08-05 ("cheesy")**; never place it anywhere. (The Three Crown Keghaus's
  different hair-on-chest/depth-perception line was not part of this ruling and stands.)
- `"interaction_type": "cultural_artifact_examination"` — no confident home.
- Machine `token_cost` values 2/3/4 for Frogger/Street Fighter/Kebab Kombat — per-machine
  mapping unknowable (only the DDR's 3-token cost is doc-anchored and transcribed).
- Minor judgment calls flagged for review: closet graffiti wall-position assignments and the
  three arcade-machine main-floor positions are census-derived (sets match, per-item pairing
  partly arbitrary); haiku-cluster lines split between the two haikus by subject-matter.

**RULED 2026-08-05 (author): cart menu prices are SOVS.** The soup's `kebab_coins` unit on
the Mystery Meat Cart menu is superseded; the quest docs' SOVS pricing (5/6/7/9/12) is canon
and the data record now uses `{"sovs": N}`. Do not relitigate. (Scope: this ruling covered
the cart menu flag; kebab_coins as the arcade/shadow-exchange alt-currency was not touched.)

---

## DEFERRED 2026-08-06 — quest-doc debt surfaced while designing the quest-creation skill

Found while auditing `design/Quests/` for the `eurobound-quest-creation` skill
(spec: `docs/superpowers/specs/2026-08-06-quest-creation-skill-design.md`). None of this was
touched — the skill routes only what it creates. Author to pick these up.

**1. Five stub general quests — latent instanced quests, never written.** Each is 2-4 lines
and describes per-city content it does not contain:

| File | Lines | The tell |
|---|---|---|
| `vinylhunt.md` | 3 | "hidden in each world's seedier corners" |
| `streetperformertrials.md` | 4 | "Scattered across all cities" |
| `taxidriverconfessionals.md` | 3 | — |
| `selfiewithlocallegend.md` | 3 | — |
| `undergroundkaraokeleague.md` | 3 | — |

Under the skill's classification these are `GENERAL-INSTANCED`: they need a master spec plus
per-city instances. `wifiroulettegame.md` (2 lines) is the one genuine systemic quest of the
twelve — "at any free Wi-Fi hotspot" — and needs only a single file. (bead Eurobound-apz)

**2. `greatdonerdebate.md` is undecomposed.** 656 lines with `## BASE GAME LOCATIONS` and
`## SHAMSTERDAM DONER LOCATIONS` inline in one file. Same shape the Brewery Tour
decomposition fixed. Wants a master spec plus city instances. (bead Eurobound-0xz)

**5. `data/quests/flags.json` does not exist.** `sidequest_template.md` requires every quest
flag be registered there. Needs an author schema ruling — the sync skill will not invent one.
Until then quest flags live only in the design docs' flag tables.
(updated 2026-11-11, Eurobound-j50: `game/assets/data/world_data/quest_flags.json` now exists as an empty
stub, `"quest_flags": {}`; the schema still needs an author ruling, bead Eurobound-vyn.)

**6. `Tools/validate_data.py` has no quest handling.** It will not validate quest JSON at all.
Open question: should it, and to what depth?
(updated 2026-11-11, Eurobound-j50: `tools/validate_data.py` now checks quest JSON against the canonical schema
(`check_quest`, af3e4da, bead Eurobound-e8c closed); the depth question stays open, bead
Eurobound-vyn.)

---

## Standing rulings 2026-11-02: Absinthe Arcade (author)

- **All Arcade money is SOVS.** The token exchange takes SOVS at **1 SOV = 1 token**. The old
  kebab-coin 1:5 rate is struck in the design package and in the engine data
  (`debaucheryville_locations.json`, `debaucheryville_interactions.json`). This settles the
  arcade half of the open kebab_coins question; the shadow exchange's kebab_coins are still
  unruled.
- **DDR restroom unlock: 3 tokens** (confirmed). **Claw machine: 5 tokens per attempt.**
- **Interiors are Bravely Default style**, with the same **fixed HD-2D tilt camera** as the
  exterior.
- **The mezzanine is visual only.** It is not a walkable floor.
- **Backpack Girl's cabinet-side spot stays on the primary route.**
- Do not relitigate.
- **Arcade cabinets are battle encounters, not mini-games.** Frogger: Existential Edition,
  Street Fighter: Identity Crisis and Kebab Kombat each release 2-3 game-inspired villain
  types that fight the bros through the existing battle system. The rigged claw machine stays
  the Arcade's one real mini-game. **Interior size: 15.4 x 18 real metres** (main hall about
  15 x 12 m, north L-wing about 8 x 6 m), framed for one fixed-tilt screen.

## Standing rulings 2026-11-08: Arcade interior and party sprites (author)

- **Real brand and game names stay as drawn** (HORNETS jersey, cap and polo logos, and real
  arcade titles such as Frogger, Street Fighter, DDR, Time Crisis, PAC-MAN). Do not swap them
  for parodies or strip them.
- **The Green Fairy mural appears inside the Arcade too**, not only on the facade.
- **Backpack Girl's hours are 14:00 to 22:00.** (The environment file's 14:00 to 04:00 was
  the stray value and is corrected.)
- **Party sprites:** Chadwick is the "38yearoldchadwick" sheet (B) and Bradley is the
  "16-Bit Hornets Sprite Sheet" (#1, B). All three bros are the same height (1.8 m).
  Pilsner walks with his arms swinging, not hands in pockets.
- **Interior main hall:** the game-camera framing (concept C) is the base. It must also hold
  the token/prize redemption counter built into the bar, and a three-pad DDR dance-off with
  one big wall screen everyone can watch (see the author's ChatGPT brief "Revise Arcade
  Layout" and `references/Interior/concepts/README.md`).
- Do not relitigate.


## Standing rulings 2026-11-09: Arcade villains, payouts and interior (author)

- **CONTINUE? paid revive belongs to Count Continue only.** 270 Vratislav and Croc Monsieur
  get new finishers of their own.
- **Wallet theft belongs to Sinking Fund only** (Buy the Dip). Count Continue keeps only his
  paid continue.
- **Existential Crisis is out of the Arcade villains.** Swap it for Confused or Embarrassed,
  "game-appropriate and slightly ridiculous". Bros react instantly and confidently.
- **Arcade fights pay TICKETS, not SOVS.** Tickets are redeemed at the Prize Redemption
  counter in the bar for 90s pizza-arcade junk: wax lips, plastic vampire teeth, fake rings
  that turn your finger green, sticky hands, finger traps, slap bracelets, dyed rabbit-foot
  keychains, ball-in-maze puzzles. "Better" prizes, absurdly bad value: a pizza-mascot
  plushie, pink and yellow pump water guns, whoopee cushions, a tie-dye "I love Absinthe
  Arcade" t-shirt. Ticket amounts and prize prices still need numbers.
- **Cabinet token costs: Frogger 2, Street Fighter 3, Kebab Kombat 4** (1 token = 1 SOVS).
- **Line-ups per cabinet:** Kebab Kombat uses a fixed resetting ladder; Frogger and Street
  Fighter use weighted random tables.
- **All proposed villain mechanics are approved** (wallet steal, enemy revive, untargetable
  dive, swallow, ally-KO and allies-alive AI triggers, Second Thoughts re-roll, mid-fight
  nameplate change, palette-spawn roll), as are the villain stats, XP, drops, 12 items and
  9 achievements. The Frogger lady-frog background gag stays.
- **Interior is built by projecting the approved paintings** onto graybox geometry, with a
  fixed camera per room. **No people are painted into room art:** every person is a movable
  NPC sprite. Hall v8 clean plates (people removed) are the hall's source.
- **Bros are sized to the furniture** (counter at waist height), not to the painted patrons.
- **North wing v4 is approved.** The interior asset list is approved.
- **The mirror corridor is its own screen** between the hall and the north wing.
- **Battle cabinet placement:** two in the back row, one on the right wall.
- **The three-pad DDR dance-off is playable:** a mini rhythm game. The player picks one bro
  to play, and the other two are game-controlled. Doing well, they still look dumb dancing
  cringily to the hits; doing badly, they look even more ridiculous. Songs named by the
  author: 90s/00s hits (Khia, Madonna, Christina Aguilera, Beyonce).
- Do not relitigate.
- **(Later on 2026-11-09)** Hall exit to the mirror corridor: an open archway in the back
  wall under the mural, between back-row cabinets 3 and 4 (option A). Battle cabinets: Frogger =
  back-row cabinet 2, Street Fighter = back-row cabinet 4, Kebab Kombat = right-wall cabinet 6
  (numbering on the decisions-page image). DDR dance-off: 2 tokens per song, 0-30 tickets by
  score, and **the real songs are licensed** (not sound-alikes); budget for master and
  publishing licences per track.
- **(Review round, 2026-11-09)** Approved: Croc Monsieur's "The Bill Will Find You" and
  270 Vratislav's "The Other Two-Seventy" finishers; "Still or Sparkling, Monsieur?"
  (Confused) and "Where Do You See Yourself in Five Lanes?" (Embarrassed); Count Continue's
  INSUFFICIENT CREDITS rule; the per-villain ticket payouts; the 13-prize Prize Redemption
  catalogue with its prices and effects.
- **Real names (author, verbatim): "The only thing that never gets the real name is
  locations. ALL other things get their real names."** Real brands, products, games, songs
  and titles keep their real names in game text and art; only locations get parody names.
  The pizza-arcade plush is the **Chuck E. Cheese Plush**.
- **Interior depth curve:** characters shrink from full size at the front of the bar to about
  68% at the hall's back wall.
- **(Round v18, 2026-11-09)** Key-items format gains `ticket_price` and `effect`. The three
  wearable prizes (Fangs for Nothing, Sixty-Minute Emerald, Two-Grand Tie-Dye Tee) live in
  key items as cosmetic wearables until an equipment format exists. Brand sweep approved:
  find every parody stand-in for a real brand/product/title, list it for the author, then
  rename the approved ones to the real names (locations excluded).
- **Brand sweep rulings (author, 2026-11-10).** Rename: Napstur -> Napster, "Guiness
  Suppositories" -> "Guinness Suppositories", Guooi -> Gucci, Rayban -> Ray-Ban, The Matricks ->
  The Matrix, Johnny Nemonic -> Johnny Mnemonic. **Keep, intentional:** EMTV (the European
  version of the network), The One True Pils ("it's funny"), Hamagotchi, iPawd, Kebab Kombat.
  Venues with real names (Brouwerij de Molen, FEBO Automat) get parody names; names to be
  proposed to the author.
- **Image-tool allowance (author, 2026-11-10):** to fix the hall's last see-through spots, use
  ChatGPT's image generator; failing that, **one** Seedream 5.5 layer decomposition on
  AtlasCloud. AtlasCloud charges per image: use it for nothing else.
- **(Round v21, 2026-11-10)** Venue renames: FEBO Automat -> **Frietomat** (author: Dutch
  "friet" plus Frito); Brouwerij de Molen -> **The Wobbly Windmill Brewery**. Standing
  permission to use ChatGPT's image generator, including downloading its results, for any art
  task.
- **(Round v22, 2026-11-10)** Hall v8f approved (final hall art for now). Leftover euro prices
  in design docs convert **1 euro = 1 SOVS**, numbers unchanged. Every Shamsterdam brewery
  except The Wobbly Windmill Brewery gets a new name (proposals to the author).
- **(Round v23, 2026-11-10) Shamsterdam breweries.** Proeflokaal 't Kansen -> **Bottoms Down**
  (name only; Kees, the jenever bar and the no-hands bow all stay). New brewery #3 -> **The
  Hoisted Pint** (the canal house 1.5 m wide and six storeys tall that leans like its
  customers; kegs and bros go up the front in a cargo net on the gable hoist hook). New brewery
  #4 -> **The Mad Monarch's Wit-tea Party** (author-minted; the Monarch's Birthday party
  thrown every day since 1998, everything orange, the bouncer paints anyone in another colour
  orange; **specialises in brewing, serving and selling wheat beer / witbier**). Concepts
  approved. Each new brewery's tour challenge, consumable beer, opener, stamp, selfie spot,
  brewmaster NPC and prices still need author rulings. Real-city sweep approved: player-facing
  text moves to the parody names; internal planning notes stay. Price cleanup approved: round
  to whole SOVS (0.50 -> 1, 3.50 -> 4, 8.99 -> 9) and fix odd wording ("Two SOVS fifty",
  "SOVS gold").
- **(Round v24, 2026-11-10)** The Hoisted Pint and The Mad Monarch's Wit-tea Party: every
  proposed detail approved as written (challenges, beers, openers, stamps, selfies, brewmasters
  Thijs and Sjors Hoedemaker, prices). The Wobbly Windmill's beer stops being a witbier so the
  Mad Monarch owns wheat beer. Shamsterdam brewery docs say four breweries, visit order free.
  City sweep's two rewritten jokes approved ("Formerly Known as Sober"; the catalogue "two
  cities east"). Sweep ALL remaining real place names to parody names (incl. Breadgasmia's
  Paris+Prague note, Nora's Galway history, "Dublin slang", marketing POV lines, the Arcade's
  "Prague-inspired" briefs). **Singular is "1 SOV"** (currency.md canon); plural SOVS.
  Price jokes: Willem's hat "exactly 247 SOVS"; the Frietomat croquette is 3 SOVS everywhere;
  Lotte's fridge magnet 3 SOVS (cheapest in her shop). "Gold" as a money word -> SOVS.
- **(Round v24, Arcade build, 2026-11-10)** Battles: HD-2D side view, bros and enemies both on
  screen in a 3D arena. Overworld: a leader with the other two following in a line. Tokens:
  the TOKENS HERE machine sells any number at 1 SOVS each; tokens live in the inventory.
  Can't afford a cabinet: the INSUFFICIENT CREDITS screen gag. Lose an arcade fight: back in
  front of that cabinet at 1 HP, tokens spent. No interaction cue (face it, press the button).
  Cabinet fight backdrop: that cabinet's own game art. Hall NPCs: the bartender, bouncers and a
  birthday party from the author's ChatGPT chat "create hero image prompt", plus the
  absinthearcade.md regulars. DDR: **songs are licensed and in hand; build with the real
  songs**; four arrow lanes; a difficulty screen permanently stuck on Hard/Expert, to the bros'
  frustration. Load the 9 Arcade villains into engine enemy data as their docs propose, plus a
  `ticket_reward` field. Mirror corridor painted with ChatGPT; north wing upscaled to
  2752x1536 with a registered day version.
- **(Round v25, 2026-11-11)** Mirror corridor (ChatGPT, v1 night/day) and north wing v5
  (v4 cropped to 16:9 + day) **approved in game**. Cabinet battle backdrops: paint them
  (ChatGPT). Battle maths: **author's** — use the existing battle system in
  `design/mechanics/Battle/` (research it; no placeholder formula). DDR: tickets = 30 x share of
  steps earned (PERFECT 1, GREAT 0.7, GOOD 0.4, MISS 0), rounded; step charts generated
  automatically from the songs and play-tested by the author; the bros' stuck-difficulty lines
  go to the Writers' Room (author approves). **Deferred to 2026-11-11 by the author:** DDR song
  files/list, chart generation, dance animations, north-wing contents. Token machine with 0 SOVS
  shows INSUFFICIENT CREDITS. Tab enforcers are **Accounts Receivable** (nameplates ACCOUNTS and
  RECEIVABLE), all proposed stats/moves/rewards/loss/flee rules approved. Cara's 21st tab:
  five shots 40 SOVS, service charge 10 SOVS flat, tab does not grow, proposed timing/opener/
  trigger approved. Junk prize shelf separate from the 13-prize catalogue (5-15 tickets, no
  effects, no duplicates). **Skee-ball and foosball are real mini-games** (costs/payouts
  delegated to Claude) and **the claw machine must exist and work**. **Token Attendant**
  (author): a separate employee from the prize-counter bartender, also in TGI-Fridays-style
  flair; fixes stuck ticket machines and token-exchange problems and services the bathrooms;
  the bros catch him asleep in the arms of a statue repurposed as a toilet-paper holder,
  passed out on absinthe. Torte Royale: Bradley's +20% pronunciation bonus is replaced by a
  different bonus (options to the author). **The hippo's former name: an agent removes every remaining mention
  from the files.** Unanswered, to re-ask: hall names, hall bouncers vs enforcers, Pilsner
  "newly single".
- **Ticket-game numbers (set by Claude under the author's v25 delegation):** Skee-ball 2 tokens
  a game (9 balls), 0-20 tickets by score; foosball 2 tokens a game vs an NPC, 15 tickets for a
  win, 3 for a loss; claw 5 tokens (ruled), prize or nothing; DDR 2 tokens a song, 0-30 tickets
  (ruled).
- **(Round v26, 2026-11-11)** Battle numbers approved as proposed in
  `design/mechanics/Battle/battle_numbers_proposal.md`:
  - Bravado tiers are Low below 1/3 and High at 2/3 or more. The damage modifier is +half max Bravado at High, +quarter at Mid and -2 at Low.
  - Damage spreads ±2, with a minimum of 1.
  - SMAAAASH crit chance is Luck%, +10 at High, minus half the target's Grit, minimum 1%. A crit doubles damage.
  - Speed is ±2 at High/Low Bravado. Flex restores 3 Bravado. The rolling HP meter drains 10 HP/s.
  - Run chance is 50% ±5% per point of average-Speed edge, clamped 10-90%. Running from a cabinet fight spends the tokens, keeps HP, and returns the bros to the cabinet.
  - Bradley: HP 30, Bravado 14, Off 12, Def 2, Spd 8, Charm 4, Luck 5, Grit 3. Chadwick: HP 35, Bravado 20, Off 6, Def 3, Spd 7, Charm 10, Luck 6, Grit 2.
  - Everyone starts with Attack, Item, Flex and Run; Pilsner also has Roast Line.
  - **Roles follow battle_system.md: Pilsner is the tank, Bradley the glass cannon.** party.md is wrong on this point.
  - Claw rig approved: the claw slips unless the PAYOUT light blinks, on a hidden every-N-plays cycle the Token Attendant hints at. It pays the Beer Pong Saint Relic or nothing until the relic is won, then junk-shelf prizes. **Both claws work** (the rigged absinthe claw and the Beanie claw).
  - Cabinet battle backdrops approved, but Kebab Kombat's top is to be repainted to match the neon cabinet bezel of the other two.
  - Ticket machines do not jam; it's background flavour. Gemini, via the Writers' Room, writes the ambient lines that the "absinthe drunken pimple faced" Token Attendant mutters when the bros walk near him.
  - Token Attendant scene approved: a new public restroom screen (to be painted), a bronze Green Fairy statue used as a toilet-paper holder, triggered on the first bathroom visit after 01:00. The Arcade Employee's machine-reset job merges into him.
  - The hall "bouncers" ARE Accounts Receivable.
  - **Lord Pilsner is newly single, game-wide canon (author): "It's part of why they went to Euromemeia."**
  - Torte Royale: Bradley's bonus is **Quark Is Protein**. He decides Topfenstrudel is a protein bar, so it heals him double (+30 HP / +30 SP), and he orders it every visit.
  - Unresolved (the notes said only "notes"): the hall names and the Cara's 21st leftovers.
- **(Round v27, 2026-11-11)** Cabinet-battle numbers approved as recommended:
  - Damage words map to multipliers: light/low x0.7, standard x1.0, moderate x1.2, heavy x1.5.
  - Accuracy: base 95% to hit, -9% per step; a miss does 0 damage.
  - Social damage = (Charm + Bravado Mod) - target's Grit, with the same multiplier, spread, floor and crit as physical; the Social resistances apply.
  - Statuses in battle use the villain-doc versions: Embarrassed is -20% ATK, -2 Bravado a turn, and locks Bravado-cost moves and Ultimates; Gains Bro is +20% ATK. Hardcore Gamer is +1% crit.
  - Stun: lose the next turn, does not stack. Confused: each action targets someone at random, never the actor.
  - Honk If You've Peaked drains 2 Bravado from each bro. Short move tables are scaled up to 100%. Full Crossing's 10% is spread proportionally before the first win.
  - A multi-villain fight pays the sum of their tickets. A downed bro leaves a won fight at 1 HP. Street Fighter always uses 2 Palette Swaps until levels exist.
  - **The v26 Bravado thirds apply game-wide**, replacing the 2026-08-06 25%/70% bands.
  - Lasting statuses (Tourist Trap Victim, Food Poisoning 5-8 battles, Broke AF, Grease Fingers) persist after the fight.
  - Villain leftovers are approved: Sinking Fund's soggy-pile refund (80%/20%), Jarmila's defeat counter, and the Mystery Brown 5% spawn.
  - Rigged claw: the PAYOUT light blinks every 7th play; the old skill method is dropped.
  - Art approved: the public restroom v1 night/day and the Kebab Kombat backdrop v2.
  - Deferred by the author to the morning: the hall names and the Cara's 21st leftovers.
- **(Round v28, 2026-11-11)**
  - **Decisions-page bug (Claude's):** on any question with an option keyed "notes", the typed note was lost and saved as the word "notes". This affected rounds v25-v28. The bug is fixed and the author has been asked to re-enter lost notes. Earlier "notes"-only answers are lost text, not empty answers.
  - The restroom door is the arched doorway in the hall's left wall beside TOKENS HERE.
  - Cabinet villains get +50% HP.
  - Embarrassed lasts 2 turns and Grease Fingers 4 (Sauce Spray, EXTRA CRISPY!, Initials Entered, Hug, Close Shave).
  - Claw controls: up to 10 s to steer left/right, then drop; the claw grabs whatever is under it.
  - PAYOUT light: the plays counter is saved. After 6 plays the light blinks before the bros pay, and that grab holds only if it is over the relic. The cycle restarts after any blinking play.
  - The Beanie claw grip holds 1 in 3 times.
  - The Beanie prize names and the junk-shelf item names go to the Writers' Room.
  - Write the Beer Pong Saint Relic doc from canon (NFT template) and register it.
  - **Villain battle sprites: go**, all nine through the sprite pipeline.
  - **Names:**
    - The bartender is **Tomáš "Two-Fifty"**.
    - The Token Attendant is **Jakub "Tokens" Dvořák**. The bartender orders him around: "Tokens. Toilet."
    - The Blonde Girl is **Woo Woo Whitney**. The other girls are **Brynleigh, Ashleigh, Kenleigh**.
    - The quest is **Grandpa Provides**, and the ring is the **Promise-ish Ring**.
  - **Cara's 21st (author):** "The ring happens at the bartenders table. There is no ring having anything to do with Cara." The girls never give Pilsner a ring; the ring is only the prize-counter tip beat. The scene must follow the author's ChatGPT story. Fix the doc and show the author the full interaction.
- **(Writers' Room desk, 2026-11-11 15:21, via eurobound-48)**
  - **The rigged claw pays out Sea-Monkeys (Mint #73), not the Beer Pong Saint Relic.** Author, verbatim: "replace the beer pong saint relic with Sea-Monkey". The relic stays struck as of 2026-08-01, which settles round v29 relic_nft.
  - Prize names approved ("Approve Gemini's favourites"):
    - Beanie claw plush: Pre-Emptive Perry, Pets.con the Sock Hound, Snorty the Bouncer Badger, Mugshot Mandy, Minty the Rare Mint Bunny (Minty's tag poem reworded to SOVS).
    - Junk shelf: Terminal Velocity Terry (parachute men, 10 tickets), Forty-Eight-Hour Tramp Stamp (temporary tattoos, 10 tickets), The Noise Violation (the whistle, 15 tickets), and the Promise-ish Ring (5 tickets).
    - Final text with tag poems and inspect lines: WritingRoom/tasks/20261111_0622_absinthe_arcade_prize_names/final.md.
  - The Beanie claw's price per play is still unruled.
  - Game-wide rule (now in CLAUDE.md): every junk item gets a short, really funny inspect line.
- **(Round v29, 2026-11-11)**
  - Restroom entry: the bros press the button facing the wall just south of the TOKENS HERE machine. No repaint.
  - After the top prize is won, the rigged claw stays rigged: junk grabs hold only on a blinking PAYOUT play.
  - The nine villain battle sprites are approved, and Count Continue keeps his size.
  - **Arcade NPC sprites approved:** Jakub (plus his asleep-in-the-statue pose), Tomáš, Cara, Woo Woo Whitney, Brynleigh, Ashleigh, Kenleigh, and both Accounts Receivable enforcers, all through the sprite pipeline.
  - **Name clashes:** the author's new names stay. The older NPCs that share them get new names (VCC bouncer Tomáš; Jakub "Euro Ink" Novák, Receptionist Jakub, and the Astronomical Cock-Up quest's Jakub; Miroslav "Father Miro" Dvořák and Václav "Vintage" Dvořák).
  - **Grandpa Provides scene:** "Ask chatgpt in its chat window to review and find the interaction between the bartender and the bros as there are lines and we are missing them. The entire interaction here between them is off."
  - **fratbronft.md conflict:** "Show me all and I will decide case by case."
  - Unanswered: the Beanie claw's price; 5 tokens stays as a placeholder.
- **(Round v29 resubmit, 2026-11-11 15:32)** The Beanie Baby claw costs **2 tokens** a play. The rigged claw stays at 5.
- **(Round v30, 2026-11-11)**
  - **Grandpa Provides is approved as written** (Tip / Approach / Unsettled Tab). Author's addition: "I think Accounts Receivable should be able to steal SOVs from them to help... recover the funds." A SOV-steal move for the enforcers is ruled in principle; its numbers go to the author.
  - Gap rulings:
    - The tip scene is unmissable; it plays the first time the bros use the prize counter.
    - The bros can pay the tab early by talking to Tomáš at the bar.
    - "Grandpa Provides" is the title only.
  - Promise-ish Ring inspect line: "A jewel of uncertain plastic origin. Makes your finger look 4% wealthier."
  - **Renames (older NPCs who clashed with the new Arcade names):**
    - the VCC bouncer Tomáš becomes **Kamil "Stone Face" Černý**
    - Jakub "Euro Ink" Novák becomes **Donát "Euro Ink" Novák**
    - Receptionist Jakub becomes **Radek**
    - the Astronomical Cock-Up local Jakub becomes **Milan**
    - Miroslav "Father Miro" Dvořák becomes **Miroslav "Father Miro" Kalich**
    - Václav "Vintage" Dvořák becomes **Václav "Vintage" Ročník**
    - Antonín "Tonda" Dvořák becomes **Antonín "Tonda" Pískal**
    - Tram Stop Tomáš Procházka becomes **Hubert Procházka**
  - fratbronft.md conflict (author): "We don't need to keep side a or side b. They're all generic crap." The block is removed.
- **(Round v31, 2026-11-11)**
  - Accounts Receivable's **Shake Down Payment** is approved as option A:
    - 5 SOVS per shake, paid toward the 40 SOVS tab.
    - It fires 15% of the time while a balance is due; Itemized Beating drops from 40% to 25%.
    - The bros never lose more than the 50 SOVS a loss costs.
  - Cara's group stands on the open floor just west of the prize/bar counter, toward the skee-ball lanes.
  - In the Astronomical Cock-Up scene, Milan is the one who says "Look. The Americans are crying."
  - A successful Run from the dispute fight counts as winning.
  - Choosing PAY with less than 40 SOVS shows "NOT ENOUGH SOVS" and the choice comes back.
  - Catalogue prizes are one of each; junk-shelf prizes can be bought repeatedly.
  - NPC sprite queue resumed.
- **(Round v32, 2026-11-11)**
  - The Arcade NPC sprites are approved: Jakub, Tomáš, Cara, Woo Woo Whitney, Brynleigh, Ashleigh, Kenleigh and Accounts Receivable.
  - Cara's group is in the Arcade from 20:00 to 02:00.
  - Jakub's asleep pose is to be shrunk to his standing scale.
- **(Round v33, 2026-11-11) 3D session budget approved as written.** Binding text: `design/style_guides/3d_asset_rules.md` → "Session budget" (the draft was deleted once it was promoted). Bead Eurobound-wv6.
  - Rules 1-8 are approved.
  - The numbers are approved: 3 Tripo tries per asset stage, 15 Blender calls per stage, and a hand-off at about 150K tokens.
  - Tripo runs through its API by default; the browser is used only for Asset Extraction. This changes the "Tripo in the browser" wording in 3d_asset_rules.md.
- **(Writers' Room desk, 2026-11-11 19:06; relayed by eurobound-48) Tony420 / FREE Wi-Fi hijack**
  - Tony's first ICQ hijack (the FREE Wi-Fi hotspot event) sets `tony420_unlocked`.
  - The Meme Black Market's second condition, `tony420_contact_unlocked_and_rare_memes_acquired`, becomes `tony420_unlocked` plus the rare-memes check.
  - Tony's goon sprite slot ("Tony420 Fake Crypto", Cyberspace Kavarna PNG spec) is now the goon holding the tablet, made at 128x128 on the character sprite pipeline. He's staged only after the Shamsterdam Döner Debate; before that, an hourly patron sits in the chair.
  - **Unbuilt:** the game has no ICQ, hotspot or Tony420 hijack code yet. eurobound-5d has recorded the plan but isn't building it (it's outside the Arcade). The data files are with eurobound-e3.
- **(Author, in eurobound-e3's chat, 2026-11-11; relayed)**
  - Strike "not mean-spirited" everywhere. It was Claude-inserted softening; struck from 51 design docs.
  - Strike "Harvard MBA" from Bobo.
  - Vlad's "$60,000" becomes **60,000 SOVS**.
  - New Arcade assignment (verbatim): "Our writers should decide upon a few hidden items in the absinthe arcade. Like all good rpgs there should be hidden things in the area and maybe chests (or their equivalent for this game)". Writers' Room task 20261111_1436_absinthe_arcade_hidden_items_and_stash_s, bead Eurobound-o9f; it needs an OpenRouter top-up before a round can run.
- **(Round v34, 2026-11-11) North wing, game clock, eurobound-e3's bead questions.** Answers were submitted on the fixed copy of the page (https://claude.ai/artifact/KWkd2o893UpDYmfCVpv2Ed); the original page's Submit was broken by my missing-field bug.
  - **North wing.**
    - The green curtain becomes the Absinthium Taproom entrance, as designed (`absinthium_taproom_curtain`, `absinthium_taproom_entrance_discovered`). Author: "go ahead and make it using the the_absinthium_taproom file and those in the subfolders to design it. use gpt image 2.6 sunburst in chatgpt".
    - The MAINTENANCE ONLY door becomes the Claw Machine Maintenance Closet Restroom door, as designed. Author: "use the clawmachinemaintenanceclosetrestroom.md and its othe files from the subfolders to design it with gpt image 2.6 sunburst in chatgpt".
    - The broken DDR becomes the 3-token unlock for the maintenance door, as designed. Author: "and when it unlocks it should play the bars \"I wanna shoop baby...\"" (Salt-N-Pepa, "Shoop"; real title kept).
    - The 15 cabinets stay set dressing; only the Time Crisis cabinet does anything.
  - **Game clock.**
    - Time moves only when the bros act, never while the player stands still or reads.
    - Day/night uses one rule for every screen: night 20:00-06:00, switching when a screen loads.
    - The time shows only on Pilsner's digital watch, in the menu.
    - Venues throw the bros out at closing. "Morning" is the next rest, which jumps the clock to 10:00.
    - A new game starts at **10:00** (morning), not 20:00.
    - Tick costs are still OPEN. Author: "How does time typically move in similar jrpgs?" It is to be answered with a comparison and re-asked.
  - **eurobound-e3.**
    - e3_commit: yes, commit and push as each bead lands.
    - e3_budgets: leave the 67 values TBD until a real performance pass.
    - e3_controls: an agent proposes mouse/keyboard + controller mappings and the author approves.
    - e3_png: use the location asset-spec sizes.
    - e3_slugs: approved.
    - e3_gag: punch up the openers' Material Gag rows in a writing round, after a credit top-up.
    - e3_grist: Set A (11%, +40 HP/+20 SP/+15% Speed for 3 turns, Navigation -20% for 5 turns, not sold).
    - e3_genever: one item, using the menu's numbers (6 SOVS, +25 SP).
    - The Shakes (Oude Genever) is -15% Accuracy for 3 turns (author, bead page, 2026-11-12, Eurobound-r1c: "-15% accuracy for 3 turns"); the legacy passport's -20% is superseded.
    - For both beers, author: "the name needs work. This is too high brow and official.... Remember, this is *satire* and *parody*. It isn't supposed to read as serious". Both need new parody names.
- **(Round v35, 2026-11-11) Clock costs, controls, Shoop, menu, Taproom and closet art.**
  - **Clock tick costs:** minutes per action. A screen change is 10 min; a fight or minigame (cabinet battle, DDR song, claw, skee-ball, foosball) is 20; buying or drinking a drink is 10; talking is free. The Meme Black Market kiosk's "exactly 3:33 AM" therefore becomes a 03:33-03:59 window.
  - **Desktop controls (e3_controls2): both approved as proposed (bead Eurobound-lbi).**
    - Battle peek: hover to peek, then hold right mouse button or Tab to pin. On a controller, hold Y for 0.4 s; a held Y on a status icon opens cures.
    - Bike crossing: W/S or Up/Down moves one lane, staying idle holds position, and Shift+Up sprints. On a controller, a D-pad press or stick flick moves one lane and RB+Up sprints.
  - **"Shoop" unlock clip:** the author will supply the audio file (`game/assets/audio/arcade/shoop_unlock.ogg`).
  - **Menu:** an agent proposes a menu from canon (sections plus a mock-up) for author approval. Pilsner's watch goes in it.
  - **Closet restroom art:** version 2 is approved (`concepts/aa_interior_maintenance_closet_v2_night.png`).
  - **"Pixelated boobs" graffiti:** keep it as blocky pixels under a big CENSORED bar, so nothing is shown. This replaces the engine data's "age_appropriate" softening.
  - **Taproom art: changes.** Author: "There shouldnt be the massive hole in the floor and the table shouldnt be tipping over". To be redone.
- **(Round v36, 2026-11-11) Taproom v2, closet framing, graffiti, Konami line, game menu.**
  - **Taproom art v2: changes.** Author: "version 2 is considerably better... but we can't just have liquid forever pouring onto the floor either. How about some form of recirculating neon pipe that comes from the broken bottle and circulates back up around the bottle and back into the broken bottle? That way it has somewhere to go continuously and gives the room another cool glowing element". Version 3 will add the recirculating neon pipe.
  - **Closet framing:** re-paint the same room framed from further back and wider, with the bros about 1/3 of the screen height like the hall. The approved v2 contents carry over.
  - **"Pixelated boobs" graffiti: uncensored. This supersedes the v35 censor-bar ruling.** Author: "we dont need to censor it. It's an MA game... and it's freaking pixelated boobies. who cares?" Crude pixel-art graffiti boobs are in-bounds; the author treats them as outside the no-nudity ceiling.
  - **Konami graffiti:** it was a typo. It now reads "Up Up Down Down Left Right Left Right B A (for love)".
  - **Game menu:** approved as proposed (scratchpad menu_proposal.md), with nine sections: Items, Equip, Status, Party, Wallet, Brewery Passport, Quest Log, Settings, Load / Quit. The root has the bros' cards and a SOVS + watch box. The clock is paused while the menu is open.
    - No Save in the menu; saving happens at hotspots and beds, plus autosave.
    - **SP is Bravado everywhere.** Drinks that say "+SP" restore Bravado.
    - Equipment slots follow the equipment template's full list: weapon, head, torso, legs, feet, necklace, ring, watch/bracelet, phone, accessory, plus combo sets.
    - The intoxication tier shows on each bro's card on the root screen. Author: "and it's obvious in how red their face gets lol".
    - The proposal's defaults are approved:
      - the watch sits in the shared SOVS box and can't be unequipped;
      - skills are read-only in Status;
      - no Achievements section, no Street Rep display, no ICQ log and no map;
      - section labels are plain;
      - Esc or Start opens the menu.
- **(Round v37, 2026-11-11) Taproom v3, graffiti decal, drink tag.**
  - **Taproom art v3: changes.** Author: "The recirculator should be up against the bottle. The very end should loop past the bottle lid and turn back and go into the lid so it completes the loop. The chairs should be in front of the recirculator, not behind it." Version 4 to follow.
  - **"Pixelated boobs" graffiti decal approved:** crude pink pixel doodle, uncensored (`scratchpad art/v35/aa_closet_decal_pixel_graffiti.png`; to be copied to Assets with the closet).
  - **Drink tag:** every alcoholic drink and beer (signature beers, shots, absinthe and so on) counts as "a drink" for the clock's 10 minutes. Food, drugs and vapes don't.
  - The closet re-frame (v3) was pulled before review: still too close per eurobound-5d's measurements. v4 is being pre-checked.
- **(Round v38, 2026-11-11) Closet v5 approved, Taproom v4 changes, Bravado clean-up.**
  - **Closet art v5 approved** (`concepts/aa_interior_maintenance_closet_v5_night.png`; ChatGPT-zoomed-out, with the canon text patched back in). The bros walk in the back ~55% of the floor, and the approved graffiti decal goes on the left wall between the door and the "He moaned" line.
  - **Taproom art v4: changes.** Author: "the problem now is with the bottle fully intact, it is too tall for a bartender to even work *at* the bar." Version 5 to follow.
  - **Bravado clean-up (bead Eurobound-5i3):**
    - e3_bravado_cells: merge each "+N Bravado | +Bravado temporarily" pair into one Bravado effect.
    - e3_sp_key: rename `sp_restore` to `heal_bravado` now.
    - e3_template_note: rewrite the ability template's SP notes for Bravado.
- **(Round v39, 2026-11-12) Taproom v5 approved; Casa Rose Heineken.**
  - **Taproom art v5 approved** (`concepts/aa_interior_taproom_v5_night.png`): the giant bottle is half-sunk, with a counter at working height and a bartender walkway behind it; the neon recirculating pipe hugs the bottle and loops back in through the cork; the stools stand in front.
  - **e3_heineken (bead Eurobound-5i3):** Casa Rose Erotic Theater's Heineken row becomes **+0 Bravado**, and the joke ("everyone knows you're stalling") stays.
- **(Round v40, 2026-11-12)**
  - Jakub's restroom scene is approved (Writers' Room desk, 2026-11-12: "Approve with your fix"; "In America" → "Back home"). The canon text is `WritingRoom/tasks/20261111_1412_jakub_restroom_scene/final.md`, linked from `jakub_tokens_dvorak.md` in place of the proposed beats.
  - Jakub's pose in that scene (author: option A): a new pose of him lying sideways across the Green Fairy's arms, as the script stages it, replacing the sitting pose at her feet.
- **(Bead page, 2026-11-12, relayed by eurobound-bb)**
  - Eurobound-pj5: the Rival Trio appears exactly once, at the Craic Tax showdown awarding Pogs; the Debaucheryville and Sinfonia showdowns stay dead (author: "Confirmed as stated").
  - Deferred by the author: Steam price, DLC and macOS until closer to launch (p22); the five stub general quests until the duplicate quest docs are resolved (apz); the next NPC sprites until the bros and Arcade NPC sprites are done (qt5).
- **(Round v41–v42, 2026-11-12, Arcade scope for the Absinthe Orchestrator)**
  - Jakub's lying pose is approved: "The pose is right." It still needs an Aseprite clean-up: stray white pixels, and a face that reads as a face.
  - **Taproom:** build the .md version: Dr. Vaněk, the opener checks, the 5-section mirror maze, Mirror Chad, the optional Wisp, the Absinthe Lager (12 SOVS) and the stamp. **"The opener must be earned, cannot be bought."** Each new number or line goes back to the author first.
  - **Closet:** build the DDR-arrow toilet, CRT mirror, sock prize chute, sparking wiring, readable blacklight graffiti and the 30-second shame timer now. The Embarrassed-only sticker and the ICQ SMAAAASH prompt (SMAAAASH prompt superseded: struck by author, Eurobound-ywe) wait for those systems.
  - **Mirror corridor shadow-switch puzzle:** yes.
  - **Backpack Girl Who Never Left:** yes. Her interaction gets reviewed against canon first. Author's standing rule for Couchsurfing Chronicles girls: one girl means one bro sleeps with her, and it is never polite, good sex. The bros are doofuses and wake up to hilarious and/or horrifying results: robbed, she's gone, an STD, beaten up for sleeping with someone's girl.
  - **Ambient hall groups** (hackers, EDM ghosts, rogue backpackers, bathroom speedrunners): yes, as real sprites, never painted into the background.
  - **Extras:** all of them: the first-entry cinematic, fake VIP arrows, the bidet stool chime, the examinable exterior bits and the club-flyer panel.
  - **Arcade Employee leftovers:** Jakub gets "you actually won that"; the Microsoft Publisher flyer line is dropped.
  - **Systems:** all, in this order: field status effects, Quest Log, Brewery Passport and openers, ICQ hotspot popups, NFT Legacy Vault. Each system's numbers go to the author.
  - **Sea-Monkeys:** Mint #73 stays. The author will write the card copy after seeing what canon has.
  - **Open (author's notes):** whether interactable props need their own assets instead of being painted into the plates, and what the hidden-item containers are (chests, time capsules or geocaches) for the Arcade, Taproom and both restrooms.
- **(Round v43, 2026-11-12, submitted 19:58Z; verbatim answers in the decisions session's scratchpad `ans43/round_v43_answers_verbatim.md`, relayed to the Absinthe Orchestrator)**
  - Jakub's cleaned cradled pose is rejected: "This needs redone. He looks pretty awful."
  - **Quest Log:** losing the Grandpa Provides fight gets its own outcome, and "Accounts Recievable should steal the money that should've been paid for the tab if the bros lose."
  - **Field statuses:**
    - Field statuses carry into battle.
    - Green Fairy Confusion reverses movement and scrambles dialogue choices, and lasts a random 30 s to 3 min.
    - The field version of Embarrassed is proposed by a designer for review.
    - Saw Yourself and Existentially Rested affect only the bro who triggers them.
    - Reality Anchor gives a 10% chance to block Confusion.
  - **ICQ:**
    - Hamstradamus is allowed: "He also shows up in the flesh at times... He never travels with the party... He operates like an NPC."
    - The two example pop-up lines are approved.
    - The Arcade's FREE Wi-Fi hotspot is the street cabinet outside the facade.
  - **Mirror corridor:** the switch order is 3 → 1 → 2.
  - **Interactables:** state-changing props get their own assets, plus the token machine, prize counter, bar and the playable cabinets ("might be interacted with so should be assets").
  - **Taproom numbers:** Mirror Chad and Wisp numbers are proposed by a designer from the approved battle numbers, for the author's review.
  - **Hidden items:** both time capsules (indoors) and geocaches (outdoors).
  - **Brewery Passport:**
    - The keychain and passport book show in both the Items list and the Passport section.
    - Signature beers can be bought only after earning that brewery's opener/stamp.
    - The tour trigger is built with Publandia.
    - "you have to have the keychain from the blarney trap to collect any opener. none can be gotten without it."
    - Keychain passives: "gather all info on what should go into the system then draft it up for my approval."
  - **Author-written copy (canon, written into the item docs):** Sea-Monkeys (Mint #73), "She Thinks My Tractor's Sexy" (Mint #42), the Bottle Opener Keychain and the Brewery Passport Book. Flags put to the author: real place names in the copy, and "twelve" openers vs canon 16.
  - **NFTs:** item files to be created for the replacement NFTs that lack one (template fields plus canon info; the author writes the rest), plus a list of the Lane-copy fields and America Online's template needs, for the author to draft.
  - **PixelLab:** the author asked "How close can we get using scenario or ludo.ai? Can we generate in chatgpt and then use the references to develop in aseprite?" (being tested).
  - **Approved in the author's v43 resubmit (20:04Z):** the Taproom mirror-maze rooms M1 v2 and M5 v2 (`concepts/aa_interior_taproom_maze_m1_v2_night.png`, `..._m5_v2_night.png`); the five maze mirrors (`references/Interior/props/taproom_mirrors/`; True has a clean gold frame, the other four tarnished brass); and Dr. Vaněk's model sheet (`npcs/absinthium_taproom/model_sheets/dr_milos_vanek_model_sheet.png`). Author: "firefly DOES have 2.6. You have to access it from the main firefly screen."
- **(Production Desk Eurobound-sue-q1, 2026-11-12) Intoxicant fields for `consumables.json`: "Approve as proposed".**
  - The field shape in `docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md` §2 is approved unchanged: optional `subtype`, `usable_in`, `max_stack`, `price {coin, amount}`, `bundles [{qty, amount}]`, and `intoxicant {status, duration {battle_turns, field_steps, ends_on_rest}, stack_rule, then {status, stacks}}`. The four required fields stay; `alcohol: true` stays separate.
  - Unruled values are `null` with a `_pending` note citing the item-doc line; numbers still belong to the balancing pass. Applied to `strawberry_shortcake_speedcakes` and `mango_og_gushers`, checked by `Tools/validate_data.py` (bead Eurobound-sue). BattleCore support is bead Eurobound-umy; status behaviour is bead Eurobound-1m4.
- **(Round v44, 2026-11-12, submitted 20:49Z; verbatim in the decisions session's scratchpad `ans44/answers/latest.json`; relayed to the Absinthe Orchestrator)**
  - **Taproom fights:**
    - Mirror Chad is in: later rulings supersede the early "killed" line.
    - Mirror Chad fights "Words Only": 54 HP, social attacks, and he Confuses you if not beaten in 3 turns.
    - Green Fairy Wisp: **72 HP**.
    - Rewards: 12 SOVS for Mirror Chad and 25 for the Wisp, no tickets.
    - The Wisp leaves after round 6 (surviving counts), with no tell for the real Wisp in phase 2.
    - The Absinthe Lager is confirmed at 12 SOVS.
    - Source: `docs/superpowers/proposals/2026-11-12-v43-design-proposals.md`.
  - **Embarrassed in the field:**
    - Lasts 60 game-minutes, and carries into battle for 2 turns.
    - Sources: the shame timer, a failed QTE and the hostel witness.
    - Resistance makes it 10% shorter per point.
  - **Keychain:**
    - Tier B "Credentials": it gates opener collection.
    - Bartender discount of 5% per completed city, max 20%.
    - Party Prep = +1 Bravado per completed city at battle start.
    - **16 openers / 16 breweries.**
    - The registry may record these.
  - **Build questions:**
    - On a Grandpa Provides loss, Accounts Receivable takes 50 SOVS (tab + service charge). The Writers' Room writes the loss line and the "tab stolen" objective.
    - Reality Anchor is party-wide.
    - Field Confusion lasts 2 turns in battle.
    - Saw Yourself and Existentially Rested stay outside battle.
  - **Vaněk's opener-check lines:** keep line 2 without the "paid for the privilege" clause; the Writers' Room writes a new line 1.
  - **Mirror maze:**
    - It sits between the curtain and the Taproom.
    - The last room's open arch counts as the True exit (4 niches: Truth + 2 Portal + 1 Trap).
    - Fixed vs shuffled layouts: the author asked for pros and cons first.
  - **Writers' Room order:** the Arcade completion lines go before Backpack Girl (both wait on the OpenRouter top-up).
  - **Art:**
    - Approved: the four ambient crowd lineups and the Taproom battle backdrop.
    - Jakub's cradled v5 needs "seriouse rework". The author asked for an adversarial ChatGPT creative-director review, a rebuild to its standard, then a showing.
  - **Jiří's hat:** a faded tram-conductor cap (he's not staff).
  - **PixelLab:** no pick. "Research other options. We went through 2000 credits... Any aseprite extensions or other ideas that might work? Cant you generate a pixelart maker that is good and effective?"
  - **Copy fixes (author):** "1 keep canon 16 2 add shamsterdam 3 Maastricht Treaty change it 'kentucky pasture' horse country europe euromemeia".
    - Applied to the round v43 author copy in the item docs.
    - The Maastricht Treaty replacement is still open.
    - Items 4-8 weren't addressed, so that copy stands.
  - **NFT copy:** the author wants to go through it one card at a time.
- **(Bead page, Eurobound-ywe, 2026-11-12) ICQ-to-Rival-Trio messaging: "Strike all ICQ-to-Rival-Trio messaging".**
  - The bros never ICQ or message the Rival Trio. The Embarrassed / Cringe Lock debuffs that came from those sends are struck. The Trio still appears once, at the Publandia Craic Tax showdown (Eurobound-pj5). Applied in design docs and engine data under Eurobound-ywe / Eurobound-7fp (c9c6002e).
  - Supersedes the "ICQ SMAAAASH prompt" half of the Round v41-v42 Closet line (that prompt was the send-to-Rival-Trio prompt); the Embarrassed-only sticker half is unaffected.
- **(Bead page, Eurobound-0q4x, 2026-11-12) Enemy docs folder: "design/worlds/<city>/enemies/ (the template proposal)".** Regular enemy docs (from `design/templates/enemy_template.md`) live in `design/worlds/<city>/enemies/<enemy_name>.md`, dungeon enemies included.
- **(Bead page, Eurobound-8gg, 2026-11-12) Windmill Grist: "Grist stays not sold: the opener gates only the stamp; sweep the purchase lines".** Windmill Grist is never sold (round v34); the Wobbly Windmill opener gates only the stamp. Purchase lines swept (282596b1).
- **(Eurobound Desk, round v45 cards, answered ~21:38Z 2026-11-12; relayed by the Absinthe Orchestrator)**
  - Jakub's cradled V6 is rejected: "Awful... This is the worst version yet." The game keeps v3.
  - **Sprite route:** "Try the blender option as a trial. Let's use Jakub... Find his original reference image and generate him with blender/tripo so I can see how that goes." (3D trial in progress)
  - **NPC scope:** named and story NPCs walk in 8 directions; the background crowd only stands and idles.
  - **NPC sheets approved:** the model sheets for Blanka, Bobo "The Blockchain" Bitsworth, the Clock Wine Vendor, the Commemorative Merchandise Vendor, CryptoBro69's "Ex", Dmitri "The Router", Hamstradamus, Janek Sýkora and Jaxson Vane (`Assets/Graphics/sprites/characters/npcs/debaucheryville/<id>/`).
  - **Passport copy (author's wording):** "Maastricht Treaty" becomes "Treaty of Tepid Compromise", and "European integration" becomes "Euromemeian integration".
  - **Millennium Bug:** the author wrote the full card copy (Mint #00 confirmed); it is being written into `design/items/millennium_bug_nft_item.md`.
- **(Eurobound Desk, 2026-11-12) Quest flags (Eurobound-vyn-q1, "Approve as proposed") and PNG specs (bead page, Eurobound-x0c).** Quest flags live in `game/assets/data/world_data/quest_flags.json` on the approved schema (docs/superpowers/specs/2026-11-12-quest-flag-schema-proposal.md), checked at tier 2 by Tools/validate_data.py (458132a6). Each Debaucheryville location has ONE PNG spec of record: the HD-2D `<Location>_Complete_PNG_Asset_Requirements.md`, with the older sprite-sheet spec folded beneath it as detail (822deceb).
- **(Eurobound Desk p1y-q2, 2026-11-12) The Golden Cutlet roster: "Approve all as drafted".** The 8 enemies live in `design/worlds/sinfonia/enemies/` and the Schnitzel King fight in `the_schnitzel_king.md` (6bfd8788); numbers PENDING the balancing pass; the defeat payoff is desk p1y-q3.
- **(Eurobound Desk eb8-q1, 2026-11-12) Grist + Genever review numbers: "Approve as proposed".** Values in docs/superpowers/specs/2026-11-12-grist-genever-review-numbers-proposal.md (1 battle turn = 40 overworld steps; The Shakes 95%->80% hit; Grist Navigation 200 steps, floor 10%) are canon and written into both drink docs. The drinks keep their names until the Writers Room rename (Eurobound-jsc).
- **(Eurobound Desk 1m4-q1, 2026-11-12) Status-effect data shape: "Approve as proposed".** Sugar Rush Hour, Gush-Locked, Crash and Cottonmouth live in `game/assets/data/skills/status_effects.json` on the approved shape (docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md, incl. the §5 two-counter rule); numbers null pending the balancing pass. Schnitzel King payoff (p1y-q3): a thimble-sized heritage measure, refilled without limit.
- **(Applied 2026-11-12, Eurobound-vh89) Openers are earned, never sold.** The Wobbly Windmill opener comes only from the Yeast Golem defeat and needs the Blarney Trap keychain (rulings 2026-08-04 and round v43); the 22 SOVS sale is removed. Eight other breweries still sell theirs: Eurobound-7env.
- **(Eurobound Desk qyxm-q1, 2026-11-12) "Text on screen" caption cards: "Not allowed: remove them all and quote them for me".** Closing caption cards that deliver the joke (with their THE PUNCHLINE headers) are a narrator substitute and are banned; all 17 removed and quoted for the author. Whether title cards / "Nobody said it out loud." captions are covered: Eurobound-meu5.
- **(Eurobound Desk h7h9-q1, 2026-11-12) NFTs never have an effect: "No effect (effect: null), like Sea-Monkeys" / "NFTs never have an effect".** Standing rule for every NFT: no stats, no inventory effect (effect: null). Applies to The Millennium Bug and removes the Tractor NFT's Bravado/Charm lines.
- **(Author ruling, 2026-11-12, said directly in chat to the Absinthe Orchestrator; relayed verbatim)** **Characters move to the Tripo/Blender 3D route, the bros included.** "WOW. LOOOOVE this version of Jakub from tripo/blender... I think I'd rather we actually do this with all characters including the bros. It just looks so much better than the crap trash we've been producing with pixel art."
  - This supersedes the Firefly → PixelLab → Aseprite pipeline in `design/style_guides/character_sprite_pipeline.md`, which has been rewritten around the 3D route.
  - The trial on Jakub: Tripo image-to-3D (55 credits) + mesh simplification (35) + humanoid auto-rig (20), then a Blender pose and toon render (`scratchpad art/v47`).
  - Open, on the Eurobound Desk (window "Sprite Development Team"): final look (pixel sprite vs higher-res render, `sprite-dev-3d-look`), redoing existing sprites (`-redo`), credit budget (`-budget`), animation scope (`-anim`), order (`-order`), and swapping in the trial Jakub (`sprite-dev-jakub-3d-approve`).
- **(Bead page, 2026-11-12) Quest flag ids.** Eurobound-9jza: "One bool per NPC (a flag_patterns family); routing lists use the Chronicles flag": `chronicles_entry_completed_{npc_id}` / `encounter_scene_completed_{npc_id}`; the Arcade's backpack_girl_couchsurf_completed is the Chronicles flag for her. Eurobound-tzbu: generic quest-JSON flag ids are renamed to `<city>.<venue>.<event>` (157d1eef).
- **(Bead page, Eurobound-b5jo, 2026-11-12) Publandia street name: "Doner Lane".** Publandia's Kebab Alley (Seedy Underbelly / After-Hours Chaos Street) is now Doner Lane; Debaucheryville keeps "Kebab Alley" (eaiq-q4). Author's pick for any future Shamsterdam or Sinfonia döner place: "The Skewer Mile" (reserved, not yet used).
- **(Eurobound Desk bp4i-q1, 2026-11-12) Wallet and airdrop flags: "Do the recommendation: drop sovs_balance, add the two airdrop flags".** The SOVS balance lives in GameState.sovs and is not a quest flag; airdrops_delivered and bagholder_assets are flags (economy_system.md §8.2, quest_flags.json).
- **(Eurobound Desk, 2026-11-12, 3D character route)**
  - Look: clean higher-res 3D renders with no pixelation, sized to sit in the painted rooms. Convention chosen: 300 px/m.
  - Redo everyone in 3D, bros included.
  - Budget: "Do everyone; I'll top up Tripo when needed".
  - Animation: walkers get 8-direction idle + walk; the crowd gets idle only, front-facing.
  - Jakub's cradled pose: "His arm needs redesigned as it is anatomically inaccurate. His midsection also needs addressed as it's tiny like a Barbie doll."
  - Still open: the order, the Jakub swap, and the Tripo API key.
- **(Eurobound Desk 2w7l-q1, 2026-11-12) Heritage Pass Route B scan timing and duplicates: "Scannable only after the Heritage Trial / the King is beaten; if already owned, the scan does nothing new".** The Pass fine-print QR cannot be scanned until the Schnitzel King is beaten; if the bros already hold Holographic Charizard, the scan grants nothing new (one collection target, counted once). Recorded in holographic_charizard_nft_item.md (Route B) and nfthuntsinfonia.md target 1; quest-doc staging waits on Eurobound-mmix.
- **(Eurobound Desk r8l8-q1, 2026-11-12) Flag write shape: "Approve".** Every flag write in design data uses `"set_flags": {"<flag id>": <value>}`; effect-list and timeline entries keep their own discriminator and carry the same object; an item's write on pickup is `"set_flags_on_acquire"`. Retired keys: set_flag, sets_flag, sets_flags, flag_set, sets_state, quest_flags_on_acquire. Templates updated; migration and validator enforcement: Eurobound-ojwi. Spec: docs/superpowers/specs/2026-11-12-flag-write-shape-proposal.md.
- **(Eurobound Desk 76gz-q1, 2026-11-12) Shamsterdam Navigation base odds: "Approve as proposed".** Base correct-exit chance is the sign table's correct row (40% "Centraal Station", 50% "Museum Plein"); wrong exits share the rest in listed proportions (largest remainder, ties to the higher row). Order: base + additive modifiers, clamp 10-90% (eb8), roll. The +5 per earlier success counts within the current tunnel visit and resets on leaving; Voetgangerstunnel roll only; the final chance shows at intersections only with a map item equipped. Recorded in voetgangerstunnel.md; engine work Eurobound-eggq.
- **(Eurobound Desk c24-q3, 2026-11-12) Canal Courage effects: "Approve as proposed".** Unlocks with all 4 Shamsterdam stamps: +20 ALL stats and -25% Bravado loss for the whole battle, then "Canal Courage Hungover" (working name): -15 all stats and Canal Confusion (-25% Navigation) for 45 minutes with the Tunnel Confusion question marks; cured by any herring at De Zilte Waarheid, sleep, or waiting it out. 75 SOVS, repurchasable at any stamped Shamsterdam location, one instance at a time; proposal §4 interactions stand. Status name, social gag and flavor text open (Eurobound-3mqo); units/scale follow Eurobound-picf. Recorded in brewerytour.md and brewery_passport_book_item.md.
- **(Eurobound Desk u1m-q1, 2026-11-12) Economy build order: "Approve the order as proposed".** Order 0, 1, 3a, 3b, 3c, 5, then 2, 4, 6 per docs/superpowers/specs/2026-11-12-economy-build-order-proposal.md (cd2b9973). Implementation beads, chained: jvwg, it49, fxon, 22n3, li0t, ou0t, ml5r, wgso, nm8y. Prices and stock stay author-owned.
- **(Eurobound Desk rcj-q1..q7, 2026-11-12) Arcade interior 3D manifest, sections A-G: "Build the missing ones" (each section).** Painted ids stay painted (superseded); missing ids and missing state sets get built, owned by the Asset Development Team (beads sjoc, lyvh, koq3, w2ig, objf, 1av7, 4nx3, zx7u). Section A has nothing missing. Recorded in absinthearcade_interior_3d_asset_manifest.md.

## Standing ruling 2026-11-13: no Dutch names in Shamsterdam (author)

- Author, in chat: "I want all dutch names from shamsterdam rethought. I don't know where they came from but I never asked for dutch names. They should be americanized, satirical, parody type names that are whitty, clever, and lean hard into what each place is. They're supposed to be funny. Not highbrow"
- Author, on the Eurobound Desk (De Wachtrij plan note): "We do not use official looking names in dutch. We use american names and they should be whitty, clever, satirical, parody type names that are fully americanized and lean heavily into what each location is".
- Applies to every invented Shamsterdam name (places, districts, NPCs, items, events, signage). Real brands and products keep their real names (2026-11-09 ruling). Existing Dutch names are being replaced; the author picks each new name on the Desk (bead Eurobound-ucpf). Never mint a new Dutch-language name.

- **Tripo API ruled out (author, 2026-11-13, chat, relayed by the Asset Development Team):** "Then no. We may not use the Tripo API. I am NOT buying a subscription AND paying API credits. Furthermore, I do not like paying API costs." All Tripo work uses the website on the existing subscription credits. `tools/char3d/tripo_client.py` is marked DO NOT USE; never propose paid APIs as an alternative. Lord Pilsner's 3D look-B passed the 1:1 hall check the same day and is live (f573bbdc).

- **Chadwick and Bradley 3D source art (author, 2026-11-13 11:07, Desk `sprite-dev-chad-brad-source`):** "go to chatgpt. Show it the artwork of pilsner and then of chadwick or bradley and have it generate similar styled work using gpt image 2.6 sunburst high". So: a painted front view of each, matching Pilsner's original painting, is shown on the Desk before any Tripo (website) build. For this job this overrides the earlier "Stay on Firefly only"; if ChatGPT can't generate, use GPT Image 2.6 from the main Firefly screen.

- **(Eurobound Desk vt7k-q2, 2026-11-13) Contact High and Space Cake Gamble: "Approve as proposed".** docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md is canon as written: Contact High (De Groene Gids interior + 30 clock min, 30% on the Coffeeshop Quarter exit, couchsurf payoff; party, field, refresh, 30 min, -15 Navigation only); Space Cake Timer 120 min then +40 Bravado and Space Cake Gamble 90 min per cake (cap 180), 15 s onset wobble, rest clears an unlanded timer; teleport on a wrong tunnel roll 50%, uniform over the 6 non-correct exits, counts as a wrong turn, +30 clock min. Engine: Eurobound-2xah.

- **(Eurobound Desk ucpf-q44/q45/q48/q49, 2026-11-13) Shamsterdam's author-kept Dutch names: the only three exceptions to the no-Dutch-names ruling.** De Pauze (Roodelicht Zone 2; q45 "Keep De Pauze (one-off, like Frietomat)"; Frietomat itself became Fritomat, q44), Meester Overhang (q48 note: "Meester Overhang can stay. This and Opa Cees aren't hard to understand so are fine"), Opa Cees and his buff (q49: "Opa Cees can stay"). Locals' Dutch first names also stay (q42). Full map: WritingRoom/tasks/shamsterdam_rename_final_map.md (bead Eurobound-ucpf).

- **(Eurobound Desk n7w5-q11, 2026-11-13) Lord Pilsner's real name is Phillip ("Phil"): "Yes, Phillip/Phil; Philosophy Phil stays (exempt)".** Author note, verbatim: "Yes and it's only used in places where a parent might normally scold a child by using their full name or first and middle name". So the name is never neutral address; it only appears in scolding moments (e.g. Chadwick's "Phil." in the WOBBLE PILSNER morning after, design/quests/publandia/wet_tshirt_contest.md). Philosophy Phil (hostel_midnight_checkout.md:280) keeps his name as a uniqueness exemption.
- **(Author, chat, 2026-11-14; Eurobound-nhxz) SAM paint zones trial: "Let's trial it on Chadwick then we will decide if I hand texture still or not".** The paint-zones route (SAM zone tracing, Claude paints by zone) is trialled on Chadwick only. 3d_asset_rules.md:33-34 (author hand-paints distress; base textures come from the author) stay in force for everything else until the author decides after seeing the trial.
- **(Bead page, Eurobound-cyb6, 2026-11-13) bagholder_assets shape: "Dictionary: coin_id -> quantity held (current proposal)".** The non-SOVS coin store is a dictionary of coin_id to quantity, default {}. Built on GameState in Eurobound-1g9t (deposit_coin, bagholder_assets, coin_quantity).
- **(Bead page, Eurobound-2ntt, 2026-11-13) Junk is an Item Type: "Add 'Junk' to the permanent template's Item Type".** permanent_item_template.md lists Permanent Cosmetic / Hybrid / Curse Item / Quest Item / Junk; junk items stay on the permanent template; the 10 Golden Cutlet junk docs carry Item Type: Junk.
- **(Bead page, Eurobound-9rj1, 2026-11-13) Golden Cutlet trap-door junk names: "Keep the working labels".** Final names: Bachelor Party VIP Lanyard, Half a Pair of Lederhosen, Bachelor Party Disposable. Ids and filenames unchanged.
- **(Bead page, Eurobound-e4bh, 2026-11-13) Club Flyers / Brewery Tour old and canon lines: "Both apply: the old lines are extra rewards/flavor on top of canon".** The old Location Specific lines added beside canon (nda-q7) in club_flyers.md and brewerytourdebaucheryville.md all ship as extras on top of canon; neither set replaces the other. Open: Path A Bravado +2 vs +1 (Eurobound Desk e4bh-q1).
- **(Bead page, Eurobound-gpfc, 2026-11-13) Underground Navigator trigger: "After 5 successful navigations (Buffs Earned, :459)".** Earned on the fifth successful navigation (lifetime count), not the first. voetgangerstunnel.md and game/core/navigation_roll.gd updated.
- **(Bead page, Eurobound-6dx6, 2026-11-13) Marloes's Blessing on the Navigation roll: "Yes: +20 on the roll for the rest of that tunnel visit".** Trigger stays as canon (buy the map AND follow her advice); cleared on leaving the tunnel. What "follow her advice" means is unruled (Eurobound-sj0s).
- **(Eurobound Desk 64vo-q1..q8, 2026-11-13) Status-behaviour rulings (spec 2026-11-12-status-effect-data-shape-proposal.md §8), verbatim:** q1 "all stats": "The six combat stats: offense, defense, speed, charm, luck, grit". q2 Crash outside battle: "Battle only: Crash waits for the next fight and runs its turns there". q3 stacks: "Stacks last longer: more Crash turns per stack; one drink per Cottonmouth stack". q4 doubled thirst: "Double the stacks: Cottonmouth arrives with twice as many stacks". q5 spoken abilities: "Tag each ability spoken or not, one by one as abilities are written (Roast Line first)". q6 hidden Hungover timer: "Pause: the timer stops while hidden and picks up again when it returns". q7 after the cancel: "Both still hit, right after the cancel". q8 Cottonmouth cure: "Any drink at all: water, soda, beer, liquor". No answer sets a number. Open engine work: Eurobound-qiof, 2uji, rry7, uwrw.
- **(Author, chat, 2026-11-14; Eurobound-nhxz) Reference-Locked 3D Texturing Protocol: "Here is the new workflow for all agents working to generate sprites and assets."** Binding text in design/style_guides/reference_locked_texturing_protocol.md: approved art is the source of truth; SAM segments materials; GPT Image 2.6 makes material studies; Tripo + Blender build and project reference pixels; Modddif repairs; ArmorPaint finishes PBR; a SAM-assisted review marks each asset APPROVED / REVISION REQUIRED / BLOCKED; approved materials go in a shared library. Rollout: "test this on one existing character and one Absinthe Arcade architectural asset before applying it everywhere" (character = Chadwick). Open on the Desk: Tripo v3.5 API vs the 2026-11-13 Tripo API ban (nhxz-q2); paid tools (nhxz-q3).
- **(Author, chat, 2026-11-14; Eurobound-31uj) Location interactables rule: "And rules for interactable items within locations."** Binding text in design/style_guides/location_interactables_rule.md: every visible thing is baked background, placed prop, interactive object or pickup; anything game logic could refer to is a separate asset declared in the location files; every location gets a scene decomposition list and an asset requirement list. Open on the Desk (31uj-q1): whether approved plates such as the Arcade are reworked or only new locations follow it.
- **(Author, chat, 2026-11-14; closes Eurobound Desk nhxz-q2) Tripo API stays banned: "We are not using the tripo api."** The Reference-Locked Texturing Protocol uses Tripo through its website only; the tripo-mcp generate tools are not to be called (Eurobound-dkoq).
- **(2026-11-14) Absinthe Arcade is reworked to the location interactables rule.** Author, on Desk `Eurobound-31uj-q1`: "Looks like we will need to do the rework." The approved Arcade plates no longer stay as painted plates with interaction points: the items the audit found painted in or missing (`docs/superpowers/reports/2026-11-14-arcade-interactables-audit.md`: 25 painted-in, 8 missing) become separate assets declared in the location files. Rule: `design/style_guides/location_interactables_rule.md`. Work: `Eurobound-31uj`.
- **(2026-11-14) Blind QC covers every type of asset and sprite.** Author: "be sure ALL types of assets/sprites are being reviewed by our blind agents". No asset type ships on self-review: characters, enemies, NPCs, portraits, building plates, 3D kits, props, interactables, pickups, item icons, NFT art, UI and VFX all pass a blind reviewer gate (`Tools/char3d/QC.md`, the asset team QC gate). Work: `Eurobound-2boh`.
- **(author, 2026-11-12, round v45, Desk question `v45-party_prep_on` "Turn on Party Prep?"):** The author chose "Leave it off" (note: none). Party Prep stays switched off. The v44 value stands as ruled and is kept, not changed: +1 Bravado per completed city at battle start. Engine matches (`PARTY_PREP_ENABLED` false; `bottle_opener_keychain.party_prep` `enabled:false`). Tier B "Credentials" and the 5% per completed city (max 20%) bartender discount are unaffected. Beads Eurobound-3988, Eurobound-pvf0.

## Resolved (moved 2026-11-11 by Eurobound-j50)

Moved verbatim from the work-tracking sections above; evidence appended to each.

**From “CRITICAL WARNINGS FOR THE REORG WINDOW”:**

1. **~240 UNCOMMITTED draft files under `Design/` carry four rounds of disk-only cleanup**
   (complete named-hippo eradication — 218 sites; ~330 world-name fixes; JSON repairs; the hippo
   de-petting). They are UNTRACKED — any `git clean`, fresh checkout, or careless delete
   destroys that work permanently. **STRONGLY RECOMMENDED: snapshot-commit everything
   (including untracked files) to a branch or archive BEFORE moving anything.** — resolved: the reorg window closed when `chore/folder-restructure` merged into main (2003ee3, 2026-08-04); `git status` now shows 12 untracked files under `design/` and 1238 tracked

**From “RESTRUCTURE RESUME CHECKLIST”:**

1. **Clean the tree first.** `git status --porcelain | wc -l` must be 0 before merging. Commit
   in-flight sweep work to the branch (never stash-and-forget, never `git clean` — see warning 1). — resolved: main was merged into `chore/folder-restructure` (f1edb57) and the branch merged into main (2003ee3, 2026-08-04)

2. **Merge main in, main wins content conflicts:**
   `git -c merge.renameLimit=15000 merge main -X theirs`
   (run ON `chore/folder-restructure`). `-X theirs` makes main's side win any conflicting hunks;
   rename detection maps main's edits onto files the restructure moved — the raised renameLimit
   is required because the restructure renamed ~800 paths. After the merge, if anything under
   `game/` changed: run BOOT + GUT (commands in
   `docs/superpowers/plans/2026-07-31-folder-restructure.md`, Global Constraints) and match the
   27/27 baseline before proceeding. — resolved: main was merged into `chore/folder-restructure` (f1edb57) and the branch merged into main (2003ee3, 2026-08-04)

**From “Open author decisions”:**

- **Brands round:** whether real brands in player-facing text (Guinness incl. "GUINNESS
  SUPPOSITORIES", Four Loko, Winamp, Hot Topic, Habbo, Oakleys, Kinko's, Advil, Uber, Muscle
  Milk) stay (Y2K authenticity, trademark exposure), get parody-renamed (safe + new jokes), or
  mixed (keep neutral mentions, parody vice-context uses). Author to rule; then one sweep round.
  **RESOLVED 2026-11-09 (author): real names stay.** "The only thing that never gets the real
  name is locations. ALL other things get their real names." No sweep needed for the brands
  listed; any existing parody-renamed brand should go back to its real name. Breweries,
  bars and other venues are locations and keep parody names.
  **Pre-ruled 2026-08-04:** Party Monk's HOLIDAY INN EXPRESS bathrobe easter egg — KEEP (author
  ruling; do not relitigate in the brands sweep). — resolved: author ruling 2026-11-09 recorded in `.claude/CLAUDE.md` ("Real brands ... keep their real names"); whether any parody-renamed brand was reverted is unverified

- ~~**Publandia's 4th NFT slot** — sanctioned open slot in `fratbronft.md`, awaiting the author's
  idea.~~ **RESOLVED: filled by America Online** (jukebox track 47, The Craic Tax; `fratbronft.md`, `legacy_vault_cards.md` Card 12). — resolved: 49f8345 ("NFT #4 America Online"); `design/Quests/general_quests/fratbronft.md` line 68

**From “DEFERRED quest-doc debt”:**

**3. `mobile_optimization` blocks — 28 files, two different problems.** Dead-branch
mobile-first residue (`claude/eurobound-jrpg-prd-uv5iog`) on a Steam/desktop target.

- **In the two quest JSONs: misnamed, not obsolete.** Contents are `screenshot_moments`,
  `dialogue_pacing`, `cutscene_skippable`, `comedy_timing: "silence_after_is_the_joke"` —
  all needed on desktop, and the comedy timing is load-bearing. Rename to `presentation`;
  drop nothing. The new sync skill already writes `presentation` for new quests.
- **In ~26 `design/worlds/*/core/` and `*/sprite_mapping/` files: real debris.** Spot-checked
  three — `cafe_sachertorte_core.json` and `voetgangerstunnel_core.json` carry `lod_level`,
  `max_particles`, `draw_calls`, `memory_mb`; `cloverleaf_sprite_mapping.json` carries
  `"compression": "PVRTC_iOS_ETC2_Android"`, an iOS texture format. These are mobile
  performance budgets and want re-budgeting for desktop, not renaming. Three of ~26 inspected;
  the rest assumed similar, unverified. — resolved: beads Eurobound-r1t (quest JSONs renamed to `presentation`, af3e4da) and Eurobound-trv (worlds JSON budgets) closed

**4. Two quest JSONs sit design-side.** `vip_wristbands.json` and `astronomical_cockup.json`
are colocated in `design/Quests/debaucheryville/` next to their `.md`. Ruled 2026-08-06: the
engine read path is `game/assets/data/quests/` (every populated sibling under
`game/assets/data/` is engine-side; only `economies/` and `quests/` are empty). Migrate them,
applying the canonical schema in the spec (`items_acquired` sub-keyed `standard`/`path_a`/
`path_b`; `localization`; `presentation`). — resolved: af3e4da, bead Eurobound-r1t closed; both now in `game/assets/data/quests/`, none left in `design/Quests/debaucheryville/` (follow-up open: Eurobound-9si)

## Author direction 2026-11-13: the story opening, step 1, plus a Writers' Room deep-dive (chat with the Absinthe Orchestrator)

Verbatim: "I think we need to have the Writing Room take a deep look into what this game is and what it's inspired by- earthbound, the inbetweeners, European vacation, road trip, wedding crashers, grand theft auto, fable and draft up what the game art for a 'cover' and a load screen should look like. I actually think we almost need to start with story... Pilsner finally receives his divorce papers. Bradley and Chadwick surprise Pilsner with a scheme to run off to Euromemeia (Europe) for a post-divorce trip to go and enjoy all of the scandalous, seedy things Debaucheryville, Sinfonia, Publandia and Shamsterdam have to offer. Pilsner leaves his gf behind and Chadwick and Bradley leave their wives behind. Pilsner is shown leaving his Mommy's house (where he's currently living) and his mommy gives him a hug and tells him 'mommy loves you. It's going to be okay sweetie. Make sure you call home and don't forget to take your blood pressure meds and put on a clean pair of socks every day (or some such ridiculousness that a nearly 40 year old man shouldn't have to hear from their mom lol) and he takes an uber to the airport where he meets up with his two former frat bros. Then it shows the plane taking off. Then they land in Debaucheryville and are shown leaving the airport and heading to the hotel. Then you nap and wake up ready to go out. But it needs to be written funny af. We will cover steps 2 and on after this."

- The beats above are the author's story (step 1 of the opening). The Writers' Room writes the comedy within these beats only; the author approves. Steps 2+ wait for the author.
- Canon touched: Pilsner is newly divorced (fits lordpilsner.md "Newly single" / "part of why they went to Euromemeia") and has a girlfriend; he lives at his Mommy's house; Chadwick and Bradley are married. "Uber" keeps its real brand name.
- RULED 2026-11-14 (Desk Eurobound-0z1r-q1), verbatim: "Keep Publandia first: the plane lands in Publandia instead". The opening lands in Publandia; city order stays Publandia → Debaucheryville → Sinfonia → Shamsterdam.

## Author rulings 2026-11-14: target audience, and why the art defaulted to cosy (Desk Eurobound-3ho-q6, Eurobound-vuqj-q1..q4)

- **Target audience (Eurobound-3ho-q6 note, verbatim):** "I have told it several times the game is for younger Gen X/xennial/millenial women". Recorded in .claude/CLAUDE.md. Every brief names this audience; the bros are the punchline.
- **vuqj-q1:** "Writers' Room rewrites the visual sections of every renamed real-venue doc before its building is painted". Root cause: docs/superpowers/reports/2026-11-14-generic-plates-root-cause.md.
- **vuqj-q2:** "Yes, add it to the template and backfill as docs are rewritten". Template: design/templates/location_validation_template.md, Visual Design → "What this building exaggerates (readable at thumbnail size)".
- **vuqj-q3:** "Palette sets the colours, but never candle-warm or golden-hour light; lighting is set per plan".
- **vuqj-q4:** "English plus pictograms (a hand with a red cross, a gear, a skull): every language, no words". This is for the Wobbly Windmill's five-language DO NOT TOUCH MACHINERY sign.

## Author rulings 2026-11-14: Bottoms Down names, Writers' Room fixes and art direction (Desk)

- **Eurobound-yhs6-q1:** "Keep Kees (a ledger exception, like Opa Cees)". Kees joins the no-Dutch-names exceptions (De Pauze, Meester Overhang, Opa Cees).
- **Eurobound-yhs6-q2:** "Keep Pim". Pim is also an exception.
- **Eurobound-3ho-q8:** "Apply all fixes (A-F)". These are the room-side fixes for clever, heroic bros: an audience line under writer_role, the bible's competence wording stripped, a room-only override of the satire-voice banter lines, failing examples, "bro wins happen despite him" in briefs, and per-writer watch notes. The satire-voice skill file itself is unchanged.
- **Eurobound-3ho-q10:** "Approve; save Part 1; Cover 3 primary; L1 > L2 > L3 rotation". This covers the inspirations deep-dive, Cover 3 "The Last Stand" as key art, and the load screens rotating L1, then L2, then L3.
- **Eurobound-3ho-room-aion-1:** "Put Aion 3.5 back in. Mini isn't cutting it".
