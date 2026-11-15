# Velvet Wristband (VIP Access)

> **Asset slug:** `velvet-wristband-vip`  
> **Type / slot:** Accessory — Regional  
> **World:** Debaucheryville  
> **Rarity / tier:** Rare  
> **Canon source:** `equipment.md`  
> **Deliverable:** 64x64 transparent PNG item icon + 128x128 master

---

## 1. What this thing is

**Effect:** +3 Club Entry, +2 Bottle Service, +1 Fake Importance.

**Flavor text:** *"Grants access to 'exclusive' areas that aren't actually exclusive."*

**Era Cringe:** Worn even to breakfast to show last night's 'achievements'.

**Why it's funny (the thing the art has to sell):** He paid extra for this. Everyone in the club has one. He has worn it for four days and it now smells. He will not cut it off because then he would be a man without a wristband.

---

## 2. PROMPT A — Gemini Pro

```text
You are a veteran SNES-era pixel artist doing item icons for a satirical
turn-based RPG. Work in the exact visual language of EarthBound (MOTHER 2).

DRAW THIS OBJECT:
A cloth event wristband lying flat as a flattened loop, in deep crushed-velvet burgundy with a sheen rendered as two hard highlight bands running along its length. A gold foil VIP mark is printed on it as a small blocky illegible pixel shape, half rubbed away. The plastic snap closure is a one-way barbed clasp, clearly not removable without cutting, with the tail end trimmed unevenly by hand. The band is grubby and darkened along one section from four days of wear, with a small dark stain and a frayed edge where the velvet nap has worn through to the woven backing. A faint sticky residue sheen near the clasp. The loop is permanently creased flat.

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
#2B1A2E outline / #7E1E3E velvet burgundy / #4A0E22 burgundy shadow / #B44E6E burgundy highlight / #D86E8E velvet sheen / #C9A227 gold foil / #8A6E14 foil shadow / #5E4A44 grubby dark / #3A2E2A stain / #A89A94 worn backing / #E0E6EA clasp plastic / #6E5F72 cast shadow / #FF00FF chroma key

DO NOT INCLUDE:
anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 3. PROMPT B — GPT Image 2

```text
Cloth event wristband lying flat as a flattened permanently creased loop in deep crushed-velvet burgundy with two hard sheen highlight bands, a small blocky illegible half-rubbed gold foil VIP mark, one-way barbed plastic snap clasp with a hand-trimmed uneven tail, grubby darkened section from days of wear with a small dark stain and a frayed edge where the velvet nap has worn through to the woven backing, sticky residue sheen near the clasp, SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no background, no hands

--no anti-aliasing, blurry edges, soft shading, smooth gradients, glow, bloom, glossy 3D render, vector art, modern flat design, material design, photorealism, photograph, watermark, signature, caption text, UI frame or border, inventory box, background scenery, floor, table, wall, hands, arms, characters holding the object, multiple objects, exploded view, isometric grid, more than 16 colors, pastel washed-out palette, cute chibi mascot styling
```

## 4. Palette

```
#2B1A2E outline / #7E1E3E velvet burgundy / #4A0E22 burgundy shadow / #B44E6E burgundy highlight / #D86E8E velvet sheen / #C9A227 gold foil / #8A6E14 foil shadow / #5E4A44 grubby dark / #3A2E2A stain / #A89A94 worn backing / #E0E6EA clasp plastic / #6E5F72 cast shadow / #FF00FF chroma key
```

## 5. Variants to generate in the same session

- **Worn variant (32x32)** — on a wrist, stacked above the LiveStrong and WWJD bands, which is a genuinely tragic image.
- **Fresh variant** — crisp, clean, gold mark intact, for the moment of purchase.
- **Cut-off variant** — severed and lying limp, for the end-of-city state.

## 6. Art-director notes

- Burgundy velvet against a dark outline is low-contrast; push the sheen bands brighter so the loop separates at 32px.
- Velvet is rendered as two hard sheen bands, never as soft nap. Any gradient and it stops being SNES.
- The barbed one-way clasp is the detail that explains why he still has it on. Make the barbs visible.

## 7. Post-process

1. Generate at 1024x1024.
2. Nearest-neighbor downsample to 128x128, then to 64x64 in Aseprite.
3. Index to a 16-color palette (`Sprite > Color Mode > Indexed`, palette from file).
4. Hand-clean the outline — the generator will always leave stray half-tone pixels on curves.
5. Key out `#FF00FF` to alpha. Export `<slug>_64.png` and keep the 128 as the master.

