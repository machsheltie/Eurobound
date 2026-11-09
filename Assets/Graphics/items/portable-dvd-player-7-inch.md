# Portable DVD Player (7-inch Screen)

> **Asset slug:** `portable-dvd-player-7-inch`  
> **Type / slot:** Consumable — Full Party Heal (Legendary)  
> **World:** Global  
> **Rarity / tier:** Legendary  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Full party heal + "Entertained" buff (immunity to boredom-based attacks, +Morale) for 5 turns.

**Flavor text:** *"Peak mobile entertainment. Battery lasts exactly 47 minutes."*

**Why it's funny (the thing the art has to sell):** Peak 2004 technology treated as a legendary artifact. It is enormous, it is silver plastic, and it will die in 47 minutes.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A chunky silver-grey portable DVD player, open in a clamshell L-shape, seen at a three-quarter angle. The 7-inch screen shows a scanline-heavy image rendered as horizontal pixel bands in dull blue and grey — no discernible picture, just interlaced noise. Thick plastic bezels, at least twice as thick as they need to be. A row of tiny blocky rubber buttons along the base. A red LED as a single hard pixel. A disc is visible in the top-loading tray, catching the light as a hard rainbow arc of three or four pixel steps. The hinge is loose and the screen tilts slightly off-square. Scuffed edges, one crack in the bezel corner, and a coiled car-adapter cord trailing off the base.

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
#2B1A2E outline / #A8AEB4 silver plastic / #6E7278 silver shadow / #D8DEE4 silver highlight / #1E2A44 screen dark / #3A5478 screen mid / #5E7EA4 screen scanline / #2A2A2E button / #E82424 LED red / #C4C8CC disc / #D83EC0 disc rainbow / #7EC4E8 disc rainbow 2 / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Chunky silver-grey portable DVD player open in a clamshell L-shape at a three-quarter angle, thick oversized plastic bezels, 7-inch screen showing dull blue and grey interlaced pixel scanline noise, row of tiny blocky rubber buttons, single red LED pixel, visible disc in the top tray with a hard-stepped rainbow arc, loose off-square hinge, cracked bezel corner, coiled car adapter cord trailing off, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8AEB4 silver plastic / #6E7278 silver shadow / #D8DEE4 silver highlight / #1E2A44 screen dark / #3A5478 screen mid / #5E7EA4 screen scanline / #2A2A2E button / #E82424 LED red / #C4C8CC disc / #D83EC0 disc rainbow / #7EC4E8 disc rainbow 2 / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Closed variant (48x48)** — clamshell shut, for the inventory grid at small size.
- **Dead-battery variant** — screen black, red LED replaced with nothing, for the 47-minute gag.
- **Battle-use FX frame** — player floating open, hard-edged pixel light bands projecting forward onto the party.

## 6. Art-director notes

- Bezel thickness is the period signal. Push it further than feels right.
- Screen content must be noise, never a recognizable image — that avoids both a licensing problem and a legibility problem at 32px.
- Legendary tier: 1.25x footprint. The open L-shape gives it a distinctive silhouette that reads instantly in the inventory grid — protect that.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

