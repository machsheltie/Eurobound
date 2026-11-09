# Advil (Half Empty Bottle)

> **Asset slug:** `advil-half-empty-bottle`  
> **Type / slot:** Consumable — Status Cure  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Cures status effects, small HP restore.

**Flavor text:** *"For when last night catches up with this morning."*

**Why it's funny (the thing the art has to sell):** The bottle is half empty and the cotton ball is long gone. This is the single most-used item in the party's shared inventory and it shows.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A small squat amber-brown plastic pill bottle, ADVIL, with a white child-proof cap that has been left half-unscrewed and sits tilted. The bottle is translucent enough that you can see the fill line — only about a third of the way up — with dark liquid-gel capsules visible as a lumpy mass of maroon pixels inside. The paper label is scuffed, with a corner torn off and one edge lifting. Two loose brown-red gel caps sit on the ground beside the bottle, one on its side. No cotton ball. The cap has a hairline crack.

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
#2B1A2E outline / #B26A22 bottle amber / #7C4514 amber shadow / #E09A45 amber highlight / #F4F1E8 cap white / #C9C4B6 cap shadow / #8E1F2A capsule maroon / #5C1119 capsule shadow / #E8E2D2 label paper / #B6AF9C label shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Small amber plastic pill bottle labeled ADVIL, white child-proof cap half-unscrewed and tilted, visible low fill line of maroon gel capsules inside, torn scuffed label, two loose capsules lying beside it, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #B26A22 bottle amber / #7C4514 amber shadow / #E09A45 amber highlight / #F4F1E8 cap white / #C9C4B6 cap shadow / #8E1F2A capsule maroon / #5C1119 capsule shadow / #E8E2D2 label paper / #B6AF9C label shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Full variant** — capsules to the neck, cap on straight, cotton ball visible. For the pre-Publandia 'before' gag.
- **Empty variant** — bottle on its side, cap off, one lonely capsule rolling out.
- **Shop-shelf prop (32x32)** — upright, cap on, for the pharmacy/off-license shelf.

## 6. Art-director notes

- The fill line is the joke — make sure the transition from empty amber to capsule mass is a hard pixel edge, clearly visible at 64px.
- Do not render a modern squeeze-clear bottle. Amber brown, opaque-ish, 2000s drugstore.
- Keep the label type blocky and low-res — three or four pixel rows suggesting letters is better than legible text.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

