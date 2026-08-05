# Brewery Tour Decomposition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Decompose the author-ruled brewery tour master spec into 38 per-item design files (36 collectibles for the 3 named cities + keychain rewrite + passport book), reconcile the six legacy brewery docs, and retire them to `design/legacy/`.

**Architecture:** Extraction-first pipeline per `docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md` (READ IT FIRST — it is the authority for this plan, and its Appendix A merge map is the source-of-truth inventory of what each legacy doc uniquely holds). Five phases: extraction table → author gap interview → skeletons + item files → quest-doc reconciliation → verification + retirement.

**Tech Stack:** Markdown design docs only. No `game/` changes; no boot/GUT gate. Git on Windows (case-insensitive FS).

## Global Constraints

- Master spec `design/quests/general_quests/brewerytour.md` wins every conflict it speaks to.
- Ambiguity escalates to the author — NEVER resolved by invention. Tasks 2 and 3 are AUTHOR-INTERACTIVE and cannot be delegated to subagents.
- MA satire ships at full strength — no sanitizing, softening, or over-explaining while transcribing. No narrator devices.
- Currency: SOVS only. Never euros, never €, never koruna.
- No real city/place/brand names in the new player-facing files (parody only). Exception: the beer-style vocabulary exemption (style terms incl. national-style adjectives in DESCRIPTIONS are exempt; item/place NAMES stay strict).
- Dead mechanics NEVER transcribed: per-location opener vendors + their prices, ICQ opener sales, one-keychain-gates-all model, per-city-opener model + cross-city barter, the prerequisite/gating "Golden Rule" chain, Shamsterdam-hangover-as-passive.
- Counts: 16 breweries total, 12 in scope this round. Shamsterdam: SKIP entirely (no stubs).
- snake_case, no spaces, for all new files/folders. `git mv` only — never `rm` (case-ambiguous FS).
- Commit at every task boundary minimum. Update `docs/superpowers/NEXT_WORK.md` whenever an author ruling lands.
- Every verification grep must first be proven against a planted positive before its silence is trusted.

---

### Task 1: Extraction table + gap manifest + contradiction list

**Files:**
- Create: `docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md`
- Read (all seven sources): `design/items/brewery_passport_book.md`, `design/items/brewery_passport_book_complete.md`, `design/items/brewery_passport_book_debaucheryville.md`, `design/items/brewery_passport_book_sinfonia.md`, `design/items/brewery_tour_bottle_opener_system.md`, `design/quests/general_quests/brewerytour.md`, `design/quests/debaucheryville/brewerytourdebaucheryville.md`
- Read (roster cross-check): `design/worlds/publandia/brewery_passport_book.md`, `game/assets/data/saves/brewery_tracker_full.json`, the Publandia city file(s) naming the 4th brewery

**Interfaces:**
- Produces: the extraction file with three sections consumed by every later task — `## Extraction Table` (one `### <brewery_slug>` block per brewery with `stamp:`, `opener:`, `beer:` field lists, each field value tagged `[source: <file> L<line>]`), `## Gap Manifest` (numbered list), `## Contradiction List` (numbered list). Also `## Roster` fixing the 12 brewery slugs.

- [ ] **Step 1: Confirm clean tree** — `git status --porcelain | wc -l` must print 0.
- [ ] **Step 2: Verify the roster.** Read the Publandia sources and the engine tracker; record the 12 slugs in `## Roster` as `<city>: blarney_trap, stoutworks_brewery, trinity_of_pints, <4th — from the city file, likely shenanigans but VERIFY>`, `debaucheryville: absinthium_taproom, three_crown_keg_haus, tap_dat_vault, ye_olde_brew_lab`, `sinfonia: standing_ovation, crown_and_cask, dancing_stein, moderato_pub`. Record each brewery's engine location ID next to its slug where the tracker has one. If the Publandia 4th brewery cannot be confirmed from any source, add it to the Gap Manifest instead of guessing.
- [ ] **Step 3: Deep-diff the stray copy.** Compare `design/worlds/publandia/brewery_passport_book.md` against `design/items/brewery_passport_book.md` (full content diff, not name-level). Record verdict in the extraction file: strict subset → retire with the rest in Task 9; unique content → add its facts to the extraction table with source tags.
- [ ] **Step 4: Build the extraction table.** For each of the 12 breweries, walk all seven sources and fill every field from the master spec's checklist (stamp: visual, ink, animation, stamper NPC, stamp speech, PNG; opener: design, inscription, material gag, PNG; beer: style, ABV, HP/SP effects, risk, price Sovs, flavor text, brewed-by, special quirk, PNG). Selection rule: master spec wins; else deepest source wins (Appendix A of the design spec says who is deepest per layer). Tag every value `[source: file Lnn]`. Dead-mechanic fields (vendor, price-of-opener, prerequisite) are NOT columns.
- [ ] **Step 5: Fill the Gap Manifest.** Every empty cell becomes a numbered gap. Seed with the known members from the design spec §3 (four Publandia stamp designs; The Fool's Gold stat block; keychain replacement gags for: Cancún, Daytona Beach, Señor Frog's, Munich/Oktoberfest, Belgium/Trappist, Germany/Czech+Pilsner Urquell; salvage decisions: 28 gatekeeper quotes, Key Collector achievement) and add everything new the walk uncovers.
- [ ] **Step 6: Fill the Contradiction List.** Seed with the known live members (Trinity of Pints unlock: "any drinking course" vs "Complete drinking lecture" vs "Senior Thesis"; Iron Gut Tripel "-10% Accuracy" unbounded vs next-turn; beer price band 8–15 Sovs template vs Blockchain Bock 18 Sovs) and add new ones found. Ruled-void items (totals ≠16, Shamsterdam 6-stamp, slot order, opener models) are listed under a `### Void (do not ask)` subheading with their ruling citations.
- [ ] **Step 7: Commit** — `git add docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md && git commit -m "extract: brewery decomposition table + gap manifest + contradictions (phase 1)"`.

