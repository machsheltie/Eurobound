# Battle HUD art: plan (asset team, for author approval)

Bead: Eurobound-du51. Status: plan only. Nothing is made until the author approves it on the Eurobound Desk (cards `asset-team-plan-battle_hud-q1` and `-q2`).

## What the battle screen needs

The battle screen already shows these slots. Today each one is a text box. The art drops in by file name, with no code change.

| Art | File | Drawn at | Count |
|---|---|---|---|
| Status icons | `game/assets/ui/status_icons/<status id>.png` | 28 x 28 px | 22 |
| Turn-order portraits | `game/assets/ui/battle/portraits/<unit id>.png` | 132 x 56 px box | 3 bros + 13 Arcade villains |
| Action-type icons (attack, item, skill, debuff) | not read by code yet | overlay on a portrait | 4 |

The 22 status ids are:
- sugar_rush_hour, gush_locked, crash, cottonmouth, the_shakes, wobbly_windmill_navigation
- contact_high, space_cake_timer, space_cake_gamble, canal_confusion, tunnel_confusion, tunnel_vision
- embarrassed, sloppy, confused, stun, grease_fingers, tourist_trap_victim
- food_poisoning, broke_af, hardcore_gamer, gains_bro

## What canon already says

- **GDD 303:** action-type icons overlay the turn-order portraits.
- **GDD 308:** status icons are animated. The GDD gives three examples:
  - Hungover: a beer mug that sloshes.
  - Grease Fingers: an oil drip.
  - Embarrassed: a blush that pulses.
- **GDD 309:** borders are colour-coded, green or blue for buffs and red or orange for debuffs.
- **Standing rules:** all icons are 3D-made (author, 2026-11-13: "anything currently done as pixel art of any sort needs redone as 3d"). Every asset passes a blind reviewer gate (gate U for UI, `dev/qc/QC_COVERAGE.md`).
- **Gaps:** no doc gives a picture for the other 19 status icons, or for the action-type icons. Those motifs are content, so they need the author (card q2).

## Proposed approach (card q1)

1. **One simple 3D object per status.** Each object is the status's joke made physical. All use the approved item-icon look B: Tripo website, then a headless Blender toon render.
2. **A round badge behind each object,** with the GDD's colour-coded border: green or blue for buffs, red or orange for debuffs. The border carries the buff or debuff meaning at 28 px, where the object alone may not read.
3. **Rendered at 256 px, then downscaled to 28 px.** Each icon passes a readability check at 28 px before blind review.
4. **Animation is a second pass,** after the still icons are approved: 4 to 6 Blender frames per icon (the slosh, the drip, the pulse). The battle screen's loader would need a small code change for frames. That goes in a separate bead.
5. **Action-type icons use the same badge,** each with a simple object: attack, item, skill, debuff.
6. **The Sprite Development Team owns the portraits.** They own all character art. They render the bros and villains from their 3D models into the 132 x 56 box. The asset team only checks that the portraits fit the strip.

## Cost and order

- **Credits:** about 90 Tripo credits per new object, so about 26 objects (22 status plus 4 action) at about 2,340 credits. Several statuses could reuse an existing icon's model (the stein, the corndog), which costs 0 credits.
- **Order:**
  1. Grease Fingers and Embarrassed come first, as a look trial. They are the two GDD examples on the needed list; Hungover is not on it.
  2. The rest follow in batches of four.
  3. Animation comes last.
