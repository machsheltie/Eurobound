# Debaucheryville Location Art: Build Audit

**Date:** 2026-11-12
**Bead:** Eurobound-6wc
**Scope:** the 28 specs in `design/worlds/debaucheryville/PNG_Assets/`. The parallel copies in `design/World Design/` are not counted.
**Purpose:** facts for the author to set the build order. This table is not ranked; the author orders the priorities (author, 2026-11-12: "Run the audit table first, then I'll order the priorities").

## How the columns were counted

- **PNG files:** unique `*.png` filenames named in the spec (sprite sheets and single images).
- **Sprites:** spec lines giving a sprite position `(x, y, ...)`, i.e. individual tiles, frames and props. This is a rough measure of work. `ye_olde_brew_lab` is written as prose with no coordinates, so it has no sprite count.
- **Spec PNGs in repo:** how many of the spec's PNG filenames exist as real files anywhere under `Assets/Graphics/` or `game/assets/`. **Result: 0 for all 28.** No spec's sprite sheets have been made.
- **Other built art:** real image files for the location in any other form. The only built location art in the repo is Absinthe Arcade's HD-2D painted plates and textures. `game/assets/worlds/` holds only `debaucheryville/absinthe_arcade/` (91 game-ready images), and `Assets/Graphics/worlds/` holds only `debaucheryville/absinthearcade/` (460 working files: references, Tripo raws, textures, captures). `Assets/Graphics/backgrounds/` and `tilesets/` are empty. `Assets/Graphics/items/` holds `.md` docs only, with no images.
- **3D / HD-2D manifest:** a `3D_Asset_Manifest_Template.md`-style manifest for the location.
- **Quest use:** quest docs under `design/quests/` that name the location. The source was the canon index (`--mode keyword --path quests`), cross-checked with grep and de-duplicated by filename.
- **Size:** S = under 100 sprites, M = 100 to 149, L = 150 or more. Brew Lab is sized M from its 7 sheets.

## Audit table

