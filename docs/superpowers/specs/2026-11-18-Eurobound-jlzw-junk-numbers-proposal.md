# Golden Cutlet Junk Items: Numbers Proposal (Eurobound-jlzw)

> **Status: PROPOSAL, waiting on the author** (Eurobound Desk `Eurobound-jlzw-q2`).
> Author's direction, verbatim (Eurobound Desk `Eurobound-jlzw-q1`, 2026-11-18): "An agent proposes numbers for all ten from the existing junk items, for my approval".
> **Every number in this file is PROPOSED.** Each one is copied from a named existing junk item, with a one-line reason.
> Nothing in `game/` or `design/` was changed. No name, description or inspect line is touched: the approved inspect
> lines stay verbatim (Eurobound-2kty-q1) and go into the engine `description` field unchanged at sync time.

Audience check: younger Gen X, xennial and millennial women. Junk is a joke you get paid pocket change to read; the numbers
keep it pocket change so nobody farms the Golden Cutlet for money.

## 1. What the existing junk items carry

The engine has three registered enemy junk drops, the Frogger: Existential Edition set. Their shape is the target shape for
all ten (bead acceptance: "same file and shape as the Frogger junk drops").

| Item | Engine entry | Fields | Enemy side |
|---|---|---|---|
| Auto-Gratuity Receipt | `game/assets/data/items/key_items.json:279` | `item_class: "permanent"`, `source: "croc_monsieur_drop"`, `sell_value: 1`, `effect: null` | `debaucheryville_enemies.json:28-29`: `item_drop`, `drop_chance: 1.0` |
| Fuzzy Dice of Doubt | `key_items.json:287` | `sell_value: 2` | `debaucheryville_enemies.json:42-43`: `drop_chance: 1.0` |
| Shell Company Business Card | `key_items.json:295` | `sell_value: 4` | `debaucheryville_enemies.json:56-57`: `drop_chance: 1.0` |

Their design docs call each one a "**Guaranteed drop** ... Junk/sell item, vendor value N SOVS"
(`croc_monsieur.md:229`, `hit_and_ponder_hatchback.md:216`, `sinking_fund.md:225`, all under
`design/worlds/debaucheryville/villains/absinthe_arcade/frogger_existential_edition/`; approved 2026-11-09).

Other junk on the curve:

| Item | Numbers | Source | Use here |
|---|---|---|---|
| Clock Snow Globe | Rarity common; price 25 SOVS; actual value 3 SOVS; sells back for 1 SOV | `design/items/debaucheryville_items/clock_snow_globe_item.md:12-14` (design data, not yet in engine) | Rarity label; the souvenir comparable |
| Lukewarm Kebab (Feral Segway Tourist) | `drop_chance: 1.0` | `debaucheryville_enemies.json:15-16` | The one regular street enemy: its drop is guaranteed too |
| Arcade junk shelf (Terminal Velocity Terry, Forty-Eight-Hour Tramp Stamp, The Noise Violation, Promise-ish Ring) | 10 / 10 / 15 / 5 **tickets**, no `sell_value` | `key_items.json:209-237`; `docs/superpowers/NEXT_WORK.md:605` | Not used: priced in tickets, not SOVS, and not sellable |
| Arcade claw plush (`aa_claw_*`) | No price, no `sell_value` | `key_items.json:129-207` | Not used: prizes, not junk |

What the schema does **not** have: no `rarity` field and no `max_stack` on any `key_items.json` entry (`max_stack` appears
only on consumables, e.g. the Regret-Free Kebab Coupon's `5`). Rarity lives in the item doc only. So the numbers to set are: `sell_value`,
`drop_chance` (enemy side), and the doc fields Rarity, Actual Value and Resale Value.

## 2. Rules used

1. **Stay on the existing curve: 1, 2 or 4 SOVS.** No new tier. No city mark-up: nothing in the ledger scales prices by city,
   so Sinfonia (third city, `design/worlds/city_progression_order.md:9`) uses the Debaucheryville curve.
2. **Value follows the object, not the enemy.** The Frogger values ignore enemy strength (Croc Monsieur, the toughest at 52 HP,
   drops the 1-SOV receipt). The Golden Cutlet enemy stats are all still PENDING anyway, so object type is the only basis.
3. **Enemy junk is a guaranteed drop (`drop_chance: 1.0`)**, like the three Frogger enemies, and like the Feral Segway Tourist's
   kebab (the one regular street enemy in data).
4. **Rarity: Common** for all ten, like the Clock Snow Globe and the guaranteed Frogger drops. The doc's "(bros think it's ...)"
   half is content, not a number, and stays PENDING (author).
5. **Actual Value = Resale Value.** The Frogger docs give one "vendor value"; the snow globe splits the two only because a
   shop marks it up. Nobody sells these.
6. **No `max_stack`**, like the three Frogger entries.

## 3. The seven enemy drops

