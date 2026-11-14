# QC coverage: every asset and sprite type, and its blind gate

Author ruling (2026-11-14, verbatim): "be sure ALL types of assets/sprites are being reviewed by our blind agents". Bead Eurobound-lrg5, under the QC review team bead Eurobound-2boh.

**Blind reviewer (the rule for every gate below):** a fresh agent that sees ONLY the asset, the approved reference and the checklist, never the producer, never the producer's reasoning or earlier attempts. The producer never reviews its own work. A fail goes back to the producer; after two failed fixes it goes to the author on the Eurobound Desk (the one mechanical exception is in `dev/asset_team/QC.md`).

**Where each gate logs:** location, item, prop and everything not a character: `dev/asset_team/reviews/qc_log.jsonl`. Characters, portraits, models and frames: `Tools/char3d/qc_log.jsonl`. Reply format for the new gates: `{"item","gate":"K|N|U|V|E|P|T|S|C","pass":true|false,"fails":["<checklist item number>: <concrete issue and where>"]}` plus `"date"`.

**Inputs the reviewer gets for the new gates:** the asset file(s), the named reference (approved art, doc line or model sheet), and the checklist. Quote any exact text (names, lettering, hex values) in the brief; do not point the reviewer at the producer's notes.

Standing rules that apply to every gate (checked as item 1 of each new checklist): no nudity; no real place names in the art; real brands keep real names; money reads SOVS, never euro or the euro glyph; no mascots or pets (ledger exceptions only); no narrator or wink; nothing sanitised.

---

## 1. Coverage map

Legend: OK = a gate covers it today. PARTIAL = a gate touches it but not the type's own failure modes. NONE = no blind gate.

### Characters and sprites

| Type | Gate today | Gap |
|---|---|---|
| Party and NPC painted portrait source (model sheet look) | G1 (Checklist A) | OK. Eight G1/G2 portraits predate the gate: see retro queue. |
| Tripo source image (arms-down copy) | G2 | OK |
| Rigged 3D model | G3, G3-face (face critic), reference-locked review, `review_3d.py` | OK. G3 not yet run on Bradley, Jakub, the 7-NPC batch, RECEIVABLE twin (queued by Sprite team). |
| Look-B 8-direction frames (party, NPC walkers) | G4 (Checklist C, critic face >= 7) | OK |
| Special poses and one-off frames (Jakub asleep, cradled/statue) | NONE | Needs a single-frame G4: new addendum **G4-S** below. |
| Crowd groups (idle only, front-facing) | NONE | New addendum **G4-C** below. |
| Texture fixes (project_ref, recolor_region, stamp_text lettering) | PARTIAL, only inside G3 | Add rule to G3 re-run: any texture fix is re-reviewed region by region, and lettering gets the A-1 letter-by-letter check. Covered by **G4-T** below. |
| Protocol trial outputs (SAM masks, material manifest, zoned texture + report) | PARTIAL: `masks` line logged for Chadwick; `review_3d.py` covers the step-10 colour comparison | Manifest and zoned texture have no gate. See **G4-T**. |
| Enemy battle sprites (`*_battle_w.png`, 15 Arcade, model sheets, palette swaps) | NONE (old pixel pipeline, never blind-reviewed) | **E** below. |
| Crowd/NPC old pixel sprites (`.aseprite`) | NONE | All being replaced under p7n6 (Sprite team); no review, not queued. |
| Dialogue portraits (in-game bust or box portraits cut from painted sources) | NONE (G1 reviews the painted source, not the cut dialogue asset) | **P** below. |

### Places

| Type | Gate today | Gap |
|---|---|---|
| Location plan | A1 (Checklist P) | OK |
| First day plate seediness thumbnail | A1.5 | OK |
| Location plates, exterior day / night / front elevation, interior day / night (emit layers where used) | A2 (Checklist L) | OK for look. **Gap:** night/emit registration is only a one-line check (L7); the clean-plate rule is not checked. Add **A2+ decomposition check** below. |
| NEW clean plates under the interactables rule | A2 only | A2+ decomposition check: nothing interactive painted in. |
| 3D building kits and modules | A3, A4, reference-locked review, `review_3d.py` | PARTIAL: no kit-level check (module reuse, seams, scale, set-wide look). **T** covers kits. |
| Arcade depth layers, battle backdrops, faces, mirror corridor | NONE (pre-QC) | Battle backdrops: **T**. Faces and depth layers: A2 at repaint. |
| In-game location scenes | A5 (critic loop, score >= 7) | Only the Arcade hall has shot lists. Each location needs its own `shots/<scene>.json` when wired. |
| Tilesets and street kits (`Assets/Graphics/tilesets/*`, currently empty) | NONE | **T** below. |
| City area plates (streets, squares) | A1/A2 by analogy only | Not produced yet. Treat as location plates: A1, A2, A2+; add T if tile-based. |

