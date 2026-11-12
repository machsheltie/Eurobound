# PROPOSAL, awaiting author approval

**Debaucheryville district diagram, drafted from canon only** (bead Eurobound-eaiq; ruling under Eurobound-467, 2026-11-12).

Nothing here is a ruling. Where canon is silent or disagrees, the item is parked in "Unplaced" or in "Open questions", with options the author can tap. No locations, districts, streets or lore were invented. Every placement and link below cites `path:line`. All paths are under `design/worlds/debaucheryville/` unless they start with `design/` or `docs/`.

Diagram: `debaucheryville_district_diagram.svg` (PNG render beside it). The Absinthe Arcade is drawn at the centre of attention, straddling the two districts canon puts it in.

Author rulings this work sits under (Eurobound-467, 2026-11-12): streets are HD-2D painted streets from a per-city modular street kit with a follow camera; agents draft a district diagram per city from canon for approval before any art; Debaucheryville first, around the Absinthe Arcade. The author attached a condition ("If this is typically how the hd-2d hybrid games handle it"), answered in the HD-2D note at the end.

## 1. District table

The six named districts come from `debaucheryville.md` lines 5-47. Three more regions appear in location docs but not in that list: Circus Grounds, Opera Ruins District, Central District. They are drawn dashed.

| District | Locations placed in it (and the line that places each) |
|---|---|
| **1 The Gilded Square** (Tourist Trap Central; `debaucheryville.md:5-10`) | Astronomical Cock-Up Square, the hub, "The Gilded Square District, Central Tourist Hub" (`astronomical_cockup_square.md:10`; `debaucheryville.md:7`). Euro Ink 4 Less, "Alley off Astronomical Cock-Up Square" (`euro_ink_4_less.md:10`, `:82`). Shadow Exchange, "Sub-basement beneath Gilded Square backstreets" (`shadowexchange.md:10`; entrance "off market square", `:29`). Three Crown Keg Haus, "Shadowed alley near Shadow Exchange" (`three_crown_keghaus.md:10`). Named only in the square doc, no profile of their own: Clocktower Cafe and Public Restroom (Paid) (`astronomical_cockup_square.md:395-398`). |
| **Circus Grounds** (own region, "edge of the Gilded Square"; not in the district list) | The Cirque du Shady (`cirque_du_shady.md:10`, `:84`, `:88`). Mystery Meat Cart, "next to carnival ringmaster tent" (`mysterymeatcart.md:10`). The Participation Trophy (`the_participation_trophy.md:11`). See Q11. |
| **2 Clocktower Plaza** (Puzzle Hub District; `debaucheryville.md:12-17`) | The Tap Dat Vault, "Hidden cellar beneath Clocktower Plaza" (`the_tap_dat_vault.md:10`, `:46`; ledger: "Clocktower Plaza cellar IS canon", `docs/superpowers/NEXT_WORK.md:263`). The Absinthe Arcade is placed here by its own doc, but see Q1. |
| **3 Neon Quarter** ("Absinthe Arcade", Neon Entertainment Quarter; `debaucheryville.md:18-23`) | Neon and Chrome Boutique, "Absinthe Arcade, Neon Entertainment Quarter (premium end)" (`neon_and_chrome_boutique.md:11`; `core/neon_and_chrome_boutique_core.json:6`). Threads and Treads (`threads_and_treads.md:11`). The Bohemian Trap (`the_bohemian_trap.md:11`). The Strobe Survival Kit, "near club entrances" (`the_strobe_survival_kit.md:11`; `core/strobe_survival_kit_core.json:6` "Neon Quarter club approach"). The Absinthe Arcade is placed here by the district list and the shop docs, but see Q1. |
| **Absinthe Arcade (building) and its inside** | Absinthe Arcade (`absinthearcade.md:10`; `location_nodes/absinthe_arcade_location_nodes.json:9`). Absinthium Taproom, "Hidden behind the Absinthe Arcade (north end)" (`the_absinthium_taproom.md:11`, `:48`; `absinthearcade.md:41`). Claw Machine Maintenance Closet, "Absinthe Arcade (hidden area)" (`clawmachinemaintenanceclosetrestroom.md:10`, `:29`). |
| **4 Hostel Row** (Budget Accommodation District; `debaucheryville.md:24-29`) | Hostel Midnight Checkout (`hostel_midnight_checkout.md:11`). Midnight Munchies General Store (`midnight_munchies_general_store.md:11`). Cyberspace Kavarna, "Basement level beneath Hostel Row" (`cyberspacekavarna.md:10`, `:29`), but see Q2. Backroom Concessions, inside the Kavarna (`backroomconcessions.md:10`, `:35`). |
| **5 Kebab Alley** (Underground Vice Corridor; `debaucheryville.md:31-39`) | Late-Night Kebab Stand, "Near Velvet Curtain Club alley exit" (`Late-Night Kebab Stand.md:10`, `:29`; the district entry mentions "the kebab stand", `debaucheryville.md:33`). Public Restroom / Grease Trap Shrine, "Debaucheryville - Kebab Alley - Behind Grease Vendor Tent" (`publicrestroomkebaballey.md:4`; `core/public_restroom_grease_trap_shrine_core.json:6`). Also in the district entry: a knockoff vape stall, a crypto ATM, Slick Greg (`debaucheryville.md:33-39`). |
| **Opera Ruins District** (own region; not in the district list) | Velvet Curtain Club, "Dead-end service lane behind opera ruins" (`velvet_curtain_club.md:10`, `:250`; "Opera Ruins District", `:522-523`). VIP Stall, behind the club's Staff Only curtain (`velvetcurtainclubvipstall.md:10`). Ye Olde B.R.E.W. Lab, club basement (`ye_olde_brew_lab.md:10`). See Q6. |
| **6 The Bacchanus Riverfront** (Fake Beach Resort District; `debaucheryville.md:41-47`) | The Bohemian Riviera: Fauxst Beach, beach-bar strip, Beatdown filming site (`bohemian_riviera.md:10`; `debaucheryville.md:44`). |
| **Central District** (own region; not in the district list) | Tram Stop 17, "Central District, between Absinthe Arcade and the Gilded Square" (`tram_stop_17.md:10`). Metro Station Entrance, named only in the tram doc (`tram_stop_17.md:234`; `location_nodes/tram_stop_17_location_nodes.json:60`). See Q7. |

