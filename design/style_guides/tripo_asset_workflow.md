# Tripo asset workflow (author, 2026-11-16)

**Binding.** This is how every character (sprite) and item is made from now on. The author built it and tested it on Lord Pilsner, so it replaces the older character and item pipelines (`character_sprite_pipeline.md`, the char3d look-B rebuilds, scripted Blender icons) wherever they disagree.

The author's words, verbatim:

> "take an MD file of either a sprite or an item and go ahead and take the art that I worked from for Lord Pilsner the picture where he has the beer in his hand and use that as our reference for what our art style looks like and with a MD file you are going to have the asset and [sprite] teams use firefly with GPT Image 2.6 Sunburst on high to generate four views of each item or sprite front left side right side backside and then you were going to open up Tripo and develop a T pose if it's a character using all four views front left side right side backside and then you're going to develop a smart mesh for characters. They get 25,000 polygons and our quads. and the smart mesh will allow you to select all four of views so that it knows what all four sides are supposed to look like and then you are going to for characters at least segment it and then fill parts. Then retopo 25,000 polygons quads (characters only). Then for all use smart uv, texture, and for characters rig and animate with at least idle and walk. Then export"

## Style reference

`Assets/Graphics/sprites/characters/party_members/lordpilsner/alts/Smug Beach Bro with Beer.png`

This is Lord Pilsner holding a beer. It shows the look every generated view must match: a photoreal studio photograph on a plain white background, with natural light and real fabric and skin texture. Attach it to every Firefly generation as the style reference.

The author's own finished example is Lord Pilsner's four views and T-pose in `Assets/Graphics/sprites/characters/party_members/lordpilsner/`.

## Steps

| # | Step | Characters | Items |
|---|---|---|---|
| 1 | Start from the asset's `.md` file: its look, palette and every detail it names. Invent nothing the file doesn't say; ask on the Desk. | yes | yes |
| 2 | **Adobe Firefly**, model **GPT Image 2.6**, style **Sunburst**, quality **High**, with the style reference attached. Generate **four views**: front, left side, right side, back. | yes | yes |
| 3 | **Tripo website** (never the API): build from all four views. For a character, make a **T-pose**. | T-pose | yes |
| 4 | **Smart Mesh**, selecting all four views so Tripo knows every side. | yes | see open questions |
| 5 | ~~**Segment**, then **Fill Parts**.~~ **Dropped** (author, Desk p7n6.6-q2, 2026-11-16: "Characters skip segment and fill parts; keep Smart UV (how Whitney was made)"). Tripo won't do both segment and Smart UV on one character. | no | no |
| 6 | **Retopology: 25,000 polygons, quads.** | yes | no |
| 7 | **Smart UV.** | yes | yes |
| 8 | **Texture.** | yes | yes |
| 9 | **Rig**, then **animate**: at least **idle** and **walk**. | yes | no |
| 10 | **Export.** | yes | yes |

## Standing rules that still apply

- Tripo website only: no paid APIs (memory: no-paid-apis). Firefly through the website. Lettering is never drawn by an image tool; it is typed and applied afterwards (bead memory `3d-item-icons-flat-or-thin-items-cards`).
- Read every word on generated art and fix misspellings (memory: generated-text).
- Blind QC gates still review the result, judged **in game**, not on a sheet: `tools/char3d/QC.md`, `asset_team/QC.md`, and the Eurobound-8c3z finding that sheets passed what looked wrong in the hall.
- Show the author the result in the Absinthe Arcade hall before it ships, as was done for Lord Pilsner on 2026-11-16 (`Assets/Graphics/characters3d/_author_pilsner_preview/`).

## Notes from the Lord Pilsner test (2026-11-16)

- **Tripo's Export box defaults "Number of Animations" to 0.** Every character export must click that row and choose Select All, or the file has no idle or walk. That is why the first `lordpilsner.glb` had none.
- If Tripo says an export succeeded but nothing arrives in Downloads (seen on Bradley, 2026-11-16), press Ctrl+J first. Tripo builds the file fine, but Chrome silently drops the hand-off. The fix that worked: let the export finish, take the finished file's link from inside the Tripo page, and download it in the same browser. The link stays in the browser. The Export box's "Send to" and the DCC Bridge are untried alternatives.
- Tripo's export came in about 0.97 m tall. He was scaled ×1.865 to 1.815 m for the hall.
- Godot loaded Tripo's FBX lying flat, so Blender converted it to GLB for viewing.
- The Tripo stock walk had negligible foot slide. A text-prompted walk tipped his head back in every frame.

## Settled the same day (author, chat, 2026-11-16)

- **Items:** "Yes on smart mesh and a 10k polygon budget for items." Items run: four views, Smart Mesh, a 10,000-polygon budget, Smart UV, texture, export. No segment, no 25k retopo, no rig.
- **Export:** "Go with your choice of export formats." Export **GLB** (Godot opens it directly; Tripo's FBX loaded lying flat). Save it in the character's or item's own folder, named after the asset.
- **Restart:** "you can start now." The pause is lifted.

## Still open

- Tripo credit budget per asset. Until it's settled, keep re-rolls lean and log the credits each asset used in its handoff.
- The author is building Bradley and Chadwick personally. Agents leave both alone.
