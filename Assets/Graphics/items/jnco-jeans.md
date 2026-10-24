# JNCO Jeans (40-inch leg opening)

> **Asset slug:** `jnco-jeans`  
> **Type / slot:** Legs  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Item Slot, -2 Speed.

**Flavor text:** *"You could hide a small child in each pant leg."*

**Era Cringe:** Each leg contains more fabric than most full outfits.

**Why it's funny (the thing the art has to sell):** Forty-inch leg openings. The hems have been dragged across four countries' worth of pavement and are now shredded to fringe. He is thirty-eight years old.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pair of enormous wide-leg jeans hanging flat on an invisible form, front view. The legs flare dramatically from the knee down into vast trumpet openings far wider than the waist, forming a bell silhouette. Medium-wash blue denim rendered in three flat tones with whiskering at the hips as short hard-edged pale pixel dashes. Oversized embroidered back-pocket stitching visible through the silhouette as blocky illegible pixel shapes. The hems are completely destroyed — shredded into a ragged fringe of frayed pale threads, dark grey with ground-in street dirt for the bottom three pixel rows. A huge cargo pocket on each thigh, one gaping open. The waist is comparatively tiny, exaggerating the flare.

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
#2B1A2E outline / #3E5E96 denim mid / #24406E denim shadow / #6E8EC4 denim highlight / #A8BEDC whiskering / #C9A227 stitching gold / #8A6E14 stitch shadow / #8E8A82 frayed thread / #3A3630 street dirt / #2A2622 dirt dark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Enormous wide-leg jeans hanging flat on an invisible form in front view, legs flaring dramatically from the knee into vast trumpet openings far wider than the small waist forming a bell silhouette, medium-wash blue denim in three flat tones with hard-edged pale whiskering dashes at the hips, blocky illegible embroidered back-pocket stitching, hems shredded into ragged pale frayed fringe with ground-in dark street dirt, huge cargo pocket on each thigh with one gaping open, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #3E5E96 denim mid / #24406E denim shadow / #6E8EC4 denim highlight / #A8BEDC whiskering / #C9A227 stitching gold / #8A6E14 stitch shadow / #8E8A82 frayed thread / #3A3630 street dirt / #2A2622 dirt dark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (64x64)** — on a legs silhouette, feet completely invisible under the fabric.
- **Rear variant** — showing the full embroidered back-pocket graphic.
- **Alt washes** — acid-wash and near-black, for palette-swap shop stock.

## 6. Art-director notes

- The bell silhouette is everything. Waist narrow, hems enormous. If the flare looks reasonable, double it.
- Shredded hems must break the outline raggedly — no clean bottom edge.
- This is one of the largest garment silhouettes in the set; make sure it still reads as trousers and not a skirt at 32px by keeping the center inseam gap visible.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

