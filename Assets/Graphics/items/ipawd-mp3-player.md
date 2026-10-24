# "iPawd" MP3 Player (Knockoff iPod)

> **Asset slug:** `ipawd-mp3-player`  
> **Type / slot:** Accessory  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Access "Napstur" at hotspots for random stat-boosting tracks.

**Flavor text:** *"Totally legal music sharing platform, 128MB storage."*

**Era Cringe:** Holds exactly 23 songs, buttons stick when sweaty.

**Why it's funny (the thing the art has to sell):** A knockoff MP3 player whose name is one letter off and whose build quality is four generations off. The click wheel is not a click wheel, it is four separate buttons pretending.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A chunky rectangular white plastic MP3 player, thicker than it should be, with a small monochrome blue-green LCD showing three rows of illegible pixel text. Below the screen, four separate square rubber buttons arranged in a diamond, badly imitating a click wheel — the plastic around them is stained yellow-brown from sweat. The word iPAWD is rendered as blocky pixel lettering on a cheap chrome-effect sticker that is peeling at one corner. The white plastic has gone cream with age. A tangled pair of thin white earbuds trails from the top, one bud's foam cover missing. A hairline crack across the screen bezel.

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
#2B1A2E outline / #EDE8DA plastic cream / #C4BEAC plastic shadow / #FBF8F0 plastic highlight / #C9BE8E sweat stain / #9E9268 stain shadow / #6EA894 LCD green / #3A6E5E LCD shadow / #A8D8C8 LCD highlight / #2A2A2E button / #A8AEB4 chrome sticker / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Chunky thick rectangular white plastic MP3 player gone cream with age, small monochrome blue-green LCD with illegible pixel text, four separate square rubber buttons in a diamond badly imitating a click wheel, sweat-stained yellow-brown plastic around them, blocky iPAWD lettering on a peeling chrome sticker, tangled thin white earbuds trailing from the top with one foam cover missing, hairline crack in the screen bezel, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #EDE8DA plastic cream / #C4BEAC plastic shadow / #FBF8F0 plastic highlight / #C9BE8E sweat stain / #9E9268 stain shadow / #6EA894 LCD green / #3A6E5E LCD shadow / #A8D8C8 LCD highlight / #2A2A2E button / #A8AEB4 chrome sticker / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Napstur screen variant (32x32)** — just the LCD, showing a hard-edged pixel download progress bar frozen at 94%.
- **Earbud-only asset** — the tangled earbuds alone, for the tangled-cord gag prop.
- **Equipped variant** — clipped to the fanny pack strap, for the accessory-combo preview.

## 6. Art-director notes

- Four separate buttons, NOT a wheel. That's the counterfeit tell. Say it explicitly every regeneration.
- Cream, not white. The yellowing is the age signal.
- Keep the earbud tangle to 3-4 clean pixel loops — real tangle detail dies at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

