# Four Loko (Original Recipe)

> **Asset slug:** `four-loko-original-recipe`  
> **Type / slot:** Consumable — Revive (Legendary)  
> **World:** Global  
> **Rarity / tier:** Legendary  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Revive + 75% HP restore; grants "Manic" (+Speed, -Accuracy) for 2 turns. Cannot use while Sober.

**Flavor text:** *"Banned in 47 states for a reason. The reason was 'too awesome.'"*

**Why it's funny (the thing the art has to sell):** This is a legendary-tier revival item and it is a tall can of pre-2010 caffeinated malt liquor. It should be lit like a holy relic and still obviously be garbage.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A tall slim 23.5oz malt liquor can, FOUR LOKO, in the original watermelon colorway — screaming hot pink and lime green in aggressive diagonal color-block bands with a black band around the base. The can is beaded with a few hard-edged pixel droplets. It is standing dead center and slightly larger in frame than a normal item, treated as a relic: a faint halo of six or eight radiating hard-edged pale-gold pixel spokes behind it, blocky and pixelated, never soft or glowing. The pull tab is intact and unopened. A small legalistic block of unreadable warning text on the lower band rendered as pure pixel noise.

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
#2B1A2E outline / #E8248C hot pink / #9C0F58 pink shadow / #FF6BB8 pink highlight / #7ED321 lime / #4A8A0F lime shadow / #B4F55E lime highlight / #1A1A1E black band / #F0D874 halo gold / #C9A227 halo gold shadow / #DCE8EE droplet / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tall slim 23.5oz FOUR LOKO malt liquor can in hot pink and lime green diagonal color blocks with a black base band, unopened pull tab, hard-edged pixel condensation droplets, illegible warning text block, framed as a holy relic with a blocky pixelated pale-gold radiating halo behind it, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #E8248C hot pink / #9C0F58 pink shadow / #FF6BB8 pink highlight / #7ED321 lime / #4A8A0F lime shadow / #B4F55E lime highlight / #1A1A1E black band / #F0D874 halo gold / #C9A227 halo gold shadow / #DCE8EE droplet / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Opened variant** — tab popped, one dent, for the post-use state.
- **Full flavor rack (four cans)** — watermelon, blue raspberry, fruit punch, grape — for the Dodgy Off-License premium shelf.
- **Battle-use FX frame** — can vertical, contents arcing out, party member silhouette not shown, hard-edged pink and lime pixel spray.

## 6. Art-director notes

- The halo must be BLOCKY. If the generator returns a soft glow, add 'halo made of individual hard square pixels arranged in radiating spokes, no glow, no bloom, no gradient.'
- Legendary tier means it renders 1.25x the footprint of a common item in the inventory grid. Keep the silhouette tall and narrow.
- This is the single most saturated sprite in the item set. Everything else stays grubby by comparison — that contrast is the tier signal.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

