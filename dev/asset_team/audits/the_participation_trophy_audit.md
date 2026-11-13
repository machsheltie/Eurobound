# Audit: The Participation Trophy (the_participation_trophy)

## Files read (full 8-file set, 2026-11-12)
All under design/worlds/debaucheryville/:
1. the_participation_trophy.md (main md, whole)
2. core/participation_trophy_core.json
3. environment/participation_trophy_environment.json
4. interactions/participation_trophy_interactions.json
5. items/participation_trophy_items.json
6. location_nodes/participation_trophy_location_nodes.json
7. npcs/Participation_Trophy/participation_trophy_npcs.json (only file in folder)
8. PNG_Assets/Participation_Trophy_Complete_PNG_Asset_Requirements.md
9. sprite_mapping/participation_trophy_sprite_mapping.json (one asset, status "built")
- events/: no match. Nothing MISSING among the eight.
- Also grepped: cirque_du_shady.md (neighbours), Cirque_du_Shady npc_vance_vallaro.md.
- Review re-viewed: the_participation_trophy_ext_review.jpg (exterior only; no interior plate exists).

## Q1, how well does it represent the location? 4 / 5
- Signage matches the md word for word: main letters, "EVERYONE'S A WINNER!" banner, "REDEEM YOUR TICKETS HERE", "No Hope." sign, handwritten "Yes, these are the GOOD prizes".
- Prize wall tiers read: belt, golden hamster, trophies up top; sword and cane in the middle; plush, balloon dog, glitter hat below; cages of junk on the floor (core.json nodes pt_grand_shelf to pt_floor_junk).
- Missing: "Smile! You 'Won'!" counter sign, any sign of Yolanda, half-smoked cigars, ticket strips, grime. The md wants "deliberately underwhelming" and "childhood disappointment, concentrated". This booth is lush, warmly lit and photogenic.

## Q2, how well does it lean into the design requirements? 3 / 5 (was 4)
- Palette: md and PNG spec say #CD5C5C red, #F0E68C yellow, #D2B48C canvas, #9370DB purple (+ #E8A33D ticket orange). Painted red/cream stripes carry it; purple is only a sword, belt and plush ribbon. core.json lists a different palette (see questions).
- Satire is present but gentle. Under the standard "I don't want respectable... seediness, over the top", this is a charming vintage carnival stall, not a scam booth. The harsh, "unflattering for prizes AND customers" lighting (md technical specs) is absent; the night plate is cozy string lights.
- The files make it a place of grime and smell ("the source of the smell"); the plate has none.

## Verdict: REDO (light, exterior day/night only). Overturns KEEP.
The layout, text and prop set are right and stay. Re-light and de-charm.

## Redo plan
**Hook:** Everyone wins; the proof is garbage.
**Palette:** keep red/cream; push #F0E68C to harsh sodium-yellow light, add #9370DB shadows and purple tier tags, #E8A33D ticket strips underfoot.
**Exterior:** same booth; harsh flat bulb light, no cozy glow; grime streaks, ticket litter, cigar butts at the counter, flies in the lamp, "Smile! You 'Won'!" sign on the counter.
**Interior (nodes only, no plate yet):** counter with ticket counter, back "Warehouse of Sadness" boxes labelled by disappointment tier.
**Satire beats made visible:** Grand-prize shelf dusty "since 2003"; price tags absurdly high; floor-level "Participation Prizes" bin; one visibly half-smoked cigar.
**Not in the file, needs approval (md vs JSON conflicts):**
- Palette: core + environment JSON say faded carnival red, sad plush brown, ticket blue, peeling cream; md/PNG spec say the hex set above. Which governs?
- Subtitle: md "You Tried! Here's Proof!" vs core "Everyone's a Winner, Spiritually False".
- Items: md catalogue (Half-Smoked Cigar, Kazoo, Corndog, etc.) vs items.json (Slightly Damp Consolation Plush, Plastic Participation Medal, Mysterious Carnival Trinket, Impossible Grand Prize, Participation Bag). Which set gets icons?
- Currency: items.json says "Kebab Coins"; project rule is SOVS only.
- Yolanda: md has surname Kovarik and four named circus NPCs (Ludvík, Recent Winner, Proud Idiot, Hamstradamus); npcs.json has only Yolanda plus "circling children". Which crowd is shown?
