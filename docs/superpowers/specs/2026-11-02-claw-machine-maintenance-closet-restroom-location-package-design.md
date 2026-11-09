# Claw Machine Maintenance Closet Restroom Location Package Design

## Intent and Identity

Define the hidden arcade restroom as an independently owned micro-location reached through Absinthe Arcade's broken DDR unlock.

- Location ID: `debaucheryville_arcade_maintenance_closet_01`
- Slug: `claw_machine_maintenance_closet_restroom`
- NPC folder: `Claw_Machine_Maintenance_Closet_Restroom`
- Primary source: `clawmachinemaintenanceclosetrestroom.md`

## Visual and Spatial Design

Absinthe Arcade owns the broken DDR machine, three-token interaction, maintenance-door exterior, and transition. This package begins at the inside threshold. The room is barely larger than a mop closet, lit by a flickering green arcade marquee, with a claw arm chandelier, DDR-pad toilet seat, janitor-bucket foot soak, CRT `INSERT COIN` mirror, dense graffiti, cleaning clutter, and awkward body-turning clearance.

The graph is intentionally tiny: threshold, fixture/DDR seat, CRT mirror, graffiti wall, bucket/claw prop zone, and return door. Camera framing must keep all primary interactions readable without pretending the closet has extra rooms.

## Gameplay, Quests, and State

The prerequisite is the permanent Arcade-side flag `arcade_maintenance_restroom_unlocked`, set after spending exactly three Arcade tokens. Inside, the location owns graffiti reading, bathroom interactions, documented Embarrassed/status consequences, audio gags, Rival Trio ICQ bindings, and cross-city bathroom-network progression. It must not charge the unlock cost again.

## Package Directives

Items cover only objects actually found or consumed inside; Arcade tokens remain externally owned. Interactions bind the existing unlock flag, not a duplicate. NPCs should remain empty or ambient-only unless the source explicitly places a speedrunner or quest character at a scheduled node. Environment needs reduced-flicker treatment. PNG and mapping cover inside door, closet faces, fixtures, graffiti states, CRT mirror content, claw/DDR props, status UI, and small FX.

## Validation

- The three-token cost exists only on the Arcade-side unlock.
- Permanent access uses the exact flag exported by Absinthe Arcade.
- No Arcade hall assets or Taproom content enter this package.
- Graffiti and bathroom-network progression use stable IDs.
- Reduced-flicker art and behavior exist.
