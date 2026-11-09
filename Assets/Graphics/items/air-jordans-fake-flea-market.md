# Air Jordans (Fake, From Flea Market)

> **Asset slug:** `air-jordans-fake-flea-market`  
> **Type / slot:** Footwear  
> **World:** Global  
> **Rarity / tier:** Uncommon  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +2 Basketball Cred, +1 Jump Height, -1 Authenticity.

**Flavor text:** *"Nobody will notice the backwards swoosh."*

**Era Cringe:** Paid $40 thinking he got a 'deal' on $200 shoes.

**Why it's funny (the thing the art has to sell):** Counterfeit basketball shoes where every detail is subtly wrong. He knows. He has decided not to know.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A single high-top basketball sneaker at a three-quarter side angle, in red, black and white — but everything is a few degrees off. The proportions are slightly wrong: the toe box is too round, the ankle collar is too tall and too straight, the midsole is thicker than it should be. The side logo mark is rendered as a blocky pixel swoosh-adjacent shape that is clearly mirrored the wrong way. Stitching is uneven with two visibly crooked seam runs. The leather has a cheap plastic sheen rendered as one over-bright hard highlight band. The tongue label is misaligned and its lettering is illegible pixel noise. Glue residue is visible as a yellowed bead along the midsole join. One eyelet is punched off-center. Laces are the wrong flat width.

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
#2B1A2E outline / #C4241E sneaker red / #7E0F0A red shadow / #E86E62 red highlight / #1A1A1E sneaker black / #3A3A42 black highlight / #F4F1E8 sneaker white / #C4BFB2 white shadow / #FFFFFF cheap sheen / #C9BE8E glue residue / #9E9268 glue shadow / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Single high-top basketball sneaker at a three-quarter side angle in red black and white with subtly wrong proportions — too round toe box, too tall and straight ankle collar, over-thick midsole — a blocky side logo mark clearly mirrored the wrong way, two visibly crooked seam runs, cheap plastic sheen as one over-bright hard highlight band, misaligned tongue label with illegible lettering, yellowed glue residue beading along the midsole join, one off-center eyelet, wrong-width flat laces, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C4241E sneaker red / #7E0F0A red shadow / #E86E62 red highlight / #1A1A1E sneaker black / #3A3A42 black highlight / #F4F1E8 sneaker white / #C4BFB2 white shadow / #FFFFFF cheap sheen / #C9BE8E glue residue / #9E9268 glue shadow / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Pair variant (64x48)** — both shoes, and the two are subtly different from each other, which is the deepest cut.
- **Box variant (48x48)** — a flimsy cardboard shoebox with a misspelled illegible label and one crushed corner.
- **Equipped variant** — on feet below JNCO jeans, only the toes visible.

## 6. Art-director notes

- Every detail should be *almost* right. That's harder than making it obviously fake and it's much funnier. Push 'subtly incorrect proportions, everything slightly off-model.'
- Do not render a real trademark. The logo mark must be a mirrored, distorted, clearly-not-that pixel shape.
- Glue residue and crooked stitching are the two fastest counterfeit tells at 64px. Keep both.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