**Counts.** 28 location node files exist under `location_nodes/`. 26 are placed in the diagram (several with an open question on them). 2 are unplaced: Internet History Museum and Meme Black Market. Three more places are named in a neighbour doc only and are drawn but have no profile: Clocktower Cafe, Public Restroom (Paid), Metro Station Entrance.

## 2. Connections stated by canon

| From - To | What canon says | Cite |
|---|---|---|
| Absinthe Arcade - Clocktower Plaza | Side street off the plaza; node data: plaza is "south", "immediate side street" | `absinthearcade.md:29`; `location_nodes/absinthe_arcade_location_nodes.json:361-364` |
| Absinthe Arcade - Tram Stop 17 | Arcade is "South, 1 block" of the stop | `tram_stop_17.md:232`; `location_nodes/tram_stop_17_location_nodes.json:48` |
| Tram Stop 17 - Gilded Square / Astronomical Cock-Up Square | "North, 2 blocks" | `tram_stop_17.md:233`; `location_nodes/tram_stop_17_location_nodes.json:54` |
| Tram Stop 17 - Metro Station Entrance | "East, 2 blocks" | `tram_stop_17.md:234`; `location_nodes/tram_stop_17_location_nodes.json:60` |
| Tram #9 | Goes to the Velvet Curtain district | `tram_stop_17.md:237`; `location_nodes/tram_stop_17_location_nodes.json:70` |
| Tram #22 | Goes to the hostel district | `tram_stop_17.md:238`; `location_nodes/tram_stop_17_location_nodes.json:75` |
| Cyberspace Kavarna - Metro platform | Hidden back exit, unlocked by one ICQ sting; Hostel Row street access by a narrow staircase | `cyberspacekavarna.md:25`, `:49`, `:160`; `:22`, `:29` |
| Absinthe Arcade - Absinthium Taproom | Hidden, through a curtain at the north end (after 20:00) | `the_absinthium_taproom.md:48`; node file `:368` |
| Absinthe Arcade - Claw Machine Closet | Locked maintenance door beside a broken DDR machine; 3 arcade tokens | `clawmachinemaintenanceclosetrestroom.md:29`; node file `:376` |
| Gilded Square - Euro Ink 4 Less | Alley off the square; "Back to Astronomical Cock-Up Square via alley" | `euro_ink_4_less.md:10`, `:31` |
| Gilded Square - Cirque du Shady | Main gate on the west side to Gilded Square streets | `cirque_du_shady.md:27`, `:268-269` |
| Cirque du Shady - Bohemian Riviera | Riverside "Shady Productions gear path", east from the Cirque, downriver from the Riviera | `cirque_du_shady.md:27`, `:273`; `bohemian_riviera.md:25`, `:76`, `:324` |
| Bohemian Riviera - Gilded Square | Landward exit; the street narrows and opens onto the sand | `bohemian_riviera.md:25`, `:72`, `:320` |
| Velvet Curtain Club - Kebab Alley | Back entrance by a milk-crate climb; Kebab Alley crowds stumble in from the club | `velvet_curtain_club.md:522`; `debaucheryville.md:37`, `:39` |
| Velvet Curtain Club - Opera Ruins | Main alley, the primary approach | `velvet_curtain_club.md:523`, `:250` |
| Shadow Exchange - Three Crown Keg Haus | Keg Haus is in a shadowed alley near the Exchange | `three_crown_keghaus.md:10`, `:46`; `:39` |
| Mystery Meat Cart - Cirque du Shady | Next to the ringmaster tent | `mysterymeatcart.md:10`, `:29` |
| Velvet Curtain Club inner links | VIP Stall behind a Staff Only curtain; Brew Lab down back stairs in the club basement | `velvetcurtainclubvipstall.md:10`, `:22`; `ye_olde_brew_lab.md:10`, `:39` |
| Kebab stand - Velvet Curtain Club | Stand sits near the club's alley exit | `Late-Night Kebab Stand.md:29` |
| Internet History Museum - Meme Black Market | Hidden behind a VHS shelf (3:33 AM) | `internethistorymuseum.md:51`; `memeblackmarket.md:29` |

