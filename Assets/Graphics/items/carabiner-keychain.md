# Carabiner Keychain (No Climbing Experience)

> **Asset slug:** `carabiner-keychain`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Outdoorsy Appearance, +1 Key Security.

**Flavor text:** *"For hanging 47 keys from your belt loop."*

**Era Cringe:** Loudest person in every quiet space.

**Why it's funny (the thing the art has to sell):** A load-rated climbing carabiner used exclusively to hang house keys off a belt loop. It has never been near a rock. It is rated for 24 kilonewtons and is carrying a Blockbuster card.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A large anodized aluminum carabiner in bright electric blue with a spring gate, hanging open at the top. Stamped kN rating numerals along the spine rendered as illegible pixel marks. Hanging from it: an absurd cluster of at least eight keys of wildly different shapes and sizes, a bottle opener, a shrunken rubber keychain mascot with the paint worn off its face, a plastic supermarket fob, and a single novelty key that is obviously not for anything. The anodizing is scuffed to bare silver along the top curve. The gate spring is visibly weakened and doesn't sit flush. Everything overlaps into a heavy jangling mass.

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
#2B1A2E outline / #1E7EE8 anodized blue / #10467E blue shadow / #6EBEFF blue highlight / #A8AEB4 bare aluminum / #6E7278 aluminum shadow / #E0E6EA aluminum highlight / #C9A227 brass key / #8A6E14 brass shadow / #C42A16 mascot red / #8E1A0E mascot shadow / #3A3A42 fob black / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Large bright electric blue anodized aluminum climbing carabiner with a spring gate, illegible stamped kN rating along the spine, anodizing scuffed to bare silver along the top curve, gate not sitting flush, hanging from it an absurd overlapping cluster of at least eight mismatched keys plus a bottle opener, a paint-worn rubber keychain mascot, a plastic loyalty fob and one obviously useless novelty key, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E7EE8 anodized blue / #10467E blue shadow / #6EBEFF blue highlight / #A8AEB4 bare aluminum / #6E7278 aluminum shadow / #E0E6EA aluminum highlight / #C9A227 brass key / #8A6E14 brass shadow / #C42A16 mascot red / #8E1A0E mascot shadow / #3A3A42 fob black / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Belt-loop equipped variant (32x32)** — clipped to a cargo short loop, keys splayed.
- **Minimal variant** — carabiner with two keys, for the 'he finally decluttered' late-game gag.
- **Individual key assets** — the eight keys separated, for reuse in puzzle/quest inventory icons.

## 6. Art-director notes

- Key count is the joke. Eight minimum, more is better. If the cluster reads as tidy, add keys.
- Bright blue anodizing against the grubby palette makes this pop on the accessory shelf — intentional.
- The worn-faced mascot is a small detail that carries the 'this has been on his belt since 2004' story. Keep the face blank.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

