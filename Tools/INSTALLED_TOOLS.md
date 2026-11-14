# Installed tools

What was added to the project and to this computer on 2026-11-14 under bead Eurobound-f8rw. The author asked, verbatim: "Install any free hooks skills and plugins you find that are free and you feel will benefit our team", and later: "Anything else you would like us to install to help our team? anything free? ... like apps or extensions or plugins for our current apps. You have my permission to install them".

Everything here is free, needs no account and no API key, has a licence that allows commercial game use, and does not filter content. Nothing was paid for. Candidates came from `docs/research/2026-11-14-plugin-and-skill-scout.md`.

**Check after install:** Godot 4.7.2 import clean; GUT suite 770 of 770 passing (62 scripts, 9,910 asserts) with both addons enabled.

## 1. Godot addons (in the repo, enabled)

Both are enabled in `game/project.godot`. That file was clean in git before the edit.

### LimboConsole

- **What it is:** a debug console inside the running game. Press the backtick key (`` ` ``, left of 1) and type commands.
- **Version:** 0.8.0 (2026-06-20). **Source:** https://github.com/limbonaut/limbo_console/releases/tag/v0.8.0
- **Licence:** MIT (`game/addons/limbo_console/LICENSE.md`). Its bundled Monaspace fonts are SIL Open Font License 1.1.
- **Godot 4.7:** the project says Godot 4.3 or newer. Verified here by import and the test suite on 4.7.2.
- **Who uses it:** gameplay, QA and any session that tests the game by hand.
- **What it changed:** folder `game/addons/limbo_console/`; in `project.godot` an autoload `LimboConsole`, a plugin entry, and three input actions (`limbo_console_toggle`, `limbo_auto_complete_reverse`, `limbo_console_search_history`).
- **Not done yet:** it has only its built-in commands, and it is not yet switched off for release builds. Both are bead Eurobound-08bo.
- **Remove it:** in the Godot editor, Project > Project Settings > Plugins, untick LimboConsole. Then delete `game/addons/limbo_console/` and the three `limbo_*` actions in the `[input]` section of `game/project.godot`.

### Controller Icons

- **What it is:** shows the right button picture for whatever the player holds (Xbox, PlayStation, Switch, Steam Deck, keyboard and mouse) and swaps it when they change device.
- **Version:** 3.1.8 (2026-07-28). **Source:** https://github.com/rsubtil/controller_icons/releases/tag/v3.1.8
- **Licence:** code MIT (`game/addons/controller_icons/LICENSE`). Icon art is Xelu's free prompt set, CC0 (public domain), as stated in the project README.
- **Godot 4.7:** the project says Godot 4.1.2 or newer. Verified here by import and the test suite on 4.7.2.
- **Who uses it:** the UI session, when it builds button prompts and menus.
- **What it changed:** folder `game/addons/controller_icons/` (only the addon folder; the demo was left out); in `project.godot` an autoload `ControllerIcons` and a plugin entry.
- **Not done yet:** nothing in the game uses it. The icon style is generic and may be repainted later.
- **Remove it:** untick Controller Icons in the Plugins list, then delete `game/addons/controller_icons/`.

## 2. Desktop tools (on this computer, not in the repo)

None of these needed administrator rights. The four "portable" ones are plain folders under `%LOCALAPPDATA%\Programs\eurobound_tools\`. They are **not on PATH**; call them by full path. The two winget ones are on PATH for new terminals.

| Tool | Version | What it's for | Who uses it | Licence | Where / how to run | Remove it |
|---|---|---|---|---|---|---|
| **ImageMagick** | 7.1.2-34 Q16-HDRI, portable | Batch image checks and conversions: sizes, alpha, formats, contact sheets | Asset teams, art cleanup | ImageMagick licence (Apache-style) | `%LOCALAPPDATA%\Programs\eurobound_tools\imagemagick\magick.exe` | Delete the `imagemagick` folder |
| **oxipng** | 10.2.1 | Makes PNGs smaller with no quality loss | Asset teams; bears on the binary-size bead Eurobound-8ia | MIT | `oxipng` (winget) | `winget uninstall --id Shssoichiro.Oxipng -e` |
| **pngquant** | 2.17.0 | Makes PNGs much smaller by reducing colours (lossy; check the result by eye) | Asset teams; Eurobound-8ia | GPL v3 (it is a tool we run; the images stay ours) | `%LOCALAPPDATA%\Programs\eurobound_tools\pngquant\pngquant.exe` | Delete the `pngquant` folder |
| **Material Maker** | 1.7 | Procedural PBR materials. A possible free stand-in for ArmorPaint in step 8 of the texturing protocol | 3D asset and texturing sessions | MIT | `material_maker` (winget) | `winget uninstall --id RodZill4.MaterialMaker -e` |
| **Audacity** | 4.0.2, portable | Editing and trimming sound effects and audio | Audio session | GPL v3 | `%LOCALAPPDATA%\Programs\eurobound_tools\audacity\bin\Audacity4.exe` | Delete the `audacity` folder |
| **rFXGen** | 5.0 | Retro sound-effect generator with a command line | Audio session; today's SFX are hand-synthesized in Python | zlib | `%LOCALAPPDATA%\Programs\eurobound_tools\rfxgen\rfxgen.exe` | Delete the `rfxgen` folder |

Sources: [ImageMagick 7.1.2-34](https://github.com/ImageMagick/ImageMagick/releases/tag/7.1.2-34), [oxipng](https://github.com/oxipng/oxipng), [pngquant](https://pngquant.org/), [Material Maker 1.7](https://github.com/RodZill4/material-maker/releases/tag/1.7), [Audacity 4.0.2](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.2), [rFXGen 5.0](https://github.com/raysan5/rfxgen/releases/tag/5.0).

Notes:

- **ImageMagick and Audacity are the portable builds**, because their normal installers ask for an administrator password. The portable ImageMagick folder is called by full path on purpose: it also contains `compare.exe` and similar names that should not shadow other programs.
- **Material Maker export targets** (read from its own material definitions): Godot 4 Standard, Godot 4 ORM, Godot 3 Spatial, Blender, glTF plane, Unity (3D, URP, HDRP), Unreal 4 and 5. It started correctly on this machine (it is itself built on Godot 4.7) and used about 1.4 GB of memory, so close it when done.
- **rFXGen command line:** `rfxgen.exe -g coin -o out.wav` makes a sound from a preset (coin, laser, explosion, powerup, hit, jump, blip). It also converts `.rfx` files to `.wav`. Tested: it wrote a coin sound.
- **pngquant 2.17.0** is from 2021. It is the newest official Windows build; newer versions are source only.
- **Audacity** opened and was closed again. Its optional cloud features need an account; we don't use them.

## 3. Already present, confirmed

- **Ucupaint** (Blender layer painting): version 3.0.0 is in Blender 5.2's extensions folder. The newest is 3.0.1; update from inside Blender when convenient.
- **ffmpeg, gh, winget, shellcheck, uv**: already installed before this work.

## 4. Hooks

No hook was installed and `.claude/settings.json` was not touched. `Tools/orchestrator/HOOKS_PROPOSAL.md` proposes three, waiting on the author's Desk answer (`Eurobound-nwqs-q1`): a commit guard, a GUT guard, and a bead-page reminder.

## 5. Left out and why

**Godot**

- **GodotSteam.** Free (MIT), but not installed. The release that names Godot 4.7.2 is a replacement Godot editor, not an addon; the drop-in addon build says only "Godot 4.4 and up". It also needs a Steam app id to test. Bead Eurobound-iflo.
- **Maaack's Game Template** (menus). Free and states Godot 4.7, but the title screen and menus are the author's design call. Bead Eurobound-beef.
- **Quest, inventory, save and scene-switching addons** (QuestSystem, GLoot, SaveKit, Scene Manager and others). They duplicate `game/core`, which stays ours.
- **GUT update** (9.4.0 to 9.6.1). An update to the test addon could change test results; it deserves its own bead and test run, not a side effect of this one.
- **Godot export templates and the Steamworks SDK.** Not needed until we make release builds.
- **gdtoolkit** (GDScript style checker). Last release is a year old and does not state Godot 4.7 support.

**Claude Code skills**

- **No skill was installed.** The project already carries 309, and the scout's housekeeping note is that there are too many.
- **segment-anything-model skill** (MIT, plain markdown). Read and left out: it documents the first SAM, while the Sprite Development Team is building on SAM 2.1 with a different API, so it would mislead more than help.
- **cc-blender-skill, mcp-for-blender, Coding-Solo/godot-mcp.** Duplicates of what we run. The last two also add tool servers, which this task may not do.
- **awesome-gamedev-agent-skills 2.0.0 update.** A major version that may rename skills in use.
- **ElevenLabs sound skill.** Paid, needs an API key.

**Blender**

- **No Blender addon was installed.** The scout rated none "worth trying" for baking, UV work or toon shading. QRemeshify and TexTools are not confirmed for Blender 5.2; Quad Remesher is paid; Principled Baker is dead. Blender's own Decimate, QuadriFlow and Bake cover the need.

**Other**

- **SAM / sam2.** The Sprite Development Team installs it in `tools/paint_zones/.venv`.
- **Modddif, ArmorPaint.** Paid, or need a multi-gigabyte compiler install (Visual Studio), which waits on the author's Desk answer (Eurobound-kj21).
- **ImageMagick and Audacity system-wide installers.** They need an administrator click. The portable builds do the same job.

**Free things that might be worth adding later (not installed)**

- **Depth Anything V2 Small** (Apache-2.0): depth maps from painted plates. A timed test, per the scout.
- **gltfpack / meshoptimizer** (MIT): shrinks 3D files before Godot, if props get heavy.
- **Kenney audio packs and the Sonniss GDC bundle**: free sound libraries (content, not tools) for when audio starts.
- **Krita** (GPL): free painting program, if the author wants one for hand-painted distress.
- **Git LFS**: only if Eurobound-8ia rules that way.
