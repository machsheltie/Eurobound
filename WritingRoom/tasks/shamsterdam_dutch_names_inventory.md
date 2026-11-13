# Shamsterdam Dutch names: inventory

Bead Eurobound-ucpf (P1). Read-only inventory, 2026-11-13. Nothing was renamed and no replacement names are proposed here.

**Author, 2026-11-13:** "I want all dutch names from shamsterdam rethought. I don't know where they came from but I never asked for dutch names. They should be americanized, satirical, parody type names that are whitty, clever, and lean hard into what each place is. They're supposed to be funny. Not highbrow." On the Desk: "We do not use official looking names in dutch." Ledger entry: `docs/superpowers/NEXT_WORK.md:853-857`.

## How this was built

- Sources: every file in `design/worlds/shamsterdam/` (place docs, npcs, PNG_Assets, core, environment, events, interactions, items, location_nodes, sprite_mapping), the Shamsterdam quests in `design/Quests/shamsterdam/`, the Shamsterdam asset-team plans in `dev/asset_team/plans/`, and engine data in `game/assets/data/`. `design/legacy/`, `design/World Design/` and worktrees were skipped.
- "Defined at" is the heading or first defining line in the canonical file.
- "Other files" counts files outside the canonical one that match the name, across `design/`, `docs/`, `production/`, `tools/` (minus generated board output and the canon index), `dev/`, `game/`, `WritingRoom/` and `marketing/`. It counts files, not lines.
- "Ids" are snake_case ids containing the name, taken from JSON/GDScript data and from documented ID lines in `design/`, `game/` and `dev/`. Files under `game/` and asset-team plan stems are listed too. "none" means the name has no id; most venues are referenced by an English or slug id instead.
- "Author-ruled before" is an exact search of the rulings ledger (`docs/superpowers/NEXT_WORK.md` and the economy spec), cross-checked with `tools/canon_index` `--rulings` on the main place names. "No" means no ledger line names it.
- English meanings are literal translations of the Dutch.

## Places (venues, districts, zones, sub-areas, aliases) (47)

