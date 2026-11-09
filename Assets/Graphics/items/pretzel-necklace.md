# Pretzel Necklace (Salt-Crusted)

> **Asset slug:** `pretzel-necklace`  
> **Type / slot:** Necklace — Regional  
> **World:** Publandia  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Snack Access, +1 German Approval, -1 Hygiene.

**Flavor text:** *"Emergency carbs around your neck for maximum efficiency."*

**Era Cringe:** Leaves salt trails on everything you touch.

**Why it's funny (the thing the art has to sell):** Six pretzels on a string worn as jewelry. He eats them off the string throughout the day. By evening it is three pretzels and a lot of crumbs and he is still wearing it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
Six large soft pretzels threaded onto a length of coarse butcher's twine and hung in a loose open circle. The pretzels are a deep glossy brown with paler tan cracks in the crust rendered as hard-edged pixel splits, each dusted with chunky white rock salt as scattered 1x1 and 2x2 pure-white pixels. Two of the six pretzels have visible bites taken out of them, one down to a stump. The twine is stained dark and greasy where it passes through the pretzel holes, and it sags unevenly under the weight. Loose salt and crumb pixels are scattered on the ground beneath. One pretzel is noticeably stale and paler with a dull matte crust.

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
#2B1A2E outline / #8E5A22 pretzel brown / #5E3610 brown shadow / #C48A46 brown highlight / #D8B078 crust crack / #C9BEA8 stale pretzel / #FFFFFF rock salt / #DCD8CC salt shadow / #C9BE96 twine / #7E6A46 twine greasy / #4A3A26 grease stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Six large soft pretzels threaded on coarse butcher's twine hung in a loose open circle, deep glossy brown crust with hard-edged paler tan cracks and chunky white rock salt as scattered 1x1 and 2x2 pure-white pixels, two pretzels with bites taken out and one down to a stump, dark greasy stained twine sagging unevenly through the holes, loose salt and crumb pixels scattered beneath, one pretzel visibly stale with a dull matte paler crust, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #8E5A22 pretzel brown / #5E3610 brown shadow / #C48A46 brown highlight / #D8B078 crust crack / #C9BEA8 stale pretzel / #FFFFFF rock salt / #DCD8CC salt shadow / #C9BE96 twine / #7E6A46 twine greasy / #4A3A26 grease stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — around a neck silhouette, hanging to mid-chest, salt visibly on the shirt below.
- **Depleted variant** — two pretzels left and a lot of bare twine, for the end-of-day state.
- **Single pretzel asset (32x32)** — one pretzel alone, reusable as a Publandia consumable and a market-stall prop.

## 6. Art-director notes

- Rock salt must be pure white 1-2px specks scattered irregularly. Regularity kills it. Ask for 'randomly scattered, uneven distribution, some clumped.'
- The bitten pretzels are what make this a story instead of a prop. Two bites minimum, one severe.
- Sagging twine gives the necklace an asymmetric silhouette that reads better at 32px than a perfect circle would.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

