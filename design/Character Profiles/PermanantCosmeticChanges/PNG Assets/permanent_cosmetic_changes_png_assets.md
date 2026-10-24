# Permanent Cosmetic Changes - Complete PNG Asset Requirements

*Artist Reference Document for Permanent Character Sprite Modifications*

**System ID**: `permanent_cosmetic_changes`  
**Priority**: HIGH (Affects all character sprites post-acquisition)  
**Integration**: Overlay system on base character sprites

---

## Art Direction Summary

### Visual Philosophy
Permanent cosmetic changes are **visible badges of poor decisions** that follow the bros throughout the game. They should be:
- Clearly visible when conditions are met
- Slightly embarrassing to anyone but the bros
- Source of NPC commentary and callback humor
- Consistent across all animation frames

### Key Principle
**What the bros see vs. what everyone else sees** - The comedy comes from the disconnect between the bros' perception of these items as status symbols and the reality that they're obviously tourist traps.

---

## COSMETIC CHANGE 1: Lord Pilsner's Duck Tattoo

### Overview
| Attribute | Value |
|-----------|-------|
| **Change ID** | `lord_pilsner_duck_tattoo` |
| **Affected Character** | Lord Pilsner only |
| **Body Location** | Lower back ("tramp stamp" position) |
| **Source Quest** | The Astronomical Cock-Up |
| **Visibility** | Conditional (outfit-dependent) |

### What It Actually Is
A **duck holding a scythe**. The tattoo artist clearly didn't understand "skeleton from the death clock" and drew a duck. The linework is wobbly (artist was also drinking), the ink is cheap (already fading), and it's unmistakably a waterfowl.

### What Lord Pilsner Believes It Is
"An authentic European death skeleton representing the cosmic dance of mortality from the ancient Astronomical Clock. Very cultured. Very classy. Like Amber's butterfly but HEAVIER."

---

### Sprite Sheet Requirements

**Filename**: `cosmetic_lord_pilsner_duck_tattoo.png`  
**Dimensions**: 128 × 64 pixels  
**Contains**: All tattoo variants for different visibility states

#### Tattoo Design (Base: 24×20 pixels)

