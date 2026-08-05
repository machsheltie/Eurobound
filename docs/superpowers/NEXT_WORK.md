# Eurobound — Next-Work Handoff (paused 2026-07-31 for folder reorganization)

## Standing rulings 2026-08-03 (CLAUDE.md / PRD-reclamation round — binding, do not relitigate)

- **The story belongs to the author alone.** The PRD branch's invented plot ("The Last Hurrah") is struck in full; the author-dictated story core is in EUROBOUND_PRD.md §4.2. No agent writes story without the author.
- **MA canon restated at full strength:** the ONLY content ceiling is no nudity — beyond that, anything goes. The seedy underbelly is shown, glorified, and ridiculed. No safe-build mechanism (`SATIRE_MODE`, `line_safe`, string swaps) may ever be created. Satire targets everything; there is no narrator; "never targets locals" is struck.
- **All tracked NPCs and locations as of 2026-08-03 are author-approved canon** — written by or with the author. This includes the full audit list (Cyberspace Kavarna, Internet History Museum, Mystery Meat Cart, The Participation Trophy, the four Debaucheryville breweries, Haute Couture Haberdashery, Bassline Opera House, Mozart's Last Rave, Café Existenz, Vape Witch Vanessa, Vlad the Validator, Suspicious Twins, Backpack Girl, CryptoBro69's Ex, Bartender Matrix, Slick Greg, the Black-Tie Backroom cast, Bohemian Riviera cast, and all Publandia/Sinfonia venues). None are agent-orphans; none get struck.
- **Killed by author ruling:** Mirror Chad; Fistø's alternate ending and any sincerity arc (Fistø survives ONLY as the graffiti-quest philosopher-janitor); Reality Check enemies/ending; the Perspective status; "The Legend" finale boss; all PRD act beats; the Holy Keg as MacGuffin (demoted back to Lord Pilsner's personal sidequest); per-city Rival Trio showdowns (Rival Trio appears ONCE, in the NFT sidequest).
- **Currency:** SOVS only — never euros, never the € display glyph, never koruna (supersedes the R5 spec §1.2 glyph rule; € price sweep COMPLETED 2026-08-04).
- **Platform:** Steam/desktop. The Apple-guidelines rationale for any content decision is void.
- **NFTs:** 12 total, 4 per city, milestones 4/8/12; 12/12 epilogue is the author-dictated CryptoBro69 press-conference arrest ("DIAMOND HANDS FOREVER!").
- **Shamsterdam is canon** — the author's fourth city, and the FINAL city of the trip (author ruling 2026-08-03): the crescendo before the airport; the finale happens there. **City order: Publandia → Debaucheryville → Sinfonia → Shamsterdam; visited cities stay open for backtracking.**
- **New author-dictated content:** Mom-call rework (Lord Pilsner secretly lives with his mom post-divorce); Bradley's wedding-ring extortion quest (player choice; DeLorean payoff); **The Weed Wraith** = minor villain in Shamsterdam; **The Schnitzel King** = minor boss of **The Golden Cutlet**, a Sinfonia dungeon (author-dictated: multi-level "authenticity" tourist-trap tavern, group-purchased VIP Cultural Heritage Pass — Chadwick's idea, basement Heritage Trial, trap doors, real combat per vault, hosts a Sinfonia NFT acquisition point; roster/boss details in development); Hot Kroger Guy stays, plus his scripted girlfriend's-phone call to Pilsner — see EUROBOUND_PRD.md §4.2–§4.4.
- **Villain template mandate:** every villain (minor villain, miniboss, city boss, finale) gets a completed `Templates/villain_template.md` profile AT CREATION — no exceptions.
- **Black-Tie Backroom Easter egg (author-dictated):** ambient entrance scene — a pretty brunette in a little black dress being chatted up by the security guards ("no way you're forty-four"); bros never notice, never explained, no name, no roster entry.
- **Risk-mitigation plans are shit-canned repo-wide** (author ruling): no risk registers, no mitigation sections, ever.
- **NO NARRATOR — swept repo-wide 2026-08-04, and no in-world substitute either.** The Aaron spec's "Narrator voice remains canon as dry stage description" carve-out is OVERRULED. Killed: the Narrator-as-Roastmaster design pillar (`party.md`), "Narrator Roast Mode" toggle (`battle_system.md`), sung "Narrator Verses" (`musicalbeats.md`), `narrator_commentary` blocks in the location template and shipped JSONs, `speaker: "narrator"` / `effect: "narrator_line"` data entries, and every `**Narrator:**` label in quest/venue docs. Prose that sat under those labels survives as **stage direction** (what is on screen, spoken by nobody). **Battle-log/UI flavor text is NOT a narrator** and stays — it is where the mechanical comedy lives ("Bradley flexes. Nobody cares. −2 Dignity"); docs that called it "the narrator's descriptions" now call it battle-log flavor text. Do not re-add a commentary section to any template.
- **Platform sweep 2026-08-03:** mobile/iOS/App Store references replaced repo-wide with Steam/desktop; App Store marketing docs banner-marked as stale history.
- The old PRD branch `claude/eurobound-jrpg-prd-uv5iog` is dead and must never be merged or treated as canon. The salvaged, author-corrected PRD lives on `claude/claude-md-game-guidelines-68oyd0`.

