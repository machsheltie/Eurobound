# Spinner Ring (Anxiety Fidget)

> **Asset slug:** `spinner-ring-anxiety-fidget`  
> **Type / slot:** Ring  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Focus, +2 Nervous Energy.

**Flavor text:** *"Spins constantly during awkward conversations."*

**Era Cringe:** Makes clicking sounds that annoy everyone within 10 feet.

**Why it's funny (the thing the art has to sell):** He spins it constantly. It clicks. Everyone at the table has noticed. Nobody has said anything, which he reads as everyone being fine with it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A wide stainless steel spinner ring at a three-quarter angle, showing the outer spinning band riding on the fixed inner band. The outer band is engraved with a repeating illegible geometric pixel pattern and is captured mid-spin: render motion as a hard-edged 1px lighter ghost band offset around the circumference, blocky, plus three short hard motion dashes trailing at the edge — never blur. The outer band is worn to a mirror sheen on its high points while the recessed pattern is packed with dark grime. There is a visible gap and wobble where the spinner has worn loose. The inner band is scratched dull. Two tiny metal shavings sit beside the ring.

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
#2B1A2E outline / #A8AEB4 steel / #6E7478 steel shadow / #E0E6EA steel highlight / #4E5458 steel dark / #C8CED4 ghost band / #3A342E grime / #24201C grime dark / #8E9298 scratch dull / #F4F8FA mirror sheen / #7E8288 shaving / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Wide stainless steel spinner ring at a three-quarter angle showing the outer spinning band riding on a fixed inner band, outer band engraved with a repeating illegible geometric pixel pattern and captured mid-spin with a hard-edged 1px lighter ghost band offset around the circumference and three short hard motion dashes, high points worn to mirror sheen with dark grime packed in the recesses, visible gap and wobble where the spinner has worn loose, dull scratched inner band, two tiny metal shavings beside it, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8AEB4 steel / #6E7478 steel shadow / #E0E6EA steel highlight / #4E5458 steel dark / #C8CED4 ghost band / #3A342E grime / #24201C grime dark / #8E9298 scratch dull / #F4F8FA mirror sheen / #7E8288 shaving / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Static variant** — no motion ghost, for the inventory icon where the spin would read as a rendering error.
- **Nervous Energy status icon (24x24)** — just the ring with four radiating jitter pixels.
- **Worn variant** — on a finger, thumb poised to flick it.

## 6. Art-director notes

- Two versions matter here: the static one for inventory legibility, the spinning one for the buff icon. Generate both, always.
- Motion ghost must be a hard offset copy in a lighter tone. If it comes back as blur, regenerate with 'motion shown as a hard-edged solid-color duplicate offset, absolutely no blur or transparency.'
- Worn-loose wobble gap is the detail that says 'he does this thousands of times a day.'

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

