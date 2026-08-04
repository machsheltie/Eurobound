# Round 5 — Economy, Wallet & Crypto Satire System (Agent-Team Plan)

> **For agentic workers:** Executed by an agent team: orchestrator + five implementer lanes with strict file ownership + one reviewer. Each implementer receives ONLY its lane section plus Global Constraints. Source of truth: `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` — read it in full, especially §0a (new binding rules), §7a (author rulings), §7b (repo reality).

**Goal:** Ship the full economy/crypto-satire system as new design docs, retrofit existing canon onto it (koruna elimination, Legacy Vault cards, NFT #12), and rebuild the engine brewery tracker from author canon.

**Architecture:** Five parallel lanes. Lane E (system docs) and Lane C (coin pool) create NEW files in `design/economy/`. Lane V creates the Vault-card file there too. Lane R does surgical retrofits in `_sorting/`. Lane B fixes the engine tracker in `game/`. No two lanes share a file.

**Tech Stack:** Markdown design docs; JSON + GDScript for the engine tracker; PowerShell/grep validation.

## Global Constraints

- **§0a rules are supreme:** (1) **NO MASCOTS, EVER** — no puppets, pets, named companion objects, fourth party members, or emotional-support entities; objects may be junk trinkets but never get names, personalities, adoption beats, or evolution mechanics. (2) **Story/lore/satire changes require an AUTHOR ruling first** — escalate ambiguity, never resolve it by invention. Sanitizing, softening, de-subversifying, or over-explaining is a **highest-severity defect**. This is an unapologetically subversive MA-rated game.
- **Trust the Player (R3 §1a):** nothing explains the joke. The wallet UI and the bros treat every worthless JPEG with total deadpan reverence. **The game NEVER winks.** No narrator aside, tooltip, or NPC may signal "this is satire."
- **Never self-aware / never scam-aware + steal corollary:** even mid-rug-pull the bros believe they're winning ("It's just a market correction!"). Sellers/scammers always know exactly what they have.
- **Ban-all world names** (real places/nations/districts/demonyms) in player-facing text; **premise-cluster exemption** (American identity, Europe frame, language names, heritage) stands. **BRANDS ARE EXEMPT AND CLOSED (§7a.1)** — never flag or change a brand.
- **QR-page concepts are exempt** from ban-all (framed as the real internet).
- **CONCURRENT-WINDOW GUARD:** never edit any file under a `**/PNG_Assets/**` directory. Run `git status --porcelain -- "<file>"` before editing ANY file; if dirty, skip and ledger it.
- **Locate files by search, not memory** — the reorg moved things (NPC profiles now sit in their location's `npcs/` folder).
- **SUPERSEDED 2026-08-01 (author ruling): the euro display-glyph rule is DEAD.** The whole game runs on Sovs; the euro sign appears nowhere. The repo-wide retrofit HAS been executed (4,215 conversions / 330 files). Prices read `40 Sovs` in prose, `40 SOVS` in signage. **Neither koruna nor euros exist.** Canon: `_sorting/Design/Economy/currency.md`.
- **Templates are floors** where item/NPC files are touched. No git commands by implementers; the orchestrator commits.

## File Ownership Map

| Lane | Owns |
|---|---|
| E | `design/economy/economy_system.md`, `design/economy/wallet_ui.md`, `design/economy/icq_airdrops.md` (create) |
| C | `design/economy/shitcoin_master_pool.md` (create) |
| V | `design/economy/legacy_vault_cards.md` (create) |
| R | Retrofit edits in `_sorting/` (koruna files, `fratbronft.md`, NFT-hunt leg files, crypto-canon files) — clean, non-PNG_Assets files only |
| B | `game/Assets/Data/saves/brewery_tracker_full.json`, `game/Scripts/systems/breweries/*`, `Tools/game_tracking/brewery_tracker_usage_example.gd` |

---

### Lane E — Economy System Docs

**Create three files in `design/economy/`.** Harvest author-locked copy from spec §1–§4 **verbatim** where the spec marks it locked.

- [ ] **Step 1: `economy_system.md`** — SOVS identity and tone (continent-wide, overly-engineered official digital fiat-crypto; high-society pretension meets sterile bureaucracy); the euro display-glyph rule (existing prices ARE SOVS amounts; ticker reads SOVS); **no gas fees/UI penalties on routine purchases**; the 90/10 split; back-alley vendors refusing SOVS ("accounts frozen by EU regulators"); kiosk terminals (Broke-ATM, QuickRug24); the 35% success / 65% rug distribution with rug-in-transit logic (vendors are honest); the three wiki-proofing layers (per-save seed, live randomized market board, in-transit roll at payment); roster rotation triggers (zone transition, rest, major beat). Include an **Engine Requirements** block: seed architecture, state flags, roster-rotation hooks, the `has_inspected_first_crypto_trash` flag.
- [ ] **Step 2: `wallet_ui.md`** — both tabs per spec §2. Tab 1 "The Legacy Vault" (unlocked at start; gallery aesthetic; the **verbatim** first-open modal copy; the permanent Portfolio Thesis sub-header; the `[N of ∞] The Legacy Vault Secured` counter; card anatomy: Edition tag / Estimated Future Value / Collector's Note / Acquisition Story). Tab 2 "Bagholder Assets" — **HIDDEN at start, does not render, no empty stub**; reveal trigger and the 3-second party reaction. State the two-tab contrast as a design note that **no character ever says aloud**.
- [ ] **Step 3: `icq_airdrops.md`** — delivery via the ICQ window + vintage "Uh-oh!" sound; senders Tony420, CryptoBro69, SpamBot99 (may add senders consistent with Darkweb Dossier canon); 0-value junk coins into Bagholder Assets; the 3-second bro misinterpretation ("institutional investors now, bro!"); write 8–12 airdrop messages in-voice.
- [ ] **Step 4: Validate** — verbatim author copy byte-exact; nothing winks; no mascots; report DONE.

### Lane C — Shitcoin Master Pool

- [ ] **Step 1: Create `design/economy/shitcoin_master_pool.md`** — **25–30 coins.** Seeds from the author: RugPullInu, GigaChadX, ThongCoin, $SPANK, SafeMoon-X, TractorCoin. Invent the rest in the game's register.
- [ ] **Step 2: Each coin needs** — ticker/name; a one-line pitch in scam-marketing voice; the **Vault Certificate** design (high-gloss laminated cardstock, dead QR code printed on it); and a **QR-page concept** (the real-world 404/Geocities-style joke page: 2–4 sentences of concept + the key on-page copy). Author examples to match in tone: RugPullInu → a broken 2000s "Poodle Paradise Dog Grooming Salon in Brazzaville" site, offline because the owner's mining rig overheated; GigaChadX → a luxury yacht-club site stamped "SEIZED BY MARITIME TAX AUTHORITIES". **QR pages are exempt from ban-all** (they're the real internet) — real places are fine there.
- [ ] **Step 3: Kiosk flavor** — Broke-ATM / QuickRug24 terminal UI copy, ticker presentation, and the 7–8 active-roster display. Add a short section noting which coins pair naturally with which city's back alleys (flavor only, no hard gating).
- [ ] **Step 4: Validate** — 25–30 coins each with all four elements; no brand is altered; nothing explains the joke; report DONE with the coin list.

### Lane V — Legacy Vault Cards

- [ ] **Step 1: Create `design/economy/legacy_vault_cards.md`** — a Vault card for **all 12 NFTs** in the Frat Bro collection plus the FuncoLand relic. Find the current NFT roster by searching `_sorting/` for `fratbronft.md` and the NFT-hunt leg files (`nfthuntdebaucheryville.md`, `nfthuntsinfonia.md`) — **read, do not edit them** (Lane R owns edits).
- [ ] **Step 2: Card anatomy per NFT** — Edition tag, Estimated Future Value (always absurdly bullish), Collector's Note, Acquisition Story (over-serious). Author-locked cards to reproduce faithfully:
  - **"She Thinks My Tractor's Sexy"** — Edition 1 of 1 — Acquired via high-stakes poker; Future Value `████████ (Loading… still loading… extremely bullish)`; Acquisition Story: *"Gifted by Aaron the Unflappable after drunkenly losing to his god-tier pocket kings. Can you FEEL IT?"*
  - **FuncoLand Nostalgia Series** — Limited Drop — Pre-2005 Retail Artifact; Future Value *"Will outpace continental real estate by 2031"*; Collector's Note *"People are going to kill for this in ten years. We're early."*; Acquisition Story about the gelato trade.
  - **"America Online"** (author-minted, Publandia #4) — a 12-second audio NFT of pure 56k modem screech, *"the birth cry of the modern internet."* Write its card in the same solemn register; it is an AUDIO piece, so the card should treat sound as fine art.
- [ ] **Step 3: Validate** — 12 NFTs + FuncoLand all carded; verbatim author copy exact; total deadpan, zero winking; report DONE.

### Lane R — Retrofit

**Locate every target by search. Check `git status --porcelain` on each before editing. Never touch `PNG_Assets/`.**

- [ ] **Step 1: Koruna elimination.** Known hits (verify with a fresh `grep -ril "koruna\|Kč"`): `trivia_champ_badge_item.md`, `bacchanusbeachbeatdown.md`, `bohemian_riviera.md`, `items/bohemian_riviera_items.json`, `npcs/Bohemian_Riviera/bohemian_riviera_npcs.json`, `npcs/Bohemian_Riviera/jaxson_vane.md`, `npcs/Bohemian_Riviera/zdenka.md`. (`PNG_Assets/Bohemian_Riviera_PNG_Assets.md` also has a hit — **SKIP IT**, ledger for the other window.) Convert prices to Sovs and re-lock Zdenka's canon-locked ladder in the new denomination: her structure and the guarantee that her shower is **the cheapest cure on the beach** must survive verbatim in meaning. **"SuperKoruna Value Hypermarket"** needs an in-world rename that keeps the discount-hypermarket joke — propose ONE name and flag it for author veto in your report.
- [ ] **Step 2: Publandia NFT #4.** Add **"America Online"** — a 12-second audio NFT of pure 56k modem screech, *"the birth cry of the modern internet"* — to `fratbronft.md` as Publandia's 4th target, and to the Publandia NFT-hunt leg file if one exists (create nothing new). Remove the "open slot / TBD" language now that the slot is filled. **"America Online" is a brand and is EXEMPT — do not alter the name.**
- [ ] **Step 3: Crypto-canon reconciliation.** One surgical consistency pass so existing crypto references point at the new system: the "Crypto Coins" running gag in `debaucheryville.md` ("Worthless currency that fluctuates wildly"), Shadow Exchange rate mechanics, CryptoBro69's existing gags, and the CRYPTO CHECK template boilerplate. Established jokes keep their exact shape — you are adding system coherence, not rewriting comedy. Cite `design/economy/economy_system.md` as the system's home.
- [ ] **Step 4: Validate** — zero `koruna`/`Kč` outside PNG_Assets; all touched JSONs parse; all prices in Sovs notation, zero euro signs remaining (the old no-retrofit criterion is superseded); report DONE with the SuperKoruna rename proposal.

### Lane B — Brewery Tracker Rebuild (engine)

- [ ] **Step 1: Rebuild `game/Assets/Data/saves/brewery_tracker_full.json`** with the author's canonical 12 (spec §7a.3). Fix the city key `deboucheryville` → `debaucheryville`. Use snake_case IDs derived from the canonical display names, e.g. `the_absinthium_taproom`, `the_tap_dat_vault`, `three_crown_keg_haus`, `ye_olde_brew_lab`; `the_blarney_trap`, `the_stoutworks_brewery`, `trinity_of_pints`, `shenanigans`; `the_moderato_pub`, `the_standing_ovation`, `crown_and_cask`, `the_dancing_stein`. Delete all 8 invented IDs (`bogmans_brewery`, `flatcap_ferments`, `liffy_lager_house`, `tattie_porter_crafthouse`, `opernhaus_ale_stube`, `sachercraft_barrelworks`, `vienna_noir_fermentarium`, `schnitzelbier_innovation_lab`) and the `absynthium` misspelling. Preserve the file's existing shape (`brewery_progress` → city → id: false, plus `brewery_global_total`).
- [ ] **Step 2: Sweep the engine for hardcoded IDs** — `game/Scripts/systems/breweries/brewery_tracker.gd`, `brewery_tracker.tres`, and `Tools/game_tracking/brewery_tracker_usage_example.gd`. Update any hardcoded brewery/city IDs to match. Do NOT restructure the code or change its API; ID strings and obvious counts only. If the `.tres` is a binary/opaque resource, report rather than guess.
- [ ] **Step 3: Validate** — JSON parses; 12 entries across 3 correctly-spelled city keys; zero invented IDs anywhere in `game/` or `Tools/`; report DONE with a before/after ID table and anything the engine session must re-generate.

---

## Review & Landing (orchestrator)

- [ ] Commit each lane on DONE (explicit paths; never `git add -A` — the other window's PNG work must stay uncommitted and untouched).
- [ ] Reviewer: §0a compliance (no mascots; nothing invented that alters story/lore/satire without a ruling; nothing sanitized or softened); Trust-the-Player sweep (**the wallet never winks**); verbatim author copy byte-exact (first-open modal, tractor/FuncoLand/America Online cards, Aaron's acquisition story); bros never scam-aware even mid-rug; ban-all compliance in-game with brands and QR pages exempt; koruna zero; brewery IDs match canon exactly; JSON validity; no `PNG_Assets/` file touched; lane discipline.
- [ ] One fix wave, scoped re-review, then land on `chore/folder-restructure` (do NOT merge to main mid-reorg — the reorg branch is the active line; note the landing decision for the author).
