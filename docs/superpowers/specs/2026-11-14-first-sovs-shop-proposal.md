# First SOVS shop: proposal for author approval

- **Bead:** Eurobound-it49 (Economy Phase 1: SOVS shop runtime)
- **Date:** 2026-11-14
- **Status:** PROPOSED. Nothing here is in `game/assets/data/world_data/Shops.json` yet. Waiting on Eurobound Desk `Eurobound-it49-q2`.
- **Answers:** Desk `Eurobound-it49-q1`, author, verbatim: "Use an existing city shop from design/worlds; propose it from the docs for my approval".

Every price and line below is copied from a canon doc and cited. Nothing is invented. Where canon is silent, this says so.

## 1. The shop

**Midnight Munchies General Store** (`debaucheryville_shop_midnight_munchies_01`), Debaucheryville, Hostel Row. Shopkeeper: Věra Novotná.

- Location doc: `design/worlds/debaucheryville/midnight_munchies_general_store.md` (identity at lines 6-12)
- Shopkeeper profile: `design/worlds/debaucheryville/npcs/Midnight_Munchies_General_Store/npc_vera_novotna.md`
- Core data: `design/worlds/debaucheryville/core/midnight_munchies_general_store_core.json`

## 2. Why this one

1. **It has the most complete price list in Debaucheryville.** Four inventory tables, 28 rows, each with a SOVS price (`midnight_munchies_general_store.md:153-195`). The same 28 rows and prices are repeated in Věra's profile (`npc_vera_novotna.md:228-267`), which calls them "canon-locked from the source location file" (`npc_vera_novotna.md:447`).
2. **It is a plain shop.** All items visible, all prices marked, Věra rings it up (`midnight_munchies_general_store.md:144-149`). That is exactly what the built shop screen does: pick a row, pay, done.
3. **The stock is mostly simple recovery items.** Eight of the rows are HP food and drink, which is the shape the engine's consumables already have (`heal_hp`, `heal_bravado`).
4. **Prices fit the wallet.** A new game starts with 20 SOVS (`game/core/game_state.gd:39`); the stock runs 2 to 25 SOVS, so the player can buy some things and not others, which exercises the cannot-afford notice.

### Shops considered and not picked

| Shop | Zone | Why not first |
|---|---|---|
| The Strobe Survival Kit | "Absinthe Arcade, near club entrances" (`the_strobe_survival_kit.md:11`) | Closest to the built Arcade and has a full price table (`the_strobe_survival_kit.md:146-184`), but most rows are worn gear (earplugs, shades). `equipment.json` is empty and its schema is deferred (Eurobound-70z). "Prices increase after midnight" has no number (`the_strobe_survival_kit.md:19`). Good second shop. |
| The Bohemian Trap | "Absinthe Arcade, Neon Entertainment Quarter" (`the_bohemian_trap.md:11`) | Seven priced rows (`the_bohemian_trap.md:141-147`), all absinthe. Each one is an intoxication mechanic and needs the intoxication law's 10-point review first. |
| Backroom Concessions | Internet café back room (`backroomconcessions.md:10`) | Five priced items (`backroomconcessions.md:175-199`), but hidden behind Cyberspace Kavarna, which is not built. |
| Late-Night Kebab Stand, Mystery Meat Cart | Velvet Curtain Club alley; Cirque du Shady | Priced menus exist, but neither location is near anything built. |
| The Absinthium Taproom | "Hidden behind the Absinthe Arcade" (`the_absinthium_taproom.md:11`) | Sells one item, Absinthe Lager, 12 SOVS (`the_absinthium_taproom.md:227`). It is the only shop item that already has an engine entry with a price (`beer_absinthium_taproom`), but one row gated behind the brewery tour is not a shop slice. |

**Midnight Munchies is in Hostel Row, not next to the Arcade.** No Hostel Row scene exists yet. If being next to the Arcade matters more than a clean recovery stock, The Strobe Survival Kit is the alternative.

## 3. Stock list (canon, base prices)

Source file for every row: `design/worlds/debaucheryville/midnight_munchies_general_store.md`. Prices are the "Base Price" column. The "2AM+" column is listed in section 6.

### Healing: Recovery Section

| # | Item | Price | Source line |
|---|---|---|---|
| 1 | Energy Drink (Standard) | 3 SOVS | :156 |
| 2 | Energy Drink (Premium) | 5 SOVS | :157 |
| 3 | Energy Drink (Extreme) | 8 SOVS | :158 |
| 4 | Greasy Kebab | 6 SOVS | :159 |
| 5 | "Hair of the Dog" | 7 SOVS | :160 |
| 6 | Hangover Kit | 12 SOVS | :161 |
| 7 | Snack Bar | 2 SOVS | :162 |
| 8 | Instant Noodles | 3 SOVS | :163 |

### Support: Enhancement Section

