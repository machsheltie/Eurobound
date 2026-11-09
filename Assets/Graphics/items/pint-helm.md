# Pint Helm (Foam Still Fresh)

> **Asset slug:** `pint-helm`  
> **Type / slot:** Head Gear — Regional  
> **World:** Publandia  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Drinking Stamina, +2 Pub Cred, -1 Dignity.

**Flavor text:** *"A genuine beer mug worn as protective headgear."*

**Era Cringe:** Foam drips down your face during serious conversations.

**Why it's funny (the thing the art has to sell):** A full dimpled pint mug, inverted and worn as a helmet, still containing beer. Physics is not consulted. The foam runs down his face during a conversation about his divorce.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A heavy dimpled glass beer mug inverted so the handle points sideways and the base sits on top like a crown, worn as a helmet. The glass is thick and amber-tinted with a regular grid of hard-edged raised dimples rendered as 3x3 pixel bosses each with one highlight pixel. Beer is visibly still inside despite the inversion, sitting in an impossible flat plane, with a thick cream foam head packed against what is now the bottom rim and three foam gobs already running down the outside as hard-edged pale drips. A soggy cardboard beer mat has been jammed inside the rim as makeshift padding. The heavy handle sticks out to one side like a mismatched ear guard. Faint scratches and a chip on the base.

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
#2B1A2E outline / #C98E2E beer amber / #96641A amber shadow / #E8B85E amber highlight / #C4D0D4 glass / #8E9EA4 glass shadow / #F0F8FA glass highlight / #EDE4C8 foam cream / #C0B69A foam shadow / #FBF6E8 foam highlight / #A89478 beer mat / #7E6E52 mat shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Heavy dimpled amber glass beer mug inverted and worn as a helmet with the base on top like a crown and the handle jutting sideways like an ear guard, regular grid of hard-edged raised dimples as 3x3 pixel bosses each with a highlight, beer still visibly inside sitting in an impossible flat plane with thick cream foam packed against the lower rim and three hard-edged pale foam drips running down the outside, soggy cardboard beer mat jammed inside the rim as padding, scratched chipped base, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C98E2E beer amber / #96641A amber shadow / #E8B85E amber highlight / #C4D0D4 glass / #8E9EA4 glass shadow / #F0F8FA glass highlight / #EDE4C8 foam cream / #C0B69A foam shadow / #FBF6E8 foam highlight / #A89478 beer mat / #7E6E52 mat shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — on a head silhouette, foam running down the face in three hard-edged drips. This is the item. Generate it.
- **Empty variant** — no beer, no foam, just a glass helmet, for the depleted state.
- **Publandia shop display (48x48)** — the mug right-way-up on a bar towel, so the player can see it's a normal pint before he ruins it.

## 6. Art-director notes

- Beer sitting flat inside an inverted mug is physically wrong and that's deliberate. EarthBound would absolutely draw it this way. Do not let the generator 'fix' it.
- Dimple grid is the recognition cue for a Publandia mug. Keep the bosses chunky enough to survive 32px.
- The foam drips on the worn variant should extend past the helmet's outline — that's the silhouette signature.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

