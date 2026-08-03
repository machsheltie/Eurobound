# Asset Pipeline

2) Production Tools & Asset Pipeline – “The Game Factory”
Engine & Build Tools
Godot 4.x – main game development, native desktop export
TileMap editor mandatory (replaces Tiled entirely — autotiling, physics shapes, and multi-layer support are now first-class in Godot 4)
Steamworks SDK & steamcmd – Steam builds, depots, store submission
Steamworks Partner Account – required for Steam testing & release

Art & Animation

UI & UX Design Workflow (Figma-Free Zone)
Primary Design Tool:
- Adobe Photoshop – sole environment for UI, HUD, menu layouts, buttons, icons, and storefront screenshot composition.
- Rationale: Native desktop speed, precise layer & pixel control, no browser latency, leverages 25+ years of design muscle memory.

Prototyping / Developer Handoff:
- Zeplin – accepts Photoshop exports, auto-generates pixel specs, asset slices, and clickable flows for developers.
- Rationale: Handles collaboration & export without forcing work inside a cloud editor. Keeps design decisions in Photoshop.

Optional Marketing Asset Tools:
- Canva Pro (optional) – for rapid marketing boards or social media graphics when Photoshop isn’t necessary.
- Affinity Publisher (optional) – for laying out large multi-screenshot storefront sets or press kits with precise typography.

Pipeline Notes:
1. All UI assets are authored in Photoshop, layered and grouped for easy export.
2. Export to Zeplin via plugin for developer access.
3. Prototyping is limited to clickable flows — no animation mockups are required unless specifically scoped.
4. Marketing assets may be adapted into Canva or Publisher, but design direction remains in Photoshop.
5. No Figma or browser-based design tools are used at any stage — prevents performance loss, UI lag, and tool overhead.

Aseprite – pixel art characters, enemies, tiles, and FX animation
Photoshop/Affinity – UI, panels, promotional art, complex composites
Godot TileMap Editor – integrated map building with collision, lighting, and layering (no external export step)
Littera / BMFont – bitmap font creation for crisp retro text
Coolors / Adobe Color – palette generation for consistent style

Audio Tools
REAPER – professional loop point editing, mixing, mastering for BGM/SFX
OpenMPT – tracker-style composition for authentic retro chiptunes
MuseScore – composition for melodic/orchestral arrangements (Vienna themes)
ChipTone / sfxr / bfxr – retro sound effect creation
Audacity / Ocenaudio – quick edits, trimming, conversions

Version Control
Git + Git LFS – version control for code + large art/audio assets
Godot Built-In Scene Version Control – cleaner merges on Node trees and scenes

Accessibility Planning (Non-Optional for storefront compliance & ratings)
Colorblind-friendly palette tests (Sim Daltonism, Coblis)
Text scaling options (Dynamic Type support)
High-contrast mode toggle
Audio cues for purely visual events
Dyslexia-friendly font option toggle (e.g., OpenDyslexic or modified bitmap font)

Desktop UX Standards” (right after Accessibility):
Input conflicts (remappable keys, keyboard/controller hot-swap)
Resolution scaling (windowed vs fullscreen layouts)
Controller rumble accessibility (global toggle)
Text scaling support (scalable bitmap/variable font strategy)
Screen reader hooks (focus order, alt text for buttons, battle log announcements)

Monetization Strategy – Decide Early
Premium upfront ($2.99–$4.99) – fits a satirical, one-shot experience
Optional IAP cosmetics – joke outfits, gag weapons
Affects:
Save system (cosmetic unlock persistence)
Content gating (unlockable maps/DLC)
Storefront featuring likelihood

Save System Architecture
Manual save at Wi-Fi hotspots (diegetic + functional)
Cloud save support via Steam Cloud
Corruption recovery via backup slot or periodic snapshot saves
Auto‑snapshot on lifecycle events
Save validation + rollback to last good snapshot

Technical Architecture & Performance Profiling
Frame rate targets: 60fps on typical desktop hardware, 30fps graceful fallback on min-spec machines
Memory usage caps to stay within budget
Texture streaming for larger worlds
Performance profiling passes for physics step and overdraw

“Lifecycle & Audio” subsection:
Background/foreground resume rules
Auto‑save on window focus loss and quit
Alt-tab/minimize pause behavior
Audio ducking + restore logic

Localization Prep (Even if English-only v1)
Externalize all strings to JSON or CSV from day one
UI tested for German/French text expansion
Cultural sensitivity review for satire-heavy scenes

Analytics Integration (Privacy-compliant)
Track player drop-off points
Identify battle difficulty spikes
Monitor menu/UI abandonment rates
Feed data into balancing and UX adjustments
Drop-off funnels, difficulty spikes, UI friction
Post-launch A/B hooks (feature flags)

FX & UI Polish
Particle Editing in Godot – reusable Shit sparks, star bursts, item pickups
Godot AnimationPlayer/Tween – microinteractions, bounce effects, crit shakes
UI Animation Standards – 120 ms button bounces, 12–20 particle bursts, rolling HP tween 1–2s

Data & Content Management
Git + Git LFS – version control for code + large binary assets
Godot’s Built-In Scene Version Control – prevents scene merge headaches
Google Sheets (optional) – balancing and stat planning before JSON commit

Steam Extras
GDExtension – controller rumble for crits, item pickups, boss moments
Build automation scripts – screenshot generation, metadata uploads
Steam Cloud Saves – cross-machine progress sync
Text Scaling Integration – scalable text for accessibility