Treat the AI output as a **paint-over base**, not a shippable asset. Neither Gemini nor GPT Image 2 produces a true pixel grid; they produce a pixel-*flavored* raster that has to be resampled and repaired.

---

## 🖼️ Physical description (icon art brief)

**[APPROVED — author, Desk Eurobound-rpac-q3, 2026-11-15: "Approve all; symbol A (neume); crown base pastel pink".]** Written in the Writers' Room (`WritingRoom/tasks/20261114_1900_item_physical_descriptions_batch_2_asset/final.md`).

| Field | Description |
|---|---|
| silhouette | A flattened oval loop of wide flat strap, wider than it is thick — it lies on its side at a three-quarter view, permanently creased flat like a band that has not been off a wrist in four days. A chunky solid clasp block sits on the band, and a short blunt tail the full band width sticks out just past it. No buckle, no buckle holes, no jewellery geometry: it reads as an event band, not a bracelet. |
| scale_cue | The oval hole and the clasp block are the two reads in an empty frame; the tail past the clasp is the third. At 32 px the loop must still be an oval loop of flat strap with a lump on it. |
| materials_and_cheap_cues | Matte crushed velvet with the nap crushed permanently flat in the pinch marks of a thumb and forefinger. The sheen is not nap — it is exactly two hard-edged lighter bands running the length of the strap, each a flat shape with stepped edges. The clasp is chunky solid grey-white plastic with bold sawtooth barbs cast into it: this band cannot come off without scissors, which is the entire point. Gold foil is thin, dull and half gone. A flat glossy residue patch beside the clasp reads as sticky, not wet. |
| colours | Velvet base: burgundy #7E1E3E. Velvet shadow: #4A0E22. Sheen band: #D86E8E — two bands only, hard edges. Ridge highlight: #B44E6E. Foil: dull gold #C9A227, shadow #8A6E14, worn through to backing grey #A89A94. Clasp: cool grey-white #E0E6EA. Grime: #5E4A44; stains: #3A2E2A. Outline: dark plum #2B1A2E. |
| contents | None — it is a band. |
| decoration | Exactly one small blocky gold foil mark, hard straight edges, no letters: a short bar and a broke-off stub of a second shape, half rubbed back to the woven backing. Nothing else printed, sewn, stamped or embroidered. |
| condition | Four days on one wrist, in flat areas: a few lighter bald patches where the velvet nap is worn through, one flat paler strip along a lower edge where it is frayed (a strip, not threads), broad hard-edged brown stains, one darker stain, a sticky residue patch beside the clasp, a crease line down the whole loop from being pressed flat. Foil worn to a stub. Tail cut unevenly and forever slightly too short. |
| garnish_and_addons | None. No bead, no charm, no rivet, no fabric tag. |
| palette_anchors | Taken from the item's own palette block (`Assets/Graphics/items/velvet-wristband-vip.md:60`): #7E1E3E, #4A0E22, #B44E6E, #D86E8E, #C9A227, #8A6E14, #5E4A44, #3A2E2A, #A89A94, #E0E6EA, #2B1A2E. Location-side anchors available and not used: `design/worlds/debaucheryville/velvet_curtain_club.md:284` deep burgundy #800020 and gold #FFD700 — both brighter and richer than these hexes; using them would make a 40-SOVS band look premium. New to this item: none. |
| reads_at_icon_size | A wide flat strap in a loop with a lumpy clasp and a stub of tail past it — an event band, never a bracelet, bangle or ring. Burgundy with two hard pale bands along it, not a gradient — flat strap, flat finish. Used: stains, fuzz-flat bald patches, a paler frayed edge strip, a rubbed foil stub. |
| must_not_look_like | Jewellery — no buckle, no clasp holes, no polished shine, no gemstone, no metal band. A bangle, cuff, bracelet or scrunchie — flat strap with a tail and a plastic block, not a ring. A pet collar, a lanyard or a hospital band — cloth velvet, wide, with a foil mark. A clean, fresh, newly-bought band — that variant exists separately; this icon is the four-days-in state. A stack of bands — one band, one loop, no wrist in frame at all. |
| lettering | None. The foil mark is canonically illegible: a bar and a stub, no letters. |

### Changes from the shipped icon
- CHANGED (was: sheen described as "two sheen bands" without form): each band is now a hard-edged flat shape with stepped edges. Soft nap or a gradient turns velvet into satin and the band into jewellery.
- CHANGED (was: "small blocky illegible pixel shape"): specified as a bar plus a broke-off stub, no letters — the doc calls the foil canonically illegible, so any readable "VIP" would contradict it.
