# Audit: Internet History Museum (debaucheryville)

Standard: "I don't want respectable Prague. I want Debaucheryville." MA game, satire at full strength.

## Files read (all under `design/worlds/debaucheryville/`)
1. Main md: `internethistorymuseum.md`
2. `core/internet_history_museum_core.json`
3. `environment/internet_history_museum_environment.json`
4. `interactions/internet_history_museum_interactions.json`
5. `items/internet_history_museum_items.json`
6. `location_nodes/internet_history_museum_location_nodes.json`
7. `npcs/Internet_History_Museum/internet_history_museum_npcs.json` (only file in that folder)
8. `PNG_Assets/Internet_History_Museum_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/internet_history_museum_sprite_mapping.json`
- `events/`: no match (MISSING). Cross-mentions only in `maps/debaucheryville_district_diagram_proposal.md` (no district placed).
- Reviews: `dev/asset_team/reviews/internet_history_museum_ext_review.jpg`, `_int_review.jpg`.

## Scores
**Q1, represents the location: 4/5.** Exterior carries every doc beat: floppy-boarded double doors, "AOL USERS ONLY" tape (twice), glitching pink Comic Sans banner, PalmPilot camera, "ZOMG LOL WTF M8?", pigeons on the 404 sign (md Exterior Description). Interior shows modem pyramid, GeoCities diorama, Angelfire flames, Habbo smiley with knife and chalk outline, MSN graveyard with green lights and webcams, iMac G3 altar with burned CDs, Chuck E. with Furbies. Misses from the new files: no Museum Lobby free-entry desk, no printer-paper Comic Sans plaques (md Decorative Elements), no readable VHS shelf at `ihm_vhs_shelf`, no Curator or Night Security stations.

**Q2, design requirements: 3/5.** The roof is now CRT Blue #4169E1 and the banner pink #FF6EC7 (core.json palette: Blockbuster blue, CRT green, static grey, Comic Sans yellow, darkroom cyan). But walls are tan and brown, the street is warm cobble, and the whole front is a tasteful weathered corner shop. The doc's joke is academic reverence for garbage; the building has no portico, plaque, or velvet queue to show it, and there is no Blockbuster-yellow. Interior is over the top and strong.

**Verdict: REDO exterior, patch interior.** Exterior is still respectable-decayed; interior stays.

## Redo plan
**Hook:** A dead Blockbuster run as a sacred museum of garbage ("Preserving Our Digital Past (In Comic Sans)").
**Palette:** #4169E1 on roof, awning AND wall wash; #FF6EC7 glitching banner and neon edge; #A9A9A9 only for pavement; add Comic Sans yellow and CRT green window spill (core.json, environment.json lighting_system).
**Exterior (`ihm_exterior`, "Former Blockbuster Façade"):** Blockbuster-blue front end to end, oversized ticket-stub canopy, floppy-and-jewel-case doorway, layered "AOL USERS ONLY" tape, 404 sign with pigeon nest, PalmPilot camera, graffiti above the door (PNG spec Sheet 1). Add Night Security Volunteer in an old vest with PalmPilot flashlight at the door (npcs.json). Windows spill CRT green and cyan; the doc asks for audible static, so show heat-shimmer and cable spaghetti, less ivy and cobble.
**Interior:** Keep all nodes: `ihm_lobby`, `ihm_modem_hall`, `ihm_geocities`, `ihm_angelfire`, `ihm_habbo`, `ihm_msn`, `ihm_imac_altar`, `ihm_vhs_shelf`, `ihm_exit`. Add a free-entry lobby desk with the Curator of the Cursed Web (museum blazer, lanyard), printer-paper Comic Sans banners, brochure stand (`ihm_exhibit_brochure`), a labelled VHS shelf by the GeoCities kiosk, and ambient visitors/school group near `ihm_msn`.
**Satire beats made visible:** (1) floppy/jewel-case doorway; (2) AOL tape; (3) Comic Sans banner; (4) pigeons on the 404; (5) velvet rope and plaque reverence on the Habbo crime scene; (6) incense altar with "DO NOT OPEN" CDs.
**Not in the file, needs approval:**
- Add a stone portico, velvet-rope queue or plaque to the exterior to sell "academic reverence"? (md names none.)
- District placement (diagram proposal Q9 is open), which fixes street context.
