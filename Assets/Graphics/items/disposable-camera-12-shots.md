# Disposable Camera (12 Shots Left)

> **Asset slug:** `disposable-camera-12-shots`  
> **Type / slot:** Consumable — Utility / Quest  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Captures evidence for sidequests or embarrassing enemy moments.

**Flavor text:** *"For memories that digital just can't capture."*

**Why it's funny (the thing the art has to sell):** A single-use film camera in the year this game is set. It is used to document humiliations that would be far better documented on a phone, but the phone is a Palm Treo.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A boxy cardboard-and-plastic disposable camera in yellow and black, seen three-quarter front. Thick chunky body. A small round plastic lens on the front, a tiny optical viewfinder window, and a flash panel with a red charge-ready LED as one hard pixel. The plastic thumb-wheel on the top right is visible and worn shiny. A small exposure counter window showing an illegible pixel numeral. The cardboard wrap is scuffed at the corners with white showing through, and one corner has been peeled back to reveal grey plastic underneath. A crooked strip of masking tape holds the flap shut.

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
#2B1A2E outline / #F0C418 camera yellow / #A88A0A yellow shadow / #FFE86E yellow highlight / #1E1E22 camera black / #3A3A42 black highlight / #2A3038 lens / #6E7A88 lens highlight / #E82424 flash LED / #E8E2D2 scuffed white / #C9BFA6 masking tape / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Boxy yellow and black cardboard disposable film camera three-quarter front, thick chunky body, small round plastic lens, tiny viewfinder window, flash panel with a single red charge LED pixel, worn shiny thumb-wheel on top right, exposure counter window with illegible numeral, scuffed corners with white cardboard showing through, one corner peeled back exposing grey plastic, crooked masking tape strip, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #F0C418 camera yellow / #A88A0A yellow shadow / #FFE86E yellow highlight / #1E1E22 camera black / #3A3A42 black highlight / #2A3038 lens / #6E7A88 lens highlight / #E82424 flash LED / #E8E2D2 scuffed white / #C9BFA6 masking tape / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Flash-fired FX frame (96x96)** — camera center, a hard-edged white pixel starburst filling the frame, for the Photo Evidence quest.
- **Used-up variant** — counter at zero, wind wheel locked, tape peeling.
- **Developed-photo prop (32x32)** — a single square print with a blurry pixel-noise image, for the quest reward inventory.

## 6. Art-director notes

- Yellow is the recognition cue. Keep it high and saturated against the grubby set — it should pop in the inventory grid.
- Chunky proportions matter: this should look thicker and cheaper than a real camera.
- The flash starburst variant is reused for the Chadwick 'content' gags — build it once, keyed cleanly.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

