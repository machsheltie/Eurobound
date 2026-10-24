# BlackBerry Pearl (Trackball Sticky)

> **Asset slug:** `blackberry-pearl`  
> **Type / slot:** Cellphone  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Special "Business Mode" buff: +2 Negotiation for one battle, ICQ Compatible.

**Flavor text:** *"For staying connected to that corporate lifestyle."*

**Era Cringe:** Trackball hasn't worked properly since 2007.

**Why it's funny (the thing the art has to sell):** He calls it his 'work phone.' There is no work. The trackball only scrolls down. He has adapted by scrolling all the way around.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A compact candybar smartphone in glossy black with a chrome side rail, held vertically. A small landscape LCD in the top half showing an illegible blocky pixel inbox list with a message-count badge. Below it, a condensed QWERTY-style keypad where each key carries two characters, rendered as tiny rounded rectangles. Dead center between the screen and keypad sits a small white trackball in a chrome ring — visibly grimy, with a dark ring of accumulated lint packed around its housing and the ball itself sitting slightly low and off-center in its socket. The glossy black is covered in fingerprint smudges. The chrome rail is scratched. A rubber charging-port cover hangs loose.

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
#2B1A2E outline / #16161A gloss black / #34343E black mid / #56566A black spec / #A8AEB4 chrome / #6E7478 chrome shadow / #E8EEF2 chrome highlight / #2E4E3E LCD green / #5E8E6E LCD mid / #A8CEB4 LCD text / #EDE8DA trackball white / #4A443A lint grime / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Compact glossy black candybar smartphone with a chrome side rail held vertically, small landscape LCD in the top half showing an illegible blocky pixel inbox list with a message-count badge, condensed QWERTY-style keypad below with two characters per tiny rounded key, a small white trackball dead center in a chrome ring sitting slightly low and off-center in its socket with a dark ring of accumulated lint packed around the housing, heavy fingerprint smudges on the gloss, scratched chrome rail, loose rubber port cover, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #16161A gloss black / #34343E black mid / #56566A black spec / #A8AEB4 chrome / #6E7478 chrome shadow / #E8EEF2 chrome highlight / #2E4E3E LCD green / #5E8E6E LCD mid / #A8CEB4 LCD text / #EDE8DA trackball white / #4A443A lint grime / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Business Mode FX frame (48x48)** — phone with three hard-edged pixel 'important' arcs and a tiny illegible pixel spreadsheet on screen, for the +2 Negotiation buff.
- **Trackball close-up (32x32)** — the grimy ball and lint ring, for the tooltip.
- **Held-variant** — gripped in a hand silhouette with a thumb on the trackball.

## 6. Art-director notes

- The lint ring around the trackball is the detail that makes this specific rather than generic. Keep it dark and unmistakable.
- Gloss black is a trap — render it as three flat tones plus one hard spec band, never as a gradient.
- Keypad keys should read as a dense grid at 64px; don't attempt legible characters.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

