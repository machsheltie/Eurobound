# Absinthe Arcade id map (code id to location-file id)

Bead Eurobound-v2bb, 2026-11-14. One table. Code is live and tested, so since this bead the data side uses the code id.
Location files: `interactions/absinthe_arcade_interactions.json` (ia, `object_id`), `location_nodes/absinthe_arcade_location_nodes.json` (nodes),
`environment/absinthe_arcade_environment.json` (env), `items/absinthe_arcade_items.json` (items), `sprite_mapping/absinthe_arcade_sprite_mapping.json` (sm, `interaction_id`).

## Hall (`game/worlds/debaucheryville/absinthe_arcade_interior_hd2d.gd`, `INTERACT_POINTS`)

| Code id | Location-file id (now) | Node (`aa_node_*`) | Was (renamed) |
|---|---|---|---|
| `cabinet_frogger` | `cabinet_frogger` | main_cabinet_loop | `frogger_existential_edition` |
| `cabinet_street_fighter` | `cabinet_street_fighter` | main_cabinet_loop | `street_fighter_identity_crisis` |
| `cabinet_kebab_kombat` | `cabinet_kebab_kombat` | main_cabinet_loop | `kebab_kombat` |
| `ddr_dance_off` | `ddr_dance_off` | main_cabinet_loop | same |
| `token_machine` | `token_machine` | token_exchange | `token_exchange_machine` |
| `skee_ball` | `skee_ball` | main_cabinet_loop | `skeeball_lanes` |
| `foosball` | `foosball` | main_cabinet_loop | `foosball_table` |
| `beanie_baby_claw` | `beanie_baby_claw` | main_cabinet_loop | same |
| `rigged_absinthe_claw_machine` | `rigged_absinthe_claw_machine` | claw_alcove | same |
| `restroom_door` | none in the arcade files (hall exit to the restroom; restroom door `aa_node_restroom_exit` in the restroom files) | (hall left arch) | n/a |
| `prize_counter` | `prize_counter` | bottle_bar | `prize_redemption_counter` |
| `vip_arrows` | `vip_arrows` | bottle_bar | `fake_vip_wayfinding` |
| `bidet_stool` | `bidet_stool` | bottle_bar | `bidet_bar_stool` |

## North wing (`absinthe_arcade_north_wing_hd2d.gd`)

| Code id | Location-file id (now) | Node | Was |
|---|---|---|---|
| `broken_ddr` | `broken_ddr` | broken_ddr | `broken_ddr_restroom_unlock` |
| `maintenance_door` | `maintenance_door` | maintenance_door | `maintenance_restroom_door` |
| `taproom_curtain` | `taproom_curtain` | taproom_curtain | `absinthium_taproom_curtain` |

## Data-only ids (no code `INTERACT_POINTS` id yet)

`mirror_shadow_puzzle`, `club_flyer_panel`, `backpack_girl_couchsurf_hook` (ia ids unchanged).

## Hall lines (`game/assets/data/locations/debaucheryville/absinthe_arcade_hall_lines.json`)

Keys are line groups, not object ids: `vip_arrows` (= the `vip_arrows` hotspot, now also the data id), `bidet_examine` (= `bidet_stool`),
`street_cabinet`, `chalkboard`, `window_cat` (exterior props; sm ids `aa_prop_street_cabinet`, `aa_prop_chalkboard`, `aa_prop_window_cat`), `first_entry`,
`flyer_before`/`flyer_after` (= `club_flyer_panel`), `ambient_barks`, `jakub_sea_monkeys_win` (= `rigged_absinthe_claw_machine`), `quest_objectives`, `grandpa_loss`.

## Maintenance closet (`game/core/closet_props.gd`, `absinthe_arcade_maintenance_closet_hd2d.gd`)

The closet's data files namespace every id with `cmr_` (the cross-location uniqueness convention in
`claw_machine_maintenance_closet_restroom_*`), so these were NOT renamed to the bare code id. Code id to data id is a fixed prefix map:

| Code id (`ClosetProps`) | Data id |
|---|---|
| `ddr_toilet` | `cmr_ddr_toilet` (event `cmr_use_fixture`) |
| `crt_mirror` | `cmr_crt_mirror` (event `cmr_scan_mirror`) |
| `graffiti_smaaaash`, `graffiti_cheat_codes`, `graffiti_tekken_haiku`, `graffiti_pixel_boobs`, `graffiti_joystick_lips` | `cmr_graffiti_wall` (one node, event `cmr_read_graffiti`) |
| `sock_chute`, `sparking_wiring` | no data node yet |
| (data only) | `cmr_inside_door`, `cmr_exit` |

### Split: `cmr_claw_bucket` (2026-11-14)

The old id covered two objects. It is now:
- `cmr_claw_chandelier`: the claw-arm chandelier (keeps all old references, including event `cmr_examine_claw`);
- `cmr_mop_bucket`: the janitor bucket foot soak and cleaning clutter (new node in `location_nodes`; no event, sprite or PNG entry yet).
Files touched: the closet interactions, location_nodes, environment, npcs, sprite_mapping and PNG requirements. Planned asset filename is now `claw_machine_maintenance_closet_restroom_cmr_claw_chandelier.png`.

## Public restroom (`absinthe_arcade_restroom_hd2d.gd`; new files this bead)

No `INTERACT_POINTS` in code yet. Location id `debaucheryville_arcade_public_restroom_01`, files `location_nodes/absinthe_arcade_restroom_location_nodes.json`, `interactions/absinthe_arcade_restroom_interactions.json`.

| Id | Meaning |
|---|---|
| `green_fairy_statue` | interactive object id for the bronze Green Fairy statue (bead pg9a) |
| `aa_node_restroom_statue`, `aa_node_restroom_exit` | nodes |
| `restroom_examine_green_fairy`, `restroom_jakub_asleep` | events (flag `jakub_restroom_discovered`) |

## Not changed (outside this bead)

- Runtime code comments naming old ids (`broken_ddr.gd:3`, `absinthe_arcade_north_wing_hd2d.gd:23`) and `game/.../hall/props/aa_hall_prize_counter.json` (`anchor`: `prize_redemption_counter`).
- The legacy engine copies `game/assets/data/locations/debaucheryville/debaucheryville_interactions.json` and `_sprite_mapping.json` (`machine_id`, `token_exchange_machine`).
- Villain folder names under `villains/absinthe_arcade/` (`frogger_existential_edition/` etc.) and the `roster_source` paths: they are game names, not object ids.
