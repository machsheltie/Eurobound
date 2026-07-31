# Design Spec: Round 4 — The Scrub Round (Deferred Work & Ledger Cleanup)

**Date:** 2026-07-31
**Status:** Approved by author (interview + design approval)
**Execution:** Agent team — orchestrator (session lead), five implementer lanes, one reviewer.
**Predecessors:** Rounds 1–3 (all on main at `2fa3fc1`). All prior binding rules remain in force,
especially R3 spec §1a (Trust the Player), §1b (Gregory Is Dead), §1c (Full-Strength Satire),
never self-aware / never scam-aware + steal corollary, templates as floors.

---

## 1. NEW BINDING RULE: Two-Tier World-Names (author-locked, game-wide, permanent)

- **Tier 1 — PLAYER-FACING text** (dialogue, display names, item/examine/UI strings, narrator
  lines, song lyrics, achievement names, ICQ messages, graffiti — anything a player could read
  in the shipped game): **world names only.** Zero real-world place/nation references.
  **AUTHOR RULING (ban-all, expansion-proofing):** this bans ALL real-world places, nations,
  districts, and demonyms — not just current parody targets — because future expansion packs may
  parody any city (e.g. Istanbul, Rotterdam, Belgium, Prussia, Ireland, De Pijp, "Amsterdammer"
  are all banned in shipped text). Jokes that depended on a real name (wrong trivia answers,
  food-heritage gags) are rewritten with in-world equivalents that preserve the joke's structure.
  Violations are defects. (Currency terms — €, koruna — are NOT in scope of this rule; their
  fate belongs to the forthcoming Economy System round.)
  **PREMISE CLUSTER EXEMPTION (author-locked):** the ban covers PLACES, not peoples, languages,
  or the continent frame. These are canon and no sweep may touch them: (1) "American"/"America"
  as the bros' identity and the locals' punchline engine; (2) "Europe/European" as the game's
  frame (the game is EuroBound); (3) real language names where language use is mechanical or
  textural (order-in-German minigame, Czech-subtitled asides; "Bohemian" is the in-world term in
  shipped Debaucheryville dialogue); (4) NPC heritage characterization (e.g. the döner vendors'
  Turkish heritage) — heritage is dignity per the full-strength-satire rule and stays.
  **Minted names (author-locked, use verbatim):** Publandia's river path "Liffey Walk" →
  **"Quay of Last Resort"**. "Old Town Square" as a zone name in drafts consolidates to its
  in-world successor **"Astronomical Cockup Square"**. Draft beer item "Blade Belgian" gets an
  in-world rename (implementer-invented, flagged for author veto at review).
- **Tier 2 — NON-SHIPPING design metadata** (parody-target headers like "(Prague Parody)",
  alias fields, voice/accent directions like "Czech-accented English", art references like
  "modeled on the Vienna State Opera", satire-angle analyses, QA checklists): real-world names
  are **PERMITTED** — parody documentation needs its targets.
- **Over-scrubbing is a defect equal to under-scrubbing.** Removing legitimate Tier-2 metadata
  destroys design information; every scrub decision must classify the text's tier first.
- Ambiguous cases (e.g. a menu-item annotation) default to Tier 2 unless the string demonstrably
  ships to the player.

## 2. Lane W — Tracked-File World-Names Sweep

Sweep all tracked files matching (case-insensitive) `prague|vienna|viennese|habsburg|vltava|
\bdublin\b|temple bar|\bczech\b|\baustria` (~40 files; regenerate the list at execution).
For each hit: classify tier; fix Tier-1 violations with world-name replacements in the file's
own voice; leave Tier-2 hits untouched and log them as classified-compliant.
Known Tier-1 violations to fix:
- `Design/Quests/greatdonerdebate.md` ~lines 217, 246 — "Prague" and "Dublin" in SPOKEN NPC
  dialogue (highest priority; rewrite in-world).
- `Design/World Design/Publandia/publandia.md` ~line 141 — NFT #1 "Temple Bar Receipt JPG" is a
  player-facing item name → rename to a Publandia-world bar name (author-taste comedy; the
  "receipt JPG" joke structure stays). Propagate the new name anywhere the NFT is referenced.
