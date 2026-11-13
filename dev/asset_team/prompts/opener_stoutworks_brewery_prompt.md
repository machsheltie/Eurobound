# Opener: The Stoutworks Brewery: item icon prompt (item-opener_stoutworks_brewery)

Source: design/items/brewery_tour/opener_stoutworks_brewery_item.md, "Design" lines 9-13 (copper pot-still shape, spout is the opener; copper-plated steel with fake-aged verdigris; hollow centre for the whistle; inscription "Forged in Flavor" only as abstract engraved marks). No per-item spec. No glow state.

## PROMPT (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A copper pot still used as a bottle opener keychain charm, shown as one single object, seen from a slight three-quarter front view, floating alone. REAL POT-STILL SHAPE: a fat round squat copper pot body on a short base, a narrower rounded helmet neck on top, and a long swan-neck lyne arm curving up and out to the right and then angling downward. The end of the lyne arm flattens into a flat notched bottle-opener lip, a clearly visible squared-off notch that catches a bottle cap, like a spout that is the opener. The metal is warm orange-copper with flat hard cel shading, copper-plated steel. Fake-aged verdigris patina in dull teal-green appears only as a few irregular vertical drips and streaks running down from the seams and the neck, different lengths, asymmetric, never round spots, never paired spots. A round hollow hole goes clean through the pot body, showing transparent magenta background through it, placed clearly off-centre in the lower left of the pot body, fairly small, so it does not look like an eye or a face. A very short recessed engraved strip low on the pot, no wider than a quarter of the pot width, made only of a few irregular single notches and dots, no letters, no words, no numbers, no enclosed boxes. Nothing else on the pot body, plain smooth copper with light and shade. Slightly lumpy like a badly sculpted clay model, chunky. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, logo, UI frame, background, floor, table, steam, liquid, multiple objects, more than 16 colors, faces, eyes, mouth, smile, paired spots, skulls, flags, people.
```

Raw kept unmodified (1254 px): dev/asset_team/raw/opener_stoutworks_brewery_raw.png.

## Palette (8 object colours plus outline and shadow, mapped by class and luminance band, not nearest colour)

Outline #2B1A2E, shadow #6E5F72 (code). Copper, 5 bands (1D k-means on copper luminance, band edges at cluster midpoints): #6B2A0A #A8420C #D8651A #F08A3C #FFC078. Verdigris (green-dominant cells), 3 bands: #2E6E5A #4E8E5E #8CC49A (only 2 used by the render at the end).

## Post-process

Magenta keyed; raw plum outline and generator shadow removed (everything below raw row 1095 cut); largest component (after a 6 px closing, so the foot stays attached); small interior holes (the generated smile marks, specks) filled, the real through-hole kept. Cell-averaged to 103 x 100 px on a 128 canvas (top at y 8), 50 percent coverage; class by green share (30 percent), band by luminance, 3x3 majority on copper bands (verdigris cells unsmoothed so the streaks survive). Outline outside the mask (8-neighbour) plus 1 px under; code-drawn elliptical shadow centred on the pot base. 64 is a 2x2 majority of the 128 object layer (opaque at 2 of 4, so the lyne arm survives), outline and shadow redone.

## Choices where the doc is silent

The generated engraving was a smile-shaped mark under the hole (reads as a face), so it was removed and redrawn in code: a 14 px recessed strip low on the pot, right of the hole, 1 px light top edge, body, 1 px dark bottom edge, and four single-pixel notches (no pairs, no enclosed boxes, no letter shapes). Verdigris stays as three irregular drips, never spots. The hole sits off-centre lower left. The opener lip is the flattened, notched end of the lyne arm as generated.

## Scripted checks (all pass)

128: 10 colours, margins t/b/l/r 9/12/13/15 (need 6), 592 edge pixels all #2B1A2E or shadow, 0 violations. 64: 9 colours, margins 4/4/6/7 (need 3), 286 edge pixels, 0 violations.
