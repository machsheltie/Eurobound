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
   the Aaron encounter's fixed-stake/€500-collateral + one-time-scene flags (thekingswerehumming
   dev notes), Zdenka's cheapest-cure constraint vs the Port-O-Cologne vendor tax (zdenka.md
   dev notes).
3. **Draft adoption rounds** (per-file formal review → commit of the ~240 drafts; each adoption
   applies full canon/tone/template review; Gregory + world names already cleaned on disk).

## Open author decisions (queued, with context)

- **Brands round:** whether real brands in player-facing text (Guinness incl. "GUINNESS
  SUPPOSITORIES", Four Loko, Winamp, Hot Topic, Habbo, Oakleys, Kinko's, Advil, Uber, Muscle
  Milk) stay (Y2K authenticity, trademark exposure), get parody-renamed (safe + new jokes), or
  mixed (keep neutral mentions, parody vice-context uses). Author to rule; then one sweep round.
- **Publandia's 4th NFT slot** — sanctioned open slot in `fratbronft.md`, awaiting the author's
  idea.

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
- **€ is SOVS's display glyph; koruna does not exist** (retrofit in Round 5).

## Small ledger (mechanical, any future round)

- Shamsterdam untracked city-file pair (byte-identical flat + folder copies): reorg window
  consolidates (folder copy canonical, matching the other three cities).
- `Design/Quests/Location Specific/Amsterdam/` folder name (real city in a path) — reorg
  window's call.
- `npcs/Old_Town-Square/` folder name (legacy zone name in a path) — reorg window's call.
- Bassline Opera House two-way ID references from older files (ledgered in Round 3 review).
- Post-reorg: re-run the tracked world-names verification greps once paths settle.
