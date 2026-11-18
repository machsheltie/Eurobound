# Handoff: Beads Deployment Team, finish Eurobound-wqui and Eurobound-b8yo (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned one small task and cleared me to edit on top of its own agents' uncommitted changes (c1gt, 7468, 9tz9). **Done. This window can be cleared.** Nothing is running. Godot and GUT were not run. Nothing was committed.

## What was done

- **Eurobound-wqui, closed.**
  - `design/worlds/publandia/environment/cloverleaf_environment.json:216` changed from `path_b_chosen` to `publandia.cloverleaf.path_b_chosen`. This is the author's dotted rule, and the existing event name is kept.
  - The flag is declared in `game/assets/data/world_data/quest_flags.json`: bool, quest, write_once, `quest_id` `publandia_sidequest_eternal_roundabout_01`, `set_by` "NOT BUILT: Path B (Roundabout Residence)".
  - c1gt's `settings.prompt_style` and 7468's `nav_tunnel_visit_rolled` and Marloes line are kept.
- **Eurobound-b8yo, closed.** Dmitri the Exchanger is removed:
  - his `shadow_exchange_dealer` entry in `game/assets/data/npcs/base_profiles/debaucheryville_core.json` (9tz9's Vlad door ids are kept);
  - his character in `npcs/sprite_mappings/debaucheryville_sprites.json` (the `underground_economy.png` sheet now has an empty `characters` list);
  - his `whispered_voice` audio entry.

  Each JSON entry was cut as text, and a check confirmed the parsed file equals the original minus that entry, so no other byte changed. His old dialogue and easter egg are left for Eurobound-rras. A comment on rras lists them, along with the three undeclared flags they use.
- `python -I Tools/validate_data.py`: **0 FAIL** (73 WARN).
- The bead page was synced.

## Uncommitted (this task)

- `cloverleaf_environment.json`
- `quest_flags.json`
- `debaucheryville_core.json`
- `debaucheryville_sprites.json`
- This handoff

The other agents' edits are in the same files.
