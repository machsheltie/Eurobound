# NFT: The Millennium Bug (Mint #00)

*Created 2026-11-12 from `design/templates/NFT_Template.md` at the author's request (round v43,
`docs/superpowers/NEXT_WORK.md:766`): "create an item file for each if they dont have one. then put
the fields from the template in there along with the info we have for each and i will draft up the
rest". Every field is sourced to canon (path:line) or marked **OPEN QUESTION (author)** /
**_[AUTHOR TO WRITE]_**. No card copy, bro line or artwork description is drafted here.*

*Replaces the struck "Pixelated Kebab Monkey" (location-derived; struck 2026-08-01, economy spec
§7c; `design/economy/legacy_vault_cards.md:105`).*

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. MA satire at full strength. Real brands and properties keep their
real names (author, 2026-11-09).

**Author-only copy** (`legacy_vault_cards.md:86-90, 96-109`; `design/quests/general_quests/fratbronft.md:15`;
`design/quests/debaucheryville/nfthuntdebaucheryville.md:4`): the Tagline, Description and
Collector's Thesis are written by the author only. "No lane writes any of it."
(`legacy_vault_cards.md:109`)

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | The Millennium Bug | `legacy_vault_cards.md:61`; `fratbronft.md:19`; `nfthuntdebaucheryville.md:8` |
| **Mint Number** | `Mint #00`. **[CANON — author, Eurobound Desk v45, 2026-11-12; canon fixes approved on the Desk, sprite-dev-millennium-bug-fixes]** **Yes** (*Mint #00 is the absolute peak number for a Y2K artifact representing the rollover event.*) | `legacy_vault_cards.md:98, 386`; `fratbronft.md:19`; author, Eurobound Desk v45 |
| **Item ID** | `item_nft_millennium_bug` (template pattern). Engine Vault key: `millennium_bug` | template §1; `game/assets/data/nft/legacy_vault.json:5` |
| **City** | Debaucheryville | `legacy_vault_cards.md:61` |
| **Collection Slot** | Debaucheryville target 1 of 4 | `legacy_vault_cards.md:61`; `nfthuntdebaucheryville.md:7` |
| **Media Type** | `Corrupted DOS Executable wrapper containing an animated 16-bit GIF` | **[CANON — author, Eurobound Desk v45, 2026-11-12]** |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | QR code graffiti in the VIP bathroom stall | `legacy_vault_cards.md:61, 97`; `design/worlds/debaucheryville/velvet_curtain_club.md:447` |
| **Venue** | The Velvet Curtain Club, Debaucheryville: VIP bathroom, behind the "Staff Only" red velvet curtain. Stall doc: `design/worlds/debaucheryville/velvetcurtainclubvipstall.md` | `velvet_curtain_club.md:465-466` |
| **Unlock Condition** | A Bravado check to get past the buffed-out bouncers, then the QR graffiti is scanned | `velvet_curtain_club.md:467-468` |
| **Graffiti around the QR** (route furniture, not artwork) | "ROI = Regret On Investment," startup ideas, altcoin schemes; the text drips champagne when viewed while drunk | `velvet_curtain_club.md:469-470` |
| **Acquisition Beat** | See **Acquisition Beat** below | **[CANON — author, Eurobound Desk v45, 2026-11-12]** |

### Acquisition Beat (What happens when they scan it)

**[CANON — author, Eurobound Desk v45, 2026-11-12]**

The party navigates the Velvet Curtain Club VIP bathroom behind the "Staff Only" red velvet curtain, surviving a brutal Bravado check against the heavily muscled bouncers guarding the inner sanctum. Inside the stall, the walls are dripping with startup pitch quotes and altcoin schemes under the champagne-flute ceiling light's RGB shimmer. Chadwick pulls out his phone and scans a scratched QR code graffiti tag sprayed right over the toilet paper dispenser.

The phone screen flashes an aggressive Amber alert screen, the QR graffiti glows, the phone chirps a scan beep and a triumphant success chime, and drops the asset straight into the Legacy Vault.

**Chadwick** *(eyes wide, phone trembling slightly)*: "Bro. Look at the metadata timestamp. It's dated December 31, 1999, at eleven-fifty-nine and fifty-nine seconds. We didn't just find a QR code in a VIP stall—we hacked the millennium."

**Canon conflict (resolved):** the VIP stall doc and both Velvet Curtain PNG specs now name The Millennium Bug
(Mint #00) as QR code graffiti (Eurobound-g56, Eurobound-222). Reveal look (author, Eurobound-222-q1, 2026-11-12): no reveal animation. The QR graffiti is on the wall from the start; scanning plays the existing highlight glow, scan beep and success chime. The reveal-frame slots are dropped.

## 3. The Artwork Itself

- **Description of the asset (What the Picture Actually Shows):** **[CANON — author, Eurobound Desk v45, 2026-11-12]**
  An animated looping GIF styled after a Windows 98 screensaver gone horribly wrong:
  - **The Subject:** A bloated, neon-green software bug with oversized compound eyes shaped like digital clock digits (`23:59`), twitching nervously and crying under a tiny party hat against a black background of cascading green binary code.
  - **The Detail:** Above its head, a cheap, pixelated party noisemaker uncoils on every fourth frame, accompanied by a faint visual flash that looks like an old CRT monitor losing horizontal sync.
  - **The Flaw:** The image resolution is locked at an awkward 320x240 stretched to fit the screen, leaving thick, blurry interpolation pixels that Chadwick insists represent "deep-layer cryptography."
- **Format crime:** **[CANON — author, Eurobound Desk v45, 2026-11-12]**
  **The Corrupted `.EXE` Self-Extractor:** The file isn't even a clean media format—it’s distributed as a disguised 16-bit DOS executable that triggers a fake `SYS$ERROR: COFFEE_OVERFLOW` dialogue box every time you try to view it in your inventory, forcing you to manually click "OK" on an unmovable pop-up window that hasn't received a software patch since the Clinton administration.
- **File/asset name:** proposed `nft_millennium_bug.png` (template pattern; extension follows Media Type)

## 4. Card Copy — Legacy Vault

Author-only (`legacy_vault_cards.md` Card 1, ⏳ AUTHOR COPY PENDING, lines 96-109).

**[CANON — author, Eurobound Desk v45, 2026-11-12]** (Tagline, Description, Collector's Thesis)

- **Tagline:** *"Everyone else spent December 31, 1999 stocking up on canned beans and generators. We minted the bug itself. That's not a software flaw, chat—that's a foundational macro event."*
- **Description:** A brutally compressed 16-bit digital artifact scraped straight from a bathroom stall graffiti tag behind the red velvet ropes of the Velvet Curtain Club. The asset depicts a glowing green, pixelated 1990s desktop computer bug wearing a tiny party hat, twitching and crying under a pixelated party noisemaker as two digits roll over from '99' to '00'. It is permanently valued at **0 SOVS** across every bank, ledger, and black-market terminal in Debaucheryville, but its psychological value to the bros is immeasurable.
- **Collector's Thesis:** "The media lied to you about the year 2000, chat. They told you airplanes were going to fall out of the sky and microwave clocks were going to reset to midnight. They didn't tell you that the bug was actually an unmined digital asset class waiting for three guys with a smartphone and a VIP bathroom pass. Mint number zero isn't a historical oversight; it's the exact second global infrastructure blinked. While the paper hands were panicking over legacy databases, we captured the vector. On the chain. Forever."
- **Estimated Future Value:** _[AUTHOR TO WRITE]_ (or derived from the Collector's Thesis by the
  Card 10/11 mapping, `legacy_vault_cards.md:106-108`)
- **Edition Tag:** _[AUTHOR TO WRITE]_ (canon: "Edition tag from the mint number", `legacy_vault_cards.md:108`)
- **Acquisition Story** (Vault card field 4, `legacy_vault_cards.md:25`): _[AUTHOR TO WRITE]_

## 5. Bros' Reaction

**[CANON — author, Eurobound Desk v45, 2026-11-12]**

- **Lord Pilsner:** "Think about what everybody else was doing when the clock hit zero. They were hiding under their desks waiting for the power grid to collapse. We waited twenty-six years for the dust to settle, walked past the bouncers, and minted the exact microsecond the old world died. That's not a collectible. That's a founding document."
- **Chadwick:** "Chat, look at the mint number. *Zero-zero.* You can't get earlier than zero. People are out there buying mint forty-two or mint seventy-three like peasants—we hold the literal genesis bug that preceded the blockchain itself. Do not talk to me about floor prices right now."
- **Bradley:** "It crashed my phone browser twice and deleted my calendar app. That means it has real software weight. I'm keeping it."

## 6. System Integration

- **Counts toward:** Ultimate Brochain Collection, 16 targets, four per city, milestones at
  4 / 8 / 12 / 16 (`fratbronft.md:12, 78-82`; `NEXT_WORK.md:26`).
- **Wallet tab:** The Legacy Vault (never Bagholder Assets).
- **Resale value:** 0 SOVS everywhere. Cannot be sold, traded or redeemed. Every vendor declines it.
- **Stats / effects:** none, `effect: null`. **[CANON — author, desk h7h9-q1, 2026-11-12: "NFTs never have an effect"]**
- **Engine:** Vault card stub `millennium_bug` exists with every copy field blank
  (`game/assets/data/nft/legacy_vault.json:5-32`). No item entry in `game/assets/data/items/`.
- **Related files:** `design/economy/legacy_vault_cards.md` (Card 1);
  `design/quests/debaucheryville/nfthuntdebaucheryville.md`; `design/quests/general_quests/fratbronft.md`;
  `design/worlds/debaucheryville/velvet_curtain_club.md`; `design/worlds/debaucheryville/velvetcurtainclubvipstall.md`.

## 7. Validation Checklist

- [x] Artwork is 90s/00s pop culture, not location-derived (the Y2K bug; image unwritten)
- [ ] Title is an oblique rebrand, not the literal property name (canon title kept as ruled)
- [x] Mint number evokes the artifact's year (#00 confirmed, author, Eurobound Desk v45, 2026-11-12)
- [x] Nothing in any copy field winks (no copy written)
- [x] Bros are never scam-aware
- [x] No mascot, companion or talking entity introduced
- [x] Asset is specified as ugly/low-effort with a named format crime (author, Eurobound Desk v45, 2026-11-12: "The Corrupted `.EXE` Self-Extractor")
- [x] Route is location-flavored and the artwork is not
- [x] Real brands/properties left exactly as named

## Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-12 | Created from NFT_Template with canon fields only (round v43) | agent |
| 2026-11-12 | Author's card copy, artwork, format crime, media type, acquisition beat, bro lines and Mint #00 transcribed verbatim (Eurobound Desk v45) | agent |
