# Absinthe Arcade rebuild: team brief

You are one of three Blender agents rebuilding the Absinthe Arcade exterior so it matches the reference as close to pixel-for-pixel as possible. An orchestrator (the main session) assigned you one element, judges your work against the reference, and relays questions to the author. Read this whole file before touching anything.

## Read first (required)

1. `.claude/CLAUDE.md` (project rules; content rules are binding).
2. `design/style_guides/3d_asset_rules.md` (binding 3D rules).
3. `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/mastercomponentbreakdown.md` (the author's component spec).
4. Your element's crops in `dev/aa_team/crops/` (listed in your assignment).
5. The SKILL.md of every blender-agent-skills skill named in your assignment, under `C:/Users/heirr/.claude/plugins/cache/blender-agent-skills/blender-agent-skills/1.1.0/skills/<skill>/SKILL.md`. Always read `blender-core` and `blender-asset-qa`.

## The references

- **The bible:** `Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/absinthearcadedaytime.png` (5248×4796, 48 MB; don't open it directly). Downscaled copy: `dev/aa_team/crops/00_bible_full_1600.png`. Full-res crops per element: `dev/aa_team/crops/0N_*.png`. Need a different crop? Cut it yourself with Pillow from the full PNG (`Image.MAX_IMAGE_PIXELS=None`).
- **Bible beats breakdown.** The breakdown describes the bible. Where its counts or details differ from what the full-res bible shows, build what the bible shows and list the difference in your report (orchestrator ruling from the author's instruction, 2026-10-28).
- **Asset sheet governs the roof and the far right edge (author, 2026-10-28):** the daytime image doesn't define the building's far right side well. The roof and the far right edge (right window column above R1, right corner and quoins, the right side elevation) must match `absinthearcadeassetsheet.jpeg`. Crops: `12_assetsheet_front_right_half.png`, `13_assetsheet_hero_iso.png`, `14_assetsheet_right_side.png`.
- **Secondary:** `.../Exterior/absinthearcadeassetsheet.jpeg` (crops `09_`, `10_`, `11_`). It is only for what the bible doesn't show: mainly the top of the building, the roof and the sides. Where the two disagree, the bible wins.
- The current model: `Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/aa_exterior.blend` (1.7 GB). Current state compared to the bible: `C:/Users/heirr/AppData/Local/Temp/claude/C--Users-heirr-Desktop-Hope2-Studio-Eurobound/a0f53930-8b05-423a-a273-a4bdc0043901/scratchpad/renders/current_preview.png`. The main miss is proportions. The model is a wide, symmetrical palazzo with lots of blank wall. The bible is a narrow three-bay facade: window columns sit tight against the mural, an angled corner bay on the left, and the mural fills the wall.

## Standing rulings (don't relitigate)

- Black cat on the stone sill OUTSIDE the left window directly above the arched window. Canon, never strip it.
- Upper windows are SASH windows: the lower sash only slides up. Q-002 asks the author whether the breakdown's "casement" overrides this. Until answered, don't build opening mechanics.
- No polygon limits. Textures in-scene capped at 4K hero / 2K props.
- Neighbouring buildings (the VÍNA/PIVA/KÁVA cafe, the plaza buildings, the clock tower) are scaffolding. Never build them.
- Player-facing text is exactly what the bible shows. No new names, no new jokes, no new content. Ambiguity goes to the author as a question, never invention.
- Agents build clean base surfaces. Don't paint cracks, grime or weathering (Q-003 pending).
- Unity URP target. 1 unit = 1 m. Street side is −Y.

## Tools and who owns what (avoid collisions)

- Blender 5.2.3: `"C:/Program Files/Blender Foundation/Blender 5.2/blender.exe"`.
- **The live Blender (MCP, port 9877) with aa_exterior.blend open belongs to `mason` (E1) only.** Everyone else works **headless only** (`blender -b ... --python ...`). Never open, save or overwrite `aa_exterior.blend` or its `.blend1` unless you are mason.
- Non-mason agents work in their own file: `Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/<element_id>.blend`. Build it from **re-runnable scripts** in `tools/content_generation/absinthe_arcade/elements/<element_id>/`. To reuse an existing asset from the main file, append only that datablock with `bpy.data.libraries.load(main_blend, link=False)`. Never load the whole 1.7 GB scene into your wip file.
- Model your assets at the world origin in `aa_kit/<asset_id>` collections, per `tools/content_generation/absinthe_arcade/README.md`. Mason places everything at integration.
- **Chrome/Tripo Studio:** only `glazier` may drive the browser in this wave. Others: no browser.
- Render out of process (`blender -b`). Close nothing you didn't open. No orphaned Blender processes: when your background renders finish, confirm with `tasklist | grep -i blender` that only the live session (and its blender-mcp helpers) remain.
- **No git commits.** The orchestrator commits.
- Keep tool output small: redirect Blender logs to a file and tail it.

## Shared dimensions

Mason owns the building's dimensions and publishes them to `dev/aa_team/interfaces.json` (window opening sizes and positions, arch opening, storey heights, facade plane Y, corner bay). Until that file exists:
- Build parametrically. Your script takes widths and heights as parameters, so it can rebuild to mason's numbers without rework.
- Derive proportions from the bible. The doorway is the yardstick: the door opening is the reference width.
Re-read `interfaces.json` before your final render. If it exists, your pieces must fit it exactly.

## Questions: hold, never guess

If anything about what the element should look like is unclear, ambiguous, contradicted between references, or would need you to invent content:
1. Check the rulings first: `docs/superpowers/NEXT_WORK.md`, the breakdown, `.claude/CLAUDE.md`, `design/worlds/debaucheryville/absinthearcade_3d_asset_manifest.md`.
2. If it's still open, call **SendMessage to "main"** with:
   `QUESTION from <agent> on <element>: <one-sentence question>` / `CONTEXT: <what you see, which crop, what conflicts>` / `OPTIONS: A) ... B) ...`
3. Then **stop all work and end your turn** with a final message that starts `HOLDING:` and states which question you are waiting on and what is finished so far. Don't continue on other parts. The orchestrator resumes you with the author's answer.

Author answers (2026-10-28, binding):
- Q-001: three masonry storeys, then the slate mansard from the asset sheet (two dormers, central carved gable, iron cresting, chimneys).
- Q-002: sash windows stand. The lower sash only slides up; the cat's window is posed open. Q-009: one undivided lower pane under the two-pane transom (no centre bar).
- Q-003: build the procedural Voronoi peeling-plaster shader as a starting layer. The author corrects it by hand.
- Q-004: the mural comes from `references/Exterior/muralreference.png` Q-010: use panel 1, the clean artwork. Upscale it to a 4K wall texture and fit it so the fairy, the pixel field and the circuit traces land where the daytime image has them. Remove the painted keystone head and extend any cut-off edges from the daytime image. Panels 4–8 are close-up detail references.
- Q-005: the small corner sign reads `TOKENS / REGRETS`.
- Q-006: the CLOCKTOWER PLAZA hanging sign is in, mounted on the Arcade's left corner.
- Q-011: the building is about 4.0 m deep (the asset sheet's one-bay right side elevation). The interior behind the doors must fit within about 3.4 m.
- The author's main building texture is `references/Exterior/texture.jpg` (seamless peeling limestone, 1254 px).

## Definition of done (every element)

You are done only when your element, rendered from a camera framed like its reference crop, is as close to the crop as you can get. That means the same parts, counts, shapes, proportions, profiles, colours and lettering. Hand in all of the following in `dev/aa_team/renders/<element_id>/`:
1. `final_<view>.png`: renders at ≥1600 px on the long side, EEVEE, daylight similar to the bible (soft overcast and warm), from a camera framed to match the crop. Add a clay version if geometry is the point.
2. `compare_<view>.png`: side-by-side made with Pillow, reference crop on the left, your render on the right, same height.
3. Your own honest diff list: every remaining difference from the crop you can see, and why it remains.
4. Numbers: object count, tris, materials, `ob.dimensions` per asset, the output files, and `qa_check.py` output (blender-asset-qa) with zero unexplained failures.
5. The script paths that rebuild everything from scratch.

Your final message is your report (the orchestrator sees only that). Keep it short: the paths, the numbers, the diff list. The orchestrator compares your compare images to the bible. If they fall short you get a critique and go round again. "Close enough" doesn't pass. Count things: panes, pots, rivets, letters, pixel squares.
