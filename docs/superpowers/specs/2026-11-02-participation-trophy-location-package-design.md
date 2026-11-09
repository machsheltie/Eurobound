# The Participation Trophy Location Package Design

## Intent and Identity

Define The Participation Trophy as Cirque du Shady's ticket-redemption booth and intentionally disappointing prize economy.

- Location ID: `debaucheryville_circus_participation_trophy_01`
- Slug: `participation_trophy`
- NPC folder: `Participation_Trophy`
- Primary source: `the_participation_trophy.md`

## Visual and Spatial Design

A weathered, peeling carnival booth sits in deliberate contrast to the loud game stalls. Its prize wall stratifies unreachable grand prizes, difficult good prizes, ordinary consolation stock, and floor-level participation junk. The playable footprint is approach/sign, ticket counter, tiered prize wall, attendant node, direct-purchase interaction, reaction space, and circus exit.

The top shelf is visual aspiration unless the source defines a real award path. Prize tiers should be modular display layers so stock and progression can change without repainting the booth.

## Gameplay, Quests, and State

The booth opens with the circus. It redeems Circus Tickets, permits documented direct gold purchases, tracks `Frequent Loser` status, reacts to prior game performance, supports Bravado responses, and grants location-specific outcomes or achievements. It consumes shared circus-game flags without owning those games.

## Package Directives

Items define the actual obtainable prize catalog, ticket costs, direct prices, rarity, effects, and display-only status. Interactions validate stock and currency before redemption and clearly distinguish unattainable display props. NPCs define Yolanda and nearby circus ambience. PNG/mapping cover booth faces, signs, prize-tier modules, stock states, tickets, attendant, customer reactions, item icons, redemption UI, and circus-light variants.

## Validation

- Display-only grand prizes cannot be granted accidentally.
- Ticket and direct-purchase prices have one authoritative definition.
- Frequent Loser progression consumes documented game outcomes.
- Circus adjacency does not merge the booth with Mystery Meat Cart.
- Prize-wall state always matches obtainable inventory.
