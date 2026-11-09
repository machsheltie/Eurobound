# Bail-Out Card

> **Asset slug:** `bail-out-card`  
> **Type / slot:** Consumable — Escape  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Guaranteed escape from any battle, no penalties or shame.

**Flavor text:** *"Daddy's credit card saves the day again."*

**Why it's funny (the thing the art has to sell):** A grown man in his late thirties carries his father's credit card as an escape item. The name on the card is not his. Everyone knows.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single credit card seen at a slight angle, gold-toned with a worn magnetic stripe on the back edge just visible. Raised embossed numbers rendered as a row of chunky pale-gold pixel blocks, deliberately unreadable. The embossed name line is longer than the card's owner would like. One corner of the card is bent and creased white. The gold plating has rubbed through to dull grey along the top edge and around the chip. A greasy fingerprint smudge sits across the center. A tiny hologram square rendered as three pixels of shifting cyan-magenta.

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
#2B1A2E outline / #C9A227 card gold / #8A6E14 gold shadow / #F0D874 gold highlight / #7E7A72 rubbed grey / #4A473F grey shadow / #E8E2D2 crease white / #2A2A2E mag stripe / #3EC6D8 holo cyan / #D83EC0 holo magenta / #A89A70 smudge / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Worn gold credit card at a slight angle, chunky illegible embossed numbers, long embossed name line, one corner bent and creased white, gold plating rubbed through to grey along the top edge, greasy fingerprint smudge across the middle, tiny cyan-magenta hologram square, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A227 card gold / #8A6E14 gold shadow / #F0D874 gold highlight / #7E7A72 rubbed grey / #4A473F grey shadow / #E8E2D2 crease white / #2A2A2E mag stripe / #3EC6D8 holo cyan / #D83EC0 holo magenta / #A89A70 smudge / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Declined variant** — card with a hard red X or a cut corner, for the late-game 'he finally froze it' beat.
- **In-wallet variant (32x32)** — card peeking out of a chain wallet, for the equipment-combo screen.
- **Battle-use FX frame** — card held up flat toward camera, a burst of radiating gold pixel lines behind it like a summon.

## 6. Art-director notes


## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

