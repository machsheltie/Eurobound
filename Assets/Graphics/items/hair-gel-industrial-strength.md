# Hair Gel (Industrial Strength)

> **Asset slug:** `hair-gel-industrial-strength`  
> **Type / slot:** Consumable — Support  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Grants "Untouchable" status — immunity to wind/weather effects.

**Flavor text:** *"Defies physics, defies logic, defies good taste."*

**Why it's funny (the thing the art has to sell):** A tub of gel with a hold rating that belongs on a construction adhesive. The product inside has partially set into a solid.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A wide squat plastic tub of hair gel with a clear domed lid, sitting slightly open. The gel inside is a translucent electric-teal mass rendered with hard-edged highlight pixels to suggest gloss, and it has partially set — one corner of the surface has hardened into a matte crust with a visible finger-gouge scooped out of it. The tub is glossy black with a chrome-effect band and blocky logo pixels reading as aggressive. Dried gel crust runs down one side of the tub. A single stiffened bristle-clump of hair is stuck to the rim. Hold-strength number rendered as an oversized pixel numeral panel.

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
#2B1A2E outline / #1A1A1E tub black / #3A3A42 black highlight / #16C4C4 gel teal / #0A7E86 teal shadow / #6EF0EE teal highlight / #B8C4C8 crust matte / #A8AEB4 chrome / #6E7278 chrome shadow / #E8EEF0 chrome highlight / #4A3E32 stuck hair / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Wide squat black plastic hair gel tub with a clear domed lid slightly open, translucent electric teal gel inside with a hardened matte crust and a scooped finger gouge, chrome band with blocky aggressive logo, dried gel crust running down the side, a stiffened clump of hair stuck to the rim, oversized hold-strength numeral panel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1A1A1E tub black / #3A3A42 black highlight / #16C4C4 gel teal / #0A7E86 teal shadow / #6EF0EE teal highlight / #B8C4C8 crust matte / #A8AEB4 chrome / #6E7278 chrome shadow / #E8EEF0 chrome highlight / #4A3E32 stuck hair / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Applied FX frame** — a hand-free floating spike of teal-glossed hair, for the Untouchable buff icon.
- **Empty scraped-out variant** — tub with only crust in the corners.
- **Frosted Tips crossover** — pair with `frosted-tips-hair-gel-permanent.md`; render both tubs side by side for the shop shelf.

## 6. Art-director notes


## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

