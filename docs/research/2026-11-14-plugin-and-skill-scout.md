# Plugin and skill scout

Date: 2026-11-14. Bead: Eurobound-j5dp. Requested by the author: "send an agent to scout for other plugins and skills that would benefit our game development or asset development".

**Nothing was installed and no setting was changed.** This is a shopping list with opinions. Every item needs your say before anyone installs it.

## The short version

- We are already well equipped. Most of the popular Godot addons for save files, quests, inventory and scene switching would duplicate code we have already written (`game/core/save_system.gd`, `quest_log.gd`, `scene_router.gd`, `data_repo.gd`). I recommend skipping those.
- The real gaps are in **shipping polish** (Steam, menus, controller button pictures, a debug console) and in the **paint-zones tool** the Sprite Development Team is building.
- There is **no ready-made HD-2D kit for Godot**. I searched twice and found none. Our own tilt-shift shader plus Godot's built-in depth of field is the route.
- Everything in the top ten is free. Items that cost money or need an account are flagged in the tables.
- One housekeeping finding that costs nothing: we carry a lot of skills and plugins for other engines (see "Housekeeping" at the end).

## Top ten, ranked

| # | Candidate | What it gives us | Verdict |
|---|---|---|---|
| 1 | **GodotSteam** | Steam achievements, cloud saves, overlay, Steam Deck input | Worth trying (when Steam work starts) |
| 2 | **Maaack's Game Template** (menus part) | Main menu, options, key rebinding, pause, credits | Worth trying |
| 3 | **Controller Icons** | Correct button pictures for Xbox, PlayStation, Switch, Steam Deck, keyboard | Worth trying |
| 4 | **LimboConsole** | A type-in debug console inside the running game | Worth trying |
| 5 | **GeoSAM2** (with SAM 2.1 underneath) | Click one part of a 3D model in one view, get that part marked on the whole mesh | Worth trying, as a short timed test |
| 6 | **A GDScript check after every edit** (Godot's own checker; optional gdtoolkit) | Agents catch broken scripts straight away | Worth trying |
| 7 | **Depth Anything V2 (Small)** | A depth map from a painted plate, to help cut layers and place blur | Worth trying, as a short timed test |
| 8 | **Free sound sources**: Kenney audio, Sonniss GDC bundle, jsfxr, ChipTone | Sound effects with no fee and no account | Worth trying (when audio starts) |
| 9 | **rembg on the graphics card / BiRefNet** | Faster, cleaner background removal in `tools/art_cleanup` | Maybe later |
| 10 | **TRELLIS.2 or Pixal3D** | Image-to-3D on our own machine, no Tripo credits | Maybe later (unproven on 8 GB) |

Reasons and risks for each are in the sections below.

## 1. What we already have

**Claude Code setup**
- `.mcp.json` connects one tool server: Godot MCP Pro (paid licence, already bought).
- `.claude/` holds 309 project skills, 49 agent definitions, 13 hooks (session start/end, commit and push checks, asset checks) and 11 rule files.
- Turned on for your account: superpowers, code-review, playwright, context7, hookify, claude-code-setup, the Blender skills plugin (22 Blender skills), plus unity and supabase.
- Also connected this session: the official Blender tool server, a Tripo tool server, PixelLab.

**Godot addons in `game/addons/`**

| Addon | Our version | Newest | Note |
|---|---|---|---|
| Dialogue Manager | 4.2.0 | 4.2.0 (2026-10-30) | Up to date |
| Phantom Camera | 0.11.0.4 | 0.11.0.4 (2026-10-27) | Up to date |
| Aseprite Wizard | 9.8.0 | 9.8.0-4 (2026-03-03) | Up to date |
| GUT (tests) | 9.4.0 | 9.6.1 (2026-07-09) | Update available |
| LimboAI | not checked | 1.8.1 (2026-08-20) | |
| NoClipBillboardSprite3D | no version listed | | |
| Godot MCP Pro | 1.17.1 | | Paid, already owned |

**Our own tools in `Tools/`**: char3d (pose, render, contact sheets), item3d, art_cleanup (uses rembg), canon_index, beads_board, blender_notes, validate_data, sprite_pipeline (old pixel route). `Tools/paint_zones/` exists and is empty.

**Blender 5.2** with Ucupaint, the official Blender MCP add-on, the Tripo bridge add-ons and our Claude Notes add-on.

**In the game already**: our own save system, quest log, scene router, data repository, game clock, and one tilt-shift shader. Three audio files.

## 2. Claude Code skills, plugins and tool servers

Found with the `find-skills` skill (skills.sh search), the `claude-automation-recommender` skill, and web search.

| Candidate | What it does for us | Who uses it | Licence / cost | Maintained | Risk | Verdict |
|---|---|---|---|---|---|---|
| **GDScript check hook** using Godot's built-in script checker | After an agent edits a `.gd` file, Godot checks it and reports errors at once. None of our 13 hooks does this today. | All coding sessions | Free, nothing to install | Part of Godot | Small: adds a second or two per edit | **Worth trying** |
| [gdtoolkit](https://github.com/Scony/godot-gdscript-toolkit) (gdlint, gdformat) | Style checker and tidy-up for GDScript | Coding sessions | MIT, free | Last release 4.5.0, 2025-10-09. A year old; Godot 4.7 support not stated | May choke on newer GDScript syntax | Maybe later |
| GDScript language-server plugins ([minami110/claude-godot-tools](https://skillselion.com/plugin/minami110/claude-godot-tools), [PurpleJelly gdscript-lsp](https://purplejelly.itch.io/gdscript-lsp), [bognari gdscript-lsp](https://claudepluginhub.com/plugins/bognari-gdscript-lsp)) | Lets Claude ask Godot "where is this function used" and get live errors | Coding sessions | MIT, free | Small community projects; one is marked as a dev version; bognari's was tested on Godot 4.6.3 | Needs the Godot editor open; we already get much of this from Godot MCP Pro | Maybe later |
| [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | The Godot skill pack | All | Apache-2.0, free | v2.0.0 on 2026-11-11 | **Already installed.** An update exists; a major version may rename things | Maybe later (update) |
| [segment-anything-model skill](https://skills.sh/orchestra-research/ai-research-skills/segment-anything-model) | A how-to for using SAM from code | Sprite Development Team | Free; about 1,100 installs | Not checked | It is only instructions; read before trusting | Maybe later |
| [cc-blender-skill](https://github.com/RobLe3/cc-blender-skill) | Blender how-to skills | 3D sessions | MIT, free | v1.4.0, 2026-10-12 | Duplicates the 22 Blender skills we already have | Skip |
| [mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) (community, formerly blender-mcp) | Lets Claude drive Blender | 3D sessions | MIT, free | Active (2026-11-13) | Duplicates the official Blender MCP we already run | Skip |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Free Godot tool server | Coding sessions | MIT, free | Last change 2026-04-16 | Duplicates Godot MCP Pro, with fewer tools | Skip |
| [comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server) | Lets Claude run local image models through ComfyUI | Asset team | Apache-2.0, free | v1.1.1, 2026-02-17 | Only useful if we adopt ComfyUI (see section 5) | Maybe later |
| [ElevenLabs sound-effects skill](https://skills.sh/elevenlabs/skills/sound-effects) | Text-to-sound-effect | Audio | **Paid service, needs an API key** | Active | Ruled out by the no-paid-API rule; hosted services also apply their own content rules | Skip |

Note on the official Blender MCP: Blender's own page warns that it runs AI-written code inside Blender with no safety checks ([comparison article](https://www.strayspark.studio/blog/official-blender-mcp-server-comparison-2026)). We already use it; the advice is simply to keep `.blend` backups.

## 3. Godot 4 addons

Dates are from each project's GitHub page, read on 2026-11-14.

### Shipping and polish

| Candidate | What it does for us | Who uses it | Licence / cost | Maintained | Risk | Verdict |
|---|---|---|---|---|---|---|
| [GodotSteam](https://codeberg.org/godotsteam/godotsteam) | Connects the game to Steam: achievements, cloud saves, overlay, rich presence, Steam Input | Release and gameplay sessions | MIT, free. Steam itself charges a one-time fee per game (about 100 USD) when you publish | v4.24, 2026-11-08. Source moved to Codeberg; the GitHub copy is archived. Its notes mention a fix for a Godot 4.7 change, so 4.7 is being followed | It is a compiled add-on; each Godot update needs a matching GodotSteam build | **Worth trying** when Steam work starts |
| [Maaack's Game Template](https://github.com/Maaack/Godot-Game-Template) | Ready main menu, options (sound, video, key rebinding), pause menu, credits, loading screen | UI session | MIT, free | v1.7.1, 2026-10-29. States "for Godot 4.7" | It also brings its own scene loader and music controller, which overlap our `scene_router`. Turn on only the menu parts. Its look must be re-skinned to ours | **Worth trying** |
| [Controller Icons](https://github.com/rsubtil/controller_icons) | Shows the right button picture for whatever the player is holding, and switches on the fly | UI session | Code MIT; icon art CC0 (Xelu's set). Free | v3.1.8, 2026-07-28; active October 2026. Needs Godot 4.1.2 or newer | Icon style is generic; we may want to repaint them later | **Worth trying** |
| [Godot Input Helper](https://github.com/nathanhoad/godot_input_helper) | Device detection and rebinding helpers, by the Dialogue Manager author | UI session | MIT, free | v4.7.0, 2025-06-08. Quiet for 17 months | Overlaps items 2 and 3 | Maybe later |
| [Keychain](https://github.com/Orama-Interactive/Keychain) | Key-rebinding screen | UI session | MIT, free | No releases; last change 2026-02 | Covered by Maaack's template | Skip |
| In-game localisation | Godot has translation tables built in, and Dialogue Manager and our `localize` skill already work with them | Writers, UI | Free | Built in | None | Use what we have; no addon needed |

### Developer tools

| Candidate | What it does for us | Who uses it | Licence / cost | Maintained | Risk | Verdict |
|---|---|---|---|---|---|---|
| [LimboConsole](https://github.com/limbonaut/limbo_console) | Press a key in the running game and type commands such as "give 500 SOVS" or "jump to the Arcade". Speeds up testing a lot | All gameplay and QA sessions | MIT, free | v0.8.0, 2026-06-20; active November 2026. Same author as LimboAI, which we already trust | Must be switched off in the shipped game | **Worth trying** |
| [Panku Console](https://github.com/Ark2000/PankuConsole) | Same idea, more features | Same | MIT, free | Last release 2024-07; no changes since 2025-01 | Stale | Skip |
| [Debug Menu](https://github.com/godot-extended-libraries/godot-debug-menu) | On-screen frame-rate and timing graphs | Performance checks | MIT, free | Last release 2023-12; minor changes in 2025 | Old but tiny | Maybe later |
| [gdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) | A second test framework | QA | MIT, free | v6.2.3, 2026-11-01 | We already use GUT; two frameworks is confusion | Skip |

### Game systems (mostly duplicates of what we wrote)

| Candidate | What it does | Licence / cost | Maintained | Verdict and why |
|---|---|---|---|---|
| [QuestSystem](https://github.com/shomykohai/quest-system) | Quest tracking | MIT, free | v2.0.2.4, 2026-08-05; Godot 4.4+ | Skip. We have `quest_log.gd` |
| [Questify](https://github.com/TheWalruzz/godot-questify) | Quest graph editor | MIT, free | Last release 2025-07 | Skip |
| [GLoot](https://github.com/peter-kish/gloot) | Inventory system | MIT, free | v3.0.2, 2026-07-05 | Maybe later. Only if our own item handling becomes a burden |
| [Expresso Inventory System](https://github.com/expressobits/inventory-system) | Inventory with crafting | MIT, free | 2.13.0, 2026-03-21 | Skip. More than we need |
| [Pandora](https://github.com/bitbrain/pandora) | Item and enemy database editor | MIT, free | No formal releases; last change 2026-08 | Skip. We have `data_repo` and validated JSON |
| [SaveKit](https://store.godotengine.org/asset/fernforestgames/savekit/) and other save addons | Save and load | MIT, free | New (2026-04) | Skip. We have `save_system.gd` |
| [Scene Manager](https://github.com/glass-brick/Scene-Manager) | Scene transitions | No licence file found | v2.1.0, 2026-08-20 | Skip. We have `scene_router.gd`, and the licence is unclear |
| [Godot State Charts](https://github.com/derkork/godot-statecharts) | State machines | MIT, free | v0.22.5, 2026-06-26 | Skip. LimboAI already includes state machines |
| [Sound Manager](https://github.com/nathanhoad/godot_sound_manager) | Music cross-fades and pooled sound effects | MIT, free | Last release v2.6.2, 2024-04; small changes in 2026 | Maybe later. Decide when the audio session starts |
| [Resonate](https://github.com/hugemenace/resonate) | Audio manager | MIT | **Archived** | Skip |

### HD-2D look

There is no maintained HD-2D kit for Godot 4. What exists:

| Candidate | What it does for us | Licence / cost | Verdict |
|---|---|---|---|
| Godot's built-in depth of field (camera attributes, works in Forward+) | Near and far blur without any addon | Free, built in | Use it alongside our tilt-shift shader |
| [godotshaders.com](https://godotshaders.com/) | Single shaders to borrow: sprite outline for 3D billboards, ambient shadowing | Per shader; many are CC0 or MIT. Check each one | Maybe later, one shader at a time |
| [GDQuest godot-shaders](https://awesome.ecosyste.ms/projects/github.com%2Fgdquest-demos%2Fgodot-shaders) | Shader collection with demos | Free | Maybe later. Its Godot 4 port is incomplete |
| [Laigter](https://github.com/azagaya/laigter) | Makes "normal maps" from flat images so 2D art reacts to light | GPL-3.0 tool, free; images it makes are ours. v1.14.0, 2026-08-07 | Maybe later. Our characters are now 3D renders, and Blender can output the same thing directly |
| [Debug Draw 3D](https://github.com/DmitriySalnikov/godot_debug_draw_3d) | Draws helper lines in 3D scenes | Free; v1.7.3, 2026-04 | Maybe later |

## 4. Blender addons and paint-zone tools

### For `tools/paint_zones/` (bead Eurobound-nhxz.1)

| Candidate | What it does for us | Licence / cost | Maintained | Risk | Verdict |
|---|---|---|---|---|---|
| [GeoSAM2](https://github.com/VAST-AI-Research/GeoSAM2) | Does almost exactly what the bead describes. It renders a model from 12 angles with Blender, you click a part in one view, and it marks that part on every face of the mesh. Made by the research arm of the company behind Tripo | Code Apache-2.0, free. **Licence of the downloadable model file is not stated on the page; check before use** | Published 2026; last change 2026-05-07; only 70 stars | Lists Linux only, so Windows may need extra work. Memory need not stated. Small project, could go quiet | **Worth trying** as a half-day test on one bro. If it works it replaces most of what the team would otherwise write |
| [SAM 2 / 2.1](https://github.com/facebookresearch/sam2) | The underlying "click a thing in a picture, get its outline" model. Works on single renders | Apache-2.0, free | Meta; last change 2026-05-30 | Low. The small versions fit an 8 GB card comfortably (from general knowledge, not measured here) | **Worth trying**. The safe base for the tool |
| [SAM 3](https://github.com/facebookresearch/sam3) | Newer: you can type "the jacket" instead of clicking | Meta's own "SAM License": free, commercial use allowed, with conditions ([summary](https://roboflow.com/model-licenses/segment-anything-3)) | Active (2026-11-13) | Reports put it at 8 to 12 GB, so our card is borderline | Maybe later |
| [MobileSAM](https://github.com/ChaoningZhang/MobileSAM) | A tiny, fast SAM | Apache-2.0, free | Last change 2026-05 | Rougher outlines | Maybe later (fallback) |
| [SAMPart3D](https://github.com/Pointcept/SAMPart3D) | Splits a 3D model into parts by itself | MIT, free | Last change 2025-05 | Heavy to set up, likely too big for 8 GB | Skip |
| [PartField](https://github.com/nv-tlabs/PartField) | Same idea, from NVIDIA | NVIDIA's own licence; **may bar commercial use, check** | Last change 2026-06 | Licence | Skip unless the licence clears |
| [Hunyuan3D-Part](https://github.com/Tencent-Hunyuan/Hunyuan3D-Part) | Same idea, from Tencent | Tencent community licence; reported to exclude the EU, UK and South Korea | Last change 2025-12 | Licence | Skip |

### Mesh clean-up, baking, shading, rendering

| Candidate | What it does for us | Licence / cost | Maintained | Risk | Verdict |
|---|---|---|---|---|---|
| Blender's built-in Decimate, QuadriFlow remesh and Bake | Reduce triangle count, rebuild tidy geometry, bake textures. All scriptable, so they fit our headless scripts | Free, built in | Blender 5.2 | None | Use these first |
| Ucupaint | Layered texture painting, with its own baking | GPL-3.0, free | [v3.0.1, 2026-11-01](https://extensions.blender.org/add-ons/ucupaint/) | None | Already used. Up to date |
| [QRemeshify](https://github.com/ksami/QRemeshify) | Turns Tripo's triangle soup into clean four-sided faces; better results than the built-in | GPL-3.0, free | Last release 1.1.0, 2024-10. Says Blender 4.2+; 5.x not confirmed | May not load in 5.2 | Maybe later |
| [Quad Remesher](https://exoside.com/) and Quadify Premium | Commercial remeshers | **Paid** | Quadify lists Blender 5.2 | Cost | Skip |
| [TexTools](https://github.com/franMarz/TexTools-Blender) | UV layout and baking helpers | GPL, free | Last release 2024-03 | Stale; Blender 5 unconfirmed | Maybe later |
| [Principled Baker](https://github.com/danielenger/Principled-Baker) | One-click bake | Free | Last change 2023 | Dead | Skip |
| [Malt / BEER](https://github.com/bnpr/Malt) | A separate cartoon-style renderer for Blender | Free | 2026-03 | Would replace the toon look in `char3d/look.py`, which already works in EEVEE | Skip |
| [meshoptimizer (gltfpack)](https://github.com/zeux/meshoptimizer) | Shrinks 3D files before they go into Godot | MIT, free | v1.3, 2026-09-25 | Low | Maybe later, if in-game 3D props get heavy |
| [Mesh2Motion](https://github.com/Mesh2Motion/mesh2motion-app) | Free rigging and animation in the browser, a Mixamo alternative | Free; licence terms not read, check | Active (2026-11-11) | Unknown fit with our shared rig | Maybe later |
| [Rokoko add-on](https://github.com/Rokoko/rokoko-studio-live-blender) | Copies an animation from one skeleton to another | LGPL, free; **may ask for a free account** | v1.4.4, 2026-11-12 | `char3d/shared_motion.py` may already cover this | Maybe later |
| Batch rendering | We already render from the command line with our own scripts | Free | | | Nothing needed |
| [Dream Textures](https://github.com/carson-katri/dream-textures) | AI image generation inside Blender | GPL-3.0, free | Last release 2024-08 | Stale; tight on 8 GB | Skip |

## 5. Free models that run on our own machine (RTX 5060, 8 GB)

Local models have no fee, no API key and no content filter of their own.

| Candidate | What it does for us | Licence / cost | Fits 8 GB? | Verdict |
|---|---|---|---|---|
| SAM 2.1 (small) | Paint zones, cut-outs | Apache-2.0 | Yes | **Worth trying** (see section 4) |
| [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2), Small model | Estimates how far away each part of a painting is. Could help cut a painted plate into layers and place blur | Small model Apache-2.0. **The larger models are non-commercial; use Small only** | Yes | **Worth trying** as a test on one Arcade plate |
| [rembg](https://github.com/danielgatis/rembg) on the graphics card, or [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) | Background removal. `art_cleanup` uses rembg on the processor today; the card would be faster, BiRefNet cleaner on hair and edges | MIT | Yes | Maybe later |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Enlarges images | BSD-3 | Yes | Maybe later. Old (2022) but still standard |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | Image to 3D model, locally, no Tripo credits | MIT | **Disputed.** Guides claim anything from 6 GB to 24 GB ([low-memory guide](https://trellis2.app/blog/trellis-2-low-vram), [contrary figure](https://www.codesota.com/news/trellis-2-3d-generation)) | Maybe later. Could cut Tripo spend, but unproven on our card |
| [Pixal3D](https://huggingface.co/TencentARC/Pixal3D) | Newer image-to-3D built on TRELLIS.2, has a low-memory switch | Reported MIT | Unconfirmed | Maybe later, same test as above |
| [TripoSR](https://github.com/VAST-AI-Research/TripoSR) | Older, fast image-to-3D | MIT | Yes | Skip. Quality is well below the Tripo website |
| [Hunyuan3D 2 / 2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | Image to 3D | Tencent licence: free under 1M USD revenue, reported to exclude the EU, UK and South Korea | Shape only at about 6 GB; texture needs about 16 GB | Skip (licence and memory) |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | A local workbench that runs image models | GPL-3.0, free | Yes for smaller image models | Maybe later. Only if you want a local alternative to Firefly and ChatGPT images |
| [Stable Audio Open Small](https://huggingface.co/stabilityai/stable-audio-open-small) / Stable Audio 3.0 Small SFX | Text to short sound effect (up to about 11 seconds) | Stability Community Licence: free for commercial use under 1M USD yearly revenue. The 3.0 models also carry Google's Gemma terms | Yes; the Small model even runs without a graphics card | Maybe later. Try after the free sound libraries |
| [MMAudio](https://github.com/hkchengrex/MMAudio), [TangoFlux](https://github.com/declare-lab/TangoFlux) | Other sound generators | Code MIT / unclear; model-file licences not confirmed | Not checked | Skip for now |
| [Ollama](https://github.com/ollama/ollama) with a small language model | A local chat model | MIT | Yes, small models only | Skip. Too weak for our writing or coding |

### Free sound that is not AI

| Source | What it is | Licence |
|---|---|---|
| [Kenney audio packs](https://kenney.nl/assets) | Interface clicks, impacts, jingles | CC0 (public domain) |
| [Sonniss GDC bundle](https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/) | Many gigabytes of professional recordings, new bundle each year | Royalty-free, commercial use allowed, no credit needed |
| [jsfxr](https://github.com/chr15m/jsfxr) and ChipTone | Make retro bleeps in the browser. Fits a 90s parody | jsfxr is Unlicense; ChipTone output reported as CC0 |
| Freesound | Huge library | Mixed. Filter to CC0 only |

Licence details in this table come from guides ([overview](https://app.cinevva.com/guides/free-sound-effects-music)), not from each site's own terms page. Read the terms page before shipping a sound.

## 6. Flags

**Costs money or needs a key or account**
- ElevenLabs skill: paid, API key. Skip.
- Quad Remesher, Quadify Premium: paid. Skip.
- Steam: one-time publishing fee per game. Unavoidable for a Steam release.
- Rokoko add-on: may need a free account.
- The Tripo tool server connected to our sessions and `Tools/char3d/tripo_client.py`: the client file is already marked "DO NOT USE" after your 2026-11-13 ruling. Worth confirming that the Tripo tool server does not spend API credits either.

**Licence needs a human read before use**
- GeoSAM2 model file, PartField, Hunyuan models, SAM 3, Stable Audio, Mesh2Motion, Scene Manager.

**Content filtering**
- Nothing recommended here filters or softens content. Local models do not filter. Hosted AI services apply their own rules, which is one more reason they are marked Skip.

**Not verified today**
- GodotSteam's exact Godot 4.7 build status (its change notes mention 4.7; the main site blocked my reader).
- Memory needs of GeoSAM2, TRELLIS.2 and Pixal3D on an 8 GB card.
- Whether QRemeshify and TexTools load in Blender 5.2.
- The official Blender MCP page blocked my reader; details come from a third-party article.

## 7. Housekeeping (no install needed)

- The project carries 309 skills. A large share are for engines we do not use: Unity, Unreal, Roblox, Bevy, Phaser, Three.js and others. The **unity** and **supabase** plugins are also switched on for your account. Each one adds a line to what every session has to read at start-up. Removing the unused ones would save a little usage in every session and make the right skill easier to pick. This needs your decision; nothing was touched.
- GUT (our test addon) is two versions behind (9.4.0 against 9.6.1).

## Suggested order, if you say yes

1. LimboConsole and the GDScript check hook (small, quick, help every session).
2. A half-day GeoSAM2 test for the Sprite Development Team, with plain SAM 2.1 as the fallback.
3. Maaack's menus and Controller Icons when the UI session starts on menus.
4. GodotSteam when the Steam page exists.
5. Free sound libraries when the audio session starts.
