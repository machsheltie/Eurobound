# NFT: Pogs (the Slammer) (Mint #94)

*Created 2026-11-12 from `design/templates/NFT_Template.md` at the author's request (round v43,
`docs/superpowers/NEXT_WORK.md:766`): "create an item file for each if they dont have one. then put
the fields from the template in there along with the info we have for each and i will draft up the
rest". Every field is sourced to canon (path:line) or marked **OPEN QUESTION (author)** /
**_[AUTHOR TO WRITE]_**. No card copy, bro line or artwork description is drafted here.*

*Replaces the struck "Blarney Trap Receipt JPG" (location-derived; struck 2026-08-01, economy spec
§7c; `design/economy/legacy_vault_cards.md:235`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. MA satire at full strength. Real brands and properties keep their
real names (author, 2026-11-09).

**Author-only copy** (`legacy_vault_cards.md:86-90, 226-238`; `design/quests/general_quests/fratbronft.md:15`;
`design/worlds/publandia/publandia.md:142`): the Tagline, Description and Collector's Thesis are
written by the author only.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Pogs (the Slammer) | `legacy_vault_cards.md:69`; `fratbronft.md:61`; `publandia.md:142` |
| **Mint Number** | `Mint #94`, **a proposal the author may override**. Confirm or override: OPEN QUESTION (author) | `legacy_vault_cards.md:228, 392`; `publandia.md:142` |
| **Item ID** | `item_nft_pogs_the_slammer` (template pattern). Engine Vault key: `pogs_the_slammer` | template §1; `game/assets/data/nft/legacy_vault.json:237` |
| **City** | Publandia | `legacy_vault_cards.md:69` |
| **Collection Slot** | Publandia target 1 of 4 | `publandia.md:142` |
| **Media Type** | OPEN QUESTION (author) | not in canon |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Reward for winning the Rival Trio Showdown ("Pub Crawl Showdown"), a 3-round gauntlet: darts, trivia, brawl. This is the showdown reward, not the POS terminal (that is Card 11). | `publandia.md:138-142`; `fratbronft.md:60`; `legacy_vault_cards.md:235-237` |
| **Venue** | The Craic Tax, Publandia | `publandia.md:139`; `fratbronft.md:60`; `NEXT_WORK.md:728` |
| **Unlock Condition** | Win the three-round showdown against the Rival Trio. This is the Rival Trio's single appearance in the game. | `NEXT_WORK.md:23, 728` |
| **Acquisition Beat** | OPEN QUESTION (author). Canon fixes only the route above. | — |

**Canon wording to check:** `legacy_vault_cards.md:227` gives the venue as "The Craic Tax / The
Blarney Trap"; `publandia.md:139` and `NEXT_WORK.md:728` say The Craic Tax only.

## 3. The Artwork Itself

- **Description of the asset:** _[AUTHOR TO WRITE]_ (canon names the artifact, Pogs and the
  Slammer, and nothing about the image)
- **Format crime:** _[AUTHOR TO WRITE]_
- **File/asset name:** proposed `nft_pogs_the_slammer.png` (template pattern; extension follows Media Type)

## 4. Card Copy — Legacy Vault

Author-only (`legacy_vault_cards.md` Card 9, ⏳ AUTHOR COPY PENDING, lines 226-238).

- **Tagline:** _[AUTHOR TO WRITE]_
- **Description:** _[AUTHOR TO WRITE]_
- **Collector's Thesis:** _[AUTHOR TO WRITE]_
- **Estimated Future Value:** _[AUTHOR TO WRITE]_ (or derived from the Collector's Thesis by the
  Card 10/11 mapping, `legacy_vault_cards.md:106-108`)
- **Edition Tag:** _[AUTHOR TO WRITE]_
- **Acquisition Story** (Vault card field 4, `legacy_vault_cards.md:25`): _[AUTHOR TO WRITE]_

## 5. Bros' Reaction

No canon bro lines exist for this NFT.

- **Lord Pilsner:** _[AUTHOR TO WRITE]_
- **Chadwick:** _[AUTHOR TO WRITE]_
- **Bradley:** _[AUTHOR TO WRITE]_

## 6. System Integration

- **Counts toward:** Ultimate Brochain Collection, 16 targets, four per city, milestones at
  4 / 8 / 12 / 16 (`fratbronft.md:12, 78-82`; `NEXT_WORK.md:26`).
- **Wallet tab:** The Legacy Vault (never Bagholder Assets).
- **Resale value:** 0 SOVS everywhere. Cannot be sold, traded or redeemed. Every vendor declines it.
- **Stats / effects:** none, `effect: null`. **[CANON — author, desk h7h9-q1, 2026-11-12: "NFTs never have an effect"]**
- **Engine:** Vault card stub `pogs_the_slammer` exists with every copy field blank
  (`game/assets/data/nft/legacy_vault.json:237`). No item entry in `game/assets/data/items/`.
- **Related files:** `design/economy/legacy_vault_cards.md` (Card 9);
  `design/quests/general_quests/fratbronft.md`; `design/worlds/publandia/publandia.md`.

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (Pogs; image unwritten)
- [ ] Title is an oblique rebrand, not the literal property name (canon title kept as ruled)
- [ ] Mint number evokes the artifact's year (#94 proposed; author to confirm)
- [x] Nothing in any copy field winks (no copy written)
- [x] Bros are never scam-aware
- [x] No mascot, companion or talking entity introduced
- [ ] Asset is specified as ugly/low-effort with a named format crime (author to write)
- [x] Route is location-flavored and the artwork is not
- [x] Real brands/properties left exactly as named

## Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Created from NFT_Template with canon fields only (round v43) | agent |