The ledger (`docs/superpowers/NEXT_WORK.md`) has no Debaucheryville district-geography ruling beyond the Tap Dat Vault cellar (`:263`). The canon index (`tools/canon_index`) found nothing further for "Debaucheryville districts geography".

## 3. Unplaced items (canon is silent, so nothing is invented)

- **Internet History Museum.** Only "Former Blockbuster building, downtown district" and "Front door back to Debaucheryville streets" (`internethistorymuseum.md:10`, `:22`, `:29`). No listed district.
- **Meme Black Market.** Inside the Museum (`memeblackmarket.md:10`, `:29`). Moves with the Museum.
- **Street links between the district clusters.** Canon states no street, alley or bridge link between: the Gilded Square cluster, the Neon Quarter/Clocktower Plaza cluster, Hostel Row, Kebab Alley / Opera Ruins, and the Riverfront, other than the links in section 2 (tram, metro, the Cirque path and the Riviera landward exit). In particular nothing states how Hostel Row, Kebab Alley or the Opera Ruins connect to the rest on foot. See Q8.
- Generic exit names in the node files (`gilded_square_streets`, `night_party_zone`, `velvet_curtain_district`, `hostel_district`; `location_nodes/astronomical_cockup_square_location_nodes.json:52`, `bohemian_riviera_location_nodes.json:45`, `:66`, `tram_stop_17_location_nodes.json:70`, `:75`) are not defined anywhere as districts and are not drawn.

## 4. Open questions

Each option below is a placement or reading already in canon. None is new content. Pick one per question, or write your own.

### Q1. Where is the Absinthe Arcade: Clocktower Plaza or the Neon Quarter?
- **For Clocktower Plaza:** `absinthearcade.md:10` ("Clocktower Plaza (side street beneath a green-lit arch)"), `:29`; `location_nodes/absinthe_arcade_location_nodes.json:9` (`clocktower_plaza_side_street`), `:361-364`; `the_tap_dat_vault.md:10` puts a cellar under the plaza.
- **For Neon Quarter:** `debaucheryville.md:18-19` (district 3 is "Absinthe Arcade", Neon Entertainment Quarter); `neon_and_chrome_boutique.md:11`, `threads_and_treads.md:11`, `the_bohemian_trap.md:11` ("Absinthe Arcade, Neon Entertainment Quarter"); `core/neon_and_chrome_boutique_core.json:6`, `core/strobe_survival_kit_core.json:6`.
- Related: "Absinthe Arcade" is both the name of district 3 (`debaucheryville.md:18`) and the name of a building, which also bumps against the all-names-unique rule.
- Options:
  1. Arcade stands in Clocktower Plaza; the Neon Quarter is a separate neighbouring district with the four shops.
  2. Arcade stands in the Neon Quarter; the "Clocktower Plaza side street" wording is dropped.
  3. Arcade sits on the boundary: entered from the Clocktower Plaza side street, inside the Neon Quarter district.

