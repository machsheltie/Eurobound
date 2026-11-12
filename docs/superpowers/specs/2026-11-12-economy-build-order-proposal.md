# Economy Build Order Proposal (for author approval)

**Date:** 2026-11-12. **Bead:** Eurobound-u1m. **Status:** PROPOSAL. Nothing here is a ruling. The author asked: "Have an agent propose a build order for me to approve". Posted to the Eurobound Desk as `Eurobound-u1m-q1`.

**Rules in force:** all money is SOVS (`1 SOV`, `40 SOVS`); no euro glyph (`.claude/CLAUDE.md`; economy spec §1.2 superseded). No numbers, prices or copy are invented here: every figure is cited to a spec or left as an open item. Binding rules: `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §0a (no mascots; story and satire need author discussion first) and §7c (NFT art is 90s/00s pop culture).

**Limits of this survey:** the author of this document had no `bd` access, so the bead text and comments were not read, and bead ids are cited only where they appear in commit history or repo files (marked "verify"). Whether maps are in scope of u1m is unconfirmed; Phase 6 is conditional on that.

---

## 1. What exists today

| Area | State | Evidence |
|---|---|---|
| SOVS wallet | Built as a bare int. `new_game` sets 20; `grant_rewards` adds; save keeps `sovs` (legacy `gold` read). **No spend API, no insufficient-funds path.** | `game/core/game_state.gd:8,39,102-105,125` |
| Inventory | `add_item(id, count, max_stack)`, `use_item`. Dictionary of id to count. | `game/core/game_state.gd:7,72-93` |
| Flags | `set_flag` / `has_flag`; flag registry is documented, many entries marked NOT BUILT. | `game/assets/data/world_data/quest_flags.json` |
| Airdrop flags | `airdrops_delivered`, the deposit store, and the hard gate on `has_inspected_first_crypto_trash` are declared, not built. Deposit type "proposed", not ruled. | `quest_flags.json:53-64,126-129,774` |
| Shops data | Empty: `"shops": {}`. | `game/assets/data/world_data/Shops.json` |
| Arcade prize shop | Working ticket-currency shop, one-off, reads `key_items.json` `ticket_price`. Owned by the Absinthe Orchestrator; read only. It does not use SOVS and is not a template for the SOVS shop, but its stock/sort/cursor/notice pattern is a reference. | `game/worlds/debaucheryville/absinthe_arcade/prize_shop.gd:26-39` |
| Intoxicant prices | Two vapes carry `"price": {"coin": "huff", ...}`. Speedcakes 420 HUFF; Gushers amount null with bundles (2 for 690, 3 for 1000, 4 null). So the item schema already expects a coin-priced shop row, but no `$HUFF` coin exists in code. | `game/assets/data/items/consumables.json:31,53-58` |
| Quest runtime | `QuestLog` is a read-only registry derived from `GameState.flags` (`started_when` / `completed_when`). No tracking store, no reward grant, no step advancement. Quest data under `quests/` is two files. | `game/core/quest_log.gd:3-36`; `game/assets/data/quests/vip_wristbands.json`, `astronomical_cockup.json` |
| Design specs | Complete design set, none engine-built: `design/economy/` (economy_system, wallet_ui, shitcoin_master_pool, icq_airdrops, legacy_vault_cards, shoptypes, itemvalue, blackmarket, currency). | `design/economy/` |
| Engine contract | Seed, flags, roster hooks, transaction API all specified, none built. | `design/economy/economy_system.md` §8 |

Recent related work (verify bead ids with `bd`): Eurobound-fe10 and -t162 (overworld compulsions from status data), the consumable intoxicant fields proposal (`docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md`), and Eurobound-gmtu / -beb7 / -hg48 (flag fixes).

---

## 2. Principles for the order

1. Vertical slice first: one buyable thing, one rug pull, one airdrop, one quest reward, end to end, before breadth.
2. The SOVS path stays frictionless (`economy_system.md` §1.4, §8.4). The 35/65 roll lives in exactly one call site (`pay_vendor`).
3. Build against the data the specs already define; do not mint content to fill a gap. Gaps become author questions.
4. The hidden Bagholder tab is instantiated only after reveal (`wallet_ui.md` §252), so the wallet UI and the flag logic ship together.

---

## 3. Phases

### Phase 0: Economy core API (no UI)

- **Scope:** wallet operations on `GameState`: `can_afford`, `spend_sovs`, `grant_sovs`, a single failure-free SOVS purchase function with no fee, pending or failure field (`economy_system.md` §8.4). `economy_seed` generated at new game and saved. Coin-balance store for non-SOVS coins (`coin_id` to quantity, shape proposed in `quest_flags.json:126`). Save/load round trip for all of it.
- **Depends on:** `game_state.gd`; `economy_system.md` §8.1-8.2.
- **Unblocks:** every later phase.
- **Rulings needed:** (a) confirm the coin-balance and `bagholder_assets` shape (proposed, not ruled); (b) whether inventory stacking applies to Vault Certificates (see Phase 3).

### Phase 1: SOVS shop runtime (vertical slice part 1)

- **Scope:** data-driven shop screen reading `Shops.json`; rows from item data; buy, cannot-afford notice, inventory grant; one shop type first. Schema for `Shops.json` defined from `design/economy/shoptypes.md`. Validate through `tools/validate_data.py`. Use the Arcade `PrizeShop` as a UI pattern reference only; do not edit it.
- **Depends on:** Phase 0; `shoptypes.md`; `itemvalue.md`; `Shops.json` schema.
- **Unblocks:** Phases 2, 3 (kiosk shares item grant), 5 (rewards), city shop content.
- **Rulings needed:** which first shop is the slice (the author picks; not invented here); the actual shop stock and SOVS prices come from the author or the economy specs. This proposal sets none. `Shops.json` is empty, so every stock row is an open content question.

### Phase 2: Intoxicant HUFF price rows (small, optional bridge)

- **Scope:** let a shop row read `price.coin` / `price.amount` / `bundles` from `consumables.json`, so the two vapes can be sold. Stays inert for null amounts.
- **Depends on:** Phases 0-1; Phase 3 for `$HUFF` to exist as a coin.
- **Unblocks:** the vape shops; the compulsion and status work already merged.
- **Rulings needed:** every `amount: null` and the 4-bundle price are author numbers (`consumables.json:53-58`); `$HUFF` is not yet confirmed in the master pool as a purchasable coin or as a vendor currency. Check `shitcoin_master_pool.md` and ask.

### Phase 3: Crypto/NFT wallet (vertical slice part 2)

Split in three increments:

- **3a. Legacy Vault (Tab 1), available from game start.** Card frames, first-open modal (verbatim copy is locked, `wallet_ui.md` §2.2), `legacy_vault_seen_intro`, the `[N of ∞]` counter, cards from `legacy_vault_cards.md`. Seven cards have empty copy blocks that only the author may fill (spec §7c; `legacy_vault_cards.md` §7b): ship those as the specified empty frames, never filled by invention.
- **3b. Kiosks and the rug pull.** Coin pool loader from `shitcoin_master_pool.md`; seed-based reliability with pool mean exactly 0.35; active roster of 7-8 coins; reshuffle hooks (`zone_transition_completed`, `rest_completed`, `story_beat_completed`, `sidequest_completed`; confirm these signals exist or add them, since none was found in the survey); `purchase_token` (cannot fail) and `pay_vendor` (the only roll); certificate grant with Inspect; Bagholder Assets tab appears when `has_inspected_first_crypto_trash` is set, with the single-play reveal flag.
- **3c. ICQ airdrops.** Deliver through the ICQ window; one-shot via `airdrops_delivered`; gated on `has_inspected_first_crypto_trash` (`icq_airdrops.md` §1.3); deposit into Bagholder Assets; uniform pick from undelivered, stop when exhausted.
- **Depends on:** Phase 0; Phase 1 for kiosk-bought items; existing ICQ window and `icq_hotspot_messages.json`; the economy spec §2-§5.
- **Unblocks:** Phase 2 (HUFF), back-alley vendors, the real-world QR ARG hosting work (out of scope per spec §5/§8).
- **Rulings needed:** the open items below (coping-line speaker, reliability spread, certificate stacking, airdrop gating confirmation, reveal reaction line, counter placement).

### Phase 4: Back-alley vendors and kiosk content

- **Scope:** place vendors that refuse SOVS and accept coins (spec §1.4); win catalog items; kiosk terminal flavor from the pool. Content breadth, built on Phase 3b.
- **Depends on:** Phases 1, 3b; `blackmarket.md`.
- **Unblocks:** economy-side progression gates.
- **Rulings needed:** win-catalog items beyond the three named in spec §3 are Lane C proposals pending author veto; confirm the ruling status of each before adding.

### Phase 5: Quest runtime

- **Scope:** extend the flag-derived `QuestLog` with a completion hook that grants rewards (SOVS, items, coins) through Phase 0/1 functions, fires `sidequest_completed(quest_id)` for the roster reshuffle, and enforces one-time rewards. Load more quest data from the `quests/` folder into `quest_log.json` as the author supplies it. Keep derivation from flags (no second store) as the current design states (`quest_log.gd:3`).
- **Depends on:** Phase 0; Phase 3b hook for `sidequest_completed`; flag registry (`quest_flags.json`).
- **Unblocks:** quest content, side-quest rewards, Phase 3b roster rotation on quest beats.
- **Rulings needed:** reward amounts per quest come from each quest doc or the author; this proposal gives none. Quest structure changes need an author ruling (`.claude/CLAUDE.md`, "Ask the author first").

### Phase 6: Maps (conditional)

- **Scope:** only if u1m's bead text includes maps. The survey found no map-specific economy dependency; map and shop placement (where `Shops.json` shops and kiosks sit) follows city layouts already in `design/worlds/`.
- **Depends on:** Phases 1, 3b for what to place.
- **Rulings needed:** confirm with the author whether maps belong to this build order at all.

---

## 4. Slice definition (end of Phases 0, 1, 3a-3c, 5 minimum)

One city: one SOVS shop selling one item; one kiosk with a rug-pull that issues a certificate; the Bagholder reveal; one ICQ airdrop; one quest completing and paying out; Legacy Vault open with its cards. Everything saved and loaded.

## 5. Open in the economy spec (flagged, not decided)

1. Coping-line speaker attribution (`economy_system.md` §9.1; `icq_airdrops.md` §5.4). Blocks dialogue and VO.
2. Reliability distribution spread around the 0.35 mean (`economy_system.md` §9.2).
3. Vault Certificate stacking: separate rows or one row (`economy_system.md` §9.3; recommended separate, unruled).
4. Airdrops gated on the first Inspect: derived, not ruled (`icq_airdrops.md` §5.1).
5. Party reaction line for the Tab 2 reveal is a draft (`wallet_ui.md` §6.2); progress-counter placement is an art call (§6.3).
6. Airdrop reaction lines AD-02 to AD-12 are drafts; payload coin assignment is provisional (`icq_airdrops.md` §5.2-5.3).
7. Seven Legacy Vault cards await author copy and mint-number confirmation (`legacy_vault_cards.md` §7b).
8. `$TRASH` ticker name flagged for veto (`shitcoin_master_pool.md` §8.1).
9. Shop stock and SOVS prices: `Shops.json` is empty and no spec sets a shop-by-shop price list that this survey found. Prices need the author.
10. `$HUFF` coin: priced in `consumables.json` but not confirmed as a mapped coin; null prices and bundles need author numbers.
11. Deposit data shape (`coin_id` to quantity) is proposed only (`quest_flags.json:126`).
12. The four roster-reshuffle signals are specified (`economy_system.md` §8.3) but their existence in the engine was not confirmed here.
13. Whether the first-open Legacy Vault modal and the first shops appear before or after the tutorial: no ruling found.

## 6. Recommended order

0, 1, 3a, 3b, 3c, 5, then 2, 4, 6. Rationale: the shop and wallet are the economy's two faucets and sinks, and the quest runtime closes the loop by paying out. HUFF rows (Phase 2) and vendor breadth (Phase 4) wait for the author's numbers.
