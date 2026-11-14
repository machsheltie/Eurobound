# Paint job: repaint or paint a location to its APPROVED plan

The orchestrator gives you: `id`, `city`, the approved plan file, which parts to paint (exterior, interior, or both), and any author notes. Everything below is binding.

1. **Worktree.** Yours is based on an old commit. READ everything from the main checkout `C:\Users\heirr\Desktop\Hope2_Studio\Eurobound`; WRITE deliverables only inside your worktree. Commit as soon as you have the first day plate, so the worktree is never empty.
2. **Brief.** Read `dev/asset_team/TEAM_BRIEF.md` in full:
   - section 2: parody, plan first, no look-alikes;
   - section 3: Firefly route and saving;
   - 4B/4C: deliverables;
   - 5: quality gates;
   - 7: cleanup.
3. **Spec.** A passing A1 (plan) line must exist in `dev/asset_team/reviews/qc_log.jsonl` before you generate anything. The approved plan is the spec. The author approved it as written, so its "needs approval" questions are settled the way the plan proposes. Read the files the plan cites: the location md, its PNG spec, and its JSONs in core/environment/interactions/items/location_nodes/npcs/sprite_mapping. Look at the current plates if any exist (you are replacing them), and at `dev/asset_team/style_refs/existing_exteriors_contact.jpg` and `existing_interiors_contact.jpg`. The new art must be clearly over the top, its palette must dominate, and it must not resemble any existing plate.
4. **Firefly first. ChatGPT image generation is allowed too** (author, 2026-11-13 evening). Close any payment or upgrade dialog with its X, and never pay. Only one agent at a time may use ChatGPT. **Two image agents never share Firefly.** Firefly's Generations history is shared, so results interleave and agents can grab each other's images. When the orchestrator runs two painters, one uses Firefly and the other uses ChatGPT, each in a fresh chat. Your brief says which.
   - Use the home screen https://firefly.adobe.com/: **GPT Image 2.6 Sunburst** (the author's chosen model; Firefly lists it now; fall back to 2.5 Sunburst only if 2.6 is missing), High, 16:9, 2K.
   - **Start every prompt with your building's plain name**, e.g. "Euro Ink 4 Less tattoo parlour exterior, ...", or for a relight "Euro Ink 4 Less night relight: ...". Firefly names each download after the prompt's first words.
   - Save with the Download button, then MOVE the file out of `C:\Users\heirr\Downloads`. **Touch only files whose names begin with your building's name.** Never delete or move anything else there; other agents share that folder, and two agents have already lost files this way.
   - Put no id tags in prompts. Take the result from your own tab's result panel. Never use refs that aren't yours.
   - **Day** is daylight, but **overcast, flat or harsh light is allowed and preferred**. A blue sky appears only if the plan asks for it. Neon reads faint. Never golden hour, sunbeams or a postcard sky.
   - **Prompts** (QC owner, 2026-11-14):
     - Open with the building name, then the plan's seedy props and its one exaggeration. Put the style boilerplate LAST.
     - Every prompt carries the standing ban list: no golden hour, sunbeams, flower boxes, potted plants, trees, moss, candle-lit windows, half-timbering or storybook lean.
     - Avoid "ancient", "quaint", "charming", "cosy", "tavern", "candlelight", "historic" and "traditional" unless the doc names them.
     - Save every prompt you send as `dev/asset_team/prompts/<id>_<n>.txt` and commit them.
     - Never build on an old or failed plate: generate fresh.
   - **A1.5 seediness check:** after your FIRST day plate, save a 512 px thumbnail as `dev/asset_team/reviews/<id>_a15_thumb.jpg` and send `main` "A1.5 READY <id>". Then wait. Do no night, elevation or lettering work until main passes it. A fail means a fresh generation, not an edit.
   - **Night**: Gemini 3.1 "Use as reference" on your day result. Register it to the day plate (`Tools/content_generation/absinthe_arcade/hd2d/register_to.py`) and resize it to the day plate's exact size.
   - **Exterior** = day + night + front elevation (straight-on orthographic facade filling the canvas, no frame), all at least 2048 wide.
   - **Interior** = one walkable room per plate, high three-quarter camera. No checkerboard floor unless the doc says so.
   - If a Gemini edit won't change the framing, outpaint a padded copy.
   - No people. Signs: doc text only, spelled exactly; zoom in on every word, and fix it by a local edit or make it illegible. No real place names anywhere. At most 3 rounds per deliverable.
5. **Deliver** (overwrite at the same paths):
   - `game/assets/worlds/<city>/<id>/exterior/<id>_ext_day.png`, `_ext_night.png`, `_ext_front_elevation_day.png`
   - `.../interior/<id>_int_day.png`, `_int_night.png`. Extra rooms are `<id>_int_<node>_day.png` / `_night.png`.
   - Review sheets `dev/asset_team/reviews/<id>_ext_review.jpg` / `<id>_int_review.jpg`, at most 1600 wide.
6. **Commit** only your files, message `art(<city>): <Name> to approved plan (asset team)`, ending with the two attribution lines the orchestrator gave you. Do not merge or push.
7. **Problems.** Never close the last tab in the shared MCP tab group: closing it deletes the group and resets every other agent's tab. When you finish, navigate your tab to about:blank instead of closing it if it's the only one left. If your tab group vanishes, send `main` "BROWSER RESET" and wait. If Chrome reports screenX about -21333, send `main` "CHROME MINIMIZED" and wait. Questions go per brief section 6. Clean up per section 7.
8. **QC.** After you report, a fresh blind reviewer checks your plates against `dev/asset_team/QC.md` Checklist L (gate A2). It reads every word letter by letter and checks palette, plan items, camera, no people, and no look-alikes. Self-check against Checklist L before you report. A fail comes back to you to fix.
9. **Report** in under 200 words: how each plan line was met (palette hexes and where they show, satire beats visible), every sign as rendered, anything you couldn't match, and cleanup.

> **SHAMSTERDAM NAMES (hold LIFTED 2026-11-13, bead Eurobound-ucpf):** the author picked every new Shamsterdam name. The final old→new map is `WritingRoom/tasks/shamsterdam_rename_final_map.md`, covering places, titles, items, events and the 36 sign lines, all in English.
> - On Shamsterdam art, every player-visible word comes from the map's NEW column, spelled exactly, and is checked at zoom. That covers signs, fascias, menus and notes.
> - The only Dutch kept is De Pauze, Meester Overhang and Opa Cees. Locals' Dutch first names stay too.
> - Never paint an old Dutch name. Where the map has nothing for a word, leave it blank or illegible and tell the orchestrator.
> - File names and engine ids do not change.
> - The Safe-Crossing's corner stays empty: its NPC still needs a ruling.
