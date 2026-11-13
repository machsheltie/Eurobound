# Audit: Shadow Exchange (shadow_exchange), full 8-file review

## Files read
- design/worlds/debaucheryville/shadowexchange.md (whole)
- core/shadow_exchange_core.json
- environment/shadow_exchange_environment.json
- interactions/shadow_exchange_interactions.json
- items/shadow_exchange_items.json
- location_nodes/shadow_exchange_location_nodes.json
- npcs/Shadow_Exchange/shadow_exchange_npcs.json, plus npc_mrs_rata.md, npc_uv_man.md, npc_token_goblin.md, cryptobro69s_ex.md (all four read)
- PNG_Assets/Shadow_Exchange_Complete_PNG_Asset_Requirements.md (6-colour palette, props, node list)
- sprite_mapping/shadow_exchange_sprite_mapping.json (asset ids and node bindings)
- events/: no match (MISSING). All 8 subfolder files exist.
- Plates: dev/asset_team/reviews/shadow_exchange_ext_review.jpg, shadow_exchange_int_review.jpg

## Q1, how well does it represent the location? 4/5 (held)
Exterior matches location_nodes se_alley_marker and se_hidden_stair closely: wet alley, hinged cobblestone hatch, tealights, butts, the crooked "SHAEDOW EXCHAENGE, Best Rates If You Don't Ask" sign. Interior delivers the arches, lattice, split-flap board, glass counters, CRT wall, amber lamp, UV glow, handbags. Missing named nodes: no visible Premium Stock Cage (se_premium_cage), no duct-taped Shadow Ledger on the Contract Desk, no cash-only candle marker as a distinct object, no "photocopied currencies pinned behind glass" (environment.json), and no stations for the three NPC md files (UV detection station one arch from the counter, Token Goblin's corner stall).

## Q2, how well does it lean into the design requirements? 3/5 (held)
Environment.json asks for "rates change faster than the player can read", "contract corrections in red pencil" and "premium cage padlocks outnumber valuable objects". None are on the walls. Palette: UV violet is faint outside and in two small glows inside, #FFD700 and #DC143C read only as lamp amber, and the board arrows are tiny. Both plates are a tasteful moody dungeon shop: tidy floors, empty counters, no clerks' mess. The doc wants "officially unofficial" post-Soviet flea market. Respectable.

## Verdict: REDO, both (light, additive; unchanged)
Bones and layout are right; keep the hatch, arches and board. Add the missing nodes and the comedy layer.

## Redo plan
- **Hook:** "Best Rates If You Don't Ask": old bank vault run as a post-Soviet flea market (md l.3), copper, old wine, toner smell (md l.33), a counterfeit Bloomberg terminal in a cellar.
- **Palette:** md/PNG md: #708090 stone, #9400D3 UV, #1C1C1C shadow, #FFD700 gold, #00FF00 CRT, #DC143C red. core.json adds "desk-lamp amber" and "copper" and drops black and gold (see conflicts).
- **Exterior:** keep hatch, tealights, sign. Add the cash-only candle marker as its own lit prop on the alley wall, a crooked-bolt sign, stacked stickers, more butts and puddles, rain drip at the stair lip (environment.json), a UV graffiti arrow.
- **Interior:** keep room; place all six interior nodes. Exchange Counter: scratched glass, several calculators, photocopied currencies pinned behind glass, board with large red and green ticks. Barter Window: iron lattice, scarves, ledger pencil, key ring. Contract Desk: single lamp, duct-taped Shadow Ledger, red-pencil corrections. Premium Stock Cage: padlocks outnumbering objects, locked. UV station and Token Goblin corner stall as props only. Cellar Exit stair.
- **Satire beats made visible:** several calculators per clerk (md l.59); receipts from three businesses with mismatched logos (md l.46); handbags with deactivated tags; WEDNESDAY wristbands in a stack (md l.117); "Depends how loudly you asked" sign (md l.121, Mrs. Rata's "Cash speaks. Whining does not.").
- **Conflicts, approval needed:** (1) NPC roster: npcs.json names The Exchange Broker, Barter Clerk, Contract Fixer; the md files give Mrs. Rata (main counter), The UV Man (barter window operator) and Token Goblin (corner stall). Same people or different? (2) CryptoBro69's Ex stands at the main counter in her md but at the premium cage in npcs.json. (3) Palette lists differ as above. (4) Cage opens on "documented post-boss state" (nodes.json) vs Count Velvet Absinthe defeat (md l.25); confirm the same.
- **Not in the file, needs approval:** wording of any hand-painted rule sign at the counter; whether the locked cage shows behind the counter before the boss.
