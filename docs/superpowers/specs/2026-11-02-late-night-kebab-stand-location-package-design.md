# Late-Night Kebab Stand Location Package Design

## Intent and Identity

Define the Late-Night Kebab Stand as Velvet Alley's post-party food vendor, status-treatment hub, and street-side gateway to the Grease Trap Shrine.

- Location ID: `debaucheryville_velvet_alley_kebab_01`
- Slug: `late_night_kebab_stand`
- NPC folder: `Late_Night_Kebab_Stand`
- Primary source: `Late-Night Kebab Stand.md`

## Visual and Spatial Design

Near the Velvet Curtain Club alley exit, blinding cart fluorescents expose a rusty open-air rotisserie, faux-Arabic `MR. CHADZ KEBABS` sign, zip-tied LEDs, chain-link fence, NFT graffiti, steam, cigarette smoke, grease-rainbow gutter, scattered cans and wrappers, and Mr. Chadz's burner phone. The service footprint is approach, menu/sign, rotisserie counter, condiment/consumption point, alley seating or standing node, Grease Trap clue/crawlspace approach, and street exits.

The stand owns the exterior trail and crawlspace transition to the Public Restroom. Discovering the cue sets `grease_trap_shrine_crawlspace_discovered`; from 03:00 through 03:59, `grease_trap_shrine_access_window_open` makes the glowing chili-sauce route traversable and it closes at 04:00. The restroom owns everything beyond the crawlspace threshold.

## Gameplay, Quests, and State

The stand is available 24/7, busiest from 22:00-06:00. It sells the documented menu for Kebab Coins and exposes additional choices when Drunk, Hungover, or Embarrassed. Purchases participate in the Great Döner Debate and status-effect economy. A qualifying kebab consumed during the restroom graffiti interaction can unlock `Stomach of Steel`; the stand exports the item/consumption state while the restroom owns the unlock interaction.

## Package Directives

Items define the complete menu, Kebab Coin costs, healing, hazards, and qualifying tags. Interactions own ordering, payment, consumption, status-aware options, Chadz's phone/business reactions, restroom clue, and district exits. NPCs center Mr. Chadz with customers and alley ambience. PNG and mapping reconcile older stand assets into cart, rotisserie, sign, food, steam/smoke, vendor, customers, UI, alley dressing, and crawlspace exterior states.

## Validation

- Menu names, prices, effects, and qualifying kebab tags agree across files.
- The stand owns the crawlspace exterior but not the restroom interior.
- The 03:00 cue is synchronized with the restroom gate.
- Status-aware menu logic does not duplicate status application.
- Reduced-smoke and low-glare states remain readable.