**Main Elements**:
- **Duck Body**: Clearly duck-shaped (round body, duck head with bill)
- **Scythe**: Held in wing (NOT a hand - it's obviously a wing)
- **Pose**: Duck standing upright, scythe over shoulder
- **Expression**: Duck looks confused (unintentional but perfect)

**Ink Quality Details**:
- Wobbly linework (suggests intoxicated artist)
- Slight color bleed outside lines
- Faded grey-blue ink color (#6B7B8B)
- Uneven shading
- One eye slightly larger than the other

**What Makes It Obviously a Duck**:
- Bill (not a skull mouth)
- Round duck body (not skeletal)
- Feather texture hints
- Webbed feet visible
- Small tail feathers

#### Sprite Variants (Position: Row 0)

| Variant | Position | Size | Use Case |
|---------|----------|------|----------|
| Full visible | (0, 0) | 24×20 | Shirtless, bent over |
| Partially visible (shirt edge) | (24, 0) | 16×12 | Shirt riding up |
| Peeking out (waistband) | (40, 0) | 12×8 | Normal idle occasionally |
| Battle damage reveal | (52, 0) | 24×20 | After taking hit |
| Hot tub/swimming | (76, 0) | 24×20 | Water scenes |

#### Animation Integration (Row 1)

| Frame | Position | Notes |
|-------|----------|-------|
| Idle peek frame | (0, 20) | 5% chance during idle loop |
| Bending over | (24, 20) | Reaching for items |
| Victory pose | (48, 20) | Arms raised, shirt rides up |
| Knocked down | (72, 20) | Full visibility |
| Sleeping | (96, 20) | Hostel scenes |

---

### Visibility Conditions

**Always Visible With These Outfits**:
- Shirtless
- Swimming trunks
- Hospital gown (back open)
- Toga party outfit
- "Crop top accident" (shirt shrunk in wash)

**Sometimes Visible With These Outfits**:
- Abercrombie Muscle Tee (too small, rides up)
- Basketball Jersey Oversized (armholes reveal)
- Deep V-Neck (when bending)
- Any "too small" shirt variants

**Visibility During Actions**:
- Bending over to pick up items
- Reaching up (shirt rides up)
- Victory celebrations
- Getting knocked down in battle
- Sleeping/unconscious scenes

**Random Visibility**:
- 15% chance during normal idle animations
- Shirt briefly rides up, tattoo peeks out

---

## COSMETIC CHANGE 2: VIP Wristbands (All Bros)

### Overview
| Attribute | Value |
|-----------|-------|
| **Change ID** | `vip_wristbands_all_bros` |
| **Affected Characters** | Lord Pilsner, Chadwick, Bradley |
| **Body Location** | Right wrist |
| **Source Quest** | VIP Wristband Scam (unlocks after Clock quest) |
| **Visibility** | ALWAYS (bros never remove them) |

### What They Actually Are
Cheap plastic children's birthday party wristbands that cost approximately €0.003 each. They say "Je mi 7!" in Czech, which translates to "I'm 7!" - as in "I am seven years old." The scammer told them it means "Level Seven Access."

### What The Bros Believe They Are
"LEVEL SEVEN VIP STATUS. These wristbands grant us access to the most exclusive venues in Europe. Seven is ABOVE platinum. This doesn't even exist in America."

---

### Sprite Sheet Requirements

**Filename**: `cosmetic_vip_wristbands_all_bros.png`  
**Dimensions**: 128 × 96 pixels  
**Contains**: Wristband variants for all three bros across degradation states

#### Wristband Design (Base: 8×4 pixels per wristband)

**Design Elements**:
- Thin plastic party band texture
- Text "Je mi 7!" (barely legible, fading)
- Cheap plastic snap clasp (already loose)
- Gradual dirt/sweat accumulation

**Text on Wristband**:
| Czech | What Bros Think | Actual Meaning |
|-------|-----------------|----------------|
| Je mi 7! | Level 7 Access | I'm 7 years old! |

**Color Per Character**:
| Character | Color | Hex |
|-----------|-------|-----|
| Lord Pilsner | Deep Red | #8B0000 |
| Chadwick | Deep Blue | #00008B |
| Bradley | Deep Purple | #4B0082 |

#### Degradation States (Columns)

| State | Days | Visual Changes |
|-------|------|----------------|
| Pristine | 1-3 | Clean plastic, text readable, clasp tight |
| Worn | 4-7 | Text fading, edges curling, dirt visible |
| Crusty | 8+ | Text barely visible, heavily soiled, fraying, clasp broken but still on wrist |

#### Sprite Layout

**Row 0: Lord Pilsner Wristband**
| Variant | Position | State |
|---------|----------|-------|
| Pristine | (0, 0) | Days 1-3 |
| Worn | (16, 0) | Days 4-7 |
| Crusty | (32, 0) | Days 8+ |
| Battle animation | (48, 0) | Swinging arm |

**Row 1: Chadwick Wristband**
| Variant | Position | State |
|---------|----------|-------|
| Pristine | (0, 32) | Days 1-3 |
| Worn | (16, 32) | Days 4-7 |
| Crusty | (32, 32) | Days 8+ |
| Selfie pose | (48, 32) | Arm extended |

**Row 2: Bradley Wristband**
| Variant | Position | State |
|---------|----------|-------|
| Pristine | (0, 64) | Days 1-3 |
| Worn | (16, 64) | Days 4-7 |
| Crusty | (32, 64) | Days 8+ |
| Research pose | (48, 64) | Holding device |

---

### Position on Character Sprites

**Wrist Position Offsets** (from sprite origin):
| Character | X Offset | Y Offset |
|-----------|----------|----------|
| Lord Pilsner | +18 | +42 |
| Chadwick | +17 | +40 |
| Bradley | +16 | +44 |

**Animation Considerations**:
- Wristband moves with arm in all animations
- Visible in all frames (never hidden)
- Clasp glints occasionally (1 frame per idle cycle)

---

## Technical Implementation

### Layer System

```
Layer Order (bottom to top):
1. base_character_sprite
2. clothing_layer
3. body_overlay_back (tattoo layer)
4. accessory_overlay_arm (wristband layer)
5. accessory_overlay_head (future: monocle, etc.)
6. effect_overlay (status effects, etc.)
```

### Overlay Blending
- **Tattoo**: Multiply blend with skin tone for natural look
- **Wristbands**: Normal blend, sits on top of arm

### Animation Frame Matching
- Overlays must match base sprite animation timing
- Tattoo visibility frames sync with idle loop
- Wristbands visible in ALL frames

---

## NPC Reaction Sprites

**Filename**: `npc_cosmetic_reactions.png`  
**Dimensions**: 64 × 64 pixels

### Reaction Icons (16×16 each)
| Reaction | Position | Trigger |
|----------|----------|---------|
| "Is that a duck?" thought bubble | (0, 0) | NPC notices tattoo |
| Stifled laugh | (16, 0) | NPC sees wristbands |
| Eye roll | (32, 0) | Bros flash VIP status |
| Confused squint | (48, 0) | NPC examines tattoo closely |

---

## Social Media / Viral Potential

### Screenshot Moments
1. **First tattoo reveal** - Player sees it's a duck before Pilsner does
2. **Mirror scene** - Pilsner admiring his "skeleton" (it's a duck)
3. **Wristband degradation** - Day 8+ crusty wristbands still worn proudly
4. **NPC reactions** - Locals laughing at "VIP" bros
5. **Post-credits callback** - Amber confirms it's a duck

### TikTok Potential
- "POV: You got a tattoo in Prague"
- "When you're LEVEL SEVEN VIP" (shows crusty wristband)
- "The tattoo artist knew exactly what he was doing"

---

## File Delivery Checklist

### Required PNG Files
- [ ] `cosmetic_lord_pilsner_duck_tattoo.png` (128×64)
- [ ] `cosmetic_vip_wristbands_all_bros.png` (128×96)
- [ ] `npc_cosmetic_reactions.png` (64×64)

### Quality Requirements
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **DPI**: 72 (screen resolution)
- **Pixel Art**: Clean edges, no anti-aliasing on small elements

### Animation Integration Requirements
- Tattoo overlays align with Lord Pilsner base sprite
- Wristband overlays align with all three bros' base sprites
- Frame timing documentation for visibility conditions

---

## Cross-Reference

### Related Files
- `permanent_cosmetic_changes.json` - Master data file
- `astronomical_cockup.md` - Source quest (tattoo)
- `vip_wristband_scam.md` - Source quest (wristbands) [TO BE CREATED]
- `lord_pilsner_sprite_sheet.png` - Base character sprite
- `chadwick_sprite_sheet.png` - Base character sprite
- `bradley_sprite_sheet.png` - Base character sprite

### Quest Integration
- Tattoo acquired in Path A of Astronomical Cock-Up
- Wristbands acquired in subsequent VIP Wristband Scam quest
- Both permanently modify character appearance

---

**END OF ASSET REQUIREMENTS**

*"It's not a duck. It's DEATH. European death. You wouldn't understand."*
— Lord Pilsner, defending his clearly duck-shaped tattoo
