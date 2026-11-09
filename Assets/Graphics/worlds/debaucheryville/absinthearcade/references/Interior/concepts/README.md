# Absinthe Arcade interior concepts

Concept drafts for the HD-2D interior (Bravely Default style, fixed tilt camera, author ruling
2026-11-02). None of these is approved yet. Canon reference: `../Neon Absinthe Arcade Bar.png`.
Content source: the main-hall and north-wing prompt briefs in
`design/World Design/Debaucheryville/PNG_Assets/Absinthe_Arcade_Complete_PNG_Asset_Requirements.md`.

| File | Made with | Notes |
|---|---|---|
| `aa_dollhouse_chatgpt_author_2026-10-30.png` | ChatGPT (author's chat "Create Dollhouse View") | Building cutaway with interior. Uses real game names and has garbled text ("DISHKL THINKING"). |
| `aa_interior_hall_v1_gpt25_iso.png` | Firefly, GPT Image 2.5 Flare, High | Isometric corner cutaway. Signs read TOKENS HERE and PRIZES correctly. |
| `aa_interior_hall_v2_gpt25_straight.png` | Firefly, GPT Image 2.5 Flare, High | Straight-on but the camera is too low; Backpack Girl missing. |
| `aa_interior_hall_v3_gpt25_gamecam.png` | Firefly, GPT Image 2.5 Flare, High | Game camera (about 40 degrees down, looking north). PRIZES sign missing. |
| `aa_interior_hall_v3b_nbpro_prizes_sign.png` | Firefly, Gemini 3 (Nano Banana Pro) 2K edit of v3 | Adds the PRIZES sign. Superseded by v5. |
| `aa_interior_hall_v3b_day_nbpro.png` | Nano Banana Pro 2K relight of v3b | Daytime state: daylight through the glass, neon subdued. Not pixel-identical to v3b (concept only). |
| `aa_interior_hero_v2_chatgpt_author.png`, `aa_interior_hero_v3_chatgpt_author_revision.png` | Author's ChatGPT chat "Revise Arcade Layout" | Content canon for the hall: DDR three-pad dance-off under one big screen, Skee-Ball, foosball, Beanie Baby claw, Bubble Bobble against a wall, fractured green-glass bar with the prize redemption counter built into its broken end, mismatched seats with exactly one bidet/toilet stool, gritty non-luxury wear. |
| `aa_interior_hall_v4_nbpro_merge.png` | Nano Banana Pro merge of v3b (camera) + ChatGPT hero (contents) | All attractions in; DDR read as one long platform; no entrance doors. |
| `aa_interior_hall_v5_ddr_prizes_bar.png` | v4 + entrance doors/spectators spliced from an NB Pro edit + DDR area redrawn by GPT Image 2.5 on a crop and pasted back | **Current main-hall concept (author picked C framing 2026-11-08).** Three separate DDR machines facing one wall screen, prize redemption in the bar, entrance doors at the bottom. |
| `aa_interior_north_wing_v1_gpt25_iso.png` | Firefly, GPT Image 2.5 Flare, High | North wing, isometric. Curtain + cracked light-gun cabinet west, dance pad + MAINTENANCE ONLY door east. |
| `aa_interior_north_wing_v2_gpt25_gamecam.png` | Firefly, GPT Image 2.5 Flare, High | North wing at the game camera. Repeats the street gate at the bottom (wrong) and is roomier than the spec. |
| `aa_interior_north_wing_v3_nbpro_no_gate.png` | Nano Banana Pro 2K edit of north v2 | Street gate removed, floor continues to the camera. Still roomier than the spec (the requested extra cabinet rows did not appear). Current north-wing concept. |

Prompt rules used for every draft: references 1 = canon interior, 2 = in-game facade texture
(`game/assets/worlds/debaucheryville/absinthe_arcade/exterior/faces/aa_face_front_day.png`);
cabinet marquees wordless and no real game names (real-brand question is open with the author);
only canon sign text (TOKENS HERE, PRIZES, MAINTENANCE ONLY). Check every word on the output.

Open author questions (decisions page, 2026-11-04): which framing; Green Fairy mural inside or
exterior-only; real brand names; Backpack Girl's hours.

- `aa_interior_hall_v6_more_cabinets.png` (2026-11-08) — **current main hall.** v5 plus 14 more upright cabinets (author: 'more video game cabinets'). Back row of 5 under the mural and 2 on the right wall (Nano Banana Pro edit, spliced in so v5's bar sign stays; the NB pass misspelled it 'RECEMPTION'). Floor island of 4 between the skee-ball lanes and the bar, plus 3 in a row by the toilet (GPT Image 2.5 crop edits, feather-pasted). Everything else unchanged from v5.
- `aa_interior_hall_v7_tycoon_layout.png` (2026-11-08): v6 floor cabinets rejected as random (author asked for a layout like Arcade Tycoon). Built from v5 + the v6 back row + right-wall pair. Adds one orderly bank in the centre: 2 rows of 4 back to back, shoulder to shoulder, parallel to the back row, with aisles on both sides (GPT Image 2.5 crop edit, feather-pasted). The scattered island and the toilet-side row are gone.
- v7 REJECTED (author): the centre bank blocks the other games and jams the floor. Rule: cabinets go in straight rows that leave real open floor, never islands that block other machines.
- `aa_interior_hall_v8_wall_rows_open_floor.png` (2026-11-08): v5 + a straight row of 5 along the back under the mural + a row along the right wall beside Bubble Bobble. The centre floor stays open.
- v8 APPROVED by the author 2026-11-09 ("all good"). It is the main-hall concept.
- `aa_interior_north_wing_v4_gpt25_wall_rows.png` (2026-11-09): GPT Image 2.5 with north v3 and hall v8 as references. Darker and lower than the hall, as the spec asks: vaulted ceiling with no mezzanine, conduit, low amber lamps, green haze. Cabinets stand only in straight wall rows (back, west, east) and the centre floor is open, following the author's v7 rule. West: a cracked light-gun cabinet pushed aside from the glowing green curtain, with a blank brass plaque. East: a broken dance machine beside the dented steel door, which has three pips and a MAINTENANCE ONLY label (spelling checked). Marquees are wordless.
- `aa_interior_hall_v8_day.png` (2026-11-09): daytime state of v8. Firefly Relight (beta) with the Sunny preset keeps every pixel, sign and word. It came out cold and killed the neon, so `tools/art_cleanup/day_grade.py` warm-grades it and screen-blends v8's emissive glow (screens, neon, green bar glass, lamps) back in at about 65%. A Nano Banana Pro prompt relight was tried first and rejected: almost no lighting change, and it garbled BUBBLE BOBBLE and TICKETS. Known gap: the stained-glass windows read dark for daytime.
