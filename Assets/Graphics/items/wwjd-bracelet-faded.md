# WWJD Bracelet (Faded Text)

> **Asset slug:** `wwjd-bracelet-faded`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Common  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +1 Moral Guidance, +1 Virtue Signaling.

**Flavor text:** *"What Would Jesus Do? Probably not this."*

**Era Cringe:** Worn by someone who hasn't been to church since confirmation.

**Why it's funny (the thing the art has to sell):** The bracelet asks a question he has not considered since 1998 and is not going to consider tonight either. The satire target is his hypocrisy, not anyone's faith — keep the object itself dignified and let him be the joke.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A woven fabric friendship-style bracelet lying flat as a loose oval, in a faded purple-and-white braided pattern with the weave rendered as a regular diagonal 1px chevron texture. Four woven letter blocks around the band are so faded and fuzzed with wear that they read only as pale illegible pixel shapes. The fabric is grimy grey along the underside, and one edge has unraveled into three loose threads. A small metal slide clasp is tarnished and stiff, with one prong bent. The braid has gone slack and flattened where it sits against the wrist. A dark permanent water stain across one section.

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
#2B1A2E outline / #6E4E96 braid purple / #42285E purple shadow / #A47ED8 purple highlight / #EDE8DA braid white / #C0BAA8 white shadow / #8E8A7E grimy grey / #5E5A50 grime dark / #A88E3E clasp tarnish / #7E6822 clasp shadow / #B0A896 loose thread / #4E4238 water stain / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Woven fabric friendship-style bracelet lying flat as a loose oval in a faded purple and white braided pattern with a regular diagonal 1px chevron weave texture, four woven letter blocks so faded and fuzzed they read only as pale illegible pixel shapes, grimy grey underside, one edge unraveled into three loose threads, tarnished stiff metal slide clasp with a bent prong, braid gone slack and flattened, dark permanent water stain across one section, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #6E4E96 braid purple / #42285E purple shadow / #A47ED8 purple highlight / #EDE8DA braid white / #C0BAA8 white shadow / #8E8A7E grimy grey / #5E5A50 grime dark / #A88E3E clasp tarnish / #7E6822 clasp shadow / #B0A896 loose thread / #4E4238 water stain / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — third band on the wrist stack with LiveStrong and Power Balance.
- **Fresh variant** — bright purple, crisp letters, for a flashback or the shop display.
- **Bracelet stack lineup (96x32)** — all four bracelets in a row.

## 6. Art-director notes

- The letters must be illegible. That's both a satire choice — the message has worn away — and it keeps the object from reading as a specific real product.
- Render the object itself with care and dignity. The joke is the man wearing it, and the art should not sneer at the thing.
- Faded purple against grubby grey is a low-contrast sprite. Push the white braid brighter so it separates at 32px.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

