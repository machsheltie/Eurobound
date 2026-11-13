# Audit: Three-Crown Keg Haus

**Files read (all 8 subfolder files plus main md), under design/worlds/debaucheryville/:**
- three_crown_keghaus.md (whole)
- core/three_crown_keg_haus_core.json
- environment/three_crown_keg_haus_environment.json
- interactions/three_crown_keg_haus_interactions.json
- items/three_crown_keg_haus_items.json
- location_nodes/three_crown_keg_haus_location_nodes.json
- npcs/Three_Crown_Keg_Haus/three_crown_keg_haus_npcs.json (the only file in that folder)
- PNG_Assets/Three_Crown_Keg_Haus_Complete_PNG_Asset_Requirements.md (incl. legacy sheets 1-5)
- sprite_mapping/three_crown_keg_haus_sprite_mapping.json
- events/: no match (MISSING)
- design/items/brewery_tour/{beer,opener,stamp}_three_crown_keg_haus_item.md
- dev/asset_team/reviews/three_crown_keg_haus_{ext,int}_review.jpg (re-viewed)

## Q1, how well does it represent the location? 2/5 (unchanged)
- Doc: "medieval dive bar reimagined by someone who failed architecture", "300-year-old castle turned frat basement", health-code violator (md Theme & Vibe). The exterior is a charming storybook cottage on a clean lane, patched roof and boarded shutters the only damage. The interior is a handsome candlelit medieval tavern with a coordinated booth set. That is respectable.
- Hits: crown-over-stein backlit sign, boarded shutters, throne behind the bar, crown heraldry, chandelier. Decoration, not decay.

## Q2, interior and exterior requirements? 2/5 (unchanged)
New files add requirements the plates ignore:
- Palette: md/PNG list #CC5500 rust, #6A0DAD faded purple, #5C4033 dive brown, #8B4513 wood decay, vomit green #9ACD32, mustard #FFDB58. core.json and environment.json use rust orange, beer amber, mold green, tarnished brass. Plates are polished amber/brown; mold green and mustard absent, purple only on doors and rugs.
- Missing: zero passed-out patrons (location_nodes tck_floor "safe and unsafe tiles among passed-out patrons"; PNG sheet 2 obstacles), no worn-versus-intact tile contrast, chandelier is large barrels not mini-kegs, sconces are plain (md: beer-foam shaped), no gaffer tape, no mustard art, no mold, no vomit, no bouncer, no tracksuits, no misaligned tap handles, no health-code signage ("Noble by Name" / "Not by Health Code"), no sticky floor outside.
- Interior is large and open; md says "single cramped room".

## Verdict: REDO, both (unchanged)
Not over the top; a tidy fantasy inn.

## Redo plan
- **Hook:** "Noble by Name, Not by Health Code" (md subtitle); card text "Noble by Liver" (core.json).
- **Palette:** #CC5500 rust on metal and signage, #5C4033 and #8B4513 grimy wood, #6A0DAD faded tracksuit and velvet, mustard #FFDB58, mold and vomit green accents (PNG Color Palette).
- **Exterior (tck_alley, tck_entry):** lopsided failed-architect building, rusting crown sign over stein, sticky stained alley, cabbage steam, "Bravado Entrance Warning" sign, kegs and bin.
- **Interior (tck_floor, tck_barflies, tck_sentinel, tck_service, tck_throne):** one cramped room; creaky-floor tiles in two tones plus warning pulse; mini-keg chandelier; foam-shaped sconces; gaffer-taped moldy booths; chairs and stools at wrong heights; mustard wall art; peeling plaster over brick; rusted heraldry; misaligned taps and goblets on the bar; velvet keg throne ringed by kegs and a velvet rope; Keg Sentinel arm-wrestling table.
- **NPC stations:** bartender in tracksuit at tck_service (npcs.json "tarnished apron and miniature crown pins"); slumped tracksuit nobles on tiles and booths; Slurring Bar Flies around booths; Keg Sentinel at keg stacks.
- **Satire beats made visible:** tracksuit nobles, mustard art, gaffer tape, "Noble by Name Not by Health Code" signs, goblet heritage next to puddle and mold (md Seedy Underbelly).
- **Lighting:** hazy orange foam sconces, flickering chandelier, minimal daylight (md); emission mask per sprite_mapping.

## Conflicts, approval questions
1. Tour slot: md "3 of 4"; core.json "Stop 2".
2. Palette: md/PNG versus core.json/environment.json (purple and brown versus amber, mold green, brass). Which governs?
3. md has bartender opener-check dialogue, bouncer mini-boss and wake-on-failure; JSONs say no opener gate and omit the bouncer. Is the bouncer cut?
4. Tracksuit nobles and bouncer are in md/PNG but not npcs.json.

## Not in the file, needs approval
Are the passed-out nobles painted into the plate or separate sprites, and how many (npcs.json caps ambient groups at 4 each)?
