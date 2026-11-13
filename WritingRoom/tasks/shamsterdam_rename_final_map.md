# Shamsterdam rename: final old→new map (bead Eurobound-ucpf)

For the Absinthe Orchestrator, who runs the rename sweep. Every "New" name is the author's pick on the Eurobound Desk (Eurobound-ucpf-q2..q62, 2026-11-13), recorded verbatim. Answer-by-answer notes are in `shamsterdam_rename_map.md`; full source rows (all references) in `shamsterdam_dutch_names_inventory.md`. "Engine ids" is the inventory's Ids column, verbatim. Ids are slugs: whether a slug is renamed or kept as an internal id is the sweep's call. The names above are what the player sees.

## Scope rulings (verbatim)
- q42: "Keep the locals' Dutch first names; only titles, nicknames and places change"
- q43: "All English; Claude sharpens the jokes in translation"

## Author-kept Dutch exceptions (only these three)
- **De Pauze** (Zone 2, formerly Het Plein van Niks). q45: "Keep De Pauze (one-off, like Frietomat)". (Frietomat itself became **Fritomat**, q44.)
- **Meester Overhang**. q48 note: "Meester Overhang can stay. This and Opa Cees aren't hard to understand so are fine"
- **Opa Cees** (and the "Opa Cees's Blessing" buff). q49: "Opa Cees can stay"

## Four English main names replaced (q46: "They REPLACE the main names (the old English names go)")
| Old main name | New | Engine ids found (grep) |
|---|---|---|
| Bicycle Warfare Accessories (alias Fietsbel & Meer) | **Spoke & Dagger** | `bicycle_warfare_accessories`, `shamsterdam_central_bicycle_warfare_01`, `bicycle_warfare_exterior`, `bicycle_warfare_interior`; doc `Bicycle_Warfare_Accessories_PNG_Assets` |
| Schrödinger's Souvenir (alias Schrödinger's Aandenken) | **Quantum Kitsch** | `schrodingers_souvenir`, `schrodingers_interior_main`, `schrodingers_exterior_zones`, `schrodingers_products`, `schrodingers_ui`, `schrodingers_effects`, `npc_schrodingers_customers` |
| Shamsterdam Bike Rental (alias Fiets Verhuur) | **Tram Track Magnets** (the FIETS VERHUUR sign follows) | `shamsterdam_bike_rental_01`, `shamsterdam_bike_rental`, `bike_rental`, `bike_rental_effects`, `bike_rental_displays`, `shamsterdam_bike_rental_npcs`, `shamsterdam_bike_rental_png_assets` |
| The Pancake House (alias Pannenkoekhuis) | **The House Of Flaps** | `the_pancake_house`, `pancake_house_interior_main`, `pancake_house_terrace`, `pancake_house_food`, `pancake_house_fixtures`, `pancake_house_ui`, `pancake_house_effects`, `npc_pancake_house_staff` |

Note: an older ruling keeps The Pancake House's CONTENT as-is (NEXT_WORK.md:154). Only the name changes.

