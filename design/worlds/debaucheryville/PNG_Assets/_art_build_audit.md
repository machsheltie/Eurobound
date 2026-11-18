# Debaucheryville Location Art: Build Audit and Build Priority

**Date:** 2026-11-17 (refreshed against the art now in `game/assets/worlds/` and `Assets/Graphics/`: Spec PNGs column, Eurobound-nven; quest names, Eurobound-0xz; Built art column and Summary, Eurobound-yafa; method notes, Eurobound-vyjs. First written 2026-11-12 and refreshed that day against commits 822deceb, 9c90bc37, 3c281703)
**Bead:** Eurobound-6wc
**Scope:** the 28 specs in `design/worlds/debaucheryville/PNG_Assets/`. The parallel copies in `design/World Design/` were removed on 2026-11-14 (Eurobound-58a).

## Build priority (author-approved)

**The Priority column is the author-approved build order** (author, 2026-11-12, Production Desk Eurobound-6wc-q1: "go with the listed order"). Build in Priority order, 1 first. The order is the order this table listed the locations in when the author ruled; the refresh below changed spec paths and art counts only, never the order. The Asset Development Team makes the art.

## How the columns were counted

- **Spec file:** the one spec of record per location, `<Location>_Complete_PNG_Asset_Requirements.md` (author, Eurobound-x0c: HD-2D sheet first, the older sprite-sheet spec folded in beneath it under "Legacy sprite-sheet detail").
- **HD-2D sheet:** whether the spec opens with an HD-2D sheet. "Yes, 3 parts PENDING" means the sheet exists but its Visual target, Spatial Composition and State and Character Coverage read "PENDING (art direction)" (Eurobound-c5rq). "PENDING" means the sheet is an empty heading (Eurobound-c5rq). "None" means the spec has no HD-2D sheet (Eurobound-xsw1).
- **Legacy PNG files / Legacy sprites:** counted from the legacy sprite-sheet spec before the merge; the numbers are unchanged. PNG files = unique `*.png` filenames; sprites = lines giving a sprite position `(x, y, ...)`. `ye_olde_brew_lab` is prose with no coordinates, so it has no sprite count.
- **Spec PNGs in repo:** how many of the `*.png` filenames named anywhere in the merged spec exist as real files under `game/assets/` or `Assets/Graphics/` (matched / named). Recounted 2026-11-17 (Eurobound-nven) with `Tools/data_validation/spec_png_match.py`: case-insensitive basename match, brace lists expanded (`{day,night,emit}`), placeholders such as `<slug>_exterior.png` skipped. The HD-2D sheets now name the built plates (`<slug>_ext_day.png`, `<slug>_ext_night.png`, `<slug>_ext_front_elevation_day.png`, `<slug>_int_day.png`, `<slug>_int_night.png`; Eurobound-z50s), so built plates match: 149 of 868 names across the 28 specs, 27 specs with at least one match. Cyberspace Kavarna has no HD-2D sheet (Eurobound-xsw1) and matches none. The unmatched names are HD-2D node art and legacy sprite-sheet files not built yet.
- **Built art:** game-ready PNGs in `game/assets/worlds/debaucheryville/<slug>/`, counted 2026-11-17 (Eurobound-yafa) with `python -I Tools/data_validation/built_art_count.py` (`--detail` gives per-subfolder counts and plate names, `--json` machine output). "Ext (n)" = n PNGs anywhere under `<slug>/exterior/`; "Int (n)" = n PNGs anywhere under `<slug>/interior/`. The usual set is Ext (3) (day, night, front elevation) + Int (2) (day, night); a cell names any other set. Arcade side rooms are counted from their Arcade subfolder. `.import` files never count, and folders holding a `.gdignore` are staging, not game-ready, so their PNGs are left out (66 in `absinthe_arcade/interior/north_wing/props_staged/`). The Spec PNGs column comes from its sibling, `python -I Tools/data_validation/spec_png_match.py` (`--missing` lists the unmatched names). `Assets/Graphics/worlds/` holds working files for the Arcade only (689 files in `debaucheryville/absinthearcade/`, as `built_art_count.py` reports: references, Tripo raws, textures, captures). `Assets/Graphics/backgrounds/` and `tilesets/` are empty.
- **3D / HD-2D manifest:** a `3D_Asset_Manifest_Template.md`-style manifest for the location.
- **Quest use:** quest docs under `design/quests/` that name the location (canon index `--mode keyword --path quests`, cross-checked with grep, de-duplicated by filename).
- **Size:** S = under 100 legacy sprites, M = 100 to 149, L = 150 or more. Brew Lab is sized M from its 7 sheets.

