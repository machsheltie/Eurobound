# NFT: Sea-Monkeys (Mint #73)

*Written 2026-11-11 from `design/templates/NFT_Template.md`, after the author's ruling at the
Writers' Room desk (15:21, round v29 `relic_nft`), verbatim: **"replace the beer pong saint relic
with Sea-Monkey"**. Every field is sourced to canon (source named) or marked **PROPOSED — NEEDS
AUTHOR RULING**. The card copy is author-only and stays empty.*

*Replaces the struck Beer Pong Saint Relic (struck 2026-08-01, spec §7c; old doc retired to
`design/legacy/Items/beer_pong_saint_relic_nft_item.md`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots: Sea-Monkeys is an image, not a pet or a companion, and nothing in it
talks, follows or has an arc. MA satire at full strength.

**Author-only copy (canon, `design/economy/legacy_vault_cards.md` Card 2 and §1a.8;
`nfthuntdebaucheryville.md`; `fratbronft.md`):** the Tagline, Description and Collector's Thesis
are written by the author only. No lane drafts them, and no placeholder prose is offered here.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Sea-Monkeys | canon: `legacy_vault_cards.md` §2 roster, `nfthuntdebaucheryville.md`, `general_quests/fratbronft.md` |
| **Mint Number** | `Mint #73`, **a PROPOSAL the author may override** | canon marks it proposed (all three files above) |
| **Item ID** | `item_sea_monkeys` (design JSONs) | follows the arcade design files' `item_` convention; the template pattern would be `item_nft_sea_monkeys`. **PROPOSED — NEEDS AUTHOR RULING** if the template id is wanted |
| **Engine key** | `sea_monkeys` (in `game/assets/data/items/key_items.json`) | the id the claw code grants (`arcade_claw.gd` `TOP_PRIZE_ID`) |
| **State flag** | `sea_monkeys_obtained` | `arcade_claw.gd` `TOP_PRIZE_FLAG`; design core JSON |
| **Item Type** | Quest item, permanent: `unique_quest_collectible`, not stackable, not consumable, rarity unique | carried over from the claw prize's design entry (`absinthe_arcade_items.json`) |
| **City** | Debaucheryville | canon |
| **Collection Slot** | Debaucheryville target 2 of 4 | canon: `legacy_vault_cards.md` §2 (#2) |
| **Media Type** | **PROPOSED — NEEDS AUTHOR RULING** | not in canon |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Rigged Absinthe Arcade claw machine (`rigged_absinthe_claw_machine`) | canon: route unchanged since 2026-08-01 (`legacy_vault_cards.md`, `nfthuntdebaucheryville.md`) |
| **Venue** | Absinthe Arcade, claw alcove (`aa_node_claw_alcove`), Debaucheryville: `design/worlds/debaucheryville/absinthearcade.md` | canon |
| **Unlock Condition** | Pay 5 Absinthe Arcade tokens per play. Steer left or right for up to 10 seconds, then drop; the claw grabs whatever is under it. The claw slips unless the PAYOUT light is blinking. The plays counter is saved: after 6 plays the light blinks before the bros pay for the 7th, and that grab holds only if the claw is over Sea-Monkeys. The cycle restarts after any blinking play. The Token Attendant, Jakub "Tokens" Dvořák, hints at the cycle. | canon: rounds v25–v28 (`NEXT_WORK.md`); rigged claw 5 tokens ruled |
| **Before / after the win** | Sea-Monkeys or nothing until it is won; then junk-shelf prizes. The claw stays rigged after the win: junk grabs hold only on a blinking PAYOUT play. | canon: v26, v29 |
| **Location Completion** | Getting Sea-Monkeys is the Absinthe Arcade's completion requirement. | canon: `absinthearcade.md` Exit Conditions (relic line replaced) |
| **Dispense Audio** | `fur_elise_crypto_victory_remix.ogg` | canon: the claw's dispense sting (`absinthe_arcade_items.json`, environment JSON) |
| **NPC Trigger** | The Arcade Employee's `you_actually_won_that` dialogue set fires on `sea_monkeys_obtained`; the lines are unwritten. | canon: `absinthe_arcade_npcs.json` |
| **Acquisition Beat** | **PROPOSED — NEEDS AUTHOR RULING.** Canon fixes only the mechanics above. The claw-win double take (`claw_win_double_take`) is canon animation. | — |

## 3. The Artwork Itself

- **Description of the asset:** **NEEDS AUTHOR RULING.** Canon names the artifact (Sea-Monkeys)
  and nothing about the image.
- **Format crime:** **NEEDS AUTHOR RULING.**
- **How it sits in the claw cabinet:** **NEEDS AUTHOR RULING.** (The relic hung on a gold thread;
  that staging is void.)
- **File/asset name:** inventory icon `aa_ui_sea_monkeys` (renamed from `aa_ui_beer_pong_saint_relic`
  in the sprite mapping). Full-size image **PROPOSED:** `nft_sea_monkeys.png`.

## 4. Card Copy — Legacy Vault

**AUTHOR-ONLY. Canon: `legacy_vault_cards.md` Card 2 — "No lane writes any of it."**

- **Tagline:** _[AUTHOR TO WRITE]_
- **Description:** _[AUTHOR TO WRITE]_
- **Collector's Thesis:** _[AUTHOR TO WRITE]_
- **Estimated Future Value / Edition Tag:** derived from the author's copy by the Card 10/11
  mapping once it exists (`legacy_vault_cards.md`).

## 5. Bros' Reaction

**NEEDS AUTHOR RULING.** Canon has no bro lines for this NFT, and none are drafted here.

- **Lord Pilsner:** _[AUTHOR TO WRITE]_
- **Chadwick:** _[AUTHOR TO WRITE]_
- **Bradley:** _[AUTHOR TO WRITE]_

## 6. System Integration

- **Counts toward:** the Ultimate Brochain Collection (12 base-game; milestones at 4 / 8 / 12).
- **Wallet tab:** The Legacy Vault.
- **Resale value:** 0 SOVS everywhere. It cannot be sold, traded or redeemed, and every vendor
  declines it (canon for every NFT, template §6).
- **Stats / effects:** **PROPOSED — NEEDS AUTHOR RULING:** none (`effect: null`). The one NFT
  precedent, `tractor_nft_item.md`, carries stat bonuses.
- **Engine registration:** `key_items.json` → `sea_monkeys`, `item_class: "quest"`,
  `source: "rigged_absinthe_claw_machine"`, `effect: null`. Its `description` is only
  "Sea-Monkeys (Mint #73)." until the author writes the card copy.
- **Related files:**
  - `design/World Design/Debaucheryville/items/absinthe_arcade_items.json`
  - `design/World Design/Debaucheryville/interactions/absinthe_arcade_interactions.json`
  - `design/World Design/Debaucheryville/core/absinthe_arcade_core.json`
  - `design/World Design/Debaucheryville/npcs/Absinthe_Arcade/absinthe_arcade_npcs.json`
  - `design/worlds/debaucheryville/absinthearcade.md`
  - `design/Quests/debaucheryville/nfthuntdebaucheryville.md`, `design/Quests/general_quests/fratbronft.md`
  - `design/economy/legacy_vault_cards.md` (Card 2)

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (the artifact is canon; the image is unwritten)
- [ ] Title is an oblique rebrand, not the literal property name. **Conflict:** canon titles it
  "Sea-Monkeys". Template rule 5 wants an oblique title; the author's 2026-11-09 ruling ("ALL other
  things get their real names") points the other way. NEEDS AUTHOR RULING.
- [ ] Mint number evokes the artifact's year (#73 is a canon PROPOSAL)
- [x] Nothing in any copy field winks (no copy written)
- [x] Bros are never scam-aware
- [x] No mascot, companion, or talking entity introduced
- [ ] Asset is ugly/low-effort with a named format crime (NEEDS AUTHOR RULING)
- [x] Route is location-flavoured (rigged arcade claw) and the artwork is not
- [x] Real brands left exactly as named (Sea-Monkeys)
