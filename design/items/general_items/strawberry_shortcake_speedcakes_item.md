# Item Definition: STRAWBERRY SHORTCAKE SPEEDCAKES™

*"YOU CANT SPELL SHORTCAKE WITHOUT GOING REALLY FAST" - Tony420, Midweek Drop*

> Built from `design/templates/consumable_item_template.md` v1.0. Design approved by the author 2026-11-11 (price coin, inspect line, effects, delivery, filing). Balance numbers are pending; fields the author has not ruled on are still marked **PROPOSED** or **pending author**.

## 📋 Item Identity
- **Item ID**: `item_strawberry_shortcake_speedcakes` (unique: no repo hits for "strawberry_shortcake" before this file, grep 2026-11-11)
- **Engine Key**: `strawberry_shortcake_speedcakes`
- **Display Name**: STRAWBERRY SHORTCAKE SPEEDCAKES™
- **Subtitle / Product Line**: Disposable Dessert-Grade Vape (author canon, 2026-11-11)
- **Internal Name**: **PROPOSED:** a gas-station disposable vape in strawberry-frosting flavor, cut with a stimulant
- **Item Type**: Consumable
- **Subtype**: vape / stimulant
- **Rarity**: Pending author
- **Vendor / Source**: Tony420 (`debaucheryville_npc_tony420_01`), ICQ broadcast "TONY420 MIDWEEK DROP". He is never seen in person
- **Location**: ICQ, any FREE Wi-Fi hotspot. Tony's ICQ reach covers all four cities (`npc_tony420.md`). Ordered over ICQ, delivered by dead drop (see Delivery below)

**Canon lineage:** replaces the retired "FLINTSTONES FENTANYL VAPES" (25 SOVS, `design/quests/general_quests/darkwebdossiercrossoverevents.md:398`). Author framing: "“Shortcake” → “Speedcake” is stupid in exactly the correct Tony420 way. It sounds like a product that absolutely should not exist."

---

## 🎭 The Deception

### What It Actually Is
**PROPOSED:** A disposable vape in a pink shrink-wrap sleeve with a cartoon slice of Strawberry Shortcake on it, the shrink-wrap applied slightly crooked by hand. It tastes like the frosting on a cake that has been in a gas-station fridge since the Clinton administration. It is not a dessert. The "SPEED" is not a metaphor.

### What The Bros Believe It Is
**PROPOSED:** "It's a dessert you breathe, bro. Bakery fresh. Zero carbs. Tony says it's *motivating*, which is basically a supplement. This is how Europeans stay thin." They think Tony fronted them a wellness product, and they think the motivation is a personality upgrade.

