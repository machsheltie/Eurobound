# Eurobound — Next-Work Handoff (paused 2026-07-31 for folder reorganization)

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
