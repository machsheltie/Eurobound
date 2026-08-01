# Wallet UI — The Legacy Vault & Bagholder Assets

**Status:** Design, Round 5. Derived from `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §2 (author-locked) under the Round 5 plan, Lane E.
**Owns:** wallet shell, both asset tabs, first-open modal placement, reveal trigger and choreography, card layout and anatomy.
**Does not own:** card *content* for specific NFTs and relics (see `design/economy/legacy_vault_cards.md`); coin and certificate content (see `design/economy/shitcoin_master_pool.md`); economy mechanics (see `design/economy/economy_system.md`).

---

## 0. Voice Contract

**The wallet never winks.** It is the most sincere object in the game.

Every surface in this UI treats a 128-pixel JPEG of milk foam with the reverence a national gallery gives a Vermeer. There is no ironic frame, no tooltip that undercuts, no "estimated value (lol)", no greyed-out disclaimer that lets the player off the hook. The gold is real gold-leaf treatment. The seals are properly embossed. The typography is expensive. Nothing in this interface has ever heard the word "grift."

If an artist or writer is ever tempted to add one small signal that the game is aware — a slightly-too-large font, a wobble on a serious word, a wink of any kind — that is the failure state of this document.

---

## 1. Wallet Shell

### 1.1 Entry

The wallet is a full-screen menu panel reachable from the pause/inventory menu. It is *not* the inventory — inventory is gear and consumables; the wallet is **assets**. The distinction matters to the bros enormously and is never explained to the player.

### 1.2 Header (persistent, both tabs)

```
SOVS                                    € [balance]
```

- Ticker label reads `SOVS`. The balance reads with the `€` glyph (per `economy_system.md` §1.3).
- Monospaced numerals, right-aligned, no animation on change beyond a single-frame value swap. The official currency does not get excited.
- No fee line. No pending line. No network status. Ever.

### 1.3 Tab strip

- **At game start the tab strip renders a single tab: `THE LEGACY VAULT`.** It reads as a section title, not as a tab — no empty second slot, no locked pill, no ghosted label, no "???", no divider hinting at a neighbour.
- After the reveal (§3) the strip becomes two tabs and behaves as a normal strip.
- The strip must be built so that adding the second tab is a layout *change*, not an unhide. If a QA player can find a hidden node in the scene tree before the trigger, the reveal is compromised.

---

## 2. TAB 1 — "The Legacy Vault"

**Unlocked from game start.** This is the wallet the party is proud of.

### 2.1 Aesthetic direction (artist-facing)

**Concept:** a private museum gallery installed inside a delusion. High-society curation applied, without a shred of hesitation, to garbage.

| Element | Treatment |
|---|---|
| Background | Deep warm charcoal to near-black, subtle vertical gradient. Gallery-wall texture at very low contrast — a faint plaster tooth, never a pattern. |
| Lighting | Soft top-down pool lights per card. Each frame catches a gentle specular bloom along its upper bevel. Cards not under the cursor sit ~15% dimmer. |
| Frames | Individually lit card frames with a milled bevel and a hairline inner mat. The mat is cream. The frame edge is brushed dark bronze with a thin gold fillet. |
| Seal | Gold-accented **"Provenance Verified"** seal, wax-medallion silhouette with an embossed rim, bottom-right of every card. Real specular highlight; it should look pressed, not printed. |
| Typography | Display serif for titles and the Vault name; a high-quality humanist sans for labels; monospace for figures. Generous letter-spacing on small caps labels. |
| Palette | Charcoal, cream, aged gold, one muted oxblood accent for figures. No neon anywhere in this tab. |
| Motion | Slow. Card hover raises 2–3px over ~180ms with an eased curve. No bounce, no pop, no confetti, no sparkle. |
| Audio | A soft felt-lined *thunk* on card select; a low room-tone bed with the barely-audible hum of gallery HVAC. No coin sounds. No chimes. |

The single most important art note: **the frames are more expensive than the art inside them, and the UI does not know that.**

### 2.2 First-open modal — AUTHOR-LOCKED, VERBATIM

Shown **once**, on the first time the player opens the wallet. Gated by `legacy_vault_seen_intro`.

> **REPRODUCE EXACTLY. Do not trim, re-punctuate, retitle, or "improve" one character of this block.**

```
WELCOME TO THE LEGACY VAULT
Generational Wealth in JPEG Form

