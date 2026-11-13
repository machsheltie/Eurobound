# Opener: Bottoms Down: item icon prompt (item-opener_bottoms_down)

Source: design/items/brewery_tour/opener_bottoms_down_item.md, "Design" lines 10-13 (tulip jenever glass shape, overfilled, surface tension visible; opener is the stem; inscription "No Hands. No Fear."; amber-tinted brass with sawdust-coloured leather loop; slightly convex meniscus). No per-item spec. The inscription is deliberately NOT legible: it is an engraved band of abstract tick marks. No glow state.

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A traditional tulip-shaped jenever shot glass used as a bottle opener keychain charm, standing upright, seen from a slight three-quarter front view, floating alone. The glass bowl is a small fat tulip shape on top, made of amber-tinted brass-gold colored glass-like metal, overfilled with golden liquid so the surface bulges above the rim as a slightly convex meniscus dome, a hard-edged lighter dome cap on top showing surface tension. Around the middle of the bowl runs a narrow engraved band made only of abstract tiny tally-like marks and notches, absolutely no letters, no words, no numbers. The stem of the glass is a flat chunky brass bottle-opener plate with a rounded oval opening hole in it. At the bottom of the stem hangs a sawdust-colored tan leather loop strap, chunky, with a visible stitch line. Amber-tinted brass: warm orange-gold with a few hard highlight clusters upper left. Slightly lumpy and warped like a badly sculpted clay model, chunky heavy forms. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, multiple objects, more than 16 colors, faces, skulls, flags, people.
```

## Palette (10 colours, mapped by class and luminance band, not nearest colour)

Outline #2B1A2E, shadow #6E5F72 (redrawn in code). Brass, 5 bands by luminance percentile (12/40/70/92): #7A3E0C #B8680E #E8A020 #FFD860 #FFF0A8. Leather (raw rows below the opener plate, by position), 3 bands (30/75): #8A5A2E #C89050 #E8C888.

## Post-process

Magenta keyed (opener hole stays transparent), generator shadow cut below raw row 1100, largest component kept, cell-averaged to 98 px tall on a 128 canvas (top at y 6), per-cell class and luminance band, 3x3 majority on bands. Outline on every 8-neighbour boundary plus 1 px under the base; code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (opaque when 2 of 4 are, so the thin leather loop survives), 8-neighbour edges recoloured, shadow redrawn at 64. Margins: 6/14/43/44 at 128, 3/7/21/22 at 64 (top/bottom/left/right).

## Review fixes (code only, on the 128 master; 64 rebuilt by 2x2 majority, edges and shadow redone)

1. Leather: the solid strap was removed and redrawn as a narrow open loop (16 px wide at 128, hole 4 x 14 px transparent) hanging straight from a small brass eyelet under the opener plate; tan edge #8A5A2E, body #C89050, highlight #E8C888, outline rules kept.
2. Meniscus: the cap was removed. A thin brass rim line (#FFD860 over #7A3E0C) now carries a low convex dome of liquid amber (#FFCB1F, shade #FF9F0A, one hard highlight streak #FFF6C0), slightly wider than the glass. No lid seam.
3. Engraved band: the even ticks were replaced by an uneven run of long, short and dot marks (single-width, no letter shapes).
Result: 13 colours at 128, 10 at 64. Margins 6/14/43/44 at 128, 3/7/21/22 at 64.

## Choices where the doc is silent

The generated band marks read as faint glyphs after downsampling, so the engraved band was redrawn in code as a plain row of vertical tick marks (no letters). The leather loop reads as a solid strap (its stitch line is lost at this size). Opener plate with oval hole as the stem, as in the generator output. Raw keeps the original marks.
