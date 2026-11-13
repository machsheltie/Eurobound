# Audit: The Cirque du Shady (cirque_du_shady), full 8-file review

## Files read (D = design/worlds/debaucheryville/)
- D cirque_du_shady.md (main, whole)
- core/cirque_du_shady_core.json
- environment/cirque_du_shady_environment.json
- interactions/cirque_du_shady_interactions.json
- items/cirque_du_shady_items.json
- location_nodes/cirque_du_shady_location_nodes.json
- npcs/Cirque_du_Shady/ : cirque_du_shady_npcs.json, crypto_clown.md, hamstradamus.md, npc_blanka.md, npc_vance_vallaro.md, suspicious_twins_polina_paulina.md (JSON whole; the five profiles read for appearance, station and sprite notes)
- PNG_Assets/Cirque_du_Shady_Complete_PNG_Asset_Requirements.md
- sprite_mapping/cirque_du_shady_sprite_mapping.json (interior plate "not_built_yet")
- events/: no match. MISSING: none of the 8 subfolders; events/ has no file.
- Reviews: cirque_du_shady_ext_review.jpg, cirque_du_shady_int_review.jpg

## Q1, how well does it represent the location? Score: 3/5 (was 4)
Exterior is faithful on signage (EST. scratched out, bathroom addendum, corkboard, "RINGMASTER - BY APPOINTMENT", ICQ CRT flap glowing blue at night, rust-ringed pole). But core.json names nine zones and a vertically integrated grift; the exterior shows only gate, tent and booth. Missing: game_alley rig, prophecy_tent seam glow, meat cart, shady_productions_office, Bubbles hay. The interior is a handsome empty ring with a target board: no zone from location_nodes appears. It reads respectable-vintage circus, not Debaucheryville.

## Q2, how well does it lean into the requirements? Score: 3/5 (unchanged)
Palette in core.json: #B22222 and #F5F0DC dominate (correct). #FF6EC7 marquee is present but thin; #C0C0C8 vape is one puff; #6A0DAD/#D4AF37 prophecy glow absent; ICQ CRT is cyan, core.json says #39FF14. Environment json requires string bulbs #FFC966 over game_alley, fax paper flutter, rust ring storytelling: only bulbs and rust ring are painted. The interior ignores environmental_storytelling entirely.

## Verdict: REDO (interior hard redo; exterior second pass)

## Redo plan
- **Hook:** a circus that has not traveled since 1997 and is a full-stack scam plus reality-TV recruiter (core.json satirical_design).
- **Palette:** #B22222 / #F5F0DC base; #FF6EC7 marquee; #C0C0C8 vape; #6A0DAD with #D4AF37 seam pulse; #39FF14 ICQ CRT; #FFC966 alley bulbs.
- **Exterior:** add concrete-weighted game_alley (milk bottles, ring toss, coin pusher tilted three degrees), prophecy_tent seams bleeding purple-gold, overflowing vape bank from Vance's flap, trampled grass to sawdust ground, ticket dispenser jammed (interactions.json), meat cart beside Vance's tent.
- **Interior:** two plates per sprite_mapping. Hero: shady_productions_office behind the canvas wall: folding card table, chair with missing wheel, fax machine with the Season 22 sign, drifts of identical flyers, 2003 shrink-wrapped pallet at the flap edge. Second: performance_circle with mismatched folding chairs, Blanka's scarred target board (human outline with a clean void), Bubbles hay glimpse, ICQ backroom CRT corner.
- **Satire beats made visible:** "(THIS INCLUDES THE BATHROOM.)"; flyer "WANTED: ATHLETIC-INTELLECTUAL HYBRID. CARGO SHORTS PREFERRED."; 2003 pallet; Season 22 sign; Bubbles missing-elephant poster; rust rings where wheels were.
- **Not in the file, needs approval:**
  - Hero interior plate: big-top ring or production office? (the json lists the office as a zone, no "interior" is named)
  - Interior CRT color: cyan as painted, or #39FF14 per environment json?
