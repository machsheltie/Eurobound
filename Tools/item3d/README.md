# tools/item3d: 3D item icons (Tripo + Blender), trial: opener_crown_and_cask
1. Reference: Firefly HOME screen, GPT Image 2.5 Sunburst, Quality High, 1:1, one object on flat light grey (prompt in `dev/asset_team/prompts/opener_crown_and_cask_3d_prompt.md`). Download button, move out of Downloads. 0 Tripo credits.
2. Tripo Studio (browser, no API key yet): upload the PNG, Generate (HD Model, default): 55 credits, about 2 min, 1.96M faces.
3. Same page, Retopo tab: Triangle, count 20000, Smart Mesh on: 35 credits, about 2 min, 19,400 faces. (This is the "simplify" step; there is none in Export.)
4. Export: GLB, 4k texture, free. Move the file out of Downloads into a dl/ folder.
5. Render: `"C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python tools/item3d/render_item.py -- <glb> <out>_512.png` writes the 512 RGBA and a 128 LANCZOS copy (`_128.png`, needs system `python` with Pillow). About 11 s.
6. Render details: deletes Icosphere* helpers, toon material from the GLB base-colour texture (`look.toon_material`), `look.lights`, `look.render`; ortho camera, yaw 28 deg, pitch 22 deg, key upper left, transparent film, Standard view transform. No outline, no palette lock, no painted shadow.
7. Scale: the model is normalised to a bounding-sphere diameter of 1.0 unit and ORTHO_SCALE = 0.95 is fixed, so every icon shares one px-per-unit (512 px / 0.95 units).
Total Tripo cost for one item: 90 credits (55 + 35). The new Tripo balance reading also drops from other users' work on the shared account.
