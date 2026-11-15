# Item Definition: Already-Spent Credit

> **Short item doc (author, Desk Eurobound-rpac-q2, 2026-11-15: "A: a short .md per item from its template").** Built from `design/templates/consumable_item_template.md`. Identity, numbers and effects are copied from `game/assets/data/items/consumables.json` (`already_spent_credit`); nothing here changes them. Sections the data does not cover say "Not designed yet." instead of inventing an answer.

## 📋 Item Identity

- **Item ID / Engine Key**: `already_spent_credit` (`game/assets/data/items/consumables.json`)
- **Display Name**: Already-Spent Credit
- **Item Type**: Consumable (revive, 10%)
- **Source**: drop (`count_continue_drop`, `game/assets/data/enemies/debaucheryville_enemies.json`)

## 🎭 The Deception

### What It Actually Is
"An arcade token stamped CREDIT 00. It has already been spent. It will be spent again. Lord Pilsner calls it a family heirloom." (engine description, canon)

### What The Bros Believe It Is
Not designed yet.

## 💰 Economic Details

Not designed yet.

## 🔍 Inspect Microcopy

Not designed yet.

## 📣 Vendor Pitch Copy

Not designed yet.

## 📊 Effects on Use

Not designed yet.

## 🍺 Intoxication Review

Not designed yet.

## ⚙️ Engine Fields (`consumables.json`)

Not designed yet.

## 🖼️ Physical description (icon art brief)

**[APPROVED — author, Desk Eurobound-rpac-q3, 2026-11-15: "Approve all; symbol A (neume); crown base pastel pink".]** Written in the Writers' Room (`WritingRoom/tasks/20261114_1900_item_physical_descriptions_batch_2_asset/final.md`).

| Field | Description |
|---|---|
| silhouette | A single heavy round token, seen almost face-on with a hair of tilt so the rim reads as thickness — a thick bevelled disc, not a coin-thin washer. Milled dots dot the rim all the way round, a shallow groove ring sits inside the rim on each face, and one edge has a bright flattened spot where a machine's coin return has kicked it back a few hundred times. Slight irregularity at one point on the rim: a flat bite out of the circle, metal pushed rather than cut. |
| scale_cue | One disc. At 128 px the read is: circular outline, dotted rim, a groove ring, two short words stacked in the middle. Nothing else in frame — no slot, no hand, no machine. |
| materials_and_cheap_cues | Brass-plated zinc: brass on the high faces, dull grey zinc showing through at the rim's worn flats and inside the stamped letters. The lettering is stamped and recessed, not printed — you can see the flat bottom of each groove. Grime is flat: green verdigris bloomed into the groove ring, brown smear across one side, both hard-edged, no speckle, no fuzz. |
| colours | Brass face: #C9A45D (anchor). Brass highlight: #E7D7B7 (anchor). Brass shadow: #8A6E14. Bare zinc wear: #A89A94. Verdigris: #0B6B50 (anchor). Brown grime: #3A2E2A. Stamped lettering: #2A2118 in the grooves, with bare metal flecks #E7D7B7 on the worn stroke tops. Rim UV paint remnant: toxic green #39FF14 (anchor), two flecks in the groove only. |
| contents | Nothing — it is a token. |
| decoration | Front face: `CREDIT 00` only. Back face: the Absinthe Arcade's angular A/hourglass emblem, stamped, worn nearly smooth — the same emblem as every other token in the building, which is the joke the bros cannot see. Rim: milled dots and the shallow groove ring. |
| condition | Spent many times over: rim flattening, one pushed-in bite, brass worn off the highest dots and the groove edge to bare zinc, verdigris in the groove, a hard-edged brown smear, lettering grooves choked with grime with only the raised strokes still catching light, one flat gouge across the rim. |
| garnish_and_addons | None. No hole, no ring, no chain, no keyring loop. It is a token, not a pendant. |
| palette_anchors | Inherited from `design/worlds/debaucheryville/core/absinthe_arcade_core.json:125-128`: #C9A45D, #E7D7B7, #0B6B50. Inherited from `design/worlds/debaucheryville/absinthearcade.md:44`: #39FF14. New to this item: #8A6E14 (brass shadow), #A89A94 (bare zinc), #2A2118 (stamped-letter grime). |
| reads_at_icon_size | A chunky round token, dotted rim, groove ring — the same family as every other arcade token at a glance. `CREDIT 00` legible as two short stacked words in the centre, and as words, not a decorative mark. Worn brass with green grime: an object that has been through a slot, not a mint coin. |
| must_not_look_like | A poker chip or a casino chip — no centre inlay disc, no card suits, no edge stripes. A generic currency coin — no portrait, no wreath, no numerals other than `00`. A medallion, pendant or charm — no loop, no hole, no ribbon. A chocolate coin — this is scuffed metal with grime in the grooves, and the lettering is recessed. A new token — brass is worn to grey at every high point. |
| lettering | Stamped, recessed, uppercase, compressed heavy sans (Impact-adjacent) in #2A2118 with bare-metal flecks on the stroke tops. Two lines, stacked and centred: `CREDIT` / `00`. No other words on either face. The reverse carries the emblem and no lettering. |

### Changes from the shipped icon
- CHANGED (was: no reverse face): canon (`absinthe_arcade_items.json`, the arcade token) gives the Arcade an angular A/hourglass emblem, so this token is visibly the same currency as the one that still works.
- CHANGED (was: no rim paint): the canon token rim glows green under UV, so two flecks of green remain in the groove — the only thing on this token still doing its job.

## 🎨 Sprite Notes

Not designed yet.

## 🔗 Quest Hooks

Not designed yet.

## 🗣️ Bro Lines on Use (optional — include only once written or approved)

Not designed yet.

## ✅ Validation Checklist

Not designed yet.

## 🚫 Warnings & Restrictions

Not designed yet.

## 📝 Development Notes

Not designed yet.

## 🔧 Development Status

- **Status**: Drafted (physical description approved; other sections not designed)
- **File Location**: `design/items/debaucheryville_items/already_spent_credit_item.md`

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-11-15 | Short item doc created per rpac-q2; approved physical description added per rpac-q3 | Writers' Room (moderator) |
