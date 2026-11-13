# Opener: The Hoisted Pint: item icon prompt (item-opener_hoisted_pint)

Source: design/items/brewery_tour/opener_hoisted_pint_item.md, "Design" lines 9-13 (brass gable hoist hook, throat of the hook is the opener; inscription "If It Fits, It Lifts."; brass hook on a twist of tarred rope as the keychain loop; hangs at 7 degrees, never straight). No per-item spec. The inscription is deliberately NOT legible: an engraved band of abstract marks of varying length. No glow state.

## PROMPT (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A brass gable hoist hook, the kind mounted on the gable of a Dutch canal house, used as a bottle opener keychain charm, shown as one single object, seen from a slight three-quarter front view, floating alone. It is a chunky heavy curved brass hook with real mass, a thick rounded shank at the top with a ring eye, curving down into a deep round belly and ending in an upturned blunt hook point, shaped like a big fat anchor-style hook, not a thin letter J. Inside the throat of the hook, on the inner curve, is a clearly visible flat notched bottle-opener lip, a squared-off notch with a lip catching a bottle cap. The brass is warm orange-gold with a few hard highlight clusters upper left. Through the top ring eye is threaded a short twist of dark tarred black-brown rope, chunky, twisted strands with diagonal twist lines, forming a small keychain loop at the top. The whole charm hangs visibly tilted about 7 degrees off vertical, leaning slightly, never perfectly straight. Around the shank of the hook runs a narrow engraved band made only of abstract tiny marks of varying length: short ticks, long ticks and dots in an irregular rhythm, absolutely no letters, no words, no numbers, no evenly spaced ruler ticks. Slightly lumpy and warped like a badly sculpted clay model, chunky heavy forms. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, multiple objects, more than 16 colors, faces, skulls, flags, people, question mark shape, letter J shape.
```

## Palette (10 colours, mapped by class and luminance band, not nearest colour)

Outline #2B1A2E, shadow #6E5F72 (redrawn in code). Brass, 5 bands by luminance percentile (12/40/70/92): #7A3E0C #B8680E #E8A020 #FFD860 #FFF0A8. Tarred rope, 3 bands (30/75): #3A261A #5C3C24 #845C38 (the lightest is the 1 px upper-left highlight on edge pixels).

## Post-process

Magenta keyed (eye and rope-loop holes stay transparent), generator shadow cut below raw row 1135, largest component kept. Rope class by position (above raw row 440) plus brown, low-luminance colour; brass class elsewhere. Raw outline pixels excluded from the luminance stats. Cell-averaged to 96 px tall on a 128 canvas (top at y 8); a cell is opaque at 50 percent coverage, 40 percent for rope cells so the thin twist survives. Per-cell class and luminance band, 3x3 majority on bands. Outline drawn OUTSIDE the object mask (8-neighbour dilation) so thin parts keep their mass, plus 1 px under the base; rope edge pixels with an outline above or left (and none below or right) get the 1 px highlight; code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (opaque when 2 of 4 are, so the rope and hook point survive), outline and shadow redone at 64. Margins 7/16/36/38 at 128, 3/7/17/18 at 64 (top/bottom/left/right). 10 colours at both sizes.

## Choices where the doc is silent

The generated engraved band read as faint glyphs, so it was redrawn in code: two thin rails with an irregular run of long, short and dot marks (no letters, no even ticks). The 7 degree tilt comes from the generation (it leans a little more than 7 degrees); the rope loop leans further than the hook. Ring eye on the hook shank for the rope; the doc does not say how the rope attaches. The raw is kept unmodified.

## Review fix (code only, on the 128 master)

The engraved band was redrawn as a plain recessed strip: #B8680E body, 1 px #FFD860 top edge, 1 px #7A3E0C bottom edge, and only single-width vertical notches and one dot in #7A3E0C (no enclosed boxes, no side-by-side dots). The 64 was rebuilt by 2x2 majority of the 128 object layer, outline and shadow redone. Still 10 colours; margins 7/16/36/38 at 128, 3/7/17/18 at 64.
