# Absinthe Shot (Debaucheryville Special)

> **Asset slug:** `absinthe-shot`  
> **Type / slot:** Consumable — Regional Specialty  
> **World:** Debaucheryville  
> **Rarity / tier:** Rare  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

> [!] **Canon flag:** Source doc names this "Prague Special." The World Naming Consistency Guide forbids real city names in content — renamed to **Debaucheryville Special**. Update `items.md` to match.

---

## 1. What this thing is

**Effect:** Massive damage boost but inflicts "Hallucinating" (random targeting).

**Flavor text:** *"The green fairy has some strong opinions."*

**Why it's funny (the thing the art has to sell):** Tourist-grade absinthe served in a shot glass with a burning sugar cube on a slotted spoon, because the bar knows exactly what the tourist came for. The ritual is theater. The product is paint thinner.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A thick-walled shot glass full of luminous acid-green liquid, sitting on a stained bar coaster. Balanced across the rim is a tarnished slotted absinthe spoon holding a sugar cube that is actively burning — the flame rendered as a small hard-edged pixel shape in blue at the base and orange-yellow at the tip, three distinct color bands, no soft glow. Caramelized sugar drips down into the glass as two dark amber pixel strands. The glass is thumbprint-smudged and the base has a green ring where it was set down in a spill. A curl of hard-edged pixel smoke rises in a stepped diagonal.

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
#2B1A2E outline / #6EE81E absinthe green / #3A9E0A green shadow / #B4FF7E green highlight / #C4D8DC glass / #8EA4A8 glass shadow / #F0F8FA glass highlight / #E8E4D8 sugar cube / #F0A418 flame orange / #F8E86E flame yellow / #3E7EE8 flame blue / #7E6244 spoon tarnish / #A87C3A caramel drip / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Thick-walled shot glass of luminous acid-green absinthe on a stained bar coaster, tarnished slotted spoon balanced across the rim holding a burning sugar cube with a hard-edged three-band pixel flame in blue and orange-yellow and no glow, caramelized sugar dripping into the glass as dark amber strands, thumbprint smudges, green spill ring at the base, stepped diagonal pixel smoke curl, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #6EE81E absinthe green / #3A9E0A green shadow / #B4FF7E green highlight / #C4D8DC glass / #8EA4A8 glass shadow / #F0F8FA glass highlight / #E8E4D8 sugar cube / #F0A418 flame orange / #F8E86E flame yellow / #3E7EE8 flame blue / #7E6244 spoon tarnish / #A87C3A caramel drip / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Unlit variant** — spoon and sugar cube resting, no flame, for the shop shelf.
- **Hallucinating status icon (24x24)** — just a small acid-green fairy silhouette in hard pixels, for the debuff strip.
- **Bottle variant (64x64)** — the full absinthe bottle with a hand-written label, for the Absinthium Taproom back-bar tileset.

## 6. Art-director notes

- The flame is the hardest element. Three hard color bands, stepped, no gradient. If it blooms, regenerate with 'flame made of flat hard-edged pixel blocks in three distinct colors, no glow, no gradient, no transparency.'
- Green must be the most saturated thing in the sprite and should visually rhyme with the Green Fairy Wisp enemy palette.
- The smoke curl is a stepped diagonal staircase of single pixels — very EarthBound. Keep it short, 6-8 pixels.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