## Follow-ups the sweep should know about (flagged, not decided)
- **Hendrik the printer** (Accommodations, roodelicht_row_district.md:363, sign `HENDRIK — 2014 —`): the author ruled "Rename the printer" (q54). The new name is on the Desk as Eurobound-ucpf-q63; a one-line addendum follows.
- **Chadwick misspells the Rijke Museum three ways.** The gag needs three new misspellings of "The Gallery of Generational Wealth" (author content; not done).
- **The Safe-Crossing** (q9 note): "Ideally paired with a flickering neon sign and a suspicious NPC standing in the corner." Staging for the Asset team; a new NPC needs its own author ruling.
- **The Final Round** sits near the battle ultimate "Final Round's On Me" (battle_system.md:299). Flagged, not changed.
- **"Gezellig" Variety Pack → The Snuggle Pack.** The game-wide Gezellig Misuse Counter was NOT renamed (the author approved the pack name without a note about the counter).
- **The Orange Crush** (was Oranje Editie) clears the Oranje-ban conflict logged on Eurobound-w5ra.
- **WILLEM KNOWS**: the tunnel graffiti already reads "Willem knows" in English (voetgangerstunnel_interactions.json:134); now consistent.
- **Out of this map:** Oude Genever (being renamed by the Writers' Room drinks task, 20261112_0816); Proeflokaal residue, real business/person names and the WILHELMUS miss (Eurobound-w5ra); NPC first names (kept, q42); 11 real products (kept).

## Places

| Old | New | Defined at | Engine ids (from inventory) |
|---|---|---|---|
| Café de Schaamte | **Dregs** | `design/worlds/shamsterdam/cafe_de_schaamte.md:1` | `shamsterdam_cafe_de_schaamte_01`, `shamsterdam_canalring_cafe_schaamte_01`<br>in plans: `cafe_de_schaamte` |
| De Botanische Leugen | **The Transient Tulip** | `design/worlds/shamsterdam/de_botanische_leugen.md:1` | `de_botanische_leugen`<br>in plans: `de_botanische_leugen` |
| De Groene Gids | **Starbaked** | `design/worlds/shamsterdam/de_groene_gids.md:1` | `de_groene_gids`, `shamsterdam_coffeeshop_groene_gids_01`<br>game/: `assets/data/skills/status_effects.json`<br>in plans: `de_groene_gids` |
| De Zilte Waarheid | **The Salty Swallow** | `design/worlds/shamsterdam/de_zilte_waarheid.md:1` | `de_zilte_waarheid`<br>game/: `assets/data/skills/status_effects.json`<br>in plans: `de_zilte_waarheid` |
| Frietomat | **Fritomat** | `design/worlds/shamsterdam/frietomat.md:1` | `discover_frietomat_shortcut`, `exit_probability_frietomat`, `frietomat_backdoor`, `frietomat_emergence`, `frietomat_hidden` (+12 more)<br>game/: `assets/data/navigation/voetgangerstunnel.json`, `assets/data/skills/status_effects.json`<br>in plans: `frietkot_de_vette_vinger`, `frietomat`, `voetgangerstunnel` |
| Kapsalon Koning | **The Kapsalon King** | `design/worlds/shamsterdam/kapsalon_koning.md:1` | `kapsalon_koning`, `shamsterdam_latenight_kapsalon_koning_01`<br>in plans: `kapsalon_koning`, `leemans_doner_palace` |
| Klompen Konfessional | **Klog Konfessional** | `design/worlds/shamsterdam/klompen_konfessional.md:1` | `klompen_konfessional`, `shamsterdam_tourist_klompen_konfessional_01`<br>in plans: `klompen_konfessional` |
| Voetgangerstunnel | **The Safe-Crossing** | `design/worlds/shamsterdam/voetgangerstunnel.md:1` | `shamsterdam_voetgangerstunnel_01`, `shamsterdam_voetgangerstunnel_bike_parking_01`, `shamsterdam_voetgangerstunnel_correct_exit_01`, `shamsterdam_voetgangerstunnel_entrance_01`, `shamsterdam_voetgangerstunnel_intersection_01` (+8 more)<br>game/: `assets/data/world_data/quest_flags.json`, `core/navigation_roll.gd`<br>in plans: `voetgangerstunnel` |
| Roodelicht Row | **The Flesh Market** | `design/worlds/shamsterdam/roodelicht_row_district.md:1` | `exit_probability_roodelicht`, `roodelicht_row`, `roodelicht_row_district`, `roodelicht_row_exit`, `roodelicht_row_surface` (+8 more)<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `casa_rose_erotic_theater`, `central_shamsterdam_bike_crossing`, `de_roze_rondleiding` (+4) |
| Leeman's Döner Paleis | **Leeman's Döner Palace (alias dropped; main name stays)** | `design/worlds/shamsterdam/leemans_doner_palace.md:8` | none |
| Fietsbel & Meer | **Spoke & Dagger (REPLACES main name Bicycle Warfare Accessories)** | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:8` | in plans: `bicycle_warfare_accessories` |
| Schrödinger's Aandenken | **Quantum Kitsch (REPLACES main name Schrödinger's Souvenir)** | `design/worlds/shamsterdam/schrodingers_souvenir.md:8` | none |
| De Ongemakkelijke Truffel | **The Awkward Truffle (alias dropped; main name stays)** | `design/worlds/shamsterdam/the_awkward_truffle.md:8` | none |
| Fiets Verhuur | **Tram Track Magnets (REPLACES main name Shamsterdam Bike Rental)** | `design/worlds/shamsterdam/shamsterdam_bike_rental.md:8` | in plans: `shamsterdam_bike_rental` |
| Pannenkoekhuis | **The House Of Flaps (REPLACES main name The Pancake House)** | `design/worlds/shamsterdam/the_pancake_house.md:8` | none |
| De Stroopwafel Kar | **The Bougie Batter Cart** | `design/worlds/shamsterdam/stroopwafel_cart.md:1` | in plans: `stroopwafel_cart` |
| Veilig-o-Maat | **Wrap-O-Matic** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:6` | `shamsterdam_system_veiligomaat_01`<br>in plans: `i_shamsterdam_sign_plinth`, `shamsterdam_condom_machines` |
| Centraal Chaos | **Terminal Chaos** | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:11` | `centraal_chaos`<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `bicycle_warfare_accessories`, `voetgangerstunnel` |
| Verdoemplein | **Damnation Square** | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:81` | in plans: `bicycle_warfare_accessories`, `stroopwafel_cart` |
| De Kuipmarkt | **The Flea Bag Market** | `design/worlds/shamsterdam/stroopwafel_cart.md:11` | in plans: `stroopwafel_cart` |
| Wandelpark | **Fondle Park** | `design/worlds/shamsterdam/bicycle_warfare_accessories.md:290` | in plans: `bicycle_warfare_accessories`, `stroopwafel_cart` |
| Museum de Gekke Schilder | **The Institute of Self-Importance** | `design/worlds/shamsterdam/shamsterdam.md:50` | in plans: `museum_de_gekke_schilder` |
| Het Rijke Museum | **The Gallery of Generational Wealth** | `design/worlds/shamsterdam/shamsterdam.md:51` | in plans: `het_rijke_museum`, `the_dong_palace` |
| De Etalagegang | **Pane & Pleasure** | `design/worlds/shamsterdam/roodelicht_row_district.md:90` | in plans: `frietkot_de_vette_vinger` |
| Het Plein van Niks | **De Pauze (AUTHOR-KEPT DUTCH EXCEPTION)** | `design/worlds/shamsterdam/roodelicht_row_district.md:99` | in plans: `de_roze_rondleiding`, `de_zweetkelder` |
| Achterom | **The Backside** | `design/worlds/shamsterdam/roodelicht_row_district.md:107` | in plans: `de_kliniek_van_achterom` |
| De Achterdeur | **The Back Door** | `design/worlds/shamsterdam/roodelicht_row_district.md:114` | none |
| De Wachtrij | **The Turnstyle** | `design/worlds/shamsterdam/roodelicht_row_district.md:347` | in plans: `de_wachtrij`, `de_zweetkelder`, `het_rode_loket` (+1) |
| Het Rode Loket | **Accommodations** | `design/worlds/shamsterdam/roodelicht_row_district.md:360` | `het_rode_loket`<br>in plans: `de_roze_rondleiding`, `de_wachtrij`, `het_rode_loket` |
| Erotiek & Zo | **The Toy Box** | `design/worlds/shamsterdam/roodelicht_row_district.md:377` | in plans: `de_wachtrij`, `erotiek_en_zo`, `t_wilde_gokje` |
| 't Wilde Gokje | **The Fungi Farmacy** | `design/worlds/shamsterdam/roodelicht_row_district.md:402` | in plans: `t_wilde_gokje` |
| Bar De Laatste Waarschuwing | **The Final Round** | `design/worlds/shamsterdam/roodelicht_row_district.md:423` | in plans: `bar_de_laatste_waarschuwing` |
| Het Rode Winkeltje | **The Morning After Market** | `design/worlds/shamsterdam/roodelicht_row_district.md:459` | `het_rode_winkeltje`<br>in plans: `het_rode_winkeltje` |
| Muntje Erin | **Peeps.** | `design/worlds/shamsterdam/roodelicht_row_district.md:483` | in plans: `de_zweetkelder`, `muntje_erin` |
| De Zweetkelder | **The Boiler Room** | `design/worlds/shamsterdam/roodelicht_row_district.md:509` | in plans: `de_roze_rondleiding`, `de_zweetkelder`, `muntje_erin` |
| Frietkot De Vette Vinger | **Brick & Lard** | `design/worlds/shamsterdam/roodelicht_row_district.md:534` | in plans: `frietkot_de_vette_vinger` |
| Het Warme Bad | **Members Only** | `design/worlds/shamsterdam/roodelicht_row_district.md:560` | `het_warme_bad`<br>in plans: `het_warme_bad` |
| De Roze Rondleiding | **The Field Trip.** | `design/worlds/shamsterdam/roodelicht_row_district.md:587` | in plans: `de_roze_rondleiding` |
| De Bijna-Toiletten | **The Holding Pattern** | `design/worlds/shamsterdam/roodelicht_row_district.md:603` | none |
| De Kliniek van Achterom | **Burning Questions Clinic** | `design/worlds/shamsterdam/roodelicht_row_district.md:617` | `shamsterdam_npc_roosmarijn_kliniek_01`<br>in plans: `de_kliniek_van_achterom` |
| De Grote Fontein | **The Fudge Spire** | `design/worlds/shamsterdam/shamsterdam.md:53` | none |
| Fontein van de Gulle Gever | **Fountain Of The Generous Giver** | `design/worlds/shamsterdam/the_dong_palace.md:48` | in plans: `the_dong_palace` |
| De Cacaogalerij | **Bonbons & Balls** | `design/worlds/shamsterdam/the_dong_palace.md:105` | in plans: `the_dong_palace` |
| De Mechanische Vleugel | **The Repressed Collection** | `design/worlds/shamsterdam/the_dong_palace.md:118` | in plans: `the_dong_palace` |
| Ervaar de Tempel | **The Climax** | `design/worlds/shamsterdam/the_dong_palace.md:133` | in plans: `the_dong_palace` |
| Vooruitgang | **The Broke Anchor** | `design/Quests/shamsterdam/couchsurfingchroniclesshamsterdam.md:387` | none |
| Proeflokaal 't Kansen (retired) | **Bottoms Down (already renamed; residue tracked on Eurobound-w5ra)** | `docs/superpowers/NEXT_WORK.md:488` | none |

## Titles and nicknames

| Old | New | Defined at | Engine ids (from inventory) |
|---|---|---|---|
| Burgemeester van Schande | **His Dishonor the Mayor** | `design/worlds/shamsterdam/shamsterdam.md:320` | none |
| Meester Overhang | **Meester Overhang (AUTHOR-KEPT DUTCH EXCEPTION)** | `design/worlds/shamsterdam/the_hoisted_pint.md:320` | `meester_overhang`, `shamsterdam_boss_meester_overhang` |
| Opa Cees | **Opa Cees (AUTHOR-KEPT DUTCH EXCEPTION)** | `design/worlds/shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_opa_cees.md:1` | `npc_opa_cees`, `opa_cees`, `opa_cees_blessing`, `shamsterdam_npc_opa_cees_repair_01`<br>game/: `assets/data/world_data/quest_flags.json`, `tests/unit/test_navigation_grants.gd`<br>in plans: `shamsterdam_bike_rental` |
| Tante Bep | **Auntie Bep** | `design/worlds/shamsterdam/stroopwafel_cart.md:169` | `vendor_tante_bep`<br>in plans: `stroopwafel_cart` |
| Mevrouw Jansen | **Judge Jansen** | `design/worlds/shamsterdam/roodelicht_row_district.md:896` | `mevrouw_jansen`, `mevrouw_jansen_at_window`, `npc_mevrouw_jansen`, `shamsterdam_npc_mevrouw_jansen_01`<br>in plans: `voetgangerstunnel` |
| Visser Maarten | **Maarten the Herring Guy** | `design/worlds/shamsterdam/PNG_Assets/De_Zilte_Waarheid_PNG_Assets.md:140` | `visser_maarten` |
| Willem Weet | **WILLEM KNOWS** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:194` | in plans: `shamsterdam_condom_machines` |
| Gerrit, Gerrit II, Gerrit III | **Gerrit, Gerrit II, Gerrit III (KEPT as written, q54)** | `design/worlds/shamsterdam/roodelicht_row_district.md:501` | in plans: `muntje_erin` |
| Hendrik (the printer) | **PENDING Desk q63 (rename; addendum to follow)** | `design/worlds/shamsterdam/roodelicht_row_district.md:363` | none |

## Items (Oude Genever excluded: the Writers' Room drinks task renames it)

| Old | New | Defined at | Engine ids (from inventory) |
|---|---|---|---|
| De Reeks | **The Lineup** | `design/worlds/shamsterdam/roodelicht_row_district.md:382` | in plans: `erotiek_en_zo` |
| De Kleine Ambtenaar | **The Intern** | `design/worlds/shamsterdam/roodelicht_row_district.md:385` | in plans: `erotiek_en_zo` |
| De Middenmoot | **The Middle Manager** | `design/worlds/shamsterdam/roodelicht_row_district.md:386` | in plans: `erotiek_en_zo` |
| De Zeewaardige | **The Battleship** | `design/worlds/shamsterdam/roodelicht_row_district.md:387` | in plans: `erotiek_en_zo` |
| De Onverzettelijke | **The Immovable Object** | `design/worlds/shamsterdam/roodelicht_row_district.md:388` | in plans: `erotiek_en_zo` |
| De Burgemeester | **The Commander-in-Chief** | `design/worlds/shamsterdam/roodelicht_row_district.md:389` | in plans: `erotiek_en_zo` |
| De Kniebuiging | **Down on One Knee** | `design/worlds/shamsterdam/roodelicht_row_district.md:432` | in plans: `bar_de_laatste_waarschuwing` |
| Het Klapstuk | **The Showstopper** | `design/worlds/shamsterdam/roodelicht_row_district.md:435` | in plans: `bar_de_laatste_waarschuwing` |
| De Blauwe Zondag | **The Two-Pump Chump** | `design/worlds/shamsterdam/roodelicht_row_district.md:438` | in plans: `bar_de_laatste_waarschuwing` |
| De Weduwenmaker | **The Widowmaker** | `design/worlds/shamsterdam/roodelicht_row_district.md:441` | in plans: `bar_de_laatste_waarschuwing` |
| De Grote Teleurstelling | **The Big Letdown** | `design/worlds/shamsterdam/roodelicht_row_district.md:444` | in plans: `bar_de_laatste_waarschuwing` |
| De Bertus | **The Bertus** | `design/worlds/shamsterdam/roodelicht_row_district.md:454` | in plans: `bar_de_laatste_waarschuwing` |
| De Grote Sleutelhanger | **The Ball & Chain** | `design/worlds/shamsterdam/roodelicht_row_district.md:469` | none |
| Bonbons van de Buurt | **Local Hotties (Box of 12)** | `design/worlds/shamsterdam/roodelicht_row_district.md:471` | none |
| De Stempelkaart | **The Punch Card** | `design/worlds/shamsterdam/roodelicht_row_district.md:372` | none |
| De Vette Vinger (menu item) | **The Greasy Finger** | `design/worlds/shamsterdam/roodelicht_row_district.md:544` | in plans: `frietkot_de_vette_vinger` |
| De Dubbele Vinger | **The Double Finger** | `design/worlds/shamsterdam/roodelicht_row_district.md:332` | in plans: `frietkot_de_vette_vinger` |
| Handreiniger | **The Hand Squirt** | `design/worlds/shamsterdam/the_dong_palace.md:230` | `handreiniger_offered_count`, `handreiniger_purchased_count` |
| De Collectie | **The Full Package** | `design/worlds/shamsterdam/npcs/The_Dong_Palace/npc_lotte_beekman.md:22` | none |
| De Oervorm | **The Original Member** | `design/worlds/shamsterdam/the_dong_palace.md:109` | in plans: `the_dong_palace` |
| De Fontein: Een Technisch Verhaal | **The Fudge Spire: A Technical Erection** | `design/worlds/shamsterdam/the_dong_palace.md:115` | none |
| De Vondstenkast | **Things Found in Slots** | `design/worlds/shamsterdam/roodelicht_row_district.md:494` | in plans: `muntje_erin` |
| De Waarheid Platter | **The Full Swallow Platter** | `design/worlds/shamsterdam/de_zilte_waarheid.md:38` | in plans: `de_zilte_waarheid` |
| Polder Pilsner | **Landfill Lager** | `design/worlds/shamsterdam/npcs/wobbly_windmill_brewery/npc_brewmaster_hendrik.md:144` | none |
| Blauwe Bok | **Blue Steel** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:62` | in plans: `shamsterdam_condom_machines` |
| De Guldenvreter | **The Old Muncher** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:71` | in plans: `shamsterdam_condom_machines` |
| De Bakfietsmaat | **The Rubber Rickshaw** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:83` | in plans: `shamsterdam_condom_machines` |
| De Plinth-o-Maat | **The Plinth-O-Matic** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:96` | in plans: `i_shamsterdam_sign_plinth` |
| De Verdronken Automaat | **Davy Jones' Lock-Box** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:105` | none |
| De Hennepautomaat | **The Hemp-O-Matic** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:115` | in plans: `the_hemp_museum` |
| Standaard (tier) | **Missionary / Missionary 3-Pack** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:129` | none |
| Nachtpakket | **The All-Nighter** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:135` | none |
| Toeristenlijn | **The Tourist Trap Line** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:137` | none |
| Molenzegel | **The Windmill Wrapper** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:142` | none |
| Tulpenreeks | **Two Lips Collection** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:143` | none |
| Klompje | **The Clog Blocker** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:144` | none |
| Oranje Editie | **The Orange Crush** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:145` | in plans: `shamsterdam_condom_machines` |
| Regionale Editie | **Local Flavor Line** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:147` | none |
| Haring-editie | **Fishy Business** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:152` | none |
| Stroopwafel-geur | **The Syrup Trap** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:153` | none |
| Hennep-vezel | **Rope-a-Dope** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:155` | none |
| "Gezellig" Variety Pack | **The Snuggle Pack** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:154` | none |
| De Rariteiten | **The Weird Stuff** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:157` | none |
| De Vraagteken | **The Mystery Slot** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:165` | none |

## Events, quests, achievements and systems

| Old | New | Defined at | Engine ids (from inventory) |
|---|---|---|---|
| De Ronde | **The Rubber Run** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:231` | none |
| De Afwijzing | **The Brush-Off** | `design/worlds/shamsterdam/roodelicht_row_district.md:266` | none |
| De Fontein Voorziet | **Gotta Go Mode** | `design/worlds/shamsterdam/the_dong_palace.md:284` | none |
| Delen is Lief | **Sharing Is Caring** | `design/worlds/shamsterdam/the_dong_palace.md:309` | none |
| Eén Keer Dopen | **One and Done** | `design/worlds/shamsterdam/the_dong_palace.md:58` | in plans: `the_dong_palace` |
| Ik Heb Niet Eens Gedoopt | **I Didn't Even Dip!** | `design/worlds/shamsterdam/the_dong_palace.md:311` | none |
| Jong vs. Oud | **Rookie vs. Geezer** | `design/worlds/shamsterdam/npcs/bottoms_down/npc_kees.md:154` | none |
| De Negen Types | **Know Your Tourist (9 Types)** | `design/worlds/shamsterdam/roodelicht_row_district.md:350` | in plans: `de_wachtrij` |
| De Handdoekregels | **The Towel Rules** | `design/worlds/shamsterdam/roodelicht_row_district.md:573` | none |
| DE MUUR | **THE SCORE WALL** | `design/worlds/shamsterdam/roodelicht_row_district.md:115` | in plans: `muntje_erin` |
| Tarievenbord | **Today's Specials** | `design/worlds/shamsterdam/roodelicht_row_district.md:363` | in plans: `het_rode_loket` |

## Sign and spoken text (q55, all approved)

| Old | New | Defined at | Engine ids (from inventory) |
|---|---|---|---|
| GEEN FOTO'S | **NO PHOTOS. NOT EVEN THAT ONE.** | `design/worlds/shamsterdam/roodelicht_row_district.md:940` | in plans: `de_wachtrij` |
| FOTOZONE | **OFFICIAL PHOTO ZONE** | `design/worlds/shamsterdam/roodelicht_row_district.md:357` | in plans: `de_wachtrij` |
| NIET DOEN / MENSEN DOEN HET | **DO NOT DO THIS / (people do this)** | `design/worlds/shamsterdam/roodelicht_row_district.md:407` | in plans: `t_wilde_gokje` |
| DE LAATSTE WAARSCHUWING — 4 SOVS ELK | **THE FINAL ROUND - 4 SOVS A SHOT. LAST WARNING.** | `design/worlds/shamsterdam/roodelicht_row_district.md:429` | in plans: `bar_de_laatste_waarschuwing` |
| DEZE KANT BOVEN | **THIS END UP** | `design/worlds/shamsterdam/roodelicht_row_district.md:400` | in plans: `erotiek_en_zo` |
| DE ZWEETKELDER — KELDER NEGEN | **THE BOILER ROOM - NINE STEPS DOWN** | `design/worlds/shamsterdam/roodelicht_row_district.md:515` | in plans: `de_zweetkelder` |
| FRIETKOT DE VETTE VINGER — OPEN TOT 06:00 | **BRICK & LARD - OPEN TIL 6AM** | `design/worlds/shamsterdam/roodelicht_row_district.md:540` | in plans: `frietkot_de_vette_vinger` |
| FRIET / FRIET SPECIAAL / MAYONAISE | **FRIES / FRIES SPECIAL (DON'T ASK) / MAYO (NOT OPTIONAL)** | `design/worlds/shamsterdam/roodelicht_row_district.md:543` | in plans: `frietkot_de_vette_vinger` |
| HET WARME BAD — TARIEVEN | **MEMBERS ONLY - RATES** | `design/worlds/shamsterdam/roodelicht_row_district.md:566` | none |
| PAK ER EEN — TAKE ONE | **TAKE ONE. TAKE TWO. YOU KNOW WHY.** | `design/worlds/shamsterdam/roodelicht_row_district.md:625` | none |
| WIJ ZIJN VERHUISD → | **(papered-over old Dong Palace front) -> WE'VE MOVED. WE GOT BIGGER. ->** | `design/worlds/shamsterdam/roodelicht_row_district.md:650` | none |
| HYGIËNESCORE / IN BEHANDELING | **HYGIENE RATING: UNDER REVIEW (SINCE 2011)** | `design/worlds/shamsterdam/the_dong_palace.md:49` | `gunter_hygiene_card_examined`<br>in plans: `the_dong_palace` |
| EEN KEER DOPEN A.U.B. / ONE DIP PLEASE | **ONE DIP PER CUSTOMER. WE ARE WATCHING.** | `design/worlds/shamsterdam/the_dong_palace.md:58` | in plans: `the_dong_palace` |
| FONTEIN VAN DE GULLE GEVER — 2011 | **FOUNTAIN OF THE GENEROUS GIVER - 2011 (your q41 pick)** | `design/worlds/shamsterdam/the_dong_palace.md:48` | in plans: `the_dong_palace` |
| DE CACAOGALERIJ — Nu Geopend | **BONBONS & BALLS - NOW OPEN** | `design/worlds/shamsterdam/PNG_Assets/The_Dong_Palace_PNG_Assets.md:65` | in plans: `the_dong_palace` |
| VERVOLG → | **(into the Mechanical Wing) -> IT KEEPS GOING ->** | `design/worlds/shamsterdam/PNG_Assets/The_Dong_Palace_PNG_Assets.md:139` | in plans: `the_dong_palace` |
| GGD GOEDGEKEURD | **HEALTH DEPT. APPROVED (PROBABLY)** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:65` | in plans: `shamsterdam_condom_machines` |
| KAPOT / WERKT WEL | **OUT OF ORDER / IT WORKS, YOU'RE DOING IT WRONG** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:190` | in plans: `shamsterdam_condom_machines` |
| BEDANKT | **THANK YOU FOR YOUR PURCHASE. NO REFUNDS.** | `design/worlds/shamsterdam/shamsterdam_condom_machines.md:170` | none |
| DE BOTANISCHE LEUGEN — TULPEN SINDS 1637 | **THE TRANSIENT TULIP - DEAD ON ARRIVAL SINCE 1637** | `design/worlds/shamsterdam/de_botanische_leugen.md:34` | in plans: `de_botanische_leugen` |
| DE ZILTE WAARHEID — Haring Sinds 1952 | **THE SALTY SWALLOW - SWALLOWING SINCE 1952** | `dev/asset_team/plans/de_zilte_waarheid_plan.md:9` | in plans: `de_zilte_waarheid` |
| Haring / Met Uitjes (price board) | **HERRING / HERRING + ONIONS** | `design/worlds/shamsterdam/de_zilte_waarheid.md:38` | in plans: `de_zilte_waarheid` |
| Klein / Groot (price board) | **REGULAR / BOUGIE** | `design/worlds/shamsterdam/stroopwafel_cart.md:35` | in plans: `stroopwafel_cart` |
| AUTOMATIEK | **FRITOMAT - SINCE 1941** | `design/worlds/shamsterdam/frietomat.md:35` | in plans: `frietomat` |
| 24 UUR | **24 HOURS. THE FOOD IS OLDER.** | `design/worlds/shamsterdam/frietomat.md:36` | in plans: `frietomat` |
| BROUWERIJ | **BREWERY** | `design/worlds/shamsterdam/wobbly_windmill_brewery.md:49` | none |
| FIETS VERHUUR | **TRAM TRACK MAGNETS (q46: the alias replaced the main name)** | `design/worlds/shamsterdam/PNG_Assets/central_shamsterdam_bike_crossing_png_assets.md:414` | in plans: `central_shamsterdam_bike_crossing` |
| VOETGANGERS: U BENT NIET DE PRIORITEIT | **PEDESTRIANS: YOU ARE NOT THE PRIORITY** | `design/worlds/shamsterdam/interactions/central_shamsterdam_bike_crossing_interactions.json:133` | none |
| Nooduitgang | **EMERGENCY EXIT** | `design/worlds/shamsterdam/location_nodes/voetgangerstunnel_location_nodes.json:287` | in plans: `voetgangerstunnel` |
| Uitgang | **EXIT (PROBABLY)** | `design/worlds/shamsterdam/voetgangerstunnel.md:114` | in plans: `voetgangerstunnel` |
| Centrum | **DOWNTOWN** | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:43` | `centrum_sign`, `sign_centrum`<br>in plans: `voetgangerstunnel` |
| Centraal Station | **TERMINAL CHAOS (your q13 pick)** | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:9` | `centraal_station`, `centraal_station_sign`, `sign_centraal_station`<br>game/: `assets/data/navigation/voetgangerstunnel.json`<br>in plans: `voetgangerstunnel` |
| Museum Plein | **MUSEUM MILE (the existing district name)** | `design/worlds/shamsterdam/interactions/voetgangerstunnel_interactions.json:29` | `museum_plein`, `museum_plein_sign`, `sign_museum_plein`, `test_navigation_wrong_split_museum_plein`<br>game/: `assets/data/navigation/voetgangerstunnel.json`, `core/navigation_roll.gd`<br>in plans: `voetgangerstunnel` |
| Politie | **POLICE** | `design/worlds/shamsterdam/PNG_Assets/central_shamsterdam_bike_crossing_png_assets.md:299` | none |
| UIT DE WEG! / BEWEGEN! | **OUTTA THE WAY! / MOVE IT, TOURIST!** | `design/Quests/shamsterdam/bicycle_thunderdome.md:52` | none |
| Dat is vier / Drie vijftig | **That's four SOVS. ...Three-fifty.** | `design/worlds/shamsterdam/shamsterdam_museum_questionable_art.md:218` | in plans: `shamsterdam_museum_of_questionable_art` |
## Addendum (q63)
| Hendrik (the printer) | **Randy** (sign: RANDY — 2014 —) | `design/worlds/shamsterdam/roodelicht_row_district.md:363` | none |
