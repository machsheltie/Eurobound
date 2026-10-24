# Visor (Upside Down)

> **Asset slug:** `visor-upside-down`  
> **Type / slot:** Head Gear  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Sun Protection, +2 Bravado.

**Flavor text:** *"Worn 'ironically' but actually thinks it looks cool."*

**Era Cringe:** The ultimate 'I peaked in college' accessory.

**Why it's funny (the thing the art has to sell):** An upside-down visor. This provides zero sun protection, which is the visor's only function. He believes this reads as playful. It reads as a man who has not been told the truth in years.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A sun visor rendered upside down and rotated so the brim curves upward like a scoop and the terrycloth headband sits along the top. White plastic brim gone cream-yellow with age, with a hairline stress crack running from the edge inward. The headband is terry towelling in faded kelly green with a small embroidered patch rendered as an illegible pixel blob, the stitching pulling loose on one side. A grey sweat stain darkens the inner band. The plastic adjustment strap at the back is visible, brittle and sun-bleached, set on the last notch. Two loose terry loops stick out.

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
#2B1A2E outline / #EDE6D2 brim cream / #C4BCA4 brim shadow / #FBF8EE brim highlight / #2E8E4A terry green / #175E2A green shadow / #6EC488 green highlight / #7E7A6E sweat stain / #4A463E stain dark / #C9C4B4 strap bleached / #8E8A7E strap shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Sun visor rendered upside down so the brim curves upward like a scoop with the terrycloth headband along the top, white plastic brim gone cream-yellow with a hairline stress crack, faded kelly green terry towelling band with an illegible embroidered patch and stitching pulling loose, grey sweat stain on the inner band, brittle sun-bleached plastic adjustment strap on the last notch, two loose terry loops, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE6D2 brim cream / #C4BCA4 brim shadow / #FBF8EE brim highlight / #2E8E4A terry green / #175E2A green shadow / #6EC488 green highlight / #7E7A6E sweat stain / #4A463E stain dark / #C9C4B4 strap bleached / #8E8A7E strap shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Right-way-up variant** — for the shop display, so the player can see he chose this.
- **Equipped variant (48x48)** — upside down on a head silhouette, brim scooping skyward.
- **Alt colorways** — faded maroon and washed navy terry, for palette-swap shop stock.

## 6. Art-director notes

- The upside-down orientation must be unmistakable in the icon, or the item stops being funny. Exaggerate the upward brim curve.
- Terry texture: a 1px irregular stipple in two greens, not a smooth field. Keep it sparse so it survives 32px.
- Cream-yellowed plastic, never white. Age is the whole story.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

