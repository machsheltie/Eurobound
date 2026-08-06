# HANDOFF — Window: `nft-vault-copy`

**Worktree name:** `nft-vault-copy`
**Branch:** `wt/nft-vault-copy`
**Local path:** `Eurobound/.worktrees/nft-vault-copy`
**Forked from:** `main` @ `d7fe136`
**Created:** 2026-08-06
**Reason for handoff:** author's laptop hardware failure; ~10 days on a borrowed machine.

> **This window owns exactly one thread: the seven replacement NFT cards, plus Round 5 economy
> finalization.** Other agent windows own brewery decomposition, PNG assets, the PRD/CLAUDE.md
> reclamation, and the Godot engine work — each has its own worktree. Do not take their work.

---

## 0. READ THESE FIRST, IN THIS ORDER

1. `CLAUDE.md` (repo root) — project rules, non-negotiable.
2. `docs/superpowers/NEXT_WORK.md` — the standing-rulings ledger. **The 2026-08-03/04 rulings
   supersede older specs.** Do not relitigate anything in it.
3. `design/economy/legacy_vault_cards.md` — this window's primary work surface.
4. `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §7c — the ruling that
   created this task. **But see the currency correction in §2 below: part of that spec is dead.**

---

## 1. THE JOB — 7 NFT cards awaiting AUTHOR-ONLY copy

Seven NFTs were struck from canon (they were location-derived, violating the 90s/00s pop-culture
rule) and replaced. **Names, mint numbers, and acquisition routes are already wired into canon.
Only the card copy is missing, and ONLY THE AUTHOR MAY WRITE IT.**

| # | NFT | Mint | Route (unchanged) |
|---|---|---|---|
| 1 | The Millennium Bug | #00 | Velvet Curtain bathroom QR graffiti (Debaucheryville) |
| 2 | Sea-Monkeys | #73 | Absinthe Arcade rigged claw machine (Debaucheryville) |
| 3 | Napster | #01 | Shadow Exchange ledger backroom (Debaucheryville) |
| 5 | Holographic Charizard | #98 | auction QR catalogue (Sinfonia) |
| 6 | Winamp | #97 | Bassline Opera House backstage terminal (Sinfonia) |
| 7 | Crystal Pepsi | #92 | Grounds For Concern latte-art AR filter (Sinfonia) |
| 9 | Pogs (the Slammer) | #94 | Rival Trio Showdown reward (Publandia) |

Mint numbers are **proposals** — the author may override any of them.

### Three fields per card, all author-written
`Tagline` · `Description` · `Collector's Thesis`

### Where the empty slots live (66 `[AUTHOR TO WRITE]` markers total)

| File | Markers |
|---|---|
| `design/economy/legacy_vault_cards.md` | 22 |
| `design/Quests/general_quests/fratbronft.md` | 21 |
| `design/Quests/sinfonia/nfthuntsinfonia.md` | 13 |
| `design/Quests/debaucheryville/nfthuntdebaucheryville.md` | 9 |
| `design/worlds/publandia/publandia.md` | 1 |

### ⛔ THE ONE RULE THAT MATTERS MOST HERE

**DO NOT WRITE THIS COPY. DO NOT OFFER DRAFTS UNLESS EXPLICITLY ASKED.** The author ruled they
author it personally. Inventing copy for these slots is a defect. Your job is to **ask for one
card at a time**, apply the author's text **verbatim** to every file that rosters it, then verify
byte-exactness.

### The workflow the author agreed to

Present **one NFT at a time**, giving: the route, the venue context it lives in, why the route
fits, and the fields needed. Wait for their copy. Apply it verbatim. Verify. Then present the
next. **Start with #1 The Millennium Bug** unless the author says otherwise.

### The register (from the author's two completed cards — study, do not copy)

`Who You Gonna Call? (Mint #84)` and `The Polyester Reserve (Mint #99)` are written and locked.
Their pattern:

- **The title never names the property.** Ghostbusters → *Who You Gonna Call?*; Beanie Babies →
  *The Polyester Reserve*. Oblique, grandiose, often financial-institutional.
- **`Mint #NN`** evokes the artifact's year.
- **The description opens `"Before [modern thing]..."`** — framing the old artifact as the
  ancestor of something current — then lands one hyper-specific absurd detail (*net-30 terms*,
  *typos on their tags*).
- **The Collector's Thesis closes on a bullishly-stated valuation contradiction** —
  *"Intrinsic value: $0.04. Market sentiment: Infinite."*
- Full template plus both reference specimens: **`Templates/NFT_Template.md`** (search for it —
  the restructure may have relocated it under `design/`).

### ⚠️ One known typo that must NEVER be "fixed"

The author's Polyester Reserve description contains `"a billionaire named Ty convince the nation"`.
**That is author copy and ships as written.** An inline note forbids correction. Any linter,
sweep, or reviewer that changes it is introducing a defect.

---

## 2. ⚠️ CURRENCY — A SPEC CORRECTION YOU MUST KNOW

The Round 5 spec says the euro glyph `€` is SOVS's display symbol. **THAT RULE IS DEAD.**

Author ruling (see `NEXT_WORK.md`): **SOVS only — never euros, never the `€` glyph, never koruna.**
A repo-wide sweep already converted 4,215 instances across 330 files. Prices read `40 Sovs` in
prose and `40 SOVS` in signage. Canon lives in `design/economy/currency.md`.

If you find `€` in player-facing text, it is a defect — flag it.

---

## 3. BINDING RULES (violating any of these is a highest-severity defect)

