# Stale Beer Nuts

> **Asset slug:** `stale-beer-nuts`  
> **Type / slot:** Consumable — Offensive (Throwable)  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Throw at enemies for minor damage + "Distracted" status.

**Flavor text:** *"Weaponized bar snacks from 2003."*

**Why it's funny (the thing the art has to sell):** A bar-top bowl of nuts that has been sitting out long enough to become ordnance. The joke is that they're being thrown, not eaten.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A small shallow amber-brown bar bowl, chipped on the rim, filled with dull reddish-brown coated peanuts. The nuts are rendered as irregular 3x3 pixel lumps with one highlight pixel each, deliberately uneven, some paler and dried out. A few loose nuts have escaped onto the ground beside the bowl. A visible dusting of salt and nut-skin debris. The bowl's glaze is scratched and cloudy. One nut in the pile is noticeably grey-green and should read as wrong.

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
#2B1A2E outline / #8E4A1E nut base / #5C2C0F nut shadow / #C47A3E nut highlight / #A8641E bowl amber / #6E3C10 bowl shadow / #D89A56 bowl highlight / #E8E2D2 salt / #7A8A5E wrong nut green / #C9BFA6 debris / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Small shallow chipped amber bar bowl filled with dull reddish-brown coated peanuts rendered as irregular pixel lumps, several loose nuts spilled beside it, salt and skin debris dusting, cloudy scratched glaze, one visibly grey-green nut in the pile, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #8E4A1E nut base / #5C2C0F nut shadow / #C47A3E nut highlight / #A8641E bowl amber / #6E3C10 bowl shadow / #D89A56 bowl highlight / #E8E2D2 salt / #7A8A5E wrong nut green / #C9BFA6 debris / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Thrown-projectile sprite (16x16)** — three nuts in a loose spray, for the battle throw animation.
- **Empty bowl variant** — just salt residue and one nut, for the depleted state.
- **Overworld bar-top prop (32x32)** — bowl straight-on for the Temple Bar Alley counter tileset.

## 6. Art-director notes

- The one bad nut is worth the pixel. It's the detail that turns 'bowl of nuts' into a joke.
- Nuts must read as individual lumps at 64px — resist any smoothing into a single mass.
- Bowl chip should break the silhouette so the object doesn't read as a generic bowl at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

