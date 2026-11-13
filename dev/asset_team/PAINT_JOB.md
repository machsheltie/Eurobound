# Paint job: repaint or paint a location to its APPROVED plan

The orchestrator gives you: `id`, `city`, the approved plan file, which parts to paint (exterior, interior, or both), and any author notes. Everything below is binding.

1. **Worktree.** Yours is based on an old commit. READ everything from the main checkout `C:\Users\heirr\Desktop\Hope2_Studio\Eurobound`; WRITE deliverables only inside your worktree. Commit as soon as you have the first day plate, so the worktree is never empty.
2. **Brief.** Read `dev/asset_team/TEAM_BRIEF.md` in full:
   - section 2: parody, plan first, no look-alikes;
   - section 3: Firefly route and saving;
   - 4B/4C: deliverables;
   - 5: quality gates;
   - 7: cleanup.
3. **Spec.** The approved plan is the spec. The author approved it as written, so its "needs approval" questions are settled the way the plan proposes. Read the files the plan cites: the location md, its PNG spec, and its JSONs in core/environment/interactions/items/location_nodes/npcs/sprite_mapping. Look at the current plates if any exist (you are replacing them), and at `dev/asset_team/style_refs/existing_exteriors_contact.jpg` and `existing_interiors_contact.jpg`. The new art must be clearly over the top, its palette must dominate, and it must not resemble any existing plate.
4. **Firefly only** (ChatGPT is retired; never touch its payment dialog).
   - Use the home screen https://firefly.adobe.com/: GPT Image 2.5 Sunburst, High, 16:9, 2K.
   - Save with the Download button, then MOVE the file out of `C:\Users\heirr\Downloads`. Only touch files you downloaded; other agents share that folder.
   - Put no id tags in prompts. Take the result from your own tab's result panel. Never use refs that aren't yours.
   - **Day** is real daylight (blue sky or neutral daylight, neon faint).
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
7. **Problems.** If Chrome reports screenX about -21333, send `main` "CHROME MINIMIZED" and wait. Questions go per brief section 6. Clean up per section 7.
8. **Report** in under 200 words: how each plan line was met (palette hexes and where they show, satire beats visible), every sign as rendered, anything you couldn't match, and cleanup.
