# Power Balance Bracelet (Hologram Missing)

> **Asset slug:** `power-balance-bracelet`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Placebo Effect, +2 Gullibility.

**Flavor text:** *"For optimal energy flow and chakra alignment."*

**Era Cringe:** Still believes it improves athletic performance.

**Why it's funny (the thing the art has to sell):** The hologram — the only part with any claimed function — has fallen off. He still says it works. He will demonstrate a balance test on you.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A black silicone sport bracelet lying flat as a slightly squashed oval ring, matte with a fine 1px stipple texture. On the front there are two circular recessed wells where holograms should sit — one still holds a scratched, clouded silver disc reduced to two dull cyan-magenta pixels, and the other is completely empty, showing a ring of yellowed dried adhesive and a bare recess. The silicone edge is nicked in three places and the band is stretched out of round. A dark grime line runs along the inner surface. Faint debossed illegible pixel lettering around the outside, half worn away. One small tear beginning at the edge of the empty well.

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
#2B1A2E outline / #1E1E22 silicone black / #34343A silicone mid / #4E4E58 silicone highlight / #8E9298 hologram silver / #5E6268 silver shadow / #3EC6D8 holo cyan / #D83EC0 holo magenta / #C9BE8E dried adhesive / #9E9268 adhesive shadow / #4A443E grime / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Matte black silicone sport bracelet lying flat as a slightly squashed oval ring with a fine 1px stipple, two circular recessed wells on the front where holograms should sit — one holding a scratched clouded silver disc reduced to two dull cyan-magenta pixels and the other completely empty showing a ring of yellowed dried adhesive and a bare recess, three nicks in the edge, stretched out of round, dark grime line along the inner surface, half-worn debossed illegible lettering, a small tear starting at the empty well, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1E22 silicone black / #34343A silicone mid / #4E4E58 silicone highlight / #8E9298 hologram silver / #5E6268 silver shadow / #3EC6D8 holo cyan / #D83EC0 holo magenta / #C9BE8E dried adhesive / #9E9268 adhesive shadow / #4A443E grime / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Balance-test FX frame (64x64)** — the bracelet with four radiating hard-edged pixel 'energy' arcs that are obviously doing nothing.
- **Worn variant (32x32)** — stacked on a wrist with the LiveStrong and WWJD bands.
- **Both-holograms-present variant** — for the shop display, so the player can see what he paid for.

## 6. Art-director notes

- The empty well is the entire item. Make the bare recess and adhesive ring unmistakable at 64px.
- Matte black with stipple, never glossy. These generators want to make silicone shiny — fight it.
- Two dull holo pixels only on the surviving disc. Any real iridescence and the joke that it doesn't work stops landing.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

