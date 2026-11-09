# Internet History Museum Location Package Design

## Intent and Identity

Define the Internet History Museum as a faux-serious nostalgia museum, cursed exhibit hub, and parent location for the Meme Black Market entrance.

- Location ID: `debaucheryville_blockbuster_internet_museum_01`
- Slug: `internet_history_museum`
- NPC folder: `Internet_History_Museum`
- Primary source: `internethistorymuseum.md`

## Visual and Spatial Design

The exterior retains the silhouette of a failed Blockbuster, boarded with floppy disks and broken jewel cases beneath Comic Sans institutional branding, caution tape, obsolete devices, graffiti, and a sagging 404 sign. Inside, a readable museum circuit connects the Hall of Modems, GeoCities Diorama, Angelfire wall, Habbo crime scene, MSN graveyard, iMac altar/darkroom, MIDI archive, staff point, secret VHS shelf, and exit.

Exhibits are deadpan museum displays first and cursed interactables second. CRT flicker, static, MIDI, and glitch effects need reduced-flash and audio-accessibility variants. The secret shelf has ordinary, hinted, puzzle-ready, and open states.

## Gameplay, Quests, and State

Public hours are 08:00-20:00. Free exhibits apply documented nostalgia, malware, or lore effects and coordinate ICQ events. Reading the prerequisite graffiti sets `meme_black_market_graffiti_clue_read` and enables `internet_museum_after_hours_access_enabled`: from 03:25-03:40 the otherwise closed front door is quest-unlatched, the public services and staff remain absent, and only the exhibit route needed for the GeoCities/MSN sequence is active. At 03:33, successful interaction sets `meme_black_market_entrance_discovered` and then `meme_black_market_entrance_unlocked` when the password sequence completes.

The museum owns the kiosk, password prompt, shelf mechanism, and transition. Meme Black Market owns the hidden room, vendor, summons, inventory, and rewards.

## Package Directives

Nodes map one directional exhibit loop with optional side inspections. Items distinguish museum artifacts from actual rewards. NPCs include curator/staff and visitors without promoting exhibit props to NPCs unless animated. PNG requirements cover the ex-Blockbuster façade, exhibit kits, plaques, CRT states, VHS shelf, terminals, characters, UI, static/glitch overlays, and accessibility replacements.

## Validation

- The 03:25-03:40 quest-unlatched access window and 03:33 puzzle trigger are explicit and testable.
- Every exhibit interaction maps to one landmark node.
- The Meme Black Market interior is excluded.
- Puzzle password/state matches the destination package.
- Hazard effects have reduced-flicker and reduced-audio alternatives.
