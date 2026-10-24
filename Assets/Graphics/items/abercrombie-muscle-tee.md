# Abercrombie Muscle Tee (Size Too Small)

> **Asset slug:** `abercrombie-muscle-tee`  
> **Type / slot:** Torso  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Sex Appeal, -2 Comfort.

**Flavor text:** *"If you can still breathe, it's not tight enough."*

**Era Cringe:** Faded logo from 1999, still $89.

**Why it's funny (the thing the art has to sell):** A shirt bought at a size that stopped being accurate around 2008 and worn at that size anyway. The seams are under load. The logo has faded but the price has not.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A sleeveless cotton muscle tee hanging flat on an invisible form, visibly too small — the fabric is stretched horizontally so the printed graphic is distorted wider than it should be, and the side seams pucker. Navy blue cotton, sun-faded to a chalky uneven tone with a paler patch across the chest. A large distressed screen-printed logo, deliberately cracked and flaking, rendered as illegible blocky pixel fragments. The neckline is stretched out and wavy. One shoulder seam has a small split with two threads showing. A cardboard price tag on a plastic barb still hangs from the hem, with an oversized illegible pixel price panel.

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
#2B1A2E outline / #2A3E6E navy / #16244A navy shadow / #52689E navy highlight / #6E7E9E faded patch / #E8E4D8 logo cream / #B8B2A2 logo shadow / #C9BFA6 price tag / #8E8878 tag shadow / #A8A296 loose thread / #4A4238 seam dark / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Sleeveless navy cotton muscle tee hanging flat on an invisible form, visibly too small with the fabric stretched horizontally so the printed graphic distorts wider and the side seams pucker, chalky uneven sun fade with a paler chest patch, large distressed cracked flaking screen-printed logo in illegible blocky fragments, stretched wavy neckline, small split shoulder seam with two loose threads, cardboard price tag still hanging from the hem, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2A3E6E navy / #16244A navy shadow / #52689E navy highlight / #6E7E9E faded patch / #E8E4D8 logo cream / #B8B2A2 logo shadow / #C9BFA6 price tag / #8E8878 tag shadow / #A8A296 loose thread / #4A4238 seam dark / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (48x48)** — on a torso silhouette where the hem does not reach the waistband and the fabric strains.
- **Alt colorways** — washed olive and faded maroon.
- **Torn variant** — the shoulder seam fully split, for the post-battle damaged-gear state.

## 6. Art-director notes

- Horizontal stretch distortion on the print is the smartest detail here. Specify it explicitly — it does the 'too small' work without needing a body.
- Logo must be illegible. Cracked-print texture only.
- The still-attached price tag implies he bought it recently at that size. That's darker and funnier than a vintage shirt. Keep the tag.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