### Props, items and pickups

| Type | Gate today | Gap |
|---|---|---|
| Separate interactables, pickups, props as 2D cut-outs (Arcade rework, Eurobound-bcnr) | NONE | **C** below. |
| Same, as 3D | A3, A4, A5, `review_3d.py` | OK |
| Arcade prop kits (cabinets, counters, closet states, shadow switches) | NONE of their own | **C** (per-state and per-set checks). |
| 3D item icons, look B | A3, A4 (Checklist T, M) | OK. All 27 Debaucheryville icons have a blind pass (qc_log). |
| Legacy pixel item icons (`*_64/_128.png`) | NONE | Maintain-only; no new ones (author 2026-11-12). Not queued. If any is ever edited, it takes a **C** review. |
| NFT art | NONE | **N** below. Standalone NFT art is not produced yet. |

### UI, FX, key art, audio

| Type | Gate today | Gap |
|---|---|---|
| UI sheets (menus, HUD, windows, icons, fonts) | NONE (`Assets/Graphics/ui/` is empty) | **U**. Not produced yet. |
| VFX and FX atlases | NONE | **V**. Not produced yet. |
| Key art (box cover, load screens, wordmark) | NONE | **K**. Source: `design/style_guides/key_art_cover_and_loadscreens.md`. |
| Audio (ElevenLabs SFX; 3 `.ogg` in game: ICQ uh-oh, QR scan beep, NFT discovery chime) | NONE | **S**. A blind reviewer can judge audio only through a spectrogram plus a written cue sheet, or a human-ears pass; see S header. |

---

## 2. Additions to existing gates

### A2+ (decomposition check, added to A2 for every plate made after the interactables rule)
Source: `design/style_guides/location_interactables_rule.md`. The reviewer gets the plate, the plan's lists (A) scene decomposition and (B) asset requirements, and the location's interactions JSON.
1. Nothing in list (A) classed interactive prop, pickup or collectible, NPC anchor, FX anchor or UI/trigger point is painted into the plate. Doors, cabinets, stools, terminals, graffiti hotspots, QR posters, pickups are absent or shown as clean empty mounts.
2. Where an interactive prop was removed, the plate behind it is clean and continuous (no ghost outline, smear, hole or patch seam).
3. Every item in list (B) has a named asset id; every visible architectural-shell item is in the plate and is not in list (B).
4. Any interactable visible on the plate that is missing from the interactions JSON is reported as a finding (the reviewer does not invent the interaction); the producer files a bead or Desk card.

### G4-S (single special-pose frame, e.g. Jakub asleep in the statue's arms)
Reviewer gets the frame, the approved portrait or model sheet, the doc line describing the pose, and a game-size crop.
1. The pose matches the doc line exactly (who holds whom, which limbs, eyes closed or open as stated).
2. Same character as the portrait: outfit items, lettering letter by letter, colours, face features.
3. Anatomy: five fingers, two of each limb, no fused or missing parts, limbs not merged with the statue or prop.
4. Scale and floor: same height_m scale as the character's walk frames, contact with the statue/prop correct, nothing floats or clips.
5. Matches the 8-direction frames' look B (outline weight, shading, resolution).
6. The face still reads at game size.
7. No sanitising, no wink, no added props the doc does not name.

### G4-C (crowd group, idle only, front-facing)
1. Count of figures equals the brief. All are distinct (no copy-paste clones beyond what the brief allows).
2. Each figure passes G4 items 1, 2 and 6 (feet on the floor line, no stretched clothing, face reads).
3. Idle reads as breathing, not frozen; loop frame counts correct, no empty frames.
4. Overlap order is readable: no figure's limbs fuse into a neighbour's.
5. No figure is a named NPC unless the brief says so; no mascots, no animals.
6. Costume and signage text letter by letter against the brief.

### G4-T (texture fixes and protocol trial outputs)
1. Fix touched only the failing regions (diff the passing regions before and after: unchanged).
2. Lettering (stamp_text) reads correctly in a large crop; no cream rim, wedge, halo or off-register edge around glyphs; digits ("1", "7") have clean strokes.
3. The recoloured region matches the doc colour named exactly (hex quoted in the brief), within the `review_3d.py` PASS threshold.
4. Material manifest: every zone named in the reference file appears with a material; no zone is empty; names match the zone files.
5. SAM masks: each named zone's mask covers its region and excludes its neighbours, checked on an overlay image.
6. The step-10 report is attached; the outcome is exactly APPROVED, REVISION REQUIRED or BLOCKED, with skipped protocol steps named.

