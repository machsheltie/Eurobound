# Bar Mat Cloak (Sticky Surface)

> **Asset slug:** `bar-mat-cloak`  
> **Type / slot:** Torso — Regional  
> **World:** Publandia  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +4 Spill Resistance, +1 Bartender Respect, -2 Fashion.

**Flavor text:** *"Repurposed bar equipment as haute couture."*

**Era Cringe:** Attracts flies and makes squelching sounds when you move.

**Why it's funny (the thing the art has to sell):** A rubber drip mat from behind the bar, worn as a cape. It is saturated. It squelches. A bartender saw him take it and said nothing, out of respect or resignation.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A long ribbed rubber bar drip mat draped as a cloak, hanging in a rough trapezoid with the top edge gathered and fastened at the neck by a bent bottle-opener used as a clasp. The mat is dark forest green rubber with a regular grid of raised ribs and drainage slots rendered as hard-edged parallel pixel channels. The surface is visibly saturated — three shades of dark wet patching, with two hard-edged amber puddles caught in the channels and a slow drip forming at the lower edge. Faint white lettering along one edge, illegible pixel shapes, half worn off. Two small dark fly silhouettes hover nearby as 2px shapes. The bottom edge is cracked and split in two places from age.

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
#2B1A2E outline / #2E4A32 rubber green / #172E1A green shadow / #4E7E54 green highlight / #1A2E1E wet dark / #0E1A10 wet darkest / #C98E2E amber puddle / #96641A puddle shadow / #E8E4D8 worn lettering / #A8AEB4 opener clasp / #1A1A1E fly / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Long ribbed dark forest green rubber bar drip mat draped as a cloak in a rough trapezoid with the top edge gathered and fastened at the neck by a bent bottle opener used as a clasp, regular grid of raised ribs and drainage slots as hard-edged parallel pixel channels, visibly saturated with three shades of dark wet patching and two hard-edged amber puddles caught in the channels and a drip forming at the lower edge, half-worn illegible white lettering along one edge, two small 2px fly silhouettes hovering nearby, cracked split bottom edge, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E4A32 rubber green / #172E1A green shadow / #4E7E54 green highlight / #1A2E1E wet dark / #0E1A10 wet darkest / #C98E2E amber puddle / #96641A puddle shadow / #E8E4D8 worn lettering / #A8AEB4 opener clasp / #1A1A1E fly / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (64x64)** — draped over a torso silhouette, hanging to mid-thigh, one amber drip mid-fall.
- **Squelch FX frame (48x48)** — three hard-edged pixel sound arcs plus two droplet pixels flying off, for the movement gag.
- **Flat variant (48x48)** — the mat laid flat on a bar top, for the Temple Bar Alley tileset.

## 6. Art-director notes

- The rib-and-channel grid is what identifies this object. Without it, it's a green rectangle. Keep the channels at 2px spacing minimum so they survive the downsample.
- Saturation is told through three tones of wet patching, not through gloss. Do not let it go shiny.
- The bottle-opener clasp is a great detail — it says he improvised this in about forty seconds. Keep it visible.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

