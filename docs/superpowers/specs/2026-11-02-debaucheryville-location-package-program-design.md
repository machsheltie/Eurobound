# Debaucheryville Location Package Program Design

## Intent

Complete the Debaucheryville production-design library by creating a master roadmap and one location-package design specification for each of the 25 unique locations that remain after Absinthe Arcade. Each approved location will ultimately receive seven coordinated JSON files and one reconciled PNG asset-requirements document.

## Deliverables

Every location package owns:

- `core/<slug>_core.json`
- `environment/<slug>_environment.json`
- `interactions/<slug>_interactions.json`
- `items/<slug>_items.json`
- `location_nodes/<slug>_location_nodes.json`
- `npcs/<Location_Folder>/<slug>_npcs.json`
- `sprite_mapping/<slug>_sprite_mapping.json`
- `PNG_Assets/<Location_Title>_Complete_PNG_Asset_Requirements.md`

The existing Absinthe Arcade package is the structural baseline and is outside this program's creation scope. Its outbound transitions remain important dependencies.

## Portfolio Scope

The 25 locations are:

1. Astronomical Cock-Up Square
2. Backroom Concessions
3. Claw Machine Maintenance Closet Restroom
4. Cyberspace Kavarna
5. Euro Ink 4 Less
6. Hostel "Midnight Checkout"
7. Internet History Museum
8. Late-Night Kebab Stand
9. Meme Black Market
10. Midnight Munchies General Store
11. Cirque du Shady - Mystery Meat Cart
12. Neon & Chrome Boutique
13. Public Restroom - Grease Trap Shrine
14. Shadow Exchange
15. The Absinthium Taproom
16. The Bohemian Trap
17. The Participation Trophy
18. The Strobe Survival Kit
19. The Tap Dat Vault
20. Threads & Treads
21. Three-Crown Keg Haus
22. Tram Stop #17
23. Velvet Curtain Club
24. Velvet Curtain Club VIP Stall
25. Ye Olde B.R.E.W. Lab

## Canon and Precedence

When sources disagree, use this order:

1. Explicit author-ruling item files under `design/items/` for item IDs, acquisition, prices, and item-specific gate behavior.
2. The dedicated location Markdown file, with explicit reconciliation exceptions below.
3. The newer `design/Quests/debaucheryville/` quest version for live state, rewards, gates, and dialogue ownership not superseded by an item ruling.
4. The matching `design/Quests/Location Specific/Debaucheryville/` version only where the newer quest is silent or absent.
5. Existing package JSON and non-hash PNG documents for schema and still-compatible implementation detail.
6. Hash-prefixed or older PNG documents as asset discovery sources, not unquestioned canon.
7. `debaucheryville_locations_index.md` as a convenience index only; it is incomplete and contains legacy spellings.

Quest dialogue remains owned by quest or NPC-profile documents. Location files bind triggers, states, schedules, and outcomes without creating competing dialogue copies.

### Reconciliation Exceptions

- `velvet_curtain_club.md` is the primary Velvet Curtain Club source because it is newer, more complete, and owns the expanded gate/state treatment. `velvetcurtainclub.md` supplies compatible omissions only.
- `publicrestroomkebaballey.md` has no formal location identity block. Its restroom content ends before the appended `# Mystery Meat Cart - Complete PNG Asset Requirements` heading. The appended cart section belongs to Mystery Meat Cart and must not enter the restroom package.
- The Public Restroom receives the normalized ID `debaucheryville_kebab_alley_grease_trap_shrine_01` and slug `public_restroom_grease_trap_shrine`.
- `absynthium_taproom` in the partial index is legacy spelling. Use the dedicated file's `debaucheryville_brewery_absinthium_taproom_01`.
- Existing Astronomical Cock-Up Square and Tram Stop #17 packages are audited and retained where correct. Euro Ink 4 Less is reconciled and receives its missing item package. No valid existing content is overwritten merely to make files uniform.
- Backroom Concessions is normalized as a hidden child of Cyberspace Kavarna's internet café. This is an approved portfolio decision inferred from the two briefs, not an explicit source identity claim.

## Shared Design Language

Debaucheryville is sincere Central European urban fabric repeatedly colonized by tourist scams, broken nightlife technology, fake exclusivity, digital nostalgia, and late-night survival commerce. Each location must preserve a readable architectural or street-vendor base beneath its comic corruption.

