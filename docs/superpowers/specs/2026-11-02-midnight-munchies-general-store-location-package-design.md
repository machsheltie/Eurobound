# Midnight Munchies General Store Location Package Design

## Intent and Identity

Define Midnight Munchies as Hostel Row's night-only convenience store and desperation-priced recovery supplier.

- Location ID: `debaucheryville_shop_midnight_munchies_01`
- Slug: `midnight_munchies_general_store`
- NPC folder: `Midnight_Munchies_General_Store`
- Primary source: `midnight_munchies_general_store.md`

## Visual and Spatial Design

The store is a small fluorescent beacon between hostels and bars, with cluttered windows, flickering neon, visible emergency supplies, and a counter watched by Věra. Inside, compressed aisles divide recovery items, food, hygiene, emergency equipment, and the heat-lamp lottery while preserving a clear entrance-to-counter loop.

Time states cover closed daytime frontage, opening setup, ordinary late night, and the visibly harsher post-02:00 desperation period. Product density should come from reusable shelf modules and overlays rather than illegible one-off paintings.

## Gameplay, Quests, and State

The store operates 22:00-08:00. Prices rise 20 percent after 02:00. It provides recovery and preparation goods, heat-lamp gamble purchases, repeat-customer recognition, Bravado interactions, and notifications about preventable poor planning. It links economically to Hostel Midnight Checkout and may satisfy item needs in `nothingisgettingthrough`, but the quest owns its dialogue and resolution.

## Package Directives

Items must be a complete purchasable inventory with base and desperation prices, effects, stock rules, and category. Interactions must compute the surcharge once and display it before confirmation. NPCs cover Věra, staff if explicitly documented, and atmospheric customers. Environment defines refrigeration hum, fluorescent buzz, street read-through, and low-intensity alternatives. PNG and mapping cover storefront states, aisle modules, stocked/depleted shelves, counter, heat lamp, signage, proprietor, customers, product icons, and shop UI.

## Validation

- Hours and the post-02:00 markup agree everywhere.
- The surcharge is not duplicated in both item base values and transaction logic.
- Hostel adjacency is physical/economic, not an interior transition.
- Quest-requested goods use the same item IDs as store inventory.
- Closed-state art and interaction denial are both present.