Every image in this vault has been carefully curated for long-term cultural and financial appreciation. In twenty years, scholars will view this portfolio the same way we view early Basquiats. We are early. Painfully early. And that is exactly where you want to be.
```

**Presentation:** centred on a dimmed gallery background, cream-on-charcoal, display serif for the title, small caps for the sub-line, body set at reading size with wide leading. A single dismiss affordance with a neutral label. No skip prompt, no "don't show again" checkbox — it shows once and the game does not negotiate about it.

**Timing:** the modal holds until dismissed. No auto-advance. The party is not in a hurry about generational wealth.

**Copy status (resolved, author ruling 2026-08-01):** the `…` after `curated` in the source spec was a transcription elision, not authorial punctuation. The author has supplied the complete body copy and it is reproduced above in full, verbatim. The body is a single unbroken paragraph and ships as one string — the line break in the block above exists only to separate the two headers from the body. Nothing in this modal is a placeholder any more; it is closed and locked.

### 2.3 Permanent sub-header — AUTHOR-LOCKED, VERBATIM

Sits directly beneath the tab title, on every visit, forever. It is never dismissible, never collapsible, and never explained.

```
Portfolio Thesis: Undervalued Nostalgia + Scarcity = Inevitable Upside
```

Set in small caps or italic display serif, centred under the title, in the muted gold accent. It reads as a gallery's mission statement engraved above a doorway. It is stated with complete confidence and no supporting evidence, which is exactly how a mission statement works.

### 2.4 Progress counter — AUTHOR-LOCKED FORMAT, VERBATIM

```
[N of ∞] The Legacy Vault Secured
```

- `N` is substituted with `legacy_vault_secured_count` — the number of Vault entries acquired. Nothing else in the string ever changes.
- The denominator is **∞**. It is always ∞. It never resolves, never converts to 12, never turns into a percentage, and no character or system ever remarks on it.
- The counter increments with a plain value swap. No completion fanfare, no "collection complete" state — completion is not a concept the Vault entertains.
- Placement: right-aligned on the tab header line, or centred beneath the Portfolio Thesis; either is acceptable, both are permanent.

### 2.5 Vault card anatomy

Cards render in a gallery grid — 2 or 3 columns depending on aspect — with generous gutters. Every card carries **all four** of the following. A card missing any of them is incomplete.

```
┌───────────────────────────────────────────┐
│  ╭─────────────────────────────────────╮  │
│  │                                     │  │   ← ARTWORK PLATE
│  │        [the actual JPEG/GIF]        │  │     presented at native
│  │                                     │  │     resolution, centred in
│  ╰─────────────────────────────────────╯  │     the mat, never upscaled
│                                           │     to hide its quality
│  TITLE OF THE PIECE                       │
│  ─────────────────────────────────────    │
│  EDITION            │  1 of 1             │   ← 1. EDITION TAG
│  ESTIMATED FUTURE   │  ████████           │   ← 2. ESTIMATED FUTURE VALUE
│  VALUE              │                     │
│                                           │
│  COLLECTOR'S NOTE                         │   ← 3. COLLECTOR'S NOTE
│  " ...................................... │
│    ...................................... │
│                                           │
│  ACQUISITION                              │   ← 4. ACQUISITION STORY
│  " ...................................... │
│    ...................................... │
│                                    ⊙      │   ← "Provenance Verified" seal
└───────────────────────────────────────────┘
```

| # | Field | Rules |
|---|---|---|
| 1 | **Edition tag** | Small caps label, monospace value. `1 of 1`, `Mint #42`, `Limited Drop`, `Pre-2005 Retail Artifact`. Scarcity is asserted flatly and never justified. |
| 2 | **Estimated Future Value** | Always absurdly bullish. Renders as a figure, a redacted block, or a sentence — whatever the entry specifies. The canonical redacted form is `████████ (Loading… still loading… extremely bullish)`. Presented in the same typographic weight a real valuation would get. **No disclaimer. No asterisk. No "estimate only" footnote.** |
| 3 | **Collector's Note** | One to three sentences of solemn curatorial assessment, in the register of an auction catalogue. Discusses composition, cultural moment, and rarity of a file someone made in MS Paint. |
| 4 | **Acquisition Story** | Over-serious provenance. How the piece entered the collection, told the way a museum tells you how it got the Rembrandt. Canonical example, author-locked: *"Gifted by Aaron the Unflappable after drunkenly losing to his god-tier pocket kings. Can you FEEL IT?"* |