### Task 2: AUTHOR GATE — gap interview (main session only, no subagent)

**Files:**
- Modify: `docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md` (append `## Rulings`)
- Modify: `docs/superpowers/NEXT_WORK.md` (rulings recorded)

**Interfaces:**
- Consumes: Gap Manifest + Contradiction List from Task 1.
- Produces: `## Rulings` — one line per gap/contradiction: `N. RULED: <author's answer verbatim-in-substance>` or `N. DEFERRED: field carries ⚠ AUTHOR TO WRITE`. Tasks 4–8 treat this section as law.

- [ ] **Step 1:** Present the manifest count to the author, then ask ONE item per message (options where they exist, e.g. salvage/kill for the gatekeeper quotes; revive/kill for Key Collector). Never batch.
- [ ] **Step 2:** After each answer, append the ruling to `## Rulings` immediately.
- [ ] **Step 3:** When the author stops or the list is done, record all rulings in the ledger's brewery section, commit both files: `git commit -m "ruling: brewery gap interview (author) - phase 2"`. Any unanswered item is recorded as DEFERRED.

### Task 3: AUTHOR GATE — skeleton templates (main session only, no subagent)

**Files:**
- Create: `design/templates/stamp_item_template.md`, `design/templates/opener_item_template.md`, `design/templates/signature_beer_item_template.md`

**Interfaces:**
- Produces: the exact section skeletons every Task 4–6 file must follow.

- [ ] **Step 1:** Present these three drafts to the author (amend per their feedback before committing):

```markdown
# Stamp: [Brewery Name]

- **Item ID**: `stamp_[brewery_slug]`
- **Brewery**: [Brewery Name] (`[engine_location_id]`)
- **City**: [City]
- **Earned**: challenge completion at this brewery (never on ordering — author ruling 2026-08-04)

## Design
- **Stamp Face**: [visual description]
- **Ink Color**: [color]
- **Stamp Animation**: [frames/beats description]

## The Stamping
- **Stamper**: [NPC name]
- **Stamp Speech**: "[the stamper's line]"

## PNG Assets
- `stamp_[brewery_slug].png` — [dimensions]; animation sheet [dimensions × frames]

## Notes
- [gags, NPC reactions, cross-references — omit section if empty]
```

```markdown
# Bottle Opener: [Brewery Name]

- **Item ID**: `opener_[brewery_slug]`
- **Brewery**: [Brewery Name] (`[engine_location_id]`)
- **City**: [City]
- **Earned**: challenge completion at this brewery — added to the Bottle Opener Keychain
  (openers are EARNED, never sold; author ruling 2026-08-04)

## Design
- **Opener**: [physical design]
- **Inscription**: "[engraved text]"
- **Material Gag**: [what it's made of and why that's funny]

## PNG Assets
- `bottle_opener_[brewery_slug].png` — [dimensions]

## Notes
- [gags, keychain-jingle interactions, cross-references — omit section if empty]
```

```markdown
# Signature Beer: [Beer Name]

- **Item ID**: `beer_[brewery_slug]`
- **Brewed By**: [Brewery Name] (`[engine_location_id]`), [City]
- **Unlocked**: challenge completion at this brewery; purchasable there afterward

## Stat Block
| Field | Value |
|---|---|
| **Style** | [style — beer-style vocabulary exemption applies to this field] |
| **ABV** | [X.X%] |
| **Effects** | [+X HP / +X SP / buffs] |
| **Risk** | [debuff chance, status, duration] |
| **Price** | [X Sovs] |
| **Special** | [the beer's unique quirk] |

## Flavor Text
> "[flavor text]"

## Notes
- [strategy, cross-references, consumption animation — omit section if empty]
```