| # | Item | Price | Source line |
|---|---|---|---|
| 9 | Caffeine Pills (6) | 6 SOVS | :168 |
| 10 | Lucky Club Stamp (Fake) | 8 SOVS | :169 |
| 11 | Emergency Phone Charger | 20 SOVS | :170 |
| 12 | Cigarettes | 8 SOVS | :171 |
| 13 | Lighter | 3 SOVS | :172 |
| 14 | Breath Mints (Tin) | 4 SOVS | :173 |
| 15 | Gum (Pack) | 2 SOVS | :174 |

### Offensive: "Just In Case" Section

| # | Item | Price | Source line |
|---|---|---|---|
| 16 | Pepper Spray | 15 SOVS | :179 |
| 17 | Personal Alarm | 10 SOVS | :180 |
| 18 | "Brass Knuckles" Keychain | 12 SOVS | :181 |
| 19 | Flash Grenades (Party Poppers) | 5 SOVS | :182 |
| 20 | Heavy Flashlight | 15 SOVS | :183 |

### Utility: Practical Section

| # | Item | Price | Source line |
|---|---|---|---|
| 21 | Club Earplugs | 10 SOVS | :188 |
| 22 | Fake VIP Wristband | 15 SOVS | :189 |
| 23 | Emergency Cab Voucher | 25 SOVS | :190 |
| 24 | Wet Wipes (Pack) | 4 SOVS | :191 |
| 25 | First Aid Kit (Basic) | 15 SOVS | :192 |
| 26 | Condoms (Pack) | 8 SOVS | :193 |
| 27 | Tissues | 2 SOVS | :194 |
| 28 | Safety Pins | 2 SOVS | :195 |

### Left out of the proposed stock

| Thing | Why |
|---|---|
| Sausage and "mystery item" at the heat lamp | Named at `midnight_munchies_general_store.md:82` and `:206`. **No price in canon.** |
| Hand warmers | Věra gives them away free in a dialogue beat (`midnight_munchies_general_store.md:266`). Not stock. |
| Bag | "Need a bag? ...1 SOV." (`midnight_munchies_general_store.md:250`). A checkout line, not a shelf item; the shop screen has no bagging step. |
| Coffee | A customer NPC exchange quotes "4 SOVS" (`midnight_munchies_general_store.md:281`), but coffee is not in any inventory table. Not treated as stock. |
| Aspirin | Mentioned in dialogue and as "3 SOVS at pharmacy: 8 SOVS here" (`midnight_munchies_general_store.md:131`), but there is no aspirin row in the inventory tables. Not treated as stock. |
| Emergency Hygiene Kit | See the conflict below. |

## 4. Canon conflict the author should know about

`design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` is a shorter list of five items that does not match the location doc. It marks itself `"price_confirmation_required": true` (line 59). This proposal follows the location doc, because the core JSON names it as the canon source (`midnight_munchies_general_store_core.json:12-15`).

| Items JSON (line) | Location doc |
|---|---|
| `mm_energy_drink` "Emergency Energy Drink", 4 SOVS (:6-9) | Three energy drinks at 3, 5 and 8 SOVS (:156-158). 4 SOVS is the Standard drink's after-2AM price. |
| `mm_instant_noodles` "Instant Noodles", 3 SOVS (:14-17) | Matches (:163). |
| `mm_heat_lamp_kebab` "Heat-Lamp Kebab", 6 SOVS (:22-25) | "Greasy Kebab", 6 SOVS (:159). Same price, different name. |
| `mm_hygiene_kit` "Emergency Hygiene Kit", 12 SOVS (:30-33) | Not in the location doc at all. Left out of the proposed stock. |
| `mm_earplugs` "Budget Earplugs", 5 SOVS (:38-41) | "Club Earplugs", 10 SOVS (:188). |

Filed as a bead for an author ruling (see section 8).

## 5. Engine entries

The shop screen can only sell an item that exists in `game/assets/data/items/consumables.json`, `key_items.json` or `equipment.json` (`game/core/shop_catalog.gd:112-114`).

- **Have an engine entry: none of the 28.**
- **Need an engine entry: all 28.**

Notes:

- `lukewarm_kebab` exists in `consumables.json`, but it is a different item (an enemy drop, `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/condiment_clan_ninja.md:182`). It is not the Greasy Kebab and is not swapped in here.
- The 8 Recovery rows have HP numbers in canon (`midnight_munchies_general_store.md:156-163`) and could be entered with the existing consumable fields. Their side effects (Speed, crash, Grease Fingers, Hangover cure) have no engine status yet.
- The other 20 rows have effects the engine has no field for today (Confidence, Charm, phone charge, transport, weapons). Several are gear, and `equipment.json` has no schema yet (Eurobound-70z).
- None of the 28 has an item design doc in `design/items/`. Per the template rule, each needs one before it is synced to the engine.

So the Shops.json entry in section 7 cannot ship until these items exist. That is follow-up work (section 8), not part of this approval.

## 6. Canon the built shop screen does not do yet

