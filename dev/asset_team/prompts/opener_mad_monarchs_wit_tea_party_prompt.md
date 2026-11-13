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

---

# ROUND 2 (supersedes round 1 above, which read as a jack-o'-lantern face; round 1 raw kept as opener_mad_monarchs_wit_tea_party_raw_round1.png)

Review asks: real teacup silhouette (flared rim, taper to a small foot ring, high three-quarter, dark inner rim), opener tooth inside the handle loop, 2-3 asymmetric brass chips at rim and foot, exactly one thumbprint off-centre, short low engraving strip, crown kept and leaning.

## PROMPT (ChatGPT image generation, round 2, used as sent)

```text
Create an image (square, 1024x1024): A classic porcelain-style teacup made of orange-enamelled brass, used as a bottle opener keychain charm, shown as one single object floating alone, seen from a slight high three-quarter angle looking down so the oval rim ellipse and a dark inner rim are visible. REAL TEACUP SILHOUETTE, not round, not spherical, not a pumpkin: a wide flared open rim at the top, the sides taper in smoothly down to a much narrower base, sitting on a small short foot ring. The enamel is flat orange with hard cel shading. Chipped enamel is only 2 or 3 tiny irregular brass-gold chips, one on the rim edge and one near the foot ring, different sizes, asymmetric, never two similar blobs side by side, no spots on the body. Exactly ONE small orange thumbprint smudge, off-centre near the root of the handle, drawn as a small irregular oval with 2 or 3 faint arc lines, not a solid dot. The handle loop is on the right side: a chunky brass loop that is the bottle opener, with a small brass tooth-like lip on the inside top of the loop that catches a bottle cap. A tiny folded lacquered cardboard paper crown, tan-gold, is glued to the rim and leans a little to one side: a simple paper-crown doodle with four plain triangular points, not a royal crest, no jewels. A very short recessed engraved strip, no wider than a quarter of the cup width, sits low on the cup just above the foot ring, made only of a few irregular single notches and dots, no letters, no words, no numbers, no enclosed boxes. Nothing at mid-height of the cup body, the body is plain smooth orange with just light and shade. Slightly lumpy like a badly sculpted clay model, chunky. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, logo, UI frame, background, floor, table, saucer, steam, tea liquid, multiple objects, more than 16 colors, faces, eyes, mouth, smile, paired spots, pumpkin shape, skulls, flags, people.
```

## Palette (round 2, 12 object colours plus outline and shadow)

Outline #2B1A2E, shadow #6E5F72 (code). Enamel, 4 bands by luminance percentile (12/40/75): #8A2E0A #C84A0C #FF7A10 #FFB050. Brass (handle x>850, opener tooth, two chips by position boxes), 4 bands (12/40/70): #7A3E0C #B8680E #E8A020 #FFD860. Crown (brass-hue pixels above raw row 440, right of x 700), 2 bands at median: #C89050 #E8C888. Dark inner rim (all-outline cells deep inside the mask): #4A1A28.

## Post-process

Magenta keyed; generator shadow removed (rows below 952; below row 895 only the foot columns kept); largest component; cell-averaged to 108 px wide (83 tall), top at y 16, 50 percent coverage; class by position and hue, band by luminance, 3x3 majority. Outline outside the mask (8-neighbour) plus 1 px under; code shadow. Engraving redrawn in code: a 14 px strip low above the foot ring (about a sixth of the cup width), irregular single notches and dots, nothing at mid-height. The thumbprint is a small irregular oval with two arc pixels, drawn in code on the lit body on the handle side. 64 is a 2x2 majority of the 128 object layer, outline and shadow redone.

## Scripted checks (all pass)

128: 14 colours, margins t/b/l/r 15/20/9/9 (need 6), 544 edge pixels all #2B1A2E or shadow, 0 violations. 64: 14 colours, margins 7/9/4/4 (need 3), 256 edge pixels, 0 violations.
