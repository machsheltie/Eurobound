# sprite_pipeline

Scripts for the character sprite pipeline. The binding spec is
`design/style_guides/character_sprite_pipeline.md` (128x128, semi-realistic, Firefly -> PixelLab -> Aseprite -> Aseprite Wizard). Run from the repo root. Needs Python with `numpy` and `Pillow`.

## Scripts

| File | What it does | Usage |
|---|---|---|
| `pixellab_client.py` | PixelLab v2 API client with subcommands `balance`, `create`, `animate`, `convert`, `rotate`, `correct`, `inpaint`, `fetch`. Key comes from `PIXELLAB_API_KEY` or the `pixellab` MCP server in `~/.claude.json`; it is never printed. | `python tools/sprite_pipeline/pixellab_client.py create --concept sheet.png --desc-file tools/sprite_pipeline/characters/<name>.txt --style "..." --size 128 --out <dir>` (run with `-h` for all options) |
| `remove_baked_shadow.py` | Strips the dithered ground shadow PixelLab bakes under the feet; copies the folder tree, cleaning every PNG. | `python tools/sprite_pipeline/remove_baked_shadow.py <src_dir> <dst_dir>` |
| `carry_master_head.py` | Crops PixelLab animation frames to 128x128 and pastes the approved head from the still frames onto each, so hand-edited faces survive. Renames clips `breathing_idle` to `idle` and `walking` to `walk`. | `python tools/sprite_pipeline/carry_master_head.py <stills_dir> <anim_dir> <out_dir> [--cut 29]` |
| `pack_aseprite.lua` | Packs a character export into one tagged `.aseprite` (tags like `idle_south`). Refuses to overwrite an existing file unless `force=1`. | `Aseprite.exe -b --script-param src=<dir> --script-param out=<file.aseprite> --script-param fps=10 --script tools/sprite_pipeline/pack_aseprite.lua` |
| `bradley_diag_lettering.py` | Bradley-specific: clears (`--blank`, author ruling) or redraws his chest lettering on the diagonal frames. | `python tools/sprite_pipeline/bradley_diag_lettering.py <src_dir> <dst_dir> [--blank]` |

## characters/

Plain-text character descriptions fed to `pixellab_client.py create --desc-file`: `lord_pilsner.txt`, `lord_pilsner_walkbase.txt`, `chadwick.txt`, `bradley.txt`, and the Arcade NPCs (`accounts_receivable`, `ashleigh`, `brynleigh`, `cara`, `jakub_tokens_dvorak`, `kenleigh`, `tomas_two_fifty`, `woo_woo_whitney`).

## Typical order

1. `create` (or `convert` + `rotate`), then `animate`, then `fetch` (PixelLab).
2. `remove_baked_shadow.py` on the export.
3. `carry_master_head.py` against the approved stills.
4. `pack_aseprite.lua`, hand-fix in Aseprite, then import to `game/assets/characters/...` with Aseprite Wizard.

Approved stills live under `Assets/Graphics/sprites/characters/party_members/<bro>/`; see the style guide for the full rules.
