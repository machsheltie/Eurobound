# Audit: Backroom Concessions (backroom_concessions)

## Files read
- design/worlds/debaucheryville/backroomconcessions.md (whole)
- design/worlds/debaucheryville/PNG_Assets/Backroom_Concessions_Complete_PNG_Asset_Requirements.md (palette, roles, mood)
- dev/asset_team/reviews/backroom_concessions_ext_review.jpg, backroom_concessions_int_review.jpg
- Grep of the name across design/: only the above plus debaucheryville.md and _art_build_audit.md (no npc/quest visuals)

## Q1, how well does it represent the location? 3 / 5
- Painted correctly: concealed door, "404: Calories Not Found" neon (doc l.25, l.36) backlit by a hacked server rack (l.37), CRT row, "Hot Pockets + Protocols" menu (l.46), mismatched chairs, steaming fry station.
- Missing or wrong: doc l.42 wants a cramped booth "wedged between two gutted vending machines" with one "stuffed with thermal paste containers" (l.47) and one "flickering with mysterious inner knowledge" (l.48). The plate shows two ordinary drink machines, no thermal paste anywhere. CRTs show a generic desktop, not the "endless pop-up ads" (l.45). No hacked electronics as lamps, no LAN badges, no visible grease or health-code rot. It reads as a tidy gamer den with a snack counter, not "mystery meat, ozone and illicit mining".

## Q2, how well does it lean into the design requirements? 3 / 5
- Palette is Neon Green #00FF41 primary, Warning Orange #FF8C00 accent, Server Black #1C1C1C ground. Painted: the green is limited to the sign and one machine, and the beige/olive plaster and brown checkerboard (never in the doc) dominate both plates. The exterior is mostly mustard wall.
- Satire: "health-code violations as underground authenticity" is not visible. Nothing is gross, nothing is absurd (no thermal paste sundae, no CryptoDöner box, no pop-up avalanche). Handsome, moody, respectable.
- The checkerboard floor duplicates the house look the brief warns against.

## Verdict: REDO (both)
Exterior: right idea, wrong colour balance. Interior: misses the doc's own jokes.

## Redo plan
**Hook:** Hacker mystique as a deep-fryer; a food court in a server closet (l.3, l.67).
**Palette:** #1C1C1C walls and floor ground; #00FF41 dominates light (sign, CRT glow, machine, spill on floor); #FF8C00 on warning lamps, fryer glow and rack LEDs; supporting #E8E8D0, #C0C0C0, #8B4513 from the PNG spec.
**Exterior:** near-black corridor wall, door ajar, sign huge and glitching, rack cables strung like intestines, grease-slick floor, nothing beige.
**Interior:** booth wedged between two gutted machines (l.42): left one packed with thermal paste tubs, right one glowing "inner knowledge"; CRTs on a pop-up error cascade; laminated menu peeling; chairs mismatched; ozone shimmer. Floor: stained concrete or sticky lino, not checkerboard.
**Satire beats made visible:** thermal paste machine as "industrial art" (l.54); pop-up infected CRTs as dining atmosphere (l.90); fryer sitting beside mining rigs (l.55); the "Hot Pockets + Protocols" menu (l.46).
**Not in the file, needs approval:**
- Which exact pop-up ad text may appear on the CRTs?
- Is Donny.exe's lanyard shown as a prop with no person present?
