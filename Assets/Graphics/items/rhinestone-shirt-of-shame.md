# Rhinestone Shirt of Shame (Bedazzled)

> **Asset slug:** `rhinestone-shirt-of-shame`  
> **Type / slot:** Torso — Regional  
> **World:** Debaucheryville  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +4 Attention Seeking, +1 Disco Ball Effect, -3 Taste.

**Flavor text:** *"Blinds enemies and bystanders with its gaudy magnificence."*

**Era Cringe:** Each rhinestone tells a story of questionable life choices.

**Why it's funny (the thing the art has to sell):** A black button-down encrusted with rhinestones in a design nobody can identify, half of which have fallen off leaving bald glue spots. It catches every light in the club and he thinks that's the shirt working.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A slim-fit black button-down shirt hanging flat on an invisible form, front view, with the top three buttons undone and the collar splayed wide. The fabric is a slick black with a slight sheen rendered as two hard highlight bands. Across the chest and one shoulder, an elaborate swirling rhinestone design rendered as clusters of individual 1x1 and 2x2 hard-edged pixels in silver-white, cyan and magenta — each with a single brighter center pixel, arranged in a pattern too chaotic to identify. Roughly a third of the stones are missing, leaving small pale yellowed glue dots in their place, clearly visible as a scatter of bare spots. The cuffs are unbuttoned and flapping. One collar point curls up. A dark sweat patch under one arm.

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
#2B1A2E outline / #16161A shirt black / #2E2E36 black mid / #4A4A56 black sheen / #F4F8FA rhinestone white / #C4CAD4 stone shadow / #3EC6D8 rhinestone cyan / #D83EC0 rhinestone magenta / #FFFFFF stone center / #C9BE8E glue dot / #9E9268 glue shadow / #3E3A44 sweat patch / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Slim-fit slick black button-down shirt hanging flat on an invisible form with the top three buttons undone and the collar splayed wide, two hard sheen highlight bands, an elaborate swirling rhinestone design across the chest and one shoulder rendered as clusters of individual 1x1 and 2x2 hard-edged silver-white cyan and magenta pixels each with a brighter center pixel in a pattern too chaotic to identify, roughly a third of the stones missing leaving pale yellowed glue dots as a scatter of bare spots, unbuttoned flapping cuffs, one curled collar point, dark sweat patch under one arm, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #16161A shirt black / #2E2E36 black mid / #4A4A56 black sheen / #F4F8FA rhinestone white / #C4CAD4 stone shadow / #3EC6D8 rhinestone cyan / #D83EC0 rhinestone magenta / #FFFFFF stone center / #C9BE8E glue dot / #9E9268 glue shadow / #3E3A44 sweat patch / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Disco Ball Effect FX frame (96x96)** — the shirt with eight hard-edged radiating pixel light spokes in cyan and magenta, for the +1 Disco Ball Effect proc.
- **Equipped variant (48x64)** — on a torso silhouette, unbuttoned to reveal chest, stones catching the light.
- **Under-club-lighting variant** — the same shirt with the palette shifted to magenta and cyan dominance, for the Velvet Curtain Club scene.

## 6. Art-director notes

- Missing stones and bare glue dots are what elevate this from 'flashy shirt' to a joke. Make roughly a third bare and scatter them irregularly.
- Each rhinestone is 1-2px with one brighter center pixel. Do not attempt sparkle rays on individual stones at this scale — save that for the FX frame.
- The chaotic unidentifiable pattern is deliberate. If the generator produces a coherent motif, ask for 'abstract, chaotic, no recognizable shape.'

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

