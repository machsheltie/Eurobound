# Design Spec: Round 5 — Economy, Wallet & Crypto Satire System

**Date:** 2026-07-31
**Status:** Author-provided master specification (locked) + interview rulings; pending author review of this transcription.
**Execution:** Agent team — orchestrator, implementer lanes, canon/tone reviewer.
**Predecessors:** Rounds 1–4 (main at `860fd90`). All binding rules remain in force: Trust the
Player (§1a R3), Gregory dead, full-strength MA satire, never self/scam-aware + steal corollary,
ban-all world names + premise-cluster exemption, templates as floors.

---

## 0. Rule Supersession (author-locked)

The "no new crypto content" rule is **formally superseded** by this spec: the author directs a
full crypto-satire economy. Crypto content is now in-lane wherever this spec places it. The
Trust-the-Player rule applies at full strength: **the game never winks or undercuts the
delusion** — the UI and the bros treat every JPEG with deadpan, solemn reverence. Sincerity is
the joke.

## 1. Currency Canon (author-locked, from interview)

1. **Sovereign-X (SOVS)** is the single, continent-wide, overly-engineered "official"
   digital fiat-crypto used for ~90% of standard transactions (tickets, doctors, tips, lodging).
   Tone: high-society pretension meets sterile European bureaucracy. **No gas fees or random UI
   penalties on routine purchases** — core transactions stay clean, frictionless, predictable.
2. **€ is SOVS's display glyph.** SOVS is pegged to and displayed with the € sign — the eurozone
   ate itself and what crawled out still uses the symbol. **All existing € prices in canon remain
   valid as-written** (they ARE SOVS amounts); the wallet ticker reads SOVS. No repo-wide price
   retrofit.
3. **Koruna does not exist.** This is not "real" Europe. The koruna-retrofit list (Lane R):
   - `zdenka.md` price-ladder greeting (canon-locked line → re-locked in € /SOVS terms; her
     "40 if you go now" structure and cheapest-cure-on-the-beach guarantee survive verbatim in
     the new denomination)
   - `trivia_champ_badge_item.md` trinket-cart kid row ("10 koruna" → €)
   - `bohemian_riviera.md` + `bohemian_riviera_npcs.json` koruna/Kč references
   - "SuperKoruna Value Hypermarket" world brand → renamed (implementer proposes in-world name,
     author veto at review; must keep the discount-hypermarket joke)
   - Lane W-class sweep for any remaining koruna/Kč in tracked files; drafts ledgered to adoption
   - `bohemian_riviera_items.json` currency-wording line updated to the SOVS/€ canon
