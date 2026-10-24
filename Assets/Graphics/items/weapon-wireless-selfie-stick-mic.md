# Wireless Selfie Stick (Retractable Mic)

> **Asset slug:** `weapon-wireless-selfie-stick-mic`  
> **Type / slot:** Weapon — Chadwick Signature  
> **World:** Global  
> **Rarity / tier:** Signature  
> **Canon source:** `Game Design Spec Sheet / chadwicksweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Chadwick's signature weapon. Support and debuff; charms NPCs, lowers enemy morale, livestreams fights for currency.

**Flavor text:** *"It extends to four feet. He has never once needed four feet."*

**Why it's funny (the thing the art has to sell):** A telescoping selfie stick with a microphone that pops out of the phone cradle. He interviews enemies mid-battle. Nobody has agreed to be interviewed.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A telescoping selfie stick extended to roughly two-thirds of its length, held at a slight diagonal, showing three visible tube sections of decreasing diameter in scuffed matte black aluminum with chrome collar joints. At the top, a spring-loaded phone cradle grips a small dark phone, its screen showing an illegible blocky pixel live-stream interface with a tiny red recording dot. A retractable microphone with a grey foam windscreen extends from a slot in the cradle's base, the foam crumbling and gone yellow-grey at the edges. The grip is textured rubber with a small illegible pixel button panel and a status LED as one blue pixel. One collar joint is slipping so a section sags slightly out of line. A frayed wrist strap dangles.

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
#2B1A2E outline / #1E1E24 matte black / #38383E black mid / #56565E black highlight / #A8AEB4 chrome collar / #6E7478 collar shadow / #E0E6EA collar highlight / #8E8A82 foam grey / #C9BE8E foam yellowed / #2E4E6E phone screen / #7EB4D8 screen text / #E82424 rec dot / #1E7EF0 status LED / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Telescoping selfie stick extended two-thirds and held at a slight diagonal showing three tube sections of decreasing diameter in scuffed matte black aluminum with chrome collar joints, spring-loaded phone cradle at the top gripping a small dark phone whose screen shows an illegible blocky pixel live-stream interface with a tiny red recording dot, a retractable microphone with a crumbling yellow-grey foam windscreen extending from a slot in the cradle base, textured rubber grip with an illegible pixel button panel and one blue LED pixel, one collar joint slipping so a section sags out of line, frayed dangling wrist strap, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #1E1E24 matte black / #38383E black mid / #56565E black highlight / #A8AEB4 chrome collar / #6E7478 collar shadow / #E0E6EA collar highlight / #8E8A82 foam grey / #C9BE8E foam yellowed / #2E4E6E phone screen / #7EB4D8 screen text / #E82424 rec dot / #1E7EF0 status LED / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Fully extended variant (96x64)** — all four sections out, absurdly long, for the reach-attack animation.
- **Livestream FX frame (96x96)** — the stick raised with four hard-edged pixel chat bubbles floating up, each containing illegible pixel text, for the currency-gain move.
- **Battle idle sprite (48x48)** — front-view combat orientation, mic deployed.

## 6. Art-director notes

- The mic emerging from the cradle base is the invention here — it's not a real product feature and it needs to read clearly. Give the mic its own distinct silhouette away from the tube.
- The slipping collar joint is a great small detail: cheap gear, over-used.
- Signature weapon — generate at 256x256 and keep a hi-res master for cutscene and title use.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

