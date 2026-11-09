# Threads & Treads Location Package Design

## Intent and Identity

Define Threads & Treads as the all-night equipment and identity shop for defensive clothing, style, and Cool Factor.

- Location ID: `debaucheryville_shop_threads_treads_01`
- Slug: `threads_and_treads`
- NPC folder: `Threads_And_Treads`
- Primary source: `threads_and_treads.md`

## Visual and Spatial Design

The narrow storefront uses black walls, chrome letters, leather, chains, combat boots, and industrial light. Inside, an entry gauntlet of jackets leads through footwear, accessories, armor/style hybrids, fitting mirror, proprietor counter, and a distinct 02:00 crowd presentation. The same floor plan becomes more candid and desperate between 02:00 and 05:00 through patrons, stock emphasis, and dialogue bindings.

## Gameplay, Quests, and State

The shop is open 24 hours. Equipment purchases modify defense and Cool Factor; the mirror assessment previews identity/status consequences; the 02:00 transformation discount and `Who Do You Want To Be?` choice shape repeat interactions. Appearance changes and equipment stats must remain mechanically distinct even when one purchase affects both.

## Package Directives

Items provide the authoritative catalog, prices, equipment slots, stat modifiers, appearance overlays, and discount eligibility. Interactions own compare, fitting, mirror assessment, purchase/equip, transformation choice, and Bravado responses. NPCs define Zdeněk, staff, and time-swapped customers. PNG and mapping cover storefront, modular racks, jackets, footwear, accessories, fitting mirror states, characters, equipment icons, player overlays, shop UI, and night-crowd variants.

## Validation

- Twenty-four-hour access and the 02:00-05:00 event are separate states.
- Cool Factor, defense, and cosmetic effects are not conflated.
- Discounts are applied once and shown before purchase.
- Fitted/equipped sprites map to stable item IDs.
- Customer swaps do not alter shop topology.
