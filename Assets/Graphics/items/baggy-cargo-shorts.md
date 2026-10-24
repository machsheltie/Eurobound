# Baggy Cargo Shorts (Knee-Length, 47 Pockets)

> **Asset slug:** `baggy-cargo-shorts`  
> **Type / slot:** Legs  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +4 Utility, +2 Dad Energy.

**Flavor text:** *"For carrying energy drinks, protein bars, and childhood trauma."*

**Era Cringe:** Pockets within pockets within pockets.

**Why it's funny (the thing the art has to sell):** There are too many pockets. Some pockets have pockets. Every single one is full and none of them contain anything he needs.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pair of baggy knee-length cargo shorts hanging flat on an invisible form, front view, in washed khaki-beige twill. An absurd number of pockets — at least eight visible from the front alone, in three different sizes, with flaps, snaps, buttons, hook-and-loop tabs and a small zip pocket set inside a larger flap pocket. Every pocket is bulging with unidentifiable contents so the outline is lumpy and irregular. A phone-shaped bulge in one thigh pocket. The fabric is stained at one knee-level pocket corner. A woven belt with a plastic buckle is threaded through and cinched. Loose thread at a torn belt loop. Frayed hems.

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
#2B1A2E outline / #C4B48E khaki / #8E7E5E khaki shadow / #E8DCB8 khaki highlight / #A89268 khaki mid / #6E5E42 pocket shadow / #3A3630 belt woven / #56504A belt highlight / #7E6A4A stain / #D8CEB4 loose thread / #8E8A82 buckle / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Baggy knee-length cargo shorts hanging flat on an invisible form in washed khaki-beige twill, at least eight visible front pockets in three sizes with flaps, snaps, buttons, hook-and-loop tabs and a small zip pocket set inside a larger flap pocket, every pocket bulging so the outline is lumpy and irregular, a phone-shaped bulge in one thigh pocket, stained pocket corner, threaded woven belt with plastic buckle, torn belt loop with loose thread, frayed hems, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C4B48E khaki / #8E7E5E khaki shadow / #E8DCB8 khaki highlight / #A89268 khaki mid / #6E5E42 pocket shadow / #3A3630 belt woven / #56504A belt highlight / #7E6A4A stain / #D8CEB4 loose thread / #8E8A82 buckle / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pockets-inventoried variant (96x64)** — shorts with contents laid out beside them: a protein bar, a folded receipt, three loose keys, a dead lighter, a wrapper. For the Utility stat tooltip.
- **Equipped variant (48x48)** — on a legs silhouette with pale calves and white socks.
- **Alt colorways** — faded olive and stone grey.

## 6. Art-director notes

- Lumpy irregular outline from overstuffed pockets is what makes these read at small size. Keep the bulges pronounced.
- Pocket count is the joke. Add more than feels right, then add two.
- Do not let the generator make these look tactical or military-current. They are mall-brand, 2004, washed out.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

