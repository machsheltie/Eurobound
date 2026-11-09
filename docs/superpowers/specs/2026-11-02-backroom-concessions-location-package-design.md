# Backroom Concessions Location Package Design

## Intent and Identity

Define Backroom Concessions as the hidden digital-underground food counter behind the main internet café.

- Location ID: `debaucheryville_internet_cafe_backroom_concessions_01`
- Slug: `backroom_concessions`
- NPC folder: `Backroom_Concessions`
- Primary source: `backroomconcessions.md`

## Visual and Spatial Design

As an approved normalization decision, Cyberspace Kavarna is the parent café even though neither brief explicitly names the other. Its café-side approach is marked by a concealed doorway and flickering `404: Calories Not Found` sign. Beyond it, a concession booth is wedged between gutted vending machines beneath buzzing fluorescent lights, surrounded by mismatched office chairs, pop-up-filled CRTs, a peeling `Hot Pockets + Protocols` menu, thermal-paste containers, and hacked-server glow.

This is a tiny destination with a strong counter/service composition. Nodes are entrance threshold, Donny.exe counter, menu display, vending-machine props, improvised seating, clue/referral node, and return transition. The source's front-restroom graffiti clue is owned visually by the parent café; this package owns the inside face of the hidden doorway.

## Gameplay, Quests, and State

Once `cyberspace_backroom_concessions_entrance_discovered` is set, the room remains available around the clock. Donny.exe sells the documented digital-food menu, applies item-specific buffs and hazards, manages black-market referrals, and reacts to the SnackHack/ICQ state. DigiDysentery, Thermal Paste Sundae effects, and RAM Chips & Dip consequences require explicit, testable status definitions.

Eating here may change how café patrons react, but the parent café owns those NPC interactions. The package exports the appropriate consumed-item or respect flags.

## Package Directives

Items are the menu and its effects; prices and status results must be authoritative in one catalog. Interactions bind purchase, confirmation, consumption, referral, vending-machine examination, and exit. NPCs center Donny.exe with only documented ambient customers. PNG requirements reconcile any prior food, counter, vending, CRT, server-light, menu, character, particle, and UI assets into HD-2D layers.

## Validation

- Discovery remains permanent after the café clue sequence.
- Every menu entry has matching price, item ID, and effect references.
- Parent-café reactions consume exported flags without duplicating Backroom logic.
- Donny.exe dialogue is referenced where externally authored.
- No full second internet café is invented inside this room.
