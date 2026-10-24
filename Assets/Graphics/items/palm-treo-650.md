# Palm Treo 650 (Stylus Missing)

> **Asset slug:** `palm-treo-650`  
> **Type / slot:** Cellphone  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 PDA Functionality, ICQ Compatible, -1 Accuracy without stylus.

**Flavor text:** *"The smartphone before smartphones were cool."*

**Era Cringe:** Uses fingernails to navigate touchscreen.

**Why it's funny (the thing the art has to sell):** The stylus is gone. It has been gone for years. He operates the resistive touchscreen with a fingernail, hard, and the screen has the scratches to prove it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A thick slab-style PDA phone in dark blue-grey plastic with a squared-off form, held vertically. A square resistive touchscreen in the upper half showing illegible blocky pixel calendar rows, its surface covered in fine hard-edged scratch marks radiating from the lower right — clearly made by a fingernail. Below, a full QWERTY thumb keyboard with tiny domed silver-grey keys. An empty stylus silo is visible along the top-right edge as a small dark rectangular hole with nothing in it. A stubby external antenna nub. The plastic case is scuffed pale at every corner, and a hairline crack runs from the silo opening. A worn belt-clip mount on the back. Battery door slightly proud on one side.

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
#2B1A2E outline / #3E4A5E body blue-grey / #242C3A body shadow / #6E7E96 body highlight / #A8AEB4 key silver / #6E7478 key shadow / #2E3E4E screen dark / #4E6E8E screen mid / #8EB4D0 screen text / #C4CAD0 scratch mark / #8E8A82 scuff pale / #1A1A1E silo hole / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Thick squared-off dark blue-grey slab PDA phone held vertically, square resistive touchscreen in the upper half showing illegible blocky pixel calendar rows and covered in fine hard-edged fingernail scratch marks radiating from the lower right, full QWERTY thumb keyboard below with tiny domed silver-grey keys, an empty stylus silo along the top-right edge as a small dark rectangular hole with nothing in it, stubby external antenna nub, corners scuffed pale, hairline crack from the silo opening, battery door sitting slightly proud, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #3E4A5E body blue-grey / #242C3A body shadow / #6E7E96 body highlight / #A8AEB4 key silver / #6E7478 key shadow / #2E3E4E screen dark / #4E6E8E screen mid / #8EB4D0 screen text / #C4CAD0 scratch mark / #8E8A82 scuff pale / #1A1A1E silo hole / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Fingernail-input variant (48x48)** — a hand silhouette jabbing the screen with a nail, for the -1 Accuracy tooltip.
- **Stylus-found variant** — a lone stylus as its own tiny quest item, so the party can restore the accuracy penalty.
- **Screen close-up (32x32)** — just the scratch pattern, for the damaged-gear state.

## 6. Art-director notes

- The empty silo is the item name rendered. It must be visible — a dark hole with a clean rectangular edge, top-right.
- Scratch marks should radiate from one corner in an arc, like a nail pivoting. That directionality sells it.
- Thick and square. These generators drift toward slim modern shapes; specify chunky depth every time.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