| Canon | Source | Runtime today |
|---|---|---|
| Open 10 PM to 8 AM only | `midnight_munchies_general_store.md:16` | Shops.json has no hours field. |
| Desperation Tax: 2 AM to 6 AM, "All prices +20-30%", with a per-item "2AM+ Price" column | `:198-202`, column in `:154-195` | One price per row. The proposal uses the base price. |
| Heat Lamp Lottery (60 / 30 / 10 quality roll on the kebab) | `:204-212` | Not built. |
| "Regular" status after 5 purchases | `:214-219` | Not built. |
| "Could Have Planned Ahead" notification | `:226-230` | Not built. |
| Bag for 1 SOV | `:250` | Not built. |

Note: the "2AM+ Price" column and the "+20-30%" rule are both canon; the column is the exact number per item, so no rounding rule needs inventing when this is built.

## 7. Cannot-afford line

**Canon has no cannot-afford line for Věra.** Neither the location doc nor her profile has a line for a customer who is short of SOVS.

The nearest lines are for other situations and are not proposed as substitutes:

- Complaining about prices: "Yes." *(nothing else)* (`npc_vera_novotna.md:146-147`)
- Attempting to negotiate: "No." (`npc_vera_novotna.md:149-150`)
- Leaving without buying: "Nothing tonight. Fine. There's a shop that opens at seven if you can wait four hours. You can't. But it's there." (`npc_vera_novotna.md:155-156`)

**It needs writing, by the author** (through the Writers' Room if the author wants options; the author approves the line). Until then the entry carries no `cannot_afford_notice`, and the screen shows its plain fallback "NOT ENOUGH SOVS" (`game/ui/sovs_shop.gd`), which is itself still waiting on author copy (asked in Desk `Eurobound-it49-q1`).

## 8. PROPOSED Shops.json entry

**PROPOSED. Do not paste into `Shops.json` until the author approves and the items exist in the engine.**

The item ids are provisional. Canon only has ids for three of these rows, and those sit in the conflicting items JSON (section 4). Final ids are set when each item gets its design doc and engine entry.

```json
{
  "schema_version": "1.0",
  "shops": {
    "midnight_munchies_general_store": {
      "display_name": "Midnight Munchies General Store",
      "currency": "SOVS",
      "location_id": "debaucheryville_shop_midnight_munchies_01",
      "stock": [
        {"item_id": "mm_energy_drink_standard", "price": 3},
        {"item_id": "mm_energy_drink_premium", "price": 5},
        {"item_id": "mm_energy_drink_extreme", "price": 8},
        {"item_id": "mm_greasy_kebab", "price": 6},
        {"item_id": "mm_hair_of_the_dog", "price": 7},
        {"item_id": "mm_hangover_kit", "price": 12},
        {"item_id": "mm_snack_bar", "price": 2},
        {"item_id": "mm_instant_noodles", "price": 3},
        {"item_id": "mm_caffeine_pills", "price": 6},
        {"item_id": "mm_lucky_club_stamp_fake", "price": 8},
        {"item_id": "mm_emergency_phone_charger", "price": 20},
        {"item_id": "mm_cigarettes", "price": 8},
        {"item_id": "mm_lighter", "price": 3},
        {"item_id": "mm_breath_mints", "price": 4},
        {"item_id": "mm_gum", "price": 2},
        {"item_id": "mm_pepper_spray", "price": 15},
        {"item_id": "mm_personal_alarm", "price": 10},
        {"item_id": "mm_brass_knuckles_keychain", "price": 12},
        {"item_id": "mm_flash_grenades", "price": 5},
        {"item_id": "mm_heavy_flashlight", "price": 15},
        {"item_id": "mm_club_earplugs", "price": 10},
        {"item_id": "mm_fake_vip_wristband", "price": 15},
        {"item_id": "mm_emergency_cab_voucher", "price": 25},
        {"item_id": "mm_wet_wipes", "price": 4},
        {"item_id": "mm_first_aid_kit_basic", "price": 15},
        {"item_id": "mm_condoms", "price": 8},
        {"item_id": "mm_tissues", "price": 2},
        {"item_id": "mm_safety_pins", "price": 2}
      ],
      "_pending": {
        "cannot_afford_notice": "No line in canon for Věra; needs writing by the author.",
        "item_ids": "Provisional; set when each item gets its design doc and engine entry.",
        "desperation_tax": "2AM+ prices (midnight_munchies_general_store.md:154-202) are not in this schema.",
        "hours": "10 PM to 8 AM (midnight_munchies_general_store.md:16) is not in this schema."
      }
    }
  }
}
```

The shape follows the schema in `game/core/shop_catalog.gd:7-25`. "Caffeine Pills (6)" is one purchase of one pack, so no `count` is set.

## 9. What happens after approval

1. Item design docs and engine entries for the approved rows (bead filed, blocked on this answer).
2. The author's ruling on the items JSON conflict (bead filed, `author-ruling`).
3. Věra's cannot-afford line from the author.
4. Paste the approved entry into `Shops.json`, run `Tools/validate_data.py`.
5. Later, separately: hours, Desperation Tax, Heat Lamp Lottery, Regular status (bead filed), and a Hostel Row scene to put the shop in.
