# Economy System — Sovereign-X (SOVS), the Back Alley, and the Kiosks

**Status:** Design, Round 5. Derived from `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` (author-locked §1, §3, §5) under the Round 5 plan, Lane E.
**Owns:** currency canon, the 90/10 split, kiosk terminals, rug-pull math, wiki-proofing, roster rotation, engine contract.
**Related docs:** `design/economy/wallet_ui.md` (both wallet tabs), `design/economy/icq_airdrops.md` (passive junk delivery), `design/economy/shitcoin_master_pool.md` (the coins themselves), `design/economy/legacy_vault_cards.md` (Vault card content).

---

## 0. Voice Contract (binding, applies to every line of copy in this system)

Three rules govern every string the economy system can put on screen. They are not stylistic preferences.

1. **The game never winks.** No tooltip, no narrator aside, no NPC line, no loading hint, no achievement name may signal that any of this is satire. There is no ironic quotation mark, no knowing pause, no "well, THAT happened." The interface is sincere. The bros are sincere. The sincerity is the comedy; explaining it kills it.
2. **The bros are never scam-aware, even mid-rug.** A token hitting $0.00 in transit is a market correction, a liquidity event, a shakeout of weak hands, a healthy consolidation. It is never a scam and it is never their fault. They do not learn. There is no arc where they wise up.
3. **Sellers and scammers always know exactly what they have.** The kiosk operators, the back-alley vendors, and the ICQ senders are not deluded — they are working. Their copy is confident sales language, not confession. Only the party is fooled.

Corollary for writers: if a line would make a player think "the game knows this is dumb," cut it.

---

## 1. Sovereign-X (SOVS)

### 1.1 What it is

**Sovereign-X**, ticker **SOVS**, is the single continent-wide official digital fiat-crypto. It handles roughly **90% of all standard transactions** in the game: train and ferry tickets, hostel and hotel lodging, doctors and pharmacies, tips, cover charges, food, taxis, laundry, admission, most shops.

It is *officially* a currency. It is *actually* the end state of a financial system that spent twenty years adding layers and never removed one. Nobody remembers who Sovereign-X was named after. The onboarding pamphlet has a foreword.

### 1.2 Tone: high-society pretension meets sterile bureaucracy

SOVS presentation should read like a private bank that was nationalized by a standards committee. Two registers, always both at once:

| Pretension layer | Bureaucratic layer |
|---|---|
| Serif capitals, hairline gold rules, "Sovereign" used as an honorific | Form numbers, revision dates, "Schedule 4(b)" |
| "Your Instrument", "the Bearer", "the Sovereign Holder" | "Transaction reference", "Instrument Class", "Ledger Segment" |
| Muted navy/cream palette, embossed seal motifs | Non-negotiable grey, no animation, monospaced numerals |
| Receipts printed on paper stock too nice for a kebab | Receipts that cite an ordinance nobody has read |

It is never *funny on purpose*. It is funny because it is extremely serious about a currency the party spends on shots.

### 1.3 Notation — SUPERSEDED BY AUTHOR RULING (2026-08-01)

> **⚠️ The former "the euro sign is SOVS's display glyph" rule is DEAD. It was overridden by direct author ruling on 2026-08-01:**
> *"Every. Country. Operates. On. Sovs. Not euros. We do not deal with exchanges of currency between areas. The whole game? Sovs."*

**The euro sign does not appear anywhere in the game.** Not as a glyph, not as a display convention, not in world text, not in the wallet, not as a commissioned sprite. `_sorting/Design/Economy/currency.md` is the only file in the repo permitted to render the forbidden forms, and only to name them.

