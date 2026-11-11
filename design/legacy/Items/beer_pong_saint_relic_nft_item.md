# NFT: Beer Pong Saint Relic — ⛔ STRUCK

> **⛔ STRUCK — do not use.** The Beer Pong Saint Relic was struck from the NFT roster on 2026-08-01
> (spec §7c, location-derived). On 2026-11-11 the author settled the conflict below (round v29
> `relic_nft`, Writers' Room desk 15:21), verbatim: **"replace the beer pong saint relic with
> Sea-Monkey"**. The rigged absinthe claw pays **Sea-Monkeys (Mint #73)**: see
> `design/items/sea_monkeys_nft_item.md` (engine key `sea_monkeys`, flag `sea_monkeys_obtained`).
> This file moved from `design/items/` to `design/legacy/Items/` and is kept for history only.
> Its Q1/Q2 are answered; its proposed card copy, mint number and bro lines are void.

*Written 2026-11-11 by author order (round v28: "Write the Beer Pong Saint Relic doc from canon
(NFT template) and register it."). Built from `design/templates/NFT_Template.md`. Every field is
either sourced to canon (source named) or marked **PROPOSED — NEEDS AUTHOR RULING**. Nothing in
this doc is invented silently.*

---

## ⚠ CANON CONFLICT — author ruling needed before this NFT is final

Two sets of author rulings disagree about this NFT. This doc does not pick a side.

1. **2026-08-01 strike (spec §7c).** `design/Quests/debaucheryville/nfthuntdebaucheryville.md`
   and `design/economy/legacy_vault_cards.md` (Card 2) record the Beer Pong Saint Relic as
   **struck as location-derived** and replaced, route unchanged, by **Sea-Monkeys (Mint #73)**,
   whose card copy is author-only and still empty. The roster in `legacy_vault_cards.md` §2 holds
   twelve NFTs, four per city, and the relic is not among them.
2. **2026-11-11 rulings (rounds v26 and v28, `docs/superpowers/NEXT_WORK.md`).** The approved
   claw rig "pays the Beer Pong Saint Relic or nothing until the relic is won", and v28 orders
   this doc written and registered. The arcade design JSONs (items, interactions, core state,
   NPC triggers) all point at `item_beer_pong_saint_relic`.

**Questions for the author:**
- **Q1.** Is the relic reinstated as Debaucheryville's claw-machine NFT, which retires Sea-Monkeys
  from that route? Or does Sea-Monkeys stay as the NFT, with the relic as the claw's non-NFT prize?
  The game has twelve NFT slots, and both cannot hold slot 2.
- **Q2.** If it is reinstated, does it pass §7c? The red Solo cup is American college beer-pong
  culture of the 90s/00s, which is in bounds. The "Saint Relic" religious-icon framing could be
  read as drawn from the host city's relic tourism, which would be location-derived. That reading
  is a guess at why it was struck in August; no surviving record says why.

Until the author rules, the engine entry carries identity and description only (`effect: null`).

---

## ⛔ Binding rules (from the template, unchanged)

The artwork is 90s/00s pop culture and never location-derived. The game never winks. The bros are
never scam-aware. No mascots. The title never names the property outright. MA satire at full
strength.

---

## 1. Identity

| Field | Value | Source |
|---|---|---|
| **Display Name** | Beer Pong Saint Relic | canon: `absinthe_arcade_items.json`, `fratbronft.md` |
| **Mint Number** | **PROPOSED — NEEDS AUTHOR RULING:** `Mint #06` (2006, the first World Series of Beer Pong: the year the basement sport went pro) | not in canon |
| **Item ID** | `item_beer_pong_saint_relic` | canon: `absinthe_arcade_items.json`, `absinthe_arcade_interactions.json`. The template pattern would be `item_nft_beer_pong_saint_relic`. The canon id is kept because four design files and the engine state flag already use it |
| **Engine key** | `beer_pong_saint_relic` (in `key_items.json`) | key_items schema ruling 2026-08-06: bare snake_case key (`item_student_id` → `student_id`) |
| **Item Type** | Quest item, permanent: `unique_quest_collectible`, not stackable, not consumable, rarity unique | canon: `absinthe_arcade_items.json` |
| **City** | Debaucheryville | canon |
| **Collection Slot** | Debaucheryville target 2 of 4, **contested** (see Canon Conflict Q1) | `fratbronft.md` lists it second; `legacy_vault_cards.md` gives slot 2 to Sea-Monkeys |
| **Media Type** | Still image: a low-resolution icon | canon: `absinthe_arcade_items.json` ("low-resolution icon") |

## 2. Acquisition

| Field | Value | Source |
|---|---|---|
| **Route** | Rigged Absinthe Arcade claw machine (`rigged_absinthe_claw_machine`) | canon: `absinthe_arcade_interactions.json`, `fratbronft.md`, `absinthearcade.md` |
| **Venue** | Absinthe Arcade, claw alcove (`aa_node_claw_alcove`), Debaucheryville: `design/worlds/debaucheryville/absinthearcade.md` | canon |
| **Unlock Condition** | Pay 5 Absinthe Arcade tokens per play. Steer left or right for up to 10 seconds, then drop; the claw grabs whatever is under it. The claw slips on every grab unless the PAYOUT light is blinking. The plays counter is saved: after 6 plays the light blinks *before* the bros pay for the 7th, and that grab holds only if the claw is over the relic. The cycle restarts after any blinking play, win or miss. The Token Attendant, Jakub "Tokens" Dvořák, hints at the cycle. | canon: rounds v26, v27, v28 (`NEXT_WORK.md`); claw cost 5 tokens (ticket-game numbers, v25) |
| **Sets State** | `beer_pong_saint_relic_obtained` | canon: `absinthe_arcade_core.json`, `absinthe_arcade_interactions.json` |
| **After the Win** | The relic hook hangs empty. From then on the claw pays junk-shelf prizes, never a second relic. | canon: interactions `post_win_state`, v26 ruling |
| **Location Completion** | Getting the relic is the Absinthe Arcade's completion requirement. | canon: `absinthearcade.md` Exit Conditions |
| **Dispense Audio** | `fur_elise_crypto_victory_remix.ogg` | canon: `absinthe_arcade_items.json` |
| **NPC Trigger** | The arcade staffer's `you_actually_won_that` dialogue set fires on `beer_pong_saint_relic_obtained`. That staffer's job merged into the Token Attendant in round v26. The lines themselves are unwritten. | canon: `absinthe_arcade_npcs.json`; merge per v26 |

**Acquisition Beat** (staged from canon; no dialogue invented):
The relic hangs inside the cabinet on a gold thread. The bros pay, steer and drop, and the claw
slips, again and again. On the seventh play the PAYOUT light is already blinking before anyone
inserts a token. The claw closes over the relic and holds. The machine plays a crypto victory
remix of *Für Elise*. The Token Attendant does a double take (the canon animation
`claw_win_double_take`).

**Superseded acquisition text, do not use:** the older "rigged physics requiring strategy over
luck" and "counter-swing / service-note / shake-meter" methods (`absinthearcade.md`, older
interactions drafts) were dropped in round v27. The every-7th-play PAYOUT light replaces them.

## 3. The Artwork Itself

- **Description of the asset** (canon, `absinthe_arcade_items.json` + `fratbronft.md` +
  `absinthearcade.md`): a red Solo cup wearing a gold-green, eight-bit halo; a deliberately bad
  MS Paint religious icon; intentionally ugly and low-resolution. Its provenance is "elaborate,
  unverifiable and printed on the back in six-point type". In the arcade it hangs inside the claw
  machine on a gold thread.
- **Format crime:** **PROPOSED — NEEDS AUTHOR RULING:** drawn at 32×32 and blown up with
  nearest-neighbour scaling to fill a holy card. The halo is a hand-placed ring of gold and green
  pixels, one pixel off-centre. The MS Paint spray-can tool was used for "divine light", and the
  Solo cup's rim is drawn in the default MS Paint red with the line tool, not quite closed.
- **File/asset name:** inventory icon `aa_ui_beer_pong_saint_relic` (canon). Full-size NFT image
  **PROPOSED — NEEDS AUTHOR RULING:** `nft_beer_pong_saint_relic.png`.
- **The provenance text on the back:** canon says it exists and is six-point. Its wording is
  **unwritten, NEEDS AUTHOR RULING**. No draft is offered here, because it overlaps with the
  Acquisition Story card field.

## 4. Card Copy — Legacy Vault

> Precedent: the author has written or reserved the card copy for every NFT since 2026-08-01
> (`legacy_vault_cards.md` §1a.8). The drafts below are offered only because the v28 order asks
> for a filled doc. Every line is **PROPOSED — NEEDS AUTHOR RULING** and may be struck outright
> in favour of the author's own copy. None of it is in the engine.

**Tagline** — **PROPOSED:** "Canonized liquidity."

**Description** — **PROPOSED:** "Before prediction markets, an entire generation of American
undergraduates staked their GPA, their dignity and somebody else's security deposit on whether a
ping-pong ball would land in sixteen ounces of Natty Light. This asset canonizes the sport's
patron: a single red Solo cup, haloed in eight bits, presiding over every rerack, every elbow
foul and every fraternity basement condemned in its name."

**Collector's Thesis** — **PROPOSED:** "A saint with a perfect record: it has never missed,
because nobody has ever thrown at it. Intrinsic value: one rerack. Market sentiment: beatified."

**Estimated Future Value** — **PROPOSED:** "Pending canonization."

**Edition Tag** — **PROPOSED:** "Edition 1 of 1 · Relic Grade". The 1-of-1 is backed by canon:
the claw pays exactly one and then never again.

## 5. Bros' Reaction

*All three lines are **PROPOSED — NEEDS AUTHOR RULING**. Canon has no bro dialogue for this NFT.*

- **Lord Pilsner:** "You don't win a relic, boys. A relic picks the hand. It picked thirty-five
  tokens' worth of hand."
- **Chadwick:** "Chat. It's a saint. On the chain. You cannot rug a saint."
- **Bradley:** "I've drunk out of like nine thousand of these. So technically I've been
  collecting this my whole life."

## 6. System Integration

- **Counts toward:** the Ultimate Brochain Collection (12 in the base game; milestones at
  4 / 8 / 12; NEXT_WORK standing rulings). Counted **only if Q1 reinstates it**. Otherwise the
  slot belongs to Sea-Monkeys.
- **Wallet tab:** The Legacy Vault (template §6; `legacy_vault_cards.md`).
- **Resale value:** 0 SOVS everywhere. It cannot be sold, traded or redeemed, and every vendor
  declines it. This is canon for every NFT (template §6, `legacy_vault_cards.md` §1a.2).
- **Stats / effects:** **PROPOSED — NEEDS AUTHOR RULING:** none (`effect: null`). It is a
  collection piece and does nothing in the field or in battle. The one NFT precedent,
  `tractor_nft_item.md`, gives +1 Bravado and +2 Charm (Bros). The author may want parity, so
  the choice is flagged rather than assumed.
- **Engine registration:** `game/assets/data/items/key_items.json` → `beer_pong_saint_relic`,
  `item_class: "quest"`. No entry in key_items.json uses an "nft" class, and the schema allows
  only permanent / curse / quest.
- **Related files:**
  - `design/World Design/Debaucheryville/items/absinthe_arcade_items.json` (design entry)
  - `design/World Design/Debaucheryville/interactions/absinthe_arcade_interactions.json` (claw rig)
  - `design/World Design/Debaucheryville/core/absinthe_arcade_core.json` (state flags)
  - `design/World Design/Debaucheryville/npcs/Absinthe_Arcade/absinthe_arcade_npcs.json` (`you_actually_won_that`)
  - `design/worlds/debaucheryville/absinthearcade.md` (venue)
  - `design/Quests/debaucheryville/nfthuntdebaucheryville.md`, `design/Quests/fratbronft.md` (quest)
  - `design/economy/legacy_vault_cards.md` (Card 2: currently Sea-Monkeys)

### Stale engine data (flagged, not touched)
`game/assets/data/locations/debaucheryville/debaucheryville_interactions.json` (~line 660–680)
still describes the pre-v27 skill-based claw and grants an item named
`beer_pong_saint_relic_nft`. `debaucheryville_locations.json` and
`debaucheryville_locations_core.json` require `obtain_beer_pong_saint_relic_nft`. Neither name
matches the canon id or the new engine key. Those files belong to another session.

### Repo defect (flagged, not touched)
`design/Quests/fratbronft.md` contains unresolved git merge-conflict markers
(`<<<<<<< HEAD` … `>>>>>>> 531592d…`) around the NFT roster, including this relic's line.

## 7. Validation Checklist

- [ ] Artwork is 90s/00s pop culture, **not** location-derived. **Open (Q2):** the Solo cup
  passes; the religious-relic framing may not.
- [x] Title is an oblique rebrand, not a literal property name
- [ ] Mint number evokes the artifact's year (#06 PROPOSED)
- [x] Nothing in any copy field winks, explains, or acknowledges worthlessness
- [x] Bros are never scam-aware; the seller/minter always knew
- [x] No mascot, companion, or talking entity introduced
- [ ] Asset is ugly/low-effort with a named format crime (format crime PROPOSED)
- [x] Route is location-flavoured (rigged arcade claw)
- [x] Real brands/properties left exactly as named (Solo, Natty Light, *Für Elise*)
