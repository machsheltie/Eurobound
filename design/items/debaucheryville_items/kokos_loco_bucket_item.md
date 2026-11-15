# Item Definition: Kokos Loco Bucket

*"This is basically what they drink in actual Hawaii, bro." - the bros (`bros_see`, `bohemian_riviera_items.json`)*

> **Template Version 1.2 — short item doc (author, Desk Eurobound-rpac-q2, 2026-11-14: "A: a short .md per item from its template").** Identity, price and effects are copied from the location data; nothing here changes them. Sections the data does not cover say "not designed yet" instead of inventing an answer.

## 📋 Item Identity
- **Item ID**: `item_kokos_loco_bucket`
- **Engine Key**: not registered in `game/assets/data/items/consumables.json` yet
- **Display Name**: Kokos Loco Bucket
- **Subtitle / Product Line**: not designed yet
- **Internal Name**: a bucket-sized piña colada in an imported plastic coconut shell
- **Item Type**: Consumable
- **Subtype**: alcohol
- **Rarity**: common (bros' belief not designed yet)
- **Vendor / Source**: Kokos Loco bar (`kokos_loco_bar_strip`), shop inventory
- **Location**: Kokos Loco, bar strip, Bohemian Riviera, Debaucheryville (`design/worlds/debaucheryville/bohemian_riviera.md:92`)

---

## 🎭 The Deception

### What It Actually Is
"A bucket-sized piña colada in an imported plastic coconut shell painted to look tropical. Kokos Loco's signature landlocked-beach cocktail." (`player_sees`, canon.) The location doc adds: "Coconut shell is imported plastic" (`bohemian_riviera.md:202`).

### What The Bros Believe It Is
"This is basically what they drink in actual Hawaii, bro." (`bros_see`, canon)

### The Comedy Gap
Not designed yet.

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Price** | 14 SOVS (`bohemian_riviera_items.json`; see Development Notes) |
| **Actual Value** | 2 SOVS |
| **Resale Value** | not designed yet |
| **Can Be Sold** | not designed yet |
| **Stack Size** | not designed yet |
| **Bundle Deals** | None recorded |

---

## 🔍 Inspect Microcopy

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy."
>
> "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."

| # | Inspect Line | Status |
|---|--------------|--------|
| 1 | not written yet | — |

---

## 📣 Vendor Pitch Copy

### Pitch
```
not written yet
```

### Purchase Line
> not written yet

---

## 📊 Effects on Use

| Effect | Value | Duration | Stack Rule | Notes |
|--------|-------|----------|------------|-------|
| Status applied | "liquid_confidence" | 3-5 turns | not designed yet | +3 Charm, +2 Bravado, -1 Accuracy (location data note) |
| Status applied | "sloppy" | 1-2 turns | not designed yet | -3 Accuracy, 15% chance to hit allies (location data note) |

### Interaction With Other Statuses
Not designed yet.

### What It Does NOT Do
Not designed yet.

---

## 🍺 Intoxication Review

Not written yet. It is alcohol, so the review (`design/narrative/bros_choose_debauchery.md`, `design/mechanics/intoxication_law.md` §8) is required before the item is registered in the engine.

---

## ⚙️ Engine Fields (`consumables.json`)

Not registered. Registration goes through the `eurobound-item-engine-sync` skill once the open sections are designed.

---

## 🖼️ Physical description (icon art brief)

**[APPROVED — author, Desk Eurobound-rpac-q1, 2026-11-14: "Approve with A: low fill + eight straws, and adopt the template".]** Written in the Writers' Room (`WritingRoom/tasks/20261114_1826_item_physical_descriptions_batch_1_kokos/final.md`).

| Field | Description |
|-------|-------------|
| **silhouette** | A squat frustum bucket shaped like the top half of a coconut: the mouth about 1.5–1.6× wider than the body is tall, a flat base disc about two-thirds of the mouth wide, walls tapering nearly straight, and a thick rolled pail rim. No handles, no loops, ever. |
| **scale_cue** | The drink sits visibly below the rim, leaving a tall band of bare ribbed inner wall above the liquid (a bowl, cup or dessert dish cannot show that much empty wall), and a fan of eight wide straws (an order for four people) sticks out of the mouth at angles. |
| **materials_and_cheap_cues** | Injection-moulded plastic with a cheap greasy sheen, glossy but slightly wrong, never ceramic. A vertical mould seam runs down one side; two ejector-pin dots sit at the base; a shallow sink dimple on the wall. Broad, shallow fake-husk bumps moulded into the wall. The lip ring is scuffed bare where the paint has worn off. |
| **colours** | Shell: amber-tan plastic #B5722F (yellow cast; never chocolate, never orange, never green). Husk bumps: darker brown #7A4A21. Drink: opaque cream-gold #F2E3A0, greyed at the edges, never white. Ice: cloudy pale blue-white #D6E7EC. Dried foam ring: hardened amber #B8912F. Paint: magenta #FF1493, lime #32CD32, orange #FF7F32. Sticker: peeling barcode-white #F2EEE4 over a brown glue shadow. Lipstick: coral #D9525B. Sand in the foot ring: #E8D4A0. Packing tape: yellowed translucent amber. Straws: two magenta #FF1493, two lime #32CD32, one orange #FF7F32, one blue #1E90FF, and two white #F8F8F8 snapped short. |
| **contents** | An opaque piña colada in cream-gold #F2E3A0 with a finely pitted, slightly grainy surface: a thick blended drink, never smooth, never swirled, never white. Four cloudy ice blocks #D6E7EC break the surface. A dried foam ring hardened to amber #B8912F marks where the drink used to sit, above the current level. One drip runs down the outside of the shell. |
| **decoration** | Three flat painted tropical shapes, all botched: a magenta hibiscus #FF1493 with one petal smeared, a lime palm frond #32CD32 laid straight across the mould seam so the seam splits it, and an orange sun #FF7F32 chewed off at the shoulder with a paint drip sagging off it. All three misregister across the seam. |
| **condition** | Reused all night by strangers: a peeling white sticker rectangle #F2EEE4 over a brown glue shadow; a coral lipstick smear #D9525B on the rim; sand crusted in the foot ring #E8D4A0; a crescent chip off the lip; a crack closed with yellowed packing tape; one long dried spill streak down the side; base scratches. |
| **garnish_and_addons** | Eight wide straws in a fan (colours above). No umbrella. |
| **palette_anchors** | From `design/worlds/debaucheryville/bohemian_riviera.md:119-124`: #FF1493 (EMTV Magenta), #32CD32 (Inflatable-Palm Green), #FF7F32 (Space Heater Orange), #E8D4A0 (Sand). New to this item: #B5722F, #7A4A21, #F2E3A0, #D6E7EC, #B8912F, #F2EEE4, #D9525B, #1E90FF, #F8F8F8. |
| **reads_at_icon_size** | 1. A wide squat tan bucket with a thick rolled pail rim, mouth far wider than tall, and a tall bare inner wall above the drink: a bucket, not a cup, bowl or cauldron. 2. A visibly liquid drink, not a dessert: opaque cream-gold (never white) with cloudy ice blocks breaking the surface and a drip down the outside. 3. Cheap imported plastic, badly painted: a glossy amber-tan shell with a mould seam splitting three misregistered paint shapes (magenta, lime, orange), a peeling white sticker rectangle, a lipstick smear, and the fan of eight straws. |
| **must_not_look_like** | A small plain coconut cup (QC round 1). Clean appetising white cream, photoreal (round 1). A green pumpkin or cauldron (round 2). Two-blob tropical paint over an empty pot (round 2). Thin loop handles (round 2). A shallow bowl of soft-serve (round 3). A cute glossy kids' dessert (round 3). A chocolate or ceramic shell with tidy decals (round 3). A toy sand bucket (the drink, ice and paint carry it; no bail). A flower pot (the ice and straws kill it). |
| **lettering** | None. The sticker is a shape and colour only, and no read depends on it being readable. |

---

## 🎨 Sprite Notes

| Attribute | Description |
|-----------|-------------|
| **Inventory Icon** | See the Physical description above. The location data currently points at the venue frontage in `bar_strip_facades.png` because no per-drink icon existed. |
| **Design** | See the Physical description above |
| **Text/Markings** | None |
| **Color/Finish** | See the Physical description above |
| **States** | not designed yet |
| **Filename** | not yet specced (Asset team icon id `item_kokos_loco_bucket`) |

---

## 🔗 Quest Hooks

None recorded.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item ID unique across the repo (grep) | ☑ |
| Physical description approved on the Desk | ☑ (rpac-q1) |
| Deception, inspect microcopy, intoxication review, engine fields | ☐ not designed yet |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke
- [ ] The only ceiling is no nudity

---

## 📝 Development Notes

- **Price mismatch, for the author:** the location doc's price table says "Piña colada in a coconut, Kokos Loco | 12 SOVS" (`bohemian_riviera.md:202`), while the item data says 14 SOVS. This doc copies the item data and doesn't settle it.
- The location data's `note_sprite` still says no per-drink icon exists; the Asset team is building one from the description above.

---

## 🔧 Development Status

- **Status**: Drafted (physical description approved; other sections not designed)
- **File Location**: `design/items/debaucheryville_items/kokos_loco_bucket_item.md`
- **Registered In**: `consumables.json` No
- **Sprite**: not yet specced

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-14 | Short item doc created per rpac-q2; approved physical description added per rpac-q1 | Writers' Room (moderator) |
