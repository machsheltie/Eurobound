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
| **Media Type** | Animated GIF (.gif) packaged inside an unplayable legacy Flash projector wrapper | **[CANON — author, round v43, 2026-11-12]** |

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

- **Description of the asset (What the Picture Actually Shows):** **[CANON — author, round v43, 2026-11-12]**
  An animated digital trading card featuring the iconic 90s mail-order cartoon illustration of Sea-Monkeys, rendered in a chunky, pixelated style reminiscent of an early Microsoft Paint GIF saved with too much JPEG compression.
  - The Subjects: Two translucent, grinning brine shrimp with distinct human facial features, majestic arched eyebrows, and tiny floating golden crowns that hover a pixel too high above their heads.
  - The Environment: A murky, lime-green 1990s fishbowl background complete with a faded plastic treasure chest that occasionally belches a single, perfectly square pixel-bubble.
  - The Flaw: Every six loops, the entire image stretches vertically for one frame like a dying cathode-ray tube television before snapping back, accompanied by a faint audio pop that sounds like a blown speaker in a 1998 Honda Civic.
- **Format crime:** **[CANON — author, round v43, 2026-11-12]**
  The .BMP-to-.GIF Traumatic Conversion: The file is saved with a custom color palette of exactly 16 violently saturated neon colors, meaning every gradient looks like a topographic map of a toxic waste dump. Worse, the creator tried to fake transparency by filling the background with a checkerboard pattern of neon pink and electric lime green that stubbornly refuses to render correctly in any modern wallet, leaving a glowing radioactive halo around the shrimp no matter what dark-mode theme you use.
- **How it sits in the claw cabinet (How it Hangs in the Claw Cabinet):** **[CANON — author, round v43, 2026-11-12]**
  Wedged awkwardly between a moldy plush frog and an empty can of imported energy drink on the top-right shelf of the rigged Absinthe Arcade claw machine, tilted at a distinct 45-degree angle so the glare from the neon overhead sign completely obliterates the shrimp's faces. It doesn't hang; it is simply trapped by gravity and friction behind scratched plexiglass that smells faintly of spilled absinthe and stale cigarette smoke. When you finally win it on the 7th play, the claw drops it with a hollow, plastic clatter while the machine belts out a distorted, triumphant Für Elise crypto-remix.
- **File/asset name:** inventory icon `aa_ui_sea_monkeys` (renamed from `aa_ui_beer_pong_saint_relic`
  in the sprite mapping). Full-size image **PROPOSED:** `nft_sea_monkeys.png`.

## 4. Card Copy — Legacy Vault

**AUTHOR-ONLY. Canon: `legacy_vault_cards.md` Card 2 — "No lane writes any of it."**

**[CANON — author, round v43, 2026-11-12]** (Tagline, Description, Collector's Thesis)

- **Tagline:** "Instant life in a foil packet, now immortalized on an unreadable L2 rollup because Harold Hillier wouldn't sign the release."
- **Description:** A high-contrast, aggressively compressed 48x48 pixel GIF of the classic 1990s comic book ad illustration—two excessively smiling, human-faced aquatic royalty figures wearing golden crowns, swimming triumphantly through what appears to be a glass bowl of murky tap water laced with green algae and unexploded nutrient powder.

  The animation consists of exactly four jerky frames where their eyes dilate in terrifying unison while a faint, low-bitrate MIDI file of the Saved by the Bell theme song plays on an infinite loop. It was minted on an abandoned side-chain whose block explorer is currently a dead link to a GeoCities guestbook. It is worth 0 SOVS at every bank, pawn shop, and shady back-alley terminal in Debaucheryville, permanently and by design.
- **Collector's Thesis:** "Everyone looks at the 1998 mail-order comic book back cover and sees a novelty gag you ordered with allowance money and a self-addressed stamped envelope. But you’re not looking at the biology, chat. You’re looking at decentralized, low-maintenance aquatic civilization delivered straight to your mailbox via USPS bulk mail. Mint number seventy-three isn't just a JPEG of two cartoon shrimp with human teeth; it's a foundational stake in the primordial soup of the digital economy. While the paper hands are crying about liquidity, we’re holding the actual building blocks of life. On the chain. Forever."
- **Estimated Future Value / Edition Tag:** derived from the author's copy by the Card 10/11
  mapping once it exists (`legacy_vault_cards.md`).

## 5. Bros' Reaction

**[CANON — author, round v43, 2026-11-12]**

- **Lord Pilsner** (holding the vault card to the light with solemn reverence): "Think about the logistics, bro. You add water, and they happen. You don't negotiate with them, you don't build a roadmap, you just watch them swim in a circle until they die of natural causes in three weeks. That's not a pet. That’s pure, unfiltered market genesis. And Jakub tried to tell us it was just plastic junk in a claw machine."
- **Chadwick** (zoomed in aggressively on his phone camera, completely vertical, vlogging to an audience of zero): "Chat, look at the crown. Look at the micro-expression on the male shrimp. That is not generated by an algorithm; that is raw, organic 1998 mail-order art history. Number seventy-three. Do you know how many people are trying to sweep the floor on this collection right now? All of them. And we got it off a rigged grabber in Debaucheryville for thirty-five SOVS total. We are basically venture capitalists."
- **Bradley** (deadpan, staring blankly past the screen while lighting a cigarette indoors): "It's on the chain. Even if the arcade burns down, the shrimp are still swimming. That's why I'm not wiping the screen off."

## 6. System Integration

- **Counts toward:** the Ultimate Brochain Collection (16 base-game, four per city; milestones at 4 / 8 / 12 / 16).
- **Wallet tab:** The Legacy Vault.
- **Resale value:** 0 SOVS everywhere. It cannot be sold, traded or redeemed, and every vendor
  declines it (canon for every NFT, template §6).
- **Stats / effects:** **[CANON — author, round v43, 2026-11-12]** effect: null (None — exactly like the tractor, it grants no combat stats, no currency yield, and no house credit, functioning purely as a priceless monument to bro-tier delusion).
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
- [x] Asset is ugly/low-effort with a named format crime (author, round v43, 2026-11-12: "The .BMP-to-.GIF Traumatic Conversion")
- [x] Route is location-flavoured (rigged arcade claw) and the artwork is not
- [x] Real brands left exactly as named (Sea-Monkeys)
