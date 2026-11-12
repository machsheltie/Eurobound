# Shadow Exchange Location Package Design

## Intent and Identity

Define Shadow Exchange as Debaucheryville's hidden currency-conversion, barter, contract, and black-market service hub.

- Location ID: `debaucheryville_gilded_square_shadow_exchange_01` (renamed from the retired oldtown id by Eurobound-a06/Eurobound-7j0m)
- Slug: `shadow_exchange`
- NPC folder: `Shadow_Exchange`
- Primary source: `shadowexchange.md`

## Visual and Spatial Design

A damp Old Town alley and candle marker lead to a hinged cobblestone step and concealed stair. Below, wine-cellar vaults have been partitioned into stalls with iron lattice, scratched counter glass, UV money-check light, smoke, CRT market screens, a clacking split-flap rate board, and the illuminated Shadow Ledger. The entrance must support hidden, hinted, discovered, and permanently known states.

The spatial graph should progress from alley clue to stair threshold, exchange counter, barter window, contract desk, premium-stock cage, clue/lore node, and exit. Three-Crown Keg Haus is a nearby alley destination discovered through the Exchange network, not a room in the cellar.

## Gameplay, Quests, and State

Once discovered, the Exchange remains accessible. It accepts multiple currencies and barter items, exposes variable rates, offers shady contracts, tracks notoriety or risk, and unlocks premium stock after the documented boss condition. Its ledger grants collection item `item_vip_wristband_png` and sets `vip_wristband_png_obtained`. The CryptoBro69's Ex aftermath may reference a scratched Pixelated Kebab Monkey image as flavor but cannot award a second NFT. Brewery-tour referral and the relevant `nothingisgettingthrough` state remain dialogue references.

The package must distinguish reversible transactions from contracts with delayed consequences. Rate-board display changes, premium-stock state, vendor availability, and notoriety reactions need stable flags.

## Package Directives

Items must classify currencies, barter goods, stock, documents, and quest-owned clues. Interactions must make conversion math and confirmation readable while preserving the location's satire. NPCs cover the documented vendor cast and ambient brokers. Environment defines cold stair air, ticker rhythm, smoke and UV overlays with reduced-effects variants. PNG and mapping cover the alley clue, moving stone, stair, cellar faces, stall kits, rate-board states, counters, ledgers, currencies, vendors, and UI.

## Validation

- Discovery and permanent-access states agree across core, nodes, and interactions.
- Currency rates and barter values have one authoritative representation.
- Premium stock has an explicit external unlock condition.
- NFT, couchsurf, brewery, and infection-related quest content remains referenced.
- Three-Crown Keg Haus is an outbound connection, not duplicated interior space.
