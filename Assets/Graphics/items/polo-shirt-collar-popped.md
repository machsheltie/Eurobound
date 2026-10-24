# Polo Shirt (Collar Popped)

> **Asset slug:** `polo-shirt-collar-popped`  
> **Type / slot:** Torso  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Prep Status, +1 Douchebag Aura.

**Flavor text:** *"Double-popped for maximum authority."*

**Era Cringe:** Available in salmon, mint, and 'aggressive yellow'.

**Why it's funny (the thing the art has to sell):** Two polos, layered, both collars popped. This is a structural decision. It requires planning. He does it on purpose every day.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
Two polo shirts layered and shown as a single flat-laid garment object from the front, hanging as if on an invisible form. The outer polo is salmon pink, the inner is mint green, and both collars are popped up and stiff, forming a rigid double fan around an empty neck opening. Three-button placket, top two undone, the buttons rendered as small hard-edged discs. The pink fabric has faded unevenly with a paler sun-bleached shoulder line. A tiny embroidered chest logo as an illegible pixel blob. Sleeve hems are slightly rolled. One small permanent grease spot near the hem. The fabric hangs with a stiff pique texture rendered as a fine regular 1px stipple.

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
#2B1A2E outline / #E8907E salmon / #A8564A salmon shadow / #FFC4B4 salmon highlight / #8ED8A8 mint / #4E9E6E mint shadow / #C4F5D8 mint highlight / #F4F0E8 button / #C4BEB0 button shadow / #C9A227 logo gold / #7E6A4A grease spot / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Two polo shirts layered as one flat-laid garment from the front hanging on an invisible form, outer salmon pink and inner mint green, both collars popped stiff into a rigid double fan around an empty neck opening, three-button placket with the top two undone, uneven sun-bleached shoulder fade, tiny illegible embroidered chest logo, rolled sleeve hems, one grease spot near the hem, fine 1px stipple pique texture, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #E8907E salmon / #A8564A salmon shadow / #FFC4B4 salmon highlight / #8ED8A8 mint / #4E9E6E mint shadow / #C4F5D8 mint highlight / #F4F0E8 button / #C4BEB0 button shadow / #C9A227 logo gold / #7E6A4A grease spot / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Single-polo variant** — one shirt, collar down, for the 'before he decided this was his thing' shop version.
- **Aggressive yellow colorway** — palette swap, plus a mint-over-salmon inversion.
- **Equipped variant (48x48)** — on a torso silhouette with a visible gut, collars framing the jaw.

## 6. Art-director notes

- Both collars popped, clearly two separate collars. If the generator merges them into one thick collar, add 'two distinct layered collars, inner collar visible behind and slightly above the outer.'
- Salmon over mint is the canonical colorway. Keep it — it's specific enough to be funny.
- Flat-laid on an invisible form reads better in an inventory grid than a folded shirt. Keep the neck opening empty and dark.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

