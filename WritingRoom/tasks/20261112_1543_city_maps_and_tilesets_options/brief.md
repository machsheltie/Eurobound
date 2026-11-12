# City maps and tilesets options

Bead Eurobound-467. The author's answer, verbatim: "Send it to the Writers' Room to draft options". The Asset Development Team brought the brief; the questions are on the Production Desk as Eurobound-467-q1..q4.

**Goal:** city MAPS and TILESETS for all four cities (Debaucheryville, Shamsterdam, Publandia, Sinfonia). The look is 2.5D HD-2D in the vein of Bravely Default 2 and Star Ocean 2. It must be original: never copied from another game and never generic. Nothing street-level exists yet.

**Your job is OPTIONS, not decisions.** For each question, give 2-3 distinct options. Each option gets a one-paragraph case, its costs and risks, and a recommendation. The author rules.

## Facts to work from
- **Approved places today are HD-2D painted plates on simple geometry.** That covers the location plates and the Absinthe Arcade, whose rooms are fixed-camera paintings at about 29 degrees pitch (game/core/.../hd2d_projected_room.gd; the exterior uses PAINT_SCALE 2.4).
- **EUROBOUND_PRD.md §13 (lines 518-538) is NOT canon.** It specifies 320x180, 16x16 oblique pixel tiles and ~250-tile tilesets per city. That PRD comes from the dead, superseded branch (.claude/CLAUDE.md). You may name its approach as one option, but never as a requirement.
- **The binding 3D rule** (design/style_guides/3d_asset_rules.md): if 3D street meshes are built, the author hand-paints distress and supplies the base material textures.
- **Travel and maps:** there is no overworld; travel between cities is a rail montage. The pause menu has no map (docs/superpowers/NEXT_WORK.md:706).

## The questions
- **Q1, build method.** Options include: HD-2D painted streets with a per-city "street kit" (ground surfaces such as cobble, canal and river; facade pieces; street props); the old tileset approach; or something else.
- **Q2, map unit.** Options include:
  - one fixed-camera painted plate per street or square, joined by exits like the Arcade rooms
  - a scrolling street with a follow camera, built from modular pieces
  - a mix: plates for squares, scrolling connectors
- **Q3, layouts.** No city has a street layout, only district lists:
  - **Debaucheryville** (design/worlds/debaucheryville/debaucheryville.md:4-47): Gilded Square, Clocktower Plaza, Absinthe Arcade/Neon Quarter, Hostel Row, Kebab Alley, Bacchanus Riverfront.
  - **Shamsterdam** (shamsterdam.md:10-56): Roodelicht Row, Canal Ring, Coffeeshop Quarter, Cheese & Clog Corner, Museum Mile. The Bike Crossing hub has exits N Canal Ring, S Roodelicht, E Museum Mile and W Coffeeshop Quarter (central_shamsterdam_bike_crossing_location_nodes.json:27-30). Roodelicht Row has a full layout (roodelicht_row_district.md:86).
  - **Publandia** (publandia.md:4-36): Market Street, The Craic Tax, Brewery District, Quay of Last Resort, Kebab Alley. The Cloverleaf is a 6-exit roundabout (cloverleaf_location_nodes.json:250).
  - **Sinfonia** (sinfonia.md:4-35): Imperial Square, MusikGasse, Kaffeehaus Row, Trainspotting Square (no location file).
  - Most locations name their district in an "Area Zone" line.
  - Draft a district-adjacency sketch per city (which district connects to which, and where each location sits). Use only existing canon names. Any NEW district or street name goes in a list for the author, unused.
  - Canon conflicts to give options on, not resolve:
    - The Arcade is placed in both Clocktower Plaza and the Neon Quarter (debaucheryville.md:13 vs :19).
    - Cyberspace Kavarna is both a Hostel Row basement and a metro platform (:76-79).
    - Shamsterdam areas named in location docs but missing from the city list: Harbor, Old Town, Floating Flower Market.
  - Debaucheryville has two Kebab Alleys (Debaucheryville and Publandia), which breaks the unique-names rule. Flag it.
- **Q4, first city.**
  - Debaucheryville: the most art (the Arcade plus about 20 location plates).
  - Shamsterdam: the clearest layout canon, plus 3 approved exteriors.
  - Publandia: first in story order.

## Deliverable: drafts/<writer>_city_maps_options.md
Four sections (Q1-Q4). Q3 has one sub-section per city. Keep it plain and decision-ready: the author taps an option.

## Rules
- No real place names in anything player-facing. Use parody names only.
- This is a design-options paper, not game text, so the bros don't speak in it.

Save early, post a summary, then vote done.
