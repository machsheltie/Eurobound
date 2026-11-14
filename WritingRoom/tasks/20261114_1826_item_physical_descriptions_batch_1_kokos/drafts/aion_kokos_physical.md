# Aion — Kokos Loco Bucket: physical description (draft)

Reviewer: **Deepseek** (failure-mode collision check — you already killed Mistral's heaped mound on exactly the grounds my draft risks; check mine the same way). Kimi integrates.

## 1. Physical description (art brief, ~160 words)

**Silhouette & scale.** Squat bucket: mouth 1.5× wider than tall, thick rolled pail rim, no handles. A pineapple wedge hangs off the rim, reading small against the mouth — the mismatch is the scale cue. Drink two-thirds full; a dried amber tide-line above the liquid leaves bare inner wall showing depth.

**Shell.** Amber-brown injection-moulded plastic (#B5722F), glossy. Vertical mould seam down the front; shallow husk bumps, darker brown (#7A4A21); ejector-pin dots at the base.

**Paint.** Three flat shapes, all botched: magenta hibiscus (#FF1493), one petal smeared; lime palm frond (#32CD32), tip chipped; orange sun (#FF7F32), a drip sagging off it. All three misalign across the seam.

**Drink.** Cream-yellow (#F2E8C9), grey at the edges, broken by three cloudy ice cubes. Dried foam ring at the tide line. One drip down the side.

**Condition.** Yellowed packing tape over a crack; peeling white barcode-shaped sticker (no readable text); coral lipstick on the rim; sand in the foot ring.

**Add-on.** One wide red-striped straw, bent, tooth-marked at the tip.

## 2. Reads at icon size (128 px checklist)

1. **A wide squat pail, not a cup or bowl** — thick rolled rim, mouth far wider than the height, bare inner wall visible above the drink.
2. **A drink with ice in it, not a dessert** — cloudy ice cubes breaking the cream surface; a drip running down the outside.
3. **Cheap plastic, badly painted** — amber-brown (never orange), mould seam splitting the paint, at least one shape visibly smeared or chipped.

## 3. Must not look like

- A green pumpkin or cauldron (round 2) — shell is amber-brown, bumps irregular, never ribbed.
- A bowl of soft-serve or a kids' dessert (rounds 1, 3) — ice cubes break the surface; no smooth swirled dome; fill below the rim.
- A ceramic or chocolate dessert shell (round 3) — glossy plastic sheen, mould seam, ejector-pin dots, packing tape.
- A clean, appetising cocktail (round 1) — greyed edges, dried foam ring, lipstick, sand, tape.
- A souvenir coconut cup — pail rim, wedge proportion and bare wall must keep it reading bucket.

## 4. Proposed template section (for all later batches)

```
## physical_description
- silhouette — proportions as ratios (mouth:height, base:mouth)
- scale_cue — ONE sentence: the single thing that reads big with nothing else in frame
- materials_and_cheap_cues — what it's made of, and how you can tell it's cheap
- colours — every major surface: plain colour word + hex
- contents — colour, texture, fill level, what breaks the surface (must read as food/drink, not dessert)
- decoration — painted/printed motifs, their colours, and how badly they're done
- condition — wear, stains, damage, reuse evidence
- garnish_and_addons — straw, garnish, stickers-as-shapes
- palette_anchors — which hexes are inherited from the location palette (so icons don't clash with location art)
- reads_at_icon_size — the three things a blind reviewer must see at 128 px
- must_not_look_like — this specific item's known failure modes
- lettering — always "none" for icons; any text-dependent joke is flagged here and moved to flavour copy
```

I back Deepseek's split of `silhouette` and `scale_cue` into two required fields and the `palette_anchors` field; both are in the list above. My addition is `lettering` as an explicit always-"none" field, so no future brief accidentally leans on a readable sticker again.

## Notes for reviewer (Deepseek)

- **My scale solve is deliberately a third option:** not Mistral's overbrim heap, not your low-fill-and-eight-straws. It's **proportion mismatch** — a full pineapple wedge (a known-size object) hanging off a rim so wide it makes the wedge look small — plus the thick rolled pail rim. The tide-line/bare-wall cue overlaps with your low fill; treat that as shared, not stolen.
- **Pre-empting your straw-count critique:** you told Mistral three straws reads as one drinker. I use ONE straw — because my scale solve doesn't live in the straw. The straw is a beverage cue and a reuse cue (tooth marks = strangers' mouths), not a scale argument. If you think one straw still drags it toward "single-serve cup," say so and I'll cut it rather than defend it.
- My hexes: #B5722F (shell), #7A4A21 (husk bumps), #F2E8C9 (drink) are new to the item; #FF1493, #32CD32, #FF7F32 are inherited from `bohemian_riviera.md` (palette anchors, confirmed in location canon).
- Risk I couldn't solve alone: at 64 px the pineapple wedge might read as noise, not a scale cue. If you think it dies at thumbnail size, the fallback is cutting the wedge and leaning harder on the pail rim + bare wall — but then my solve converges with yours and the author loses a genuinely different option. Flag it either way.
