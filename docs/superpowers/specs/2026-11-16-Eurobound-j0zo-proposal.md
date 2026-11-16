# First-slice Settings list: proposal

**Status:** PROPOSED. Nothing here is canon until the author rules on Eurobound Desk card `Eurobound-j0zo-q2`.
**Bead:** Eurobound-j0zo. **Date:** 2026-11-16.
**Author's instruction (Desk, 2026-11-16):** "An agent proposes a short first-slice list from the UX guide and the GDD for my approval".
**Rule for this doc:** every item comes from `design/ux/UX & Accessibility Guide.md` or `design/game_design_document.md` (plus the volume item the ledger ties to this bead). Nothing is invented. Line numbers are the current ones; the bead's older numbers had drifted.

## What the Settings screen does today

- `game/ui/field_menu.gd:555-556` (`_settings_text`) prints the controls and "Reduced motion: On/Off" as static text. Nothing on it can be changed.
- Reduced motion already works as a flag: `game/worlds/debaucheryville/arcade_ambient_fx.gd:17` (`settings.reduced_motion`, `set_reduced` at :55). The field menu toggles it from the Settings entry at `game/ui/field_menu.gd:296-298`. Only the Arcade ambient effects read it.
- Volume works in code, with no screen: `game/core/audio.gd:8` (`set_volume` / `get_volume`, stored under `settings.volume.<bus>`, `:16`, `:27`). Three channels (ledger `docs/superpowers/NEXT_WORK.md:903`).
- Keys are fixed: `game/characters/player/player_controller.gd:380-395`.
- Text size, high contrast, chat speed, prompt style and rumble: no code at all.

## Proposed first slice (6 rows)

| # | Setting | Source | In game/ today? |
|---|---|---|---|
| 1 | **Reduced motion** (On/Off). Guide: "disables shakes, rapid animations, and particle clutter" | Guide :21; GDD :321 | Flag and toggle exist; make it a real row on the Settings screen |
| 2 | **Volume: Music, SFX, Ambience** (three sliders) | Ledger :903 ties the volume question to this bead; the Guide and GDD do not list it | Code exists (`audio.gd:8`); no slider |
| 3 | **Text size** (scaling steps) | Guide :13, :19 | No |
| 4 | **High-contrast mode** | Guide :14, :19; GDD :314, :321 | No |
| 5 | **Chat speed** (and fast-scroll) for ICQ chats | GDD :259 | No |
| 6 | **Controller / keyboard prompt style** | GDD :351 | No |

Why these six: the Guide's own first-launch screen (:19) names text size, high contrast, rumble and reduced motion, so the docs treat those as basic. Chat speed and the prompt toggle are the two the GDD asks for on screens the slice already has (ICQ chats, battle menus).

## Held for after the slice

| Setting | Source | Why later |
|---|---|---|
| Rumble toggle | Guide :7, :15, :19 | Needs a rumble event map first (Guide :7); no rumble exists |
| Remappable keys and bindings | Guide :16 | Biggest build; keys are hard-coded today |
| First-launch accessibility screen | Guide :19 | Only useful once rows 1, 3, 4 exist, then it reuses them |
| Screen reader strings, focus order | Guide :4, :12 | Guide says "before alpha", not the slice |
| Auto UI and resolution scaling | Guide :20 | Engineering, not a player setting |
| Animation speed toggles | GDD :352 (a one-line changelog note, no spec) | Undefined |
| Sung-chorus toggle in audio settings | `design/audio/musicalbeats.md:17` | Only matters once sung choruses exist |
| Colorblind screenshot check | Guide :22 | Asset pipeline step, not a setting |

## Open decisions for the author

1. **Does voice get its own volume channel?** Ledger :903 says to decide it with this bead; it stays at three until then. This proposal assumes three.
2. **Where do the values live?** Assumption: `GameState.flags` under `settings.<name>`, the pattern reduced motion and volume already use. No save-format change is proposed.
3. **High contrast and text size need a palette and a size table.** The Guide asks for "swatches + pass criteria" (:6) but none exist. That is design work, not something this proposal invents.

## On approval

Record the list in the ledger and file a build bead for a working Settings screen (the bead's acceptance criterion). Rows 1 and 2 are cheapest because the code exists.
