# Item physical descriptions: tracker (bead Eurobound-rpac)

Author rulings, 2026-11-14, verbatim: "The writing room should be giving all items physical descriptions that go into detail complete with colors" (Desk, asset-team-qc-kokos_loco_bucket), and "Our agents need to devise descriptions for all items/assets that are vague/lack one so the asset team can successfully generate them. They should be in the items Md files" (relayed by the Sprite Development Team; on the bead and in the ledger).

Owner: the Writers' Room (moderator window eurobound-2b). Each batch is approved on the Eurobound Desk before it is written into the item .md files. A description covers looks only: shape, size, materials, colours (with hex), markings, every word of lettering spelled out, and wear. It never changes what an item is, its numbers or its story; those go to the Desk.

Built 2026-11-14 from `docs/catalog/items.md` (255 rows) and a scan of each item's doc for an appearance section (Visual Specifications / Physical Appearance / Sprite Notes / Design / The Artwork Itself) and for colour, material and size words. **described** = 50+ words with 2+ colours, a material and a size cue; **vague** = some text but short of that; **none** = no appearance section or placeholder only. The scan is a first pass: every row is re-read by hand when its batch is written. Update the Status and Batch columns as batches land.

Totals: 255 items. described 4, vague 65, none 186. Items with their own .md: 82. Items that exist only in a location JSON (no item .md): 173.

## Batch plan