Art direction follows the established Godot 4.4 painterly HD-2D method: painted architectural faces or location cards on simple 3D massing, selected depth layers, cutout/billboard props, restrained particles, emission masks, and state overlays. Existing pixel-art concepts are retained as in-world screens, signage, icons, graffiti, or deliberately retro props rather than forcing the complete environment into a pure tile-sheet style.

Accessibility variants are first-class requirements. Strobe, chromatic aberration, smoke, mirror distortion, rapid flashes, and screen glitch effects need reduced-motion, reduced-flash, and high-readability states where applicable.

## Spatial Ownership Rules

- A parent location owns the visible approach, door, curtain, crawlspace, stair, or puzzle that exposes an outbound transition.
- A destination location owns everything beyond its transition threshold, including interior art, NPCs, rewards, combat, and local state.
- Open-air stalls and carts still receive an "interior" node group representing their service footprint, counter space, stock display, and player interaction zone.
- Hidden locations must define both undiscovered and discovered traversal states.
- A node graph must distinguish physical adjacency from quest-only relationships.
- Shared streets, alleys, and plazas may be referenced by multiple packages but each prop or interaction has one owning location.

## Cross-Location Dependency Groups

### Old Town and Transit

Astronomical Cock-Up Square seeds the VIP wristband quest and Euro Ink visit. Tram Stop #17 bridges Old Town and the neon district. Shadow Exchange anchors black-market referrals and the route to Three-Crown Keg Haus.

### Hostel and Digital Underground

Hostel "Midnight Checkout," Cyberspace Kavarna, Backroom Concessions, Midnight Munchies, Internet History Museum, and Meme Black Market form the accommodation, ICQ, cursed-web, and late-night survival network. Hidden backrooms remain separate locations with explicit parent transitions.

### Neon Quarter and Nightlife

Absinthe Arcade exposes the Absinthium Taproom and maintenance restroom. Velvet Curtain Club owns its bouncer gate and exposes the VIP Stall and Ye Olde B.R.E.W. Lab. Neon & Chrome, Threads & Treads, The Strobe Survival Kit, and The Bohemian Trap support club preparation and status economies without becoming rooms inside either venue.

### Brewery Tour

The tour sequence is Absinthium Taproom, Three-Crown Keg Haus, Tap Dat Vault, then Ye Olde B.R.E.W. Lab. Each brewery owns one stamp, signature brew, selfie landmark, local challenge, and return exit.

The current item rulings supersede older location prose about opener purchases and gatekeeper checks:

- `bottle_opener_keychain` is the externally owned permanent container granted in Publandia.
- Debaucheryville brewery doors do not check the Blarney Trap opener or sell local openers.
- Challenge completion earns that brewery's local opener and stamp together; local openers are never sold.
- `bottle_opener_keychain` does not gate physical entry, ordinary exploration, or completion of the local challenge. It gates Brewery Tour reward eligibility: opener, stamp, brewmaster selfie, and signature-beer unlock cannot be granted before the Publandia tour trigger.
- If a challenge was completed before tour activation, store its completion flag and defer the tour rewards. On the first post-activation service interaction while carrying `bottle_opener_keychain`, grant the opener, stamp, selfie unlock, and signature-beer purchase access without requiring challenge replay.
- The four exact opener IDs are `opener_absinthium_taproom`, `opener_three_crown_keg_haus`, `opener_tap_dat_vault`, and `opener_ye_olde_brew_lab`.
- Signature beers remain purchases after their documented service unlock: `beer_absinthium_taproom` at 12 Sovs, `beer_three_crown_keg_haus` at 10 Sovs, `beer_tap_dat_vault` at 14 Sovs, and `beer_ye_olde_brew_lab` at 18 Sovs with a live plus/minus-5 volatility roll.
- Older Blarney authorization dialogue, local-opener purchase alternatives, and opener-as-stamp-gate text are deprecated. Only the item files' salvaged ambient greetings survive.

### Food and Circus

Late-Night Kebab Stand owns the alley food footprint and exposes the 3 AM crawlspace to the Grease Trap Shrine. Cirque du Shady - Mystery Meat Cart and The Participation Trophy are separate circus vendors connected through shared ticket, food, and performance states.

## Shared Transition and Collection Contracts

