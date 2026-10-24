# Weighted Keg Tap Handle

> **Asset slug:** `weapon-weighted-keg-tap-handle`  
> **Type / slot:** Weapon — Bradley (Alt)  
> **World:** Publandia  
> **Rarity / tier:** Rare  
> **Canon source:** `bradleysweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Heavy crushing attacks; can dispense "liquid courage" buffs.

**Flavor text:** *"Taken from the one establishment that banned him for life."*

**Why it's funny (the thing the art has to sell):** A tap handle wrenched off a bar, weighted at the base, swung like a mace. It is a trophy from a lifetime ban. He tells the ban story as though it were a knighthood.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A tall carved wooden beer tap handle mounted on a heavy steel base collar, held vertically like a short mace. The handle is a lacquered dark hardwood shaped into a tapering column with a broad shield-shaped medallion at the top bearing an illegible blocky pixel brewery crest in gold and cream, the paint chipped at the edges. The lacquer is chipped and one long crack runs down the grain. Below, the threaded steel ferrule is still attached — with a jagged section of torn brass tap collar hanging off it where it was wrenched free, wrenched threads visible as hard-edged pixel spirals. A wrap of black grip tape covers the lower shaft. Dried beer residue crusts the ferrule. A lead weight ring is bolted to the base with two visible hex bolts.

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
#2B1A2E outline / #5E3216 hardwood dark / #381C08 wood shadow / #8E5A2E wood highlight / #C9A227 crest gold / #8A6E14 gold shadow / #EDE4C8 crest cream / #A8AEB4 steel ferrule / #6E7478 steel shadow / #C98E2E brass collar / #8E6A18 brass shadow / #8E7A56 beer residue / #1A1A1E grip tape / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Tall carved lacquered dark hardwood beer tap handle on a heavy steel base collar held vertically like a short mace, tapering column with a broad shield-shaped medallion at the top bearing an illegible blocky pixel brewery crest in gold and cream with chipped paint edges, chipped lacquer and one long grain crack, threaded steel ferrule still attached with a jagged torn section of brass tap collar hanging off it and wrenched threads as hard-edged pixel spirals, black grip tape on the lower shaft, dried beer residue crusting the ferrule, a lead weight ring bolted to the base with two hex bolts, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #5E3216 hardwood dark / #381C08 wood shadow / #8E5A2E wood highlight / #C9A227 crest gold / #8A6E14 gold shadow / #EDE4C8 crest cream / #A8AEB4 steel ferrule / #6E7478 steel shadow / #C98E2E brass collar / #8E6A18 brass shadow / #8E7A56 beer residue / #1A1A1E grip tape / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Liquid Courage FX frame (96x64)** — the handle pulled forward with a hard-edged amber pixel stream and a foam burst, for the buff dispense move.
- **Bar-mounted variant (48x64)** — the handle intact on a brass tap tower, for the Publandia tavern tileset — and so the player sees where he stole it from.
- **Battle idle sprite (48x48)** — front-view combat orientation.

## 6. Art-director notes

- The torn brass collar with wrenched threads is the theft made visible. Do not let the generator render a clean detachment.
- Brewery crest stays an abstract blocky pixel shape. No real brewery marks.
- This weapon is the most 'trophy-like' in Bradley's set. Let the woodwork look genuinely nice above the damage — the contrast between the fine handle and the violent tear is the joke.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

