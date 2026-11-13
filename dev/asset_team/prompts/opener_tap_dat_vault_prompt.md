# Bottle Opener: The Tap Dat Vault: item icon prompt (item-opener_tap_dat_vault)

Source: design/items/brewery_tour/opener_tap_dat_vault_item.md, "Design" (L10 vault door shape with soundwave pattern cutout, opener integrated into the door handle; L11 inscription "Inhaled & Survived"; L12 brushed chrome with cyan/hot-pink neon that glows; L13 tiny LED). No per-item spec exists; PROMPT B follows the style guide. The inscription is deliberately NOT legible (team brief): it is an engraved band of abstract tally marks and squiggles. Two states like the Absinthium opener: base and `_glow` (doc PNG list: `bottle_opener_tap_dat_vault_glow.png`).

## PROMPT B (ChatGPT image generation, 1 round, used as sent)

```text
Create an image (square, 1024x1024): A heavy brushed-chrome bank-vault door seen head-on, slightly three-quarter, used as a bottle opener keychain charm, floating alone. The door is a fat round slab with a thick riveted rim and a thick chunky chrome handle bar across the lower middle whose underside has a clear rectangular bottle-opener slot cut through it, big enough to see through. In the center of the door a round recessed panel with a soundwave pattern cut out as a row of seven vertical bars of different heights, symmetrical like an audio waveform, the cutout glowing hot-pink neon with a cyan neon ring tracing the panel edge. Around the upper rim a narrow engraved band of tiny abstract tally-like marks and squiggles, absolutely no letters, no words, no numbers. A single tiny round LED at the top right of the door, lit bright cyan. Hot-pink neon trim lines along the rim. Brushed chrome: cool grey-silver with a few hard horizontal brushed streak bands, small hard white highlight clusters upper left. Neon drawn as flat saturated color with a hard-edged 1px lighter core stripe, absolutely no glow, no bloom, no gradient. Slightly lumpy and warped like a badly sculpted clay model. SNES 16-bit item sprite in EarthBound MOTHER 2 style, single centered object on flat #FF00FF magenta chroma background, chunky visible square pixels, zero anti-aliasing, hard 1px dark plum-brown #2B1A2E outline thicker underneath, flat three-tone cel shading, light from upper left, strict 16-color palette, one small hard elliptical drop shadow beneath, silhouette readable at 32x32, no text, no border, no extra objects, lots of empty margin around the object. Avoid: anti-aliasing, blur, gradients, glow, bloom, glossy 3D render, vector art, photorealism, watermark, readable letters or numbers, brand logo, UI frame, background scenery, floor, table, multiple objects, more than 16 colors, faces, skulls, flags, chibi mascot styling.
```

## Palette (mapped by class and luminance band, not nearest colour)

Source pixels were classified (transparent, dark line, chrome, pink neon, cyan neon) by hue, saturation and value, majority-voted per target cell (neon wins at 30 percent of a cell). Chrome cells take one of 5 bands by luminance percentile (15/45/75/93), then a 3x3 majority on the chrome band map. Neon cells take 3 levels by luminance tercile within their class.

- Shared: outline #2B1A2E, shadow #6E5F72 (redrawn in code), chrome #4A5058 #6E7478 #A8AEB4 #D0D6DA #F4F6F8.
- Base (13 colours): pink #96186A #E0349E #FF80CC, cyan #187690 #24B8C8 #96E8F0. LED is the darkest cyan (unlit-looking).
- Glow (15 colours): the same pixels, neon stepped one band brighter (pink #FF3CB4 #FF9AD8 #FFE0F4, cyan #28D8E8 #B8FAFF #F0FFFF), LED at the near-white core, plus a hard 1 px tint band on chrome pixels 4-adjacent to neon (pink #E07AB8, cyan #6ED0E0). No soft halo, no alpha.

## Post-process

Magenta keyed (the opener slot stays transparent), generator shadow cut off below row 906 of the 1254 px raw, largest component kept, resampled to 90x104 on a 128 canvas, outline rebuilt on every 8-neighbour boundary plus 1 px under the base, code-drawn elliptical shadow. 64 is a 2x2 majority of the 128 object layer (opaque when 2 of 4 are, neon wins ties, then outline), 8-neighbour edges recoloured to the outline, shadow redrawn at 64.

## Review fix (code only)

The generator's X-shaped valve wheel sat beside the soundwave window and read as a face (two eyes over the slot mouth). It was removed in code on base and glow: the area (x 80-95, y 51-67 at 128) was patched with brushed-chrome bands plus two rivets cloned from the bottom rim rivet, then the 64 was rebuilt from the patched 128 with one extra 3x3 majority on the chrome pixels only (neon and outline untouched). The raw keeps the wheel; the hinge bar on the left stays.

## Choices where the doc is silent

Keyring loop at the top (it is a keychain clip-on), a hinge bar on the left (generator dressing on a vault door), seven-bar soundwave, LED upper right, pink rim trim.