Includes the asset team's plan names ('t Wilde Gokje, Bar De Laatste Waarschuwing, Erotiek & Zo, Muntje Erin, De Wachtrij, Het Rode Loket and the other Roodelicht sub-locations). Their only design source is `roodelicht_row_district.md`; each also has a plan in `dev/asset_team/plans/`.

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| Café de Schaamte | Café of Shame | Canal-side outdoor café; main quest hub and Agent Havok's base | `design/worlds/shamsterdam/cafe_de_schaamte.md:1` | 24 | `shamsterdam_cafe_de_schaamte_01`, `shamsterdam_canalring_cafe_schaamte_01`<br>in plans: `cafe_de_schaamte` | No |
| De Botanische Leugen | The Botanical Lie | Floating flower-market stall selling tulip bulbs that will never survive US customs | `design/worlds/shamsterdam/de_botanische_leugen.md:1` | 9 | `de_botanische_leugen`<br>in plans: `de_botanische_leugen` | No |
| De Groene Gids | The Green Guide | Flagship tourist coffeeshop chain ("the Starbucks of getting high") | `design/worlds/shamsterdam/de_groene_gids.md:1` | 32 | `de_groene_gids`, `shamsterdam_coffeeshop_groene_gids_01`<br>game/: `assets/data/skills/status_effects.json`<br>in plans: `de_groene_gids` | No |
| De Zilte Waarheid | The Salty Truth | Harbour raw-herring stand; the Herring Challenge | `design/worlds/shamsterdam/de_zilte_waarheid.md:1` | 15 | `de_zilte_waarheid`<br>game/: `assets/data/skills/status_effects.json`<br>in plans: `de_zilte_waarheid` | Named in a mechanics ruling only (Canal Courage cure, NEXT_WORK.md:849). Related: "herring vendor" is in the Dutch heritage gag cluster, KEEP AS-IS (NEXT_WORK.md:154); that ruling covers the content, not the name |
| Frietomat | Fries-o-mat (Dutch "friet" + automat) | 24-hour wall-of-hatches automat fast food (croquettes, frikandel) | `design/worlds/shamsterdam/frietomat.md:1` | 48 | `discover_frietomat_shortcut`, `exit_probability_frietomat`, `frietomat_backdoor`, `frietomat_emergence`, `frietomat_hidden` (+12 more)<br>game/: `assets/data/navigation/voetgangerstunnel.json`, `assets/data/skills/status_effects.json`<br>in plans: `frietkot_de_vette_vinger`, `frietomat`, `voetgangerstunnel` | **Yes.** Author-minted, Round v21 (NEXT_WORK.md:481: FEBO Automat -> Frietomat, "Dutch friet plus Frito"); croquette price joke Round v24 (NEXT_WORK.md:508) |
| Kapsalon Koning | Kapsalon King ("kapsalon" = barbershop, also the real dish) | Late-night kapsalon stand run by Big Wim | `design/worlds/shamsterdam/kapsalon_koning.md:1` | 13 | `kapsalon_koning`, `shamsterdam_latenight_kapsalon_koning_01`<br>in plans: `kapsalon_koning`, `leemans_doner_palace` | No |
| Klompen Konfessional | Clogs Confessional (Dutch "klompen" + mock-Dutch spelling of Confessional) | Wooden-shoe souvenir shop selling clogs that end up on shelves | `design/worlds/shamsterdam/klompen_konfessional.md:1` | 5 | `klompen_konfessional`, `shamsterdam_tourist_klompen_konfessional_01`<br>in plans: `klompen_konfessional` | Related: "Klompen shop" is in the Dutch heritage gag cluster, KEEP AS-IS (NEXT_WORK.md:154); that ruling covers the content, not the name |
| Voetgangerstunnel | Pedestrian Tunnel | Underground tunnel maze; the city's navigation-roll hazard | `design/worlds/shamsterdam/voetgangerstunnel.md:1` | 29 | `shamsterdam_voetgangerstunnel_01`, `shamsterdam_voetgangerstunnel_bike_parking_01`, `shamsterdam_voetgangerstunnel_correct_exit_01`, `shamsterdam_voetgangerstunnel_entrance_01`, `shamsterdam_voetgangerstunnel_intersection_01` (+8 more)<br>game/: `assets/data/world_data/quest_flags.json`, `core/navigation_roll.gd`<br>in plans: `voetgangerstunnel` | Named in a mechanics ruling only (navigation odds, NEXT_WORK.md:848); the name itself was never ruled |
| Roodelicht Row | Red Light Row ("roodelicht" is a mock-Dutch compound) | The red-light district and its ten-stage Cascade night | `design/worlds/shamsterdam/roodelicht_row_district.md:1` | 40 | `exit_probability_roodelicht`, `roodelicht_row`, `roodelicht_row_district`, `roodelicht_row_exit`, `roodelicht_row_surface` (+8 more)<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `casa_rose_erotic_theater`, `central_shamsterdam_bike_crossing`, `de_roze_rondleiding` (+4) | No |
| Leeman's Döner Paleis | Leeman's Döner Palace (Dutch "paleis") | Dutch-Turkish alias of Leeman's Döner Palace, Mehmet's late-night döner stand | `design/worlds/shamsterdam/leemans_doner_palace.md:8` | 0 | none | No |
| Fietsbel & Meer | Bike Bell & More | Dutch alias of Bicycle Warfare Accessories (bells and gear for tourist renters) | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:8` | 2 | in plans: `bicycle_warfare_accessories` | No |
| Schrödinger's Aandenken | Schrödinger's Souvenir | Dutch alias of Schrödinger's Souvenir, the CBD/hemp legal-grey-area shop | `design/worlds/shamsterdam/schrodingers_souvenir.md:8` | 0 | none | No |
| De Ongemakkelijke Truffel | The Awkward Truffle | Dutch alias of The Awkward Truffle, the anatomical-chocolate shop | `design/worlds/shamsterdam/the_awkward_truffle.md:8` | 0 | none | No |
| Fiets Verhuur | Bike Rental | Dutch name (and sign/mat text) of Shamsterdam Bike Rental | `design/worlds/shamsterdam/shamsterdam_bike_rental.md:8` | 3 | in plans: `shamsterdam_bike_rental` | No |
| Pannenkoekhuis | Pancake House | Dutch name of The Pancake House | `design/worlds/shamsterdam/the_pancake_house.md:8` | 0 | none | Related: "Pancake House" is in the Dutch heritage gag cluster, KEEP AS-IS (NEXT_WORK.md:154); content, not the Dutch alias |
| De Stroopwafel Kar | The Stroopwafel Cart | Mobile stroopwafel cart run by Tante Bep (display name is Dutch) | `design/worlds/shamsterdam/stroopwafel_cart.md:1` | 2 | in plans: `stroopwafel_cart` | No |
| Veilig-o-Maat | Safe-o-Mat | Brand of the 34-machine city-wide condom vending network | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:6` | 4 | `shamsterdam_system_veiligomaat_01`<br>in plans: `i_shamsterdam_sign_plinth`, `shamsterdam_condom_machines` | No |
| Centraal Chaos | Central Chaos (Dutch "centraal") | Central transit hub / RED danger zone; a tunnel exit | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:11` | 9 | `centraal_chaos`<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `bicycle_warfare_accessories`, `voetgangerstunnel` | No |
| Verdoemplein | Damnation Square (pun on the real Dam square) | RED-zone central square on the bike danger map; cart stop | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:81` | 5 | in plans: `bicycle_warfare_accessories`, `stroopwafel_cart` | No |
| De Kuipmarkt | The Tub Market (pun on the real Albert Cuyp market) | Street market where the stroopwafel cart parks mornings | `design/worlds/shamsterdam/stroopwafel_cart.md:11` | 2 | in plans: `stroopwafel_cart` | No |
| Wandelpark | Walking Park (pun on the real Vondelpark) | GREEN beginner zone on the bike danger map; park entrance | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:290` | 7 | in plans: `bicycle_warfare_accessories`, `stroopwafel_cart` | No |
| Museum de Gekke Schilder | Museum of the Mad Painter | Museum Mile selfie museum nobody enters; gift shop outsells admissions | `design/worlds/shamsterdam/shamsterdam.md:50` | 1 | in plans: `museum_de_gekke_schilder` | No |
| Het Rijke Museum | The Rich Museum (pun on the real Rijksmuseum) | Museum Mile museum whose name Chadwick misspells three ways | `design/worlds/shamsterdam/shamsterdam.md:51` | 4 | in plans: `het_rijke_museum`, `the_dong_palace` | No |
| De Etalagegang | The Display Corridor | Roodelicht Zone 1, the red-lit window corridor | `design/worlds/shamsterdam/roodelicht_row_district.md:90` | 1 | in plans: `frietkot_de_vette_vinger` | No |
| Het Plein van Niks | The Square of Nothing | Roodelicht Zone 2, the paved square (bench, bin, dry fountain, duck) | `design/worlds/shamsterdam/roodelicht_row_district.md:99` | 2 | in plans: `de_roze_rondleiding`, `de_zweetkelder` | No |
| Achterom | Round the Back | Roodelicht Zone 3, the un-red-lit back street (clinic, bakery) | `design/worlds/shamsterdam/roodelicht_row_district.md:107` | 2 | in plans: `de_kliniek_van_achterom` | No |
| De Achterdeur | The Back Door | Roodelicht Zone 4, the service layer behind the venues | `design/worlds/shamsterdam/roodelicht_row_district.md:114` | 0 | none | No |
| De Wachtrij | The Queue | Arrivals-triage queue at the Zone 1 entrance; Rutger and his chart (Cascade stage 1) | `design/worlds/shamsterdam/roodelicht_row_district.md:347` | 7 | in plans: `de_wachtrij`, `de_zweetkelder`, `het_rode_loket` (+1) | Named in the 2026-11-13 no-Dutch ruling itself (NEXT_WORK.md:856): flagged for rename |
| Het Rode Loket | The Red Counter | "The Yes Desk": the booking counter that sells everything (Cascade stage 2) | `design/worlds/shamsterdam/roodelicht_row_district.md:360` | 5 | `het_rode_loket`<br>in plans: `de_roze_rondleiding`, `de_wachtrij`, `het_rode_loket` | No |
| Erotiek & Zo | Erotica & Such | Sex-toy emporium; Bradley buys The Item (Cascade stage 3) | `design/worlds/shamsterdam/roodelicht_row_district.md:377` | 5 | in plans: `de_wachtrij`, `erotiek_en_zo`, `t_wilde_gokje` | No |
| 't Wilde Gokje | The Wild Guess | Smart shop (psychedelics) with the dosing chart (Cascade stage 4) | `design/worlds/shamsterdam/roodelicht_row_district.md:402` | 3 | in plans: `t_wilde_gokje` | No |
| Bar De Laatste Waarschuwing | Bar The Last Warning | Eleven-stool shot bar run by Bertus (Cascade stage 5) | `design/worlds/shamsterdam/roodelicht_row_district.md:423` | 2 | in plans: `bar_de_laatste_waarschuwing` | No |
| Het Rode Winkeltje | The Little Red Shop | District gift shop: ponchos, t-shirts, keyrings (Cascade stage 6) | `design/worlds/shamsterdam/roodelicht_row_district.md:459` | 4 | `het_rode_winkeltje`<br>in plans: `het_rode_winkeltje` | No |
| Muntje Erin | Coin In ("Insert Coin") | Coin-op peep booths; Bradley's back goes (Cascade stage 7) | `design/worlds/shamsterdam/roodelicht_row_district.md:483` | 4 | in plans: `de_zweetkelder`, `muntje_erin` | No |
| De Zweetkelder | The Sweat Cellar | Nine-steps-down cellar club with a shirt check (Cascade stages 8, 14) | `design/worlds/shamsterdam/roodelicht_row_district.md:509` | 4 | in plans: `de_roze_rondleiding`, `de_zweetkelder`, `muntje_erin` | No |
| Frietkot De Vette Vinger | Fry Shack The Greasy Finger | 3 AM fry hatch in a brick wall (Cascade stage 10) | `design/worlds/shamsterdam/roodelicht_row_district.md:534` | 2 | in plans: `frietkot_de_vette_vinger` | No |
| Het Warme Bad | The Warm Bath | Members bathhouse with the towel rules (Cascade stage 11) | `design/worlds/shamsterdam/roodelicht_row_district.md:560` | 2 | `het_warme_bad`<br>in plans: `het_warme_bad` | No |
| De Roze Rondleiding | The Pink Guided Tour | Red-light walking tour with numbered paddles, run by Nienke | `design/worlds/shamsterdam/roodelicht_row_district.md:587` | 3 | in plans: `de_roze_rondleiding` | No |
| De Bijna-Toiletten | The Almost-Toilets | Coin pay toilets with no change (Cascade stage 13) | `design/worlds/shamsterdam/roodelicht_row_district.md:603` | 2 | none | No |
| De Kliniek van Achterom | The Clinic Round the Back | Walk-in clinic in Zone 3; "WHY IT IS WORSE AT THIRTY-NINE" (Cascade stage 15) | `design/worlds/shamsterdam/roodelicht_row_district.md:617` | 2 | `shamsterdam_npc_roosmarijn_kliniek_01`<br>in plans: `de_kliniek_van_achterom` | No |
| De Grote Fontein | The Big Fountain | Four-metre chocolate-phallus fountain on the Dong Palace forecourt | `design/worlds/shamsterdam/shamsterdam.md:53` | 6 | none | No |
| Fontein van de Gulle Gever | Fountain of the Generous Giver | Official (unused) plaque name of the fountain | `design/worlds/shamsterdam/the_dong_palace.md:48` | 1 | in plans: `the_dong_palace` | No |
| De Cacaogalerij | The Cocoa Gallery | Dong Palace ground-floor gallery of artisan chocolate genitalia | `design/worlds/shamsterdam/the_dong_palace.md:105` | 4 | in plans: `the_dong_palace` | No |
| De Mechanische Vleugel | The Mechanical Wing | Dong Palace first floor: the Victorian peep-show collection | `design/worlds/shamsterdam/the_dong_palace.md:118` | 4 | in plans: `the_dong_palace` | No |
| Ervaar de Tempel | Experience the Temple | Dong Palace second floor: photo ops and exit | `design/worlds/shamsterdam/the_dong_palace.md:133` | 2 | in plans: `the_dong_palace` | No |
| Vooruitgang | Progress | Captain Noortje's permanently moored houseboat (couchsurf host) | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:387` | 0 | none | No |
| Proeflokaal 't Kansen (retired) | Tasting Room The Chances | Retired former name of Bottoms Down; still in docs | `docs/superpowers/NEXT_WORK.md:488` | 5 | none | **Yes, already renamed** to Bottoms Down (NEXT_WORK.md:116, :488). Residue: economy spec :180 still lists it; "proeflokaal" wording remains in bottoms_down.md:268, :316, :426, :431 and its PNG doc |

