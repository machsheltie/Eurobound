# NFT: Napster (Mint #01)

*Created 2026-11-12 from `design/templates/NFT_Template.md` at the author's request (round v43,
`docs/superpowers/NEXT_WORK.md:766`): "create an item file for each if they dont have one. then put
the fields from the template in there along with the info we have for each and i will draft up the
rest". Every field is sourced to canon (path:line) or marked **OPEN QUESTION (author)** /
**_[AUTHOR TO WRITE]_**. No card copy, bro line or artwork description is drafted here.*

*Replaces the struck "VIP Wristband PNG" (location-derived; struck 2026-08-01, economy spec §7c;
`design/economy/legacy_vault_cards.md:132`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. MA satire at full strength. "Napster" is a brand and is exempt and
closed (`legacy_vault_cards.md:133-134`; economy spec §7a.1); it is the real name by the author's
brand sweep ruling (Napstur → Napster, `NEXT_WORK.md:472`).

**Author-only copy** (`legacy_vault_cards.md:86-90, 123-134`; `design/quests/general_quests/fratbronft.md:15`;
`design/quests/debaucheryville/nfthuntdebaucheryville.md:4`): the Tagline, Description and
Collector's Thesis are written by the author only.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Napster | `legacy_vault_cards.md:63`; `fratbronft.md:31`; `nfthuntdebaucheryville.md:20` |
| **Mint Number** | `Mint #01`, **a proposal the author may override**. Confirm or override: OPEN QUESTION (author) | `legacy_vault_cards.md:125, 388`; `fratbronft.md:31` |
| **Item ID** | `item_nft_napster` (template pattern). Engine Vault key: `napster` | template §1; `game/assets/data/nft/legacy_vault.json:63` |
| **City** | Debaucheryville | `legacy_vault_cards.md:63` |
| **Collection Slot** | Debaucheryville target 3 of 4 | `legacy_vault_cards.md:63`; `nfthuntdebaucheryville.md:19` |
| **Media Type** | OPEN QUESTION (author) | not in canon |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Shadow Exchange ledger backroom: inspecting the duct-tape bound Shadow Ledger | `legacy_vault_cards.md:63, 124`; `design/worlds/debaucheryville/shadowexchange.md:42, 126` |
| **Venue** | The Shadow Exchange, Debaucheryville: the Shadow Ledger sits on an illuminated desk | `design/worlds/debaucheryville/shadowexchange.md:42` |
| **Unlock Condition** | The NFT sidequest must already be started to access the ledger content | `shadowexchange.md:127` |
| **Verification fee** | The location doc mentions a "verification fee system" on the ledger hunt; no amount in canon. OPEN QUESTION (author) | `shadowexchange.md:235` |
| **Acquisition Beat** | OPEN QUESTION (author). Canon fixes only the route above. | — |

**Canon conflict (not resolved here):** `shadowexchange.md:126` still says the ledger provides the
struck "VIP Wristband PNG" NFT.

## 3. The Artwork Itself

- **Description of the asset:** _[AUTHOR TO WRITE]_ (canon names the artifact, Napster, and nothing
  about the image)
- **Format crime:** _[AUTHOR TO WRITE]_
- **File/asset name:** proposed `nft_napster.png` (template pattern; extension follows Media Type)

## 4. Card Copy — Legacy Vault

Author-only (`legacy_vault_cards.md` Card 3, ⏳ AUTHOR COPY PENDING, lines 123-134).

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
- **Engine:** Vault card stub `napster` exists with every copy field blank
  (`game/assets/data/nft/legacy_vault.json:63`). No item entry in `game/assets/data/items/`.
- **Related files:** `design/economy/legacy_vault_cards.md` (Card 3);
  `design/quests/debaucheryville/nfthuntdebaucheryville.md`; `design/quests/general_quests/fratbronft.md`;
  `design/worlds/debaucheryville/shadowexchange.md`.

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (Napster; image unwritten)
- [ ] Title is an oblique rebrand, not the literal property name (canon title kept as ruled; brand exempt)
- [ ] Mint number evokes the artifact's year (#01 proposed; author to confirm)
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
