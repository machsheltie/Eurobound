# Invicta Watch (Oversized Face)

> **Asset slug:** `invicta-watch-oversized`  
> **Type / slot:** Watch / Bracelet  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Time Awareness, +2 Wrist Strain.

**Flavor text:** *"Tells time in 47 time zones you'll never visit."*

**Era Cringe:** Face is larger than most dinner plates.

**Why it's funny (the thing the art has to sell):** An enormous chronograph with more subdials than any human needs, worn by a man who has never used a single complication and cannot set two of them.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
An absurdly oversized chronograph wristwatch seen face-on, the case comically larger than the bracelet that carries it so the proportions look structurally wrong. Heavy polished gold-tone and steel two-tone bracelet with chunky links. The dial is crowded past the point of legibility: three subdials, a date window, a tachymeter bezel with illegible pixel numerals, four hands, and a rotating inner ring — all rendered as dense blocky pixel detail. The crystal is domed and thick with two hard highlight bands. One subdial hand is visibly stuck at an angle that means nothing. The gold plating has worn to grey on the bracelet's outer link edges. A screw-down crown guard on the side is oversized. Deep scratches across the caseback edge.

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
#2B1A2E outline / #C9A227 gold tone / #8A6E14 gold shadow / #F0D874 gold highlight / #A8AEB4 steel / #6E7478 steel shadow / #E0E6EA steel highlight / #1A1E28 dial dark / #3A424E dial mid / #6E7A88 subdial / #8E8A82 worn plating / #F4F8FA crystal spec / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Absurdly oversized chronograph wristwatch face-on with the case comically larger than the chunky two-tone gold and steel link bracelet so the proportions look structurally wrong, dial crowded past legibility with three subdials a date window a tachymeter bezel of illegible pixel numerals four hands and a rotating inner ring all in dense blocky pixel detail, thick domed crystal with two hard highlight bands, one subdial hand stuck at a meaningless angle, gold plating worn to grey on the outer link edges, oversized crown guard, deep caseback scratches, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C9A227 gold tone / #8A6E14 gold shadow / #F0D874 gold highlight / #A8AEB4 steel / #6E7478 steel shadow / #E0E6EA steel highlight / #1A1E28 dial dark / #3A424E dial mid / #6E7A88 subdial / #8E8A82 worn plating / #F4F8FA crystal spec / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — on a wrist where the case is visibly wider than the forearm. Generate this; the proportion gag is the item.
- **Side-profile variant** — showing the absurd case thickness.
- **Alt colorways** — all-gold and a truly regrettable blue-dial version.

## 6. Art-director notes

- Oversize past plausibility. The case should look like it would leave a mark. If it looks wearable, scale it up.
- Dial clutter is intentional — it should be unreadable, which is the point. Dense pixel noise beats legible detail here.
- Two-tone gold and steel is the specific 2000s mall-jeweler signal. Do not simplify to one metal.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

