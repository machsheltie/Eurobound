# Dog Tag Chain (Not Military)

> **Asset slug:** `dog-tag-chain-not-military`  
> **Type / slot:** Necklace  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Toughness, +1 Stolen Valor.

**Flavor text:** *"Engraved with fraternity letters and blood type."*

**Era Cringe:** Worn over the shirt for maximum visibility.

**Why it's funny (the thing the art has to sell):** Dog tags he had made at a mall kiosk, engraved with Greek letters and a blood type he does not actually know. He has never served. He lets people assume.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
Two stamped metal dog tags on a ball chain, laid flat and overlapping, one slightly rotated. Dull nickel-grey stainless with a rolled edge, one tag fitted with a black silicone silencer ring that has cracked and gone chalky. The engraving is rendered as recessed illegible pixel lines in four short rows — three Greek-letter-shaped blocky glyphs on the top line, then shorter rows below. The ball chain is a repeating string of 2px spheres, kinked and with one section clearly replaced by a mismatched brighter length. Both tags are scratched with a hard crosshatch and one corner is bent. A dark grime line where the tags rub together.

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
#2B1A2E outline / #9EA4AA nickel / #6A7076 nickel shadow / #D4DADE nickel highlight / #4E5458 nickel dark / #2A2A2E silencer black / #56565E silencer cracked / #C4C8CC chain bright / #7E8288 chain shadow / #4A443E grime / #8E8A82 scratch / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Two stamped dull nickel-grey stainless dog tags on a ball chain laid flat and overlapping with one slightly rotated, rolled edges, one tag fitted with a cracked chalky black silicone silencer ring, engraving rendered as recessed illegible pixel lines in four short rows with three blocky Greek-letter-shaped glyphs on the top line, ball chain as a repeating string of 2px spheres kinked with one mismatched brighter replacement section, hard crosshatch scratching, one bent corner, dark grime line where the tags rub, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #9EA4AA nickel / #6A7076 nickel shadow / #D4DADE nickel highlight / #4E5458 nickel dark / #2A2A2E silencer black / #56565E silencer cracked / #C4C8CC chain bright / #7E8288 chain shadow / #4A443E grime / #8E8A82 scratch / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn-over-shirt variant (48x48)** — tags on top of a polo, cross-referencing `polo-shirt-collar-popped.md`. Over the shirt is the whole gag.
- **Single-tag close-up (32x32)** — engraving visible, for the Stolen Valor tooltip.
- **Kiosk variant** — the tags still on their cardboard backing card.

## 6. Art-director notes

- Engraving stays illegible. Greek-letter-shaped glyphs are fine as abstract pixel forms; do not spell anything real.
- The mismatched chain section says 'this broke and he cheaped out on the repair.' Small detail, big payload.
- Over-the-shirt is the equipped-variant joke. Prioritize that render.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

