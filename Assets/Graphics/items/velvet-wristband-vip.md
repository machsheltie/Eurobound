# Velvet Wristband (VIP Access)

> **Asset slug:** `velvet-wristband-vip`  
> **Type / slot:** Accessory — Regional  
> **World:** Debaucheryville  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Club Entry, +2 Bottle Service, +1 Fake Importance.

**Flavor text:** *"Grants access to 'exclusive' areas that aren't actually exclusive."*

**Era Cringe:** Worn even to breakfast to show last night's 'achievements'.

**Why it's funny (the thing the art has to sell):** He paid extra for this. Everyone in the club has one. He has worn it for four days and it now smells. He will not cut it off because then he would be a man without a wristband.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A cloth event wristband lying flat as a flattened loop, in deep crushed-velvet burgundy with a sheen rendered as two hard highlight bands running along its length. A gold foil VIP mark is printed on it as a small blocky illegible pixel shape, half rubbed away. The plastic snap closure is a one-way barbed clasp, clearly not removable without cutting, with the tail end trimmed unevenly by hand. The band is grubby and darkened along one section from four days of wear, with a small dark stain and a frayed edge where the velvet nap has worn through to the woven backing. A faint sticky residue sheen near the clasp. The loop is permanently creased flat.

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
#2B1A2E outline / #7E1E3E velvet burgundy / #4A0E22 burgundy shadow / #B44E6E burgundy highlight / #D86E8E velvet sheen / #C9A227 gold foil / #8A6E14 foil shadow / #5E4A44 grubby dark / #3A2E2A stain / #A89A94 worn backing / #E0E6EA clasp plastic / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Cloth event wristband lying flat as a flattened permanently creased loop in deep crushed-velvet burgundy with two hard sheen highlight bands, a small blocky illegible half-rubbed gold foil VIP mark, one-way barbed plastic snap clasp with a hand-trimmed uneven tail, grubby darkened section from days of wear with a small dark stain and a frayed edge where the velvet nap has worn through to the woven backing, sticky residue sheen near the clasp, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7E1E3E velvet burgundy / #4A0E22 burgundy shadow / #B44E6E burgundy highlight / #D86E8E velvet sheen / #C9A227 gold foil / #8A6E14 foil shadow / #5E4A44 grubby dark / #3A2E2A stain / #A89A94 worn backing / #E0E6EA clasp plastic / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — on a wrist, stacked above the LiveStrong and WWJD bands, which is a genuinely tragic image.
- **Fresh variant** — crisp, clean, gold mark intact, for the moment of purchase.
- **Cut-off variant** — severed and lying limp, for the end-of-city state.

## 6. Art-director notes

- Burgundy velvet against a dark outline is low-contrast; push the sheen bands brighter so the loop separates at 32px.
- Velvet is rendered as two hard sheen bands, never as soft nap. Any gradient and it stops being SNES.
- The barbed one-way clasp is the detail that explains why he still has it on. Make the barbs visible.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