4. **10% back-alley economy:** shady off-grid vendors refuse SOVS ("accounts frozen by EU
   regulators") and accept only volatile darknet shitcoins, purchased at adjacent exchange kiosks.

## 2. Wallet UI Architecture (author-locked)

Two asset tabs, strictly controlled visibility:

- **TAB 1 — "The Legacy Vault"** (unlocked from game start). High-society museum gallery meets
  unhinged tech-bro delusion: soft-lit card frames, gold-accented "Provenance Verified" seals,
  absurdly optimistic "Estimated Future Value" metrics. Houses narrative NFTs, early-2000s
  nostalgic relics, cultural artifacts from quests.
  - **First-open modal (verbatim, author-locked):** "WELCOME TO THE LEGACY VAULT / Generational
    Wealth in JPEG Form" + the "Every image in this vault has been carefully curated… We are
    early. Painfully early. And that is exactly where you want to be." copy.
  - Permanent sub-header: "Portfolio Thesis: Undervalued Nostalgia + Scarcity = Inevitable Upside"
  - Progress counter: "[N of ∞] The Legacy Vault Secured"
  - Every NFT card carries: Edition tag, Estimated Future Value (always absurd; the tractor NFT's
    is "████████ (Loading… still loading… extremely bullish)"), a solemn Collector's Note, and an
    over-serious Acquisition Story (e.g. the tractor NFT: "Gifted by Aaron the Unflappable after
    drunkenly losing to his god-tier pocket kings. Can you FEEL IT?").
- **TAB 2 — "Bagholder Assets"** (HIDDEN at game start — does not render, no empty stub).
  - **Trigger:** first time the player is rug-pulled, receives a Vault Certificate, and selects
    "Inspect" → set `has_inspected_first_crypto_trash = true` → tab permanently reveals with a
    subtle badge and a 3-second party reaction line.
  - Houses physicalized crypto trash: dead paper Vault Certificates, $SPANK tokens, ICQ airdrop
    spam.
- The two-tab contrast is itself a quiet joke: one folder of scams they got rugged on, one folder
  of nostalgia bait they believe is high art. Nobody in the game ever says this out loud (§1a).

## 3. Shitcoin Kiosk System (author-locked)

- **Master Pool:** 25–30 unique shitcoins (RugPullInu, GigaChadX, ThongCoin, $SPANK, SafeMoon-X,
  TractorCoin as seeds; Lane C invents the rest — each coin needs name, gag concept, certificate
  design, and QR-page concept; all subject to author veto list at review).
- **Active roster:** kiosk UI (Broke-ATM / QuickRug24 terminals) renders a clean ticker of 7–8
  active coins from the pool. Roster reshuffles on: major zone transition, hostel/hotel rest,
  major story/side-quest beat completion.
- **Rug-pull logic:** vendors are honest — they genuinely want to sell their goods; the rug pull
  happens IN TRANSIT on-chain between kiosk and counter. **35% success / 65% rug.**
  - Win: transaction clears; player buys exclusive/overpowered/progress-skipping items
    (Gold-Thread Fanny Pack, VIP Backstage Pass, Illegal Energy Drinks — Lane C expands the
    catalog).
  - Loss: token hits $0.00 exactly as the player pays; vendor refuses the dead coin; instant bro
    coping line ("It's just a market correction, Chadwick! Diamond hands!"); player receives a
    physical collectible certificate (§5).
- **Wiki-proofing (three layers):** (A) per-save random seed — a coin that pays on one save is a
  100% scam on another; (B) live randomized market board, reshuffled on zone re-entry/rest;
  (C) the 35/65 roll executes at the moment of payment, mimicking a liquidity drain.

## 4. ICQ Airdrops (author-locked)

Delivered via the in-game ICQ window with the vintage "Uh-oh!" sound. Senders: Tony420,
CryptoBro69, SpamBot99 (+ Lane C may add senders consistent with Darkweb Dossier canon).
Passive, comedy-only: 0-value junk coins (e.g. 100,000 $SPANK) land in Bagholder Assets, with a
3-second bro misinterpretation line ("Chadwick, we just got airdropped 100k SpankTokens! We're
institutional investors now, bro!").

## 5. Physicalized Crypto Trash + Real-World QR ARG (author-locked)

On every rug pull the kiosk prints a high-gloss laminated **"Vault Certificate"** / paper wallet
for that failed coin — cardstock guaranteeing ownership of worthless tokens, with a dead QR code
printed on the item asset. **The QR codes are real:** scanning with an actual phone opens a
custom-built, hilarious 404/Geocities-style page per coin (e.g. RugPullInu → a broken 2000s
"Poodle Paradise Dog Grooming Salon in Brazzaville" site, offline because the owner's mining rig
overheated; GigaChadX → a luxury yacht-club site stamped "SEIZED BY MARITIME TAX AUTHORITIES").
This round DESIGNS the pages (concept + copy per coin, filed with each coin's entry); building
and hosting the actual web pages is production work, explicitly out of scope, ledgered.
Note: QR pages are real-world content — the ban-all rule applies in-game only; the joke pages
may reference real places (Brazzaville) since they are framed as the real internet.

## 6. Integration & Retrofit (from interview + canon reconciliation)

1. **Existing NFTs get Legacy Vault cards** (Lane V): the 12-NFT Frat Bro collection —
   including "She Thinks My Tractor's Sexy" (Edition 1 of 1 — Acquired via high-stakes poker),
   "Blarney Trap Receipt JPG", "Pixelated Kebab Monkey", "Mask Selfie GIF", etc. — each gets the
   full card treatment (edition tag, future value, collector's note, acquisition story) appended
   to its canon (item file where one exists; the NFT quest files otherwise). FuncoLand Nostalgia
   Series (author-provided card copy) joins the Vault as a new relic entry.
2. **Koruna retrofit** per §1.3 (Lane R).
3. **Existing crypto canon reconciled** (Lane R): CryptoBro69's gags, the Crypto Coins running
   gag in `debaucheryville.md` ("Worthless currency that fluctuates wildly"), Shadow Exchange
   rates, and the CRYPTO CHECK template boilerplate get one consistency pass so they reference
   the SOVS/shitcoin system rather than generic "crypto coins." Surgical; established jokes keep
   their shape.
4. **System doc home:** new `Design/Mechanics/Economy/` folder — `economy_system.md` (SOVS, 90/10,
   kiosks, rug-pull math, wiki-proofing), `wallet_ui.md` (both tabs, reveal trigger, card
   layouts, verbatim UI copy), `shitcoin_master_pool.md` (all 25–30 coins), `icq_airdrops.md`.
   Engine Requirements blocks in each (seed architecture, state flags, roster rotation triggers).
5. **Aaron consistency:** the tractor NFT's Vault card acquisition story quotes his canon
   ("Can you FEEL IT?" is his vibes-speech lineage); his profile and thekingswerehumming.md are
   referenced, not edited, unless the reviewer finds a contradiction.

## 7. Team Structure (proposed)

- **Lane E — System docs** (§6.4): the four Economy/ files, harvesting this spec verbatim where
  copy is author-locked.
- **Lane C — Coin content:** the master pool (25–30 coins: name, gag, certificate, QR-page
  concept), kiosk terminal flavor (Broke-ATM/QuickRug24), win-catalog expansion, airdrop set.
  Runs after Lane E's economy_system.md exists (cites its mechanics).
- **Lane V — Vault cards:** Legacy Vault card entries for the 12 existing NFTs + FuncoLand;
  first-open modal + UI copy placement in wallet_ui.md coordination with Lane E (E owns the
  file; V delivers card content as its own section-file or via sequencing — plan decides).
- **Lane R — Retrofit:** koruna elimination (§1.3), crypto-canon reconciliation (§6.3).
- **Reviewer:** §1a sweep (nothing winks — the deadpan holds everywhere), tone (bros never
  scam-aware even mid-rug: every loss is a market correction), canon fidelity (verbatim
  author-locked UI copy), ban-all compliance (in-game text; QR-page concepts exempt per §5),
  template compliance where item files are touched, ID/naming consistency, no edits to Aaron's
  profile or quest, lane discipline.

## 8. Out of Scope

Building/hosting the real QR web pages (production, ledgered); engine implementation (Godot
session); draft adoption; brands ruling; the Dutch cultural-heritage cluster; Publandia's 4th
NFT slot content (the slot itself is unaffected by this round).