---

## 3. New checklists

### K: key art (box cover, load screens, wordmark, Steam capsules)
Reference: the approved concept text for that piece in `design/style_guides/key_art_cover_and_loadscreens.md` (Cover 3 "The Last Stand" primary; load screens L1, L2, L3). Reviewer gets the art, the concept's section, the wordmark treatment and the checklist.
1. Standing rules clear (no nudity, no real places, no mascots, no fourth party member, nothing traceable to a real street or landmark).
2. Exactly three living figures: Pilsner, Chadwick, Bradley. No pets or animals. Background NPCs only where the concept names a witness, mid-task, turned away.
3. Each bro matches his sheet and the doc: Pilsner navy tee riding up, cargo shorts, white crew socks, black flip-flops, frosted tips, puka shells; Chadwick popped collar, backward hat; Bradley jersey a size too small. The key props the concept names are present.
4. Sincere composition: nobody winks, nobody is cool or sexy; no rim light sculpting a jaw; camera at chest height; the bros do not look at each other.
5. Every element the chosen concept lists is present and no unlisted gag is added. Count them.
6. Wordmark: heavy collegiate slab, all caps, chrome bevel with pink-top to teal-bottom gradient, final O is a face-on bottle cap. Spelling EUROBOUND exactly (letter by letter). It survives on the plate (contrast).
7. All other text on the image is exact doc text, letter by letter, or absent.
8. Style: HD-2D painterly diorama with tilt-shift, the world beautiful and the bros the anachronism, not photoreal and not flat vector.
9. Format: the dimensions in the concept (cover aspect, load screen 16:9 at the minimum width the concept names); safe margins clear of the wordmark.
10. Thumbnail test: at 231x87 it still reads as "three guys, sky, logo" (the Cover 3 equivalent per its own thumbnail line).
11. No unapproved invented text, slogans or award laurels; nothing the author has not ruled (open items: wordmark is PROPOSED, so flag it as such, do not pass or fail it on taste).

### N: NFT art
Reference: the NFT's own doc built from `design/templates/NFT_Template.md`, plus the item doc. NFT artwork is 90s/00s pop culture, never location-derived (`.claude/CLAUDE.md`).
1. The subject is the 90s or 00s pop-culture reference the doc names. Real brands, games, songs and titles keep real names.
2. Nothing in the image is derived from the location where it is found: no location name, building, landmark, local signage or city palette.
3. No real place names, no euro or euro glyph, no nudity, no mascot or pet unless the doc names one.
4. Text on the image (title, serial, token id, watermark) is exact doc text letter by letter, or absent.
5. Single self-contained artwork, frame and format as the template states (aspect, size, transparent or flat background as stated). Edges are not cropped.
6. Reads as collectible artwork at the template's thumbnail size and at the in-game inventory size.
7. Style matches the template's art direction; not photoreal unless the doc says so; the era's look (CRT, early-CGI, pixel, Y2K chrome) is visible, not generic.
8. Each NFT in a set is visibly distinct from the others (no near-duplicates), and not a look-alike of any location plate.
9. Nothing sanitises the doc's joke or explains it.

### U: UI sheets (menus, HUD, windows, buttons, icons, fonts)
Reference: the UI spec or mock named in the brief (where none exists the reviewer returns BLOCKED, not pass).
1. Every element listed in the spec is on the sheet; none is extra. Count them.
2. Every label is exact spec text, letter by letter. Currency reads SOVS (singular "1 SOV"), never euro.
3. States: each interactive element has all its states (normal, hover or focus, pressed, disabled, selected) and they are distinguishable at 1x without colour alone.
4. Contrast: text on its background is legible at 1080p and at the Steam Deck size named in the brief (compare at that scale, 1x nearest).
5. Nine-slice and tiling: panels and buttons have a defined slice margin, corners are intact, the centre tiles without seams.
6. Grid and pixel consistency: one pixel grid across the sheet; no mixed pixel scales, no anti-aliased edges where the sheet is pixel art.
7. Safe area: nothing the spec places near the screen edge sits outside the safe margin.
8. Icons and glyphs: consistent stroke weight and perspective, centred in their cell with the stated padding; controller glyphs match the platform they name.
9. Sheet layout: cells aligned to the atlas grid, no bleed between cells, transparent where the spec says.
10. Style: consistent with the game's look and the approved UI reference; no stock-template look, no corporate or professional tone in microcopy (NPCs and menus are funny).
11. Gameplay data text is not invented (stats, prices, rules come from the docs only).