## Audit table

| Priority | Location | Spec file | HD-2D sheet | Legacy PNG files | Legacy sprites | Spec PNGs in repo | Built art | 3D / HD-2D manifest | Quest use | Size |
|---|----------|-----------|-------------|------------------|----------------|-------------------|-----------|---------------------|-----------|------|
| 1 | Absinthe Arcade | `Absinthe_Arcade_Complete_PNG_Asset_Requirements.md` | Yes | 4 | 116 | 38 / 147 | 242 PNGs in `absinthe_arcade/`: exterior 62 (23 faces, 39 props); interior 180 (hall 60, closet 42, mirror corridor 21, taproom maze M1/M5 16, depth layers 14, restroom 10, masks 7, battle backdrops 4, north wing 3, taproom 3); scenes in `game/worlds/debaucheryville/`. Not counted: 66 staged PNGs in `interior/north_wing/props_staged/` (`.gdignore`). Plus 689 working files | Yes: `absinthearcade_3d_asset_manifest.md`, `absinthearcade_interior_3d_asset_manifest.md`, `Assets/Graphics/.../absinthearcade_exterior/hd2d_asset_manifest.md` | Yes: brewerytourdebaucheryville, club_flyers, couchsurfingchronicles(debaucheryville), eternal_commuter, nfthuntdebaucheryville, vip_wristbands, grandpa_provides, nothingisgettingthrough, fratbronft, publicrestroomgraffiti | M |
| 2 | Astronomical Cockup Square | `Astronomical_Cockup_Square_Complete_PNG_Asset_Requirements.md` | Yes | 29 | 139 | 4 / 37 | Ext (4): day, night, front elevation, exits | No | Yes: astronomical_cockup, grandpa_provides | M |
| 3 | Backroom Concessions | `Backroom_Concessions_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 7 | 96 | 5 / 24 | Ext (3) + Int (2) | No | No | S |
| 4 | Bohemian Riviera | `Bohemian_Riviera_Complete_PNG_Asset_Requirements.md` | PENDING | 30 | 114 | 2 / 35 | Ext (2): day and night; the front elevation was removed (2daeb5b1: outdoor area, no facade) | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | M |
| 5 | Cirque du Shady | `Cirque_du_Shady_Complete_PNG_Asset_Requirements.md` | PENDING | 25 | 76 | 5 / 30 | Ext (3) + Int (2) | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | S |
| 6 | Claw Machine Maintenance Closet | `Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 121 | 4 / 22 | 42 PNGs as an Arcade side room: `absinthe_arcade/interior/closet/aa_int_closet_{day,night,emit,night_uv}.png` + 38 props; scene `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.tscn` | Covered by the Arcade interior manifest only | Yes: publicrestroomgraffiti | M |
| 7 | Cyberspace Kavarna | `Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md` | None | 6 | 114 | 0 / 20 | Ext (3) + Int (2) (`game/worlds/debaucheryville/cyberspace_kavarna/` still holds a chair script only) | No | Yes: icqscammersting, great_doner_debate | M |
| 8 | Euro Ink 4 Less | `Euro_Ink_4_Less_Complete_PNG_Asset_Requirements.md` | Yes | 27 | 171 | 5 / 35 | Ext (3) + Int (2) | No | Yes: astronomical_cockup, grandpa_provides | L |
| 9 | Hostel Midnight Checkout | `Hostel_Midnight_Checkout_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 11 | 107 | 5 / 32 | Ext (3) + Int (8): main interior day and night, plus day and night for 3 rooms (bunk confession, dorm, kitchen) | No | No | M |
| 10 | Internet History Museum | `Internet_History_Museum_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 14 | 176 | 5 / 35 | Ext (3) + Int (2) | No | Yes: memeblackmarket | L |
| 11 | Late Night Kebab Stand | `Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 6 | 118 | 3 / 11 | Ext (3) | No | Yes: club_flyers, vip_wristbands, great_doner_debate | M |
| 12 | Meme Black Market | `Meme_Black_Market_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 10 | 113 | 5 / 28 | Ext (3) + Int (2) | No | Yes: memeblackmarket | M |
| 13 | Midnight Munchies General Store | `Midnight_Munchies_General_Store_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 10 | 90 | 5 / 29 | Ext (3) + Int (2) | No | Yes: nothingisgettingthrough | S |
| 14 | Mystery Meat Cart | `Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 7 | 105 | 3 / 12 | Ext (3) | No | Yes: great_doner_debate | M |
| 15 | Neon and Chrome Boutique | `Neon_And_Chrome_Boutique_Complete_PNG_Asset_Requirements.md` | Yes | 9 | 152 | 5 / 31 | Ext (3) + Int (2) | No | No | L |
| 16 | The Bohemian Trap | `Bohemian_Trap_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 144 | 3 / 26 | Ext (3) | No | No | M |
| 17 | The Participation Trophy | `Participation_Trophy_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 136 | 3 / 28 | Ext (3) | No | No (the name appears only as a reward item in Shamsterdam's fabergeegghunt) | M |
| 18 | The Strobe Survival Kit | `Strobe_Survival_Kit_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 135 | 3 / 28 | Ext (3) | No | No | M |
| 19 | Threads and Treads | `Threads_And_Treads_Complete_PNG_Asset_Requirements.md` | Yes | 9 | 133 | 5 / 29 | Ext (3) + Int (2) | No | No | M |
| 20 | Tram Stop 17 | `Tram_Stop_17_Complete_PNG_Asset_Requirements.md` | Yes | 17 | 155 | 3 / 24 | Ext (3) | No | Yes: eternal_commuter | L |
| 21 | The Absinthium Taproom | `Absinthium_Taproom_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 165 | 3 / 24 | 3 PNGs as an Arcade side room: `absinthe_arcade/interior/taproom/aa_int_taproom_{day,night,emit}.png`; scene `absinthe_arcade_taproom_hd2d.tscn` | Covered by the Arcade interior manifest only | Yes: brewerytour, brewerytourdebaucheryville | L |
| 22 | Public Restroom Grease Trap Shrine | `Public_Restroom_Grease_Trap_Shrine_Complete_PNG_Asset_Requirements.md` | Yes | 4 | 58 | 5 / 22 | Ext (3) + Int (2) (separate from the Arcade restroom plates) | No | Yes: great_doner_debate | S |
| 23 | Shadow Exchange | `Shadow_Exchange_Complete_PNG_Asset_Requirements.md` | Yes | 6 | 132 | 5 / 28 | Ext (3) + Int (2) | No | Yes: brewerytourdebaucheryville, couchsurfingchronicles(debaucheryville), nfthuntdebaucheryville, nothingisgettingthrough, fratbronft | M |
| 24 | The Tap Dat Vault | `Tap_Dat_Vault_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 238 | 5 / 27 | Ext (3) + Int (2) | No | Yes: brewerytourdebaucheryville | L |
| 25 | Three Crown Keg Haus | `Three_Crown_Keg_Haus_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 220 | 5 / 26 | Ext (3) + Int (2) | No | Yes: brewerytour, brewerytourdebaucheryville | L |
| 26 | Velvet Curtain Club | `Velvet_Curtain_Club_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 205 | 5 / 28 | Ext (3) + Int (2) | No | Yes: club_flyers, vip_wristbands | L |
| 27 | Velvet Curtain Club VIP Stall | `Velvet_Curtain_Club_VIP_Stall_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 95 | 5 / 21 | Ext (3) + Int (2) | No | Yes: memeblackmarket, publicrestroomgraffiti | S |
| 28 | Ye Olde Brew Lab | `Ye_Olde_BREW_Lab_Complete_PNG_Asset_Requirements.md` | Yes | 7 | n/a (prose spec) | 5 / 29 | Ext (3) + Int (2) | No | Yes: brewerytour, brewerytourdebaucheryville | M |

## Summary

- **Built art of any kind: 28 of 28** (Built art column and these counts recounted 2026-11-17, Eurobound-yafa, with `python -I Tools/data_validation/built_art_count.py`). Absinthe Arcade is the only fully built location (HD-2D exterior and interior, props, depth layers, masks, battle backdrops, playable scenes).
- **Exterior and interior plates: 17.** Backroom Concessions, Cirque du Shady, Cyberspace Kavarna, Euro Ink 4 Less, Hostel Midnight Checkout (Int 8), Internet History Museum, Meme Black Market, Midnight Munchies General Store, Neon and Chrome Boutique, Public Restroom Grease Trap Shrine, Shadow Exchange, The Tap Dat Vault, Threads and Treads, Three Crown Keg Haus, Velvet Curtain Club, Velvet Curtain Club VIP Stall, Ye Olde Brew Lab. All are Ext (3) + Int (2) except Hostel Midnight Checkout.
- **Exterior plates only: 8.** Astronomical Cockup Square (4), Bohemian Riviera (2), Late Night Kebab Stand, Mystery Meat Cart, The Bohemian Trap, The Participation Trophy, The Strobe Survival Kit, Tram Stop 17 (3 each).
- **Interior plates only: 0.**
- **Arcade side rooms: 2.** Claw Machine Maintenance Closet (room plates and 38 props), The Absinthium Taproom (room plates).
- **No art at all: 0 of 28.**
- **Plates only, no node art yet.** Outside the Arcade, no location has its landmark cutouts, NPC sprites, emission masks or depth cards; the built plates match the spec's exterior and interior painted layers only.
- **HD-2D sheet gaps:** Bohemian Riviera (Ext (2)) and Cirque du Shady (Ext (3) + Int (2), exterior and interior plates) have built plates but an empty HD-2D sheet; 7 specs have 3 PENDING parts (Eurobound-c5rq). Cyberspace Kavarna now has Ext (3) + Int (2) plates, but its spec has no HD-2D sheet, so it names none of them (0 / 20; Eurobound-xsw1).
- **3D / HD-2D manifest:** only Absinthe Arcade (the closet and taproom fall under its interior manifest).
- **Used in a quest:** 21 of 28. The 7 with no quest are Backroom Concessions, Hostel Midnight Checkout, Neon and Chrome Boutique, The Bohemian Trap, The Participation Trophy, The Strobe Survival Kit, and Threads and Treads.
- **Sizes:** 5 S, 15 M, 8 L.
- Five locations also have `environment/` and `location_nodes/` JSON data (Astronomical Cockup Square, Bohemian Riviera, Cirque du Shady, Euro Ink 4 Less, Tram Stop 17). This is data only, not art.

## Duplicates flagged (for bead acceptance; not resolved here)

- `design/World Design/Debaucheryville/PNG_Assets/` is gone (removed 2026-11-14, Eurobound-58a). Its last file's HD-2D reconciliation section was ported into the `design/worlds/` Cyberspace Kavarna spec first (Eurobound-6rl).
- Update 2026-11-12 (Eurobound-x0c, author: "HD-2D sheet is the spec of record; fold the older sprite-sheet spec in beneath it as detail, one file per location"): each location now has one `<Location>_Complete_PNG_Asset_Requirements.md`, with the legacy sprite-sheet spec under "Legacy sprite-sheet detail". Bohemian Riviera and Cirque du Shady were renamed from `*_PNG_Assets.md` (Eurobound-co3m).
- The bead's Character Profiles copy is gone: `design/Character Profiles/` no longer exists, and the one remaining cosmetics PNG spec is `design/characters/permanent_cosmetic_changes/png_assets/permanent_cosmetic_changes_png_assets.md` (Eurobound-fhg3).
- The Bohemian Trap and Bohemian Riviera are separate specs with similar names. Whether they are the same location is an author question; this audit treats them as two.
