# Mood Necklace (Perpetually Black)

> **Asset slug:** `mood-necklace-perpetually-black`  
> **Type / slot:** Necklace  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Emotional Awareness, +2 Melancholy.

**Flavor text:** *"Always shows 'stressed' or 'horny'."*

**Era Cringe:** Bought from a mall novelty shop in 2001.

**Why it's funny (the thing the art has to sell):** The stone is permanently black. It has been black for twenty years. The chart on the back says black means 'stressed / tense.' He has never once checked.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A teardrop-shaped mood pendant on a thin tarnished silver chain, laid flat with the chain in a loose S. The stone is a domed oval of liquid-crystal glass that is completely opaque black — flat, dead, with just two hard specular highlight pixels on the dome to show it is glass. A cheap silver-tone bezel setting, tarnished to a dull grey-brown with green oxidation in the crevices. The chain is thin, kinked in two places, with a lobster clasp that has lost its plating. Behind the pendant, a small folded paper mood-chart card is visible, water-damaged and illegible, its color swatches faded to pale ghosts.

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
#2B1A2E outline / #0E0E14 stone black / #22222C stone mid / #4E4E5E stone spec / #8E8A88 bezel tarnish / #5E5A58 bezel shadow / #B8B4B0 bezel highlight / #6E8A4A oxidation green / #A8AEB4 chain silver / #6E7278 chain shadow / #D8D4C4 chart paper / #B0AC9C paper stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Teardrop mood pendant on a thin tarnished silver chain laid flat with the chain in a loose S, the domed oval liquid-crystal stone completely opaque dead black with just two hard specular highlight pixels, cheap silver-tone bezel tarnished to dull grey-brown with green oxidation in the crevices, thin chain kinked in two places with a lobster clasp that has lost its plating, a small water-damaged folded paper mood-chart card behind it with color swatches faded to pale ghosts, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #0E0E14 stone black / #22222C stone mid / #4E4E5E stone spec / #8E8A88 bezel tarnish / #5E5A58 bezel shadow / #B8B4B0 bezel highlight / #6E8A4A oxidation green / #A8AEB4 chain silver / #6E7278 chain shadow / #D8D4C4 chart paper / #B0AC9C paper stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Working variant (32x32)** — the same pendant lit teal-blue, for a one-time gag when it briefly works and everyone panics.
- **Chart close-up (32x32)** — the mood chart card readable-ish, for the tooltip.
- **Pairs with** `mood-ring-stuck-on-angry.md` — same stone tech, same dead black. Generate together for consistency.

## 6. Art-director notes

- Dead black. No color, no shimmer, no iridescence. The whole point is that it has stopped working.
- Two specular pixels only. That's what separates 'black glass' from 'a hole in the sprite.'
- Green oxidation in the bezel crevices is the cheapest-jewelry tell. Keep it subtle — three or four pixels.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

