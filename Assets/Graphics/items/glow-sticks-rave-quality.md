# Glow Sticks (Rave Quality)

> **Asset slug:** `glow-sticks-rave-quality`  
> **Type / slot:** Consumable — Support / Light  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Illuminates dark areas, minor party mood boost.

**Flavor text:** *"From that warehouse party in '02."*

**Why it's funny (the thing the art has to sell):** Twenty-year-old glow sticks. Two of them are cracked and dead. The party is going to snap them anyway and be genuinely surprised when nothing happens.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A loose bundle of four cylindrical glow sticks lying in a rough fan. Two are cracked and actively lit — one acid green, one hot magenta — rendered as saturated solid color with a hard-edged 1px lighter core stripe, no soft glow, no bloom. The other two are unactivated: dull translucent grey-yellow, clearly dead, one visibly leaking a dark stain at the end. Plastic end-caps in dull white. A tangled length of the cheap plastic connector cord loops around them. A faded paper band on one stick with illegible pixel print.

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
#2B1A2E outline / #7EF018 acid green / #4A9E0A green shadow / #C4FF8E green core / #F018A8 hot magenta / #9E0A66 magenta shadow / #FF8ED8 magenta core / #C4BE96 dead stick / #8E8A6E dead shadow / #E8E4D8 end cap / #2E2418 leak stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Loose fan of four cylindrical glow sticks, two cracked and lit in acid green and hot magenta rendered as flat saturated color with a hard 1px lighter core stripe and no glow or bloom, two unactivated dull translucent grey-yellow and clearly dead with one leaking a dark stain, dull white end caps, tangled plastic connector cord, faded illegible paper band, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7EF018 acid green / #4A9E0A green shadow / #C4FF8E green core / #F018A8 hot magenta / #9E0A66 magenta shadow / #FF8ED8 magenta core / #C4BE96 dead stick / #8E8A6E dead shadow / #E8E4D8 end cap / #2E2418 leak stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Necklace variant** — sticks joined into a loop, for the Debaucheryville rave equipment set.
- **All-dead variant** — four dull sticks, nothing lit, for the gag where none of them work.
- **Light-source overlay (128x128)** — a hard-edged pixel light cone for the dark-area illumination effect, green and magenta versions.

## 6. Art-director notes

- No glow. Say it in every regeneration. The moment these bloom, the sprite stops matching the rest of the set.
- The two dead sticks are the joke — do not let the generator light all four.
- The leak stain is a small detail that reads as 'these are chemically past it.' Keep it.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