| # | Location | Spec file | PNG files | Sprites | Spec PNGs in repo | Other built art | 3D / HD-2D manifest | Quest use | Size |
|---|----------|-----------|-----------|---------|-------------------|-----------------|---------------------|-----------|------|
| 1 | Absinthe Arcade | `Absinthe_Arcade_Complete_PNG_Asset_Requirements.md` | 4 | 116 | 0 | 85 game-ready HD-2D images (56 exterior faces/props; 29 interior: hall, mirror corridor, north wing, Arcade restroom, depth layers, 3 battle backdrops) + 460 working files | Yes: `absinthearcade_3d_asset_manifest.md`, `absinthearcade_interior_3d_asset_manifest.md`, `Assets/Graphics/.../absinthearcade_exterior/hd2d_asset_manifest.md` | Yes: brewerytourdebaucheryville, club_flyers, couchsurfingchronicles(debaucheryville), eternal_commuter, nfthuntdebaucheryville, vip_wristbands, grandpa_provides, nothingisgettingthrough, fratbronft, publicrestroomgraffiti | M |
| 2 | Astronomical Cockup Square | `Astronomical_Cockup_Square_PNG_Assets.md` | 29 | 139 | 0 | None | No | Yes: astronomical_cockup, grandpa_provides | M |
| 3 | Backroom Concessions | `Backroom_Concessions_Complete_PNG_Asset_Requirements.md` | 7 | 96 | 0 | None | No | No | S |
| 4 | Bohemian Riviera | `Bohemian_Riviera_PNG_Assets.md` | 30 | 114 | 0 | None | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | M |
| 5 | Cirque du Shady | `Cirque_du_Shady_PNG_Assets.md` | 25 | 76 | 0 | None | No | Yes: bacchanusbeachbeatdown, couchsurfingchronicles(debaucheryville), nothingisgettingthrough | S |
| 6 | Claw Machine Maintenance Closet | `Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md` | 8 | 121 | 0 | 3 HD-2D room plates (`game/assets/.../absinthe_arcade/interior/closet/aa_int_closet_{day,night,emit}.png`, scene `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.tscn`) | Covered by the Arcade interior manifest only | Yes: publicrestroomgraffiti | M |
| 7 | Cyberspace Kavarna | `Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md` | 6 | 114 | 0 | None | No | Yes: icqscammersting, greatdonerdebate | M |
| 8 | Euro Ink 4 Less | `Euro_Ink_4_Less_PNG_Assets.md` | 27 | 171 | 0 | None | No | Yes: astronomical_cockup, grandpa_provides | L |
| 9 | Hostel Midnight Checkout | `Hostel_Midnight_Checkout_Complete_PNG_Asset_Requirements.md` | 11 | 107 | 0 | None | No | No | M |
| 10 | Internet History Museum | `Internet_History_Museum_Complete_PNG_Asset_Requirements.md` | 14 | 176 | 0 | None | No | Yes: memeblackmarket | L |
| 11 | Late Night Kebab Stand | `Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md` | 6 | 118 | 0 | None | No | Yes: club_flyers, vip_wristbands, greatdonerdebate | M |
| 12 | Meme Black Market | `Meme_Black_Market_Complete_PNG_Asset_Requirements.md` | 10 | 113 | 0 | None | No | Yes: memeblackmarket | M |
| 13 | Midnight Munchies General Store | `Midnight_Munchies_General_Store_Complete_PNG_Asset_Requirements.md` | 10 | 90 | 0 | None | No | Yes: nothingisgettingthrough | S |
| 14 | Mystery Meat Cart | `Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` | 7 | 105 | 0 | None | No | Yes: greatdonerdebate | M |
| 15 | Neon and Chrome Boutique | `Neon_And_Chrome_Boutique_PNG_Assets.md` | 9 | 152 | 0 | None | No | No | L |
| 16 | The Bohemian Trap | `The_Bohemian_Trap_PNG_Assets.md` | 8 | 144 | 0 | None | No | No | M |
| 17 | The Participation Trophy | `The_Participation_Trophy_PNG_Assets.md` | 8 | 136 | 0 | None | No | No (the name appears only as a reward item in Shamsterdam's fabergeegghunt) | M |
| 18 | The Strobe Survival Kit | `The_Strobe_Survival_Kit_PNG_Assets.md` | 8 | 135 | 0 | None | No | No | M |
| 19 | Threads and Treads | `Threads_And_Treads_PNG_Assets.md` | 9 | 133 | 0 | None | No | No | M |
| 20 | Tram Stop 17 | `Tram_Stop_17_PNG_Assets.md` | 17 | 155 | 0 | None | No | Yes: eternal_commuter | L |
| 21 | The Absinthium Taproom | `absinthium_taproom_png_asset_requirements.md` | 5 | 165 | 0 | 3 HD-2D room plates (`.../absinthe_arcade/interior/taproom/aa_int_taproom_{day,night,emit}.png`, scene `absinthe_arcade_taproom_hd2d.tscn`) | Covered by the Arcade interior manifest only | Yes: brewerytour, brewerytourdebaucheryville | L |
| 22 | Public Restroom Grease Trap Shrine | `public_restroom_grease_trap_shrine_png_asset_requirements.md` | 4 | 58 | 0 | None (the Arcade restroom plates are a different room) | No | Yes: greatdonerdebate | S |
| 23 | Shadow Exchange | `shadow_exchange_png_asset_requirements.md` | 6 | 132 | 0 | None | No | Yes: brewerytourdebaucheryville, couchsurfingchronicles(debaucheryville), nfthuntdebaucheryville, nothingisgettingthrough, fratbronft | M |
| 24 | The Tap Dat Vault | `tap_dat_vault_png_asset_requirements.md` | 5 | 238 | 0 | None | No | Yes: brewerytourdebaucheryville | L |
| 25 | Three Crown Keg Haus | `three_crown_keg_haus_png_asset_requirements.md` | 5 | 220 | 0 | None | No | Yes: brewerytour, brewerytourdebaucheryville | L |
| 26 | Velvet Curtain Club | `velvet_curtain_club_png_asset_requirements.md` | 5 | 205 | 0 | None | No | Yes: club_flyers, vip_wristbands | L |
| 27 | Velvet Curtain Club VIP Stall | `velvet_curtain_club_vip_stall_png_asset_requirements.md` | 5 | 95 | 0 | None | No | Yes: memeblackmarket, publicrestroomgraffiti | S |
| 28 | Ye Olde Brew Lab | `ye_olde_brew_lab_png_asset_requirements.md` | 7 | n/a (prose spec) | 0 | None | No | Yes: brewerytour, brewerytourdebaucheryville | M |

## Summary

- **Built art of any kind: 3 of 28.** Absinthe Arcade (full HD-2D exterior and interior), plus the Claw Machine Closet and the Absinthium Taproom (one painted room plate set each, built as Arcade side rooms).
- **No art at all: 25 of 28.**
- **None of the 28 specs' own sprite sheets exist.** The Arcade was built as HD-2D painted plates, not as the 2D tilesets its PNG spec describes.
- **3D / HD-2D manifest:** only Absinthe Arcade (the closet and taproom fall under its interior manifest).
- **Used in a quest:** 21 of 28. The 7 with no quest are Backroom Concessions, Hostel Midnight Checkout, Neon and Chrome Boutique, The Bohemian Trap, The Participation Trophy, The Strobe Survival Kit, and Threads and Treads.
- **Sizes:** 5 S, 15 M, 8 L.
- Five locations also have `environment/` and `location_nodes/` JSON data (Astronomical Cockup Square, Bohemian Riviera, Cirque du Shady, Euro Ink 4 Less, Tram Stop 17). This is data only, not art.

## Duplicates flagged (for bead acceptance; not resolved here)

- `design/World Design/Debaucheryville/PNG_Assets/` still holds a parallel set of these specs. Some are reconciled copies (for example Cyberspace Kavarna has a "2026 Authoritative HD-2D Reconciliation" section that the `design/worlds/` copy lacks). The bead names Astronomical_Cockup_Square x2, Euro_Ink_4_Less x2, and the Claw Machine closet x2.
- The Bohemian Trap and Bohemian Riviera are separate specs with similar names. Whether they are the same location is an author question; this audit treats them as two.