**Artwork plate rule (binding):** the art is displayed honestly. Low-resolution pieces stay low-resolution, aliasing intact, JPEG artefacts visible, checkerboard transparency preserved where canon says it is visible. The frame does not crop, smooth, upscale, or flatter the file. The gap between the frame's quality and the file's quality is the entire visual joke and it only works if neither side is adjusted.

**Audio pieces:** entries that are sound rather than image (e.g. the Publandia audio NFT) use a waveform plate in place of the artwork plate — a static rendered waveform in the same mat, with a playback affordance. Treated as fine art with no change in register whatsoever.

### 2.6 Detail view

Selecting a card opens a full-panel detail: enlarged artwork plate, all four fields at reading size, seal rendered at full detail. Left/right navigation between entries. Exit returns to the grid at the same scroll position.

No share button. No "value history" graph. No market data of any kind — the Vault is above markets; it deals in *legacy*.

---

## 3. TAB 2 — "Bagholder Assets"

### 3.1 Hidden at game start (binding)

Before the trigger fires, the Bagholder Assets tab **does not exist in the interface.**

- It does not render.
- There is **no empty stub**, no locked tab, no greyed pill, no placeholder label, no "Coming soon", no tooltip explaining how to unlock it.
- Nothing anywhere in the game hints that a second tab is possible. No NPC mentions it. No tutorial references it. No menu help text lists it.
- The player's first knowledge that the wallet has two tabs arrives at the moment of reveal.

### 3.2 Reveal trigger

Strictly ordered. All three steps, in sequence, in the same encounter:

1. The player is **rug-pulled** at a back-alley vendor (`economy_system.md` §5).
2. The kiosk prints and the player **receives a Vault Certificate** for the dead coin.
3. The player selects **"Inspect"** on that certificate.

→ set `has_inspected_first_crypto_trash = true` → the tab **permanently reveals.**

Notes:

- The trigger is the *inspection*, not the rug. A player who ignores the certificate keeps a one-tab wallet. Curiosity is the key.
- Once true, the flag never resets, and the tab never hides again — even if the player somehow ends up holding nothing.
- Only the first inspection triggers it. Subsequent certificates are just items.

### 3.3 Reveal choreography (~3 seconds)

The reveal is **subtle**. This is not a fanfare moment; it is an administrative one.

| Beat | Timing | Content |
|---|---|---|
| 1 | 0.0s | Tab strip reflows from one tab to two. Quiet, no flourish — a soft ease over ~250ms, as though the tab had always been loading. |
| 2 | ~0.3s | A small badge appears on the new tab. Understated: a single unobtrusive marker, no colour scream, no bounce. |
| 3 | ~0.4s–3.0s | **Party reaction line**, one line, ~3 seconds on screen, in the party's normal dialogue presentation. Delivered as good news. |

**Party reaction rules:**

- The line treats the appearance of a folder for worthless junk as an **achievement, a graduation, or an institutional milestone.** Diversification. A second portfolio. A dedicated wing.
- It is never suspicious, never rueful, never a punchline about being scammed.
- It plays **exactly once**, gated by `bagholder_reveal_played`.
- No narrator line accompanies it. No UI tooltip explains the new tab. The player figures out what it holds by opening it.

**DRAFT candidate lines** *(in-register; author veto at review — the register, not any specific line, is what this document locks):*

- "Two portfolios. That's diversification, bro."
- "We needed a second wing. The Vault was getting crowded."
- "This is what a real firm looks like, Chadwick."

### 3.4 Contents

Bagholder Assets houses physicalized crypto trash:

- **Dead paper Vault Certificates** — one per rugged coin, high-gloss laminated cardstock with the dead QR printed on the asset.
- **$SPANK tokens** and other physical token junk.
- **ICQ airdrop deposits** — 0-value junk coins arriving passively (see `design/economy/icq_airdrops.md`).

### 3.5 Aesthetic direction (artist-facing)

The visual inverse of the Vault — and, crucially, **not a "joke" style.** It is the honest style. This tab is what the assets actually look like when nobody has framed them.

| Element | Treatment |
|---|---|
| Background | Flat neutral grey. No gradient, no texture, no lighting. |
| Layout | A dense list or utilitarian tile grid. Tight rows, thin dividers, no gutters worth the name. Scrollbar visible. |
| Items | Photographed flat, top-down, on the grey. Certificates show their laminate sheen and their fingerprints. Nothing is lit. Nothing is centred with love. |
| Typography | System sans throughout. Small. Left-aligned. No small caps, no serif, no gold. |
| Data shown | Quantity and denomination, stated plainly. `100,000 $SPANK`. `Vault Certificate — RugPullInu`. Value is shown as `$0.00` where a value field exists, with no commentary. |
| Motion | None. Rows do not hover-lift. Nothing animates. |
| Audio | Nothing. Silence in this tab is a deliberate contrast to the Vault's room tone. |

