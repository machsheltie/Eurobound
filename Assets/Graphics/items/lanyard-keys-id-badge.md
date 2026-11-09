# Lanyard (Keys + ID Badge)

> **Asset slug:** `lanyard-keys-id-badge`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Organization, +2 Office Drone Energy.

**Flavor text:** *"Jingles with the weight of corporate servitude."*

**Era Cringe:** Worn around neck like a badge of suburban surrender.

**Why it's funny (the thing the art has to sell):** He is on vacation in another country and he is still wearing his office lanyard. The badge is from a job he may or may not still have.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A flat woven polyester lanyard in navy blue with a repeating illegible pixel-noise company logo along its length, hanging in a loose U with a plastic breakaway clasp at the back of the neck. At the bottom, a metal split ring carries a laminated ID badge in a scratched clear plastic sleeve — the badge shows a tiny blocky portrait of a tired middle-aged man and unreadable pixel text. Four keys of different sizes hang alongside, one of them a chunky car key with a worn rubber head. A supermarket loyalty fob. The lanyard fabric is grubby along the neck section and frayed at one edge. The badge sleeve is cloudy with wear.

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
#2B1A2E outline / #1E3A6E lanyard navy / #12224A navy shadow / #4A6EA8 navy highlight / #8E8478 grubby fabric / #A8AEB4 key metal / #6E7278 metal shadow / #E0E6EA metal highlight / #D8D4C8 badge sleeve / #C4A88E badge portrait / #2A2A2E clasp black / #C42A16 loyalty fob / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Flat woven navy polyester lanyard with a repeating illegible pixel-noise logo hanging in a loose U with a plastic breakaway clasp, metal split ring at the bottom carrying a laminated ID badge in a scratched cloudy plastic sleeve showing a tiny blocky portrait of a tired middle-aged man, four keys of different sizes including a chunky worn rubber-headed car key, a supermarket loyalty fob, grubby frayed fabric along the neck section, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E3A6E lanyard navy / #12224A navy shadow / #4A6EA8 navy highlight / #8E8478 grubby fabric / #A8AEB4 key metal / #6E7278 metal shadow / #E0E6EA metal highlight / #D8D4C8 badge sleeve / #C4A88E badge portrait / #2A2A2E clasp black / #C42A16 loyalty fob / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (48x48)** — around a neck silhouette, badge resting mid-chest, for the equip preview.
- **Badge close-up (32x32)** — the ID alone, to reuse for the 'he still works there?' ICQ gag.
- **Key-cluster asset** — the keys and fob alone, for the jingle SFX trigger prop.

## 6. Art-director notes

- The badge portrait should be the same tired face used on `fake-id-laminated-at-kinkos.md` — same man, different document. Cross-reference it.
- Keys should be four clearly different silhouettes so the cluster reads at small size.
- Navy is a deliberately dead color here — it should be the least interesting thing in the accessory shelf lineup, which is the joke.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