## Paused mid-interview 2026-08-04 (author researching — resume from here)

**Finale interview** (author chose "interview me"): Q1 answered — Shamsterdam is the final city. Q2 answered — order Publandia → Debaucheryville → Sinfonia → Shamsterdam, visited cities stay open for backtracking. **Q3 pending: what is the finale beat itself in Shamsterdam** (last blowout / final boss / money-runs-out / author's own shape). Author is thinking it through; do not invent.

**Other open author decisions:**
- Publandia dungeon: author wants NON-food concept; pitches on the table: The Dead Poets' Lock-In (literary-heritage ghosts, recommended), The Craic Mines, The Eternal Students' Union, The Bookies' Labyrinth. Needs pick + its own boss (villain template mandatory).
- The Golden Cutlet: enemy roster proposal (8 types + Schnitzel King) awaiting author kill/swap approval; NFT placement proposal = Heritage Pass fine-print QR as an alternate route to one of Sinfonia's four (Holographic Charizard suggested) — author to pick or veto.
- Rival Trio reconciliation awaiting confirm: the single game-wide appearance = the Craic Tax showdown awarding Pogs (per the author's FINAL Publandia NFT roster); Debaucheryville/Sinfonia showdowns stay dead.
- NFT card copy (Tagline/Description/Collector's Thesis) for the seven replacement NFTs: AUTHOR WRITES ONLY, blocks are empty on purpose.
- Shamsterdam city boss + quest skeleton: undefined, author's to dictate. Steam price point: open. Deluxe Roast Pack DLC: open. macOS support: open. Golden Cutlet venue doc + villain profiles: to be written from templates once roster approved.

**State at pause:** Rounds 1–4 landed and pushed to `origin/main`. Round 5 (Economy/Wallet/Crypto)
spec is approved-in-substance and committed; its PLAN and EXECUTION have NOT started — paused by
author order pending the folder reorg. Branch: `feature/bacchanus-beach-beatdown` (same as main).

## ⚠️ CRITICAL WARNINGS FOR THE REORG WINDOW

1. **~240 UNCOMMITTED draft files under `Design/` carry four rounds of disk-only cleanup**
   (complete Gregory eradication — 218 sites; ~330 world-name fixes; JSON repairs; the hippo
   de-petting). They are UNTRACKED — any `git clean`, fresh checkout, or careless delete
   destroys that work permanently. **STRONGLY RECOMMENDED: snapshot-commit everything
   (including untracked files) to a branch or archive BEFORE moving anything.**
2. All specs/plans/briefs in `docs/superpowers/` reference current absolute/relative paths.
   After the reorg, the first work session must run a path-refresh pass before executing
   anything from them.
3. `Assets/` and `Scripts/` remain the engine (Godot) session's domain — its uncommitted
   changes were still in the working tree at pause (modified Assets/Data JSONs, deletions
   under Design/World Design/Debaucheryville/sprites/, .import files).

## 🔁 RESTRUCTURE RESUME CHECKLIST (added 2026-08-04, author-ordered — do not improvise)

When the folder restructure resumes on `chore/folder-restructure`, execute in this exact order:

1. **Clean the tree first.** `git status --porcelain | wc -l` must be 0 before merging. Commit
   in-flight sweep work to the branch (never stash-and-forget, never `git clean` — see warning 1).
2. **Merge main in, main wins content conflicts:**
   `git -c merge.renameLimit=15000 merge main -X theirs`
   (run ON `chore/folder-restructure`). `-X theirs` makes main's side win any conflicting hunks;
   rename detection maps main's edits onto files the restructure moved — the raised renameLimit
   is required because the restructure renamed ~800 paths. After the merge, if anything under
   `game/` changed: run BOOT + GUT (commands in
   `docs/superpowers/plans/2026-07-31-folder-restructure.md`, Global Constraints) and match the
   27/27 baseline before proceeding.
3. **Re-run the platform/currency sweeps on moved files:** the Sovs-only retrofit (no euros, no
   koruna — standing ruling below, canon `currency.md` wherever it currently lives, originally
   `_sorting/Design/Economy/currency.md`) and the tracked world-names verification greps (small
   ledger, last bullet). Files have new paths since the sweeps last ran — sweep by content match,
   not by remembered path lists.
4. **Continue the walkthrough** per `docs/superpowers/plans/2026-07-31-folder-restructure.md`
   (Tasks 4–7: author personally places files; `_sorting/` must reach ZERO files then be deleted;
   then Tasks 8–15 game batches). Session 1 (World Design cities) state: legacy PNG-spec merges
   done with 13 `> ⚠ CONFLICT:` callouts awaiting author rulings — grep `CONFLICT` under the
   Debaucheryville design docs to find them.

## Next execution work (in priority order)

1. **Round 5: Economy, Wallet & Crypto Satire System** — spec at
   `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` (author-approved in
   substance; formal review of the transcription still open). Next: writing-plans → agent team
   (proposed lanes E system docs / C coin pool / V vault cards / R retrofit + reviewer).
   Includes the koruna elimination list (§1.3: Zdenka's ladder, badge kid, Riviera JSONs,
   SuperKoruna rename) and Legacy Vault cards for the 12 existing NFTs.
2. **Engine coordination (Godot session):** rebuild the brewery-tracker roster from author
   canon — `Assets/Data/saves/brewery_tracker_full.json` + `Scripts/systems/breweries/brewery_tracker.gd`
   currently track AI-invented breweries (`vienna_noir_fermentarium`, `opernhaus_ale_stube`,
   `sachercraft_barrelworks`, `schnitzelbier_innovation_lab`, `liffy_lager_house`, and a
   `"deboucheryville"` key typo) instead of the author's named breweries (Sinfonia: The Standing
   Ovation, Crown & Cask, The Dancing Stein; see city files for all cities). Also carried
   engine notes: per-NPC `chronicles_entry_completed[<npc_id>]` flags (Herp quest dev notes),
   the Aaron encounter's fixed-stake/500-Sovs-collateral + one-time-scene flags (thekingswerehumming
   dev notes), Zdenka's cheapest-cure constraint vs the Port-O-Cologne vendor tax (zdenka.md
   dev notes).
