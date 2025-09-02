# Dev Workflow & Skills

3) Developer Skills & Workflow Spec Sheet – “The Game Maker”
Hard Skills (Technical):
GDScript – your main coding language; event handling, combat logic, UI behavior
Godot Scene/Node Structure – how to organize maps, actors, UI, and reusable components
TileMap Editing – collision, layering, parallax backgrounds
Animation – sprite frame animation, tween-based UI/FX, timing for impact
Data-Driven Design – load JSON into game, use for balancing without rewriting code
Mobile UX Optimization – touch input, safe area anchors, responsive scaling
Version Control (Git) – commit early/often, branch for features
iOS Build Process – export from Godot, sign in Xcode, run on device

Soft Skills (Creative & Project Management):
Timeboxing – setting small, achievable build goals each week
Iterative Testing – playing on real device early and often to catch UX issues
Asset Consistency – enforcing palette, pixel size, and animation timing rules
Cutting for Scope – knowing what to drop or simplify to meet deadlines
Feedback Integration – pulling in playtester notes without losing your vision
Emotional Resilience – staying motivated and confident through slow phases
Detail Obsession – microinteractions, SFX sync, pacing, UI readability

Workflow Mindset:
Build vertical slices first (1 map + 1 battle + 1 shop) → expand
Test touch feel on iPhone before adding more content
Keep data modular so you can add enemies/items without breaking systems
Prioritize player clarity over complexity — every action should feel instant and satisfying

Game State & Systems Architecture:
Quest/story flags (central registry + scene-local caches)
Inventory sync (authoritative model + UI bindings)
Party status preservation (HP/SP/conditions across scenes)

Error Handling & Stability” section:
Save Corruption Detection & Recovery – checksum or backup slot fallback.
Network Timeout & Retry Policy – if any online features are later added.
iOS Version Support Matrix – minimum version, graceful degrade for older devices.
Crash Reporting Integration – Sentry or Firebase Crashlytics for bug diagnostics.

UI & UX Design Workflow (Figma-Free Zone)
Primary Design Tool:
- Rationale: Native desktop speed, precise layer & pixel control, no browser latency, leverages 25+ years of design muscle memory.

Prototyping / Developer Handoff:
- Zeplin – accepts Photoshop exports, auto-generates pixel specs, asset slices, and clickable flows for developers.
- Rationale: Handles collaboration & export without forcing work inside a cloud editor. Keeps design decisions in Photoshop.

Optional Marketing Asset Tools:
- Canva Pro (optional) – for rapid marketing boards or social media graphics when Photoshop isn’t necessary.

Pipeline Notes:
1. All UI assets are authored in Photoshop, layered and grouped for easy export.
2. Export to Zeplin via plugin for developer access.
3. Prototyping is limited to clickable flows — no animation mockups are required unless specifically scoped.
4. Marketing assets may be adapted into Canva or Publisher, but design direction remains in Photoshop.
5. No Figma or browser-based design tools are used at any stage — prevents performance loss, UI lag, and tool overhead.

--- NEW SECTION ---
Phaser.js Mobile Performance & Loading:
- Mobile performance profiling with iPhone 8 as baseline; ensure battle scenes run <50ms frame times.
- Memory management: cap sprite atlases at 2048×2048px and unload after each world; stream audio on demand.
- Progressive loading: load World 1 instantly, stream Worlds 2 and 3 in background during play.

--- NEW SECTION ---
Content Production Pipeline Enhancements:
Writing Workflow:
- Maintain dialogue in Google Sheets with columns for speaker, emotion, tone, and triggers.
- Export to JSON and lock per world before final art pass to prevent scope creep.

Balance Testing Methodology:
- Target normal battles to last 3–5 turns, bosses 6–8 turns.
- Test with novice, casual, and veteran RPG players; adjust stats in 5% increments until ≥80% satisfaction across tiers.