- Absinthe Arcade to maintenance restroom: `arcade_maintenance_restroom_unlocked`.
- Absinthe Arcade to Taproom discovery: `absinthium_taproom_entrance_discovered`.
- Kebab Stand to Grease Trap Shrine: `grease_trap_shrine_crawlspace_discovered`; `grease_trap_shrine_access_window_open` is true from 03:00 through 03:59 and false at 04:00.
- Museum clue: `meme_black_market_graffiti_clue_read`.
- Museum after-hours access: `internet_museum_after_hours_access_enabled`; when the clue is set, the quest-unlatched front-door route is active from 03:25 through 03:40 and the puzzle fires at 03:33.
- Museum shelf discovery/unlock: `meme_black_market_entrance_discovered` and `meme_black_market_entrance_unlocked`.
- Velvet wristbands applied: `vip_wristbands_all_bros`.
- Velvet first-entry sequence completed/repeat access: `vip_wristband_quest_complete` and `velvet_curtain_club_access_was_always_free`.
- Velvet to VIP Stall: `velvet_vip_stall_entrance_discovered` and `velvet_vip_stall_access_unlocked`.
- Velvet to B.R.E.W. Lab: `brew_lab_entrance_discovered` and `brew_lab_access_unlocked`.
- Cyberspace to Backroom Concessions normalization: `cyberspace_backroom_concessions_entrance_discovered`.

The authoritative three-piece Debaucheryville NFT mapping is (canon: ruling 2026-08-01 §7c; `design/economy/legacy_vault_cards.md` §2; corrected Eurobound-hay4):

