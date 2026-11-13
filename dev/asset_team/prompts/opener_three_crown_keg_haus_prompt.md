# Opener: Three-Crown Keg Haus: item icon prompt (item-opener_three_crown_keg_haus)

Source: design/items/brewery_tour/opener_three_crown_keg_haus_item.md, "Design" lines 10-13 (three rusted crowns stacked vertically with the bottle opener as base/throne, miniature stein charm dangling from a ring; inscription "Noble by Liver"; intentionally tarnished brass with rust-orange patina; stein charm holds 1ml of liquid). The PNG Assets list (lines 16-17) is the opener 48x48 plus a 24x24 charm, with no glow or alternate state, so there is no _shift variant; the charm is drawn dangling in the one icon. The inscription is deliberately an engraved band of abstract marks (no legible text).

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A tiny keychain bottle opener charm, standing upright, seen from a slight three-quarter front view, floating alone. Three small crowns are stacked vertically in a tall column, one on top of the next, each a chunky five-point crown with a rounded band, and the bottom of the column sits on a flat wide bottle-opener plate that acts as the throne base (an opener plate with a rounded oval opening hole in it). Intentionally tarnished old brass with rust-orange patina crusted in the crevices: warm dull gold brass base with big patches of rust orange and darker brown-olive tarnish, the crowns look neglected and rusty. Around the base plate runs a narrow engraved band made only of abstract tiny blocky marks and notches, absolutely no readable letters or words or numbers. At the left side of the base plate a small brass split ring, and hanging from the ring on a short loop a miniature beer stein charm: a tiny squat brass-rimmed stein with a handle, with a small glass window showing a band of amber beer in it (flat amber color, hard-edged, no glow). Make it slightly lumpy and warped like a badly sculpted clay model, chunky heavy forms. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading per material, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, flags, shields, faces, skulls, people, UI frame, background scenery, floor, table, multiple objects, more than 16 colors.
```

## Palette (mapped by luminance band and hue, not nearest colour)

#2B1A2E outline / #6E5F72 cast shadow (redrawn in code) / brass by luminance quantile: #7A5A1C, #C9A227, #E8C860 / rust patina (orange hue) by luminance quantile: #7A3012, #B84A16, #D87424 / stein beer (box region only): #B86E1A, #E8A830 / stein foam band #EDE8D8. 11 colours.

## Post-process

Magenta and the generator shadow keyed out, largest components kept, box-downsampled to 108 px tall on a 128 canvas, material classes assigned by hue and luminance band, 3x3 majority on the class map, the thin split ring grown 1 px so brass survives between its outlines, outline rebuilt on every 8-neighbour boundary plus 1 px under the base, code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 (ties to the darker colour), 8-neighbour edges recoloured to the outline. One connected object, no semi-alpha.

## Choices where the doc is silent

Ring placed at the left of the base plate with the stein hanging at lower left; the doc gives no position. The 1ml liquid is shown as a hard amber band behind a small cream foam band. "Noble by Liver" is not rendered as text, only as a band of abstract notches around the base.
