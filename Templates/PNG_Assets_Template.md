# PNG Assets Template

**Purpose:** Standardized art specification for every location. One of these files is MANDATORY per location (see `location_validation_template.md`). Every section below is REQUIRED — a PNG Assets file is not complete until all 14 sections are filled in.

**File naming:** `[Location_Name]_PNG_Assets.md` (e.g. `Euro_Ink_4_Less_PNG_Assets.md`)
**Save location:** `Design/World Design/[World]/PNG_Assets/`

**Conventions:**
- **PNG_Assets specs are authoritative over location profiles for sprite filenames, dimensions, and sheet membership.** This file is the artist's delivery contract; where a location profile or NPC profile disagrees with it, the spec wins and the profile is stale and must be corrected.
- Location ID format: `world_area_type_##` (e.g. `debaucheryville_clocktower_arcade_01`)
- All PNG filenames: `snake_case`, all lowercase
- All coordinates: top-left origin (0,0), listed as `(x, y)` with `WxH` size
- Sprite sheet section headers: pick a fitting emoji per sheet (🏪 🕹️ 👥 ✨ 🎮 etc.)
- Animation timing: specify in seconds (not just frames)

Copy everything below the line into the new file and replace the bracketed placeholders.

---

# [Location Name] - Complete PNG Asset Requirements

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
- **Mobile Optimization:** [Reduced version for low-end devices, or "None needed"]

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
- [Touch zones minimum 44px for interactive elements]

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** [PVRTC 4BPP / ASTC — note any assets needing higher quality]
- **Android:** [ETC2 with alpha]
- **Fallback:** [PNG high quality for detail-critical assets]

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| [location]_environment | [tileset, background, props] | 1024x1024 |
| [location]_characters | [NPC sheets, expressions] | 512x512 |
| [location]_effects | [particles, UI, overlays] | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

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
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅/❌ | [World name only] |
| Cultural Specificity | ✅/❌ | [Which culture/stereotype satirized] |
| Satirical Targets Appropriate | ✅/❌ | [Tourists/bros, not locals — punch up] |
| Seedy Underbelly Present | ✅/❌ | [Vice/exploitation element] |
| Gameplay Value Established | ✅/❌ | [Mechanics served] |
| Technical Feasibility | ✅/❌ | [Mobile optimization documented] |
| Mobile Performance Budget | ✅/❌ | [FPS, draw calls, memory] |
| Accessibility Features | ✅/❌ | [Visual audio cues included] |
| No Crypto Elements | ✅/❌ | [Unless established in source material] |
| Social Media Integration | ✅/❌ | [Viral moments identified] |

**[Closing paragraph: one bold statement summarizing what this location becomes for the player once assets are delivered.]**
