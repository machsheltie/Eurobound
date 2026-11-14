# PNG Assets Template

**Purpose:** Standardized art specification for every location. One of these files is MANDATORY per location (see `location_validation_template.md`). Every section below is REQUIRED; a PNG Assets file is not complete until all of them are filled in.

**Layout (author ruling on Eurobound-a8cm, 2026-11-12, verbatim: "Update the template to the Debaucheryville layout: HD-2D sheet sections first, sprite-sheet detail beneath, named <Location>_Complete_PNG_Asset_Requirements.md"):** one file per location. The Painterly HD-2D sheet comes first and is the spec of record. The older pixel-coordinate sprite-sheet spec sits beneath it under `## Legacy sprite-sheet detail`. Where the two disagree, the HD-2D sheet wins.

**File naming:** `[Location_Name]_Complete_PNG_Asset_Requirements.md` (e.g. `Shadow_Exchange_Complete_PNG_Asset_Requirements.md`)
**Save location:** `design/worlds/[city]/PNG_Assets/`
**Finished example:** `design/worlds/debaucheryville/PNG_Assets/Shadow_Exchange_Complete_PNG_Asset_Requirements.md`

**Conventions:**
- **PNG_Assets specs are authoritative over location profiles for sprite filenames, dimensions, and sheet membership.** This file is the artist's delivery contract; where a location profile or NPC profile disagrees with it, the spec wins and the profile is stale and must be corrected.
- Location ID format: `world_area_type_##` (e.g. `debaucheryville_clocktower_arcade_01`)
- All PNG filenames and asset IDs: `snake_case`, all lowercase
- Every asset ID in the Required PNG Assets table also appears in `design/worlds/[city]/sprite_mapping/[location_slug]_sprite_mapping.json`; every node ID matches the location's nodes and interactions JSON
- Legacy section only: all coordinates top-left origin (0,0), listed as `(x, y)` with `WxH` size; sprite sheet section headers pick a fitting emoji per sheet (🏪 🕹️ 👥 ✨ 🎮 etc.); animation timing in seconds (not just frames)

Copy everything below the line into the new file and replace the bracketed placeholders.

---

# [Location Name] - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `world_area_type_##`
- **Authoritative slug:** `[location_slug]`
- **Engine:** Godot 4.7
- **Pipeline:** [Painterly HD-2D painted faces, depth cards, cutout/billboard props, emission masks and state overlays; list what this location uses]
- **Visual target:** [One sentence: what the place looks like and the satirical point it makes]
- [Optional extra rows the location needs, e.g. **Source boundary:**, **Tour reward rule:**, **Purpose:**]

## Resolution and Frame Layout

Every required PNG uses one of these production classes; do not infer canvas size from the visible subject:

<!-- This table is identical in every finished Debaucheryville sheet. Copy it as written; change a row only if the location's sprite mapping overrides it, and say so in the row. -->

| Asset role | Resolution class | Frame layout |
|---|---:|---|
| Exterior, threshold or full interior scene plate | 2048x1152 px | Single 16:9 frame; provide clean plate and separate depth cards |
| Node or landmark cutout | 1024x1024 px | Single transparent frame with 8 px safe padding |
| NPC or creature animation | 2048x512 px | Four 512x512 cells in one row: idle, talk, react, service/combat; 8 fps unless mapping overrides |
| Item, reward or inventory icon | 256x256 px | Single transparent frame with 16 px safe area |
| UI atlas | 2048x1024 px | Power-of-two atlas; label frame rectangles in delivery manifest |
| FX atlas | 2048x2048 px | 8x8 grid of 256x256 cells; unused cells transparent |
| Emission/occlusion mask | Match its source asset exactly | One grayscale mask per source frame; preserve frame order |

## Spatial Composition

