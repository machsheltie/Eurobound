# NFT: Crystal Pepsi (Mint #92)

*Created 2026-11-12 from `design/templates/NFT_Template.md` at the author's request (round v43,
`docs/superpowers/NEXT_WORK.md:766`): "create an item file for each if they dont have one. then put
the fields from the template in there along with the info we have for each and i will draft up the
rest". Every field is sourced to canon (path:line) or marked **OPEN QUESTION (author)** /
**_[AUTHOR TO WRITE]_**. No card copy, bro line or artwork description is drafted here.*

*Replaces the struck "Foam Face #17" and its "#17 / at least sixty" edition gag (location-derived;
struck 2026-08-01, economy spec §7c; `design/economy/legacy_vault_cards.md:193`;
`design/quests/sinfonia/nfthuntsinfonia.md:36`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. MA satire at full strength. "Crystal Pepsi" is a brand and is exempt
and closed (`legacy_vault_cards.md:194-195`; economy spec §7a.1).

**Author-only copy** (`legacy_vault_cards.md:86-90, 184-195`; `nfthuntsinfonia.md:4`;
`design/quests/general_quests/fratbronft.md:15`): the Tagline, Description, Collector's Thesis,
artwork description and Bro Read are written by the author only.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Crystal Pepsi | `legacy_vault_cards.md:67`; `fratbronft.md:52`; `nfthuntsinfonia.md:30` |
| **Mint Number** | `Mint #92`, **a proposal the author may override**. Confirm or override: OPEN QUESTION (author) | `legacy_vault_cards.md:186, 391`; `nfthuntsinfonia.md:30` |
| **Item ID** | `item_nft_crystal_pepsi` (template pattern). Engine Vault key: `crystal_pepsi` | template §1; `game/assets/data/nft/legacy_vault.json:179` |
| **City** | Sinfonia | `legacy_vault_cards.md:67` |
| **Collection Slot** | Sinfonia target 3 of 4 | `nfthuntsinfonia.md:28`; `legacy_vault_cards.md:67` |
| **Media Type** | OPEN QUESTION (author) | not in canon |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Latte-art AR filter: the espresso stand's tablet renders a milk-foam heart over the customer's face while the barista judges the order. The filter has a MINT button in the corner in a font nobody at the stand chose. | `nfthuntsinfonia.md:29`; `legacy_vault_cards.md:185, 194` |
| **Venue** | Grounds For Concern, Kaffeehaus Row, Sinfonia: `design/worlds/sinfonia/grounds_for_concern.md` | `nfthuntsinfonia.md:28` |
| **Unlock Condition** | Buy the five-SOVS cappuccino and press MINT on the filter | `nfthuntsinfonia.md:35`; `legacy_vault_cards.md:194` |
| **Reality** | Ferdinand sighs, delivers the latte, applies the standard visible disappointment and takes the five SOVS. He has watched roughly two hundred tourists mint the same one and has never once mentioned how many. | `nfthuntsinfonia.md:35` |
| **Acquisition Beat** | OPEN QUESTION (author). Canon fixes the route and Reality above. | — |

**Canon conflict resolved (author, 2026-11-12, Eurobound-dk9):** Ferdinand the Focused runs the AR
filter. `nfthuntsinfonia.md:29, 35` now name him, and `grounds_for_concern.md` (Quest Integration)
carries the route.

## 3. The Artwork Itself

- **Description of the asset:** _[AUTHOR TO WRITE]_ (canon names the artifact, Crystal Pepsi, and
  nothing about the image; artwork description is author-only, `nfthuntsinfonia.md:4`)
- **Format crime:** _[AUTHOR TO WRITE]_
- **File/asset name:** proposed `nft_crystal_pepsi.png` (template pattern; extension follows Media Type)

## 4. Card Copy — Legacy Vault

Author-only (`legacy_vault_cards.md` Card 7, ⏳ AUTHOR COPY PENDING, lines 184-195).

- **Tagline:** _[AUTHOR TO WRITE]_
- **Description:** _[AUTHOR TO WRITE]_
- **Collector's Thesis:** _[AUTHOR TO WRITE]_
- **Estimated Future Value:** _[AUTHOR TO WRITE]_ (or derived from the Collector's Thesis by the
  Card 10/11 mapping, `legacy_vault_cards.md:106-108`)
- **Edition Tag:** _[AUTHOR TO WRITE]_
- **Acquisition Story** (Vault card field 4, `legacy_vault_cards.md:25`): _[AUTHOR TO WRITE]_

## 5. Bros' Reaction

Canon Bro Read: _[AUTHOR TO WRITE]_ (`nfthuntsinfonia.md:34`).

- **Lord Pilsner:** _[AUTHOR TO WRITE]_
- **Chadwick:** _[AUTHOR TO WRITE]_
- **Bradley:** _[AUTHOR TO WRITE]_

## 6. System Integration

- **Counts toward:** Ultimate Brochain Collection, 16 targets, four per city, milestones at
  4 / 8 / 12 / 16 (`fratbronft.md:12, 78-82`; `NEXT_WORK.md:26`).
- **Wallet tab:** The Legacy Vault (never Bagholder Assets).
- **Resale value:** 0 SOVS everywhere. Cannot be sold, traded or redeemed. Every vendor declines it.
- **Stats / effects:** none, `effect: null`. **[CANON — author, desk h7h9-q1, 2026-11-12: "NFTs never have an effect"]**
- **Engine:** Vault card stub `crystal_pepsi` exists with every copy field blank
  (`game/assets/data/nft/legacy_vault.json:179`). No item entry in `game/assets/data/items/`.
- **Related files:** `design/economy/legacy_vault_cards.md` (Card 7);
  `design/quests/sinfonia/nfthuntsinfonia.md` (target 3); `design/quests/general_quests/fratbronft.md`;
  `design/worlds/sinfonia/grounds_for_concern.md`.

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (Crystal Pepsi; image unwritten)
- [ ] Title is an oblique rebrand, not the literal property name (canon title kept as ruled; brand exempt)
- [ ] Mint number evokes the artifact's year (#92 proposed; author to confirm)
- [x] Nothing in any copy field winks (no copy written)
- [x] Bros are never scam-aware; the barista knows (canon Reality)
- [x] No mascot, companion or talking entity introduced
- [ ] Asset is specified as ugly/low-effort with a named format crime (author to write)
- [x] Route is location-flavored and the artwork is not
- [x] Real brands/properties left exactly as named

## Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Created from NFT_Template with canon fields only (round v43) | agent |
