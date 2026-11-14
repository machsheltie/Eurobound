# Mistral — Kokos Loco Bucket physical description (batch 1)

Item: `item_kokos_loco_bucket` — Kokos Loco Bucket, Kokos Loco, Bohemian Riviera bar strip, Debaucheryville. Ruled facts unchanged: 14 SOVS, actual value 2, liquid_confidence + sloppy, existing player_sees/bros_see lines. Icon renders with no lettering; no read may depend on readable words.

## 1. Physical description (art brief, 160 words)

A wide, squat bucket shaped like the top half of a coconut: mouth clearly wider than tall, walls tapering to a narrow flat base, thick rolled rim. Injection-moulded plastic in caramel tan #C89B6A with a cheap glossy sheen; a vertical mould seam down one side, two ejector-pin dots at the base, broad shallow husk bumps moulded into the wall in darker tan #A87F4F. Painted on badly: magenta hibiscus #FF1493, lime palm frond #32CD32, orange sun #FF7F32 — smeared, misregistered, the sun half off the edge, paint chipped at the rim. Filled just over the brim with opaque, slightly grainy pale-yellow piña colada #F2E3A0, flecked with pineapple fibre #D9B96A, one drip down the outside. A squised pineapple wedge #E8C95C hooks the rim. Three wide straws stick out at angles: red #E03131, blue #1E90FF, one white snapped short #F8F8F8. Worn all night: base scratches, a peeling white sticker rectangle #EFEFEF, a coral lipstick smear #D96A6A on the rim, a dried drink ring inside.

Scale cue (my solve, different from the other drafts): no person, no second object — scale reads from the three wide-bore straws (human-mouth-sized objects) plus the mouth-wider-than-tall squat silhouette and the drink heaped above the rim. At 128 px those three straws are the loudest "bucket, not cup" signal.

## 2. Reads at icon size (128 px thumbnail checklist)

- [ ] A wide squat tan bucket with a thick rolled rim and pale-yellow liquid heaped above the rim — bucket + full drink, not a bowl.
- [ ] Three coloured straws sticking out at angles (red, blue, snapped white) — human scale and "this is sipped, not eaten".
- [ ] Glossy caramel plastic with three misregistered paint blobs (magenta, lime, orange) and a drip on the side — imported fake-tropical, not ceramic, not a pumpkin.

## 3. Must not look like

- A small plain coconut cup (R1) — mouth wider than tall, straws, heaped fill.
- Clean appetising white cream, photoreal (R1) — grainy pale yellow with fibre flecks, not smooth white.
- A green pumpkin or cauldron (R2) — caramel tan, not green; no lid.
- Two-blob tropical paint / empty pot (R2) — three distinct paint shapes plus visible liquid surface and straws.
- Thin loop handles (R2) — no handles at all; solid thick rolled rim.
- A shallow bowl of soft-serve (R3) — deep tapering walls, thick rim, straws, grainy texture, no smooth swirl.
- Cute glossy kids' dessert (R3) — scuffs, peeling sticker, lipstick smear, chipped paint, squised wedge.
- Chocolate/ceramic shell, tidy decals (R3) — light caramel glossy plastic, smeared misregistered paint, peeling white sticker rectangle.

## 4. Proposed template section (for all later item batches)

Heading: `physical_description` (icon art brief). Fields:
- `silhouette_and_scale` — overall shape + the scale cue that reads at 64–128 px in an empty frame.
- `materials_and_cheap_cues` — material + seams, mould lines, ejector pins, sticker residue, wrong sheen.
- `colours` — every major surface as a plain colour word + hex code.
- `contents` — drinks/food: colour, texture, fill level, inclusions, drips.
- `decoration` — painted/decaled motifs: what, which colours, how badly applied (smeared, misregistered, chipped).
- `condition` — wear, stains, damage implying reuse by strangers.
- `garnish_and_addons` — anything sticking out of or hooked on the rim.
- `reads_at_icon_size` — 3-item blind-QC checklist at 128 px.
- `must_not_look_like` — list built from failed QC rounds.
- `lettering` — always "none"; the icon renders with no text, and no read may depend on readable words.

## Reviewer

Kimi (integration + plain-paintable-language pass); Deepseek to spot-check that the object alone lands the tourist-trap joke for the target audience at a glance.