[The walk through the location, in the order the player meets it, one numbered node per line. Bold the node's player-facing name.]

1. **[Entrance / exterior node]** — [What it looks like and what happens there]
2. **[Node]** — [Description]
3. **[Node]** — [Description]
4. **[Exit node]** — [Where it returns or leads]

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `[location_slug]_exterior` | `[location_slug]_exterior.png` | exterior/threshold painted layer | `[node_id]` |
| `[location_slug]_interior` | `[location_slug]_interior.png` | interior painted faces | `[node_id]` |
| `[location_slug]_node_[node_id]` | `[location_slug]_[node_id].png` | [landmark type: service / shop / quest / transition / exit] | `[node_id]` |
| `[location_slug]_npc_[npc_id]` | `[location_slug]_[npc_id].png` | character sprite | `[node_id]` |
| `[location_slug]_item_[item_id]` | `[location_slug]_[item_id]_icon.png` | item/UI icon | global |
| `[location_slug]_ui_[purpose]` | `[location_slug]_[purpose]_ui.png` | [UI role] | global |
| `[location_slug]_fx_atmosphere` | `[location_slug]_atmosphere_fx.png` | [FX overlays] | global |
| `[location_slug]_mask_emission` | `[location_slug]_emission_masks.png` | lighting masks | global |

## Asset Requirement List

**Rule (author, 2026-11-14, binding):** `design/style_guides/location_interactables_rule.md`. One row for each non-background item in the location's scene decomposition list (that list is in the location profile).

**Background plates are painted clean of anything in classes other than architectural shell.** Non-interactive props, interactive props, pickups/collectibles, NPC anchors, FX/VFX anchors and UI/trigger points are separate assets and are never painted into the plate.

| Asset name | Asset type | Reuse or unique | Collision | Interaction | State variations | Animation | Sound cue | Quest dependency | Inventory icon | Material set |
|---|---|---|---|---|---|---|---|---|---|---|
| `[asset_id]` | [non-interactive prop / interactive prop / pickup-collectible / NPC anchor / FX-VFX anchor / UI-trigger point] | [Reuse (from where) / Unique] | [Yes/No; collision or trigger shape] | [Yes/No; interaction ID] | [States, or "none"] | [Yes/No; what] | [Cue, or "none"] | [Quest ID, or "none"] | [Yes/No] | [Material set, or "none"] |

## State and Character Coverage

<!-- Finished sheets title this section for what it covers, e.g. "Character, Item, and State Coverage" or "Tour and Challenge States". -->

- **[NPC name]:** idle, talk, react and service/combat frames; [wardrobe and prop notes].
- **[Item name]:** inventory/service icon and acquired/disabled state.
- [Discovery states: hidden, hinted, discovered, permanently known, as applicable].
- [Base, active and completed states for each interactive system].

## Accessibility Assets

- [Reduced-motion / reduced-particle variant of each moving or flashing element].
- [Static alternative for each animated information display].
- [High-contrast variant of each confirmation or key interactive cue].
- [Subtitle or visual equivalent for each audio cue].
- Text/icon equivalents for audio and color-only cues.
- Clean plates beneath smoke, dust, glow and other overlays.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/[location_slug]_sprite_mapping.json`.
- [ ] Interactive states match `interactions/[location_slug]_interactions.json`.
- [ ] Transparent assets have clean alpha and 8 px atlas padding.
- [ ] Color, normal and emission-ready variants are supplied for painted faces.

---

## Legacy sprite-sheet detail (HD-2D sheet above is the spec of record)

> The pixel-coordinate sprite-sheet spec. Where anything in this section contradicts the HD-2D sheet above, the HD-2D sheet wins.

## 📋 Overview
[One-paragraph description of the location and what this document specifies — capture the location's satirical essence in a sentence.]

**Location ID:** `world_area_type_##`
**Theme:** [Brief thematic description / satirical target]
**Zone:** [District/area within the city]
**Hours:** [Operating hours or "Always accessible"]
**Primary Function:** [Shop / quest hub / puzzle / battle / exploration + key mechanics served]

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| [Primary name] | #HEXCODE | [Main surfaces] |
| [Secondary name] | #HEXCODE | [Accent elements] |
| [Accent 1 name] | #HEXCODE | [Highlights] |
| [Accent 2 name] | #HEXCODE | [Special effects] |
| [Night/alt name] | #HEXCODE | [Night scenes, alt states] |

---

## 📁 File Structure
```
assets/sprites/locations/[world]/[location_name]/
├── environment/
│   ├── [location]_tileset.png
│   ├── [location]_background.png
│   └── [location]_effects.png
├── npcs/
│   └── [npc_name].png
├── objects/
│   └── [object_name].png
├── effects/
│   └── [effect_name].png
└── ui/
    └── [ui_element].png
```

---

## 🏪 Sprite Sheet 1: [Sheet Name]
**File:** `[filename].png`
**Dimensions:** [Width]x[Height] pixels
**Color Palette:** [Hex codes specific to this sheet, if they differ from the global palette]

### [Category Name]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| [Element Name] | (x, y) | WxH | [What it is / state it shows] |

### [Category Name 2]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| [Element Name] | (x, y) | WxH | [Description] |

### Technical Notes:
- [Animation timing, blend modes, shader needs]
- [Special behaviors]
- [Performance considerations]

---

[Repeat the Sprite Sheet section for each sheet: environment/tileset, interactive objects, NPCs, effects/particles, UI. Number them sequentially. Typical locations need 5–13 sheets.]

---

## 🎬 Animation Specifications

### [Animation Name]:
- **Duration:** [X seconds total / cycle length]
- **Frames:** [N]
- **Pattern:** [Frame 1 → 2 → 3 → loop/hold]
- **Trigger:** [Constant / player action / timer / quest state]
- **Purpose:** [What atmosphere or feedback this creates]
- **Audio Sync:** [Sound cue and timing, or "None"]
- **Performance Optimization:** [Reduced version for low-end hardware, or "None needed"]

[Repeat for each animation.]

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| [Key interactive element outline/silhouette] | (x, y) | WxH | [Enhanced visibility version] |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| [Static/reduced-motion variant] | (x, y) | WxH | [Non-flashing, non-pulsing alternative] |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| [Sound visualization sprite] | (x, y) | WxH | [Audio-independent visual for each critical sound cue] |

### Colorblind Considerations:
- [Pattern/shape-based indicators wherever color codes meaning]
- [Clear focus/click targets for interactive elements]

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** [VRAM compression (S3TC/BPTC) — note any assets needing higher quality]
- **Fallback:** [PNG high quality for detail-critical assets]

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| [location]_environment | [tileset, background, props] | 1024x1024 |
| [location]_characters | [NPC sheets, expressions] | 512x512 |
| [location]_effects | [particles, UI, overlays] | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | [Full particles, all animations, shader effects] |
| Medium | [Reduced particle density, simplified effects] |
| Low | [Static elements, minimal particles, no shaders] |

### Performance Targets:
- **Target FPS:** [60]
- **Max Draw Calls:** [15 per frame]
- **Memory Footprint:** [XX MB maximum]
- **Particle Limit:** [20]

### Performance Notes:
- [Location-specific optimizations: on-demand loading, animation limits, crowd caps]

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- [Node types needed: TileMap, ParallaxBackground, CPUParticles2D (not GPU), shaders]
- [Special systems: state machines, random activation scripts, progressive states]

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| [Sprite/animation] | [Sound effect] | [On what frame/event] |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| [Quest name] | [Sprites involved] | [How/where they connect] |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| [Location name] | [Shared/connecting sprites] | [Visual/audio transition] |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "[One-line aesthetic statement]"
- **Color Mood:** [Dominant colors and what they evoke]
- **Lighting:** [Light sources, mood, day/night handling]
- **Texture:** [Surface qualities — decay, gloss, grime, etc.]

### Environmental Storytelling:
- [Key visual details that tell the location's story without dialogue]
- [Satirical elements integrated into the environment itself]

### Character Integration Notes:
- [NPC visual direction, positioning, rendering notes (translucency, outlines)]

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **[Element]** - [Why it's shareable]
2. **[Element]** - [Why it's shareable]
3. **[Element]** - [Why it's shareable]

### Quote Potential:
- "[Memorable NPC line or in-world text]"
- "[Memorable NPC line or in-world text]"

---

## 📋 Required PNG Files (N Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | [filename].png | WxH |
| 2 | [filename].png | WxH |

**Total Estimated Memory:** ~XX MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `[filename].png` (WxH)
- [ ] `[filename].png` (WxH)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet [+ parallax layer guide if applicable]

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] [Location-specific visual checks — key gags/elements read clearly]
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets
- [ ] Hidden areas/interactions have discoverable visual cues
- [ ] Performance optimized (CPU particles, atlas limits respected)
- [ ] Interactive elements clearly sized and readable for focus/click targeting
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅/❌ | [World name only] |
| Cultural Specificity | ✅/❌ | [Which culture/stereotype satirized] |
| Satire Sharp and Specific | ✅/❌ | [The bros' delusion AND the city's culture are both fair game — no punch-direction rules (author ruling 2026-08-03)] |
| Seedy Underbelly Present | ✅/❌ | [Vice/exploitation element] |
| Gameplay Value Established | ✅/❌ | [Mechanics served] |
| Technical Feasibility | ✅/❌ | [Optimization documented] |
| Performance Budget | ✅/❌ | [FPS, draw calls, memory] |
| Accessibility Features | ✅/❌ | [Visual audio cues included] |
| Crypto Conforms to Canon | ✅/❌ | [Any crypto art conforms to `design/economy/economy_system.md`; coins only from `design/economy/shitcoin_master_pool.md`] |
| Social Media Integration | ✅/❌ | [Viral moments identified] |

**[Closing paragraph: one bold statement summarizing what this location becomes for the player once assets are delivered.]**
