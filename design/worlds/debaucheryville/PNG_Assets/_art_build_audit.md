# Debaucheryville Location Art: Build Audit and Build Priority

**Date:** 2026-11-12 (refreshed the same day against commits 822deceb, 9c90bc37, 3c281703 and the art now in `game/assets/worlds/`)
**Bead:** Eurobound-6wc
**Scope:** the 28 specs in `design/worlds/debaucheryville/PNG_Assets/`. The parallel copies in `design/World Design/` are not counted.

## Build priority (author-approved)

**The Priority column is the author-approved build order** (author, 2026-11-12, Production Desk Eurobound-6wc-q1: "go with the listed order"). Build in Priority order, 1 first. The order is the order this table listed the locations in when the author ruled; the refresh below changed spec paths and art counts only, never the order. The Asset Development Team makes the art.

## How the columns were counted

- **Spec file:** the one spec of record per location, `<Location>_Complete_PNG_Asset_Requirements.md` (author, Eurobound-x0c: HD-2D sheet first, the older sprite-sheet spec folded in beneath it under "Legacy sprite-sheet detail").
- **HD-2D sheet:** whether the spec opens with an HD-2D sheet. "Yes, 3 parts PENDING" means the sheet exists but its Visual target, Spatial Composition and State and Character Coverage read "PENDING (art direction)" (Eurobound-c5rq). "PENDING" means the sheet is an empty heading (Eurobound-c5rq). "None" means the spec has no HD-2D sheet (Eurobound-xsw1).
- **Legacy PNG files / Legacy sprites:** counted from the legacy sprite-sheet spec before the merge; the numbers are unchanged. PNG files = unique `*.png` filenames; sprites = lines giving a sprite position `(x, y, ...)`. `ye_olde_brew_lab` is prose with no coordinates, so it has no sprite count.
- **Spec PNGs in repo:** how many of the `*.png` filenames named anywhere in the merged spec exist as real files under `game/assets/` or `Assets/Graphics/` (matched / named). Built plates are named `<slug>_ext_day.png`, `<slug>_ext_night.png`, `<slug>_ext_front_elevation_day.png`, `<slug>_int_day.png` and `<slug>_int_night.png`, while most HD-2D sheets name `<slug>_exterior.png` and `<slug>_interior.png`, so built art does not match by filename (Eurobound-z50s).
- **Built art:** game-ready images in `game/assets/worlds/debaucheryville/<slug>/`. "Ext" = exterior day, night and front elevation (3 PNGs); "Int" = interior day and night (2 PNGs). `Assets/Graphics/worlds/` holds working files for the Arcade only (523 files: references, Tripo raws, textures, captures). `Assets/Graphics/backgrounds/` and `tilesets/` are empty.
- **3D / HD-2D manifest:** a `3D_Asset_Manifest_Template.md`-style manifest for the location.
- **Quest use:** quest docs under `design/quests/` that name the location (canon index `--mode keyword --path quests`, cross-checked with grep, de-duplicated by filename).
- **Size:** S = under 100 legacy sprites, M = 100 to 149, L = 150 or more. Brew Lab is sized M from its 7 sheets.

## Audit table

