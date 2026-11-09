# Backwards Trucker Hat (Mesh Back)

> **Asset slug:** `backwards-trucker-hat`  
> **Type / slot:** Head Gear  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Confidence, -1 Intelligence.

**Flavor text:** *"The mesh provides 'ventilation' for all that deep thinking."*

**Era Cringe:** Peak 2003 energy with faded beer logo.

**Why it's funny (the thing the art has to sell):** Worn backwards, which means the sun protection is aimed at his neck and the structured front panel is aimed at nothing. Sweat has bleached a permanent tide-line into the brim.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A five-panel trucker cap shown from a three-quarter rear angle so the mesh back and the plastic snapback closure face the viewer, with the curved brim pointing away and slightly down. Front panel is faded brick-red foam with a cracked screen-printed beer logo rendered as blocky illegible pixel shapes, the print flaking off in visible gaps. The mesh back is white and rendered as a regular grid of 1px holes, yellowed and sagging on one side. The plastic snapback strap has seven visible pegs and is set on the loosest hole. A dark sweat-salt tide-line stains the fabric above the brim. The brim is bent into a tight curve and the edge binding is fraying.

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
#2B1A2E outline / #A83A2E brick red / #6E1E16 red shadow / #D86E5E red highlight / #E8E4D8 mesh white / #B8B4A4 mesh yellowed / #8E8A78 mesh shadow / #C9A227 logo gold / #8A6E14 logo shadow / #7E6E52 sweat stain / #4A423A stain dark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Five-panel trucker cap from a three-quarter rear angle showing the yellowed sagging white mesh back rendered as a regular grid of 1px holes and the plastic snapback strap on the loosest hole, faded brick-red foam front panel with a cracked flaking screen-printed beer logo in illegible pixel shapes, dark sweat-salt tide-line above the brim, tightly bent curved brim with fraying edge binding, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A83A2E brick red / #6E1E16 red shadow / #D86E5E red highlight / #E8E4D8 mesh white / #B8B4A4 mesh yellowed / #8E8A78 mesh shadow / #C9A227 logo gold / #8A6E14 logo shadow / #7E6E52 sweat stain / #4A423A stain dark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Front-facing variant (48x48)** — logo panel toward viewer, for the shop display.
- **Worn-backwards equipped variant** — on a balding head silhouette, brim over the neck.
- **Alt colorways** — faded navy and washed camo, for palette-swap shop stock.

## 6. Art-director notes

- Rear three-quarter is the correct hero angle — the mesh and the snapback ARE the item. Do not let the generator turn it front-on.
- The mesh hole grid must survive downsampling. Consider a 2px hole spacing at 128 so it reads as mesh at 64.
- Sweat tide-line is non-negotiable. It's the detail that ages the hat twenty years.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