### V: VFX and FX atlases
Reference: the effect's doc or ability/status entry (`ability_template.md`, `status_effect_template.md`) and, for animated effects, the timing in the brief.
1. The effect named in the doc is what the sheet shows (the right element and colours; hex quoted in the brief).
2. Frame count, frame size and grid match the brief; no empty or duplicate frames; each frame is aligned to its cell.
3. Loop: loopers loop with no pop between last and first frame; one-shots start from nothing and end on transparent.
4. Timing: the key frame (impact, peak) lands where the brief says, measured as a frame index.
5. Transparency: clean alpha, no matte or fringe halo against dark and light backdrops; additive effects are on black as specified.
6. Readability at game size over a busy plate and a dark plate; it does not hide the characters' faces more than the brief allows.
7. Pivot and anchor: the origin is where the brief states; scaled by the stated factor it stays on its anchor.
8. Style: matches the look in the brief, painterly HD-2D or pixel as stated, not a stock particle pack.
9. Photosensitivity: no full-screen flash above three flashes per second, large high-contrast strobes flagged as a finding for the author (intoxication effects follow `design/mechanics/intoxication_law.md`: no free advantage encoded in the look).
10. Drugs, drink and sex effects are drawn at full strength and not softened (content rule); the reviewer flags softening as the highest severity.

### E: enemy battle sprites
Reference: the enemy's doc from `design/templates/enemy_template.md`, its model sheet, and the existing `<id>_battle_w.png` pattern.
1. The enemy matches its model sheet: silhouette, proportions, every costume element, colours (hex from the doc where named). Count the parts.
2. Every word on the sprite (name tags, signs, shirts) letter by letter against the doc, or absent.
3. West-facing battle pose as the pattern requires; reads clearly as the facing direction.
4. Anatomy matches the design (limb counts as designed, no fused or missing parts, no accidental extra limbs).
5. Canvas and scale: the size the pattern states; the enemy sits on the shadow or floor line and sits at the scale of its class; a boss reads bigger than a regular.
6. Alpha: clean outline, no matte halo, no leftover background, nothing cut off at the edge.
7. Palette and shading consistent with the other battle sprites; palette swaps change only the colours the doc names, and each swap is distinct at a glance.
8. Silhouette reads at battle size against the Arcade battle backdrops (test on each).
9. It reads as a parody of its theme at a glance and is not generic, corporate or professional; the joke is not explained by the image.
10. No real place names, no nudity, no mascot, no pet as an ally. Real brands keep real names.
11. Sanitising check: nothing the doc makes seedy or scandalous is cleaned up.
12. Every state the battle data asks for (idle, hit, defeat, attack poses) is present where the data lists them.

### P: dialogue portraits (cut from painted sources)
Reference: the G1-approved painted portrait or the model sheet, plus the dialogue data listing the expressions needed.
1. Same character as the approved source: face features, hair, outfit items, colours. Count the items.
2. Crop and framing match the dialogue spec (bust or head-and-shoulders, safe margins, eyes at the stated height). The face is not cut off; the crop is not stretched or squeezed.
3. Expression set: every expression the dialogue data names exists, each is readable and distinct from the others at the dialogue box size. Bros stay sincere doofuses: never smug, clever, afraid or disgusted.
4. Face detail at the G1 bar: open eyes with lids, irises and catchlights, defined nose, mouth and teeth, skin texture. Not airbrushed.
5. Text on the portrait (hat patches, name tags) letter by letter against the doc.
6. Alpha or background: as the spec states, clean edge, no matte halo, identical across the set so swaps do not jump.
7. Consistent position and scale across expressions: flicking between them does not move the face.
8. Size: native size or an exact integer scale; no unjustified upscaling or blur.
9. Reads at the dialogue box's real size with the box frame on top.
10. Nothing sanitises the character or contradicts the doc.

