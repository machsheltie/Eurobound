# Summer Vacation Trivia Champ Badge: item icon prompt (item_trivia_champ_badge)

Source: design/items/trivia_champ_badge_item.md, "What The Item Actually Is" (line 18: ~0.008 SOVS gold plastic kids' sheriff badge, flaking glitter print) and "Visual Specifications" (lines 38-47: gold-painted injection-molded plastic, five-point star about 4 cm, bent metal pin, glitter text curved around the face, gold paint thin at the points even on Day 1). No per-item spec exists; PROMPT B follows the style guide and digital-watch-calculator.md as the model. The stamped text is deliberately NOT painted legibly (team brief: no legible text).

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): Cheap plastic kids' toy sheriff badge, a classic five-point star with a small ball tip on each point, seen straight-on from the front with a very slight three-quarter tilt, floating alone. Gold-painted injection-molded plastic with a flat cheap sheen, not shiny metal: the gold paint is thin and already wearing off at the five tips, showing dull gray plastic at the tips. A thin molding seam line runs across the star's edge where two plastic halves were fused. In the center of the star face, a round raised disc ring with a curved band of flaking glitter print made only of chunky abstract blocks and cracked gold and silver glitter flecks with some flecks peeled off, no letters, no words, no numbers, no faces, no skulls, no flags, no stars inside. Make the star slightly lumpy and warped like a badly sculpted clay model. Faint hint of a bent flimsy pin clasp peeking out from behind one lower edge. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color warm grubby palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no hands, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, hands, multiple objects, more than 16 colors, faces, skulls, flags, chibi mascot styling.
```

## Palette (mapped by material luminance band, not nearest colour)

#2B1A2E outline / #6E5F72 cast shadow (redrawn in code) / painted gold ramp by luminance quantile: #8A6E1E, #C98E2E, #C9A227, #E8B430, #C9BE8E / worn gray plastic and silver glitter (low saturation pixels) ramp: #6E7478, #A8AEB4, #E0E6EA. 10 colours total.

## Post-process

Magenta keyed out, generator shadow dropped, largest connected component kept, box-downsampled to 92 px tall on a 128 canvas, gold and gray pixels remapped by luminance quantile bands (gray picked out by saturation), outline rebuilt on every 8-neighbour boundary plus 1 px under the base, clean elliptical shadow drawn in code. 64 is a 2x2 majority of the 128, then 8-neighbour edge pixels recoloured to the outline colour, underside row added, shadow redrawn.

## Choices where the doc is silent

Ball-tipped points (classic toy-sheriff look), a raised central disc ring carrying the glitter band, the mold seam, the pin clasp only hinted behind the lower edge, Day 1-3 "pristine" state with thin gold already showing gray at the five tips (per the Finish row).
