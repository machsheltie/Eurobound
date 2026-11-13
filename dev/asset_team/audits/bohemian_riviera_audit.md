# Audit: The Bohemian Riviera (bohemian_riviera), full 8-file review

## Files read (D = design/worlds/debaucheryville/)
- D bohemian_riviera.md (main, whole)
- core/bohemian_riviera_core.json
- environment/bohemian_riviera_environment.json
- interactions/bohemian_riviera_interactions.json (events and objects; read to the sign-up and gauntlet sequences, remainder skimmed)
- items/bohemian_riviera_items.json (badge, stein, Hamagotchi, Kokos Loco Bucket, Tan Line Shooter)
- location_nodes/bohemian_riviera_location_nodes.json
- npcs/Bohemian_Riviera/ : bohemian_riviera_npcs.json, janek_sykora.md, jaxson_vane.md, petra_production_assistant.md, queen_riviera_renata.md, rosta.md, standa.md, zdenka.md (station and appearance lines read)
- PNG_Assets/Bohemian_Riviera_Complete_PNG_Asset_Requirements.md (palette, bar facades, props)
- sprite_mapping/bohemian_riviera_sprite_mapping.json (interior plate "not_built_yet")
- events/: no match. MISSING: no subfolder file; no events/ file; no interior plate.
- Review: bohemian_riviera_ext_review.jpg (no interior review exists)

## Q1, how well does it represent the location? Score: 3/5 (was 4)
Painted well: three-unit potty catapult, "BEATDOWN - LETO - SEZONA 22" banner, EMTV crane, 2003 pallet, NO DIVING sign, heaters, inflatable palms, and the three bars (container, tanning-bed neon, tiki hut). core.json names six zones; the plate shows three. Missing: signup_table with fanned forms (Petra), prize_podium (Janek's fourth mark, Jaxson's raised mark), Zdenka's shower cart, Rosta's boat-hook station and potty monuments, Standa in the tower with the paperback, the stapled "40 TONS - NOT FOR HUMAN CONSUMPTION" receipt on the signpost, the damp stain, the broken centre latch. Palms stand upright (doc: sag). River reads as clear green. The interior is entirely absent, and the sprite mapping confirms it.

## Q2, how well does it lean into the requirements? Score: 3/5 (unchanged)
Palette: #E8D4A0 sand correct, #32CD32 palms correct, #5E7350 river is pretty rather than murky. #FF1493 EMTV magenta appears as a small logo and bar neon, not on the signage. Environment json asks for heat shimmer off the sand, camera flashes, flies, a lifeguard spotlight sweep and #FFC966 string pools: only string lights and one heater glow appear. The whole plate reads tropical resort, not the "beach resort for a country with no beach and no shame."

## Verdict: REDO (exterior; interior not built)
Good bones, too clean, half the zones missing.

## Redo plan
- **Hook:** a landlocked beach resort run on trucked-in sand and a reality-TV catapult (core.json satirical_design).
- **Palette:** #E8D4A0, #5E7350 murky, #FF1493, #708090, #32CD32 drooping, #FF7F32, #FFC966.
- **Exterior:** keep layout. Add signup_table with four-page forms and headset, prize_podium with Shady Productions banner creased through the fold, Zdenka's cart and sun-bleached sign, Rosta's stand with chart in a plastic sleeve, Standa's tower, the stapled receipt, damp stain, open centre latch, heat shimmer, flies, spotlight sweep. Sagging palms.
- **Interior:** no interior in any file; the sprite mapping reserves bohemian_riviera_int_day/night. If approved, use the three bar interiors (Za Za Beach Klub container, The Tan Line tanning-bed sports bar, Kokos Loco tiki hut) with the shared bar TV looping the episode.
- **Satire beats made visible:** NO DIVING (SERIOUSLY, IT'S 40cm); 2003 pallet; plastic coconuts; potty monuments with laundry; "THE BOHEMIAN RIVIERA" signpost with a manifest number.
- **Not in the file, needs approval:**
  - Does the Riviera get an interior, or only bar facades? (no file defines one)
  - night_party_zone plate, with Queen Riviera Renata's spot?
