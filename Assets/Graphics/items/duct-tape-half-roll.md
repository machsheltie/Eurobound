# Duct Tape (Half Roll)

> **Asset slug:** `duct-tape-half-roll`  
> **Type / slot:** Consumable — Utility  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `items.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Repairs broken equipment or temporarily fixes status ailments.

**Flavor text:** *"The handyman's secret weapon."*

**Why it's funny (the thing the art has to sell):** Half a roll of duct tape, which in this party's hands has been used to repair a shoe, a phone, a pool cue and at least one relationship.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A partially used roll of silver duct tape seen at a three-quarter angle, showing both the flat face and the edge. The cardboard core is visible and crushed slightly out of round. The remaining tape is uneven — the roll is visibly thicker on one side because it was rewound badly. The loose end is torn, not cut, with a ragged fibrous edge and it has folded back and stuck to itself. The silver surface has the characteristic fabric weave rendered as a fine regular crosshatch of 1px darker pixels. Grey lint and hair are stuck along one edge. A little grime on the exposed adhesive.

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
#2B1A2E outline / #A8ACB0 tape silver / #6E7276 silver shadow / #D8DCE0 silver highlight / #7E7276 weave dark / #C49A6E cardboard core / #8E6E4A core shadow / #8E8A82 lint grey / #4A443E grime / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Partially used roll of silver duct tape at a three-quarter angle showing face and edge, crushed out-of-round cardboard core, unevenly rewound so one side is thicker, ragged torn loose end folded back and stuck to itself, fabric weave rendered as a fine 1px crosshatch, grey lint and hair stuck along the edge, grimy exposed adhesive, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8ACB0 tape silver / #6E7276 silver shadow / #D8DCE0 silver highlight / #7E7276 weave dark / #C49A6E cardboard core / #8E6E4A core shadow / #8E8A82 lint grey / #4A443E grime / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Applied-patch overlay (32x32)** — an X of two torn tape strips, for slapping onto broken-equipment icons.
- **Nearly-empty variant** — bare cardboard core with one last strip.
- **Colored variants** — a black roll and a camo roll for the Bradley 'tactical' gag.

## 6. Art-director notes

- The weave crosshatch is what makes it read as duct tape rather than foil at 64px. Do not let it smooth out.
- Torn end, never cut. The raggedness is the character.
- This is the most-used utility sprite in the game — keep it maximally legible and boring in silhouette so it never competes with hero items.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

