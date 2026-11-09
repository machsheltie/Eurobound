# Muscle Milk (Chalky Vanilla)

> **Asset slug:** `muscle-milk-chalky-vanilla`  
> **Type / slot:** Consumable — Healing  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Restores HP over 3 turns, grants "Gains Bro" (+ATK) for 2 turns.

**Flavor text:** *"Nature's perfect protein, bro. Tastes like liquid chalk and broken dreams."*

**Why it's funny (the thing the art has to sell):** A tub of powder bought in 2009 that has been opened maybe four times. The scoop is buried. The art has to sell 'this has been in a closet for a decade' — not 'fitness product.'

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A squat plastic protein powder tub, MUSCLE MILK, chalky vanilla flavor. Wide black lid, slightly askew, not screwed on straight. Body of the tub is dull pearl-white with a broad electric-blue band and a mustard-yellow stripe. A crude pixel silhouette of a flexing arm on the label. The tub is dented on one side. A cheap translucent plastic scoop is jammed into the lid at an angle, half-buried in beige powder, with a small puff of chalky dust hanging above the opening as three or four loose off-white pixels. A faint powder residue ring is caked around the rim. The label has one corner peeled up.

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
#2B1A2E outline / #F2EAD8 tub base / #C9BFA6 tub shadow / #FFFBF0 tub highlight / #1E4FA8 blue band / #12356E blue shadow / #E8B430 mustard stripe / #A87616 mustard shadow / #211C22 lid / #3A343C lid highlight / #D8C9A4 powder / #B0A183 powder shadow / #8E6A3F residue ring / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Squat plastic protein powder tub labeled MUSCLE MILK vanilla, dented side, black lid askew, translucent scoop jammed in the opening, chalky beige powder puffing out, peeling label corner, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #F2EAD8 tub base / #C9BFA6 tub shadow / #FFFBF0 tub highlight / #1E4FA8 blue band / #12356E blue shadow / #E8B430 mustard stripe / #A87616 mustard shadow / #211C22 lid / #3A343C lid highlight / #D8C9A4 powder / #B0A183 powder shadow / #8E6A3F residue ring / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Empty variant** — lid off, tub tipped, only powder dust at the bottom. Used for the depleted-stack inventory state.
- **Shop-shelf prop (32x32)** — same tub straight-on, no scoop, for the Brew Stall shelf tileset.
- **Battle-use FX frame** — the tub mid-shake, a wide chalky dust cloud of hard-edged off-white pixel blobs bursting from the lid.

## 6. Art-director notes

- The dent is the whole gag. Do not let the generator render a clean retail product — push it toward 'found in a garage.'
- Blue band should sit in the upper third so the silhouette still reads as a tub at 32px.
- If it comes out looking like a paint can, add 'plastic supplement container, wide screw lid' to the subject line.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