3. **Draft adoption rounds** (per-file formal review → commit of the ~240 drafts; each adoption
   applies full canon/tone/template review; Gregory + world names already cleaned on disk).

## Open author decisions (queued, with context)

- **Brands round:** whether real brands in player-facing text (Guinness incl. "GUINNESS
  SUPPOSITORIES", Four Loko, Winamp, Hot Topic, Habbo, Oakleys, Kinko's, Advil, Uber, Muscle
  Milk) stay (Y2K authenticity, trademark exposure), get parody-renamed (safe + new jokes), or
  mixed (keep neutral mentions, parody vice-context uses). Author to rule; then one sweep round.
  **Pre-ruled 2026-08-04:** Party Monk's HOLIDAY INN EXPRESS bathrobe easter egg — KEEP (author
  ruling; do not relitigate in the brands sweep).
- **Publandia's 4th NFT slot** — sanctioned open slot in `fratbronft.md`, awaiting the author's
  idea.
- **Shamsterdam's 4 brewery names** (author to mint; ruled 2026-08-04 that every city has 4
  breweries): rename "Brouwerij de Molen" (REAL Dutch brewery — brand liability, zero joke)
  and "Proeflokaal 't Kansen" (generic Dutch, no satire; keep Kees + jenever-distillery
  character, name only), plus invent 2 new establishments. Sweep references after minting.

## Brewery Tour — RULED 2026-08-04 (canonical spec: design/quests/general_quests/brewerytour.md)

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
- **SUPERSEDED 2026-08-01:** the euro display-glyph rule is dead by author ruling. The whole game is Sovs; **neither euros nor koruna exist**. Repo-wide retrofit already executed. Canon: `_sorting/Design/Economy/currency.md`.

## Small ledger (mechanical, any future round)

- Shamsterdam untracked city-file pair (byte-identical flat + folder copies): reorg window
  consolidates (folder copy canonical, matching the other three cities).
- `Design/Quests/Location Specific/Amsterdam/` folder name (real city in a path) — reorg
  window's call.
- `npcs/Old_Town-Square/` folder name (legacy zone name in a path) — reorg window's call.
- Bassline Opera House two-way ID references from older files (ledgered in Round 3 review).
- Post-reorg: re-run the tracked world-names verification greps once paths settle.

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
- club_flyers.md: main's scrub-round rework won all hunks (Path-B 100-Sovs payment line and
  dev-notes section from the older draft dropped with it - in git history if wanted).

## Engine data sanity-check 2026-08-04 (post-repair verification — PASSED with notes)

All five debaucheryville data JSONs parse; zero oldtown residue; shadow_exchange salvage and
kebab union (crypto vendor sheet + animation sequences + rotisserie) verified intact;
environmental & sprite_mapping are complete supersets of the pre-corruption base. Two
interaction records (kebab_alley_restroom_01, velvet_alley_kebab_01) are UNRECOVERABLE:
the line-sort corruption predates all tracked history on the main line (the merge-base file
is itself the wreck), and the branch's engine-session rebuild never included them. Their
line-soup is preserved in commit e0a18a4's fragment blob. RE-AUTHOR these two interaction
records when the engine window next works the kebab stand / kebab alley restroom (their
design-source content is intact in the quest and location docs). For the engine window: (a) locations.json (16 recs)
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
