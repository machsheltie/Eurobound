# Public Restroom - Grease Trap Shrine Location Package Design

## Intent and Identity

Normalize the malformed Kebab Alley restroom brief into a dedicated secret-location package without importing its accidentally appended Mystery Meat Cart asset section.

- Location ID: `debaucheryville_kebab_alley_grease_trap_shrine_01`
- Slug: `public_restroom_grease_trap_shrine`
- NPC folder: `Public_Restroom_Grease_Trap_Shrine`
- Primary source: restroom content in `publicrestroomkebaballey.md` before `# Mystery Meat Cart - Complete PNG Asset Requirements`

## Visual and Spatial Design

The Late-Night Kebab Stand owns the grease tent, hand-scrawled `NOT A TOILET` sign, debris, pickle barrels, chili-sauce trail, and crawlspace exterior. This package starts inside a tiny grease-glazed restroom under sickly orange shrine light and a fluorescent bulb hung from a meat skewer. Key props are the receipt toilet paper, cursed sink collection, oily reflective walls, cracked mirror with QR/meat glyphs, kebab-eyed graffiti, Fistø pilgrimage tag, haiku, and return crawlspace.

The graph is threshold, toilet/receipt, sink relics, mirror glyphs, Fistø tag, hungover kebab icon, haiku/completion point, and exit. Reflection effects require a low-distortion alternative.

## Gameplay, Quests, and State

The destination requires `grease_trap_shrine_crawlspace_discovered` and `grease_trap_shrine_access_window_open`, which is true from 03:00 through 03:59 and false at 04:00. Eating a qualifying kebab while reading the graffiti unlocks `Stomach of Steel`. The pixel kebab glows only while Hungover and grants Fistø lore; completing the documented graffiti set while Hungover unlocks `The Greasy Prophet`. The combined Absinthe + Grease Kebab + graffiti condition triggers the referenced Fistø ICQ message.

## Package Directives

Items include the cursed coin, antacid, receipt, and other props only when collectible; otherwise they remain examinations. Interactions must evaluate compound requirements atomically. NPCs are normally empty. Environment owns grease shimmer, steam/fog, flies or ambient effects inside, and accessibility variants. PNG and mapping cover restroom faces, fixture props, graffiti states, glyphs, mirror/reflection masks, status cues, buff/title UI, and crawlspace interior.

## Validation

- No content after the appended Mystery Meat heading is imported.
- The normalized ID is used by all seven JSON files and the stand transition.
- The 03:00 gate and compound buff/lore conditions are exact.
- Graffiti completion uses a defined set, not arbitrary wall clicks.
- Effects remain readable with reflections and particles reduced.