**The `$0.00` rule:** where a value renders, it renders `$0.00`, flatly, in the same grey as everything else. No red. No strikethrough. No sad-trombone. The interface has no opinion.

### 3.6 The contrast is a design note, not a line of dialogue (binding)

Two tabs sit side by side: one folder of scams they got rugged on, one folder of nostalgia bait they believe is high art — and they are, materially, the same category of object presented two different ways.

**No character in the game ever says this out loud.** No narrator, no NPC, no bro, no tooltip, no achievement text, no item description. The player is trusted to see it. If any line of shipped copy articulates this observation, that line is a defect (Trust the Player, §1a).

---

## 4. Engine Requirements

### 4.1 Flags consumed

| Flag | Owner | Wallet use |
|---|---|---|
| `legacy_vault_seen_intro` | wallet | Gates the first-open modal to one showing |
| `legacy_vault_secured_count` | economy | Substituted into `[N of ∞] The Legacy Vault Secured` |
| `has_inspected_first_crypto_trash` | economy | **Gates Tab 2 existence.** Wallet must read this at panel construction, not at panel show. |
| `bagholder_reveal_played` | wallet | Gates the 3-second party reaction to one playing |
| `vault_certificates_owned` | economy | Populates Bagholder Assets certificate rows |
| `sovs_balance` | economy | Header balance, rendered with `€`, labelled `SOVS` |

Flag definitions and defaults are canonical in `design/economy/economy_system.md` §8.2.

### 4.2 Construction rules

- Tab 2's scene subtree is **instantiated only when `has_inspected_first_crypto_trash` is true.** It is not built-and-hidden. A hidden-but-present node is a datamining leak and a QA leak.
- The tab strip is a layout container that takes its children from a runtime list, not a hand-placed pair of buttons.
- The Vault grid is data-driven from the Vault entry table (content in `legacy_vault_cards.md`); adding an entry must require no scene edits.

### 4.3 Card data contract

Each Vault entry supplies, at minimum:

```
id                : String
title             : String
media_type        : enum { IMAGE, ANIMATED, AUDIO }
media_path        : String        # rendered honestly, never upscaled or smoothed
edition_tag       : String
future_value      : String        # rich text; may contain block glyphs (████████)
collectors_note   : String
acquisition_story : String
```

`future_value` must support the redacted-block form and inline ellipses without the text renderer normalizing them. Verify `████████` (U+2588) and `…` (U+2026) render in the shipped font before locking the font choice.

### 4.4 Localization note

The author-locked strings in §2.2, §2.3, and §2.4 ship as **fixed English copy**. `[N of ∞] The Legacy Vault Secured` uses positional substitution for `N` only; the `∞` is part of the literal and must not be treated as a numeric token by any formatter.

---

## 5. Accessibility

- Card text meets contrast minimums against the cream mat — the gallery is dim, the *text* is not.
- The `████████` redaction form must have an equivalent for screen readers: read the field's literal string, including the parenthetical, exactly as written. Do not substitute a description of the blocks.
- The 3-second party reaction respects the global text-speed and hold-duration settings; if hold-forever is enabled, it waits for input.
- The Bagholder Assets grey palette must still clear contrast minimums despite being deliberately drab. Drab is a style; illegible is a bug.

---

## 6. Open Items / Escalations

1. ~~**First-open modal ellipsis (blocking for final copy).**~~ **RESOLVED — author ruling 2026-08-01.** The ellipsis was an elision; the full author copy is now in §2.2 and the copy hold is lifted. No open question remains on this modal.
2. **Party reaction line for the Tab 2 reveal.** Register is locked by this doc; the specific line is DRAFT pending author selection (§3.3).
3. **Progress counter placement.** Two acceptable placements offered (§2.4); final pick is an art/layout call, not a canon call.

## 7. Cross-References

- Economy mechanics, flags, seed, rug logic → `design/economy/economy_system.md`
- Vault card content for the 12 NFTs + FuncoLand relic → `design/economy/legacy_vault_cards.md`
- Coins, certificates, QR pages, terminal copy → `design/economy/shitcoin_master_pool.md`
- Airdrop delivery into Bagholder Assets → `design/economy/icq_airdrops.md`
- Source spec → `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §2