- Store all strings in external JSON from day one.
- Avoid puns that cannot be translated; create fallback jokes.
- Limit UI labels to ≤25 characters.


--- Added Battle Systems Architecture Details, Behavioral Easter Egg Engine ---
[CONTENT FROM PLAN ABOVE]



## QA & Bug Tracking

### Defined Bug Triage Process
- Severity + Player Impact matrix to prioritize based on how bugs affect the critical first 10 minutes of gameplay.
- Maintain a Repro Steps + Expected/Actual template to avoid vague bug reports.
- GIF or short video capture required for UI/animation bugs to speed visual debugging.
- Label bugs with tags like “Mobile-Specific,” “Satire-Text,” “Combat Logic” for quick filtering.
- Weekly triage review cross-referencing last 7 days of commits to spot regressions early.

### Hotfix Deployment Plan
- Maintain a pre-patched hotfix branch always synced to latest live version.
- Target 24-hour turnaround for P0/P1 issues.
- Automated flow: Build → TestFlight/Itch.io private release → QA sign-off → push live.
- Public “Hotfix Notes” presented in humorous in-universe style.

### Balance Testing Methodology
- Use session-based telemetry to measure average battle length, skill usage frequency, and status cure rates.
- Recruit persona-based testers: satire enjoyers, RPG min-maxers, casual mobile dabblers.
- Comedy cadence testing — humor punchlines in combat must land without being cut off by battle pacing.
- Target curve: Normal fights = 3–5 turns; Boss fights = 6–8 turns; survivability baseline = 2–3 mistakes before wipe.
- Log rage-quit triggers (e.g., stacked debuffs, resource starvation) and adjust pacing.

### Cultural Sensitivity Reviews as Formal Step in QA
- Use Cultural Sensitivity Review Template with explicit satire intent checkboxes.
- In-region reviewer ensures cultural accuracy; final decision for inclusion rests with developer (you) and Apple for store approval.
- Flag non-obvious risks (jokes fine in English but risky if literally translated).
- Maintain a “Satire Safety Changelog” for modified or removed lines.

## EuroBound Main Doc

### Easter Egg System Plan
- Data-driven triggers in JSON to allow adding/changing eggs without code edits.
- Tiered types: Visual (props), Audio (leitmotif stingers), Mechanical (hidden combat effects).
- Eggs reference other worlds, Darkweb Dossier, and meta-commentary.
- Track Easter Egg completion %; reaching thresholds unlocks cosmetic gags or secret cutscenes.

- Banter lines stored in JSON with tags for Mood, Context, and Frequency.
- Conditional hooks for status effects, quest completion, and gear choices.
- Regional slang variants for authenticity and humor per city.

### Behaviorally Tailored Dialogue Based on Known “Patterns”
- Player profile tracks aggression, spending habits, and status effect frequency.
- Certain patterns unlock Easter Eggs or special interactions.

## 25% Improvement Layer

### Cross-File QA Step
- One Unified Pre-Merge Checklist for all pipelines (art, writing, code, audio):
  - Performance — FPS/memory checks, asset size budgets, mobile input responsiveness.
- "Context echo" check — verify that a change in one file doesn’t break tone, visual consistency, or feature hooks in related files.
- QA lead (developer) logs a pass/fail note in a shared “Merge Gate” sheet before merge.
- All checks performed in final runtime context (UI on device, audio in-engine, code in latest build).

### Performance Profiling Targets
- Baseline device: iPhone 8 (A11, 2GB RAM).
- Pass criteria:
  - FPS: Target 60; no dips <30.
  - Memory: ≤ 350 MB peak.
  - Battery: ≤ 8%/15min overworld; ≤ 10%/15min battle.
  - Load: ≤ 5s initial, ≤ 2s scene change.
- QA logs results in Perf Tracker sheet with build ID/date/env.
- Auto-profiling script outputs frame/memory logs to `/logs/perf/`.