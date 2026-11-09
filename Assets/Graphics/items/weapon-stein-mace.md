# Stein Mace (Lord Pilsner Signature)

> **Asset slug:** `weapon-stein-mace`  
> **Type / slot:** Weapon — Lord Pilsner  
> **World:** Global  
> **Rarity / tier:** Signature  
> **Canon source:** `Game Design Spec Sheet / lordpilsnersweapons.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** Lord Pilsner's signature weapon. Balanced physical damage; doubles as a drinking vessel in cutscenes.

**Flavor text:** *"It holds a liter. That is not a design compromise, that is the feature."*

**Why it's funny (the thing the art has to sell):** A ceremonial beer stein welded onto a mace haft. He drinks from it between swings without wiping it off. The lid still works, which he considers the mark of real craftsmanship.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A medieval-style mace where the head is a full ceramic beer stein mounted sideways on a short oak haft. The stein is grey salt-glazed stoneware with a cobalt-blue painted band and raised relief figures rendered as blocky illegible pixel shapes, and it has a hinged pewter lid with a thumb lever, currently flipped open. Beer sloshes visibly inside and a hard-edged foam gob is escaping the open lid. Four stubby iron flanges are bolted around the stein's base like mace spikes, crudely welded with visible slag beads. The oak haft is wrapped in fraying leather cord with a worn brass ferrule. Two chips in the ceramic and one long hairline crack sealed with a bead of glue.

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
#2B1A2E outline / #C4C0B4 stoneware grey / #908C80 stoneware shadow / #E8E4D8 stoneware highlight / #1E3A8E cobalt band / #10225E cobalt shadow / #8E9298 pewter lid / #5E6268 pewter shadow / #C98E2E beer amber / #EDE4C8 foam / #7E5A2E oak haft / #4E3418 haft shadow / #C9A227 brass ferrule / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Medieval mace with a full grey salt-glazed ceramic beer stein as its head mounted sideways on a short oak haft, cobalt-blue painted band and blocky illegible relief figures, hinged pewter lid with a thumb lever flipped open with beer sloshing inside and a hard-edged foam gob escaping, four stubby iron flanges crudely welded around the stein base like mace spikes with visible slag beads, fraying leather cord wrap on the haft with a worn brass ferrule, two ceramic chips and a hairline crack sealed with glue, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #C4C0B4 stoneware grey / #908C80 stoneware shadow / #E8E4D8 stoneware highlight / #1E3A8E cobalt band / #10225E cobalt shadow / #8E9298 pewter lid / #5E6268 pewter shadow / #C98E2E beer amber / #EDE4C8 foam / #7E5A2E oak haft / #4E3418 haft shadow / #C9A227 brass ferrule / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Drinking-pose cutscene frame (64x64)** — the mace tipped mouth-down as a mug, foam running down the haft.
- **SMAAAASH crit FX frame (96x96)** — the stein head at impact, ceramic chips flying as six hard-edged pixel shards, beer spraying in a hard-edged arc.
- **Battle idle sprite (48x48)** — front-view battle orientation, head raised, for the EarthBound-style front-view combat frame.

## 6. Art-director notes

- Sideways stein mounting is what makes this read as a mace and not a mug on a stick. Keep the stein's axis perpendicular to the haft.
- Crude welds with slag beads are the 'he made this himself' tell. Do not let the generator render clean machined joints.
- This is Lord Pilsner's signature — it appears in cutscenes, battle frames and the title screen. Generate it at 256x256 and keep a high-res master.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

