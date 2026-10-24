# Vintage Camcorder (Chain Attached)

> **Asset slug:** `weapon-vintage-camcorder-chain`  
> **Type / slot:** Weapon — Chadwick (Alt)  
> **World:** Global  
> **Rarity / tier:** Rare  
> **Canon source:** `chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Swinging chain attacks; can "record" enemy weaknesses. Gets stronger when enemies are at low health.

**Flavor text:** *"It captured the one moment anyone ever cared about. Now it's a flail."*

**Why it's funny (the thing the art has to sell):** The camcorder that recorded his single viral moment, bolted to a length of chain and swung like a flail. He still has the tape. He will not let you watch it. He will describe it.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A chunky 1990s shoulder-less handheld camcorder swung as a flail head, connected to a heavy nickel chain that loops away and terminates in a taped wooden handle. The camcorder body is silver-grey plastic with a black rubber grip strap, a fat protruding lens barrel with a scratched glass element rendered as two hard highlight bands, and a small flip-out LCD panel hanging open at an angle showing illegible blocky pixel static. A red REC LED as one hard pixel. The tape hatch is open on one side with a cassette half-ejected. The plastic is cracked across one corner with a chunk missing, and the chain is bolted through a crudely drilled hole with a washer and a visible burr. Scuffs and gaffer-tape residue all over the body.

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
#2B1A2E outline / #A8AEB4 body silver / #6E7478 silver shadow / #E0E6EA silver highlight / #1E1E24 rubber black / #38383E black highlight / #2A3E52 lens glass / #7EAECC lens highlight / #3E5E4E LCD static / #A8CEB4 static bright / #E82424 REC LED / #8E9298 chain nickel / #7E5A2E handle wood / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Chunky 1990s handheld camcorder swung as a flail head connected to a heavy nickel chain looping away to a taped wooden handle, silver-grey plastic body with a black rubber grip strap and a fat protruding lens barrel with a scratched glass element in two hard highlight bands, small flip-out LCD panel hanging open at an angle showing illegible blocky pixel static, one hard red REC LED pixel, tape hatch open with a cassette half-ejected, cracked corner with a chunk missing, chain bolted through a crudely drilled hole with a washer and a visible burr, scuffs and gaffer-tape residue, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #A8AEB4 body silver / #6E7478 silver shadow / #E0E6EA silver highlight / #1E1E24 rubber black / #38383E black highlight / #2A3E52 lens glass / #7EAECC lens highlight / #3E5E4E LCD static / #A8CEB4 static bright / #E82424 REC LED / #8E9298 chain nickel / #7E5A2E handle wood / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Record FX frame (96x96)** — the LCD showing an enemy silhouette in a hard-edged pixel viewfinder frame with corner brackets, for the weakness-scan move.
- **Swing FX frame (96x96)** — the camcorder mid-arc with the chain extended and five hard-edged pixel motion dashes trailing.
- **Cassette prop (32x32)** — the half-ejected VHS-C tape as a standalone quest item with a hand-written illegible pixel label.

## 6. Art-director notes

- Chunky 1990s proportions — fat lens barrel, thick body, small screen. These generators drift modern; specify the era hard.
- The crudely drilled chain mount with a burr is the 'he did this himself with a power drill' detail. Do not let it render as a factory fitting.
- The cassette prop is worth building separately — it's a natural quest item and a bulletin-board gag.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

