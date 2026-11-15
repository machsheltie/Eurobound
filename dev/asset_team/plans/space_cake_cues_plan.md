# Space Cake and Contact High cue art: plan (asset team, for author approval)

Bead: Eurobound-k3qa.

**Author ruling:** "Start now: a writing round with me for the lines, the art team makes the cue art from the PNG spec, and the screen parts get built when both are in".

**Status:** plan only. Nothing is painted until the author approves this plan on the Eurobound Desk (card `asset-team-plan-space_cake_cues`).

## Sources (canon)
- The PNG spec: `design/worlds/shamsterdam/PNG_Assets/De_Groene_Gids_PNG_Assets.md`, lines 340-356 (sheet `groene_gids_ui.png`, 512x512, palette #228B22, #39FF14, #708090, #C8BFA6) and lines 497-502 (the two-hour Space Cake system).
- The approved spec: `docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md`, items SC4, SC5c, SC7, T6 and CH.
- `design/worlds/shamsterdam/de_groene_gids.md`, lines 214, 219-240 and 279.

## Art needed (on the Asset Board under `space_cake_ui`)

| Asset | Size | What canon says | Proposed method | Gate |
|---|---|---|---|---|
| Space Cake Timer UI | 192x64, size disputed (Eurobound-m1uo) | "Visible two-hour countdown, game time" | Flat painted UI panel in the sheet palette. The countdown digits are drawn by the game, not painted. | U |
| "It's Not Working" dialogue plate | 192x96 | Available at 30, 60 and 90 minutes | Flat painted plate. The text area is left blank for the lines from the writing round. | U |
| Staff Response plate | 128x96 | Lines: "It is working. You will know. Wait." / "Ninety more minutes." | Flat painted plate. The text is typed from the doc and rendered by the game or with a font, never drawn by an image tool. | U |
| Contact High Indicator | 48x48 | "Ambient AoE affecting the whole party while inside" | One small 3D object on the approved battle-icon badge (`battle_hud_icons_plan.md`). The object is a canon haze motif; if canon names none, the Writers' Room proposes it (author rule). | A3/A4 + U |
| Onset: 3 distortion rings | 2.0 s at 1.5 FPS | Fires at 120 minutes | A 3-frame VFX sprite strip: concentric warp rings in the sheet palette. | V |
| Warp vignette | full screen | Engages with the rings. On Low LOD it becomes a static corner overlay; in reduced-motion mode it is replaced by an onset sting icon | A screen-edge overlay texture, a static corner variant, and the sting icon. | V (overlays), U (icon) |
| Bros trio "OH." frame (x3) | sprite frames | The trio's reaction at landing | Character art. **The Sprite Development Team** does these in their look-B pipeline; the asset team does not. | Sprite gates |
| Teleport cue (T6) | VFX | `NavigationRoll` returns teleported; the Voetgangerstunnel scene does not exist yet | A short VFX, scheduled after the tunnel scene exists. | V |

## Rules applied
- **Physical descriptions first (author, 2026-11-15).** Where canon gives no picture or colours, for example the Contact High object or the ring look beyond "distortion", the Writers' Room proposes it before we paint. The spec's sheet palette sets the colours for the UI panels.
- **Icons go 3D** (author, 2026-11-13). The UI panels and VFX are 2D painted to match the existing UI.
- **Lettering is never drawn by an image tool.** Text areas stay as the spec has them, waiting on the writing round.
- **Every asset goes through a blind gate:** U for UI, V for VFX, A3/A4 for icons (`dev/qc/QC_COVERAGE.md`).

## Order
1. The Contact High Indicator and the Timer UI. These are the parts the player sees first.
2. The Staff Response and "It's Not Working" plates, after the writing round.
3. The onset rings, the vignette and the sting icon.
4. The teleport cue, after the Voetgangerstunnel scene exists.

## Cost
- About 90 Tripo credits for the Contact High object, unless a Blender-scripted object fits (0 credits).
- Everything else is painted or scripted at 0 credits.
