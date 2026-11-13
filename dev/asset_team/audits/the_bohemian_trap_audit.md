# Audit: The Bohemian Trap (debaucheryville)

## Files read
1. Main: design/worlds/debaucheryville/the_bohemian_trap.md (whole)
2. core/: design/worlds/debaucheryville/core/bohemian_trap_core.json (tagline "Authentic Absinthe, Recently Antiqued")
3. environment/: design/worlds/debaucheryville/environment/bohemian_trap_environment.json
4. interactions/: design/worlds/debaucheryville/interactions/bohemian_trap_interactions.json
5. items/: design/worlds/debaucheryville/items/bohemian_trap_items.json
6. location_nodes/: design/worlds/debaucheryville/location_nodes/bohemian_trap_location_nodes.json
7. npcs/: design/worlds/debaucheryville/npcs/The_Bohemian_Trap/npc_emil_green_fairy.md and bohemian_trap_npcs.json
8. PNG_Assets/: design/worlds/debaucheryville/PNG_Assets/Bohemian_Trap_Complete_PNG_Asset_Requirements.md
9. sprite_mapping/: design/worlds/debaucheryville/sprite_mapping/bohemian_trap_sprite_mapping.json
- events/: MISSING (no match). Brewery-tour items: none. Greps of design/items, Quests, World Design: no hits.
- Image: dev/asset_team/reviews/the_bohemian_trap_ext_review.jpg (no interior; a cart needs none; interior plate listed "not built yet" in the spec).

## Q1. How well does it represent the location? 3/5
The cart is on-model: green-and-gold, backlit bottle array, two fountains, "See the Green Fairy Tonight", the "Traditional Recipe Since 1997" board, the 70% ABV tag, green underglow and ground fog (doc lines 29-41). But the doc's core joke is a 2015 cart "deliberately antique... aged artificially" (l.30) in a district that is "completely anachronistic" (l.31). The plate paints a genuinely lovely, authentic-looking antique cart. No visible fakery: no price tags climbing with "authenticity" (l.47), no educational posters (l.56-60), no Emil, no sugar-cube spoon theater at readable scale. The setting is a rain-slick cobbled lane with ivy, roses and gas lamps: the Arcade's neon quarter is missing entirely.

## Q2. How well does it lean into the design requirements? 2/5
Palette: doc wants Absinthe Green #7FFF00 dominant, Antique Gold #CFB53B accent, Night Black #1A1A1A ground. Painted green is a dark emerald and #7FFF00 appears only in the underglow strip and bottles; the frame is dominated by warm amber windows, brown stone and pink roses. Satire: this is exactly "fake Prague, let's Prague it up" (Brief s.2). It reads as a charming heritage vendor, a respectable one. Nothing is scandalous, seedy or absurd.

The sub-folder files confirm it: core.json's tagline is "Authentic Absinthe, Recently Antiqued" and its contrast line is "a 2015 cart artificially aged"; the spec adds "suspiciously modern shoes" on the performer and a flame-theater ritual. None of the "recently" shows in the plate.

## Verdict: REDO (exterior)
Both scores are under 4 and it is not over the top. Interior: none needed.

## Redo plan
- **Hook**: A 2015 flat-pack "antique" cart selling 3 SOVS of booze for 25 SOVS with theater (l.77, l.446).
- **Palette**: #7FFF00 floods the frame (tube neon, bottles, fountains, fog); #CFB53B on obviously sprayed trim; #1A1A1A street and cart body; #A9A9A9 fog.
- **Exterior**: Cart in a black neon street, not a heritage lane. Gold paint chipping to bare MDF and a visible "AGED 2015" workshop stamp or fresh screws; tube-neon Art Nouveau sign fastened on with zip ties; fog machine and dry ice bucket in plain sight; oversized fountains.
- **Interior**: None (cart).
- **Satire beats made visible**: price tags rising with "authenticity", House Special most marked up (l.45-47); "Since... 1997" and tiny 70% warning (l.38-39); posters of Van Gogh, Hemingway, Toulouse-Lautrec (l.56-60); Believer and Skeptic stand-ins as sprites later (l.249-261); ring light on a tripod (l.263).
- **Not in the file, needs approval**: Is Emil's costume rack and "mail-order catalogue" box visible on the cart? Do we paint the Arcade's neon neighbours, or keep the street plain?