Known Tier-2 (leave): "(X parody)" headers, "Czech Alias" fields, voice directions,
"Czech-parody pipeline" production notes, art-reference lines.
**Concurrent-session guard:** before editing ANY file, check `git status --porcelain -- <file>`;
if the file has uncommitted modifications (another session's in-flight work), SKIP it and ledger
it in the report instead of editing. This applies especially to anything under `Assets/`.
Deliverable: the fixes + a classification table (file → hits → tier → action/skipped) in the lane report.

## 3. Lane G — Full Draft Clean (~55 uncommitted files)

All uncommitted draft files under `Design/` (regenerate the list: disk-grep minus tracked):
1. **De-Gregory** per R3 spec §1b: every gregory/puppet reference (case-insensitive, including
   dependent puppet lines) CUT or rewritten as a plain understated Bradley line with the
   explanatory observation deleted. Truth-telling function transferred to no one.
2. **Two-tier scrub** of Tier-1 (player-facing) text only, same method as Lane W.
Drafts REMAIN UNCOMMITTED — these are disk edits so no future session inherits the puppet or a
real-world name from pattern-matching the drafts. No other draft content is reviewed, improved,
or adopted this round.

## 4. Lane S — Structural Hygiene

1. **City-file dedupe (tracked):** for each pair — `Design/World Design/sinfonia.md` vs
   `Design/World Design/Sinfonia/sinfonia.md`, and `Design/World Design/debaucheryville.md` vs
   `Design/World Design/Debaucheryville/debaucheryville.md` (also check publandia/shamsterdam
   flat-vs-folder pairs and dedupe any found where both are tracked) — diff the pair, merge any
   unique content into the FOLDER-layout file (canonical going forward), then `git rm` the flat
   duplicate. Nothing is deleted without a documented content diff; the merge decisions go in
   the lane report and commit message.
2. **Bassline Opera House consolidation (drafts):** merge the two draft .md variants
   (`bassline_opera_house.md`, `the_bassline_opera_house.md`) into ONE draft whose location ID
   matches its own data suite's usage; delete the other on disk. Fix the two stale
   `sinfonia_baroness_ballroom_01` → `sinfonia_hidden_baroness_ballroom_01` refs in the Bassline
   core/environment JSONs (tracked or draft — fix wherever they live).
3. **Typo rename (repo-wide, tracked):** `sinfonia_imperalsquare_haute_couture_01` →
   `sinfonia_imperialsquare_haute_couture_01` everywhere it appears (the Haberdashery .md line 6
   declaration + all references). It is a clear misspelling of a canonical ID; fix while cheap.
4. **`night_porter.png` backfill:** add the sprite line (64×96) to the Haberdashery .md's PNG
   Asset Requirements Summary (Character Sprites), matching the summary's format.
5. **Template fix (draft):** `Templates/location_validation_template.md` — the Sinfonia checklist
   line instructing "Habsburg references" is rewritten to comply with the two-tier rule (Tier-2
   guidance phrasing, e.g. "old-imperial flavor per the city's parody-target metadata").

## 5. Lane T — Riviera Trio + NFT ID

1. Full 16-section `Templates/NPC_Profile_Template.md` profiles, harvesting existing canon from
   the Riviera JSONs/location file (their registrations, roles, any established lines are
   binding; invent the rest in house voice, tone rules apply):
   - `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/rosta.md` (`debaucheryville_npc_rosta_01`)
   - `.../standa.md` (`debaucheryville_npc_standa_01`)
   - `.../zdenka.md` (`debaucheryville_npc_zdenka_01`)
   (If the Riviera NPCs JSON already carries different provisional IDs for them, THOSE win —
   verify before minting.)
2. `Design/Quests/fratbronft.md`: declare canonical quest ID `global_sidequest_fratbro_nft_01`
   (one ID line in the file's own style). The Backroom JSONs' `quest_file` pointers stay valid
   and unchanged. Publandia's 4th NFT slot remains a sanctioned open slot — no change.

## 6. Reviewer Dimensions

Two-tier classification correctness in BOTH directions (no under-scrub: zero Tier-1 real-world
names remain in tracked files; no over-scrub: Tier-2 metadata survives intact); Gregory/puppet =
zero hits across the ENTIRE disk under Design/ (tracked + drafts); dedupe safety (diff-verified:
no unique content lost from any deleted file); trio profiles 16/16 template H2s + tone rules;
no content invented by mechanical scrubs beyond necessary replacement lines; JSONs still parse;
`imperalsquare` = zero hits; lane discipline.

## 7. Out of Scope (explicit)

Draft adoption/quality review (future rounds); Publandia 4th NFT content; Aaron/Black-Tie beats
(done); engine implementation. Concurrent-session working-tree files (Assets/, Godot/) are never
touched.