### Q2. Cyberspace Kavarna: Hostel Row basement, or beside the metro?
- **Hostel Row basement:** `cyberspacekavarna.md:10` ("Basement level beneath Hostel Row"), `:22`, `:29`, `:33`; node file id `debaucheryville_hostelrow_cyberspace_kavarna_01` (`location_nodes/cyberspace_kavarna_location_nodes.json:2`).
- **Metro side:** `debaucheryville.md:76` ("Underground Connection Point") and `:79` ("Metro platform access for quick travel"); `design/game_design_document.md:138` (Wi-Fi at "metro platform"); `cyberspacekavarna.md:49`, `:160` (hidden back exit to the metro). The tram doc puts the Metro Station Entrance 2 blocks east of Tram Stop 17 in the Central District (`tram_stop_17.md:234`).
- Note: no doc says "beside the metro" in those words. The closest is the hub doc's "Underground Connection Point". The tension is Hostel Row (district 4) versus the Central District where the tram doc puts the metro.
- Options:
  1. Hostel Row basement; the metro is reached only through the hidden back exit (underground link, no street adjacency).
  2. Hostel Row basement, and the Metro Station Entrance also sits in Hostel Row.
  3. Move the Kavarna to the Central District beside the Metro Station Entrance.

### Q3. "Kebab Alley" is a duplicate name (all names must be unique)
- **Debaucheryville:** `debaucheryville.md:31` (district 5, Underground Vice Corridor), `publicrestroomkebaballey.md:4`, `velvet_curtain_club.md:522`.
- **Publandia:** `design/worlds/publandia/publandia.md:30-31` ("Kebab Alley (Seedy Underbelly)", After-Hours Chaos Street), `design/game_design_document.md:58`, `design/Quests/general_quests/greatdonerdebate.md:86`.
- Options:
  1. Debaucheryville keeps the name; Publandia's is renamed.
  2. Publandia keeps the name; Debaucheryville's is renamed.
  3. Rename both.

### Q4. Is Euro Ink's "24-Hour Kebab Shop" the Late-Night Kebab Stand?
- Euro Ink's doc says a "24-Hour Kebab Shop" is "next door" to it in the Gilded Square (`euro_ink_4_less.md:384`; node file `location_nodes/euro_ink_4_less_location_nodes.json:53`).
- The Late-Night Kebab Stand is "Near Velvet Curtain Club alley exit" (`Late-Night Kebab Stand.md:10`, `:29`) and in the Kebab Alley entry (`debaucheryville.md:33`).
- Options:
  1. Same place; the Euro Ink adjacency line is the one to change.
  2. Two kebab places: the Stand in Kebab Alley and an unprofiled 24-Hour Kebab Shop in the Gilded Square.
  3. Same place, and Euro Ink's alley sits next to Kebab Alley.

### Q5. Is Euro Ink's "Suspicious Currency Exchange" the Shadow Exchange?
- Euro Ink: "Other neighbor, 3% worse rates" (`euro_ink_4_less.md:385`).
- Shadow Exchange: sub-basement beneath Gilded Square backstreets, entrance off the market square (`shadowexchange.md:10`, `:29`).
- Options:
  1. Same place.
  2. Two currency changers; the Euro Ink neighbour is an unprofiled street-level one.
  3. Leave unplaced until the author says.

### Q6. Which district is the Velvet Curtain Club in?
- It is "behind opera ruins" and in "Opera Ruins District" (`velvet_curtain_club.md:10`, `:250`, `:522-523`). It has a back entrance onto Kebab Alley (`velvet_curtain_club.md:522`; `debaucheryville.md:37`, `:39`). Tram #9 goes to the "Velvet Curtain district" (`tram_stop_17.md:237`). The six-district list does not name any of these.
- Options:
  1. Opera Ruins District is a seventh district, adjacent to Kebab Alley.
  2. The club belongs to Kebab Alley (district 5); "Opera Ruins" is just its alley.
  3. The club belongs to the Neon Quarter (nightclub next to the club approach, `core/strobe_survival_kit_core.json:6`).

### Q7. What is the "Central District", and where is the metro?
- Tram Stop 17 is in the "Central District, between Absinthe Arcade and the Gilded Square" (`tram_stop_17.md:10`), 1 block from the Arcade and 2 from the Gilded Square (`:232-233`). The Central District is not in the district list.
- Options:
  1. Central District is its own district (seventh or eighth).
  2. It is the strip of Clocktower Plaza streets between the Arcade and the Gilded Square.
  3. It is just the streets between districts, with no region of its own; the stop and metro entrance are street furniture.

### Q8. How do Hostel Row, Kebab Alley / Opera Ruins and the Riverfront connect on foot?
- Canon gives only: Tram #22 to the hostel district, Tram #9 to the Velvet Curtain district, the Kavarna metro back exit, the Riviera landward exit and the Cirque path (section 2). No street joins them to the Gilded Square / Clocktower / Neon cluster.
- Options:
  1. Use only the tram and metro links for Hostel Row and Opera Ruins; no street links.
  2. Metro is the hub: Hostel Row and the Central District are joined underground, other districts by tram.
  3. Author supplies the street layout for these districts.

