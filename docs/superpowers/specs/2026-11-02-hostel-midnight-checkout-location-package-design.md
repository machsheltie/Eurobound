# Hostel "Midnight Checkout" Location Package Design

## Intent and Identity

Define the hostel as Debaucheryville's primary accommodation, recovery, confession, and rotating-traveler hub.

- Location ID: `debaucheryville_hostel_midnight_checkout_01`
- Slug: `hostel_midnight_checkout`
- NPC folder: `Hostel_Midnight_Checkout`
- Primary source: `hostel_midnight_checkout.md`

## Visual and Spatial Design

A converted four-story nineteenth-century building combines an ornate doorway with peeling paint, random window units, cheap plastic signs, and flickering neon. The interior must read as controlled chaos: inconsistent reception, circulation to dorm and private-room thresholds, compressed bunk room, passive-aggressive kitchen-note gallery, shared social space, Wi-Fi/ICQ point, and exit.

The package should model the playable representative rooms rather than imply that every floor and bed is explorable. Bunk occlusion, narrow aisles, and rotating guests need clear staging for dialogue and image generation. Day/night and occupancy states should visibly change the same spaces.

## Gameplay, Quests, and State

Reception is nominally 24/7. Booking tiers cost money and influence bed quality, privacy, recovery, random roommate events, and next-day statuses. Core systems are check-in, sleep, confession encounters, kitchen interactions, Wi-Fi/ICQ access, and the survival-of-one-night milestone. Couchsurfing and other traveler quests may route NPCs through the hostel, but their dialogue remains externally owned.

The hostel connects physically to Hostel Row and economically to Midnight Munchies. Cyberspace Kavarna is reached from the same street district, not through an invented internal basement door unless an authoritative source explicitly assigns one.

## Package Directives

Items distinguish room-service purchases, consumables, kitchen props, and quest-owned belongings. NPCs include staff, scheduled guests, and rotating archetype groups with occupancy rules. Nodes must encode room-type thresholds and prevent randomized events from spawning in impossible locations. PNG requirements cover the façade, reception, dorm, bunks, kitchen, social area, signs, notes, bedding states, guest variants, and UI. Repeated rooms should be modular assets rather than unique scene paintings.

## Validation

- Prices, rest quality, privacy, and status effects agree across files.
- One-night completion and repeat-stay progression use stable flags.
- Rotating guests never overwrite fixed quest NPC schedules.
- Midnight Munchies and Cyberspace are district exits/referrals, not invented hostel rooms.
- The node graph represents a playable subset without promising a complete four-story simulation.