### T: tilesets, street kits and 3D kit modules
Reference: the tileset spec or kit manifest (`3D_Asset_Manifest_Template.md` for 3D), plus one approved plate for the area's look.
1. Every tile or module in the manifest exists; none is extra. Count them.
2. Tile size, grid and padding match the spec. Tiles are exactly the stated pixel size with no bleed between neighbours and (for atlases) a margin or extrusion where the engine needs it.
3. Seams: tiles that must tile do tile, horizontally and vertically, shown on a 3x3 repeat. Autotile or transition tiles join their neighbours without a visible edge.
4. Perspective and camera: all tiles match the fixed tilt camera (about 30 to 40 degrees); no tile drawn from a different angle.
5. Palette: the area's hex values from its doc dominate; no invented colour families; lighting is neutral enough to be relit by the scene (no baked golden hour).
6. Variation: ground and wall tiles come with enough variants that a 20x20 area shows no obvious repeat.
7. Collision and walkability intent: walkable and blocking tiles are visually distinguishable, and the manifest's flags match what is drawn.
8. 3D modules: scale in metres matches the manifest; pivots on the stated corner; modules snap to each other with no gap or overlap; kit is reused rather than regenerated (Checklist M item 4).
9. Parody and seediness: the kit carries the area's theme (graffiti, trash, signage as props where the doc says), not generic fantasy-town tiles. No real place names or text unless doc text.
10. Not a look-alike of the existing tilesets of other cities; distinct material and shape vocabulary.
11. Distress left for the author's hand-paint on 3D surfaces (`3d_asset_rules.md`).

### C: 2D cut-outs (interactables, pickups, props, prop kits and states)
Reference: the plan's list (B) asset requirement, the clean plate it sits on, and the interactions JSON entry.
1. The asset is exactly the item on list (B): right object, right states. Cabinet, counter, closet and shadow-switch kits include every state the interactions list (closed, open, lit, off, broken, and so on).
2. Perspective and lighting match the clean plate it is composited on: same camera angle, same light direction and colour; the composite shows no seam.
3. Scale: its size relative to the plate and to a bro (height_m) is plausible and consistent across the set.
4. Alpha: clean cut, no halo or leftover background; the shadow sits on its own layer if the spec says so.
5. Anchor: origin and interaction point at the position the interactions JSON uses; collision footprint is drawn or given.
6. Text on it letter by letter against doc text, or absent.
7. State pairs register to each other: switching states does not shift the silhouette base by even 1 px unless the animation requires it.
8. Style matches the plate: painterly HD-2D, same brush weight; not photoreal, not flat vector; no hand-painted distress where the author hand-paints it.
9. It reads as an interactable at game size (a visible affordance the design allows, with no UI-type arrow or sparkle painted in).
10. Pickups and junk items carry their funny item name and the doc's visual joke (see the junk-items ruling); nothing corporate or neutral.
11. No people painted in, no mascots, no nudity, no real place names.

### S: audio (ElevenLabs SFX and other sound)
A blind reviewer cannot hear. Gate S therefore runs in two parts, both blind: (S-a) a fresh agent reads a cue sheet generated from the file (duration, sample rate, channels, peak and RMS in dBFS, leading and trailing silence, spectrogram image, loop point check) against the spec; (S-b) RETIRED by the author 2026-11-14 (Desk Eurobound-lrg5-q2: "The agent's check is enough; I'll hear them in game"): S passes on S-a alone; the author hears sounds in game. Reference: the sound's doc line or the cue request.
1. Format: the file type and sample rate the project uses (`.ogg`, 44.1 or 48 kHz as the audio spec states); mono for positional sounds, stereo only where specified. No clipping (true peak at or below -1 dBFS).
2. Duration is inside the brief's range; no more than 50 ms of leading silence and no clipped tail; fade-out present where the sound is not a hard stop.
3. Loudness: peak and RMS within +/-3 dB of the project's reference cue for its class (UI, pickup, jingle, ambience).
4. Loopers: first and last samples match (zero crossing or a crossfade); the spectrogram shows no click at the seam.
5. The spectrogram matches the described sound: for a chime, tonal peaks and a decay; for a beep, a single band; for an impact, a broadband transient. A mismatch to the brief is a fail.
6. Not a duplicate or near-duplicate of an existing cue (spectral and duration comparison against `game/assets/audio/`).
7. Tone: the brief's tone words (for example "uh-oh", "success chime") are met; the cue is not corporate or generic stock. Judged by the blind agent from the cue sheet and the brief (S-b retired, lrg5-q2).
8. No lyrics, spoken words or sampled copyrighted music except where the doc names a real song or title (real titles keep real names); any voice line's text is exact doc text.
9. Naming: snake_case, location folder as in `game/assets/audio/<location>/`, an `.import` present only after the editor creates it (never hand-written).
10. Content: nothing sanitised; adult themes stay at full strength.

---

## 4. Wiring (not done here, needs the owner)
- Add an entry for each new gate id to the reviewer reply in `dev/asset_team/QC.md` (A-gates) and `Tools/char3d/QC.md` (G-gates): only the pointer sections were added in this job.
- Extend `Tools/critic_loop` with per-scene shot lists as locations are wired (A5).
- Gate E, P, C and T need the item names for qc_log lines; use the asset id as `item`.
