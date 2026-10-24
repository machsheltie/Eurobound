# Slap Bracelet (Leopard Print)

> **Asset slug:** `slap-bracelet-leopard`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Nostalgia, +2 Juvenile Regression.

**Flavor text:** *"Slaps wrist with the force of lost childhood."*

**Era Cringe:** Worn to 'break the ice' at parties.

**Why it's funny (the thing the art has to sell):** He carries a slap bracelet to parties and deploys it on strangers as an icebreaker. The fabric has split and the bare spring steel underneath has drawn blood at least once.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A leopard-print slap bracelet shown half-curled — one end coiled into a tight spiral and the other end still straight, caught mid-transition. The fabric wrap is a loud tan-and-black leopard print rendered as hard-edged irregular pixel rosettes, faded and pilled with a fuzzy worn nap along the high points. At the straight end the fabric has split open and peeled back, exposing a strip of bare blue-grey spring steel with a sharp visible edge and a small rust bloom. The stitched seam along one side has burst in two places. A dark stain near the coiled end. The steel shows a permanent kink where it has been over-bent.

STYLE RULES — follow all of them:
- Medium: 1990s Super Nintendo item sprite, drawn in the visual language of *EarthBound / MOTHER 2*.
- Framing: one single object, centered, slight three-quarter front view, floating on a flat pure-magenta `#FF00FF` chroma-key field. Nothing else in frame.
- Pixels: chunky, deliberate, visible square pixels. No anti-aliasing. No soft gradients. No blur. Ordered/checkerboard dither only, used sparingly.
- Palette: hard limit of 16 colors (15 + transparency), SNES 15-bit-safe. Warm and a little grubby — brick red, mustard, dull teal, muddy denim, off-cream. Never neon-clean.
- Outline: 1px dark plum-brown `#2B1A2E`, never pure black. Outline thickens by one pixel on the underside of the object.
- Shading: flat cel shading, exactly three tones per material — base, one shadow, one highlight — plus a single hard specular pixel-cluster. Light source upper-left.
- Form language: slightly lumpy and hand-sculpted, as though the object were built out of modeling clay, photographed, then reduced to pixels — the MOTHER 2 clay-model look. Edges bulge. Nothing is perfectly straight or perfectly symmetrical.
- Shadow: one small hard-edged elliptical drop shadow directly beneath the object, no blur, 1 tone darker than the key field.
- Readability: the silhouette must still read as the correct object when scaled down to 32x32.

PALETTE — use these and nothing else:
#2B1A2E outline / #C9A056 leopard tan / #96743A tan shadow / #E8CE96 tan highlight / #2A2018 leopard black / #4A3C2E black highlight / #7E8A96 spring steel / #4E5A66 steel shadow / #C4D0DA steel highlight / #B84A16 rust / #8E8478 pilled nap / #3E3228 stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Leopard-print slap bracelet shown half-curled with one end in a tight spiral and the other still straight caught mid-transition, loud tan and black leopard fabric rendered as hard-edged irregular pixel rosettes faded and pilled with a fuzzy worn nap, the fabric split and peeled back at the straight end exposing bare blue-grey spring steel with a sharp edge and a small rust bloom, burst stitching in two places, dark stain near the coil, permanent kink in the steel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A056 leopard tan / #96743A tan shadow / #E8CE96 tan highlight / #2A2018 leopard black / #4A3C2E black highlight / #7E8A96 spring steel / #4E5A66 steel shadow / #C4D0DA steel highlight / #B84A16 rust / #8E8478 pilled nap / #3E3228 stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Deployed FX frame (48x48)** — the bracelet fully coiled with three hard-edged impact pixel bursts, for the icebreaker gag.
- **Flat variant** — fully straight, for the inventory icon where the half-coil might read as damage.
- **Alt prints** — neon zebra and a 1990s geometric pattern, for palette-swap stock.

## 6. Art-director notes

- Half-curled is the hero pose — it's instantly recognizable and gives a distinctive silhouette at 32px.
- Exposed steel is the danger detail and it's what makes the item funny rather than just nostalgic. Keep the sharp edge visible.
- Leopard rosettes must be hard-edged irregular pixel blobs. Any soft or photographic print texture and the SNES read collapses.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