## NPC and business titles and nicknames (9)

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| Burgemeester van Schande | Mayor of Shame | Shamsterdam city boss, in the City Hall basement | `design/worlds/shamsterdam/shamsterdam.md:320` | 0 | none | No |
| Meester Overhang | Master (lawyer's title) Overhang | The Hoisted Pint tour boss: the neighbour's lawyer | `design/worlds/shamsterdam/the_hoisted_pint.md:320` | 2 | `meester_overhang`, `shamsterdam_boss_meester_overhang` | **Yes.** Round v24 approved every Hoisted Pint detail as written (NEXT_WORK.md:500-502; the_hoisted_pint.md:5-9); the ledger does not quote the name |
| Opa Cees | Grandpa Cees | Bike-rental mechanic grandfather; "Opa Cees's Blessing" buff | `design/worlds/shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_opa_cees.md:1` | 15 | `npc_opa_cees`, `opa_cees`, `opa_cees_blessing`, `shamsterdam_npc_opa_cees_repair_01`<br>game/: `assets/data/world_data/quest_flags.json`, `tests/unit/test_navigation_grants.gd`<br>in plans: `shamsterdam_bike_rental` | No |
| Tante Bep | Auntie Bep | Stroopwafel cart owner | `design/worlds/shamsterdam/stroopwafel_cart.md:169` | 3 | `vendor_tante_bep`<br>in plans: `stroopwafel_cart` | No |
| Mevrouw Jansen | Mrs. Jansen | Resident who watches from her window and scores the night out of ten | `design/worlds/shamsterdam/roodelicht_row_district.md:896` | 8 | `mevrouw_jansen`, `mevrouw_jansen_at_window`, `npc_mevrouw_jansen`, `shamsterdam_npc_mevrouw_jansen_01`<br>in plans: `voetgangerstunnel` | No |
| Visser Maarten | Fisherman Maarten | Herring-stand vendor (title used on his sprite sheet) | `design/worlds/shamsterdam/PNG_Assets/De_Zilte_Waarheid_PNG_Assets.md:140` | 2 | `visser_maarten` | No |
| Willem Weet | Willem Knows | Graffiti tag / condom-machine sticker by Willem | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:194` | 1 | in plans: `shamsterdam_condom_machines` | No |
| Gerrit, Gerrit II, Gerrit III | Gerrit (Dutch man's name) | Muntje Erin's retired mops on plaques (separate from Gerrit the Traffic Philosopher) | `design/worlds/shamsterdam/roodelicht_row_district.md:501` | 1 | in plans: `muntje_erin` | No |
| Hendrik (the printer) | Hendrik (Dutch man's name) | Het Rode Loket's named thermal printer (separate from Brewmaster Hendrik) | `design/worlds/shamsterdam/roodelicht_row_district.md:363` | 0 | none | No |

## Items (products, menu items, exhibits, machines) (45)

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| De Reeks | The Range / The Series | Erotiek & Zo product range (five laminated tiers) | `design/worlds/shamsterdam/roodelicht_row_district.md:382` | 1 | in plans: `erotiek_en_zo` | No |
| De Kleine Ambtenaar | The Little Civil Servant | Erotiek & Zo entry-tier product | `design/worlds/shamsterdam/roodelicht_row_district.md:385` | 1 | in plans: `erotiek_en_zo` | No |
| De Middenmoot | The Mid-Table | Erotiek & Zo mid-tier product | `design/worlds/shamsterdam/roodelicht_row_district.md:386` | 1 | in plans: `erotiek_en_zo` | No |
| De Zeewaardige | The Seaworthy | Erotiek & Zo upper-tier product | `design/worlds/shamsterdam/roodelicht_row_district.md:387` | 1 | in plans: `erotiek_en_zo` | No |
| De Onverzettelijke | The Unyielding | Erotiek & Zo top-tier product ("The Item" Bradley buys) | `design/worlds/shamsterdam/roodelicht_row_district.md:388` | 1 | in plans: `erotiek_en_zo` | No |
| De Burgemeester | The Mayor | Erotiek & Zo behind-the-counter product, not for sale | `design/worlds/shamsterdam/roodelicht_row_district.md:389` | 1 | in plans: `erotiek_en_zo` | No |
| De Kniebuiging | The Genuflection | Shot on the Laatste Waarschuwing board | `design/worlds/shamsterdam/roodelicht_row_district.md:432` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| Het Klapstuk | The Showpiece | Shot on the Laatste Waarschuwing board | `design/worlds/shamsterdam/roodelicht_row_district.md:435` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| De Blauwe Zondag | The Blue Sunday (idiom: a fling that barely lasted) | Shot on the Laatste Waarschuwing board | `design/worlds/shamsterdam/roodelicht_row_district.md:438` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| De Weduwenmaker | The Widowmaker | Shot on the Laatste Waarschuwing board | `design/worlds/shamsterdam/roodelicht_row_district.md:441` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| De Grote Teleurstelling | The Great Disappointment | Free glass of water on the Laatste Waarschuwing board | `design/worlds/shamsterdam/roodelicht_row_district.md:444` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| De Bertus | The Bertus | Bertus's invented shot, served only to people who do not ask | `design/worlds/shamsterdam/roodelicht_row_district.md:454` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| De Grote Sleutelhanger | The Big Keyring | Het Rode Winkeltje keyring, 6 SOVS | `design/worlds/shamsterdam/roodelicht_row_district.md:469` | 0 | none | No |
| Bonbons van de Buurt | Bonbons of the Neighbourhood | Het Rode Winkeltje box of 12 chocolates | `design/worlds/shamsterdam/roodelicht_row_district.md:471` | 0 | none | No |
| De Stempelkaart | The Stamp Card | Het Rode Loket nine-stamp loyalty card | `design/worlds/shamsterdam/roodelicht_row_district.md:372` | 0 | none | No |
| De Vette Vinger (menu item) | The Greasy Finger | Signature item on the Frietkot menu | `design/worlds/shamsterdam/roodelicht_row_district.md:544` | 1 | in plans: `frietkot_de_vette_vinger` | No |
| De Dubbele Vinger | The Double Finger | Frietkot double portion; all three bros order it (Cascade stage 10) | `design/worlds/shamsterdam/roodelicht_row_district.md:332` | 1 | in plans: `frietkot_de_vette_vinger` | No |
| Handreiniger | Hand Cleaner | Lotte's 4 SOVS fountain-shaped hand sanitiser (removes 2 stacks) | `design/worlds/shamsterdam/the_dong_palace.md:230` | 3 | `handreiniger_offered_count`, `handreiniger_purchased_count` | No |
| De Collectie | The Collection | Boxed chocolate set from the Dong Palace gift shop, 45 SOVS | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_lotte_beekman.md:22` | 1 | none | No |
| De Oervorm | The Original Form | 1974 chocolate centrepiece in a nitrogen case (exhibit) | `design/worlds/shamsterdam/the_dong_palace.md:109` | 2 | in plans: `the_dong_palace` | No |
| De Fontein: Een Technisch Verhaal | The Fountain: A Technical Story | Dong Palace display about building the fountain (exhibit) | `design/worlds/shamsterdam/the_dong_palace.md:115` | 1 | none | No |
| De Vondstenkast | The Findings Cabinet | Muntje Erin glass case of objects pulled from coin slots (exhibit) | `design/worlds/shamsterdam/roodelicht_row_district.md:494` | 1 | in plans: `muntje_erin` | No |
| De Waarheid Platter | The Truth Platter | Top item on the herring stand price board, 8 SOVS | `design/worlds/shamsterdam/de_zilte_waarheid.md:38` | 2 | in plans: `de_zilte_waarheid` | No |
| Polder Pilsner | Polder (reclaimed-land) Pilsner | Starter beer in the Wobbly Windmill flight | `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md:144` | 2 | none | No |
| Oude Genever | Old Jenever (a real jenever category) | Bottoms Down unlockable consumable (+25 Bravado, The Shakes) | `design/worlds/shamsterdam/bottoms_down.md:226` | 12 | game/: `assets/data/items/consumables.json` | Effect ruled (NEXT_WORK.md:682, The Shakes). Name already in a rename round: author called it "too high brow and official" (bead Eurobound-jsc; WritingRoom/tasks/20261112_0816_shamsterdam_drink_renames_and_opener_gag, still open) |
| Blauwe Bok | Blue Buck (male goat) | Condom machine Mk. IV, the pristine variant | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:62` | 1 | in plans: `shamsterdam_condom_machines` | No |
| De Guldenvreter | The Guilder-Eater | Condom machine Mk. II, ancient and jammed, takes only guilders | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:71` | 3 | in plans: `shamsterdam_condom_machines` | No |
| De Bakfietsmaat | The Cargo-Bike Buddy (bakfiets + -maat) | Condom machine repurposed onto a cargo bike | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:83` | 1 | in plans: `shamsterdam_condom_machines` | No |
| De Plinth-o-Maat | The Plinth-o-Mat | Condom machine bolted to the empty I SHAMSTERDAM plinth | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:96` | 1 | in plans: `i_shamsterdam_sign_plinth` | No |
| De Verdronken Automaat | The Drowned Machine | Condom machine at the canal bottom (holds the "?" slot) | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:105` | 0 | none | No |
| De Hennepautomaat | The Hemp Machine | Condom machine in the Hemp Museum | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:115` | 1 | in plans: `the_hemp_museum` | No |
| Standaard (tier) | Standard | Condom machine Tier 1 and its 3-pack "Standaard Drie" (Standard Three) | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:129` | 0 | none | No |
| Nachtpakket | Night Pack | Condom machine Tier 1 six-pack | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:135` | 0 | none | No |
| Toeristenlijn | Tourist Line | Condom machine Tier 2 | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:137` | 0 | none | No |
| Molenzegel | Windmill Seal | Tier 2 souvenir condom | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:142` | 0 | none | No |
| Tulpenreeks | Tulip Series | Tier 2 four-colour condom set | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:143` | 0 | none | No |
| Klompje | Little Clog | Tier 2 clog-shaped tin | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:144` | 0 | none | No |
| Oranje Editie | Orange Edition | Tier 2 condom, always orange | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:145` | 1 | in plans: `shamsterdam_condom_machines` | No |
| Regionale Editie | Regional Edition | Condom machine Tier 3 | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:147` | 0 | none | No |
| Haring-editie | Herring Edition | Tier 3 herring-themed condom | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:152` | 0 | none | No |
| Stroopwafel-geur | Stroopwafel Scent | Tier 3 scented condom | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:153` | 0 | none | No |
| Hennep-vezel | Hemp Fibre | Tier 3 hemp condom, Hemp Museum only | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:155` | 0 | none | No |
| "Gezellig" Variety Pack | Cosy (untranslatable Dutch "gezellig") | Tier 3 pack; also the game-wide Gezellig Misuse Counter | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:154` | 1 | none | No |
| De Rariteiten | The Oddities | Condom machine Tier 4 | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:157` | 0 | none | No |
| De Vraagteken | The Question Mark | Condom machine Tier 5, the single "?" slot | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:165` | 0 | none | No |

## Events, quests, achievements and systems (11)

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| De Ronde | The Round | Ilse's restocking micro-quest (visit the machines) | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:231` | 0 | none | No |
| De Afwijzing | The Rejection | Timer-fired rejection-ladder ambient system; applies Rebuffed | `design/worlds/shamsterdam/roodelicht_row_district.md:266` | 0 | none | No |
| De Fontein Voorziet | The Fountain Provides | Fountain status tier 4 (urgent-navigation state) | `design/worlds/shamsterdam/the_dong_palace.md:284` | 1 | none | No |
| Delen is Lief | Sharing is Caring | Achievement: reach fountain Tier 5 | `design/worlds/shamsterdam/the_dong_palace.md:309` | 1 | none | No |
| Eén Keer Dopen | Dip Once | Achievement: leave Shamsterdam having dipped exactly once (also the ONE DIP sign) | `design/worlds/shamsterdam/the_dong_palace.md:58` | 2 | in plans: `the_dong_palace` | No |
| Ik Heb Niet Eens Gedoopt | I Didn't Even Dip | Achievement: Bradley reaches Tier 3 without a voluntary dip | `design/worlds/shamsterdam/the_dong_palace.md:311` | 1 | none | No |
| Jong vs. Oud | Young vs. Old | Round 1 of the Jenever Taste Test gauntlet | `design/worlds/shamsterdam/npcs/bottoms_down/npc_kees.md:154` | 2 | none | No |
| De Negen Types | The Nine Types | Rutger's laminated chart of nine visitor categories (De Wachtrij) | `design/worlds/shamsterdam/roodelicht_row_district.md:350` | 1 | in plans: `de_wachtrij` | No |
| De Handdoekregels | The Towel Rules | Het Warme Bad laminated rules in nine languages | `design/worlds/shamsterdam/roodelicht_row_district.md:573` | 0 | none | No |
| DE MUUR | The Wall | Chalked back-of-house scoreboard in Zone 4; quest hook "De Muur" | `design/worlds/shamsterdam/roodelicht_row_district.md:115` | 1 | in plans: `muntje_erin` | No |
| Tarievenbord | Rates Board | Het Rode Loket's live price board | `design/worlds/shamsterdam/roodelicht_row_district.md:363` | 1 | in plans: `het_rode_loket` | No |

## Dutch sign text (default: English; author to confirm) (36)

Sign, board and stencil text in Dutch. Two rows at the end are spoken Dutch lines, not signs; they are listed because they are player-facing Dutch text.

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| GEEN FOTO'S | No photos | Prohibition sign stack (De Wachtrij and the district's fifty-one signs) | `design/worlds/shamsterdam/roodelicht_row_district.md:940` | 1 | in plans: `de_wachtrij` | No |
| FOTOZONE | Photo zone | Painted box facing a wall with a mirror, at De Wachtrij | `design/worlds/shamsterdam/roodelicht_row_district.md:357` | 1 | in plans: `de_wachtrij` | No |
| NIET DOEN / MENSEN DOEN HET | Don't do it / People do it | Red band on 't Wilde Gokje's dosing chart and the hand-added line beneath | `design/worlds/shamsterdam/roodelicht_row_district.md:407` | 1 | in plans: `t_wilde_gokje` | No |
| DE LAATSTE WAARSCHUWING — 4 SOVS ELK | The Last Warning — 4 SOVS each | Shot-board header at the bar | `design/worlds/shamsterdam/roodelicht_row_district.md:429` | 1 | in plans: `bar_de_laatste_waarschuwing` | No |
| DEZE KANT BOVEN | This side up | Stencil on the crate for The Item (Erotiek & Zo) | `design/worlds/shamsterdam/roodelicht_row_district.md:400` | 1 | in plans: `erotiek_en_zo` | No |
| DE ZWEETKELDER — KELDER NEGEN | The Sweat Cellar — Cellar Nine | Club frontage sign | `design/worlds/shamsterdam/roodelicht_row_district.md:515` | 1 | in plans: `de_zweetkelder` | No |
| FRIETKOT DE VETTE VINGER — OPEN TOT 06:00 | Fry shack The Greasy Finger — open till 06:00 | Frietkot menu header | `design/worlds/shamsterdam/roodelicht_row_district.md:540` | 1 | in plans: `frietkot_de_vette_vinger` | No |
| FRIET / FRIET SPECIAAL / MAYONAISE | Fries / Fries special / Mayonnaise | Frietkot menu lines (friet speciaal is a real snack) | `design/worlds/shamsterdam/roodelicht_row_district.md:543` | 1 | in plans: `frietkot_de_vette_vinger` | No |
| HET WARME BAD — TARIEVEN | The Warm Bath — Rates | Bathhouse tariff board header | `design/worlds/shamsterdam/roodelicht_row_district.md:566` | 0 | none | No |
| PAK ER EEN — TAKE ONE | Take one | Clinic leaflet-rack header (already bilingual) | `design/worlds/shamsterdam/roodelicht_row_district.md:625` | 0 | none | No |
| WIJ ZIJN VERHUISD → | We have moved → | Papered-over old Dong Palace frontage on Roodelicht Row | `design/worlds/shamsterdam/roodelicht_row_district.md:650` | 0 | none | No |
| HYGIËNESCORE / IN BEHANDELING | Hygiene score / Under review | Municipal hygiene card on the fountain plinth and Gunter's cart | `design/worlds/shamsterdam/the_dong_palace.md:49` | 2 | `gunter_hygiene_card_examined`<br>in plans: `the_dong_palace` | No |
| EEN KEER DOPEN A.U.B. / ONE DIP PLEASE | Dip once, please | The ever-growing fountain warning plate (already bilingual) | `design/worlds/shamsterdam/the_dong_palace.md:58` | 2 | in plans: `the_dong_palace` | No |
| FONTEIN VAN DE GULLE GEVER — 2011 | Fountain of the Generous Giver — 2011 | Fountain plinth plaque | `design/worlds/shamsterdam/the_dong_palace.md:48` | 1 | in plans: `the_dong_palace` | No |
| DE CACAOGALERIJ — Nu Geopend | The Cocoa Gallery — Now Open | Banner that has said Now Open since 2011 | `design/worlds/shamsterdam/PNG_Assets/The_Dong_Palace_PNG_Assets.md:65` | 2 | in plans: `the_dong_palace` | No |
| VERVOLG → | Continued → | Doorway sign from the Cacaogalerij to the Mechanical Wing | `design/worlds/shamsterdam/PNG_Assets/The_Dong_Palace_PNG_Assets.md:139` | 2 | in plans: `the_dong_palace` | No |
| GGD GOEDGEKEURD | Approved by the GGD (the real Dutch municipal health service) | Decal on the Mk. IV condom machine | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:65` | 1 | in plans: `shamsterdam_condom_machines` | No |
| KAPOT / WERKT WEL | Broken / It does work | Condom-machine stickers | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:190` | 1 | in plans: `shamsterdam_condom_machines` | No |
| BEDANKT | Thank you | Receipt in the 1% empty "?" package | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:170` | 0 | none | No |
| DE BOTANISCHE LEUGEN — TULPEN SINDS 1637 | The Botanical Lie — Tulips since 1637 | Main sign of the tulip stall | `design/worlds/shamsterdam/de_botanische_leugen.md:34` | 2 | in plans: `de_botanische_leugen` | No |
| DE ZILTE WAARHEID — Haring Sinds 1952 | The Salty Truth — Herring since 1952 | Herring-stand main sign | `dev/asset_team/plans/de_zilte_waarheid_plan.md:9` | 2 | in plans: `de_zilte_waarheid` | No |
| Haring / Met Uitjes (price board) | Herring / With onions | Herring-stand price board (real dish names) | `design/worlds/shamsterdam/de_zilte_waarheid.md:38` | 2 | in plans: `de_zilte_waarheid` | No |
| Klein / Groot (price board) | Small / Large | Stroopwafel cart price board | `design/worlds/shamsterdam/stroopwafel_cart.md:35` | 2 | in plans: `stroopwafel_cart` | No |
| AUTOMATIEK | Automat | Frietomat door lettering ("SINCE 1941") | `design/worlds/shamsterdam/frietomat.md:35` | 2 | in plans: `frietomat` | No |
| 24 UUR | 24 hours | Frietomat hours sign | `design/worlds/shamsterdam/frietomat.md:36` | 2 | in plans: `frietomat` | No |
| BROUWERIJ | Brewery | Carved over the Wobbly Windmill Brewery door | `design/worlds/shamsterdam/wobbly_windmill_brewery.md:49` | 1 | none | No |
| FIETS VERHUUR | Bike rental | Bike-rental shopfront sign seen from the bike crossing | `design/worlds/shamsterdam/PNG_Assets/central_shamsterdam_bike_crossing_png_assets.md:414` | 1 | in plans: `central_shamsterdam_bike_crossing` | No |
| VOETGANGERS: U BENT NIET DE PRIORITEIT | Pedestrians: you are not the priority | Multilingual sign at the bike crossing (Dutch line) | `design/worlds/shamsterdam/interactions/central_shamsterdam_bike_crossing_interactions.json:133` | 0 | none | No |
| Nooduitgang | Emergency exit | Green tunnel sign (the reliable one) | `design/worlds/shamsterdam/location_nodes/voetgangerstunnel_location_nodes.json:287` | 2 | in plans: `voetgangerstunnel` | No |
| Uitgang | Exit | Red tunnel signs near the Red Light exit | `design/worlds/shamsterdam/voetgangerstunnel.md:114` | 1 | in plans: `voetgangerstunnel` | No |
| Centrum | City centre | Tunnel direction sign | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:43` | 3 | `centrum_sign`, `sign_centrum`<br>in plans: `voetgangerstunnel` | No |
| Centraal Station | Central Station (the REAL Amsterdam station name) | Tunnel direction sign; label of a navigation sign in engine data | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:9` | 12 | `centraal_station`, `centraal_station_sign`, `sign_centraal_station`<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `voetgangerstunnel` | Named in the navigation-odds approval (NEXT_WORK.md:848) as a sign label; the name was never ruled |
| Museum Plein | Museum Square (the REAL Amsterdam Museumplein) | Tunnel direction sign; label of a navigation sign in engine data | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:29` | 10 | `museum_plein`, `museum_plein_sign`, `sign_museum_plein`, `test_navigation_wrong_split_museum_plein`<br>game/: `assets/data/navigation/voetgangerstunnel.json`, `core/navigation_roll.gd`<br>in plans: `voetgangerstunnel` | Named in the navigation-odds approval (NEXT_WORK.md:848) as a sign label; the name was never ruled |
| Politie | Police | Police uniform lettering on the bike-crossing officer sprite | `design/worlds/shamsterdam/PNG_Assets/central_shamsterdam_bike_crossing_png_assets.md:299` | 0 | none | No |
| UIT DE WEG! / BEWEGEN! | Out of the way! / Move! | Cyclists' shouted lines (dialogue, not a sign) | `design/Quests/shamsterdam/bicycle_thunderdome.md:52` | 0 | none | No |
| Dat is vier / Drie vijftig | That is four / Three fifty | Daan's mumbled price in the museum gift shop (dialogue, not a sign) | `design/worlds/shamsterdam/shamsterdam_museum_questionable_art.md:218` | 4 | in plans: `shamsterdam_museum_of_questionable_art` | No |

