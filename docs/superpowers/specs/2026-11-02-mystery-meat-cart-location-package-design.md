# Cirque du Shady - Mystery Meat Cart Location Package Design

## Intent and Identity

Define Mystery Meat Cart as a separate circus food vendor, clown-gear interaction hub, and Great Döner Debate participant.

- Location ID: `debaucheryville_cirque_mystery_cart_01`
- Slug: `mystery_meat_cart`
- NPC folder: `Mystery_Meat_Cart`
- Primary source: `mysterymeatcart.md`
- Secondary asset source: the accidentally appended cart section in `publicrestroomkebaballey.md`, after reconciliation.

## Visual and Spatial Design

Beside the ringmaster tent, a steam-belching pushcart uses violent carnival light, a carousel-shaped neon rotisserie, glitching menu letters, cracked clown-mask display, suspicious storage, and Chef Chuckles' knife-flipping station. The service footprint is approach, animated sign, rotisserie/menu counter, Chuckles node, ingredient/storage examination, consumption/reaction point, circus route, and exit.

Night-performance effects intensify the same cart; they do not create a separate room. Flashing light requires a reduced-flash replacement that preserves timing cues.

## Gameplay, Quests, and State

The cart is available during circus hours. It sells the documented meat menu for Kebab Coins, applies food-specific risks and rewards, participates in the Great Döner Debate, and unlocks Chef Chuckles' sidequest when full clown gear is equipped. Circus-performance and night states may modify effects and vendor behavior.

## Package Directives

Items define every menu product, cost, effect, tag, and clown-gear prerequisite reference. Interactions own purchase, consumption, knife-performance reaction, gear check, sidequest binding, and examinations. NPCs define Chef Chuckles and circus customers. PNG/mapping reconcile both asset sources into cart faces, rotisserie states, menu sign, food, props, chef animations, customers, steam/grease, UI, and accessibility states.

## Validation

- Restroom assets are excluded from this package despite source contamination.
- Full clown gear checks exact external equipment IDs.
- Menu costs and status effects agree across files.
- Night enhancements preserve a safe reduced-flash mode.
- The cart remains distinct from The Participation Trophy and ringmaster tent.