1. Absinthe Arcade claw machine: Sea-Monkeys (Mint #73), `item_sea_monkeys`; acquisition state `sea_monkeys_obtained`. ~~`item_beer_pong_saint_relic`; acquisition state `beer_pong_saint_relic_obtained`~~ struck (ruling 2026-08-01 §7c, Eurobound-hay4).
2. Velvet Curtain VIP Stall QR graffiti: The Millennium Bug (Mint #00), `item_nft_millennium_bug`; acquisition state `millennium_bug_obtained`. ~~`item_pixelated_kebab_monkey`; acquisition state `pixelated_kebab_monkey_obtained`~~ struck (ruling 2026-08-01 §7c, Eurobound-hay4).
3. Shadow Exchange ledger: Napster (Mint #01), `item_nft_napster`; acquisition state `napster_obtained`. ~~`item_vip_wristband_png`; acquisition state `vip_wristband_png_obtained`~~ struck (ruling 2026-08-01 §7c, Eurobound-hay4).

~~Struck Millennium Bug, Sea-Monkeys, and Napster route text is non-canon. Shadow Exchange's scratched Pixelated Kebab Monkey couchsurf aftermath is flavor-only and cannot grant a duplicate collection item.~~ struck (Eurobound-hay4): Millennium Bug, Sea-Monkeys and Napster are the canon pieces. CryptoBro69 mints and shills The Millennium Bug; his ex's couchsurf morning leaves a scratched Millennium Bug (`item_nft_millennium_bug_scratched`), and that alternate acquisition route stays (author, Production Desk Eurobound-g56-q1).

## Authoritative PNG Outputs

Each implementation reconciles every prior PNG document into the target below. Older non-target and hash-prefixed documents remain archival unless the user later requests deletion; they are superseded, not co-authoritative.

| Location slug | Authoritative PNG document |
|---|---|
| `astronomical_cockup_square` | `Astronomical_Cockup_Square_Complete_PNG_Asset_Requirements.md` |
| `backroom_concessions` | `Backroom_Concessions_Complete_PNG_Asset_Requirements.md` |
| `claw_machine_maintenance_closet_restroom` | `Claw_Machine_Maintenance_Closet_Restroom_Complete_PNG_Asset_Requirements.md` |
| `cyberspace_kavarna` | `Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md` |
| `euro_ink_4_less` | `Euro_Ink_4_Less_Complete_PNG_Asset_Requirements.md` |
| `hostel_midnight_checkout` | `Hostel_Midnight_Checkout_Complete_PNG_Asset_Requirements.md` |
| `internet_history_museum` | `Internet_History_Museum_Complete_PNG_Asset_Requirements.md` |
| `late_night_kebab_stand` | `Late_Night_Kebab_Stand_Complete_PNG_Asset_Requirements.md` |
| `meme_black_market` | `Meme_Black_Market_Complete_PNG_Asset_Requirements.md` |
| `midnight_munchies_general_store` | `Midnight_Munchies_General_Store_Complete_PNG_Asset_Requirements.md` |
| `mystery_meat_cart` | `Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` |
| `neon_and_chrome_boutique` | `Neon_And_Chrome_Boutique_Complete_PNG_Asset_Requirements.md` |
| `public_restroom_grease_trap_shrine` | `Public_Restroom_Grease_Trap_Shrine_Complete_PNG_Asset_Requirements.md` |
| `shadow_exchange` | `Shadow_Exchange_Complete_PNG_Asset_Requirements.md` |
| `absinthium_taproom` | `Absinthium_Taproom_Complete_PNG_Asset_Requirements.md` |
| `bohemian_trap` | `Bohemian_Trap_Complete_PNG_Asset_Requirements.md` |
| `participation_trophy` | `Participation_Trophy_Complete_PNG_Asset_Requirements.md` |
| `strobe_survival_kit` | `Strobe_Survival_Kit_Complete_PNG_Asset_Requirements.md` |
| `tap_dat_vault` | `Tap_Dat_Vault_Complete_PNG_Asset_Requirements.md` |
| `threads_and_treads` | `Threads_And_Treads_Complete_PNG_Asset_Requirements.md` |
| `three_crown_keg_haus` | `Three_Crown_Keg_Haus_Complete_PNG_Asset_Requirements.md` |
| `tram_stop_17` | `Tram_Stop_17_Complete_PNG_Asset_Requirements.md` |
| `velvet_curtain_club` | `Velvet_Curtain_Club_Complete_PNG_Asset_Requirements.md` |
| `velvet_curtain_club_vip_stall` | `Velvet_Curtain_Club_VIP_Stall_Complete_PNG_Asset_Requirements.md` |
| `ye_olde_brew_lab` | `Ye_Olde_BREW_Lab_Complete_PNG_Asset_Requirements.md` |

## Package Contracts

- `core` owns identity, access, exits, parent/destination references, mood, satire, global flags, and performance intent.
- `environment` owns lighting, audio, time/weather states, particles, environmental storytelling, hazards, and accessibility variants.
- `interactions` owns player verbs, shops, puzzles, gates, examinations, state transitions, quest bindings, and result references.
- `items` owns locally sold, found, awarded, or consumed objects and explicitly labels externally owned references.
- `location_nodes` owns the image-generation-ready spatial graph, landmarks, traversal, sightlines, occlusion, entrances, and exits.
- `npcs` owns local cast bindings, schedules, node placement, roles, ambient groups, and sprite requirements while referencing authoritative dialogue.
- `PNG_Assets` owns the reconciled visible asset inventory, dimensions or resolution class, layers, states, animations, masks, naming, and delivery checks.
- `sprite_mapping` maps asset IDs to filenames, frames, node roles, depth, lighting, UI, atlas groups, and optimization behavior.

## Naming and Reference Rules

- All seven JSON files in a package use the exact dedicated location ID.
- IDs are lowercase snake case and stable across files.
- A destination ID is never substituted for a transition-node ID.
- Asset IDs in sprite mapping must match the PNG document.
- Quest IDs and NPC IDs are referenced exactly when supplied by their authoritative sources; uncertain IDs are marked as external references rather than guessed aliases.
- Display punctuation may differ from slugs, but slugs remain consistent across the seven JSON filenames.

## Validation

For every location:

- Seven JSON files parse successfully.
- The shared location ID, slug, exits, transition destinations, item IDs, NPC IDs, node IDs, and asset IDs agree across the package.
- Gates, hours, costs, status effects, rewards, and quest states match authoritative sources.
- Parent and child locations do not duplicate one another's interiors.
- Open-air footprints do not invent inaccessible building interiors.
- PNG and sprite mapping describe the painterly HD-2D pipeline and include accessibility states for hazardous effects.
- Existing good data survives reconciliation.
- Deprecated, struck, duplicated, or document-contaminated content does not leak into authoritative files.

## Approval Boundary

This program design and its 25 child specifications must be approved before implementation plans or production package files are generated. Implementation plans will be location-specific, ordered by dependency group, and will include portfolio-wide cross-reference validation after the final package.
