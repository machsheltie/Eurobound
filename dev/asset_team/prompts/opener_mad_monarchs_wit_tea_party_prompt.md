# Opener: The Mad Monarch's Wit-tea Party: item icon prompt (item-opener_mad_monarchs_wit_tea_party)

Source: design/items/brewery_tour/opener_mad_monarchs_wit_tea_party_item.md, "Design" lines 9-13 (orange-enamelled brass teacup, handle is the opener, tiny lacquered cardboard crown glued to the rim, brass shows through chipped enamel, orange thumbprint "pre-sprayed"; inscription "The Morning After Is For Cowards." only as abstract engraved marks). No per-item spec. No glow state.

## PROMPT (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): An orange-enamelled brass teacup used as a bottle opener keychain charm, shown as one single object, seen from a slight three-quarter front view, floating alone. It is a chunky fat teacup with a thick rounded bowl in glossy-flat orange enamel, with a few chipped spots where bare warm brass shows through, and a small hard orange thumbprint smudge on the side. The handle on the right is a chunky brass loop that is the bottle opener: its loop is the grip, and its inner lip is a clearly visible notched cap-catching lip. A tiny folded cardboard paper crown, lacquered tan-gold cardboard, is glued to the rim of the cup: a simple paper-crown doodle with exactly three or four plain triangular points, not a real royal crest, no jewels, no emblem. A narrow recessed engraved strip runs around the cup body made only of irregular single notches and dots of varying length, absolutely no letters, no words, no numbers, no enclosed boxes. Slightly lumpy and warped like a badly sculpted clay model, chunky heavy forms. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, saucer, steam, multiple objects, more than 16 colors, faces, skulls, flags, people, eyes, smile.
```

## Palette (12 colours plus outline and shadow, mapped by class and luminance band, not nearest colour)

Outline #2B1A2E, shadow #6E5F72 (redrawn in code). Enamel, 4 bands by luminance percentile (12/40/75): #8A2E0A #C84A0C #FF7A10 #FFB050. Brass (handle, chips), 4 bands (12/40/70): #7A3E0C #B8680E #E8A020 #FFD860. Cardboard crown (by position above raw row 445, brass hue), 3 bands (30/75): #8A5A2E #C89050 #E8C888. Class by hue (above 36 degrees is brass).

## Post-process

Magenta keyed, generator shadow cut below raw row 935, largest component kept, raw outline pixels excluded from luminance stats. Cell-averaged to 108 px wide (77 tall) on a 128 canvas (top at y 20), a cell is opaque at 50 percent coverage; per-cell class and band, 3x3 majority on bands (crown cells kept unsmoothed so its points survive). Outline drawn outside the mask (8-neighbour) plus 1 px under; code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (opaque at 2 of 4), outline and shadow redone. Margins 19/20/9/9 at 128 and 9/9/4/4 at 64 (top/bottom/left/right, shadow included).

## Choices where the doc is silent

The engraved strip was redrawn in code as a short recessed strip on the left of the cup body (light top edge, dark bottom edge, single-width notches and dots, no enclosed boxes, no letter shapes), kept short so it does not read as a mouth; the remaining raw vertical ticks to its right stay as single notches. The thumbprint smudge is a small darker orange oval drawn in code. The handle is a plain brass loop as generated. Raw kept unmodified.
