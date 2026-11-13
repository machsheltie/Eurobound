# Audit: VIP Stall (velvet_curtain_club_vip_stall)

Standard: "I don't want respectable Prague. I want Debaucheryville." MA game; no nudity.

## Files read (all under `design/worlds/debaucheryville/`)
1. Main md: `velvetcurtainclubvipstall.md`
2. `core/velvet_curtain_club_vip_stall_core.json`
3. `environment/velvet_curtain_club_vip_stall_environment.json`
4. `interactions/velvet_curtain_club_vip_stall_interactions.json`
5. `items/velvet_curtain_club_vip_stall_items.json`
6. `location_nodes/velvet_curtain_club_vip_stall_location_nodes.json`
7. `npcs/Velvet_Curtain_Club_VIP_Stall/velvet_curtain_club_vip_stall_npcs.json` (no named NPCs; ambient only)
8. `PNG_Assets/Velvet_Curtain_Club_VIP_Stall_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/velvet_curtain_club_vip_stall_sprite_mapping.json`
- `events/`: no match (MISSING). Related: `velvet_curtain_club.md`, core/items of the parent club.
- Reviews: `dev/asset_team/reviews/velvet_curtain_club_vip_stall_ext_review.jpg`, `_int_review.jpg`.

## Scores
**Q1, represents the location: 4/5.** Interior hits the nodes: `vcs_fixture` (stained black-velvet seat, chipped champagne holder with bottle), `vcs_selfie_mirror` (pink overhead mirror), `vcs_graffiti` ("ROI = Regret On Investment", "I BLEW IT... literally", "Buy Low, Cry High"), `vcs_qr_graffiti` (QR code on the floor), champagne-flute chandelier, RGB edge strips. Exterior has the STAFF ONLY curtain, glitter and wristband trail, rope (md Exterior Description). Missing: the "generously sponsored by Tech Bros Who Can't Hold Their Liquor" plaque (md Signage; core.json subtitle), the two buffed bouncers (md Entrance; PNG Sheet 3), the "DO NOT LOOK AT THE BABY" clue (interactions.json `vcs_read_clue`, location_nodes `vcs_graffiti`), the "Scan for Velvet DAO Invite (Not a Scam, Probably)" text, and the CryptoQueen filter text.

**Q2, design requirements: 3/5.** Palette: interior meets gold #FFD700, black velvet #1C1C1C and RGB shimmer. But core.json asks for "cracked tile grey" and the doc wants a toilet "performing luxury through stains": the gold toilet, brass sink and polished harlequin floor read as real luxury, not glitter Mod Podge fakery. The exterior is genuinely opulent damask, tassels and brass, with red dominant, a handsome lounge entrance rather than a scam bathroom. Wall graffiti is tidy handwriting. Bass-synced RGB flicker is not visible.

**Verdict: REDO exterior; patch interior.**

## Redo plan
**Hook:** A toilet stall sold as a VIP lounge, sponsored by tech bros who cannot hold their liquor; "Smells like ROI in here."
**Palette:** #FFD700 as flaking gold paint, #1C1C1C velvet, #F7E7CE champagne, cracked-tile grey, RGB shimmer (core.json).
**Exterior (`vcs_inside_curtain` approach, md Approach):** Cheap shiny STAFF ONLY curtain, "STAFF ONLY" in cracked embroidery, frayed hem. Large faux-brass plaque, full sponsor text. Trail of glitter, lip gloss and expired wristbands. Two buffed bouncers flanking (silhouette only if sprites are separate). RGB flicker round the frame; muffled bass pulse in the curtain.
**Interior:** Keep fixture, mirror, QR floor, chandelier. Add: cracked grey tile under glitter, flaking gold on the toilet, sponsor plaque, scribbled @ handles and altcoin schemes, "DO NOT LOOK AT THE BABY" legible on the wall, CryptoQueen filter text on the mirror, "Moët 2003: Spite Reserve" label on the bottle (items.json).
**Satire beats made visible:** (1) sponsorship plaque; (2) "I BLEW IT... literally"; (3) bottle label; (4) velvet DAO invite QR; (5) bouncers guarding a toilet; (6) Mod Podge glitter marble.
**Not in the file, needs approval:**
- May bouncer props (oversized jackets, earpieces) stand in for the guards in the plate?
- What does the "baby" in the clue look like? The file gives only the sentence.
