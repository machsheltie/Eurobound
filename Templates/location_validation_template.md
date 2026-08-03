# Location Profile Validation Checklist & Templates

## 🚨 **MANDATORY PRE-SUBMISSION CHECKLIST**

**Use this checklist for EVERY location profile before implementation:**

## **🚨 MANDATORY PRE-SUBMISSION CHECKLIST**

**Use this checklist for EVERY location profile before implementation:**

**⚠️ FOR EXISTING LOCATIONS: Complete preservation checklist above FIRST**

### **🔍 World Consistency Validation**

- [ ] **NO real city names used** (must use Debaucheryville, Sinfonia, Publandia only)
- [ ] **Satirical world names used consistently** throughout all descriptions
- [ ] **Cross-location references use satirical names**
- [ ] **Cultural elements reflect specific city stereotypes** (not generic European)
- [ ] **Location fits city's specific cultural satirical targets**
- [ ] **Environmental details support city's party culture themes**

#### **City-Specific Cultural Accuracy Requirements**
##### **Debaucheryville Locations Must Include:**
- [ ] **Underground nightlife scene details** (lighting, music, atmosphere)
- [ ] **Tourist party destination indicators** (overpriced items, tourist traps)
- [ ] **Digital nomad/backpacker culture references**
- [ ] **Post-communist architectural decay meets neon excess**
- [ ] **Scam vendor economy** (exploiting tourist desperation)

##### **Publandia Locations Must Include:**
- [ ] **Pub culture and drinking traditions** (authentic Irish elements)
- [ ] **Literary heritage references** (books, poets, writers)
- [ ] **Celtic cultural elements** (music, symbols, language)
- [ ] **University/student culture presence**
- [ ] **Weather-related atmospheric details** (rain, mist, cold)