- Prices in world text, item files, shop tables, dialogue and UI read **`40 Sovs`** (prose) or **`40 SOVS`** (signage, menus, price boards, all-caps contexts). Singular is `1 Sov` / `1 SOV`.
- **The repo-wide retrofit has been executed** (2026-08-01): 4,215 conversions across 330 files. The previous rule forbidding it no longer applies.
- **Writers add prices in Sovs.** Never author a euro sign, `EUR`, or "euro(s)" as money.
- **The symbol is the word. There is no Sov glyph.** Art specs must letter `SOVS`, never commission a currency mark. Price tiers use `S` / `SS` / `SSS` (cheap / mid / expensive) — see §1.3a.
- Full canon: `_sorting/Design/Economy/currency.md`.

**Koruna does not exist.** This is not a real continent and there is no koruna. Any surviving koruna/Kč reference is a defect (Lane R owns elimination). The same now applies to euros.

**Koruna does not exist.** This is not a real continent and there is no koruna. Any surviving koruna/Kč reference is a defect (Lane R owns elimination).

### 1.3a Price-tier marks (binding — art and UI)

Some shops rank goods by expense rather than printing a figure (bargain-bin tags, menu boards, market stalls). Because there is no currency glyph, tiers are lettered:

| Tier | Mark | Reads as |
|---|---|---|
| Cheap | `S` | one Sov-capital |
| Mid | `SS` | two |
| Expensive | `SSS` | three |

- Block capitals in the location's own display face; no coin art, no pips, no repeated symbol.
- Three capitals fit a 32x32 sprite cell at ~8px per character. A tier tag never needs more than 32x32.
- **A tier mark is not a price.** Where an exact figure is shown it is always `N SOVS` in full.

### 1.4 No friction on routine purchases (binding rule)

Core transactions are **clean, frictionless, and predictable**. SOVS is the boring part of the joke and it must stay boring.

Explicitly forbidden on any SOVS purchase:

- gas fees, network fees, priority fees, or any deducted surcharge
- confirmation delays, pending states, spinners, block-height counters
- slippage warnings, failed transactions, "insufficient gas" errors
- randomized price wobble at the point of sale
- any minigame, prompt, or button-mash to complete a payment

A SOVS purchase is: select, pay, done. If a build introduces friction here, that is a bug, not flavor. **All volatility lives in the back alley, never in the shop.**

---

## 2. The 90/10 Split

| Segment | Share | Currency | Where |
|---|---|---|---|
| **Official economy** | ~90% | SOVS | Shops, transit, lodging, clinics, venues, restaurants, licensed vendors, tips |
| **Back-alley economy** | ~10% | Volatile darknet shitcoins | Off-grid vendors in alleys, service corridors, basements, unlisted stalls, after-hours markets |

The 10% is not a shop tier — it is a *parallel* market with different goods. Back-alley vendors do not sell better potions. They sell things the official economy will not carry at all: exclusive, overpowered, or progress-skipping items (Gold-Thread Fanny Pack, VIP Backstage Pass, Illegal Energy Drinks; full win-catalog in `shitcoin_master_pool.md`).

This is the entire structural reason the party ever touches a shitcoin. The best gear in the game is behind a payment rail that eats 65% of what you put into it, and the party considers this a reasonable arrangement.

---

## 3. Back-Alley Vendors

### 3.1 They refuse SOVS

Every back-alley vendor rejects SOVS, and every one of them gives the same reason:

> **"accounts frozen by EU regulators"** *(author-locked phrasing — the stated cause is always regulatory, never criminal)*

Each vendor delivers this in their own voice, but the cause never changes and is never elaborated. It is stated the way people state the weather. No vendor jokes about it, winks about it, or acknowledges that it might be untrue.

**Do not write a vendor who explains their real reason.** There is no reveal. The line is the line.

### 3.2 Vendors are honest

This is the load-bearing detail of the whole system and it is easy to get wrong.

**Back-alley vendors genuinely want to complete the sale.** They have the goods. They will hand them over. They are not running the scam — they are downstream of it, and a dead coin costs them a sale they wanted to make. A vendor whose customer's token dies is *annoyed*, not smug.

