# T-Mobile Sidekick (Relic)

> **Asset slug:** `t-mobile-sidekick`  
> **Type / slot:** Cellphone — Relic  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 PDA Functionality, ICQ Compatible, -1 Accuracy without stylus, "Ping" 5% chance to interrupt enemies.

**Flavor text:** *"The swivel is the best sound a phone ever made."*

**Era Cringe:** Swivels it open in meetings for the sound.

**Why it's funny (the thing the art has to sell):** The screen swivels open with a satisfying mechanical clack, and that clack is the only remaining source of joy in his life. He does it in quiet rooms on purpose.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A wide landscape-format phone with a swiveling screen, shown mid-swivel — the display panel rotated about forty degrees off its closed position, revealing part of the QWERTY keyboard beneath. Chunky rounded body in dark silver with a rubberized black grip band around the edge, worn shiny and smooth at the thumb positions. The landscape LCD shows an illegible blocky pixel chat interface with a small alert icon. A thumbwheel and two round buttons on the right edge. The swivel pivot is visible as a chunky chrome post with wear marks arcing around it. A stretched wrist lanyard loop dangles from one corner. Keys are worn blank in the center of the keyboard. A rubber trim strip is lifting at the base.

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
#2B1A2E outline / #7E848A body silver / #4E5458 silver shadow / #B4BAC0 silver highlight / #1E1E22 grip black / #3A3A44 grip worn / #56566A grip shiny / #2E5E4E LCD green / #5E9E7E LCD mid / #A8D8C0 LCD text / #A8AEB4 chrome pivot / #8E8A82 wear arc / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Wide landscape-format swivel-screen phone shown mid-swivel with the display panel rotated about forty degrees off closed revealing part of the QWERTY keyboard beneath, chunky rounded dark silver body with a rubberized black grip band worn shiny at the thumb positions, landscape LCD showing an illegible blocky pixel chat interface with an alert icon, thumbwheel and two round buttons on the right edge, chunky chrome swivel pivot with wear marks arcing around it, stretched wrist lanyard loop dangling, keys worn blank in the keyboard center, lifting rubber trim at the base, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7E848A body silver / #4E5458 silver shadow / #B4BAC0 silver highlight / #1E1E22 grip black / #3A3A44 grip worn / #56566A grip shiny / #2E5E4E LCD green / #5E9E7E LCD mid / #A8D8C0 LCD text / #A8AEB4 chrome pivot / #8E8A82 wear arc / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Closed variant (48x48)** — screen fully closed over the keyboard, for the inventory icon.
- **Fully-open variant** — screen swiveled 180 degrees, keyboard exposed, for the ICQ chat interface frame.
- **Ping FX frame (64x64)** — the phone with four hard-edged radiating pixel sound arcs, for the 5% enemy-interrupt proc.

## 6. Art-director notes

- Mid-swivel is the hero pose — it's a unique silhouette nothing else in the item set has. Protect it.
- Worn wear-arc around the pivot is the detail that says he's done this a hundred thousand times.
- This phone is the party's ICQ hardware, so the open variant will get reused in the Wi-Fi hotspot UI. Generate it clean and keyed.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