| Priority | Location | Spec file | HD-2D sheet | Legacy PNG files | Legacy sprites | Spec PNGs in repo | Built art | 3D / HD-2D manifest | Quest use | Size |
|---|----------|-----------|-------------|------------------|----------------|-------------------|-----------|---------------------|-----------|------|
| 1 | Absinthe Arcade | `Absinthe_Arcade_Complete_PNG_Asset_Requirements.md` | Yes | 4 | 116 | 14 / 102 | 210 PNGs in `absinthe_arcade/`: exterior 62 (23 faces, 39 props); interior 148 (hall 60, mirror corridor 21, closet 20, taproom maze M1/M5 16, depth layers 14, restroom 7, battle backdrops 4, north wing 3, taproom 3); scenes in `game/worlds/debaucheryville/`. Plus 523 working files | Yes: `absinthearcade_3d_asset_manifest.md`, `absinthearcade_interior_3d_asset_manifest.md`, `Assets/Graphics/.../absinthearcade_exterior/hd2d_asset_manifest.md` | Yes: brewerytourdebaucheryville, club_flyers, couchsurfingchronicles(debaucheryville), eternal_commuter, nfthuntdebaucheryville, vip_wristbands, grandpa_provides, nothingisgettingthrough, fratbronft, publicrestroomgraffiti | M |
| 2 | Astronomical Cockup Square | `Astronomical_Cockup_Square_Complete_PNG_Asset_Requirements.md` | Yes | 29 | 139 | 0 / 34 | None | No | Yes: astronomical_cockup, grandpa_provides | M |
| 3 | Backroom Concessions | `Backroom_Concessions_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 7 | 96 | 0 / 21 | None | No | No | S |
| 4 | Bohemian Riviera | `Bohemian_Riviera_Complete_PNG_Asset_Requirements.md` | PENDING | 30 | 114 | 0 / 30 | Ext (3) | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | M |
| 5 | Cirque du Shady | `Cirque_du_Shady_Complete_PNG_Asset_Requirements.md` | PENDING | 25 | 76 | 0 / 25 | Ext (3) | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | S |
| 6 | Claw Machine Maintenance Closet | `Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 121 | 0 / 20 | 20 PNGs as an Arcade side room: `absinthe_arcade/interior/closet/aa_int_closet_{day,night,emit}.png` + 17 props; scene `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.tscn` | Covered by the Arcade interior manifest only | Yes: publicrestroomgraffiti | M |
| 7 | Cyberspace Kavarna | `Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md` | None | 6 | 114 | 0 / 6 | None (`game/worlds/debaucheryville/cyberspace_kavarna/` holds a chair script only) | No | Yes: icqscammersting, greatdonerdebate | M |
| 8 | Euro Ink 4 Less | `Euro_Ink_4_Less_Complete_PNG_Asset_Requirements.md` | Yes | 27 | 171 | 0 / 32 | Ext (3) + Int (2) | No | Yes: astronomical_cockup, grandpa_provides | L |
| 9 | Hostel Midnight Checkout | `Hostel_Midnight_Checkout_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 11 | 107 | 0 / 29 | Ext (3) + Int (2) | No | No | M |
| 10 | Internet History Museum | `Internet_History_Museum_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 14 | 176 | 0 / 32 | Ext (3) + Int (2) | No | Yes: memeblackmarket | L |
| 11 | Late Night Kebab Stand | `Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 6 | 118 | 0 / 6 | Ext (3) | No | Yes: club_flyers, vip_wristbands, greatdonerdebate | M |
| 12 | Meme Black Market | `Meme_Black_Market_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 10 | 113 | 0 / 25 | Int (2) | No | Yes: memeblackmarket | M |
| 13 | Midnight Munchies General Store | `Midnight_Munchies_General_Store_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 10 | 90 | 0 / 26 | Ext (3) + Int (2) | No | Yes: nothingisgettingthrough | S |
| 14 | Mystery Meat Cart | `Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` | Yes, 3 parts PENDING | 7 | 105 | 0 / 7 | Ext (3) | No | Yes: greatdonerdebate | M |
| 15 | Neon and Chrome Boutique | `Neon_And_Chrome_Boutique_Complete_PNG_Asset_Requirements.md` | Yes | 9 | 152 | 0 / 28 | Ext (3) + Int (2) | No | No | L |
| 16 | The Bohemian Trap | `Bohemian_Trap_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 144 | 0 / 23 | Ext (3) | No | No | M |
| 17 | The Participation Trophy | `Participation_Trophy_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 136 | 0 / 25 | Ext (3) | No | No (the name appears only as a reward item in Shamsterdam's fabergeegghunt) | M |
| 18 | The Strobe Survival Kit | `Strobe_Survival_Kit_Complete_PNG_Asset_Requirements.md` | Yes | 8 | 135 | 0 / 25 | Ext (3) | No | No | M |
| 19 | Threads and Treads | `Threads_And_Treads_Complete_PNG_Asset_Requirements.md` | Yes | 9 | 133 | 0 / 26 | Ext (3) + Int (2) | No | No | M |
| 20 | Tram Stop 17 | `Tram_Stop_17_Complete_PNG_Asset_Requirements.md` | Yes | 17 | 155 | 0 / 22 | Ext (3) | No | Yes: eternal_commuter | L |
| 21 | The Absinthium Taproom | `Absinthium_Taproom_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 165 | 0 / 23 | 3 PNGs as an Arcade side room: `absinthe_arcade/interior/taproom/aa_int_taproom_{day,night,emit}.png`; scene `absinthe_arcade_taproom_hd2d.tscn` | Covered by the Arcade interior manifest only | Yes: brewerytour, brewerytourdebaucheryville | L |
| 22 | Public Restroom Grease Trap Shrine | `Public_Restroom_Grease_Trap_Shrine_Complete_PNG_Asset_Requirements.md` | Yes | 4 | 58 | 0 / 19 | Ext (3) + Int (2) (separate from the Arcade restroom plates) | No | Yes: greatdonerdebate | S |
| 23 | Shadow Exchange | `Shadow_Exchange_Complete_PNG_Asset_Requirements.md` | Yes | 6 | 132 | 0 / 25 | Ext (3) + Int (2) | No | Yes: brewerytourdebaucheryville, couchsurfingchronicles(debaucheryville), nfthuntdebaucheryville, nothingisgettingthrough, fratbronft | M |
| 24 | The Tap Dat Vault | `Tap_Dat_Vault_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 238 | 0 / 24 | Ext (3) + Int (2) | No | Yes: brewerytourdebaucheryville | L |
| 25 | Three Crown Keg Haus | `Three_Crown_Keg_Haus_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 220 | 0 / 23 | Ext (3) + Int (2) | No | Yes: brewerytour, brewerytourdebaucheryville | L |
| 26 | Velvet Curtain Club | `Velvet_Curtain_Club_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 205 | 0 / 25 | Ext (3) + Int (2) | No | Yes: club_flyers, vip_wristbands | L |
| 27 | Velvet Curtain Club VIP Stall | `Velvet_Curtain_Club_VIP_Stall_Complete_PNG_Asset_Requirements.md` | Yes | 5 | 95 | 0 / 18 | Int (2) | No | Yes: memeblackmarket, publicrestroomgraffiti | S |
| 28 | Ye Olde Brew Lab | `Ye_Olde_BREW_Lab_Complete_PNG_Asset_Requirements.md` | Yes | 7 | n/a (prose spec) | 0 / 26 | Ext (3) + Int (2) | No | Yes: brewerytour, brewerytourdebaucheryville | M |

## Summary

- **Built art of any kind: 25 of 28.** Absinthe Arcade is the only fully built location (HD-2D exterior and interior, props, depth layers, battle backdrops, playable scenes).
- **Exterior and interior plates (5 PNGs): 12.** Euro Ink 4 Less, Hostel Midnight Checkout, Internet History Museum, Midnight Munchies General Store, Neon and Chrome Boutique, Public Restroom Grease Trap Shrine, Shadow Exchange, The Tap Dat Vault, Threads and Treads, Three Crown Keg Haus, Velvet Curtain Club, Ye Olde Brew Lab.
- **Exterior plates only (3 PNGs): 8.** Bohemian Riviera, Cirque du Shady, Late Night Kebab Stand, Mystery Meat Cart, The Bohemian Trap, The Participation Trophy, The Strobe Survival Kit, Tram Stop 17.
- **Interior plates only (2 PNGs): 2.** Meme Black Market, Velvet Curtain Club VIP Stall.
- **Arcade side rooms: 2.** Claw Machine Maintenance Closet (room plates and 17 props), The Absinthium Taproom (room plates).
- **No art at all: 3 of 28.** Astronomical Cockup Square, Backroom Concessions, Cyberspace Kavarna.
- **Plates only, no node art yet.** Outside the Arcade, no location has its landmark cutouts, NPC sprites, emission masks or depth cards; the built plates match the spec's exterior and interior painted layers only.
- **HD-2D sheet gaps:** Bohemian Riviera and Cirque du Shady have exterior plates but an empty HD-2D sheet; 7 specs have 3 PENDING parts (Eurobound-c5rq). Cyberspace Kavarna has no HD-2D sheet (Eurobound-xsw1).
- **3D / HD-2D manifest:** only Absinthe Arcade (the closet and taproom fall under its interior manifest).
- **Used in a quest:** 21 of 28. The 7 with no quest are Backroom Concessions, Hostel Midnight Checkout, Neon and Chrome Boutique, The Bohemian Trap, The Participation Trophy, The Strobe Survival Kit, and Threads and Treads.
- **Sizes:** 5 S, 15 M, 8 L.
- Five locations also have `environment/` and `location_nodes/` JSON data (Astronomical Cockup Square, Bohemian Riviera, Cirque du Shady, Euro Ink 4 Less, Tram Stop 17). This is data only, not art.

## Duplicates flagged (for bead acceptance; not resolved here)

- `design/World Design/Debaucheryville/PNG_Assets/` now holds one file, `Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md`, whose "2026 Authoritative HD-2D Reconciliation" section the `design/worlds/` copy lacks (Eurobound-xsw1; parallel-copy cleanup is Eurobound-58a). The other parallel copies the bead named (Astronomical_Cockup_Square x2, Euro_Ink_4_Less x2, the Claw Machine closet x2) are gone.
- Update 2026-11-12 (Eurobound-x0c, author: "HD-2D sheet is the spec of record; fold the older sprite-sheet spec in beneath it as detail, one file per location"): each location now has one `<Location>_Complete_PNG_Asset_Requirements.md`, with the legacy sprite-sheet spec under "Legacy sprite-sheet detail". Bohemian Riviera and Cirque du Shady were renamed from `*_PNG_Assets.md` (Eurobound-co3m).
- The bead's Character Profiles copy is gone: `design/Character Profiles/` no longer exists, and the one remaining cosmetics PNG spec is `design/characters/PermanantCosmeticChanges/PNG Assets/permanent_cosmetic_changes_png_assets.md` (folder names keep the "Permanant" typo and a space; Eurobound-fhg3).
- The Bohemian Trap and Bohemian Riviera are separate specs with similar names. Whether they are the same location is an author question; this audit treats them as two.
