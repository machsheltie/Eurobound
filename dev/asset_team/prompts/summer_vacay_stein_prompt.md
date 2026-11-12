# Souvenir Champion Stein: item icon prompt (item_summer_vacay_stein)

Source: design/items/summer_vacay_stein_item.md, "What The Item Actually Is" (line 18): hollow plastic stein from a defective 2003 pallet, yellowed to a "concerning urine tone", unsealed mold seam with a thin constant drip line down the side, "CHAMPION" in flaking glitter print on the front. No per-item spec exists; PROMPT B follows the style guide and weapon-stein-mace.md as the model.

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): Cheap souvenir plastic beer stein, tall tapered mug with one C-shaped handle on the right, seen from the front in slight three-quarter view, empty, no lid, open top with a thick lip. The plastic has yellowed from cheerful gold to a murky urine-yellow, mustard-olive and grubby, slightly lumpy and warped like a badly sculpted clay model. A thin vertical molding seam runs down the front side where two plastic halves were fused, with a thin constant drip line of pale liquid running down from the seam and one single fat droplet hanging at the bottom of the seam. On the front, a flaking glitter print emblem: a plain rectangular banner of chunky abstract block shapes in cracked gold and silver glitter flecks with some flecks peeled off, no letters, no words, no numbers, no faces, no skulls, no flags. A few stray glitter flecks stuck on the rim. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, lumpy hand-sculpted clay-model forms, strict 16-color warm grubby palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no hands, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, hands, multiple objects, more than 16 colors, faces, skulls, flags, puddle, chibi mascot styling.
```

## Palette (mapped by material luminance band, not nearest colour)

#2B1A2E outline / #6E5F72 cast shadow (redrawn in code) / yellowed plastic ramp by luminance: #5A4A18 deep, #8A6E1E shadow, #C9A227 base, #E8B430 light, #C9BE8E highlight, #EDE8D8 top highlight and drip / glitter silver #A8AEB4 and #E0E6EA

## Post-process

Magenta keyed out, generator shadow dropped, object box-downsampled to 98 px tall on a 128 canvas, plastic pixels remapped by luminance quantile bands, silver glitter picked out by low saturation, outline rebuilt on every 8-neighbour boundary plus 1 px under the base, clean elliptical shadow drawn in code. 64 is a 2x2 majority of the 128, then 8-neighbour edge pixels recoloured to the outline colour.