- Vendors never gloat over a rug.
- Vendors never rug the player themselves.
- Vendors are entitled to be irritated, bored, or unsympathetic. They are not entitled to be in on it.
- The scam lives on-chain, in transit, between the kiosk and the counter — a place with no face attached to it.

### 3.3 Placement

Back-alley vendors are always paired with an exchange kiosk within sight. The kiosk is the on-ramp; the vendor is the counter. The walk between them is where the money dies.

City-level pairing flavor (which coins haunt which alleys) is documented per-coin in `shitcoin_master_pool.md`. It is **flavor only — no hard gating.** Any coin can appear on any roster.

---

## 4. Exchange Kiosks

Two terminal brands operate the on-ramp. They are physically distinct machines and should read as competing products from the same sad industry.

### 4.1 Broke-ATM

A converted cash machine. Beige plastic gone yellow, a numeric keypad with three worn keys, a monochrome or low-color screen, a receipt slot, and a laminated card slot that dispenses **Vault Certificates**. Bolted to masonry at an angle nobody chose. Hum audible from three metres.

### 4.2 QuickRug24

Newer, worse. A slim upright with an oversized glossy touch panel, an aggressive backlight, and animated promotional banners along the top bezel. Advertises 24-hour availability on a machine that is frequently mid-reboot. The touch layer is calibrated about four millimetres off.

### 4.3 Shared terminal behaviour

Both machines do the same three things:

1. **Display the active roster** — a clean, professional ticker of **7–8 coins** drawn from the master pool, with names, prices, and 24h deltas.
2. **Sell tokens for SOVS** — a straightforward exchange. This step *always succeeds*. Buying the coin is never the failure point.
3. **Print** — a receipt on success at the vendor counter; a **Vault Certificate** on a rug.

The ticker presentation is deliberately competent: aligned columns, monospaced numerals, green and red deltas, a timestamp. It looks like real market data. It is real market data about nothing. Terminal UI copy, ticker layout details, and per-brand voice live in `shitcoin_master_pool.md`.

**The ticker never leaks the truth.** See §6.

---

## 5. Transaction Resolution — the 35/65

### 5.1 The distribution (author-locked)

> **35% success / 65% rug.**

### 5.2 Sequence of a back-alley purchase

1. Player approaches the kiosk, buys a token from the active roster with SOVS. **Always succeeds.** No roll here.
2. Player walks to the vendor and selects goods. Vendor quotes a price in that token. Vendor is cooperative.
3. Player confirms payment. **The roll executes here, at the moment of payment.**
4. **Success (35%)** — the transaction clears. Vendor hands over the item. No fanfare, no congratulation, no "lucky!" from anyone. The bros are not surprised; they expected this, because they are geniuses. Play it completely straight.
5. **Rug (65%)** — the token hits **$0.00 exactly as the player pays.** Not before. Not while browsing. On the confirm.
   - The vendor refuses the dead coin. Goods stay on the counter. The vendor's reaction is a working person's reaction to a declined card.
   - **Instant bro coping line**, no beat of silence between the price hitting zero and the line landing:
     > **"It's just a market correction, Chadwick! Diamond hands!"** *(author-locked, verbatim)*
   - The kiosk prints a **Vault Certificate** for the dead coin — a high-gloss laminated paper wallet on cardstock, guaranteeing ownership of worthless tokens, with a dead QR code printed on the asset. The player receives it as a physical collectible item.
   - The SOVS spent is gone. There is no refund, no partial recovery, no pity mechanic.

### 5.3 Coping is a pool, not a line

The author-locked line above is the canonical anchor and must appear verbatim wherever it is used. Additional coping lines may be written for variety **only in the same register**: diagnosis-free, blame-free, forward-looking, financially literate in vocabulary and illiterate in substance.

Permitted register: consolidation, shakeout, weak hands, entry point, accumulation zone, healthy pullback, we're early.
**Forbidden register:** anything that recognizes theft, fraud, a scam, a pattern, a mistake, or a lesson. The bros have never been rugged before, every time.

