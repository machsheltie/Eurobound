# Collapsed Light Stand

> **Asset slug:** `weapon-collapsed-light-stand`  
> **Type / slot:** Weapon — Chadwick (Alt)  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Staff and spear moveset; can blind enemies when "deployed".

**Flavor text:** *"Three hundred dollars. Used exactly twice."*

**Why it's funny (the thing the art has to sell):** A light stand, collapsed, used as a quarterstaff. Deploying it takes four seconds during which he is completely defenseless and he does it anyway, for the presentation.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A collapsed three-section light stand held vertically, the tripod base folded flat against the column so the three legs lie parallel to the shaft like a fluted spear butt. Chrome-plated steel sections with black plastic knurled tightening knobs, two of which are cross-threaded and sitting crooked. A brass spigot at the top with a small illegible pixel size stamp. The chrome is pitted with rust at every joint as small irregular orange pixel patches, and one leg is visibly bent so the fold does not sit flush. The rubber leg feet are cracked and one is missing, showing bare tube. A knotted length of black bungee cord holds the legs closed. A faded price sticker still on the column.

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
#2B1A2E outline / #B4BAC0 chrome / #7A8086 chrome shadow / #EDF2F6 chrome highlight / #B84A16 rust / #7E2E0A rust dark / #1E1E24 knob black / #38383E knob highlight / #C9A227 brass spigot / #2A2A32 bungee cord / #4A4A52 rubber foot / #C9BE8E price sticker / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Collapsed three-section light stand held vertically with the tripod base folded flat against the column so the three legs lie parallel to the shaft like a fluted spear butt, chrome-plated steel sections with black plastic knurled tightening knobs two of which sit crooked and cross-threaded, brass spigot at the top with an illegible pixel size stamp, chrome pitted with small irregular orange rust patches at every joint, one leg visibly bent so the fold does not sit flush, cracked rubber leg feet with one missing showing bare tube, knotted black bungee cord holding the legs closed, a faded price sticker on the column, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #B4BAC0 chrome / #7A8086 chrome shadow / #EDF2F6 chrome highlight / #B84A16 rust / #7E2E0A rust dark / #1E1E24 knob black / #38383E knob highlight / #C9A227 brass spigot / #2A2A32 bungee cord / #4A4A52 rubber foot / #C9BE8E price sticker / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Deployed variant (64x96)** — fully extended with legs splayed, for the blind-attack setup pose.
- **Deploy Blind FX frame (96x96)** — a hard-edged flat white pixel starburst from the spigot end with an enemy silhouette recoiling.
- **Battle idle sprite (48x48)** — front-view combat orientation, held as a staff.

## 6. Art-director notes

- Folded legs parallel to the column give this a fluted silhouette that distinguishes it from the tripod leg and boom pole at 32px. Protect that.
- Rust at every joint. Chrome fails at joints first and it's the fastest way to age plated steel.
- The knotted bungee holding it shut is a small, specific detail that says he lost the original strap years ago.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

