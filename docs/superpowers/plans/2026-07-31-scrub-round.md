# Round 4 Scrub Round Implementation Plan (Agent-Team Edition)

> **For agentic workers:** Executed by an **agent team**: orchestrator + four parallel implementer lanes with strict file ownership + one reviewer. Each implementer gets ONLY its lane section plus Global Constraints. Source of truth: `docs/superpowers/specs/2026-07-31-scrub-round-design.md` (read in full — §1's two-tier rule governs every scrub decision).

**Goal:** Clear the Rounds 1–3 ledger: two-tier world-names sweep of tracked files, full Gregory+names clean of ~55 drafts, structural dedupe/typo/backfill hygiene, and the three deferred Riviera profiles.

**Architecture:** Four fully parallel lanes (W tracked-names, G drafts, S structural, T trio+ID) with exclusion lists preventing overlap; orchestrator commits per lane (drafts stay uncommitted); reviewer sweeps; one fix wave; land on main.

**Tech Stack:** Markdown/JSON edits; PowerShell/grep validation; git for dedupe.

## Global Constraints

- **Two-tier world-names rule (spec §1, binding):** Tier 1 player-facing text = world names only, zero real-world references. Tier 2 design metadata (parody headers, aliases, voice directions, art references, satire notes) KEEPS real-world names. **Over-scrubbing = defect equal to under-scrubbing.** Classify before touching. Ambiguous → Tier 2 unless demonstrably shipped to the player.
- **All prior rules in force:** R3 §1a nothing explains the joke; §1b Gregory strip-on-sight (cut, or plain understated Bradley with the observation deleted; function transferred to no one); §1c full-strength MA satire; never self/scam-aware + steal corollary; templates are floors (NPC = 16 H2s).
- **Concurrent-session guard (every lane):** before editing ANY file, run `git status --porcelain -- "<file>"`; if it shows uncommitted modifications (`M`/`AM` etc. — another session's in-flight work), SKIP the file and ledger it in your report. Untracked (`??`) is NOT dirty for this purpose — Lane G's drafts are untracked by definition.
- **Pre-minted names (use verbatim, no alternatives):**
  - NFT #1 rename: "Temple Bar Receipt JPG" → **"Blarney Trap Receipt JPG"** (reuses the established Publandia location The Blarney Trap; the receipt-JPG joke structure is unchanged).
  - Typo rename: `sinfonia_imperalsquare_haute_couture_01` → **`sinfonia_imperialsquare_haute_couture_01`** (Lane S owns this replace everywhere, including files other lanes normally hold).
  - Trio NPC IDs (unless the Riviera NPCs JSON already carries provisional IDs for them, which then win): `debaucheryville_npc_rosta_01`, `debaucheryville_npc_standa_01`, `debaucheryville_npc_zdenka_01`.
  - NFT quest ID: `global_sidequest_fratbro_nft_01`.
- **Git discipline:** implementers run only read-only git commands where their lane section says so (status/diff/ls-files); Lane S additionally runs the exact `git rm` steps its section specifies. The orchestrator does all commits with explicit paths.
- **Surgical edits only.** Mechanical scrubs invent no content beyond the necessary replacement line, written in the file's own voice.

## File Ownership & Exclusions

| Lane | Owns | Excluded (owned elsewhere) |
|---|---|---|
| W | All TRACKED files with world-name hits | Lane S's files (city pairs, Haberdashery .md, Bassline JSONs, template), Lane T's `fratbronft.md`, anything dirty, anything untracked |
| G | All UNTRACKED files under `Design/` | Lane S's drafts (both Bassline .md variants, `Templates/location_validation_template.md`) |
| S | The city flat/folder pairs; `Design/World Design/Sinfonia/haute_couture_haberdashery.md`; both Bassline .md drafts + Bassline core/environment JSONs; `Templates/location_validation_template.md`; every file touched by the imperalsquare rename | — |
| T | Create 3 trio profiles; `Design/Quests/fratbronft.md` | — |

---

### Lane W: Tracked-File World-Names Sweep

- [ ] **Step 1: Regenerate the hit list.** `git grep -i -l -E "prague|vienna|viennese|habsburg|vltava|\bdublin\b|temple bar|\bczech\b|\baustria" -- "Design/" "Assets/"` — then subtract your exclusion list (above) and any dirty files (guard).
- [ ] **Step 2: Classify every hit** (file, line, quoted text → Tier 1 or Tier 2, one row each). Tier-2 rows get action "keep".
- [ ] **Step 3: Fix Tier-1 violations.** Known: `Design/Quests/greatdonerdebate.md` ~217 and ~246 — "Prague"/"Dublin" inside spoken NPC dialogue; rewrite the sentences in-world (Debaucheryville/Publandia or in-fiction phrasing), preserving each joke's structure. `Design/World Design/Publandia/publandia.md` ~141 — rename the NFT to "Blarney Trap Receipt JPG" (pre-minted). Fix any additional Tier-1 hits your classification surfaces, same method.
- [ ] **Step 4: Validate** — re-grep: every remaining hit in your swept files maps to a Tier-2 row in your table. Report DONE with the full classification table.

### Lane G: Full Draft Clean

- [ ] **Step 1: Regenerate the draft list.** All files under `Design/` on disk that are NOT tracked (`git ls-files` complement; PowerShell compare works). Subtract Lane S's two Bassline drafts. (`Templates/` drafts are S's too.)
- [ ] **Step 2: De-Gregory every draft** per the Global Constraints rule — including dependent puppet lines that reference him without the name (search gregory, puppet, muffled, "from Bradley's hand", ventriloq, "miniature opera cape"; case-insensitive).
- [ ] **Step 3: Two-tier scrub of Tier-1 text in drafts** — same classification discipline as Lane W; Tier-2 metadata stays.
- [ ] **Step 4: Validate** — case-insensitive gregory/puppet = ZERO across all drafts; spot-list five example Tier-1 fixes and five Tier-2 keeps in the report. Drafts remain uncommitted; do not stage anything. Report DONE with per-file counts (sites cut / rewritten / names fixed).

### Lane S: Structural Hygiene

- [ ] **Step 1: City-pair dedupe.** For each tracked pair — `Design/World Design/sinfonia.md` vs `Design/World Design/Sinfonia/sinfonia.md`; `Design/World Design/debaucheryville.md` vs `Design/World Design/Debaucheryville/debaucheryville.md`; ALSO check for flat `publandia.md`/`shamsterdam.md` vs folder versions where BOTH are tracked — produce a diff, merge any content unique to the flat file into the folder file (folder file is canonical), then `git rm "<flat file>"`. Record per-pair: unique content found (quoted) and where it was merged. If a pair's diff shows the flat file has NO unique content, `git rm` with a note. If any file in a pair is dirty (guard), skip the pair and ledger it.
- [ ] **Step 2: Bassline consolidation (drafts).** Diff the two draft .md variants; keep the one whose location ID matches the Bassline data suite's own usage (check the suite JSONs — the survivor must agree with them), merge unique content from the other, delete the loser from disk (plain file delete — untracked). Then fix the two stale refs in the Bassline core/environment JSONs: `sinfonia_baroness_ballroom_01` → `sinfonia_hidden_baroness_ballroom_01` (wherever those JSONs live, tracked or draft; JSONs must still parse).
- [ ] **Step 3: imperalsquare typo rename, repo-wide.** `git grep -l "imperalsquare"` + disk grep of drafts; replace `sinfonia_imperalsquare_haute_couture_01` → `sinfonia_imperialsquare_haute_couture_01` in EVERY file found (this crosses other lanes' normal domains by design — you own this operation). Validate: zero "imperalsquare" hits anywhere on disk afterward; all edited JSONs parse.
- [ ] **Step 4: night_porter.png backfill.** In `haute_couture_haberdashery.md`'s PNG Asset Requirements Summary → Character Sprites: add `night_porter.png - 64x96 - Night porter (PATH B)` in the list's exact format; update the sprite count if the section states one.
- [ ] **Step 5: Template fix (draft).** `Templates/location_validation_template.md`: rewrite the Sinfonia checklist line instructing "Habsburg references" into two-tier-compliant guidance (e.g. "old-imperial flavor consistent with the city's parody-target metadata (see two-tier world-names rule)"). Do not restructure the template otherwise.
- [ ] **Step 6: Validate + report** — per-step evidence, JSON parses, zero imperalsquare, dedupe diffs summarized. Report DONE.

### Lane T: Riviera Trio + NFT Quest ID

- [ ] **Step 1: Verify IDs.** Read `Design/World Design/Debaucheryville/npcs/Bohemian_Riviera/bohemian_riviera_npcs.json` — if Rosťa/Standa/Zdenka rows carry provisional IDs, use those verbatim; else use the pre-minted trio IDs.
- [ ] **Step 2: Three full profiles** — `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/rosta.md`, `standa.md`, `zdenka.md`; all 16 template H2s each; harvest ALL established canon from the Riviera NPCs JSON, location .md, and any quest references (their registrations/roles/lines are binding); invent the rest in house voice (read `janek_sykora.md` for style). Tone rules apply in full — locals are winners/operators/unbothered; never explain any joke.
- [ ] **Step 3: NFT quest ID.** In `Design/Quests/fratbronft.md`, add the canonical ID declaration `global_sidequest_fratbro_nft_01` in the file's own style (one line, near the top). While in the file: if it contains "Temple Bar" anywhere, apply the pre-minted rename "Blarney Trap Receipt JPG" for consistency with Lane W's publandia.md fix.
- [ ] **Step 4: Validate** — 3 × 16/16 H2s in template order; zero gregory/real-world-name hits in the new files; report DONE.

---

## Review & Landing (orchestrator)

- [ ] Commit lanes W, S, T on DONE (explicit paths; Lane S's commits include the `git rm`s). Lane G produces no commits (drafts) — its report is the artifact.
- [ ] Reviewer: two-tier correctness both directions (sample Lane W's table AND independently spot-check ~10 files); gregory/puppet = zero across the ENTIRE `Design/` disk tree; dedupe safety (verify no unique flat-file content lost — re-diff against git history); trio 16/16 + tone; imperalsquare = zero; JSONs parse; no invented content in scrubs; lane discipline incl. dirty-file guard compliance.
- [ ] One fix wave, scoped re-review, then land: fetch origin, fast-forward main, push.
