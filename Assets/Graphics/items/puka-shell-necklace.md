# Puka Shell Necklace (Authentic Fake)

> **Asset slug:** `puka-shell-necklace`  
> **Type / slot:** Necklace  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +5 Charisma, -5 Perception.

**Flavor text:** *"Too distracted by your own reflection to notice anything else."*

**Era Cringe:** Bought at a gas station in landlocked Ohio.

**Why it's funny (the thing the art has to sell):** Fake shells, molded plastic, bought inland. +5 Charisma and -5 Perception is the most accurate stat line in the game.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A puka shell necklace laid in a loose open circle, made of small flat off-white disc beads with holes through the center — but they are clearly injection-molded plastic rather than shell: too uniform, too regular, each disc identical with a visible mold seam line and a faint sprue nub. Rendered as a ring of 3x3 pixel discs with a hard highlight pixel each. The cord is a thin waxed black nylon with a cheap barrel screw clasp in tarnished gold. Two of the discs have gone yellow-cream from skin oil. The cord is fraying at one bead hole. A price sticker residue patch clouds one disc.

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
#2B1A2E outline / #EDE8D8 shell white / #C0BAA6 shell shadow / #FBF8F0 shell highlight / #C9BE8E shell yellowed / #9E9268 yellowed shadow / #1A1A1E cord black / #3A3A42 cord highlight / #A88E3E clasp gold tarnish / #7E6822 clasp shadow / #D8D4C8 sticker residue / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Puka shell necklace laid in a loose open circle made of small flat off-white disc beads with center holes, clearly injection-molded plastic rather than shell — too uniform and identical with visible mold seam lines and faint sprue nubs, rendered as a ring of 3x3 pixel discs each with one hard highlight pixel, thin waxed black nylon cord with a tarnished gold barrel screw clasp, two discs gone yellow-cream from skin oil, cord fraying at one bead hole, clouded price sticker residue on one disc, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE8D8 shell white / #C0BAA6 shell shadow / #FBF8F0 shell highlight / #C9BE8E shell yellowed / #9E9268 yellowed shadow / #1A1A1E cord black / #3A3A42 cord highlight / #A88E3E clasp gold tarnish / #7E6822 clasp shadow / #D8D4C8 sticker residue / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — around a neck silhouette, sitting high and tight at the throat.
- **Broken variant** — cord snapped, discs scattering, for the bar-fight damaged-gear state.
- **Necklace shelf lineup (96x64)** — this plus the sharktooth, mood and dog-tag necklaces on a rotating rack, for the shop display.

## 6. Art-director notes

- Uniformity is the counterfeit tell. Real puka shells are irregular; these must be identical. Say 'perfectly identical machine-made discs, unnaturally regular.'
- The two yellowed discs break that uniformity in the right way — skin-oil aging, not variation.
- Keep the circle open and flat-laid. A dangling necklace loses its silhouette at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