- [ ] **Step 2:** On author approval, commit: `git commit -m "templates: stamp/opener/signature-beer item skeletons (author-approved)"`.

### Task 4: Publandia item files (12)

**Files:**
- Create: `design/items/brewery_tour/stamp_<slug>_item.md`, `opener_<slug>_item.md`, `beer_<slug>_item.md` for the 4 Publandia slugs from Task 1 `## Roster`

**Interfaces:**
- Consumes: extraction table blocks + `## Rulings` + the three committed templates (copy them; templates are floors).
- Produces: 12 files whose content is verbatim-in-substance from tagged sources/rulings; DEFERRED fields carry `⚠ AUTHOR TO WRITE` exactly.

- [ ] **Step 1:** Write the 12 files. Every field value must trace to an extraction-table tag or a Ruling; no untagged content.
- [ ] **Step 2: Verify.** Run the planted-positive protocol: add a scratch file containing `Munich` + `€` under `design/items/brewery_tour/`, confirm `grep -rnE "Cancún|Cancun|Daytona|Munich|Belgium|Germany|Czech|Oktoberfest|Señor Frog|Pilsner Urquell|Amsterdam|€|koruna" design/items/brewery_tour/` catches it, delete the scratch file, re-run — must now be silent. Also `grep -rniE "opener vendor|buy.*opener|opener.*[0-9]+ Sovs|prerequisite chain|golden rule" design/items/brewery_tour/` (planted-positive first) — silence required.
- [ ] **Step 3: Commit** — `git commit -m "content: publandia brewery item files (12) - decomposition phase 3"`.

### Task 5: Debaucheryville item files (12)

**Files:**
- Create: same trio pattern for the 4 Debaucheryville slugs.

**Interfaces:** same as Task 4. Beer files MUST carry the city files' deep fields the `complete` doc stripped (Iron Gut Tripel 2-Sov goblet deposit; Blockchain Bock live menu-price re-roll + negative-Sovs crash risk; Absinthe Lager debuffs-user-by-design; Vape Stout vapor-cloud animation; "Welcome to the Brewvolution™" untruncated).

- [ ] **Step 1:** Write the 12 files (trace rule as Task 4).
- [ ] **Step 2:** Verify — same two grep protocols over the folder (planted-positive first each time).
- [ ] **Step 3: Commit** — `git commit -m "content: debaucheryville brewery item files (12) - decomposition phase 3"`.

### Task 6: Sinfonia item files (12)

**Files:**
- Create: same trio pattern for the 4 Sinfonia slugs.

**Interfaces:** same as Task 4. Beer files MUST carry the Sinfonia Special fields (crown glass you keep +3 Sovs; foam swirls clockwise; served with a bow; recipe unchanged since 1848); stamp files carry the full stamp speeches ("Welcome to the debate, forever" / "*stamps with flourish*" / "Rise, Knight of the Cask! Your liver serves the crown!" / "Welcome to the dancers, friend!") with their source-file attributions from the extraction table.

- [ ] **Step 1:** Write the 12 files (trace rule as Task 4).
- [ ] **Step 2:** Verify — same two grep protocols (planted-positive first).
- [ ] **Step 3: Commit** — `git commit -m "content: sinfonia brewery item files (12) - decomposition phase 3"`.

### Task 7: Keychain rewrite + passport book item file

**Files:**
- Modify: `design/items/bottle_opener_keychain_item.md` (full rewrite in place)
- Create: `design/items/brewery_passport_book_item.md`

