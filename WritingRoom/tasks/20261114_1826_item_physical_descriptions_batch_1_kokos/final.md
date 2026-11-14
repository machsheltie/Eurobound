# Item physical descriptions batch 1 — Kokos Loco Bucket (PROPOSED, awaiting author scale decision)

Item: `item_kokos_loco_bucket` — Kokos Loco Bucket, sold at Kokos Loco on the Bohemian Riviera bar strip, Debaucheryville. Price 14 SOVS, actual value 2, effects `liquid_confidence` + `sloppy`, and the existing `player_sees` / `bros_see` lines are unchanged. This document adds a physical description only.

Ruling applied (author, Eurobound Desk asset-team-qc-kokos_loco_bucket, 2026-11-14): every item gets a physical description in detail, complete with colours, specific enough for an artist to build the icon without guessing. The icon is rendered with no lettering; no read may depend on readable words.

Three icon rounds have failed blind QC (dev/asset_team/reviews/qc_log.jsonl): round 1 read as a small plain coconut cup with appetising clean cream; round 2 read as a green pumpkin/cauldron with an empty pot; round 3 read as a shallow bowl of cute glossy soft-serve in a chocolate or ceramic shell. The shared body and every scale option below are written to kill those reads.

---

## Physical description (icon art brief)

### silhouette
A squat frustum bucket shaped like the top half of a coconut: the mouth about 1.5–1.6× wider than the body is tall, a flat base disc about two-thirds of the mouth wide, walls tapering nearly straight, and a thick rolled pail rim. No handles, no loops, ever. Deep enough that bare inner wall can show above the drink.

### scale_cue
[AUTHOR DECISION NEEDED: pick ONE primary scale solve. All three options below share the same body, paint, drink and condition; only the fill height and the straw/garnish layer change. The options are mutually exclusive — do not merge them.]

- **Option A (Deepseek) — low fill, eight straws.** The drink sits visibly below the rim, leaving a tall band of bare ribbed inner wall above the liquid; a bowl, cup or dessert dish cannot show that much empty wall. A fan of eight wide straws (a four-person order) sticks out of the mouth at angles: two magenta #FF1493, two lime #32CD32, one orange #FF7F32, one blue #1E90FF, and two white #F8F8F8 snapped short.
- **Option B (Aion) — pineapple wedge, one straw.** Fill two-thirds up, with a dried amber tide-line and bare inner wall above the liquid. A full pineapple wedge #E8C95C hangs off the rim and reads small against the mouth — a known-size object dwarfed by the bucket. One wide red-striped straw #E03131, bent, tooth-marked at the tip.
- **Option C (Mistral) — heaped fill, three straws.** The drink is heaped just over the brim in a grainy mound with one drip running down the outside; three wide straws stick out at angles: red #E03131, blue #1E90FF, one white #F8F8F8 snapped short. **Known risk:** the heaped opaque mound is the round-3 soft-serve failure. This option exists only with the ice cubes breaking the surface; even then it is the weakest of the three against QC history.

### materials_and_cheap_cues
Injection-moulded plastic with a cheap greasy sheen — glossy but slightly wrong, never ceramic. A vertical mould seam runs down one side; two ejector-pin dots sit at the base; a shallow sink dimple on the wall. Broad, shallow fake-husk bumps moulded into the wall. The lip ring is scuffed bare where the paint has worn off.

### colours
- Shell: amber-tan plastic #B5722F (yellow cast; never chocolate, never orange, never green). **Chosen over Deepseek's #C09A62 and Mistral's #C89B6A:** #B5722F is the furthest from both the round-3 chocolate read and the round-2 orange-pumpkin read while staying visibly plastic, not husk.
- Husk bumps: darker brown #7A4A21.
- Drink: opaque cream-gold #F2E3A0, greyed at the edges (never white).
- Ice: cloudy pale blue-white #D6E7EC.
- Dried foam ring: hardened amber #B8912F.
- Paint: magenta #FF1493, lime #32CD32, orange #FF7F32 (all location palette anchors, below).
- Sticker: peeling barcode-white #F2EEE4 over a brown glue shadow.
- Lipstick: coral #D9525B.
- Sand in foot ring: #E8D4A0.
- Packing tape: yellowed translucent amber.
- Option B wedge: #E8C95C. Option B straw: #E03131 with white stripe. Option A/C straw colours as listed per option.

### palette_anchors
- Inherited from `bohemian_riviera.md` Technical Specifications: #FF1493 (EMTV Magenta), #32CD32 (Inflatable-Palm Green), #FF7F32 (Space Heater Orange), #E8D4A0 (Sand).
- New to this item: #B5722F, #7A4A21, #F2E3A0, #D6E7EC, #B8912F, #F2EEE4, #D9525B, #E8C95C, #E03131, #1E90FF, #F8F8F8.

### contents
An opaque piña colada in cream-gold #F2E3A0 with a finely pitted, slightly grainy surface — a thick blended drink, never smooth, never swirled, never white. Four cloudy ice blocks #D6E7EC break the surface. Options A and B only: a dried foam ring hardened to amber #B8912F marks where the drink used to sit (C is filled over the brim, so it has none). One drip runs down the outside of the shell. Fill height is set by the chosen scale option.

