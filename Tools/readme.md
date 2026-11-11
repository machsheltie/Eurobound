# tools

Internal tooling. Run everything from the repo root. Godot project is in `game/`, design docs in `design/`.

| Directory / file | Purpose | Run |
|---|---|---|
| `validate_data.py` | Checks that the vertical-slice JSON files under `game/assets/data/` parse and contain required keys. Exits 1 on failure. | `python tools/validate_data.py` |
| `canon_index/` | Search index over `design/` plus the rulings ledger. | See [canon_index/README.md](canon_index/README.md) |
| `art_cleanup/` | Cleans AI-generated sprites and props before Godot import. | See [art_cleanup/README.md](art_cleanup/README.md) |
| `sprite_pipeline/` | PixelLab client, animation fitting, Aseprite packing for character sprites. | See [sprite_pipeline/README.md](sprite_pipeline/README.md) |
| `content_generation/` | `blockout_absinthe_arcade.py` (glTF blockout generator, `python tools/content_generation/blockout_absinthe_arcade.py [--preview]`) and `absinthe_arcade/` (Blender pipeline). | See [content_generation/absinthe_arcade/README.md](content_generation/absinthe_arcade/README.md) |
| `game_tracking/` | Two GDScript usage examples (`BreweryTracker` progress, couchsurf scene trigger). Reference snippets, not wired in. | Copy into a Godot scene; needs the `BreweryTracker` autoload / a `dialogue_controller` node |
| `godot_mcp_pro_server/` | Godot MCP Pro server (paid, gitignored, reinstall from the purchase zip). Configured through `.mcp.json`. | Started by the MCP client |

## Placeholders (empty files, nothing to run yet)

- `analytics/`: `interaction_logger.gd`, `playtime_tracker.gd`
- `build_scripts/`: `deploy_web.sh`, `export_all_platforms.sh`, `package_demo.sh`
- `data_validation/`: `asset_auditor.py`, `dialogue_checker.py`, `npc_checker.py`
- `content_generation/`: `dialogue_converter.py`, `npc_generator.py`

Each holds only a one-line title comment. Build them out (or delete them) before relying on them.