Pipeline Flow
Concept & Sketch – paper/digital
Pixel Art Creation – export sprite sheets/tiles
Godot Import – pixel snap on, filters/mipmaps off
Data Entry – JSON for stats, gear, skills, strings
Combat Logic – stats, skills, rolling HP meter
Accessibility Pass – palettes, fonts, audio cues
Polish Layer – particles, microinteractions, SMAAAASH! crits
Performance Profiling – FPS, memory
Build & Test the desktop export – input/UI fixes early
QA & Content Lock – Steam beta branch release
--- NEW SECTION ---
Audio Strategy & Branding:
- Adaptive music with unique loops for overworld, battle, boss fights, and "seedy underbelly" areas.
- Implement browser-friendly "Click to Start" screen to enable audio autoplay in the browser build.
- Use looping-friendly formats (OGG for desktop and browser) and keep music memory footprint under ~10MB.

--- NEW SECTION ---
Monetization Strategy – Expanded:
- Satire compliance testing with external reviewers to avoid storefront "targeted group" violations.
- Regional sensitivity review with European playtesters to ensure humor is received as intended.
- Fallback monetization: HTML5/browser build sold via Itch.io or Stripe checkout (~$4.99) if the Steam version is rejected.


[CONTENT FROM PLAN ABOVE]



## Audio Strategy

### Adaptive Music System Plan
- Unique BGM loops per environment (overworld, battle, boss, “seedy underbelly”).
- Combat layers crossfade based on player state (normal vs. low HP vs. Inspired buff).
- Transitions triggered by event cues (e.g., entering a VIP area muffles the music).
- Comedic stingers for crits, status cures, and plot twists.
- Character leitmotifs layered into battle tracks when active; inverted or warped during debuffs.
- Environmental audio ducking in cutscenes for roast line clarity.

### Browser Audio Autoplay Compliance (Click to Start)
- Pre-title “Click to Start” screen meets browser audio unlock rules.
- Diegetic click trigger (e.g., clicking the jukebox) instead of generic start button.
- Click triggers short gag SFX that segues into main theme.
- Cache intro so replays can bypass the click without breaking compliance.

### Audio Memory Cap Target (~10 MB)
- Compressed OGG (desktop and browser).
- Limit to one in-memory music track + two SFX banks.
- Stream long tracks instead of fully loading into memory.
- Shared SFX banks for similar environments.
- Loop point trimming in REAPER to remove unused audio padding.

### Leitmotif Plan for Key Characters
- Short melodic phrase per major character woven into scenes.
- Instrumentation varies by location/state (e.g., pompous brass → drunken tuba).
- Micro-motifs hidden in environmental SFX for proximity clues.
- Leitmotif callbacks in boss themes to foreshadow plot.

## Asset Workflow Gaps

### Photoshop → Godot Import Guidelines
- PSD → PNG export with power-of-two dimensions; pixel snap on, filters off.
- Naming conventions for batch import (e.g., ui_btn_attack@2x.png).
- Export profiles auto-strip unused layers and trim transparencies.

### Pixel Art Style Guide & Consistency Standards
- Fixed palette; 1:1 pixel ratio; consistent outline weight.
- Defined lighting rules for all shading.
- Standard animation timing (8 frames @ 12fps for idle loops).
- Separate pixel grid for UI vs. character assets.
- Style guide sheet with do/don’t examples for satire readability.

### Retina-Safe Retro Font Rendering
- Bitmap fonts scaled ×2–×3; mipmaps off; pixel snap enabled.
- Test readability on high-PPI devices & in Sim Daltonism.
- Hinted fonts for heavy text screens to avoid strain.

### Tileset Creation Process
- Modular 16×16 or 32×32 tile chunks; autotile templates for Godot.
- Palette lock per world for instant recognition.
- Metadata tags for auto-collision and gameplay flags.
- Reusable prop sheet for satire gags.

## Storefront Release & Marketing Playbook

### Compliance & Sensitivity
- European tester roster tagged by region/city expertise.
- Pre-submission satire compliance pass using storefront flagged-term filters.
- Maintain storefront “story-safe” screenshots that pass review without humor dilution.

### Monetization Contingency
- Itch.io and browser builds ready if Steam rejects.
- “Deluxe Roast Pack” DLC with extra gag cosmetics; no gameplay gating.
- Browser build marketed as “uncensored edition” to spin rejection into PR.

## UX & Accessibility Implementation Guide

### QA Testing & Accessibility
- Test all menus for clear focus/click targets, color contrast, and focus order.
- Battle animation speed toggle (Normal/Fast/Off).
- High-contrast mode recolors UI and status icons for sunlight play.
- Keyboard-only and controller-only navigation both fully supported.
- Controller rumble map (crit hit = strong buzz, cure = short pulse) with global toggle.

### Localization-Ready Humor
- All text entries:
  ```json
  {
    "en": "Careful, you’ve got more grease on your fingers than a kebab cart.",
    "fallback": "Careful, you’ve got slippery hands there."
  }
  ```
- Fallback lines keep comedic intent without culture-locked idioms.
- Localization sheet columns: Has Pun (Y/N), Needs Fallback (Y/N).
- STRUCK (author ruling 2026-08-03): the `SAFE_LOCALE` high-risk-line auto-swap and "Cultural Risk" flagging were sanitization machinery — banned. Jokes ship at full strength in every locale; a translation may adapt a pun, never soften it.
- Translator notes explain original joke for adaptive rewrites.

Localization Prep:

A satirical, EarthBound-inspired RPG where the player roasts, debuffs, and out-styles a traveling rival trio — Lord Pilsner and his two frat-bro friends — across three heightened caricatures of European cities: Publandia (Dublin), Debaucheryville (Prague), and Sinfonia (Vienna). SNES-style pixel art, EarthBound-style front-view battles with a rolling HP meter, gear/items with comedic buffs, and premium desktop UX for Steam.