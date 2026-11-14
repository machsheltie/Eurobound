# NFT: Winamp (Mint #97)

*Created 2026-11-12 from `design/templates/NFT_Template.md` at the author's request (round v43,
`docs/superpowers/NEXT_WORK.md:766`): "create an item file for each if they dont have one. then put
the fields from the template in there along with the info we have for each and i will draft up the
rest". Every field is sourced to canon (path:line) or marked **OPEN QUESTION (author)** /
**_[AUTHOR TO WRITE]_**. No card copy, bro line or artwork description is drafted here.*

*Replaces the struck "Backstage Laminate (Unauthorized)" (location-derived; struck 2026-08-01,
economy spec §7c; `design/economy/legacy_vault_cards.md:179`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. MA satire at full strength. "Winamp" is a brand and is exempt and
closed (`legacy_vault_cards.md:181-182`; economy spec §7a.1).

**Author-only copy** (`legacy_vault_cards.md:86-90, 170-182`; `design/quests/sinfonia/nfthuntsinfonia.md:4`;
`design/quests/general_quests/fratbronft.md:15`): the Tagline, Description, Collector's Thesis,
artwork description and Bro Read are written by the author only.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Winamp | `legacy_vault_cards.md:66`; `fratbronft.md:46`; `nfthuntsinfonia.md:20` |
| **Mint Number** | `Mint #97`, **a proposal the author may override**. Confirm or override: OPEN QUESTION (author) | `legacy_vault_cards.md:172, 390`; `nfthuntsinfonia.md:20` |
| **Item ID** | `item_nft_winamp` (template pattern). Engine Vault key: `winamp` | template §1; `game/assets/data/nft/legacy_vault.json:150` |
| **City** | Sinfonia | `legacy_vault_cards.md:66` |
| **Collection Slot** | Sinfonia target 2 of 4 | `nfthuntsinfonia.md:18`; `legacy_vault_cards.md:66` |
| **Media Type** | OPEN QUESTION (author) | not in canon |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Backstage terminal: a coin-operated CRT kiosk in the backstage labyrinth | `nfthuntsinfonia.md:18-19`; `legacy_vault_cards.md:66, 171` |
| **Venue** | The Bassline Opera House, Sinfonia (backstage labyrinth): `design/worlds/sinfonia/bassline_opera_house.md` | `nfthuntsinfonia.md:18`; `bassline_opera_house.md:1077` |
| **Unlock Condition** | Two SOVS for ten minutes on the kiosk; sticky keyboard, orange-on-black text mode, still logged into the previous user's account. Minting prints a receipt on a dot-matrix printer nobody has reloaded since the last century. | `nfthuntsinfonia.md:19`; `legacy_vault_cards.md:180-181` |
| **Reality** | The previous user minted it on the clock and thought nothing of it. The kiosk takes the two SOVS either way. | `nfthuntsinfonia.md:25` |
| **Acquisition Beat** | OPEN QUESTION (author). Canon fixes the route and Reality above. | — |

**Flag carried from canon:** the old Reality line's "joke about being made to work a double" was
written against the struck asset and is flagged for the author with the new copy
(`nfthuntsinfonia.md:26`).

## 3. The Artwork Itself

- **Description of the asset:** _[AUTHOR TO WRITE]_ (canon names the artifact, Winamp, and nothing
  about the image; artwork description is author-only, `nfthuntsinfonia.md:4`)
- **Format crime:** _[AUTHOR TO WRITE]_
- **File/asset name:** proposed `nft_winamp.png` (template pattern; extension follows Media Type)

## 4. Card Copy — Legacy Vault

Author-only (`legacy_vault_cards.md` Card 6, ⏳ AUTHOR COPY PENDING, lines 170-182).

- **Tagline:** _[AUTHOR TO WRITE]_
- **Description:** _[AUTHOR TO WRITE]_
- **Collector's Thesis:** _[AUTHOR TO WRITE]_
- **Estimated Future Value:** _[AUTHOR TO WRITE]_ (or derived from the Collector's Thesis by the
  Card 10/11 mapping, `legacy_vault_cards.md:106-108`)
- **Edition Tag:** _[AUTHOR TO WRITE]_
- **Acquisition Story** (Vault card field 4, `legacy_vault_cards.md:25`): _[AUTHOR TO WRITE]_

## 5. Bros' Reaction

Canon Bro Read: _[AUTHOR TO WRITE]_. Staging kept from canon (route, not artwork): the line is
delivered by Chadwick while he is backstage in a European opera house, standing next to a mop
(`nfthuntsinfonia.md:24`).

- **Lord Pilsner:** _[AUTHOR TO WRITE]_
- **Chadwick:** _[AUTHOR TO WRITE]_ (the Bro Read)
- **Bradley:** _[AUTHOR TO WRITE]_

## 6. System Integration

- **Counts toward:** Ultimate Brochain Collection, 16 targets, four per city, milestones at
  4 / 8 / 12 / 16 (`fratbronft.md:12, 78-82`; `NEXT_WORK.md:26`).
- **Wallet tab:** The Legacy Vault (never Bagholder Assets).
- **Resale value:** 0 SOVS everywhere. Cannot be sold, traded or redeemed. Every vendor declines it.
- **Stats / effects:** none, `effect: null`. **[CANON — author, desk h7h9-q1, 2026-11-12: "NFTs never have an effect"]**
- **Engine:** Vault card stub `winamp` exists with every copy field blank
  (`game/assets/data/nft/legacy_vault.json:150`). No item entry in `game/assets/data/items/`.
- **Related files:** `design/economy/legacy_vault_cards.md` (Card 6);
  `design/quests/sinfonia/nfthuntsinfonia.md` (target 2); `design/quests/general_quests/fratbronft.md`;
  `design/worlds/sinfonia/bassline_opera_house.md`.

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (Winamp; image unwritten)
- [ ] Title is an oblique rebrand, not the literal property name (canon title kept as ruled; brand exempt)
- [ ] Mint number evokes the artifact's year (#97 proposed; author to confirm)
- [x] Nothing in any copy field winks (no copy written)
- [x] Bros are never scam-aware; the minter thought nothing of it (canon Reality)
- [x] No mascot, companion or talking entity introduced
- [ ] Asset is specified as ugly/low-effort with a named format crime (author to write)
- [x] Route is location-flavored and the artwork is not
- [x] Real brands/properties left exactly as named

## Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Created from NFT_Template with canon fields only (round v43) | agent |