### decoration
Three flat painted tropical shapes, all botched: a magenta hibiscus #FF1493 with one petal smeared, a lime palm frond #32CD32 laid straight across the mould seam so the seam splits it, and an orange sun #FF7F32 chewed off at the shoulder with a paint drip sagging off it. All three shapes misregister across the seam — printed by a machine that was never aligned.

### condition
Reused all night by strangers: a peeling white sticker rectangle #F2EEE4 over a brown glue shadow; a coral lipstick smear #D9525B on the rim; sand crusted in the foot ring #E8D4A0; a crescent chip off the lip; a crack closed with yellowed packing tape; one long dried spill streak down the side; base scratches.

### garnish_and_addons
Set by the chosen scale option: A — eight wide straws (colours above); B — one pineapple wedge hooked on the rim plus one bent, tooth-marked red-striped straw; C — three wide straws (red, blue, snapped white). No umbrella in any option.

### reads_at_icon_size (128 px blind checklist — holds for all three options)
- [ ] A wide squat tan bucket with a thick rolled pail rim, mouth far wider than tall — a bucket, not a cup, bowl or cauldron. (Option A also shows the tall bare inner wall; B also shows the dwarfed wedge; C also shows the mound above the rim.)
- [ ] A visibly liquid drink, not a dessert — opaque cream-gold (never white) with cloudy ice blocks breaking the surface and a drip down the outside.
- [ ] Cheap imported plastic, badly painted — glossy amber-tan shell with a mould seam splitting three misregistered paint shapes (magenta, lime, orange), a peeling white sticker rectangle and a lipstick smear.

### must_not_look_like
- A small plain coconut cup (R1) — mouth far wider than tall, thick pail rim, scale layer per option.
- Clean appetising white cream, photoreal (R1) — cream-gold with greyed edges, pitted surface, dried amber foam ring, lipstick.
- A green pumpkin or cauldron (R2) — amber-tan shell, no green body, no lid, no bail handle, no ribs.
- Two-blob tropical paint over an empty pot (R2) — three distinct split-and-smeared paint shapes plus a visible liquid surface.
- Thin loop handles (R2) — no handles, no loops, ever.
- A shallow bowl of soft-serve (R3) — ice breaking the surface, grainy texture, no smooth swirled dome; C carries this risk by design and needs the ice to survive it.
- A cute glossy kids' dessert (R3) — scuffed lip, peeling sticker, lipstick, sand, packing tape, dried spill.
- A chocolate or ceramic shell with tidy decals (R3) — yellow-cast plastic with seam and ejector dots; paint misregistered and split by the seam.
- A toy sand bucket — the drink, ice and paint carry it; no bail, no lettering.
- A flower pot — ice blocks and straws kill it.

### lettering
None. The icon renders with no text. The sticker is a shape and colour only — a peeling barcode-white rectangle over a glue shadow — and no read depends on it being readable.

---

## Proposed template section for all later item batches (PROPOSED)

Heading: `## Physical description (icon art brief)` — required on every item doc from batch 2 onward. Fields (12, Aion's list, backed by Deepseek and Mistral):

1. `silhouette` — the shape in one sentence, plain proportions (mouth:height, base:mouth).
2. `scale_cue` — ONE sentence: the single thing that reads big at 64–128 px with nothing else in frame. Split from silhouette because all three failed rounds were scale failures.
3. `materials_and_cheap_cues` — material plus seams, mould artefacts, wrong sheen, sticker residue.
4. `colours` — every major surface as plain colour word + hex.
5. `contents` — colour, texture, fill level, inclusions, what has dried on it; must read as food/drink, not dessert.
6. `decoration` — what is painted/printed, in which colours, and how badly.
7. `condition` — wear, stains, damage implying reuse by strangers.
8. `garnish_and_addons` — anything sticking out, hooked on, or stuck to it; state explicitly when there is none.
9. `palette_anchors` — which hexes are inherited from the owning location's palette versus new to the item, so icons sit next to location art without clashing.
10. `reads_at_icon_size` — the three mandatory reads in a 128 px thumbnail.
11. `must_not_look_like` — anti-cue list seeded from previous failed QC rounds plus this item's own risks.
12. `lettering` — always "none" for icons; any text-dependent joke is flagged here and moved to flavour copy.

---

## Outstanding author decisions

1. **Scale solve** — Option A (low fill + eight straws), B (pineapple wedge + one straw), or C (heaped fill + three straws). Recommendation: A or B. C re-imports the round-3 failure mode.
2. **Template adoption** — approve the 12-field `## Physical description (icon art brief)` section as the standing format for batches 2+ (to be added to the item templates in `design/templates/`).

## Integration notes (room record)

- Cut per moderator order: "husk bumps moulded upside down" (unpaintable), "one hard white highlight" (lighting belongs to the render), all non-paintable adjectives.
- Fixed Mistral's tide-line contradiction (overbrim fill cannot coexist with a dried interior ring): Option C now carries no interior tide-line; the foam ring in shared `contents` applies to options A and B.
- Deepseek's paint hexes (#E8228C / #5FB53C / #E4761F) were replaced with the canonical location anchors #FF1493 / #32CD32 / #FF7F32 per `bohemian_riviera.md` Technical Specifications.
- Shell hex #B5722F chosen over #C09A62; husk bumps #7A4A21 chosen over #8B6B3B, per moderator order to pick one and say which.
