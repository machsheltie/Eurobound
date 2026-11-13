# Opener: The Blarney Trap: item icon prompt (item-opener_blarney_trap)

Source: design/items/brewery_tour/opener_blarney_trap_item.md, "Design" lines 9-13 (Celtic-knot shamrock with the opener in the stem; "authentic" brass that is spray-painted zinc; inscription "May Your Glass Never Be Empty" only as engraved marks; shamrock spins on its ring). No per-item spec. No glow state.

## PROMPT (ChatGPT image generation, 1 round, used as sent; picked image 1 of 2, the one with the split ring)

```text
Create an image (square, 1024x1024): A three-leaf shamrock bottle opener keychain charm, shown as one single object, seen from a slight three-quarter front view, floating alone. The shamrock has exactly three heart-shaped leaves, each made of interlaced Celtic-knot bands that weave over and under, chunky thick bands. A short stem hangs down from the leaves and flattens into a bottle opener: a flat squared-off throat with a clearly visible notched lip that catches a bottle cap. The metal is fake brass: warm gold paint with a couple of small irregular scuffs where dull flat grey zinc shows through the gold. At the very top of the shamrock, between the two upper leaves, a small split ring (two-turn key ring) is threaded through a small loop, so the shamrock hangs from it. On the stem runs one short recessed engraved strip made only of a few single notches and dots, no letters, no words, no numbers, no enclosed boxes, no paired dots. Exactly three leaves, never a four-leaf clover, no harp, no flag, no emblem. Make the knot gaps small and irregular so they never look like eyes or a face. Slightly lumpy like a badly sculpted clay model, chunky heavy forms. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading per material, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, logo, UI frame, background scenery, floor, table, multiple objects, more than 16 colors, faces, eyes, skulls, flags, people, four-leaf clover, harp.
```

Raw kept unmodified (1254 px): dev/asset_team/raw/opener_blarney_trap_raw.png.

## Palette (10 colours, mapped by class and luminance band, not nearest colour)

Outline #2B1A2E, shadow #6E5F72 (redrawn in code). Brass, 5 bands by luminance percentile (12/40/70/92): #7A3E0C #B8680E #E8A020 #FFD860 #FFF0A8. Zinc (low-saturation cells), 3 bands (30/75): #5E5A66 #9896A0 #D0CED6.

## Post-process

Magenta keyed, generator shadow cut below raw row 1120, largest component kept (ring and knot gaps stay transparent where real). Cell-averaged to 98 px tall (59 wide) on a 128 canvas (top at y 8); a cell is opaque at 50 percent coverage. Raw outline pixels excluded from luminance stats; cells that are mostly raw outline take the darkest brass band, which keeps the knot over/under lines. Zinc class where grey (low saturation) share is above 30 percent. 3x3 majority on gold bands only (zinc cells unsmoothed so the scuffs survive). Outline drawn outside the object mask (8-neighbour) plus 1 px under; code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (opaque at 2 of 4; any zinc pixel keeps the cell zinc), outline and shadow redone.

## Choices where the doc is silent

The generated engraving was a column of dots, so it was redrawn in code on the stem: a 4x8 px recessed strip (1 px #FFD860 top edge, #B8680E body, 1 px #7A3E0C bottom edge) with three single #7A3E0C notch pixels, none touching, no boxes, no pairs, no letter shapes. Four small zinc scuffs come from the generation. The split ring hangs through a small loop at the top between the upper leaves; the ring hole is transparent.

## Scripted checks (all pass)

128: 10 colours, margins t/b/l/r 7/11/33/34 (need 6), 421 edge pixels all #2B1A2E or shadow, 0 violations. 64: 10 colours, margins 3/5/16/16 (need 3), 168 edge pixels, 0 violations.
