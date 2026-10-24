# Chain Wallet (3-foot chain)

> **Asset slug:** `chain-wallet-3-foot-chain`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** -10% theft chance, +10 Weight.

**Flavor text:** *"Chain long enough to trip over while walking."*

**Era Cringe:** Makes jingling sounds that announce your arrival.

**Why it's funny (the thing the art has to sell):** The chain is absurdly, unnecessarily long. It is longer than the wallet is valuable. He has tripped on it in three countries.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A fat black leather trifold wallet, bulging and unable to close flat, with a heavy nickel chain attached to a belt loop clip. The chain is comically long — render it looped in three or four generous coils spilling down and pooling beside the wallet, each link a distinct hard-edged pixel oval. The leather is cracked and pale grey along the fold line, with a worn white circle where a can lid has permanently pressed into the back. Frayed stitching along one edge. A card corner and a folded receipt stick out of the top. The clip is scratched down to raw metal.

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
#2B1A2E outline / #1E1A1C leather black / #3A3234 leather mid / #6E6264 leather cracked / #A8AEB4 chain nickel / #6E7278 chain shadow / #E0E6EA chain highlight / #E8E2D2 receipt / #C4BFAE receipt shadow / #C9A227 card corner / #8E8A82 raw metal / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Fat bulging black leather trifold wallet that will not close flat, heavy nickel chain with distinct hard-edged pixel links looped in three or four generous coils pooling beside it, cracked pale grey leather along the fold, worn white can-lid ring pressed into the back, frayed stitching, a card corner and folded receipt sticking out, scratched raw-metal clip, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1A1C leather black / #3A3234 leather mid / #6E6264 leather cracked / #A8AEB4 chain nickel / #6E7278 chain shadow / #E0E6EA chain highlight / #E8E2D2 receipt / #C4BFAE receipt shadow / #C9A227 card corner / #8E8A82 raw metal / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Equipped variant (32x32)** — wallet in a back pocket with the chain arcing to a belt loop, for the character equip preview.
- **Open variant** — trifold spread showing three $1 bills and a video rental card, to visually rhyme with `money-clip-empty.md`.
- **Chain-only asset** — a tileable length of chain for reuse on other accessory sprites.

## 6. Art-director notes

- Chain length is the joke — make it excessive to the point of absurdity. If the coils look reasonable, add more.
- Every link should be individually readable at 64px. If they merge into a rope, add 'chain links clearly separated, each link a distinct visible oval.'
- Bulge matters. This wallet should look structurally incapable of closing.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