##### **Sinfonia Locations Must Include:**
- [ ] **Classical music and opera culture** (instruments, performances)
- [ ] **Coffeehouse intellectual traditions** (chess, newspapers, debates)
- [ ] **Imperial history and architecture** (old-imperial grandeur consistent with the city's parody-target metadata — see the two-tier world-names rule)
- [ ] **Art museum and gallery aesthetic** (paintings, sculptures, cultural events)
- [ ] **Formal/high society etiquette expectations** (dress codes, manners)

### **📋 Location Design Completeness**

#### **Identity & Classification**
- [ ] **Location ID follows naming convention**: `world_area_type_##`
- [ ] **Display Name and Satirical Subtitle clearly defined**
- [ ] **World Location and Area Zone specified**
- [ ] **Location Type matches gameplay function**
- [ ] **Accessibility Requirements documented** (time locks, stat checks, item requirements)

#### **Visual & Atmospheric Design**
- [ ] **Exterior Description includes approach and entrance details**
- [ ] **Interior Visuals provide comprehensive sensory details**
- [ ] **Lighting specifications for on-screen visibility**
- [ ] **Color Palette with hex codes for key atmosphere colors**
- [ ] **Particle Effects and Environmental FX detailed**
- [ ] **Performance Optimization considerations noted** (draw calls, memory usage)

#### **Satirical Design Requirements**
- [ ] **Theme clearly defined and focused on specific cultural target**
- [ ] **Humor Style consistent with game tone**
- [ ] **Satirical Elements integrated into environment** (not just dialogue)
- [ ] **Social Media Moments identified** (screenshot opportunities, viral quotes)
- [ ] **Seedy underbelly element present** (vice, exploitation, corruption)
- [ ] **Cultural stereotypes handled with wit, not malice**

### **🎮 Gameplay Integration Validation**

#### **Mechanical Functionality**
- [ ] **Primary Function clearly defined** (shop, quest hub, puzzle, battle, exploration)
- [ ] **Secondary Functions documented** (couchsurf, selfie, item discovery)
- [ ] **Entry Requirements specified** (stats, items, time, previous locations)
- [ ] **Exit Conditions detailed** (completion requirements, progression locks)
- [ ] **Interactive Elements catalogued** (NPCs, objects, hidden areas)

#### **Economic Integration**
- [ ] **Shop Inventories balance risk/reward** (if applicable)
- [ ] **Currency Systems logical** (local currency, barter, special tokens)
- [ ] **Price Points reflect location's socioeconomic satire**
- [ ] **Post-Boss Unlocks provide meaningful progression**

#### **Quest & Progression Systems**
- [ ] **Quest Hooks identified and documented**
- [ ] **Couchsurf Integration planned** (trigger conditions, rewards)
- [ ] **Cross-Location Dependencies mapped** (unlocks, references, continuity)
- [ ] **Repeat Visit Value established** (changing content, new discoveries)

### **🔧 Technical Implementation Validation**

#### **Performance Standards**
- [ ] **Asset Count optimized** (sprite count, texture memory)
- [ ] **Animation Timing specified in seconds** (not frames)
- [ ] **Interactive Element Sizing appropriate** (clear focus/click targets)
- [ ] **Text Readability ensured** (contrast, font size, desktop viewing)
- [ ] **Performance Budget calculated** (draw calls, particles, audio)

#### **Audio Integration**
- [ ] **Ambient Audio specified** (background music, environmental sounds)
- [ ] **Interactive Audio defined** (button presses, object interactions)
- [ ] **Satirical Stingers identified** (comedy timing audio cues)
- [ ] **Audio Transitions planned** (enter/exit location, scene changes)

### **📄 Required File Generation Checklist**

**⚠️ MANDATORY: Every location MUST generate ALL of the following files:**

| File Type | Filename Pattern | Required? |
|-----------|------------------|-----------|
| **Location Profile** | `[location_name].md` | ✅ ALWAYS |
| **PNG Asset Requirements** | `[Location_Name]_PNG_Assets.md` | ✅ ALWAYS |
| **Core Data JSON** | `[location_name]_core.json` | ✅ ALWAYS |
| **NPCs JSON** | `[location_name]_npcs.json` | ✅ ALWAYS (even if empty array) |
| **Interactions JSON** | `[location_name]_interactions.json` | ✅ ALWAYS |
| **Environment JSON** | `[location_name]_environment.json` | ✅ ALWAYS |
| **Sprite Mapping JSON** | `[location_name]_sprite_mapping.json` | ✅ ALWAYS |
| **Location Nodes JSON** | `[location_name]_location_nodes.json` | ✅ ALWAYS |
| **Items JSON** | `[location_name]_items.json` | ⚠️ IF location has purchasable/findable items |

---

## **📚 Location Profile Template**

```markdown
# [Location Name]

*[Satirical subtitle that captures the location's essence]*

## Location Identity
- **Location ID**: `world_area_type_##`
- **Display Name**: [Full Location Name]
- **Satirical Subtitle**: [Tagline]
- **World Location**: [Debaucheryville/Publandia/Sinfonia]
- **Area Zone**: [Specific District]
- **Location Type**: [shop/quest_hub/puzzle/battle/exploration]

---

## Access & Requirements

### Entry Conditions
- **Time Restrictions**: [Hours or "Always accessible"]
- **Stat Requirements**: [Bravado/Charm/etc. minimums or "None"]
- **Item Requirements**: [Required items or "None"]
- **Previous Location Requirements**: [Prerequisite locations or "None"]
- **Special Conditions**: [Quest flags, status effects, or "None"]

### Exit Conditions
- **Normal Exit**: [How player leaves]
- **Completion Requirements**: [What must be done to progress]
- **Failure States**: [What happens if player fails]
- **Progressive Unlocks**: [What becomes available after completion]

---

## Visual Design

### Exterior Description
- **Approach**: [How player reaches location]
- **Entrance**: [Door, pathway, portal appearance]
- **Signage**: [Signs, markers, visual indicators]
- **Atmosphere**: [Weather, lighting, crowds]
- **Environmental Context**: [Surrounding area, neighboring locations]

### Interior Visuals
- **Layout**: [Room arrangement, size, flow]
- **Lighting**: [Light sources, shadows, mood]
- **Furniture & Props**: [Key objects and their arrangement]
- **Decorative Elements**: [Posters, art, environmental storytelling]
- **Atmospheric Effects**: [Smoke, particles, ambient motion]
- **Hidden Areas**: [Secret spots, easter eggs]

### Technical Specifications
- **Color Palette**: [Primary and accent hex codes]
- **Lighting Setup**: [Ambient color, intensity, sources]
- **Particle Systems**: [Smoke, glow, debris, etc.]
- **Animation Elements**: [Moving objects, flickering lights, ambient motion]
- **Performance Optimization**: [LOD settings, texture compression, draw call budget]

---

## Satirical Design

### Theme & Vibe
**Core Concept**: [One paragraph explaining the satirical target]

**The Irony**: [What makes this location funny/satirical]

### Cultural Targets
- **Primary Satirical Focus**: [Main target of humor]
- **Secondary Targets**: [Additional satirical elements]
- **Cultural Specificity**: [How it reflects the specific city]
- **Humor Approach**: [Comedy style and tone]
- **Sensitivity Considerations**: [How to punch up, not down]

### Seedy Underbelly Elements
- **Primary Vice**: [Main exploitation/corruption theme]
- **City-Specific Comedy Operations**: [How location creates comedy]
- **Buffoon Exploitation**: [How bros are made ridiculous]
- **Comedy of Errors**: [Slapstick and misunderstanding opportunities]
- **Consequence System**: [Embarrassing outcomes]

### Buffoon Delusion Scenarios
**What bros THINK is happening**: [Their delusional interpretation]

**What is ACTUALLY happening**: [The hilarious reality]

**Obvious signs they ignore**: [Visual/dialogue cues players see]

### Social Media Potential
- **Screenshot Opportunities**: [Visual moments worth sharing]
- **Quotable Moments**: [Memorable dialogue lines]
- **Easter Eggs**: [Hidden references]
- **Viral Content Hooks**: [Meme-worthy elements]

---

## Gameplay Mechanics

### Primary Functions
- **Core Purpose**: [Main gameplay reason]
- **Player Actions**: [What player can do]
- **Rewards Available**: [Items, progression, unlocks]
- **Risk/Reward Balance**: [Potential consequences]

### Interactive Elements
- **NPCs Present**: [Characters at location]
- **Objects & Items**: [Searchable, collectible, equipment]
- **Environmental Interactions**: [Buttons, switches, secrets]
- **Mini-Games**: [Puzzles, challenges, skill tests]

### Economic Integration
- **Shop Functionality**: [Items sold, services offered]
- **Currency Accepted**: [Gold, barter, special tokens]
- **Price Structure**: [Cost ranges and satirical pricing]
- **Economic Role**: [How location fits broader economy]

### Quest Integration
- **Quest Hub Role**: [Quests that start/center here]
- **Information Source**: [Clues, lore, hints available]
- **Meeting Point**: [Character meetup functions]
- **Objective Location**: [Quests requiring visits]

---

## NPCs

### [NPC Name]
- **Role**: [Function in location]
- **Appearance**: [Visual description]
- **Personality**: [Traits, speech patterns]
- **Key Dialogue**: [Sample lines]
- **Services/Function**: [What they provide]

[Repeat for each NPC]

---

## Audio Design

### Environmental Audio
- **Ambient Soundscape**: [Background audio]
- **Music Style**: [Genre, mood]
- **Audio Transitions**: [Enter/exit sounds]
- **Interactive Audio**: [Action sound effects]

### Comedy Audio Integration
- **Satirical Stingers**: [Comedic audio cues]
- **Character Voice Direction**: [How NPCs should sound]
- **Environmental Comedy**: [Funny ambient sounds]
- **Social Media Audio**: [Shareable sound moments]

---

## Connected Locations

### Directly Adjacent
[List connected locations with directions]

### Quest-Connected
[List locations connected via quests]

---

## Implementation Specifications

### Technical Requirements
- **Asset List**: [Sprites, textures needed]
- **Animation Requirements**: [Moving elements]
- **Performance Budget**: [FPS, memory, draw calls]
- **Platform Considerations**: [Desktop optimizations]

### State Tracking
```
location_state:
  - key_state_variable: type
  [etc.]
```

---

## Quality Assurance Checklist

### Pre-Implementation Review
- [ ] World consistency verified
- [ ] Cultural specificity confirmed
- [ ] Satirical targets appropriate
- [ ] Gameplay value established
- [ ] Technical feasibility confirmed
- [ ] No crypto elements (unless explicitly required)
- [ ] Seedy underbelly present

### Post-Implementation Testing
- [ ] Navigation tested
- [ ] Interactive elements functional
- [ ] Performance optimized
- [ ] Cultural sensitivity verified
- [ ] Cross-location integration confirmed
```

---

## **📂 Required JSON File Structure**

**⚠️ MANDATORY: Every location implementation must generate ALL of these files:**

### **1. Location Core Data** (`[location_name]_core.json`)

**Purpose**: Basic location identity, access requirements, visual theme, and state tracking.

```json
{
  "location_id": "world_area_type_##",
  "display_name": "Full Location Name",
  "satirical_subtitle": "Tagline description",
  "world": "satirical_world_name",
  "zone": "specific_district",
  "location_type": "shop/quest_hub/puzzle/battle/exploration",
  "sub_types": ["additional", "type", "tags"],
  
  "access": {
    "time_restrictions": {
      "always_accessible": true,
      "open_time": "HH:MM",
      "close_time": "HH:MM"
    },
    "stat_requirements": {"bravado": 2, "charm": 1},
    "item_requirements": ["bottle_opener_keychain"],
    "previous_locations": ["other_location_id"],
    "special_conditions": {
      "required_state": "state_name",
      "drunk_status": false
    }
  },
  
  "exits": [
    {
      "exit_id": "to_destination",
      "destination": "destination_location_id",
      "direction": "cardinal_or_descriptive",
      "requirements": null
    }
  ],
  
  "atmosphere": {
    "primary_mood": "mood_descriptor",
    "secondary_moods": ["mood1", "mood2"],
    "crowd_level": "empty/low/medium/high/very_high",
    "noise_level": "silent/low/medium/high",
    "lighting": {
      "day": "lighting_description",
      "night": "lighting_description"
    }
  },
  
  "visual_theme": {
    "primary_colors": ["#HEXCODE", "#HEXCODE"],
    "accent_colors": ["#HEXCODE"],
    "architectural_style": "style_description",
    "key_visual_elements": ["element1", "element2"]
  },
  
  "satirical_design": {
    "primary_target": "main_satirical_focus",
    "secondary_targets": ["target1", "target2"],
    "buffoon_delusion": {
      "what_bros_think": "their interpretation",
      "what_actually_happens": "reality"
    }
  },
  
  "state_tracking": {
    "visited": false,
    "quest_complete": false,
    "custom_state_var": "value"
  },
  
  "performance": {
    "target_fps": 60,
    "max_draw_calls": 15,
    "memory_budget_mb": 30,
    "particle_limit": 20
  }
}
```

---

### **2. NPCs** (`[location_name]_npcs.json`)

**Purpose**: All NPCs at this location with full profiles, dialogue, and behaviors.

```json
{
  "location_id": "world_area_type_##",
  
  "npcs": [
    {
      "npc_id": "npc_unique_id_01",
      "display_name": "NPC Display Name",
      "full_name": "Full Character Name",
      "npc_type": "vendor/quest_giver/ambient/service_provider/boss",
      "role": "specific_function",
      "location_zone": "where_in_location",
      "behavior": "stationary/roaming/patrol/triggered",
      
      "appearance": {
        "age": 35,
        "build": "description",
        "clothing": "outfit_description",
        "accessories": ["item1", "item2"],
        "notable_features": ["feature1", "feature2"]
      },
      
      "personality": {
        "traits": ["trait1", "trait2", "trait3"],
        "speech_pattern": "description",
        "energy": "high/medium/low"
      },
      
      "dialogue": {
        "greeting": "Hello dialogue",
        "idle_chatter": ["line1", "line2"],
        "transaction": "Purchase dialogue",
        "farewell": "Goodbye dialogue",
        "special_triggers": {
          "trigger_name": "triggered dialogue"
        }
      },
      
      "services": [
        {
          "service_id": "service_name",
          "price": 50,
          "description": "What this service does"
        }
      ],
      
      "schedule": {
        "present_hours": "10:00-22:00",
        "absent_reason": "Why not present at other times"
      },
      
      "quest_connections": [
        {
          "quest_id": "quest_id",
          "role": "quest_giver/target/helper"
        }
      ],
      
      "voice_direction": "How this NPC should sound",
      "sprite_sheet": "npc_sprite_filename.png"
    }
  ],
  
  "ambient_npcs": [
    {
      "npc_id": "ambient_npc_01",
      "display_name": "Ambient Character",
      "npc_type": "ambient",
      "behavior": "crowd_member/background_action",
      "count_range": "3-5",
      "dialogue": {
        "overheard": ["background line 1", "background line 2"]
      }
    }
  ],
  
  "npc_interactions": {
    "npc_to_npc": {
      "description": "How NPCs interact with each other"
    }
  }
}
```

---

### **3. Interactions** (`[location_name]_interactions.json`)

**Purpose**: Events, dialogue sequences, interactive objects, and gameplay triggers.

```json
{
  "location_id": "world_area_type_##",
  
  "events": [
    {
      "event_id": "event_unique_id",
      "display_name": "Event Name",
      "event_type": "scheduled/triggered/dialogue_sequence/mini_game",
      "trigger": {
        "type": "location_entry/time_based/state_change/interaction",
        "condition": "specific_trigger_condition"
      },
      "duration_seconds": 60,
      "sequence": [
        {
          "phase": "phase_name",
          "duration_seconds": 10,
          "description": "What happens",
          "speaker": "character_name",
          "dialogue": "Spoken line",
          "animation": "animation_name",
          "audio": "audio_cue"
        }
      ],
      "post_event_effects": [
        {
          "effect": "set_state/unlock/trigger",
          "target": "state_or_location",
          "value": true
        }
      ]
    }
  ],
  
  "interactive_objects": [
    {
      "object_id": "object_unique_id",
      "type": "examinable/container/switch/usable",
      "interaction_text": "Examine the thing",
      "description": "What player sees/gets",
      "rewards": [
        {
          "item": "item_id",
          "probability": 0.7
        }
      ],
      "requirements": {
        "stat": "bravado",
        "minimum": 3
      },
      "animation": "interaction_animation",
      "audio_cue": "sound_effect",
      "one_time_only": false,
      "easter_egg": {
        "trigger": "condition",
        "reveal": "hidden content"
      }
    }
  ],
  
  "environmental_interactions": [
    {
      "trigger_id": "trigger_unique_id",
      "type": "switch/pressure_plate/proximity",
      "requirement": {"stat": "bravado", "minimum": 3},
      "effect": "unlock_secret_area",
      "audio_cue": "secret_door_open"
    }
  ],
  
  "mini_games": [
    {
      "mini_game_id": "game_unique_id",
      "display_name": "Mini Game Name",
      "type": "timing/rhythm/puzzle/skill",
      "duration_seconds": 120,
      "mechanics": {
        "objective": "What player must do",
        "controls": "How to play",
        "scoring": "How success is measured"
      },
      "rewards": {
        "success": "reward_description",
        "failure": "consequence_description"
      }
    }
  ],
  
  "return_visit_changes": {
    "visit_2": {
      "new_dialogue": true,
      "new_items_available": ["item_id"],
      "npc_recognition": true
    }
  },
  
  "narrator_commentary": {
    "on_entering": "Narrator line when entering",
    "on_key_moment": "Narrator line at important moment",
    "on_exit": "Narrator line when leaving"
  }
}
```

---

### **4. Environment** (`[location_name]_environment.json`)

**Purpose**: Audio, lighting, particles, weather, time-of-day changes, and atmospheric systems.

```json
{
  "location_id": "world_area_type_##",
  
  "ambient_audio": {
    "background_music": "music_file.ogg",
    "music_style": "genre_description",
    "environmental_sounds": [
      "sound1_description",
      "sound2_description"
    ],
    "audio_transitions": {
      "enter": "fade_in_2s",
      "exit": "fade_out_1s"
    },
    "interactive_audio": {
      "action_name": "sound_file.ogg"
    },
    "comedy_stingers": {
      "moment_name": "stinger_file.ogg"
    }
  },
  
  "status_effects": {
    "environmental_buffs": ["buff_name"],
    "atmospheric_debuffs": ["debuff_name"],
    "location_specific_states": {
      "state_name": {
        "trigger": "condition",
        "duration_minutes": 30,
        "effects": {
          "stat_modifier": 1.2
        }
      }
    },
    "recovery_options": ["recovery_method"]
  },
  
  "couchsurf_integration": {
    "available": true,
    "host_npc": "npc_id",
    "trigger_conditions": ["condition1", "condition2"],
    "unique_benefits": ["benefit1"],
    "narrative_progression": "story_unlock"
  },
  
  "time_of_day_changes": {
    "morning": {
      "lighting": "description",
      "crowd_density": "level",
      "special_notes": "unique_features"
    },
    "afternoon": {},
    "evening": {},
    "night": {},
    "late_night": {}
  },
  
  "weather_effects": {
    "clear": {
      "modifier": 1.0,
      "description": "normal"
    },
    "rain": {
      "modifier": 0.7,
      "audio": "rain_sound.ogg",
      "visual": "rain_particles"
    }
  },
  
  "particle_effects": {
    "effect_name": {
      "type": "ambient/burst/stream",
      "source": "emission_point",
      "color": "#HEXCODE",
      "density": "sparse/medium/dense",
      "movement": "pattern_description"
    }
  },
  
  "lighting_system": {
    "primary_ambient": {
      "color": "#HEXCODE",
      "intensity": 0.8,
      "coverage": "entire_location"
    },
    "accent_lighting": {
      "affected_areas": ["area1", "area2"],
      "color": "#HEXCODE",
      "flicker_pattern": "description"
    },
    "point_lights": [
      {
        "source": "light_source_name",
        "color": "#HEXCODE",
        "radius": 64,
        "intensity": 0.8
      }
    ]
  },
  
  "environmental_storytelling": {
    "permanent_details": [
      {
        "element": "detail_name",
        "description": "what it shows",
        "location": "where_in_space"
      }
    ],
    "dynamic_details": [
      {
        "element": "detail_name",
        "description": "what changes",
        "visibility": "trigger_condition"
      }
    ]
  }
}
```

---

### **5. Items** (`[location_name]_items.json`)

**Purpose**: All purchasable, findable, or quest items at this location.

**⚠️ Required IF location has any items. Skip only for pure exploration locations.**

```json
{
  "location_id": "world_area_type_##",
  "item_category": "shop_inventory/quest_items/findable/scam_merchandise",
  
  "items": [
    {
      "item_id": "item_unique_id",
      "display_name": "Item Display Name",
      "item_type": "consumable/equipment/quest_item/junk/throwable/cosmetic",
      "rarity": "common/uncommon/rare/unique",
      "vendor": "vendor_npc_id",
      "price": 50,
      "actual_value": 5,
      "scam_level": "none/low/medium/high/complete",
      
      "description": {
        "player_sees": "(What player/narrator knows)",
        "bros_see": "What the bros believe"
      },
      
      "effects": {
        "stat_modifier": {"bravado": 1, "charm": -1},
        "status_applied": "status_effect_name",
        "special_effect": "unique_mechanic"
      },
      
      "equipment_slot": "head/torso/hands/feet/accessory",
      
      "consumable_details": {
        "uses": 1,
        "duration_minutes": 30
      },
      
      "quest_connection": {
        "quest_id": "connected_quest",
        "required_for": "quest_phase"
      },
      
      "accumulation": {
        "visible_in_hostel": true,
        "max_displayed": 6
      },
      
      "sprite": "item_sprite_filename.png"
    }
  ],
  
  "shop_economics": {
    "total_items_available": 5,
    "price_range": {"min": 10, "max": 200},
    "actual_value_total": 50,
    "markup_percentage": 400,
    "currency_accepted": "gold"
  },
  
  "hidden_items": [
    {
      "item_id": "hidden_item_id",
      "location_hint": "Where to find it",
      "discovery_method": "How to get it",
      "rarity": "rare"
    }
  ]
}
```

---

### **6. Sprite Mapping** (`[location_name]_sprite_mapping.json`)

**Purpose**: Exact pixel coordinates for all sprites, animation sequences, texture atlases.

```json
{
  "location_id": "world_area_type_##",
  
  "sprite_sheets": {
    "main_tileset": {
      "file": "location_name_tileset.png",
      "dimensions": {"width": 1024, "height": 1024},
      "tile_size": {"width": 32, "height": 32},
      "sections": {
        "floor_tiles": {"x": 0, "y": 0, "width": 256, "height": 256},
        "wall_tiles": {"x": 256, "y": 0, "width": 256, "height": 256},
        "ceiling_tiles": {"x": 512, "y": 0, "width": 256, "height": 256},
        "decorative_tiles": {"x": 768, "y": 0, "width": 256, "height": 256}
      },
      "special_tiles": {
        "interactive_highlight": {"x": 0, "y": 256, "width": 128, "height": 128},
        "damaged_variants": {"x": 128, "y": 256, "width": 128, "height": 128},
        "glow_overlay": {"x": 256, "y": 256, "width": 128, "height": 128}
      }
    },
    "interactive_objects": {
      "file": "location_interactive_spritesheet.png",
      "dimensions": {"width": 2048, "height": 1024},
      "object_size": {"width": 64, "height": 96},
      "objects": {
        "object_name": {
          "idle": {"x": 0, "y": 0, "width": 64, "height": 96},
          "active": {"x": 64, "y": 0, "width": 64, "height": 96},
          "broken": {"x": 128, "y": 0, "width": 64, "height": 96}
        }
      }
    },
    "environmental_elements": {
      "file": "location_environmental_effects.png",
      "dimensions": {"width": 1024, "height": 512},
      "elements": {
        "element_name": {
          "base": {"x": 0, "y": 0, "width": 192, "height": 96},
          "animation": [
            {"x": 192, "y": 0, "width": 192, "height": 96, "frame": 1},
            {"x": 384, "y": 0, "width": 192, "height": 96, "frame": 2}
          ],
          "animation_timing": {"fps": 8, "loop": true}
        }
      }
    },
    "npc_sprites": {
      "file": "location_npcs_spritesheet.png",
      "dimensions": {"width": 512, "height": 384},
      "characters": {
        "npc_name": {
          "idle": {"x": 0, "y": 0, "width": 64, "height": 96},
          "talking": {"x": 64, "y": 0, "width": 64, "height": 96},
          "action": {"x": 128, "y": 0, "width": 64, "height": 96}
        }
      }
    },
    "background_parallax": {
      "file": "location_parallax_background.png",
      "dimensions": {"width": 1024, "height": 512},
      "layers": {
        "far_background": {"x": 0, "y": 0, "width": 256, "height": 512, "scroll_speed": 0.1},
        "mid_background": {"x": 256, "y": 0, "width": 256, "height": 512, "scroll_speed": 0.3},
        "near_background": {"x": 512, "y": 0, "width": 256, "height": 512, "scroll_speed": 0.5}
      }
    }
  },
  
  "animation_sequences": {
    "sequence_name": {
      "sprite_source": "sheet_name",
      "frames": 8,
      "duration_seconds": 2,
      "loop": true,
      "timing": {"fps": 4}
    }
  },
  
  "lighting_effects": {
    "primary_ambient": {
      "color": "#HEXCODE",
      "intensity": 0.8,
      "reactive_sprites": ["sprite_list"]
    },
    "accent_lighting": {
      "affected_sprites": ["sprite_list"],
      "flicker_pattern": "pattern_description",
      "color": "#HEXCODE"
    }
  },
  
  "particle_effect_sprites": {
    "particle_name": {
      "sprite_sheet": "effects_sheet.png",
      "coordinates": {"x": 0, "y": 0, "width": 32, "height": 32},
      "frames": 4,
      "animation_speed": "0.3_seconds_per_frame"
    }
  },
  
  "ui_elements": {
    "location_specific_ui": {
      "background": {"x": 0, "y": 0, "width": 128, "height": 32},
      "icon": {"x": 128, "y": 0, "width": 16, "height": 16}
    }
  },
  
  "performance_optimization": {
    "texture_atlases": [
      {
        "name": "location_main_atlas",
        "files": ["tileset.png", "interactive.png"],
        "max_size": "2048x2048",
        "compression": "S3TC_BPTC_desktop"
      }
    ],
    "lod_levels": {
      "high": "full_effects",
      "medium": "reduced_particles",
      "low": "minimal_effects"
    }
  }
}
```

---

### **7. Location Nodes** (`[location_name]_location_nodes.json`)

**Purpose**: Node connections, interior features, gameplay functions, quest hooks.

```json
{
  "locations": [
    {
      "name": "Location Display Name",
      "tag_id": "location_snake_case_id",
      "region": "World Name",
      "exterior": {
        "description": "Detailed exterior description including visual landmarks, atmospheric details, and approach experience.",
        "entry_condition": "Stat requirement, item requirement, time restriction, or 'Accessible anytime'"
      },
      "interior": {
        "theme": "Core visual/atmospheric theme in one descriptive phrase",
        "features": [
          "entry_point",
          "primary_function_node",
          "quest_npc: npc_name",
          "shop_node: shop_type",
          "couchsurf_trigger",
          "puzzle_node: puzzle_type",
          "dungeon_entrance: connected_location",
          "selfie_prop: prop_description",
          "npc_group: group_type",
          "event_hook: event_name",
          "mini_game: game_name",
          "examinable: object_name",
          "hidden_area: unlock_condition"
        ]
      },
      "functions": [
        "Primary gameplay function",
        "Secondary gameplay function",
        "Tertiary gameplay function",
        "Special unlock or progression function"
      ]
    }
  ],
  
  "node_connections": {
    "location_tag_id": {
      "connects_to": [
        {
          "destination": "destination_location_id",
          "direction": "cardinal_or_descriptive",
          "requirements": null,
          "transition_type": "normal/quest_unlock/paid"
        }
      ],
      "quest_connections": [
        {
          "quest_id": "quest_id",
          "role": "quest_origin/quest_location/quest_destination",
          "npc_trigger": "npc_id"
        }
      ],
      "unlocks_at": [
        {
          "destination": "unlocked_location",
          "condition": "unlock_condition",
          "state_change": "state_variable"
        }
      ]
    }
  },
  
  "feature_details": {
    "feature_tag": {
      "type": "feature_type",
      "description": "Detailed description of what this feature does",
      "mechanics": "How it works gameplay-wise"
    }
  },
  
  "ambient_npcs": {
    "npc_group_name": {
      "count_range": "3-5",
      "types": ["type1", "type2"],
      "behavior": "behavior_pattern"
    }
  }
}
```

---

**Location Node Feature Types Reference:**

| Feature Type | Format | Description |
|--------------|--------|-------------|
| `entry_point` | `entry_point` | Standard location entry marker |
| `quest_npc` | `quest_npc: npc_id` | NPC that gives or advances quests |
| `couchsurf_trigger` | `couchsurf_trigger` or `couchsurf_trigger: host_name` | Couchsurfing stay location |
| `puzzle_node` | `puzzle_node: puzzle_type` | Interactive puzzle element |
| `dungeon_entrance` | `dungeon_entrance: destination_id` | Connection to dungeon location |
| `selfie_prop` | `selfie_prop: prop_description` | Photo opportunity object |
| `npc_group` | `npc_group: group_type` | Ambient NPC grouping |
| `event_hook` | `event_hook: event_name` | Triggered event location |
| `shop_node` | `shop_node: shop_type` | Purchasable items location |
| `boss_arena` | `boss_arena: boss_id` | Boss encounter zone |
| `mini_mob` | `mini_mob: enemy_type` | Minor enemy encounter |
| `boss` | `boss: boss_id` | Major boss encounter |
| `save_point` | `save_point` | Manual save location |
| `fast_travel` | `fast_travel` | Fast travel node |
| `hidden_area` | `hidden_area: unlock_condition` | Secret area access |
| `mini_game` | `mini_game: game_name` | Interactive mini-game |
| `examinable` | `examinable: object_name` | Inspectable object |

---

## **🖼️ PNG Asset Requirements Document**

**⚠️ MANDATORY: Generate a separate PNG asset requirements markdown file for EACH location.**

### File Naming Convention
`[Location_Name]_PNG_Assets.md`

Example: `Euro_Ink_4_Less_PNG_Assets.md`

### Purpose
This document serves as the complete art specification for each location, providing:
- Exact pixel coordinates for all sprites
- Color palette hex codes
- Animation timing specifications
- Technical integration notes
- Quality assurance checklists

---

### **PNG Asset Requirements Template**

```markdown
# [Location Name] - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `world_area_type_##`  
**Theme:** [Brief thematic description]  
**Zone:** [Area within city]  
**Hours:** [Operating hours if applicable]

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Primary | #HEXCODE | Main surfaces |
| Secondary | #HEXCODE | Accent elements |
| Accent 1 | #HEXCODE | Highlights |
| Accent 2 | #HEXCODE | Special effects |

---

## 📁 File Structure
```
assets/sprites/locations/[world]/[location_name]/
├── environment/
│   ├── [location]_tileset.png
│   ├── [location]_background.png
│   └── [location]_effects.png
├── npcs/
│   ├── [npc_name].png
│   └── [npc_name].png
├── objects/
│   ├── [object_name].png
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

### [Category]:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Element Name | (x, y) | WxH | Description |

### Technical Notes:
- [Animation timing]
- [Special behaviors]
- [Performance considerations]

---

[Repeat for each sprite sheet]

---

## 🎬 Animation Specifications

### [Animation Name]:
- **Duration:** X seconds
- **Frames:** N
- **Loop:** Yes/No
- **Timing:** [Pattern]

---

## 🖥️ Performance & Assets

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| Atlas Name | Files included | 2048x2048 |

### Performance Notes:
- [Optimization considerations]

---

## 📋 Required PNG Files (N Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | filename.png | WxH |

**Total Estimated Memory:** ~XXmb

---

## ✅ Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅/❌ |
| Cultural Specificity | ✅/❌ |
| Satirical Targets | ✅/❌ |
| Gameplay Value | ✅/❌ |
| No Crypto Elements | ✅/❌ |
| Performance Optimization | ✅/❌ |
```

---

## **📊 File Generation Summary**

### **Required Files Per Location**

| # | File Type | Filename | Always Required? |
|---|-----------|----------|------------------|
| 1 | Location Profile | `[location_name].md` | ✅ YES |
| 2 | PNG Assets | `[Location_Name]_PNG_Assets.md` | ✅ YES |
| 3 | Core JSON | `[location_name]_core.json` | ✅ YES |
| 4 | NPCs JSON | `[location_name]_npcs.json` | ✅ YES |
| 5 | Interactions JSON | `[location_name]_interactions.json` | ✅ YES |
| 6 | Environment JSON | `[location_name]_environment.json` | ✅ YES |
| 7 | Sprite Mapping JSON | `[location_name]_sprite_mapping.json` | ✅ YES |
| 8 | Location Nodes JSON | `[location_name]_location_nodes.json` | ✅ YES |
| 9 | Items JSON | `[location_name]_items.json` | ⚠️ IF has items |

**Minimum files per location: 8**
**Maximum files per location: 9**

---

## **⚠️ CRYPTO WARNING - CRITICAL**
- [ ] **Crypto elements ONLY if already established** in existing location description or specifically requested by user
- [ ] **NO automatic crypto assumptions** - crypto is minor gag used sparingly (2% of game maximum)  
- [ ] **Focus on city-specific vices instead** (absinthe, pub culture, opera pretension, mystery meat, health violations)
- [ ] **Target aging frat bro psychology and tourist exploitation** - NOT tech culture unless location specifically calls for it
- [ ] **DEFAULT: Assume NO crypto involvement** unless explicitly stated in source material

---

## **🎯 Satirical Design Guidelines**

### **🍺 BUFFOON DELUSION SCENARIOS (Required for Vice Venues)**

> **⚠️ READ FIRST: `Design/Character Profiles/bros_core_principle.md`**
> The bros went to Europe **seeking debauchery** — the sex, drugs, drinking, partying, sex clubs, sex workers, the whole menu, on every front, as much as possible. They are not innocent tourists, they are not afraid, and the cities deliver in spades. Their delusion is about **themselves** (that they can handle it), never about what Europe is. Never write them horrified, frightened, ashamed, or corrupted.
> **This game is RIDICULOUS SATIRE and MA-rated. It is not safe, not boring, not mundane, not corporate, and nobody in it is a sober realistic professional.** Everyone is absurd — vendors and locals as much as the bros; there is no straight man. The bros GET everything they came for and it escalates into ridiculous results. Never write anticlimax, terror, or paperwork as a punchline. Write it filthy and funny.
> **What defeats them is ALWAYS their aging bodies or the women — never the world.** They are nearly 40 living a 20-year-old's life: stomachs wrecked by constant greasy late-night food, bodies that cannot survive all-night drugs and drinking, an onslaught of STDs, and total certainty they can still pull beautiful younger women while being turned down for younger hotter men. They never once identify age as the cause. Locations should tax a body that cannot take it, or land a rejection they instantly rationalise.

**For Clubs, Bars, Strip Venues, "Escort" Services, Drug Scenes:**
- [ ] **What do the bros THINK is happening?** (their delusional interpretation)
- [ ] **What is ACTUALLY happening?** (the hilarious reality they're missing)
- [ ] **How impaired are they?** (drunk/high enough to miss obvious clues)
- [ ] **What obvious signs do they ignore?** (visual/dialogue cues players see)
- [ ] **How does the "service provider" play along?** (NPCs who humor them for money)
- [ ] **What makes it comedically obvious to players?** (truth visible to audience)

### **🎭 COMEDY TONE GUIDELINES**
- [ ] **"The Hangover" meets "EarthBound"** tone - outrageous but not genuinely uncomfortable
- [ ] **Satirical exaggeration over realistic depiction** (cartoonish consequences, not actual harm)
- [ ] **Players root for the buffoons despite their flaws** (like Galavant, they're incompetent but charming)
- [ ] **Vice tourism becomes comedy of errors** rather than actual moral degradation
- [ ] **Cultural tourism pretensions become pratfalls** (literally and figuratively)

---

## **🎯 Location Development Workflow**

### **Daily Location Production Target: 1-2 Locations**
- **Morning**: Location profile creation (2-3 hours)
- **Afternoon**: JSON file generation (2-3 hours)
- **Evening**: Cross-reference validation and integration testing (1 hour)

### **Per-Location Checklist**
1. ☐ Create `[location_name].md` profile
2. ☐ Create `[Location_Name]_PNG_Assets.md` art spec
3. ☐ Create `[location_name]_core.json`
4. ☐ Create `[location_name]_npcs.json`
5. ☐ Create `[location_name]_interactions.json`
6. ☐ Create `[location_name]_environment.json`
7. ☐ Create `[location_name]_sprite_mapping.json`
8. ☐ Create `[location_name]_location_nodes.json`
9. ☐ Create `[location_name]_items.json` (if applicable)
10. ☐ Validate all cross-references
11. ☐ Copy to outputs folder
12. ☐ Present files to user

**Total Time Per Location: 4-6 hours average**

---

## **📊 Success Metrics & Quality Standards**

### **Completion Targets**
- **30+ total locations** across all three worlds
- **10+ core gameplay locations** per world (shops, quest hubs, progression points)
- **5+ specialty locations** per world (hidden areas, bonus content, easter eggs)
- **100% cultural specificity** (each location clearly reflects its city's satirical targets)

### **Quality Standards**
- **Complete world consistency** across all locations
- **Performance optimization** for all environmental effects and interactions
- **Cultural authenticity** balanced with respectful satirical humor
- **Social media potential** integrated into every location design
- **Cross-location continuity** maintained throughout narrative progression
- **All 8-9 required files generated** for every location

**This system ensures every location maximizes satirical impact, runtime performance, and viral social media potential while maintaining world integrity!**