| Item (engine key) | Enemy | Rarity | Sell value | Drop chance | Comparable | Reason |
|---|---|---|---|---|---|---|
| Loose Breastplate Crumbs (`loose_breastplate_crumbs`) | The Triple-Dredged Knight | Common | **1 SOV** | **1.0** | Auto-Gratuity Receipt (1) | Scrap shed off a costume, worth what the receipt is: nothing, plus one |
| Splintered Mallet Head (`splintered_mallet_head`) | Tableside Thumper | Common | **2 SOVS** | **1.0** | Fuzzy Dice of Doubt (2) | A broken but solid prop, the dice's tier of cheap physical object |
| Page Two of the Pass (`page_two_of_the_pass`) | The Living Asterisk | Common | **4 SOVS** | **1.0** | Shell Company Business Card (4) | Same job as the card: the paperwork of the scam that runs the dungeon, so same top-of-curve value |
| Souvenir Frame (Empty) (`souvenir_frame_empty`) | Flash Pillory | Common | **1 SOV** | **1.0** | Clock Snow Globe (sells back for 1) | A tourist-trap souvenir; the snow globe sets what a souvenir sells back for |
| Plastic Goblet, Sticky (`plastic_goblet_sticky`) | On-The-House Wenches | Common | **2 SOVS** | **1.0** | Fuzzy Dice of Doubt (2) | Intact cheap plastic novelty, the dice's tier |
| Turnip, Bitten (`turnip_bitten`) | Method Peasant | Common | **2 SOVS** | **1.0** | Fuzzy Dice of Doubt (2) | Spoiled produce would be 1, but it carries a whole object (the veneer), so one step up |
| Lemon Wedge, Used (`lemon_wedge_used`) | Total Plate Eclipse | Common | **1 SOV** | **1.0** | Auto-Gratuity Receipt (1) | Used-up table leftover from a meal, the receipt's tier |

The Voluntold Wrangler is not in this set: whether he gets a junk drop is still an open author question (Eurobound-lei5).
If he gets none, the existing pattern is `item_drop: null`, `drop_chance: 0.0` (four drop-less Debaucheryville enemies,
`debaucheryville_enemies.json:153-196`).

## 4. The three trap-door finds (The Schnitzel King, Phase 2)

Canon: each *Trap Door Ruling* sends a bro into the vault and he always comes back "holding a junk item"
(`design/worlds/sinfonia/villains/the_golden_cutlet/the_schnitzel_king.md:174`, `:185`). So the find itself is certain; the
number to set is which of the three he brings back.

| Item (engine key) | Rarity | Sell value | Find chance per trap door | Comparable | Reason |
|---|---|---|---|---|---|
| Bachelor Party VIP Lanyard (`bachelor_party_vip_lanyard`) | Common | **4 SOVS** | **1 in 3** (weight 1) | Shell Company Business Card (4) | A status credential on a string, the closest object match to the card |
| Half a Pair of Lederhosen (`half_a_pair_of_lederhosen`) | Common | **2 SOVS** | **1 in 3** (weight 1) | Fuzzy Dice of Doubt (2) | Half a garment: solid, unusable, the dice's tier |
| Bachelor Party Disposable (`bachelor_party_disposable`) | Common | **4 SOVS** | **1 in 3** (weight 1) | Shell Company Business Card (4) | The only one of the ten that still works (one shot left), so it takes the curve's top |

Find chance: certain per trap door (canon), item picked at equal weights 1:1:1; a repeat is possible. How often *Trap Door
Ruling* fires and how long the bro is gone are the King's numbers (balancing pass, bead Eurobound-26v) and are not proposed here.

## 5. Against the existing junk curve

| Set | Items | Sell values (SOVS) | Mean | Drop |
|---|---|---|---|---|
| Frogger: Existential Edition (existing, approved) | 3 | 1, 2, 4 | 2.3 | 1.0 each |
| Clock Snow Globe (existing, design data) | 1 | 1 | 1.0 | shop item |
| **Golden Cutlet enemy drops (proposed)** | 7 | 1, 1, 1, 2, 2, 2, 4 | 1.9 | 1.0 each |
| **Golden Cutlet trap-door finds (proposed)** | 3 | 2, 4, 4 | 3.3 | certain per trap door, 1 in 3 each |
| **All ten (proposed)** | 10 | 1 ×3, 2 ×4, 4 ×3 | 2.3 | |

Full sweep (one of each enemy type): 13 SOVS of junk; the Frogger cabinet's three enemies: 7. No value above 4 SOVS, so every one
sells for less than the cheapest SOVS-priced item in `consumables.json` (Oude Genever, 6 SOVS, `consumables.json:123`).

## 6. What the sync writes after approval (bead Eurobound-jlzw, not done now)

One `key_items.json` entry per item, Frogger shape, for example:

```json
"loose_breastplate_crumbs": {
  "display_name": "Loose Breastplate Crumbs",
  "item_class": "permanent",
  "source": "triple_dredged_knight_drop",
  "sell_value": 1,
  "effect": null,
  "description": "<approved inspect line, verbatim>"
}
```

Trap-door finds use `"source": "schnitzel_king_trap_door_find"`. Each item doc gets Rarity, Actual Value and Resale Value
(and Can Be Sold: yes, which follows from having a sell value); Can Be Dropped and Can Be Traded are not numbers and stay
PENDING (author). The seven enemy docs get `item_drop` and `drop_chance`; `game/assets/data/enemies/sinfonia_enemies.json` is
still empty, so the enemy-side values land when bead Eurobound-26v registers the enemies. The engine has no item-pool field for
a boss move that hands out an item (no `item_pool`, `loot_table` or `grant_item` anywhere in `game/`), so the 1:1:1 trap-door
weights need a home; that gap is filed as its own bead.