Speaker attribution for the anchor line is unassigned in source (it addresses Chadwick) — see §9 Open Items.

### 5.4 Failure is not punishment

A rug costs SOVS and returns a collectible. Design it as a *transaction*, not a penalty:

- No stat loss, no debuff, no morale hit, no failure sting.
- The Vault Certificate is a real item with real presence in the wallet.
- The first rug is a system unlock, not a setback — it is the gateway to the second wallet tab (see `wallet_ui.md` §3).

---

## 6. Wiki-Proofing (three layers)

Goal: no player, wiki, spreadsheet, or datamined table can produce a reliable "which coins pay out" answer. Every layer must hold independently; together they make the question unanswerable.

### Layer A — Per-save seed

At new-game, generate and store `economy_seed`. Each coin derives a stable **per-save reliability** from `hash(economy_seed, coin_id)`.

- A coin that pays reliably on one save is effectively a **100% scam on another**.
- Reliability values are drawn so that the **pool mean is exactly 0.35**, preserving the author-locked 35/65 across a playthrough while scattering it unrecognizably across coins.
- Reliability is **never displayed, never hinted at, never inferable from any in-game text**. No NPC has an opinion about which coins are good. No rumour system leaks it.

### Layer B — Live randomized market board

The kiosk roster and its displayed prices/deltas reshuffle on the triggers in §7.

- Displayed price, 24h delta, volume, and any other market cosmetic are **fully decorrelated from reliability.** A coin at +900% is exactly as likely to rug as one at −80%.
- Roster membership is likewise decorrelated. Being on the board means nothing.
- The board is beautiful, detailed, updates convincingly, and carries zero information.

### Layer C — Roll at payment

The 35/65 roll fires **at the moment of payment at the vendor counter**, not at purchase, not on roster generation, not on save load.

- Mechanically this mimics a liquidity drain: the money was fine until someone tried to move it.
- It also means save-scumming the kiosk purchase teaches nothing, and reloading before payment re-rolls.

**Anti-leak checklist for implementers:** reliability must not appear in save data in plaintext under a readable key; must not be logged; must not affect ticker rendering, sound, particle, or shader state; must not alter vendor dialogue selection before the roll resolves.

---

## 7. Roster Rotation

The active roster is **7–8 coins** drawn from the 25–30 coin master pool.

**Reshuffle triggers (author-locked):**

1. **Major zone transition** — entering a new city or a distinct major district, not every doorway.
2. **Hostel/hotel rest** — any full rest that advances time.
3. **Major story or side-quest beat completion** — main-story chapter beats and completed side-quests, not incidental objectives.

Rules:

- Rotation replaces the *whole* board, not individual rows. Coins may repeat across rotations; there is no cooldown or exclusion list.
- Rotation is **silent**. No "the market has changed!" prompt, no notification, no NPC comment. The board is simply different when the party comes back, exactly as a real market board would be.
- Rotation never alters per-save reliability (Layer A). The same coin carries the same reliability all playthrough, whether or not it is currently listed.
- Vault Certificates already held are unaffected by rotation. Dead is permanent.

---

## 8. Engine Requirements

Implementation contract for the Godot session. Names are proposals; behaviour is not.

### 8.1 Seed architecture

```
economy_seed : int                  # generated once at new-game, persisted in save, never regenerated
coin_reliability(coin_id) -> float  # deterministic: hash(economy_seed, coin_id) -> [0.0, 1.0]
                                    # distribution normalized so pool mean == 0.35
```

- `economy_seed` must survive save/load and must not be exposed in any debug overlay shipped to players.
- `coin_reliability` is computed on demand, not stored per-coin in the save file (reduces datamining surface).
- Transaction resolution: `success = rng_transaction.randf() < coin_reliability(coin_id)`, evaluated **only** inside the payment-confirm handler.
- `rng_transaction` is a separate RNG stream from cosmetic/market RNG so that observing the board cannot desync-predict the roll.

### 8.2 State flags