## NPC personal names (author to decide if in scope) (70)

Dutch first names and surnames on invented NPCs. Not treated as automatically in scope. Names that are also common in English or internationally (Jesse, Theo, Tessa, Mila, Margot, Fleur) are marked in the "What it is" column. Non-Dutch NPC names (Gunter, Werner, Sophie, Bogdan, Katya, Mehmet, Kemal, Elif, Yusuf, Nigel, Takeshi and others) are left out.

| Dutch name | English (literal) | What it is | Defined at | Other files | Ids | Author-ruled before |
|---|---|---|---|---|---|---|
| Wim (Big Wim) | Dutch personal name | Kapsalon Koning vendor | `design/worlds/shamsterdam/npcs/Kapsalon_Koning/npc_big_wim.md:1` | 21 | `big_wim`, `npc_big_wim`, `shamsterdam_npc_big_wim_01`, `the_wim_ordered`, `the_wim_survived` (+6 more)<br>in plans: `kapsalon_koning`, `leemans_doner_palace` | No |
| Willem | Dutch personal name | Eternal busker in the Voetgangerstunnel | `design/worlds/shamsterdam/npcs/Voetgangerstunnel/npc_willem_eternal_busker.md:1` | 16 | `graffiti_willem_knows`, `is_willem_actually_dead`, `npc_opa_willem`, `npc_opa_willem_repair`, `npc_willem` (+48 more)<br>in plans: `shamsterdam_bike_rental`, `voetgangerstunnel` | Named in a price ruling (hat "exactly 247 SOVS", NEXT_WORK.md:508); name not ruled |
| Henk | Dutch personal name | Henk the Helpful (Unhelpful), tunnel misdirector | `design/worlds/shamsterdam/npcs/Voetgangerstunnel/npc_henk_helpful_unhelpful.md:1` | 14 | `ask_henk_directions`, `graffiti_dont_follow_henk`, `henk_alertness`, `henk_at_booth`, `henk_booth` (+27 more)<br>in plans: `voetgangerstunnel` | No |
| Marloes | Dutch personal name | Tunnel map seller | `design/worlds/shamsterdam/npcs/Voetgangerstunnel/npc_henk_helpful_unhelpful.md:156` | 10 | `marloes_advice_tracker`, `marloes_in_kiosk`, `marloes_interactions`, `marloes_kiosk`, `marloes_map_vendor` (+9 more)<br>in plans: `voetgangerstunnel` | No |
| Lotte Beekman | Dutch personal name | Dong Palace gift-shop attendant | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_lotte_beekman.md:1` | 8 | `lotte_beekman`, `lotte_floor_space_heard`, `lotte_lennon_conversation`, `lotte_met`, `lotte_visit_count` (+2 more)<br>in plans: `the_awkward_truffle` | Named in a price ruling (fridge magnet 3 SOVS, NEXT_WORK.md:509); name not ruled |
| Ruud | Dutch personal name | Dong Palace floor attendant ("No flash") | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_gunter.md:504` | 5 | `shamsterdam_npc_ruud_01`<br>in plans: `the_dong_palace` | No |
| Anke | Dutch personal name | Dong Palace ticket seller | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_gunter.md:503` | 7 | `shamsterdam_npc_anke_01`<br>in plans: `the_dong_palace` | No |
| Gerda Vonk | Dutch personal name | Municipal hygiene inspector | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_gunter.md:387` | 5 | `gerda_vonk`, `shamsterdam_npc_gerda_01`<br>in plans: `the_dong_palace` | No |
| Marijke Doornbos (withdrawn) | Dutch personal name | Withdrawn earlier draft of the fountain cart vendor | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_gunter.md:758` | 0 | none | No |
| Femke | Dutch personal name | Manager of The Glove Compartment | `design/worlds/shamsterdam/npcs/The_Glove_Compartment/npc_manager_femke.md:1` | 13 | `femke_met`, `femke_nursing_asked`, `femke_visit_count`, `manager_femke`, `npc_manager_femke` (+1 more)<br>in plans: `the_glove_compartment` | No |
| Ruben | Dutch personal name | Manager of Schrödinger's Souvenir | `design/worlds/shamsterdam/npcs/Schrodingers_Souvenir/npc_manager_ruben.md:1` | 5 | `manager_ruben`, `npc_manager_ruben`, `ruben_destination_given`, `ruben_met`, `ruben_research_behaviour` (+2 more) | No |
| Bas | Dutch personal name | Budtender Bas, De Groene Gids | `design/worlds/shamsterdam/npcs/De_Groene_Gids/npc_budtender_bas.md:1` | 7 | `bas_how_are_you_asked`, `bas_met`, `bas_photo_warned`, `bas_tobacco_attempted`, `bas_visit_count` (+3 more) | No |
| Marieke | Dutch personal name | De Groene Gids upsell budtender | `design/worlds/shamsterdam/PNG_Assets/De_Groene_Gids_PNG_Assets.md:514` | 3 | none | No |
| Anneke van der Berg | Dutch personal name | Bike Rental owner | `design/worlds/shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_anneke_van_der_berg.md:1` | 11 | `anneke_at_insurance_desk`, `anneke_brings_opa_coffee_sometimes`, `anneke_comment`, `anneke_counter`, `anneke_counter_01` (+20 more)<br>in plans: `shamsterdam_bike_rental` | No |
| Dirk van der Berg | Dutch personal name | Bike Rental recoveries son | `design/worlds/shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_dirk_van_der_berg.md:1` | 9 | `dirk_anneke`, `dirk_at_counter`, `dirk_canal_recovery_count`, `dirk_comment`, `dirk_commentary_based_on_condition` (+18 more)<br>in plans: `shamsterdam_bike_rental` | No |
| Cees (Opa Cees) | Dutch personal name | Bike Rental grandfather mechanic | `design/worlds/shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_opa_cees.md:1` | 15 | `cees_blessing_acquired`, `cees_canal_wall_seen`, `cees_history_heard`, `cees_interaction_count`, `cees_met` (+5 more)<br>game/: `assets/data/world_data/quest_flags.json`, `tests/unit/test_navigation_grants.gd`<br>in plans: `shamsterdam_bike_rental` | No |
| Kees (Cornelis) | Dutch personal name | Bartender at Bottoms Down | `design/worlds/shamsterdam/npcs/bottoms_down/npc_kees.md:1` | 14 | `kees_met`, `npc_kees`, `shamsterdam_npc_kees_01` | **Yes.** Round v23: "Kees, the jenever bar and the no-hands bow all stay" (NEXT_WORK.md:488-489; also :116) |
| Pim | Dutch personal name | Kees's assistant at Bottoms Down | `design/worlds/shamsterdam/PNG_Assets/bottoms_down_png_assets.md:213` | 2 | none | No |
| Hendrik | Dutch personal name | Brewmaster of the Wobbly Windmill Brewery | `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md:1` | 10 | `brewmaster_hendrik`, `hendrik_gift_discount`, `hendrik_met`, `hendrik_seagull_beat_played`, `hendrik_speech_completed` (+3 more) | No |
| Bram | Dutch personal name | Wobbly Windmill apprentice | `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md:443` | 3 | `gift_shop_attendant_bram` | No |
| Thijs | Dutch personal name | Brewmaster of The Hoisted Pint | `design/worlds/shamsterdam/the_hoisted_pint.md:305` | 7 | `brewmaster_thijs` | **Yes.** Round v24 approves "brewmasters Thijs and Sjors Hoedemaker" (NEXT_WORK.md:502) |
| Sjors Hoedemaker | Dutch personal name | Brewmaster of the Mad Monarch's Wit-tea Party | `design/worlds/shamsterdam/the_mad_monarchs_wit_tea_party.md:292` | 6 | `brewmaster_sjors_hoedemaker` | **Yes.** Round v24 (NEXT_WORK.md:502) |
| Mehmet Leeman (surname) | Dutch personal name | Döner master; "Leeman" is a Dutch surname and names the venue | `design/worlds/shamsterdam/npcs/Leemans_Doner_Palace/npc_mehmet_leeman.md:1` | 16 | `leemans_doner_palace`, `mehmet_leeman`, `npc_mehmet_leeman`, `shamsterdam_latenight_leemans_doner_01`, `shamsterdam_npc_mehmet_leeman_01`<br>in plans: `kapsalon_koning`, `leemans_doner_palace` | No |
| Maarten | Dutch personal name | Herring-stand vendor (De Zilte Waarheid) | `design/worlds/shamsterdam/de_zilte_waarheid.md:210` | 6 | `visser_maarten`<br>in plans: `de_zilte_waarheid` | No |
| Evi | Dutch personal name | Herring-stand staff | `design/worlds/shamsterdam/PNG_Assets/De_Zilte_Waarheid_PNG_Assets.md:134` | 2 | `assistant_evi` | No |
| Margriet | Dutch personal name | Tulip-stall seller (De Botanische Leugen) | `design/worlds/shamsterdam/de_botanische_leugen.md:188` | 4 | `vendor_margriet`<br>in plans: `de_botanische_leugen` | No |
| Piet | Dutch personal name | Tulip-stall assistant | `design/worlds/shamsterdam/de_botanische_leugen.md:204` | 3 | `assistant_piet`<br>in plans: `de_botanische_leugen` | No |
| Hendrika | Dutch personal name | Klompen Konfessional owner | `design/worlds/shamsterdam/klompen_konfessional.md:223` | 3 | `proprietor_hendrika`<br>in plans: `klompen_konfessional` | No |
| Pieter | Dutch personal name | Klompen Konfessional craftsman | `design/worlds/shamsterdam/PNG_Assets/Klompen_Konfessional_PNG_Assets.md:177` | 3 | `craftsman_pieter`<br>in plans: `klompen_konfessional` | No |
| Jeroen | Dutch personal name | Klompen Konfessional associate | `design/worlds/shamsterdam/PNG_Assets/Klompen_Konfessional_PNG_Assets.md:188` | 3 | `associate_jeroen`<br>in plans: `klompen_konfessional` | No |
| Koen | Dutch personal name | Bicycle Warfare Accessories staff | `design/worlds/shamsterdam/PNG_Assets/Bicycle_Warfare_Accessories_PNG_Assets.md:136` | 3 | `assistant_koen`<br>in plans: `bicycle_warfare_accessories` | No |
| Wouter | Dutch personal name | Café de Schaamte barista | `design/worlds/shamsterdam/cafe_de_schaamte.md:135` | 1 | none | No |
| Margot | Dutch personal name | Café de Schaamte server | `design/worlds/shamsterdam/cafe_de_schaamte.md:140` | 2 | none | No |
| Joop | Dutch personal name | Agent Havok's local cover name | `design/worlds/shamsterdam/PNG_Assets/Cafe_De_Schaamte_PNG_Assets.md:198` | 3 | none | No |
| Daan | Dutch personal name | Museum of Questionable Art gift-shop clerk | `design/worlds/shamsterdam/shamsterdam_museum_questionable_art.md:106` | 5 | in plans: `shamsterdam_museum_of_questionable_art` | No |
| Sanne | Dutch personal name | Hemp Museum growing-room attendant | `design/worlds/shamsterdam/PNG_Assets/The_Hemp_Museum_PNG_Assets.md:262` | 5 | `growing_room_attendant_sanne`<br>in plans: `the_hemp_museum` | No |
| Jan | Dutch personal name | The Pancake House chef | `design/worlds/shamsterdam/PNG_Assets/The_Pancake_House_PNG_Assets.md:231` | 0 | none | No |
| Marleen | Dutch personal name | The Pancake House hostess | `design/worlds/shamsterdam/PNG_Assets/The_Pancake_House_PNG_Assets.md:207` | 2 | none | No |
| Jesse | Dutch personal name | The Pancake House server (name also common in English) | `design/worlds/shamsterdam/the_pancake_house.md:195` | 3 | none | No |
| Anouk | Dutch personal name | Frietomat restocker | `design/worlds/shamsterdam/PNG_Assets/frietomat_png_assets.md:278` | 5 | `counter_worker_anouk`<br>in plans: `frietomat` | No |
| Theo | Dutch personal name | Frietomat kitchen worker (name also common in English) | `design/worlds/shamsterdam/PNG_Assets/frietomat_png_assets.md:287` | 3 | in plans: `frietomat` | No |
| Bep | Dutch personal name | Stroopwafel cart owner (Tante Bep) | `design/worlds/shamsterdam/stroopwafel_cart.md:169` | 3 | `vendor_tante_bep`<br>in plans: `stroopwafel_cart` | No |
| Mila | Dutch personal name | Tante Bep's helper (name also international) | `design/worlds/shamsterdam/stroopwafel_cart.md:184` | 3 | in plans: `stroopwafel_cart` | No |
| Joost | Dutch personal name | Condom-machine NPC (Glove Compartment relationship section) | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:274` | 6 | `associate_joost`<br>in plans: `the_glove_compartment` | No |
| Ilse | Dutch personal name | Condom-machine route technician; De Ronde quest-giver | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:283` | 4 | `shamsterdam_npc_ilse_route_tech_01`<br>in plans: `shamsterdam_condom_machines` | No |
| Jansen | Dutch personal name | Mevrouw Jansen, Roodelicht resident | `design/worlds/shamsterdam/roodelicht_row_district.md:896` | 8 | `mevrouw_jansen`, `mevrouw_jansen_at_window`, `npc_mevrouw_jansen`, `shamsterdam_npc_mevrouw_jansen_01`<br>in plans: `voetgangerstunnel` | No |
| Gerrit | Dutch personal name | Gerrit the Traffic Philosopher, bike crossing | `design/worlds/shamsterdam/central_shamsterdam_bike_crossing.md:222` | 4 | `gerrit_approval`, `gerrit_approval_achievement`, `gerrit_approval_selfie`, `gerrit_commentary`, `gerrit_newspaper` (+12 more) | No |
| Johannes | Dutch personal name | Wobbly Windmill tourist | `design/worlds/shamsterdam/wobbly_windmill_brewery.md:309` | 1 | none | No |
| Fleur | Dutch personal name | Tolerance Hostel couple member | `design/worlds/shamsterdam/the_tolerance_hostel.md:260` | 0 | none | No |
| Tessa | Dutch personal name | Wobbly Windmill / brewery NPC (name also English) | `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md:443` | 3 | none | No |
| Bregje | Dutch personal name | Het Rode Loket, The Yes Desk | `design/worlds/shamsterdam/roodelicht_row_district.md:665` | 3 | `shamsterdam_npc_bregje_loket_01`<br>in plans: `de_kliniek_van_achterom`, `het_rode_loket` | No |
| Rutger | Dutch personal name | De Wachtrij arrivals triage | `design/worlds/shamsterdam/roodelicht_row_district.md:687` | 3 | `shamsterdam_npc_rutger_queue_01`<br>in plans: `de_wachtrij`, `het_warme_bad` | No |
| Sjoerd | Dutch personal name | Erotiek & Zo retail floor | `design/worlds/shamsterdam/roodelicht_row_district.md:702` | 2 | `shamsterdam_npc_sjoerd_retail_01`<br>in plans: `erotiek_en_zo` | No |
| Wietse | Dutch personal name | 't Wilde Gokje smart shop | `design/worlds/shamsterdam/roodelicht_row_district.md:717` | 2 | `shamsterdam_npc_wietse_smartshop_01`<br>in plans: `t_wilde_gokje` | No |
| Bertus | Dutch personal name | Bar De Laatste Waarschuwing owner | `design/worlds/shamsterdam/roodelicht_row_district.md:734` | 2 | `shamsterdam_npc_bertus_shotbar_01`<br>in plans: `bar_de_laatste_waarschuwing` | No |
| Teun | Dutch personal name | Muntje Erin turnaround cleaner | `design/worlds/shamsterdam/roodelicht_row_district.md:749` | 2 | `shamsterdam_npc_teun_hygiene_01`<br>in plans: `muntje_erin` | No |
| Fenna | Dutch personal name | De Zweetkelder rope | `design/worlds/shamsterdam/roodelicht_row_district.md:766` | 3 | `shamsterdam_npc_fenna_rope_01`<br>in plans: `de_zweetkelder` | No |
| Griet | Dutch personal name | Het Warme Bad towels | `design/worlds/shamsterdam/roodelicht_row_district.md:783` | 2 | `shamsterdam_npc_griet_towels_01`<br>in plans: `het_warme_bad` | No |
| Dirkje | Dutch personal name | Frietkot De Vette Vinger | `design/worlds/shamsterdam/roodelicht_row_district.md:798` | 2 | `shamsterdam_npc_dirkje_frietkot_01`<br>in plans: `frietkot_de_vette_vinger` | No |
| Trijntje | Dutch personal name | Het Rode Winkeltje gift shop | `design/worlds/shamsterdam/roodelicht_row_district.md:813` | 3 | `shamsterdam_npc_trijntje_giftshop_01`<br>in plans: `het_rode_winkeltje` | No |
| Nienke | Dutch personal name | De Roze Rondleiding tour guide | `design/worlds/shamsterdam/roodelicht_row_district.md:829` | 2 | `shamsterdam_npc_nienke_guide_01`<br>in plans: `de_roze_rondleiding` | No |
| Joris | Dutch personal name | Civil enforcement officer | `design/worlds/shamsterdam/roodelicht_row_district.md:846` | 0 | `shamsterdam_npc_joris_enforcement_01` | No |
| Roosmarijn | Dutch personal name | De Kliniek van Achterom | `design/worlds/shamsterdam/roodelicht_row_district.md:862` | 3 | `shamsterdam_npc_roosmarijn_kliniek_01`<br>in plans: `de_kliniek_van_achterom` | No |
| Saskia | Dutch personal name | District operations (runs a book on stag parties) | `design/worlds/shamsterdam/roodelicht_row_district.md:876` | 2 | `shamsterdam_npc_saskia_operations_01` | No |
| Machteld | Dutch personal name | Couchsurf host "Magnet Machteld" | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:49` | 0 | none | No |
| Willemijn | Dutch personal name | Couchsurf host "Tourmistress Willemijn" | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:158` | 0 | none | No |
| Sietske & Renske | Dutch personal name | Couchsurf hosts "The Not-Girlfriends" | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:265` | 0 | none | No |
| Noortje | Dutch personal name | Couchsurf host "Captain Noortje of the Vooruitgang" | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:387` | 0 | none | No |
| Rikst | Dutch personal name | Couchsurf host "Rikst Who Does Not Dismount" | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:494` | 0 | none | No |
| Nataniël Gomes | Dutch personal name | The "port city barber" who invented the kapsalon (see surprises) | `design/worlds/shamsterdam/kapsalon_koning.md:302` | 2 | in plans: `kapsalon_koning` | No |

