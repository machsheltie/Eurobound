# Audit: Tram Stop #17 (tram_stop_17), full 8-file review

## Files read (D = design/worlds/debaucheryville/)
- D tram_stop_17.md (main, whole to Connected Locations and Progressive Visual Changes)
- core/tram_stop_17_core.json
- environment/tram_stop_17_environment.json
- interactions/tram_stop_17_interactions.json (events and objects: tram_schedule_1994, shrine_offerings, jiris_documentation, adjacent_bench_seat)
- items/tram_stop_17_items.json (jiris_blessing only)
- location_nodes/tram_stop_17_location_nodes.json
- npcs/Tram_Stop_17/ : tram_stop_17_npcs.json (Jiri six visual states, pedestrian, tourist, tender), npc_tram_stop_17_ambient.md (Shrine Tender, Photo Tourist, others)
- PNG_Assets/Tram_Stop_17_Complete_PNG_Asset_Requirements.md
- sprite_mapping/tram_stop_17_sprite_mapping.json (exterior only, "built"; no interior entry)
- events/: no match. MISSING: no events/ file; no interior plate (none specified; the location is open-air, only the post-credits Heritage tram has an interior sprite, PNG doc l.285).
- Review: tram_stop_17_ext_review.jpg (no interior review)

## Q1, how well does it represent the location? Score: 3/5 (unchanged)
Painted: ornate green shelter, bench, "TRAMVAJ 17" sign, two lit boards, pigeons, tracks, trees. The plate is visit-1 "normal stop" and charming. The environment json requires things that sell the joke and are absent: the worn path in the cobbles in front of the bench, "17 FOREVER" scratched into the shelter glass, the 2002 "LOCAL MAN VOWS TO WAIT FOR TRAM" clipping pinned inside, the "FOUND / He's at Stop 17" missing poster, an umbrella, cracked plastic over a 1994 timetable, #17 tracks less worn than #9 and #22 (main md l.45). Tracks here are all equally mossy. Boards are tidy, no highlighter obsession.

## Q2, how well does it lean into the requirements? Score: 2/5 (unchanged)
Palette: #2E8B57 present but ornate and respectable; #708090 present; #A9A9A9 pigeons are only a few; #FF8C00 appears only as board glow, no candles (candles start at visit 5, so a visit-1 plate is defensible); #D2B48C cobbles dominate; #87CEEB sky only in the front elevation. Lighting spec asks streetlight #FFD700 radius 128 and shadow pools #696969; the night plate has cool blue and no warm streetlight. This is the "respectable Prague" result the author rejected. The grief is the doc's point, but the visual jokes (obsessive highlighting, pigeon colony, absurd documentation, city treating him as landmark) are missing.

## Verdict: REDO (exterior; no interior needed)

## Redo plan
- **Hook:** "The 17 Should Be Here Any Moment. The Schedule Says... Ah, The Schedule Is From 1994." (core.json subtitle).
- **Palette:** #2E8B57 chipped shelter, #708090, #A9A9A9 colony, #FF8C00 first candle stubs, #D2B48C cobbles with a visibly worn bench path, #87CEEB, #FFD700 streetlight at night.
- **Exterior:** rusted "TRAMVAJ 17" edges; cracked plastic over a yellowed 1994 timetable with Jiri's handwritten notes beside it (sprite_mapping: schedule_1994, jiris_notes); route map faded except the highlighted #17; "17 FOREVER" scratched in glass; pinned 2002 clipping; FOUND poster on a nearby wall; #9 and #22 tracks bright, #17 rusted and weedy; 4-6 pigeons including on the bench; bread pile by the bench leg; metro entrance and Absinthe Arcade glow at edges (location_nodes).
- **Interior:** none. Open-air by design.
- **Satire beats made visible:** the 1994 schedule; obsessively highlighted line; pigeons; worn cobble path; "17 FOREVER"; "LOCAL MAN VOWS TO WAIT FOR TRAM".
- **Not in the file, needs approval:**
  - Which Jiri state is the hero plate: visit 1 per the plate, or a more decayed state such as 5 (candles)?
  - Jiri as a separate sprite layer over the bench, as the sprite mapping implies?
  - Is a seedier tone wanted, given the doc's own "poignant, treated respectfully" line (Sensitivity Considerations)? Author ruling.
