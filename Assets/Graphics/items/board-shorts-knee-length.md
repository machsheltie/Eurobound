# Board Shorts (Knee-Length)

> **Asset slug:** `board-shorts-knee-length`  
> **Type / slot:** Legs  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Beach Vibes, +1 Flexibility.

**Flavor text:** *"For surfing the concrete waves of suburbia."*

**Era Cringe:** Worn 200 miles from the nearest ocean.

**Why it's funny (the thing the art has to sell):** Board shorts in a landlocked European city, in autumn. He has never surfed. He owns four pairs.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A pair of knee-length board shorts hanging flat on an invisible form, front view, in a loud tropical print — hard-edged pixel hibiscus flowers in coral and white over a teal-and-navy diagonal wave stripe, no gradients, all flat blocks. A white drawstring hangs unevenly from the waistband with one aglet missing and a hard knot. The nylon has a slight sheen rendered as two hard highlight bands. Sun-faded across the seat and one thigh so the print is visibly paler there. A small velcro key pocket with the flap curled up and the hook side gone furry with lint. The side seam has a contrast panel. The hems are stiff and slightly flared.

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
#2B1A2E outline / #2E7E96 teal / #17505E teal shadow / #6EC4D8 teal highlight / #1E2E5E navy / #10183A navy shadow / #E86E5E coral / #A83E32 coral shadow / #FBAE9E coral highlight / #F4F0E4 print white / #C4BEB0 faded patch / #8E9A9E lint grey / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Knee-length board shorts hanging flat on an invisible form in a loud tropical print of hard-edged pixel hibiscus flowers in coral and white over teal and navy diagonal wave stripes with no gradients, uneven white drawstring with one missing aglet and a hard knot, two hard nylon sheen highlight bands, sun-faded paler patches across the seat and one thigh, small velcro key pocket with the flap curled and the hook side furry with lint, contrast side seam panel, stiff slightly flared hems, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #2E7E96 teal / #17505E teal shadow / #6EC4D8 teal highlight / #1E2E5E navy / #10183A navy shadow / #E86E5E coral / #A83E32 coral shadow / #FBAE9E coral highlight / #F4F0E4 print white / #C4BEB0 faded patch / #8E9A9E lint grey / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (48x48)** — on a legs silhouette with pale un-tanned legs, in a clearly non-beach context.
- **Alt prints** — a palm-frond print and an unhinged flame print, for palette-swap shop stock.
- **Wet variant** — darker saturation and drip pixels, for the fountain-related incident.

## 6. Art-director notes

- Print must be flat hard-edged pixel shapes. No airbrush tropical gradient — that's the fastest way to break the SNES read.
- Sun-fade patches are what make these look like they've been worn for a decade. Keep them irregular.
- Pale legs in the equipped variant do the joke. Make the contrast between shorts and skin obvious.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