## Kept: real product or brand (11)

Real products, dishes, drinks and brands keep their real names (author ruling 2026-11-09). Not for renaming; listed so a sweep skips them.

| Name | Why kept | Files mentioning |
|---|---|---|
| Stroopwafel | Real product | 24 |
| Kapsalon (the dish) | Real dish (but "Kapsalon Koning" is listed under Places) | 20 |
| Haring / Hollandse herring, Broodje haring, Kibbeling, Augurken, Uitjes | Real foods | 4 |
| Kroket, Frikandel (Speciaal), Bamischijf, Kaassouflé, Satéschotel, Berehap, Mexicano, Bitterballen, Friet speciaal | Real Dutch snacks (Frietomat / Frietkot menus) | 3 |
| Spekpannenkoek, Kaaspannenkoek, Appelpannenkoek, pannenkoeken | Real dishes (Pancake House menu) | 2 |
| Jenever, Jonge Jenever, Korenwijn, Kopstootje | Real drinks and drinking custom; NOTE "The Kopstootje" is also the Bottoms Down final boss and "The Kopstootje Combo" a menu item | 4 |
| Gouda, Delft (blue) | Real cheese / real ceramic style | 10 |
| Heineken, Albert Heijn, Jumbo, Bulldog | Real brands / real businesses | 13 |
| Bakfiets | Real product (cargo bike); also inside "De Bakfietsmaat" (listed under Items) | 8 |
| Proeflokaal, Bloemenmarkt, polder, gezellig (as words) | Real Dutch words / a real market used in design commentary only | 15 |
| Ayran, Dürüm, Tavuk, Ekmek, Karışık, Dana | Real Turkish foods (Leeman's menu); not Dutch | 4 |

## Surprises and conflicts

1. **Real Amsterdam place names in player-facing data.** "Centraal Station" and "Museum Plein" are the real names (Centraal Station, Museumplein). They are tunnel sign labels in `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:9, :29`, sign keys and labels in the engine file `game/assets/data/navigation/voetgangerstunnel.json:5-15`, and are quoted in the approved navigation-odds ruling (`docs/superpowers/NEXT_WORK.md:848`). The PNG names `cart_location_damsquare.png` and `cart_location_vondelpark.png` (`design/worlds/shamsterdam/stroopwafel_cart.md:350-351`) also use real place names; the asset plan already flags them (`dev/asset_team/plans/stroopwafel_cart_plan.md:29`).
2. **Thin puns on real places:** Het Rijke Museum (Rijksmuseum), Verdoemplein (Dam square), Wandelpark (Vondelpark), De Kuipmarkt (Albert Cuyp market), Museum de Gekke Schilder (the Van Gogh Museum, by implication).
3. **Real business and person names.** The Hemp Museum's "Alternative Name" is "Hash, Marihuana & Hemp Museum" (`design/worlds/shamsterdam/the_hemp_museum.md:9`), the real museum's name. Big Wim's kapsalon origin story names "El Aviva snack bar" and "Nataniël Gomes" (`design/worlds/shamsterdam/kapsalon_koning.md:302, :305`; `npcs/Kapsalon_Koning/npc_big_wim.md:69`). These are close to the real Rotterdam snack bar and the dish's real inventor. "GGD GOEDGEKEURD" (`shamsterdam_condom_machines.md:65`) names the real Dutch municipal health service.
4. **Dutch names the author already approved.** These conflict with the new ruling and need an author call, not a silent rename: **Frietomat** (author-minted, Round v21, `NEXT_WORK.md:481`); **Meester Overhang** and brewmasters **Thijs** and **Sjors Hoedemaker** (Round v24, `NEXT_WORK.md:502`); **Kees** (kept by Round v23, `NEXT_WORK.md:488`).
5. **Heritage gag cluster ruling.** `NEXT_WORK.md:154` says "Pancake House / Klompen shop / herring vendor ... KEEP AS-IS". It covers the content, but a sweep may read it as covering Klompen Konfessional, De Zilte Waarheid and Pannenkoekhuis. The author should say whether the names are included.
6. **Renames already in flight.** Oude Genever is in an open Writers' Room rename task the author called "too high brow and official" (bead Eurobound-jsc, `WritingRoom/tasks/20261112_0816_shamsterdam_drink_renames_and_opener_gag/`, 0 rounds run). The author rejected Dutch-sounding names before: on 2026-11-12 Condomerie and Venustempel became The Glove Compartment and The Dong Palace (`WritingRoom/tasks/20261112_0801_shamsterdam_parody_business_names/final.md`).
7. **Retired name residue.** "Proeflokaal 't Kansen" was renamed Bottoms Down in Round v23 but is still listed in `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md:180`. "proeflokaal" is still the venue noun in `bottoms_down.md:268, :316, :426, :431`.
8. **Internal contradiction.** `the_mad_monarchs_wit_tea_party.md:25, :363` says no "Oranje" in any name, but the condom machines sell an "Oranje Editie" (`shamsterdam_condom_machines.md:145`).
9. **Engine footprint is small.** Only Frietomat, Roodelicht Row, Centraal Chaos, Centraal Station and Museum Plein appear as ids in `game/assets/data/navigation/voetgangerstunnel.json`. Voetgangerstunnel is also the file name and a status-effect source, and De Groene Gids and De Zilte Waarheid appear in `game/assets/data/skills/status_effects.json` notes. Most Dutch names live only in design docs, asset plans and the beads/WritingRoom trail. The Roodelicht sub-locations have no standalone docs; their only design source is `roodelicht_row_district.md`.
10. **Duplicate root names.** "Gerrit" is two characters: the bike-crossing Traffic Philosopher and Muntje Erin's three mops. "Hendrik" is also two: the brewmaster and Het Rode Loket's printer. "Kees" and "Cees" are distinct NPCs by design (`npcs/bottoms_down/npc_kees.md:460`).
