# absinthe_shot (Absinthe Shot, Debaucheryville Special): scripted Blender lathe (batch 15, round 1)
Method: `Tools/item3d/lathe_item.py absinthe` (+ `palette_mesh.py`): glass lathed from an (r,z) profile, thick walls and heavy base, opaque satin tint #C4D8DC; opaque liquid top disc + body-colour band #6EE81E; all parts fused to one mesh, flat-colour atlas, no transparency. 0 credits, no image tool. Fallback, pre-rollout.
Canon: `Assets/Graphics/items/absinthe-shot.md` L31 (DRAW THIS OBJECT) and L60 (palette). Pixel-art redo.
Shows: thick shot glass of acid green, stained coaster with green spill ring and coffee ring, tarnished slotted spoon across the rim, sugar cube, two caramel drips, hard 3-band flame (blue/orange-yellow), stepped smoke curl.
Not built: thumbprint smudges (too fine at icon scale).
Choices not in the docs: coaster colour (#E8E4D8 reused from the sugar cube), glass proportions, number of smoke steps (3, doc says 6-8 pixels), flame as stacked hex cones.
No lettering.

## Round 2 (A3 R1 fail)
Rebuilt: one connected object. Glass wall is a painted cylinder map (green liquid, caramel-brown drips, thumbprint smudges, sticky green base, all flat). FAT slotted spoon (0.90 x 0.16 x 0.07, 4 bold slots) in tarnished dull silver #9AA3A6 with dark patches #5E5A52, sunk into the rim. Coaster rings and stains painted flat. Two fat caramel strands, ONE solid teardrop flame (blue/orange/yellow by height) fused to the cube. Smoke, floating cubes and decal rings deleted. Art: `absinthe_shot_paint.png`. Script: `lathe_item.py absinthe <out.glb> <paint.png>`.
