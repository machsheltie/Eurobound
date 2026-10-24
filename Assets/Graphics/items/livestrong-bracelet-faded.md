# LiveStrong Bracelet (Faded Yellow)

> **Asset slug:** `livestrong-bracelet-faded`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Stamina, Immune to "Wrist Rash".

**Flavor text:** *"From when being charitable was trendy."*

**Era Cringe:** Still believes Lance Armstrong was innocent.

**Why it's funny (the thing the art has to sell):** A silicone charity wristband from 2004 that has never come off. It has fused to his personality. He has opinions about the doping thing and he will share them.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A silicone wristband lying flat as a slightly squashed oval ring, in a badly faded mustard-yellow that was once bright — with an uneven sun-fade so one arc of the band is noticeably paler, almost cream. The debossed lettering around the band is rendered as recessed illegible blocky pixel glyphs, worn shallow and nearly gone on the paler section. The silicone has gone slightly tacky and has collected a dark grime line along the inner edge and two dark specks embedded in the surface. One section is stretched and misshapen where it was pulled over a hand too many times, and there is a small nick in the edge. A pale hairline stress crack runs partway through.

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
#2B1A2E outline / #D8B02E band yellow / #9E7C14 yellow shadow / #F0D46E yellow highlight / #E8DCA8 band faded / #C4B884 faded shadow / #4A423A grime / #2E2822 grime dark / #B8A05E debossed recess / #F8EEC4 stress crack / #7E7462 embedded speck / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Silicone wristband lying flat as a slightly squashed oval ring in badly faded mustard-yellow with an uneven sun-fade making one arc almost cream, debossed lettering rendered as recessed illegible blocky pixel glyphs worn nearly gone on the pale section, slightly tacky surface with a dark grime line along the inner edge and two embedded dark specks, one stretched misshapen section, a small edge nick and a pale hairline stress crack, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #D8B02E band yellow / #9E7C14 yellow shadow / #F0D46E yellow highlight / #E8DCA8 band faded / #C4B884 faded shadow / #4A423A grime / #2E2822 grime dark / #B8A05E debossed recess / #F8EEC4 stress crack / #7E7462 embedded speck / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — on a wrist alongside the WWJD and Power Balance bracelets, all three at once. That stack is the real item.
- **Bracelet stack lineup (96x32)** — all four bracelets laid in a row for the shop display.
- **Alt colorways** — a pink and a blue band, for the 'he has a cause for every occasion' gag.

## 6. Art-director notes

- Uneven fade is critical — one arc pale, the rest less pale. A uniform faded band looks like a color choice instead of twenty years of sun.
- Lettering stays illegible debossed glyphs. Do not render readable words.
- This is a very simple silhouette. Lean hard on surface storytelling — grime, specks, crack, nick — or it will read as a plain ring at 64px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