### The Comedy Gap
**PROPOSED:** They think they bought a snack with drive. They get a bro who will not stop cleaning, will not stop talking, and then cannot get up. The player reads "NO REFUNDS IF YOU CLEAN YOUR WHOLE APARTMENT" as a warning label. The bros read it as a guarantee.

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | **420 VapeSwap ($HUFF)** (`design/economy/shitcoin_master_pool.md` #24). Coin approved by the author ("1 $HUFF is perfect. And you choose the price.", 2026-11-11); amount chosen by the moderator at the author's direction. Its SOVS value follows $HUFF's rate, which is pending the author's economy pass |
| **Actual Value** | Pending author |
| **Resale Value** | Pending author |
| **Can Be Sold** | Pending author |
| **Stack Size** | Pending author |
| **Bundle Deals** | None ruled |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | "Tastes like strawberry frosting licked off a car battery." | Canon (author, 2026-11-11) |

---

## 📣 Vendor Pitch Copy

### Pitch
Author canon, verbatim (also in `design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md`, Spam Broadcast: Midweek Drop):
```
🔥TONY420 MIDWEEK DROP🔥
🍓 STRAWBERRY SHORTCAKE SPEEDCAKES 🍰
BERRY SWEET 💯 BAKERY FRESH 💯 INCREDIBLY MOTIVATING 💯
"YOU CANT SPELL SHORTCAKE WITHOUT GOING REALLY FAST"
NO REFUNDS IF YOU CLEAN YOUR WHOLE APARTMENT
```

### Purchase Line
> Pending author. No purchase reply has been written for this product.

### Delivery
Author ruling (2026-11-11), verbatim: "A drop. All tony delivered things are drop delivered, unless a goon is already in a scene, or it's somewhere sheisty (say he's dealing with another darkweb adjacent character or they're at the kavarna or the shadow exchange)"

- **Default**: dropped by Tony420 as a dead drop. Tony is never seen.
- **Goon exception**: if one of Tony's goons is already in the scene, or the scene is somewhere sheisty (a darkweb-adjacent character is involved, or the bros are at the Cyberspace Kavarna or the Shadow Exchange), the goon hands it over instead (goon-and-tablet staging).
- Drop spot, drop message and pickup interaction: pending author.

---

## 📊 Effects on Use

**APPROVED (author, 2026-11-11):** the effect design below, including the "Sugar Rush Hour" name, the cleaning compulsion, the Crash follow-up, the stack rules and the battle cleaning behaviour. **No numbers are set**: every value marked TBD waits for the balancing pass.

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| HP restored | 0 | Instant | — | `heal_hp`. It is not food, whatever the sleeve says |
| Bravado restored | Pending author (registered as 0) | Instant | — | `heal_bravado`. The approval did not set an on-use Bravado value; the engine entry carries 0 until the balancing pass. In battle he gets Bravado by stealing it instead (below) |
| Status applied | "Sugar Rush Hour" (APPROVED new status; name unused in repo) | Short, TBD | Second hit while active extends the cleaning compulsion and stacks the crash, never the speed | +Speed (TBD), faster dialogue text, jaw-clench idle animation, −Accuracy (TBD) |
| Cleaning compulsion | Overworld loss of control (APPROVED) | Bounded, TBD | Extends on re-use | The bro breaks off at intervals to wipe, scrub or straighten the nearest interactable. Any hostel rest while active: he deep-cleans the whole room overnight |
| Battle cleaning | Physical attacks become cleaning hits (APPROVED, author 2026-11-11) | While Sugar Rush Hour is active | Does not stack; on or off with the status | Damage reduced (TBD). Each cleaning hit steals some of the enemy's Bravado (TBD), which goes to the bro. See Battle Cleaning below |
| Delayed effect | "Crash" (existing status, `design/mechanics/Battle/status_effects.md`: −3 all stats, 75% skip turn) | Per existing status | Stacks per hit taken | Fires when Sugar Rush Hour ends. The bill for everything above |

### Battle Cleaning (APPROVED, author 2026-11-11)
Author ruling, verbatim: "if he has that status effect he 'cleans' enemies when in battle. It could make physical attacks for the player less effective but cleaning the enemies 'steals' some of their magic/bravado."

- While Sugar Rush Hour is active, the bro "cleans" enemies instead of hitting them cleanly.
- His physical attacks deal reduced damage. **Reduction: TBD (balancing pass).**
- Each cleaning hit steals some of the enemy's magic/Bravado, and the stolen amount goes to the bro. **Amount stolen per hit, cap, and behaviour against enemies with no Bravado: TBD (balancing pass).**
- Applies to physical attacks only; skills and items are unchanged unless the balancing pass says otherwise.

**Battle text for a cleaning hit (PROPOSED):**

| # | Line | Status |
|---|------|--------|
| 1 | "[BRO] scrubs [ENEMY] down like a hostel bunk after a Contiki group checked out! Barely a mark. [X] Bravado comes off with the grime." | PROPOSED |
| 2 | "[BRO] licks his thumb and works a smudge off [ENEMY]'s face for nine straight seconds! [ENEMY] has never been this clean or this humiliated. [BRO] pockets [X] Bravado." | PROPOSED |

### Interaction With Other Statuses
| Existing Status | What Happens |
|-----------------|--------------|
| Alcohol ladder (Buzzed → Catastrophe) | **APPROVED:** while Sugar Rush Hour is active, the bro's drunk tier displays one step lower than it really is. He feels sober, keeps drinking, and the real tier lands with the Crash ("deliberately distorted information", intoxication law §3) |
| "Hungover" | **APPROVED:** suppressed while active, returns when the Crash fires |
| "Port-O-Cologne" | **APPROVED:** the cleaning compulsion does not cure it. He cleans everything except himself |

### What It Does NOT Do
- ❌ Count as dessert
- ❌ Burn calories, build abs, or make anyone look 26
- ❌ Come with a refund, ever, under any circumstances, especially the one listed

---

## 🍺 Intoxication Review

**APPROVED (author, 2026-11-11); numbers TBD for the balancing pass.**

### The Three Questions (`design/narrative/bros_choose_debauchery.md`)
| Question | Answer |
|----------|--------|
| **What does the bro THINK he's getting?** | A bakery-fresh pick-me-up that gives him the drive, stamina and focus of his 2003 self, with zero carbs |
| **What does he ACTUALLY get?** | A short burst of speed he can't aim, a compulsion to clean anything in reach, and a Crash that costs more than the high gave |
| **The gap: how does it become a gameplay consequence?** | The player loses control of the bro to cleaning, and the hostel morning-after reveals what he did overnight: the room is spotless, he has alphabetized the party inventory, and he threw something away |

### No Free Advantage
"Intoxicants do not provide uncomplicated, consequence-free advantages." The cost: the Speed comes with −Accuracy, the cleaning compulsion takes control away in the overworld, his physical attacks in battle turn into weak cleaning hits (the Bravado he steals is the only upside), and the Crash (−3 all stats, 75% skip) arrives after every use.

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | STRAWBERRY SHORTCAKE SPEEDCAKES™, bought from Tony420 over ICQ |
| 2 | Immediate effect | "Sugar Rush Hour": +Speed, −Accuracy, faster dialogue; in battle his physical attacks become cleaning hits (less damage, steal enemy Bravado) |
| 3 | Escalation conditions | A second hit while active extends the compulsion and stacks the Crash. Mixing with alcohol masks the drunk tier |
| 4 | Visible player-facing cues | Jaw-clench idle, sped-up text scroll, a pink sparkle-and-sponge status icon, the bro wiping surfaces unprompted |
| 5 | Effect on player control | Bounded overworld interruptions: the bro walks off to clean the nearest interactable, then returns. No menu lock, no movement lock beyond the interruption. In battle the player still picks every action; physical attacks resolve as cleaning hits |
| 6 | Duration and recovery | Ends on its timer or at the next hostel rest; the Crash follows and clears per the existing status |
| 7 | Comedic consequence | The deep-cleaned hostel room, the alphabetized inventory, one thrown-away item, and "NO REFUNDS" honored to the letter |
| 8 | Interaction with other established statuses | Masks the alcohol tier; suppresses then returns Hungover; feeds the existing "Crash" |
| 9 | Technical implementation dependencies | `consumables.json` has no status, duration or stack fields; overworld interruption, displayed-tier distortion, the inventory sort and the battle cleaning-hit resolution (damage reduction + Bravado steal) are all proposed engineering work |
| 10 | Requires further author approval? | Design approved 2026-11-11. Still open: every number (balancing pass), which item gets thrown away (it must never be a key item), the PROPOSED battle text |

---

## ⚙️ Engine Fields (`consumables.json`)

**Registered 2026-11-11** via `eurobound-item-engine-sync`, key `strawberry_shortcake_speedcakes`, using only the four live fields.

| Field | Value |
|-------|-------|
| `display_name` | STRAWBERRY SHORTCAKE SPEEDCAKES™ |
| `heal_hp` | 0 |
| `heal_bravado` | 0 (the doc leaves on-use Bravado open; 0 until the balancing pass) |
| `description` | "Tastes like strawberry frosting licked off a car battery." (the canon inspect line) |
| **Fields the schema does not have yet** | Crypto price and coin (420 $HUFF), stack size, subtype, status applied, duration, delayed Crash, overworld compulsion, battle cleaning (damage reduction, Bravado steal). All proposed engineering work |
| **Registered** | Yes |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | PROPOSED: a slim disposable vape, upright |
| **Design** | PROPOSED: pink-and-cream sleeve, cartoon strawberry shortcake slice, a strawberry-shaped LED tip that lights on each puff, shrink-wrap visibly crooked |
| **Text/Markings** | "STRAWBERRY SHORTCAKE SPEEDCAKES™" and "Disposable Dessert-Grade Vape". Proofread every word on generated art (SPEEDCAKES and SHORTCAKE are easy for generators to mangle) |
| **Color/Finish** | PROPOSED: bubblegum pink, frosting cream, strawberry red, cheap glossy plastic |
| **States** | PROPOSED: full / LED flickering (last use) |
| **Filename** | Not yet specced |

---

## 🔗 Quest Hooks

| Hook | Quest / File | Reader (who or what reads it) | Flag | Status |
|------|--------------|-------------------------------|------|--------|
| Midweek Drop broadcast | `design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md` (Spam Broadcast, Items Sold row) | ICQ broadcast system / the player at any hotspot | none | Canon copy; item ID not yet added to that row |
| Replaces the retired vape line | `design/quests/general_quests/darkwebdossiercrossoverevents.md:398` | Darkweb Dossier ICQ event script | none | Done (2026-11-11 sweep): the line is now the Speedcakes ad at 420 huff |
| Morning-after deep clean | Hostel rest scene | Rest/morning-after script | `speedcakes_deep_clean_pending` | PROPOSED (flag name; the deep clean itself is approved) |
| Dead-drop pickup | Tony420 delivery (see Delivery) | Overworld drop-spot interaction, or the goon in goon/sheisty scenes | none ruled | Delivery rule canon; drop staging pending author |

No quest has been ruled to require or reward this item.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID and engine key unique across the repo (grep) | ☑ |
| Display name unique across the game (real brands keep real names) | ☑ |
| No real city or place names in player-facing text | ☑ |
| Price in SOVS or a named master-pool coin; no euros, no € glyph, no koruna, no bare numbers | ☑ 420 $HUFF |
| Deception written: actual vs believed vs gap | ☑ PROPOSED (not covered by the 2026-11-11 answers) |
| Inspect microcopy written, short, funny, and junk items included | ☑ Canon |
| Effects, durations and stack rules specified (or marked PROPOSED) | ☑ Approved design, numbers TBD |
| Intoxication review complete (if intoxicating) | ☑ Approved 2026-11-11 |
| A real cost pays for every benefit | ☑ |
| Engine fields match the live `consumables.json` schema | ☑ |
| Quest hooks name their readers | ☑ |
| Every unruled field marked PROPOSED | ☑ |
| Comedy value preserved at full strength | ☑ |
| Bros never achieve self-awareness, fear or disgust | ☑ |

---

## 🚫 Warnings & Restrictions

### Content
- [x] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [x] No sanitized version, no safe-build swap, no softened synonym
- [x] The only ceiling is no nudity
- [x] The bros stay willing and delusional; the consequences stay funny

### Crypto
- [x] Coins come from `design/economy/shitcoin_master_pool.md`; no one-off coins invented in an item file
- [x] Coin exchange rates come from the author's economy pass, not from this file
- [x] The vendor always knows exactly what the coin is worth; the bros never do

---

## 📝 Development Notes

- Routed to `design/items/general_items/` under the item-creation skill's step 3: Tony420 is filed in Debaucheryville, but he sells over ICQ at hotspots in all four cities. If the author wants Tony's stock filed with his home city, move it to `design/items/debaucheryville_items/`.
- Filing ruled (author, 2026-11-11): stays in `design/items/general_items/`.
- Tony420 is never seen. Delivery ruled (author, 2026-11-11): dead drop by default; a goon hands it over only if a goon is already in the scene or the scene is sheisty (darkweb-adjacent character, the Kavarna, the Shadow Exchange).
- The Crash reuses the existing "Crash" status rather than inventing a new comedown.
- Registered in `consumables.json` (2026-11-11) with `heal_hp` 0, `heal_bravado` 0, description = canon inspect line.
- **Engineering follow-up (schema; needs an author ruling before adding fields):** `consumables.json` has no fields for price/coin (420 $HUFF), status (Sugar Rush Hour), duration, stack rules, the delayed Crash, the overworld cleaning compulsion, or the battle cleaning hit (damage reduction + Bravado steal). Nothing was added; the four-field schema was kept.
- Balancing pass owes: Sugar Rush Hour duration, Speed/Accuracy deltas, compulsion interval, cleaning-hit damage reduction, Bravado stolen per hit, on-use Bravado, $HUFF SOVS rate.
- Still open for the author: purchase line, rarity, stack size, resale/can-be-sold, which item the deep clean throws away (never a key item), drop staging, sprite, the PROPOSED battle text and Deception copy.

---

## 🔧 Development Status

- **Status**: Approved (design), numbers pending
- **File Location**: `design/items/general_items/strawberry_shortcake_speedcakes_item.md`
- **Registered In**: `consumables.json` Yes (`strawberry_shortcake_speedcakes`)
- **Sprite**: Not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-11 | Initial item doc from consumable template v1.0; author canon name, subtitle and Midweek Drop copy; effects, inspect lines and concept PROPOSED | Claude (agent) |
| 2026-11-11 | Author answers applied: price 420 $HUFF (coin approved by author, amount by moderator); canon inspect line (car battery), other candidate removed; effect sketch APPROVED plus battle cleaning (reduced physical damage, steals enemy Bravado; numbers TBD) with PROPOSED battle text; dead-drop delivery rule with goon exception; filing confirmed general_items; registered in consumables.json; status Approved (design), numbers pending | Claude (agent) |
