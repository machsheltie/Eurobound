# VIP All-Access Wristband: item icon prompt (item-vip_all_access_wristband)

Source: design/items/vip_wristband_item.md, "What The Item Actually Is" (line 18: cheap plastic children's birthday-party wristband, about 0.003 SOVS, printed "Je mi 7!") and "Physical Appearance" (lines 41-48: thin party-supply plastic, about 1.5 cm wide, cheap plastic snap clasp, printed slogan). Lines 103-113 distinguish it from the velvet wristband. No per-item spec exists; PROMPT B follows the style guide. The slogan is deliberately NOT painted legibly (team brief: no legible text), it is a band of balloons, stars and confetti.

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A cheap thin plastic children's birthday-party wristband, a single flat strip of glossy bright plastic, laid as a slightly open loop seen from a three-quarter front view, floating alone. The strip is narrow and thin, like a party-supply-store wristband, bright cheerful kid-party colors: the band is sunny yellow with a wide printed pattern band running along its length made only of chunky abstract balloons, stars and confetti blocks in red, blue and green, absolutely no letters, no words, no numbers, no faces. At one end a small cheap white plastic snap clasp: a round peg snapped into a hole, slightly crooked. Glossy cheap plastic sheen with a small hard-edged white highlight streak, slightly curled edge. Make it slightly lumpy and warped like a badly sculpted clay model. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no hands, no wrist, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, hands, multiple objects, more than 16 colors, faces, skulls, flags, chibi mascot styling, velvet, fabric.
```

## Palette (mapped by material luminance band, not nearest colour)

#2B1A2E outline / #6E5F72 cast shadow (redrawn in code) / yellow plastic ramp by luminance quantile: #B87C1C, #E8B430, #F6D840 / cream clasp and gloss streaks (low saturation): #C9BFA6, #F4EEDC / print motifs by hue: red #C0302A, blue #2E5ED0, green #3E9A4E. 10 colours total.

## Post-process

Magenta and generator shadow keyed out, largest component kept, box-downsampled to 114 px wide on a 128 canvas, material classes assigned by hue and luminance band, outline rebuilt on every 8-neighbour boundary plus 1 px under the base, code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (alpha kept when 2 of 4 are opaque so the thin back wall stays continuous), 8-neighbour edges recoloured to the outline, shadow redrawn at 64. Final: one connected object, no semi-alpha.

## Choices where the doc is silent

Sunny yellow band (the doc only gives per-bro colours for the sprite overlay, #CC0000/#0000CC/#6600CC; the icon is the neutral stock party band), a wide printed pattern band of balloons, stars and confetti standing in for the slogan, white round snap peg clasp, glossy highlight streaks for cheap plastic, slightly open loop with the clasp at the back right.