- **NO MASCOTS, EVER.** No puppets, pets, named companion objects, fourth party members, or
  emotional-support entities — and no replacements for removed ones. Objects may be junk
  trinkets; they never get names, personalities, adoption beats, or evolution mechanics.
  *(Case law: "Gregory", an AI-invented hand puppet, eradicated from 218 sites. "Gregory the
  Hippo" de-petted to a mute junk trinket by author order.)*
- **NO NARRATOR.** Swept repo-wide; no in-world substitute permitted. Prose that sat under
  narrator labels survives as **stage direction** (what is on screen, spoken by nobody).
  Battle-log/UI flavor text is NOT a narrator and stays.
- **THE GAME NEVER WINKS.** Nothing explains the joke. The wallet UI and the bros treat every
  worthless JPEG with total solemn reverence. Sincerity is the joke; naming it kills it.
- **The bros are never self-aware and never scam-aware.** Even mid-rug-pull they believe they are
  winning. Whoever sold, gifted, or minted a thing always knew exactly what it was worth.
- **MA-rated and unapologetically subversive.** The only content ceiling is **no nudity**. Beyond
  that, anything goes. **Sanitizing, softening, de-subversifying, or over-explaining is the most
  severe defect in this project.** No safe-build mechanism (`SATIRE_MODE`, `line_safe`, string
  swaps) may ever be created.
- **NFT artwork is ALWAYS 90s/00s pop culture, NEVER location-derived.** The acquisition *route*
  is location-flavored; the *artwork* never is. This rule is exactly why the seven were struck.
- **BRANDS ARE EXEMPT AND CLOSED.** Guinness, Winamp, Napster, Crystal Pepsi, America Online,
  FuncoLand and the rest stay exactly as named. Never flag or rename a brand.
- **World names only** in player-facing text — Debaucheryville, Sinfonia, Publandia, Shamsterdam.
  No real places, nations, districts, or demonyms. **Exempt:** American identity, the Europe
  frame, language names, NPC heritage, and QR-page concepts (framed as the real internet).
- **Story, lore, and satire changes require an AUTHOR ruling first.** Escalate ambiguity; never
  resolve it by invention. The story belongs to the author alone.
- **Templates are mandatory floors** for any new NPC, location, item, quest, or villain.

---

## 4. GIT DISCIPLINE — LEARNED THE HARD WAY

**Multiple agent windows share this repository.** A real mistake made in this window: running
`git add <my files> && git commit` swallowed **161 files** of another window's staged work,
because `git commit` commits the entire index, not just what you added.

**Always commit with path scoping:**

```
git commit -o <path1> <path2> -m "..."
```

`-o` / `--only` commits *only* the named paths regardless of what else is staged.

Other rules:

- Before editing ANY pre-existing file: `git status --porcelain -- "<file>"`. If it is dirty,
  **skip it and ledger it** — another window is working there.
- Never `git add -A` or `git add -u`.
- Required commit trailers:
  ```
  Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
  Claude-Session: <session url>
  ```
- **Currently dirty and owned by another window — DO NOT TOUCH:**
  `design/items/brewery_tour/*.md` (brewery item decomposition).

---

## 5. STATE OF ROUND 5 (this window's larger context)

**Shipped and landed:**

- `design/economy/economy_system.md` — SOVS, 90/10 split, 35/65 rug-pull, 3-layer wiki-proofing
- `design/economy/wallet_ui.md` — Legacy Vault plus the hidden Bagholder Assets tab
- `design/economy/shitcoin_master_pool.md` — 28 coins with certificates and QR-page concepts
- `design/economy/legacy_vault_cards.md` — 12 NFT cards plus the FuncoLand relic
- `design/economy/icq_airdrops.md` — 12 airdrop messages
- Engine brewery tracker rebuilt from author canon (12 breweries, bare snake_case IDs)
- `Absynthium` → `Absinthium` corrected repo-wide including a scene-file rename

**Settled rulings this window produced (do not relitigate):**

- Publandia's NFT roster is FINAL at 4; the "poker pot" acquisition is struck
- The tractor NFT keeps BOTH `Edition 1 of 1` and `Mint #42` — the contradiction is deliberate
- FuncoLand is ONE holding (the Vault card is the display layer for `funcoland_futures_nft.json`)
- `SuperKoruna Value Hypermarket` → `SuperSovs Value Hypermarket`
- The Legacy Vault first-open modal uses the FULL text (the "early Basquiats" version)
- The brands question is CLOSED — keep all; no brands round will ever run

**Open after the cards are written:**

- A reviewer pass over the whole Round 5 batch — it never ran; the round paused for the reorg
- QR joke-pages for the 28 shitcoins are DESIGNED but not built or hosted (production, ledgered)
- Publandia NFT #4 "America Online" is sited at The Craic Tax, jukebox track 47

---

## 6. FIRST ACTIONS FOR THE CLOUD AGENT

1. Run `git log --oneline -15` and read `docs/superpowers/NEXT_WORK.md`. The repo moves fast
   across windows — assume canon has changed since this document was written.
2. Confirm the seven slots are still empty: `grep -rc "AUTHOR TO WRITE" design/`
3. Greet the author, state which worktree you are (`nft-vault-copy`), and present **NFT #1 —
   The Millennium Bug** for their copy. One at a time. Do not draft it for them.
4. When copy arrives: apply it verbatim to every file rostering that NFT, then verify with a
   byte-exact `grep -F` on each string before reporting done.

**The author is on a borrowed machine for roughly ten days. Keep turns tight, batch questions,
and never make them re-explain a ruling that is already written down here.**