### Q9. Where is the Internet History Museum?
- "Former Blockbuster building, downtown district" (`internethistorymuseum.md:10`, `:29`). "Downtown" is not a listed district.
- Options:
  1. Leave unplaced until the author places it.
  2. Treat "downtown" as the Central District (see Q7).
  3. Treat "downtown" as the Gilded Square (tourist hub).

### Q10. Is Clocktower Plaza the same ground as the Gilded Square's clock square?
- Gilded Square is "Centered on Astronomical Cock-Up Square, the ancient-clock landmark" (`debaucheryville.md:7`). Clocktower Plaza has "Time-based switches... clock chimes" (`debaucheryville.md:13-16`) and no listed landmark. The Gilded Square has a "Clocktower Cafe" (`astronomical_cockup_square.md:397`); the Velvet Curtain Club needs wristbands "from Clock Square" (`velvet_curtain_club.md:526`).
- Options:
  1. Two districts, as the list states; Clocktower Plaza has no landmark clock.
  2. Clocktower Plaza is the clock square, part of the Gilded Square.
  3. Two districts, with the Plaza a back square off the clock square (author to say).

### Q11. Is the Circus Grounds its own district?
- "Circus Grounds (edge of the Gilded Square District)" (`cirque_du_shady.md:10`), "accessible from the Gilded Square District" (`:23`). The hub doc lists the Cirque under Buildings, not Streets & Districts (`debaucheryville.md:69-73`).
- Options:
  1. Own district beside the Gilded Square.
  2. Part of the Gilded Square District.
  3. Part of the Riverfront (it links to the Riviera by the gear path).

### Other findings (no question needed)
- `debaucheryville.md:84` misspelled "The Bohemian Trap" (the location doc and node file had it right). Fixed under Eurobound-kkp5.

## 5. HD-2D note (answers the author's condition on ruling q1)

I searched the web (Unreal Engine developer interviews, Nintendo Life, Inverse, game reviews) and could fetch only some pages directly. Findings:

- Octopath Traveler I and II, Triangle Strategy: 3D environments with 2D pixel-art sprites on top. Octopath II's interview says the team combined UE4's 3D environments with 2D pixels ([Unreal Engine interview](https://www.unrealengine.com/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style); also [Nintendo Life on Octopath II](https://www.nintendolife.com/news/2022/10/octopath-traveler-ii-devs-aimed-to-make-its-hd-2d-visuals-picture-perfect)). Triangle Strategy's producers describe "rich HD 3D backdrops" with pixel-art characters ([Nintendo Life](https://www.nintendolife.com/news/2022/05/triangle-strategy-producers-talk-hd-2d-and-why-other-devs-havent-used-it)).
- Camera: search summaries of the Octopath II interview say exploration still uses a fixed camera, as in the first game, so places fit on one screen, with camera rotation used for battle effects and events. The Triangle Strategy producer piece says Octopath used a fixed camera while Triangle Strategy needed a map you can rotate 360 degrees (same Nintendo Life link). I could not fetch the Unreal Engine page itself (HTTP 403), so the Octopath exploration-camera line comes from search summaries of it.
- Bravely Default 2: reviews say the towns zoom out to show the whole town and zoom in to run the paths, with a diorama or pop-up-book feel, and the camera pans when you enter a town ([Tom's Guide](https://tomsguide.com/reviews/bravely-default-ii-review), [GamesRadar](https://www.gamesradar.com/bravely-default-2-review)). I did not find a clear statement of whether its field camera is fixed or player-rotatable.
- Star Ocean: The Second Story R: the director says it is not an HD-2D title, but a blend of 2D pixel characters with a custom shader in 3D environments ([Inverse interview](https://www.inverse.com/gaming/star-ocean-second-story-r-interview-developers-square-enix)). I found nothing on its town cameras or sizes.
- Live A Live HD-2D was not researched.

**Verdict.** "HD-2D streets are 3D environments with 2D sprites, rendered in an engine such as UE4" matches the sources. "Painted textures", "a per-city modular kit" and "town size" are not confirmed by anything I found, and no source says how many screens or square metres a town covers. The real difference is the camera: Octopath's exploration camera is reported as fixed per area (a place fits on one screen), and only Triangle Strategy is described as freely rotating, so a scrolling follow camera over a streets-long district is not shown by these sources and should be treated as the author's own design choice.
