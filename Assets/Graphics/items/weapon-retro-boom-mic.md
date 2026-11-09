# Retro Boom Mic (Telescoping)

> **Asset slug:** `weapon-retro-boom-mic`  
> **Type / slot:** Weapon — Chadwick (Alt)  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Extending spear attacks, sound-based abilities, feedback screeches.

**Flavor text:** *"Professional equipment, purchased before the question of whether he could use it came up."*

**Why it's funny (the thing the art has to sell):** A full boom pole with a shotgun mic in a dead-cat windshield. He bought the whole kit. He has never recorded usable audio. He uses it as a spear.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A long telescoping boom pole held at a diagonal, showing four tube sections of decreasing diameter in brushed aluminum with black rubber collar locks, one collar visibly slipping. At the tip, a shotgun microphone hangs in a black elastic shock-mount cradle — the elastic bands are slack and one has snapped, so the mic hangs crooked. The mic wears a grey furry windshield with the fur rendered as an irregular 1px fringe breaking the silhouette, matted and patchy with two bald spots. A coiled XLR cable spirals down the pole and terminates in a bent three-pin connector. The pole's foam grip is compressed and split, with gaffer tape over the split. Scratches and one shallow bend in the second section.

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
#2B1A2E outline / #A8AEB4 aluminum / #6E7478 aluminum shadow / #E0E6EA aluminum highlight / #1E1E24 rubber black / #38383E black highlight / #8E8A82 windshield fur / #5E5A52 fur shadow / #C4C0B8 fur highlight / #4A4A52 foam grip / #3A3A44 gaffer tape / #C9A227 connector pin / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Long telescoping boom pole at a diagonal with four brushed-aluminum tube sections of decreasing diameter and black rubber collar locks with one visibly slipping, a shotgun microphone hanging crooked at the tip in a black elastic shock-mount cradle with slack bands and one snapped, grey furry windshield rendered as an irregular 1px fringe breaking the silhouette and matted patchy with two bald spots, coiled XLR cable spiraling down the pole ending in a bent three-pin connector, compressed split foam grip patched with gaffer tape, scratches and a shallow bend in the second section, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8AEB4 aluminum / #6E7478 aluminum shadow / #E0E6EA aluminum highlight / #1E1E24 rubber black / #38383E black highlight / #8E8A82 windshield fur / #5E5A52 fur shadow / #C4C0B8 fur highlight / #4A4A52 foam grip / #3A3A44 gaffer tape / #C9A227 connector pin / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Feedback screech FX frame (96x64)** — the mic tip with six hard-edged concentric pixel arcs and four jagged pixel spikes, for the sound attack.
- **Collapsed variant (48x48)** — the pole fully retracted, for the inventory icon.
- **Battle idle sprite (48x48)** — front-view combat orientation, pole angled as a spear.

## 6. Art-director notes

- The furry windshield's irregular fringe is the one place in the whole item set where a ragged silhouette is correct. Lean into it.
- Crooked mic from the snapped shock-mount band is the 'nothing he owns works properly' beat. Keep the tilt obvious.
- Distinguish from the light stand and tripod leg by the fur and the XLR coil — at 32px those are the only cues.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