**Interfaces:**
- Consumes: Rulings (keychain replacement gags), base-passport extraction rows (Menu Integration ASCII mockups, Stamp Mechanics incl. account-persistence, book/UI PNG specs), `complete` rows (acquisition, Seamus's intro monologue).
- Produces: the two container items the 36 collectible files reference by ID (`bottle_opener_keychain`, `brewery_passport_book`).

- [ ] **Step 1:** Rewrite the keychain: 16-brewery count; granted (with first opener + passport) on the Publandia special-beer order trigger — not purchased; author-minted parody gags replacing every real-world reference; keep the authored jokes that survive (jingling audio cringe, airport security penalty, cargo-shorts weight, twist-offs line, party banter) verbatim.
- [ ] **Step 2:** Write the passport book file: acquisition via the same trigger; the base file's Menu Integration section with all three ASCII mockups copied verbatim; stamp mechanics (four unlock archetypes, 6-step process, permanence: non-tradeable, persists across save files, tied to account not save, timestamps); selfie gallery = the bros' scrapbook (Chadwick posts to his feed, #EuroboundMoments); stamp-slot pages for 4 cities × 4; book/UI PNG specs from the base file.
- [ ] **Step 3:** Verify — run both Task 4 grep protocols over the two files (planted-positive first). Additionally `grep -nE "\b12 breweries|\b14\b|\b18\b" <both files>` (plant `12 breweries` first) — silence required.
- [ ] **Step 4: Commit** — `git commit -m "content: keychain geography rewrite + canonical passport book item"`.

### Task 8: Quest-doc reconciliation

**Files:**
- Create: `design/quests/publandia/brewerytourpublandia.md`, `design/quests/sinfonia/brewerytoursinfonia.md`
- Modify: `design/quests/debaucheryville/brewerytourdebaucheryville.md`, `design/quests/general_quests/brewerytour.md`

**Interfaces:**
- Consumes: extraction rows for quest-layer systems (design spec Appendix A.5) + Rulings.
- Produces: city instance files the item files' "Notes" sections may reference.

- [ ] **Step 1:** Write the two new city files from EXISTING content only: city hangover full block (Full Irish Experience w/ "Legendary Hungover" status + no-stack rule + cures | Imperial Concerto w/ Imperial Hangover, 4 comedic effects, cure, 60-Sov repurchase, strategy block), city selfie spots + badge ("Photogenic Drinker" ladder for Publandia; "Culturally Distinguished" for Sinfonia), The Master's Toast full mechanics, city beer/stamp overview tables pointing at the item files. Challenge sections read exactly: `⚠ AUTHOR TO DESIGN — [city] challenges trend [drinking games / performance-social] per the master spec; nothing is designed yet.`
- [ ] **Step 2:** Align the Debaucheryville city file to the master spec: dead mechanics out (ICQ opener sales; keep/convert per Rulings any fake-opener scam gag the author ordered), keep Y2K Bingo + Y2K Archaeologist, Peak Y2K Tourist (MIDI Hamster Dance opener upgrade), selfie props, access gates (Three-Crown +1 Bravado; Tap Dat Vault midnight-only; 1-hour lockout; time-gated states), Neon Nightmare full block, and repoint item detail to the item files.
- [ ] **Step 3:** Update the master spec: add a `## File Map` section listing the item-file paths + city files; flip nothing else (Source Reconciliation flips in Task 9).
- [ ] **Step 4:** Verify — both grep protocols over the four files (planted-positive first).
- [ ] **Step 5: Commit** — `git commit -m "content: brewery city quest files + master spec file map - phase 4"`.

### Task 9: Coverage matrix, sweeps, retirement

**Files:**
- Modify: `docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md` (append `## Coverage Matrix`)
- Move (git mv): the six legacy docs + (if Task 1 verdict = subset) `design/worlds/publandia/brewery_passport_book.md` → `design/legacy/`
- Modify: each moved file (prepend banner), `design/quests/general_quests/brewerytour.md` (flip Source Reconciliation), `docs/superpowers/NEXT_WORK.md` (completion)

**Interfaces:**
- Consumes: design spec Appendix A (the fact inventory), all files produced by Tasks 3–8.

- [ ] **Step 1:** Build the Coverage Matrix: one row per unique fact in Appendix A.1–A.5 → `HOME: <file>#<section>` or `KILLED: <ruling>`. Every row must resolve; an unresolvable row goes back to the author before proceeding.
- [ ] **Step 2:** Re-run every grep protocol from Tasks 4–8 across `design/items/brewery_tour/`, the two container items, and the four quest files (planted-positive first, every time).
- [ ] **Step 3:** Prepend to each retiring file: `> ⚠ SUPERSEDED 2026-08-05 — decomposed into design/items/brewery_tour/, design/items/brewery_passport_book_item.md, bottle_opener_keychain_item.md, and the quests/<city>/brewerytour<city>.md files per docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md. Kept for provenance; do not edit.`
- [ ] **Step 4:** `git mv` each retiring file to `design/legacy/` (exact-case paths; two-hop rename if only case differs).
- [ ] **Step 5:** Flip the master spec's Source Reconciliation section to: `DONE 2026-08-05 — six legacy docs merged and retired to design/legacy/; coverage matrix in docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md.` Update the ledger's brewery section to point at the completed round and remaining Shamsterdam follow-on.
- [ ] **Step 6:** Final check: `git status --porcelain | wc -l` shows only intended changes staged; commit `git commit -m "verify+retire: brewery legacy docs to design/legacy/ - coverage matrix complete (phase 5)"`; push; `git status --porcelain | wc -l` prints 0.
