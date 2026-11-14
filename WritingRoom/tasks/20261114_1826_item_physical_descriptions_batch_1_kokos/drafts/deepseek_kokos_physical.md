# Deepseek — Kokos Loco Bucket physical description (batch 1)

Item: `item_kokos_loco_bucket` — Kokos Loco Bucket, Kokos Loco, Bohemian Riviera bar strip. Ruled facts unchanged: 14 SOVS, actual value 2, `liquid_confidence` + `sloppy`, existing `player_sees`/`bros_see` lines. Icon renders with no lettering; no read may depend on readable words.

## 1. Physical description (art brief, 158 words)

**Silhouette:** squat frustum — mouth 1.6× wider than the body is tall, flat base disc two-thirds of the mouth wide, walls tapering nearly straight, lip a thick rolled bead. **Scale, empty frame:** the mouth swallows eight straws at once, and the drink sits low enough to leave a tall bare inner wall above it.

**Shell:** ochre-brown #C09A62 plastic (yellow cast, never chocolate), fake-husk bumps #8B6B3B moulded upside down, greasy semi-matte sheen, one hard white highlight, a vertical mould seam, a sink dimple.

**Paint, badly:** magenta #E8228C hibiscus, lime #5FB53C frond laid straight across the mould seam so the seam splits it, orange #E4761F sun chewed off at the shoulder; the whole lip ring scuffed bare; one fresh glossy touch-up blob #FF58B4.

**Drink, three-quarters up:** opaque creamy gold #EDD9A6, never white, finely pitted; four cloudy ice blocks #D6E7EC breaking the surface; a dried foam ring hardened to amber #B8912F.

**Eight straws:** magenta, lime, two snapped white.

**Condition:** sand crusted in the foot ring #E8D4A0; coral #D9525B and plum #6E2236 lipstick smears an inch apart; a crescent chip off the lip; a peeling white barcode rectangle #F2EEE4 over a brown glue shadow; one long dried spill streak.

## Scale solve (mine)

The bucket reads big from **proportion plus a visible deep interior**, not from garnish: the frustum ratio is hardware-bucket, and the drink is set *below* the rim so the icon shows a tall band of bare ribbed inner wall over the liquid. A bowl, cup or soft-serve dish cannot show that much inner wall. Eight straws (a four-person order) carry the human scale; no heaped mound, because a piled opaque dome is the round-3 "soft-serve" failure.

## 2. Reads at icon size (128 px blind checklist)

- [ ] Wide squat tan shell, mouth far wider than tall, thick rolled lip, drink visibly *below* the rim with a tall bare inner wall — a deep bucket, not a bowl or dish.
- [ ] Broad ellipse of opaque creamy-gold liquid with four cloudy ice blocks breaking it and a hard amber foam ring — liquid, not cream, not a mound.
- [ ] Greasy semi-matte tan plastic carrying magenta, lime and orange paint plus one peeling white rectangle, and eight straws in a fan — cheap imported fake-tropical plastic.

## 3. Must not look like

- Small plain coconut cup (R1) — frustum mouth, eight straws, deep visible interior.
- Clean appetising white cream / photoreal (R1) — gold with a yellow cast, pitted, dried amber foam ring.
- Green pumpkin or cauldron (R2) — tan shell, no green body, no lid, no bail handle.
- Two-blob paint / empty pot (R2) — three distinct paint shapes, and liquid clearly visible below the rim.
- Thin loop handles (R2) — no handles, no loops, ever.
- Shallow bowl of soft-serve heap (R3) — low fill, ice on the surface, tall inner wall, no dome.
- Cute glossy kids' dessert (R3) — semi-matte shell, chips, lipstick, sand, peeling sticker, scuffed lip.
- Chocolate or ceramic, tidy decals (R3) — yellow-cast tan plastic, misregistered paint split by the seam.
- *My own risks:* a toy sand bucket (kill with the drink + paint, no lettering, no bail); an ice-cream sundae (kill with the amber foam ring and non-white gold); a flower pot (kill with the ice and straws).

## 4. Proposed template section (all later item batches)

Heading: `## Physical description (icon art brief)` — required on every item doc.

Fields:
- `silhouette` — the shape in one sentence, in plain proportions (no adjectives a painter can't draw).
- `scale_cue` — **the one thing that reads big at 64–128 px with nothing else in frame.** Split out from silhouette on purpose: every round-1/2/3 failure was a scale failure, and a painter needs one sentence they cannot hedge.
- `materials_and_cheap_cues` — material, seam, mould artefacts, wrong sheen, sticker residue.
- `colours` — every major surface as plain colour word + hex.
- `palette_anchors` — which hexes are inherited from the owning location's palette (canon anchors) and which are new to this item. Added because item icons must sit next to location art without clashing.
- `contents` — colour, texture, fill level, inclusions, what has dried on it.
- `decoration` — what is painted/printed, in which colours, and how badly.
- `condition` — wear, stains, damage that implies reuse by strangers.
- `garnish_and_addons` — anything sticking out, hooked on, or stuck to it; state explicitly when there is none.
- `reads_at_icon_size` — the three mandatory reads in a 128 px thumbnail.
- `must_not_look_like` — the anti-cue list, seeded from previous failed QC rounds plus this item's own risks.
- `lettering` — always "none"; no read may depend on readable text.

## Reviewer

Mistral — adversarial cross-check that two competing scale solves are not accidentally blended into one icon brief (they are options for the author, not a composite). Kimi integrates and does the plain-paintable-language pass.