1. **Batch 1: Kokos Loco Bucket.** Written; on the Desk as Eurobound-rpac-q1 (scale option + the 12-field section format).
2. **Batch 2: the Asset team's blocked icons**, worst first (their list, 2026-11-14). The descriptions also answer the Asset team's open look questions on the Desk for these items.
   - `item_shady_loot_crate_voucher` (`design/worlds/debaucheryville/items/cirque_du_shady_items.json`): no look, no printed text.
   - `item_used_glitter_hat` (same file): what kind of hat is never said.
   - `questionable_goulash` (`game/assets/data/items/consumables.json`): no pot, stew or colour; 3 refs failed.
   - `item_broken_symbol_game_boy` / `aa_broken_symbol_handheld` (`absinthe_arcade_items.json`, `key_items.json`): sticker look, which symbol, body tone, battery bay; 3 refs failed.
   - `velvet_wristband_vip` (`Assets/Graphics/items/velvet-wristband-vip.md`): wear, foil, sheen.
   - `item_beatdown_casting_flyer` (`cirque_du_shady_items.json`): text exact, paper and look missing.
   - NFTs `the_millennium_bug`, `sea_monkeys`, `napster`, `meme_lords_first_selfie`: what the icon shows.
   - **2b:** Arcade Hall props (the Sea-Monkeys prize's physical form, the VIP arrows' material, Backpack Girl's backpack). Also confirm or correct the details agents had to pick for finished icons: `item_tan_line_neon_shooter` colour, `hamagotchi_consolation` shell colour, `cracked_mirror_shard` shape and cracks, `green_fairy_essence` flask, `already_spent_credit` token, `mango_og_gushers` box.
3. **Batch 3a: the Asset team's next queue.** Debaucheryville: `i_survived_tshirt`, `rhinestone_shirt_of_shame`, `clock_snow_globe`, `leopard_print_thong`, `vip_all_access_wristband`. Then the legacy pixel icons being redone, with specs in `Assets/Graphics/items/<slug>.md`: `advil_half_empty_bottle`, `aquafina_room_temperature`, `axe_body_spray_concentrated_blast`, `bail_out_card`, `bawls_guarana_blue_bottle`, `bluetooth_earpiece_blinking_led`, `chug_of_the_gods_mystery_beer`, `disposable_camera_12_shots`, `duct_tape_half_roll`, `fake_id_laminated_at_kinkos`, `four_loko_original_recipe`, `glow_sticks_rave_quality`, `hair_gel_industrial_strength`, `monster_energy_original_formula`, `muscle_milk_chalky_vanilla`. Real brands keep their real names.
   The battle-screen status icons (20) wait on Desk asset-team-plan-battle_hud-q2 (who picks).
3. **Batch 3: items with their own .md and no icon yet** (rows marked "3" below), then 3b (.md, icon exists).
4. **Batch 4: NFTs** (`design/items/*_nft_item.md`, section "The Artwork Itself").
5. **Batch 5: brewery beers and openers** (`design/items/brewery_tour/`).
6. **Batch 6: brewery stamps** (`design/items/brewery_tour/stamp_*.md`).
7. **JSON-only items** wait on Desk Eurobound-rpac-q2: the author's ruling says the descriptions belong in the item .md files, and these items have none yet.
8. **Assets beyond items** (props and other assets with their own docs, per "items/assets"): listed after the item batches, from the Asset team's queue.

## Items

| Batch | Name | City | Kind | Doc | Status | Icon art | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Kokos Loco Bucket | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/bohemian_riviera_items.json` | none | no | json only (no item .md) |
| 3 (item .md, no icon yet) | Clock Energy Wine | Debaucheryville | Consumable / Scam Product | `design/worlds/debaucheryville/items/clock_wine_item.md` | vague | no | md: Hostel Room Appearance |
| 3 (item .md, no icon yet) | Participant Wristband | Debaucheryville | Junk item (permanent key item; no effect) | `design/items/debaucheryville_items/participant_wristband_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | The Leopard-Print Thong | Debaucheryville | Permanent Hybrid (Cosmetic + Passive) — equippable, bound to Lord Pil… | `design/items/leopard_print_thong_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | MANGO OG GUSHERS™ | General | Consumable | `design/items/general_items/mango_og_gushers_item.md` | vague | no | md: 🎨 Sprite Notes |
| 3 (item .md, no icon yet) | STRAWBERRY SHORTCAKE SPEEDCAKES™ | General | Consumable | `design/items/general_items/strawberry_shortcake_speedcakes_item.md` | vague | no | md: 🎨 Sprite Notes |
| 3 (item .md, no icon yet) | Trinity Student ID | Publandia | Permanent Cosmetic (flashed, not worn) | `design/items/publandia_items/student_id_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Bachelor Party Disposable | Sinfonia | Junk | `design/items/sinfonia_items/bachelor_party_disposable_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Bachelor Party VIP Lanyard | Sinfonia | Junk | `design/items/sinfonia_items/bachelor_party_vip_lanyard_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Half a Pair of Lederhosen | Sinfonia | Junk | `design/items/sinfonia_items/half_a_pair_of_lederhosen_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Lemon Wedge, Used | Sinfonia | Junk | `design/items/sinfonia_items/lemon_wedge_used_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Loose Breastplate Crumbs | Sinfonia | Junk | `design/items/sinfonia_items/loose_breastplate_crumbs_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Page Two of the Pass | Sinfonia | Junk | `design/items/sinfonia_items/page_two_of_the_pass_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Plastic Goblet, Sticky | Sinfonia | Junk | `design/items/sinfonia_items/plastic_goblet_sticky_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Souvenir Frame (Empty) | Sinfonia | Junk | `design/items/sinfonia_items/souvenir_frame_empty_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Splintered Mallet Head | Sinfonia | Junk | `design/items/sinfonia_items/splintered_mallet_head_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | The Gold Circle Coin | Sinfonia | Quest Item (equippable accessory — party-wide effect, never sellable,… | `design/items/gold_circle_coin_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | The Member's Card | Sinfonia | Quest Item (permanent — key-item slot, cannot be dropped, sold, or de… | `design/items/members_card_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | The Shark Fin | Sinfonia | Permanent Hybrid (Cosmetic + Passive) | `design/items/shark_fin_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3 (item .md, no icon yet) | Turnip, Bitten | Sinfonia | Junk | `design/items/sinfonia_items/turnip_bitten_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 3b (item .md, icon exists) | Hamagotchi™ Virtual Hamster Pal | General | Junk / Key Item (Non-Removable Curiosity) | `design/items/hamagotchi_consolation_item.md` | none | yes | md, no appearance section |
| 3b (item .md, icon exists) | Souvenir Champion Stein | General | Removable Inventory Item (Consumable-Use Trinket) | `design/items/summer_vacay_stein_item.md` | none | yes | md, no appearance section |
| 3b (item .md, icon exists) | VIP All-Access Wristband | General | Permanent Cosmetic / Quest Item | `design/items/vip_wristband_item.md` | vague | yes | md: 🎨 Visual Specifications; Physical Appearance |
| 3b (item .md, icon exists) | The Brewery Passport Book | Publandia |  | `design/items/brewery_passport_book_item.md` | none | yes | md, no appearance section |
| 4 (NFTs) | Napster | Debaucheryville |  | `design/items/napster_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 4 (NFTs) | The Millennium Bug | Debaucheryville |  | `design/items/millennium_bug_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 4 (NFTs) | Pogs (the Slammer) | Publandia |  | `design/items/pogs_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 4 (NFTs) | "She Thinks My Tractor's Sexy" (Mint #42) | Sinfonia | Quest Item (permanent — key-item slot, cannot be dropped, sold, or de… | `design/items/tractor_nft_item.md` | vague | no | md: 🎨 Visual Specifications; Physical Appearance |
| 4 (NFTs) | Crystal Pepsi | Sinfonia |  | `design/items/crystal_pepsi_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 4 (NFTs) | Holographic Charizard | Sinfonia |  | `design/items/holographic_charizard_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 4 (NFTs) | Winamp | Sinfonia |  | `design/items/winamp_nft_item.md` | vague | no | md: 3. The Artwork Itself |
| 5 (beers) | Absinthe Lager | Debaucheryville | Signature Beer | `design/items/brewery_tour/beer_absinthium_taproom_item.md` | none | yes | md: PNG Assets |
| 5 (beers) | Blockchain Bock | Debaucheryville | Signature Beer | `design/items/brewery_tour/beer_ye_olde_brew_lab_item.md` | none | yes | md: PNG Assets |
| 5 (openers) | Bottle Opener: The Absinthium Taproom | Debaucheryville | Brewery Opener | `design/items/brewery_tour/opener_absinthium_taproom_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Tap Dat Vault | Debaucheryville | Brewery Opener | `design/items/brewery_tour/opener_tap_dat_vault_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: Three-Crown Keg Haus | Debaucheryville | Brewery Opener | `design/items/brewery_tour/opener_three_crown_keg_haus_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: Ye Olde B.R.E.W. Lab | Debaucheryville | Brewery Opener | `design/items/brewery_tour/opener_ye_olde_brew_lab_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (beers) | Iron Gut Tripel | Debaucheryville | Signature Beer | `design/items/brewery_tour/beer_three_crown_keg_haus_item.md` | none | yes | md: PNG Assets |
| 5 (beers) | Vape Stout | Debaucheryville | Signature Beer | `design/items/brewery_tour/beer_tap_dat_vault_item.md` | none | yes | md: PNG Assets |
| 5 (beers) | Academic Amber | Publandia |  | `design/items/brewery_tour/beer_trinity_of_pints_item.md` | none | no | md: PNG Assets |
| 5 (openers) | Bottle Opener: Shenanigans | Publandia |  | `design/items/brewery_tour/opener_shenanigans_item.md` | vague | no | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Blarney Trap | Publandia |  | `design/items/brewery_tour/opener_blarney_trap_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Stoutworks Brewery | Publandia |  | `design/items/brewery_tour/opener_stoutworks_brewery_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: Trinity of Pints | Publandia |  | `design/items/brewery_tour/opener_trinity_of_pints_item.md` | vague | no | md: Design; PNG Assets |
| 5 (beers) | The Fool's Gold | Publandia |  | `design/items/brewery_tour/beer_shenanigans_item.md` | none | no | md: PNG Assets |
| 5 (beers) | The Sweet Surrender | Publandia |  | `design/items/brewery_tour/beer_blarney_trap_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Vat Master's Reserve | Publandia |  | `design/items/brewery_tour/beer_stoutworks_brewery_item.md` | none | no | md: PNG Assets |
| 5 (openers) | Bottle Opener: Bottoms Down | Shamsterdam |  | `design/items/brewery_tour/opener_bottoms_down_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Hoisted Pint | Shamsterdam |  | `design/items/brewery_tour/opener_hoisted_pint_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Mad Monarch's Wit-tea Party | Shamsterdam |  | `design/items/brewery_tour/opener_mad_monarchs_wit_tea_party_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Wobbly Windmill Brewery | Shamsterdam |  | `design/items/brewery_tour/opener_wobbly_windmill_brewery_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (beers) | Load-Bearing Tripel | Shamsterdam |  | `design/items/brewery_tour/beer_hoisted_pint_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Oude Genever | Shamsterdam |  | `design/items/brewery_tour/beer_bottoms_down_item.md` | vague | no | md: PNG Assets |
| 5 (beers) | Six O'Clock Wit | Shamsterdam |  | `design/items/brewery_tour/beer_mad_monarchs_wit_tea_party_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Windmill Grist | Shamsterdam |  | `design/items/brewery_tour/beer_wobbly_windmill_brewery_item.md` | vague | no | md: PNG Assets |
| 5 (openers) | Bottle Opener: Crown & Cask | Sinfonia |  | `design/items/brewery_tour/opener_crown_and_cask_item.md` | vague | yes | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Dancing Stein | Sinfonia |  | `design/items/brewery_tour/opener_dancing_stein_item.md` | vague | no | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Moderato Pub | Sinfonia |  | `design/items/brewery_tour/opener_moderato_pub_item.md` | vague | no | md: Design; PNG Assets |
| 5 (openers) | Bottle Opener: The Standing Ovation | Sinfonia |  | `design/items/brewery_tour/opener_standing_ovation_item.md` | vague | no | md: Design; PNG Assets |
| 5 (beers) | Curtain Call Copper | Sinfonia |  | `design/items/brewery_tour/beer_standing_ovation_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Heir Apparent Ale | Sinfonia |  | `design/items/brewery_tour/beer_crown_and_cask_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Tempo Tantrum | Sinfonia |  | `design/items/brewery_tour/beer_moderato_pub_item.md` | none | no | md: PNG Assets |
| 5 (beers) | Waltz Weizen | Sinfonia |  | `design/items/brewery_tour/beer_dancing_stein_item.md` | none | no | md: PNG Assets |
| 6 (stamps) | Stamp: The Absinthium Taproom | Debaucheryville | Brewery Stamp | `design/items/brewery_tour/stamp_absinthium_taproom_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Tap Dat Vault | Debaucheryville | Brewery Stamp | `design/items/brewery_tour/stamp_tap_dat_vault_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Three-Crown Keg Haus | Debaucheryville | Brewery Stamp | `design/items/brewery_tour/stamp_three_crown_keg_haus_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Ye Olde B.R.E.W. Lab | Debaucheryville | Brewery Stamp | `design/items/brewery_tour/stamp_ye_olde_brew_lab_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Shenanigans | Publandia |  | `design/items/brewery_tour/stamp_shenanigans_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Blarney Trap | Publandia |  | `design/items/brewery_tour/stamp_blarney_trap_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Stoutworks Brewery | Publandia |  | `design/items/brewery_tour/stamp_stoutworks_brewery_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Trinity of Pints | Publandia |  | `design/items/brewery_tour/stamp_trinity_of_pints_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Bottoms Down | Shamsterdam |  | `design/items/brewery_tour/stamp_bottoms_down_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Hoisted Pint | Shamsterdam |  | `design/items/brewery_tour/stamp_hoisted_pint_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Mad Monarch's Wit-tea Party | Shamsterdam |  | `design/items/brewery_tour/stamp_mad_monarchs_wit_tea_party_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Wobbly Windmill Brewery | Shamsterdam |  | `design/items/brewery_tour/stamp_wobbly_windmill_brewery_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: Crown & Cask | Sinfonia |  | `design/items/brewery_tour/stamp_crown_and_cask_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Dancing Stein | Sinfonia |  | `design/items/brewery_tour/stamp_dancing_stein_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Moderato Pub | Sinfonia |  | `design/items/brewery_tour/stamp_moderato_pub_item.md` | vague | no | md: Design; PNG Assets |
| 6 (stamps) | Stamp: The Standing Ovation | Sinfonia |  | `design/items/brewery_tour/stamp_standing_ovation_item.md` | vague | no | md: Design; PNG Assets |
| JSON-only: waits on Desk rpac-q2 | 2 AM Identity Overhaul | Debaucheryville | Service | `design/worlds/debaucheryville/items/threads_and_treads_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | AIM Away-Message Icon | Debaucheryville | Lore Collectible | `design/worlds/debaucheryville/items/meme_black_market_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Absinthe Arcade Ticket | Debaucheryville | Location Currency | `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Absinthe Arcade Token | Debaucheryville | Location Currency | `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | vague | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Authentic Euromemeian Tattoo | Debaucheryville | Permanent Cosmetic | `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Authentic-ish Absinthe | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/bohemian_trap_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Ballad of the Bros | Debaucheryville | Quest Owned Collectible Reference | `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Belly Of Chadz | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Bravery Lollipop | Debaucheryville | Consumable Prop | `design/worlds/debaucheryville/items/euro_ink_4_less_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Broken Handheld with Weird Symbols | Debaucheryville | Cross City Quest Item | `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | vague | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Broken Prize Tag | Debaucheryville | Lore Item | `design/worlds/debaucheryville/items/claw_machine_maintenance_closet_restroom_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Budget Earplugs | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Budget Flash Tattoo | Debaucheryville | Repeatable Cosmetic Service | `design/worlds/debaucheryville/items/euro_ink_4_less_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Chain Wallet | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/threads_and_treads_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Chrome Club Shoes | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/neon_and_chrome_boutique_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Clock Commemorative Plate | Debaucheryville | Throwable | `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Clock Snow Globe | Debaucheryville | Junk | `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Clown Dog Deluxe | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/mystery_meat_cart_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Club Flyer Stack | Debaucheryville | Quest Reference | `design/worlds/debaucheryville/items/velvet_curtain_club_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Corrupted Reaction GIF | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/meme_black_market_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Counterfeit Lucky Charm | Debaucheryville | Barter Stock | `design/worlds/debaucheryville/items/shadow_exchange_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | CryptoDöner Box | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/backroom_concessions_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Cursed Sink Coin | Debaucheryville | Quest Curio | `design/worlds/debaucheryville/items/public_restroom_grease_trap_shrine_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Dancing Baby Charm | Debaucheryville | Meme Trinket | `design/worlds/debaucheryville/items/meme_black_market_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Designer Strobe Shades | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/neon_and_chrome_boutique_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Direct-Purchase Participation Bag | Debaucheryville | Prize | `design/worlds/debaucheryville/items/participation_trophy_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Disposable ICQ Login | Debaucheryville | Service | `design/worlds/debaucheryville/items/cyberspace_kavarna_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Doner of Illusions | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/mystery_meat_cart_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Dorm Bed Booking | Debaucheryville | Service | `design/worlds/debaucheryville/items/hostel_midnight_checkout_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Drunken Sauce Shot | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Emergency Energy Drink | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Emergency Hygiene Kit | Debaucheryville | Utility | `design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | EuroMeat Pocket | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Foam Earplugs | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Genuine-ish Leather Jacket | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/threads_and_treads_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Glizzénstein's Brain Brat | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/mystery_meat_cart_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Glow Harness | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/neon_and_chrome_boutique_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Glow Stick Bundle | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Gutbuster Wrap | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Half-Chewed Antacid | Debaucheryville | Examinable Prop | `design/worlds/debaucheryville/items/public_restroom_grease_trap_shrine_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Half-Smoked Cigar | Debaucheryville | Junk | `design/worlds/debaucheryville/items/cirque_du_shady_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Heat-Lamp Kebab | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Hemingway Intended Reserve | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/bohemian_trap_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | House Absinthe | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/bohemian_trap_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | I Survived The Cock-Up T-Shirt | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Impossible Grand Prize | Debaucheryville | Display Only | `design/worlds/debaucheryville/items/participation_trophy_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Infinite Badger Loop | Debaucheryville | Meme Trinket | `design/worlds/debaucheryville/items/meme_black_market_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Instant Noodles | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/midnight_munchies_general_store_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Internet History Museum Brochure | Debaucheryville | Lore Item | `design/worlds/debaucheryville/items/internet_history_museum_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Jiří's Blessing | Debaucheryville | Permanent Buff | `design/worlds/debaucheryville/items/tram_stop_17_items.json` | vague | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Lambsomnia Special | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Level Seven Wristbands | Debaucheryville | Quest Reference | `design/worlds/debaucheryville/items/velvet_curtain_club_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | MIDI Archive Token | Debaucheryville | Quest Reference | `design/worlds/debaucheryville/items/internet_history_museum_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Meatball on a Lollipop Stick | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/mystery_meat_cart_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | MegaMix Box (Regret Platter) | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Meme Lord's First Selfie | Debaucheryville | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Mixed Currency Bundle | Debaucheryville | Exchange Input | `design/worlds/debaucheryville/items/shadow_exchange_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Moët 2003: Spite Reserve | Debaucheryville | Examinable Prop | `design/worlds/debaucheryville/items/velvet_curtain_club_vip_stall_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Musician Earplugs | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Mysterious Carnival Trinket | Debaucheryville | Prize | `design/worlds/debaucheryville/items/participation_trophy_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Mystery Fridge Food | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/hostel_midnight_checkout_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Mystery Meat Corndog | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/cirque_du_shady_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | NFT Affinity Protection | Debaucheryville | Non Item Buff | `design/worlds/debaucheryville/items/velvet_curtain_club_vip_stall_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Night Combat Boots | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/threads_and_treads_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Night Survival Pouch | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | One Regret-Free Kebab Coupon | Debaucheryville | Comedy Consumable Coupon | `design/worlds/debaucheryville/items/absinthe_arcade_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Patch-Ready Denim Vest | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/threads_and_treads_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Plastic Participation Medal | Debaucheryville | Prize | `design/worlds/debaucheryville/items/participation_trophy_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Premium Wrist Cuff | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/neon_and_chrome_boutique_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Private Room Booking | Debaucheryville | Service | `design/worlds/debaucheryville/items/hostel_midnight_checkout_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Programmable LED Glasses | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/neon_and_chrome_boutique_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Protocol Pocket | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/backroom_concessions_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Questionable Aftercare Packet | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/euro_ink_4_less_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Quiet-ish Bed Booking | Debaucheryville | Service | `design/worlds/debaucheryville/items/hostel_midnight_checkout_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | RAM Chips & Dip | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/backroom_concessions_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Sausage of Suspicion | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/mystery_meat_cart_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Shadow Contract | Debaucheryville | Quest Document | `design/worlds/debaucheryville/items/shadow_exchange_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Shady Loot Crate Voucher | Debaucheryville | Quest Item | `design/worlds/debaucheryville/items/cirque_du_shady_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Shady Productions Casting-Call Flyer | Debaucheryville | Quest Item | `design/worlds/debaucheryville/items/cirque_du_shady_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Slightly Damp Consolation Plush | Debaucheryville | Prize | `design/worlds/debaucheryville/items/participation_trophy_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Strobe-Resistant Shades | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/strobe_survival_kit_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Temporary Clock Tattoo | Debaucheryville | Cosmetic | `design/worlds/debaucheryville/items/astronomical_cockup_square_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Terminal Rental - All Night | Debaucheryville | Service | `design/worlds/debaucheryville/items/cyberspace_kavarna_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Terminal Rental - One Hour | Debaucheryville | Service | `design/worlds/debaucheryville/items/cyberspace_kavarna_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Lord Pilsner Special | Debaucheryville | Permanent Cosmetic Service | `design/worlds/debaucheryville/items/euro_ink_4_less_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Tan Line Neon Shooter | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/bohemian_riviera_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Thermal Paste Sundae | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/backroom_concessions_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Traditional Ritual Experience | Debaucheryville | Service | `design/worlds/debaucheryville/items/bohemian_trap_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Used Glitter Hat | Debaucheryville | Equipment | `design/worlds/debaucheryville/items/cirque_du_shady_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Vampire Slayer Garlic Fries | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Velvet House Drink | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/velvet_curtain_club_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Warm 2004 Kebab Receipt | Debaucheryville | Lore Item | `design/worlds/debaucheryville/items/public_restroom_grease_trap_shrine_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Yogurt Reboot | Debaucheryville | Consumable | `design/worlds/debaucheryville/items/late_night_kebab_stand_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | "ASK ME ABOUT TOKENS" Pin | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Absinthe Shot | General | Engine entry | `game/assets/data/items/consumables.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Already-Spent Credit | General | Engine entry | `game/assets/data/items/consumables.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Auto-Gratuity Receipt | General | Engine entry | `game/assets/data/items/key_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Chuck E. Cheese Plush | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Fangs for Nothing | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Five-Finger Lint Discount | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Flamingo Hydro Bro 2000 | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Forty-Eight-Hour Tramp Stamp | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Fuchsia Foot of Fortune | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Fuzzy Dice of Doubt | General | Engine entry | `game/assets/data/items/key_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Highlighter Hydro Bro 2000 | General | Engine entry | `game/assets/data/items/key_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Lukewarm Kebab | General | Engine entry | `game/assets/data/items/consumables.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Minty the Rare Mint Bunny | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Mugshot Mandy | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Neon Wrist Guillotine | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Paraffin Pucker | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Pets.con the Sock Hound | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Pinky Promise Prison | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Pre-Emptive Perry | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Promise-ish Ring | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Questionable Goulash | General | Engine entry | `game/assets/data/items/consumables.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Revision Sticker | General | Engine entry | `game/assets/data/items/consumables.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Shell Company Business Card | General | Engine entry | `game/assets/data/items/key_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Sit-Down Comedy Special | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Sixty-Minute Emerald | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Snorty the Bouncer Badger | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Sobriety Test Deluxe | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Terminal Velocity Terry | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Noise Violation | General | Engine entry | `game/assets/data/items/key_items.json` | none | yes | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Nordic Vacuum Warranty | General | Collectible Nft | `design/items/faberge_egg_item.json` | vague | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Two-Grand Tie-Dye Tee | General | Engine entry | `game/assets/data/items/key_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | America Online | Publandia | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Bradley's Roundabout Photo | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Dashboard Rosary Beads | Publandia | Rental Addon | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Dried Flower from Margaret's Crown | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | GPS Navigation | Publandia | Rental Addon | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | GPS Thank You Note | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Gift Shop Grand Opening Flyer (1994) | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Kevin's Spare L-Plate | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Map Book | Publandia | Rental Addon | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Paddy's Premium Motors Rental Keys | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Premium Insurance | Publandia | Rental Addon | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Road Warrior Medal | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Roundabout Veteran Badge | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Seán's Hand-Drawn Exit Map | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Emerald Dream (Premium) | Publandia | Rental Vehicle | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Full Irish (Luxury) | Publandia | Rental Vehicle | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Lucky Charm (Standard) | Publandia | Rental Vehicle | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Polyester Reserve | Publandia | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Shamrock (Economy) | Publandia | Rental Vehicle | `design/worlds/publandia/items/paddys_premium_motors_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Tour Bus Orientation Pamphlet | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Tuft of Sheep Wool | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Wedding Tin Can (1987) | Publandia |  | `design/worlds/publandia/items/cloverleaf_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Who You Gonna Call? | Publandia | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | FuncoLand Nostalgia Series | Relic | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Cargo Parade Invitation | Shamsterdam |  | `design/worlds/shamsterdam/items/central_shamsterdam_bike_crossing_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Proof of Dairy Culture | Shamsterdam | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Bedrock Chewable Reserve | Shamsterdam | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | The Diapered Vector Loop | Shamsterdam | Engine entry | `game/assets/data/nft/legacy_vault.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Bradley's Harness | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Café Chaos Badge | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Café Damage Receipt | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Chess Notation Card | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Classical Sheet Music | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Fountain Coins | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Gustav's Opera Cape | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Hans-Jürgen's Schnapps | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Horse Costume (Two-Person) | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Horse Whisperer Badge | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Lucky Coin | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Patron of the Arts | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Photo of Gustav | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Photo: Gustav with Cream on Face | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Photograph of 'Emperor's Letter' | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Pocket Skittles | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Property Damage Bill | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Shrine Offerings | Sinfonia |  | `design/worlds/sinfonia/items/opera_house_plaza_items.json` | none | no | json only (no item .md) |
| JSON-only: waits on Desk rpac-q2 | Valued Patron Card | Sinfonia |  | `design/worlds/sinfonia/items/cafe_sachertorte_items.json` | none | no | json only (no item .md) |
| check | Sea-Monkeys | Debaucheryville | Quest item, permanent: unique_quest_collectible, not stackable, not c… | `design/items/sea_monkeys_nft_item.md` | described | no | md: 3. The Artwork Itself |
| check | Summer Vacation Trivia Champ Badge | General | Permanent Hybrid (Cosmetic + Passive) | `design/items/trivia_champ_badge_item.md` | described | yes | md: 🎨 Visual Specifications; Physical Appearance |
| check | Bottle Opener Keychain | Publandia | Hybrid (Permanent Cosmetic + Quest Container) | `design/items/bottle_opener_keychain_item.md` | described | no | md: 🎨 Visual Specifications; Physical Appearance — PROPOSED Prod |
| check | Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes | Sinfonia | Permanent Hybrid (Novelty + Use Effect) — not a consumable; the carto… | `design/items/candy_smokes_item.md` | described | no | md: 🎨 Visual Specifications; Physical Appearance |
