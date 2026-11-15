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

- **Description of the asset:** **[APPROVED — author, Desk Eurobound-rpac-q4, 2026-11-15: "Napster A"; proposed by the Writers' Room as "The Cat At Four Percent"]** A 640×480 screenshot of the Napster client window, taken whole, with the Windows 98 taskbar still along the bottom. The cat-with-headphones mark sits large in the upper two-thirds of the window; under it a single file is downloading: one green bar filled about a twentieth of the way, a speed readout, an ETA in minutes that is not decreasing. The mouse arrow is parked mid-window, mid-click, where the screenshot was grabbed.
- **Format crime:** **[APPROVED — author, Desk Eurobound-rpac-q4]** a screen grab, not a file. The Windows taskbar and Start button are cropped in at the bottom, the cursor is baked into the image forever, and the whole thing is JPEG'd hard enough that the window chrome has a dirty halo.
- **File/asset name:** proposed `nft_napster.png` (template pattern; extension follows Media Type)

## 🖼️ Physical description (icon art brief)

**[APPROVED — author, Desk Eurobound-rpac-q4, 2026-11-15: "Approve: slab + Napster A + selfie A".]** Written in the Writers' Room (`WritingRoom/tasks/20261114_2023_nft_icon_images_four_slabs/`). The icon is the shared cheap trading-card slab (`design/items/docs/nft_icon_slab.md`) with this image inside it.

| Field | Description |
|---|---|
| **silhouette** | Mistral §1 slab: 5:7 vertical case, beveled rim, label strip across the top sixth. Inside the window, one horizontal screen-filling rectangle (the whole screenshot, uncropped, so it does not fill the window evenly and leaves a beige sliver of card at the bottom edge), and inside that a large round-headed cat shape in the upper half with a wide progress bar across the lower third. |
| **scale_cue** | At 128 px: white top strip with a red dot, then a grey-white screen containing one dark round-eared head and one short green bar. Nothing else survives, and nothing else needs to. |
| **materials_and_cheap_cues** | Shared slab cues exactly as Mistral §1 (polystyrene regrind tint, mold seams, sprue nub, crooked paper strip with one air bubble, hairline scratches, dust sealed under the plastic, greasy fingerprint on the lower-right of the window). The printed card inside is thin glossy photo paper printed from a screenshot at the wrong aspect ratio, so the image is stretched slightly wide and the card is cut off-square by a millimetre. |
| **colours** | Slab: case **#DDE3E6**, label **#F5F5F0**, red sticker **#D02A2A**, rim highlight **#FFFFFF**, inner lip **#9AA3A8** (all Mistral §1, unchanged). Image window: client window white **#F0F0F0**; window chrome and taskbar grey **#C0C0C0**; title bar navy **#000080**; cat mark near-black **#1A1A1A** with headphone cups in the same near-black outlined **#3A3A3A**; download bar green **#00C000** on a dark trough **#5A5A5A**, filled one-twentieth; CRT glass tint over the whole window **#E8FFE8** at low opacity; JPEG halo around the chrome **#8A8A8A**; beige sliver of exposed card at the bottom edge **#C9BFA6**. |
| **contents** | none (printed card; the progress bar is image content, not a drink). |
| **decoration** | Shared slab label strip, round red "AUTHENTIC" sticker, barcode sticker (Mistral §1). No other added decor; the taskbar, the title bar and the baked-in cursor are part of the printed image. |
| **condition** | Shared slab wear plus: the card's top-right corner lifted off the sleeve, one faint horizontal band across the screen where the printer ran low on cyan, and a small crease through the cat's left headphone cup. |
| **garnish_and_addons** | none. |
| **palette_anchors** | From `design/worlds/debaucheryville/shadowexchange.md:51` — Stone Grey **#708090** (used as the plastic rim's reflection tint), UV Purple **#9400D3** (used as the faint purple fringe on the screen's right edge, the case's only colour contamination), Vault Black **#1C1C1C** (the shadow pooled inside the bevel). New to this item: client white **#F0F0F0**, chrome grey **#C0C0C0**, title navy **#000080**, cat black **#1A1A1A**, bar green **#00C000**, trough grey **#5A5A5A**, card beige **#C9BFA6**. |
| **reads_at_icon_size** | 1. Clear slab, white top strip, red sticker dot. 2. A grey-white screen filling the window. 3. A dark round-eared cat head above one short green bar. |
| **must_not_look_like** | Not a real grader's slab (§1). Not a modern browser or a current streaming app — the grey chrome and the navy title bar must read as an old desktop, not a clean UI. Not a photograph of a cat, a pet, or a plush; the mark is flat two-tone print. Not a music note, a cassette, or a headphone product shot. The window must not be centred and clean: the taskbar strip at the bottom and the off-square card edge are what make it a screenshot of a screen. |
| **lettering** | Slab: **"BROCHAIN CERTIFIED"** / **"GRADE BRO 10"** / **"SERIAL 00-BRO-99"** / **"AUTHENTIC"**, exactly as Mistral §1. Inside the image, rendered as illegible grey smudge at icon size and never load-bearing: the title bar's word, the taskbar's leftmost button, one filename row, one speed readout, one ETA. No read above depends on any of it. |

---

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
