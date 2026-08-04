# EuroBound

**EuroBound** is a retro-inspired mobile JRPG built in the spirit of EarthBound with a sharply satirical twist. Players control a trio of washed-up frat bros—Lord Pilsner, Chadwick, and Bradley—on a final bender across Europe as they attempt to reclaim their youth one terrible decision at a time.

## 📍 Core Features
- Front-view, turn-based combat with rolling HP meter and absurd status effects
- Three unique parody cities: Publandia (Dublin), Debaucheryville (Prague), Sinfonia (Vienna)
- Visible overworld encounters, ICQ-style save/chat terminals, NFT sidequests
- Deep narrative systems and world state persistence
- Built for mobile: one-handed UX, high-contrast modes, fluid microinteractions

## 🧠 Repository Structure

```
Eurobound/
├── game/          ← the Godot 4.4 project — open THIS folder in Godot
│   ├── core/            autoloads (data_repo, game_state, save_system,
│   │                    input_manager, scene_router) + main/game_manager scenes
│   ├── systems/         shared gameplay systems (dialogue, breweries,
│   │                    economy, shadow_exchange, icq_events, utilities)
│   ├── battle/          battle scenes + scripts together
│   ├── characters/      player, party, NPC base, enemy scenes + scripts
│   ├── ui/              title screen, menus, HUDs, dialogue, popups
│   ├── worlds/
│   │   ├── debaucheryville/   everything for the city: scenes,
│   │   │                      restrooms/, interactables/, data/
│   │   └── shared/            location templates + shared world scripts
│   ├── assets/          global data (JSON the engine loads) + audio
│   ├── addons/          GUT test framework
│   └── tests/           unit tests (run via GUT)
├── design/        ← the complete game design wiki
│   ├── worlds/          per-city design: debaucheryville, publandia,
│   │                    sinfonia, shamsterdam (+ shared interactables)
│   ├── characters/      the bros, NPCs, cosmetic changes
│   ├── quests/          general_quests/ (cross-city chains) + per-city folders
│   ├── items/           item docs (docs/ = masters, per-item .md files)
│   ├── mechanics/       battle, progression, social, systems
│   ├── economy/         Sovs currency canon, shops, crypto satire
│   ├── narrative/       main quest, dialogue system, backstories
│   ├── style_guides/    writing style, humor, naming consistency
│   ├── ux/              accessibility guide, HUD, wireframes
│   ├── templates/       authoring templates (NPC, quest, PNG specs...)
│   ├── reference/       EarthBound reference material
│   ├── audio/           music design
│   └── legacy/          retained old-era docs (author's call)
├── docs/          ← PRD, specs, plans, the NEXT_WORK ledger
├── marketing/     ← press kit, store compliance, screenshots
├── production/    ← schedules, workflows, weekly write-ups
├── tools/         ← Python utilities (validation, content gen)
└── builds/        ← export output (contents gitignored)
```

**Where does X go?** Game code/scenes/data the engine loads → `game/` (city
content in its city folder, shared systems in `systems/`). Design writing →
`design/` (city content in `design/worlds/<city>/`, quests in `design/quests/`,
items in `design/items/`). Process/planning → `production/`. Product-level
docs and specs → `docs/`.

## 🎯 Project Goals
Create a mobile-first, narrative-rich RPG that delivers on humor, design, and accessibility.

## 🚧 Current Status
Pre-production — design wiki restructured (2026-08); engine slice boots with
GUT tests green. See `docs/superpowers/NEXT_WORK.md` for the active work ledger.
