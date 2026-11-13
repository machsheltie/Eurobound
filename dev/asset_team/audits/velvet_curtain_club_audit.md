# Audit: Velvet Curtain Club (debaucheryville)

Standard: "I don't want respectable Prague. I want Debaucheryville." MA game; club and sex-work content in bounds, no nudity.

## Files read (all under `design/worlds/debaucheryville/`)
1. Main md: `velvet_curtain_club.md`
2. `core/velvet_curtain_club_core.json`
3. `environment/velvet_curtain_club_environment.json`
4. `interactions/velvet_curtain_club_interactions.json`
5. `items/velvet_curtain_club_items.json`
6. `location_nodes/velvet_curtain_club_location_nodes.json`
7. `npcs/Velvet_Curtain_Club/`: `velvet_curtain_club_npcs.json`, `npc_velvet_curtain_bouncer.md`, `npc_second_bouncer.md`, `vape_witch_vanessa.md`, `vlad_the_validator.md`
8. `PNG_Assets/Velvet_Curtain_Club_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/velvet_curtain_club_sprite_mapping.json`
- `events/`: no match (MISSING). Reviews: `dev/asset_team/reviews/velvet_curtain_club_ext_review.jpg`, `_int_review.jpg`.

## Scores
**Q1, represents the location: 4/5.** The current plates are better than the last audit said. Exterior: graffiti-slathered lane, opera-ruins billboard, gold plaque with the tagline, heavy red velvet curtain with tassels and rope, neon tubes, graffiti dumpster (md Exterior Description). Interior: burgundy booths with LED underglow and QR menus, brass poles with coats, broken-throne DJ dais, "The Real Party's in Your Head" neon, STAFF ONLY curtain, cracked mirror wall, LED-tip plants, crystal chandelier. Missing: Kamil and Marek at the rope (npcs.json, `vcc_bouncer_gate`), `vcc_bar` drink service, Vlad's backroom door, vape clouds, the children's-party window gag.

**Q2, design requirements: 3/5.** Palette hits burgundy and gold but #4B0082 purple is thin and the floor is a refined harlequin marble. The card is "Studio 54 meets Eastern Bloc goth gone to seed" and "cheap gold" (core.json palette); the plates read as an expensive, tasteful venue. The vape-pen chandelier is plain crystal, there is no crowd, no stage clutter, nothing grubby or scammy. The curtain does not pulse.

**Verdict: REDO (targeted).** Keep the alley framing and the layout; make both plates seedier and populated.

## Redo plan
**Hook:** Fraudulent exclusivity: a free club selling "VIP" to tourists, in a ruined opera house (core.json atmosphere).
**Palette:** #800020 burgundy dominant, #4B0082 on floor and shadows, #FFD700 as cheap tarnished gold, neon #FF1493/#00FFFF/#00BFFF, ground #696969/#1a1a1a (md Technical Specifications).
**Exterior (`vcc_alley`, `vcc_bouncer_gate`):** Add Kamil (cybernetic eye, black coat) and Marek (buff, velvet-rope gloves) at the rope. Curtain bulging with bass, sagging gold fringe, scuffed. Add a kids'-party window with "I'm 7!" wristbands visible (md Wristband Running Gag). Keep graffiti mural and billboard; add wet neon reflections (environment.json).
**Interior:** Vape-pen chandelier with visible crushed pens (md; PNG Sheet 1). Add `vcc_bar` with Vape Witch Vanessa (crystals, peach-mango vape cloud) at the booths; Vlad (too-tight crypto tee) at the rear VIP Backroom door; DJ Sound Alchemist on the dais; patrons: age-denial crew, NFT crop-top wearer, opera-cloak thrift shopper. Fog thicker, glitter trail to STAFF ONLY, vape clouds, scuffed sticky floor under tarnished gold.
**Satire beats made visible:** (1) "Vibes Only. No Shoes? No Dignity? You're In." plaque over a free door; (2) bouncers smirking at the wristbands; (3) vape-pen chandelier; (4) pole coat racks; (5) neon aphorism; (6) QR cocktail menus; (7) Vlad's blockchain "VIP list".
**Not in the file, needs approval:**
- Any visual for the Influencer Blood Ritual or a livestream rig on the floor?
- Pole-dancer silhouettes (no nudity)? The md names poles only as coat racks.
