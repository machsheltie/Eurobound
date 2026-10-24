# SET: The Suburban Dad Regression

> **Asset slug:** `set-the-suburban-dad-regression`  
> **Type / slot:** Special Combo Set  
> **World:** Global  
> **Rarity / tier:** Set Bonus  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Visor + Abercrombie Tee + Pleated Khakis + white sneakers with socks. Bonus: +8 Dad Energy, +2 Lawn Care Knowledge, -5 Cool Points.

**Flavor text:** *"Somewhere in Europe, a man is explaining mulch."*

**Why it's funny (the thing the art has to sell):** The final form. He has stopped trying to look young and started looking like a man who owns a leaf blower, except he is doing it in a nightclub queue in another country.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A four-piece outfit laid out as a flat-lay set sheet in a vertical column on the magenta field: at the top the upside-down green terry visor, below it the too-small navy sleeveless muscle tee with its cracked flaking print, below that the short-hemmed pleated stone khakis with their knife creases, and at the bottom a pair of chunky white leather sneakers with white crew socks stuffed into them, socks visible above the collar. Each piece is a separate object with its own outline and small drop shadow, evenly spaced with clear gaps. Three small hard-edged gold pixel plus-signs between the pieces.

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
Combined from the four member items. Key anchors: #2B1A2E outline / #2E8E4A terry green / #EDE6D2 visor cream / #2A3E6E tee navy / #D8CCAE khaki pale / #F0EDE2 sneaker white / #E8E4D4 sock white / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Must index to 16 colors total.

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Four-piece outfit flat-lay set sheet in a vertical column, upside-down green terry visor at top, too-small navy sleeveless muscle tee with cracked flaking print below, short-hemmed pleated stone khakis with knife creases below that, and at the bottom a pair of chunky white leather sneakers with white crew socks stuffed in and visible above the collar, each piece a separate object with its own outline and small drop shadow evenly spaced with clear gaps, three hard-edged gold pixel plus-signs between, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
Combined from the four member items. Key anchors: #2B1A2E outline / #2E8E4A terry green / #EDE6D2 visor cream / #2A3E6E tee navy / #D8CCAE khaki pale / #F0EDE2 sneaker white / #E8E4D4 sock white / #C9A227 plus-sign gold / #6E5F72 cast shadow / #FF00FF chroma key. Must index to 16 colors total.
```

## 5. Variants to generate in the same session

- **Equipped full-body variant (64x96)** — worn on a silhouette, with a visible band of bare ankle between the khaki hem and the sock. That gap is the set bonus made visual.
- **Set-bonus badge (32x32)** — a tiny visor-and-sock-line icon for the Dad Energy buff.
- **Sneaker asset (48x32)** — the white leather sneakers with socks as a standalone footwear sprite; this piece is not in the individual gear list and needs to be built.

## 6. Art-director notes

- The white sneakers with crew socks do not exist as a standalone item file yet. Build them here and consider promoting them to their own footwear entry.
- The ankle gap in the equipped variant is the payoff. Make it wide and unmistakable.
- This is the palest, chalkiest set of the three. Lean into the washed-out palette — it's characterizing.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

