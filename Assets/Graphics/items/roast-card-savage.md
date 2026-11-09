# Roast Card (Savage)

> **Asset slug:** `roast-card-savage`  
> **Type / slot:** Consumable — Offensive (Scaling)  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Deals damage based on enemy's current confidence level.

**Flavor text:** *"Your mom jokes, but make them hurt."*

**Why it's funny (the thing the art has to sell):** A trading-card-sized index card with a handwritten insult on it. Chadwick made a deck of these. He laminated them. He rates them by tier.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single index card, portrait orientation, held-and-carried worn — soft rounded corners, one corner creased over. Off-white card stock with faint blue ruled lines. A handwritten insult in blocky dark blue ballpoint rendered as pure illegible pixel scribble, three short lines of it, deliberately unreadable. In the top-right corner a hand-drawn tier marker: three small hard-edged flame shapes in orange and red pixels. The bottom edge has a thin strip of yellowed clear tape where it was badly laminated. A coffee ring stain crosses the lower left.

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
#2B1A2E outline / #EDE8D8 card stock / #C4BFAE card shadow / #FBF8EE card highlight / #8EA8C4 ruled lines / #1E3A7E ballpoint blue / #E86A18 flame orange / #C42A16 flame red / #F0C438 flame yellow / #C9A56E coffee ring / #E8E4C8 tape yellowed / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Worn off-white index card in portrait orientation with faint blue ruled lines, three lines of illegible blocky dark blue ballpoint pixel scribble, one creased corner, hand-drawn three-flame tier marker in orange and red pixels in the top right, yellowed clear tape strip along the bottom edge, coffee ring stain, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE8D8 card stock / #C4BFAE card shadow / #FBF8EE card highlight / #8EA8C4 ruled lines / #1E3A7E ballpoint blue / #E86A18 flame orange / #C42A16 flame red / #F0C438 flame yellow / #C9A56E coffee ring / #E8E4C8 tape yellowed / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Tier set (three cards)** — one flame, two flames, three flames, fanned out. For the shop display.
- **Battle-use FX frame** — card held toward camera, hard-edged orange pixel impact starburst behind it.
- **Burnt variant** — card charred at the edges, for the post-crit state.

## 6. Art-director notes

- Text must be illegible scribble. If the generator renders readable words it becomes a translation problem for localization.
- The flame tier marker is how the player reads rarity at a glance — keep it high-contrast and top-right consistently across all Roast Card variants.
- Card should read as index card, not playing card. No suit symbols, no rounded playing-card border.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