| Flag | Type | Default | Purpose |
|---|---|---|---|
| `economy_seed` | int | generated | Layer A root |
| `active_coin_roster` | Array[String] | generated | 7–8 coin IDs currently on the board |
| `roster_rotation_count` | int | 0 | Increments per reshuffle; drives cosmetic market history |
| `has_inspected_first_crypto_trash` | bool | `false` | **Gates the Bagholder Assets tab.** Set true the first time the player is rug-pulled, receives a Vault Certificate, and selects **Inspect** on it. All three conditions, in that order. Once true, never resets. |
| `bagholder_reveal_played` | bool | `false` | Ensures the 3-second party reaction on tab reveal plays exactly once |
| `legacy_vault_seen_intro` | bool | `false` | Gates the first-open Legacy Vault modal to a single showing |
| `legacy_vault_secured_count` | int | 0 | Feeds the `[N of ∞]` progress counter (see `wallet_ui.md`) |
| `vault_certificates_owned` | Array | `[]` | Dead-coin certificates held; each entry carries `coin_id` for asset/QR lookup |
| `sovs_balance` | int | starting value | Displayed as a bare numeral; the `SOVS` ticker label carries the unit. **No currency glyph — the symbol is the word.** |

### 8.3 Roster rotation hooks

Subscribe the roster manager to existing world signals; do not invent a polling timer.

| Hook | Fires on |
|---|---|
| `zone_transition_completed(zone_id)` | Major zone/city load finished |
| `rest_completed(location_id)` | Hostel/hotel rest resolved |
| `story_beat_completed(beat_id)` | Main-story chapter beat |
| `sidequest_completed(quest_id)` | Side-quest marked complete |

All four call the same `reshuffle_active_roster()`. Reshuffle is idempotent per frame — two triggers in the same frame produce one reshuffle, not two.

### 8.4 Transaction API constraints

- `purchase_token(coin_id, sovs_amount)` — **cannot fail**. No roll, no fee, no delay.
- `pay_vendor(vendor_id, coin_id)` — contains the *only* call site of the 35/65 roll.
- SOVS purchase path (`purchase_sovs(item_id)`) must expose **no** fee field, pending state, or failure return. If the shop UI has a fee row in its scene tree, delete the row.

### 8.5 Asset/print hooks

- On rug: `print_vault_certificate(coin_id)` → grants item, pushes to `vault_certificates_owned`, and makes the certificate **Inspect**-able.
- Certificate art is per-coin (high-gloss laminated cardstock, dead QR printed on the asset). Art spec and QR-page concepts live in `shitcoin_master_pool.md`.
- Building and hosting the real QR web pages is **production work, explicitly out of scope this round** and ledgered.

---

## 9. Open Items / Escalations

1. **Coping-line speaker attribution.** `"It's just a market correction, Chadwick! Diamond hands!"` addresses Chadwick, so the speaker is one of the other two. Source does not assign it. Needs an author ruling before VO/dialogue implementation.
2. **Reliability distribution shape.** Pool mean is fixed at 0.35 by canon; the *spread* around that mean (how many coins per save land near-zero versus near-certain) is a tuning value with no author ruling. Proposed default: a wide spread so that most saves contain 1–2 "lucky" coins the player will never identify. Tuning, not canon.
3. **Vault Certificate stack behaviour.** Whether duplicate certificates for the same dead coin stack or list separately is unspecified. Recommend listing separately — the joke is quantity — but flagging rather than deciding.

## 10. Cross-References

- Wallet presentation, both tabs, reveal trigger, card layout → `design/economy/wallet_ui.md`
- Coin roster, certificate art, QR-page concepts, terminal copy, win catalog → `design/economy/shitcoin_master_pool.md`
- Legacy Vault card content for the 12-NFT collection + FuncoLand relic → `design/economy/legacy_vault_cards.md`
- Passive junk-coin delivery → `design/economy/icq_airdrops.md`
- Source spec → `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md`
