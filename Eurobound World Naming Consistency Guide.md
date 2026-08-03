# Character Profile Validation Checklist & Templates

## 🚨 **MANDATORY PRE-SUBMISSION CHECKLIST**

**Use this checklist for EVERY character profile before implementation:**

---

### **📝 World Consistency Validation**

- [ ] **NO real city names used** (must use Debaucheryville, Sinfonia, Publandia only)
- [ ] **Satirical world names used consistently** (Debaucheryville, Sinfonia, Publandia)
- [ ] **Cross-world references use satirical names**
- [ ] **Cultural elements reflect specific city stereotypes** (not generic European)
- [ ] **Tourist references use world names** ("Debaucheryville tourist" not "real city tourists")
- [ ] **Character reflects city's specific cultural satirical targets**

#### **City-Specific Cultural Accuracy Requirements**
##### **Debaucheryville Characters Must Reference:**
- [ ] **Tech startup culture** (if applicable to character)
- [ ] **Underground nightlife scene** (if nightlife-related)
- [ ] **Tourist party destination reputation** 
- [ ] **Digital nomad/backpacker culture**
- [ ] **Bohemian artistic traditions** (generic cultural reference)

##### **Publandia Characters Must Reference:**
- [ ] **Pub culture and drinking traditions**
- [ ] **Literary heritage and cultural tourism**
- [ ] **Celtic cultural elements** (generic reference)
- [ ] **University/student culture**
- [ ] **Weather-related daily life**

##### **Sinfonia Characters Must Reference:**
- [ ] **Classical music and opera culture**
- [ ] **Coffeehouse intellectual traditions**  
- [ ] **Imperial history and architecture tourism**
- [ ] **Art museum and gallery scene**
- [ ] **Formal/high society etiquette expectations**

### **📋 Markdown Profile Completeness**

#### **Identity Block**
- [ ] **NPC ID follows naming convention**: `world_area_type_##`
- [ ] **Display Name and Nickname clearly defined**
- [ ] **World Location and Area Zone specified**
- [ ] **Character Type matches satirical archetype**

#### **Satirical Design Requirements**
- [ ] **Archetype clearly defined and unique**
- [ ] **Satirical Target is specific and focused**
- [ ] **Humor Style consistent with game tone**
- [ ] **Catchphrase is memorable and character-specific**
- [ ] **Roast Vulnerability provides comedy potential**
- [ ] **Fatal Flaw drives character interactions**
- [ ] **Running Gag sustainable across multiple encounters**
- [ ] **Character reflects city's specific stereotype/culture**
- [ ] **Satirical theme not over-represented** (check theme distribution matrix)
- [ ] **Seedy underbelly element clearly present** (vice, scam, exploitation, etc.)

#### **Thematic Diversity Requirements**
- [ ] **Character fills underrepresented theme** (check balance targets)
- [ ] **Satirical target different approach from existing characters in same theme**
- [ ] **Cultural stereotype specific to assigned city**
- [ ] **Business context makes sense** for character's location and role
- [ ] **Exploitation method unique** within same theme category
- [ ] **Socioeconomic level varies** from other characters in same theme
- [ ] **Tourist vs. local dynamic considered** and balanced across world

#### **Game Integration**
- [ ] **Mechanical role clearly defined** (shop, quest, info, battle)
- [ ] **Special abilities serve satirical purpose**
- [ ] **Economic integration logical and balanced**
- [ ] **Area unlocks make narrative sense**
- [ ] **Party recognition system accounts for all 3 members**

#### **Technical Specifications**
- [ ] **Animation timing specified in seconds**
- [ ] **Audio cues detailed and realistic**
- [ ] **Performance optimization considerations noted**
- [ ] **Sprite sheet and coordinates planned**

---

### **🔧 JSON Implementation Validation**

#### **Core Data Completeness**
- [ ] **All markdown personality elements reflected in core JSON**
- [ ] **Detailed backstory data included**
- [ ] **Visual specifications match markdown descriptions**
- [ ] **Animation timing numerically specified**
- [ ] **Party recognition system fully implemented**

#### **Sprite Mapping JSON Updates**
- [ ] **All sprite states from markdown profile added to sprite mapping**
- [ ] **Animation timing matches character profile specifications**
- [ ] **Color palette hex codes specified accurately** 
- [ ] **Particle effects defined for signature animations**
- [ ] **Audio clips mapped to character-specific animations**
- [ ] **Visual distinguishing features positioned correctly**
- [ ] **Performance props and environmental elements specified**
- [ ] **Performance optimization settings included**

#### **Technical Implementation**
- [ ] **Behavioral flags match character psychology**
- [ ] **Audio clips planned and named consistently across all JSON files**
- [ ] **Sprite optimization settings specified**
- [ ] **Performance considerations addressed**

#### **Analytics Integration**
- [ ] **Screenshot moments identified for social media**
- [ ] **Interaction events tracked for UX insights**
- [ ] **Social sharing triggers maximize viral potential**

---

### **🎭 Character Consistency & Thematic Balance Guidelines**

**Use these guidelines to ensure character diversity and thematic distribution:**

#### **Satirical Theme Balance Principles**
- [ ] **Dominant themes should not exceed 30% of total NPCs per world**
- [ ] **Each satirical category should have multiple character archetypes** (not just one approach)
- [ ] **City-specific themes prioritized** over universal themes
- [ ] **Seedy underbelly spectrum broadly covered** across all business types

#### **Debaucheryville Theme Distribution (Prague-inspired)**
| Theme Category | Balance Target | Current Status | Business Applications |
|---------------|----------------|----------------|----------------------|
| **Crypto/Tech** | ~20% of NPCs | 3 characters ⚠️ REVIEW | FinTech bars, startup cafes, crypto ATMs |
| **Party/Club Nightlife** | ~25% of NPCs | 0 characters | Clubs, bars, late-night eateries |
| **Tourist Exploitation** | ~20% of NPCs | 0 characters | Tour companies, transport, accommodations |
| **Digital Age Vices** | ~15% of NPCs | 0 characters | Internet cafes, phone shops, social media spots |
| **Substances/Party Enhancement** | ~10% of NPCs | 0 characters | "Wellness" shops, energy drink vendors |
| **Accommodation/Service Scams** | ~10% of NPCs | 0 characters | Hostels, Airbnbs, service providers |

#### **Publandia Theme Distribution (Dublin-inspired)**  
| Theme Category | Balance Target | Current Status | Business Applications |
|---------------|----------------|----------------|----------------------|
| **Pub Culture Exploitation** | ~30% of NPCs | 0 characters | Pubs, breweries, whiskey tours |
| **Literary/Cultural Tourism** | ~20% of NPCs | 0 characters | Bookshops, cultural sites, walking tours |
| **University/Youth Exploitation** | ~15% of NPCs | 0 characters | Student areas, gap year services |
| **Weather/Seasonal Scams** | ~10% of NPCs | 0 characters | Umbrella rentals, weather gear shops |
| **Music/Entertainment** | ~15% of NPCs | 0 characters | Traditional music venues, buskers |
| **Food/Dining Tourism** | ~10% of NPCs | 0 characters | "Authentic" restaurants, food tours |

#### **Sinfonia Theme Distribution (Vienna-inspired)**
| Theme Category | Balance Target | Current Status | Business Applications |
|---------------|----------------|----------------|----------------------|
| **Classical Music/Opera** | ~25% of NPCs | 0 characters | Concert halls, music shops, street performers |
| **Coffeehouse Culture** | ~20% of NPCs | 0 characters | Traditional cafes, modern coffee shops |
| **Imperial History Tourism** | ~20% of NPCs | 0 characters | Palace tours, historical sites, museums |
| **Art/Gallery Scene** | ~15% of NPCs | 0 characters | Art galleries, antique shops, art supply stores |
| **Luxury/High Society** | ~10% of NPCs | 0 characters | Upscale shops, luxury services |
| **Academic/Intellectual** | ~10% of NPCs | 0 characters | Universities, libraries, intellectual cafes |

#### **Balance Warning System**
🟢 **BALANCED**: Theme under 25% of world's NPCs
🟡 **REVIEW NEEDED**: Theme 25-35% of world's NPCs - consider diversifying  
🔴 **OVER-SATURATED**: Theme over 35% of world's NPCs - stop creating this theme type

#### **Archetype Diversity Within Themes**
- [ ] **Multiple approaches to each theme** (e.g., crypto: desperate vs. successful vs. fake expert)
- [ ] **Different business contexts** for same theme (e.g., nightlife: clubs vs. bars vs. late-night food)
- [ ] **Varying exploitation methods** (scamming tourists vs. locals vs. each other)
- [ ] **Different socioeconomic levels** within same theme

---

### **💬 Dialogue Quality Standards**

#### **Catchphrase Requirements**
- [ ] **Under 12 words for on-screen readability**
- [ ] **Instantly recognizable as this character**
- [ ] **Incorporates satirical target elements**
- [ ] **Memorable enough for social media quotes**

#### **Party Recognition Standards**
- [ ] **Lord Pilsner**: Seen as outdated/traditional
- [ ] **Chadwick**: Social media savvy acknowledged  
- [ ] **Bradley**: Physical strength referenced with confusion

#### **Status Effect Reactions**
- [ ] **Hungover**: Character-specific concern/mockery
- [ ] **Grease Fingers**: Hygiene commentary matching personality
- [ ] **Embarrassed**: Social dynamics observation

---

### **🌍 Cross-World Reference Standards**

#### **Acceptable References**
- ✅ **"Debaucheryville has better [thing] than Publandia"**
- ✅ **"I heard about your reputation from Sinfonia"**
- ✅ **"Bohemian traditions" / "Alpine culture" / "Celtic influence"**

#### **Forbidden References**
- ❌ **Any real city names (must use satirical world names only)**
- ❌ **Specific real venues or landmarks**
- ❌ **Real politicians or celebrities by name**

---

### **🖥️ Performance & Assets Checklist**

#### **Dialogue Readability**
- [ ] **All text readable at common desktop resolutions**
- [ ] **No single dialogue line exceeds 280 characters**
- [ ] **Font size considerations documented**
- [ ] **High contrast mode compatibility noted**

#### **Interaction Design**
- [ ] **Interactive elements clearly sized for focus/click targeting**
- [ ] **Animation performance optimized for 30fps minimum**
- [ ] **Audio files compressed to fit memory budget**
- [ ] **Particle effects scaled for performance**

---

### **🎯 Easter Egg Integration Standards**

#### **Easter Egg Requirements**
- [ ] **At least 2 easter eggs per major character**
- [ ] **Trigger conditions realistic but discoverable**
- [ ] **Rewards meaningful but not game-breaking**
- [ ] **Social media screenshot potential maximized**

#### **Behavioral Pattern Recognition**
- [ ] **Character remembers player behavioral patterns**
- [ ] **Unique reactions to repeat status effects**
- [ ] **Cross-character gossip system considerations**

---

### **⚡ Pre-Implementation Final Check**

**Before converting ANY character to JSON, verify:**

1. **World Consistency**: Run text search for real city names
2. **Uniqueness**: Compare against existing character matrix
3. **Technical Specs**: All animation/audio details specified
4. **Platform Readiness**: Input targets and performance considered
5. **Marketing Potential**: Screenshot/sharing opportunities identified
6. **Complete Implementation Path**: All three JSON files will be updated

### **📂 Required JSON File Updates**

**Every character implementation must update ALL THREE files:**

#### **1. Core NPC Data (`assets/data/npcs/base_profiles/[world]_core.json`)**
- [ ] **Complete character entry with all markdown details**
- [ ] **Backstory integration and personality drivers**
- [ ] **Party recognition system implemented**
- [ ] **Game mechanics and behavioral flags**

#### **2. Dialogue Trees (`assets/data/npcs/dialogue_trees/[world]_dialogue.json`)**
- [ ] **Default greeting with party-specific overrides**
- [ ] **Complete conversation trees with branching options**
- [ ] **Status effect reactions updated**
- [ ] **World state responses with satirical names**
- [ ] **Repeat interaction logic implemented**

#### **3. Sprite Mapping (`assets/data/npcs/sprite_mappings/[world]_sprites.json`)**
- [ ] **All animation states from markdown profile**
- [ ] **Precise timing specifications (in seconds)**
- [ ] **Color palette with exact hex codes**
- [ ] **Particle effects for signature animations**
- [ ] **Audio clip mapping with character attribution**
- [ ] **Visual props and environmental elements**
- [ ] **Performance optimization settings**

---

### **🚫 AUTOMATIC REJECTION CRITERIA**

**Immediately reject character profiles that contain:**
- Real world city names anywhere in text
- Themes that would push over 35% saturation in their world
- Identical archetypes to existing characters  
- Generic European stereotypes not specific to assigned city
- No clear seedy underbelly/vice/exploitation element
- Dialogue longer than on-screen text limits
- No clear satirical purpose or target
- Missing technical implementation details
- Cultural references that could cause legal issues
- Character that could exist in any city without modification

#### **Business Context Requirements**
**Auto-reject if:**
- [ ] **Business type doesn't support character's satirical theme**
- [ ] **Location doesn't make sense for character's exploitation method**
- [ ] **No clear customer/victim base** for character's scam/vice
- [ ] **Character role conflicts with business function**

#### **Theme Balance Warnings**
**Be cautious if:**
- [ ] **Theme approaching 25% of world's NPCs** (yellow warning zone)
- [ ] **Same exploitation method used by multiple characters**
- [ ] **Business type over-represented** without thematic diversity
- [ ] **Only targeting tourists OR only targeting locals** (need balance)
- [ ] **Character could exist in different city without changes** (too generic)

#### **Immediate Development Guidance**
**Current Debaucheryville Status (3 total NPCs):**
- 🔴 **Crypto/Tech: 100% (3/3)** - STOP creating crypto characters
- 🟢 **All other themes: 0%** - PRIORITIZE these areas
- 🎯 **Next characters should focus on**: Nightlife, tourist exploitation, digital age vices

---

### **✅ APPROVAL WORKFLOW**

1. **Self-Review**: Creator runs through full checklist
2. **Peer Review**: Second person validates world consistency  
3. **Technical Review**: Implementation feasibility confirmed
4. **Cultural Sensitivity**: External review if needed
5. **Complete JSON Implementation**: All three JSON files updated and verified
6. **Cross-File Validation**: Ensure consistency between core data, dialogue, and sprites
7. **Final Approval**: Character ready for game engine implementation

---

### **🔄 Post-Implementation Verification**

**After updating all JSON files, run these checks:**

#### **Data Consistency Verification**
- [ ] **Character name identical across all three JSON files**
- [ ] **Animation states referenced in dialogue match sprite mapping**
- [ ] **Audio clips named consistently in core data and sprite mapping**
- [ ] **Status effect reactions present in both core and dialogue files**
- [ ] **Party recognition system matches across core and dialogue files**

#### **Technical Validation**
- [ ] **All animation timing specified in seconds (not frames)**
- [ ] **Color codes use proper hex format (#RRGGBB)**
- [ ] **Audio file paths follow naming convention**
- [ ] **Particle effects properly linked to animation triggers**
- [ ] **Performance optimization flags set appropriately**

#### **Integration Testing Preparation**
- [ ] **Sprite sheet coordinates don't overlap other characters**
- [ ] **Audio clips don't conflict with existing sound design**
- [ ] **Behavioral flags compatible with game systems**
- [ ] **Shop mechanics integrate with economy system**
- [ ] **Quest mechanics align with progression system**

---

## **🎮 Character Profile Template (Updated)**

**Use this enhanced template for all new characters:**

```markdown
# Character Name

*One-line character description*

## Character Identity
- **NPC ID**: world_area_type_##
- **Display Name**: Full Character Name  
- **Nickname/Title**: How they're known
- **World Location**: Satirical world name only
- **Area Zone**: Specific location within world
- **Character Type**: Satirical archetype

## Visual Design
### Sprite Information
- **Sprite Sheet**: filename.png
- **Sprite Coordinates**: [x, y, width, height]
- **Sprite States**: List all animation states needed
- **Animation Timing**: Specific intervals in seconds for each state
- **Color Specifications**: Hex codes for key colors
- **Desktop Considerations**: Focus/click target sizes, readability

### Visual Characteristics  
- **Satirical Visual Elements**: What makes satire obvious
- **Social Media Potential**: Screenshot-worthy visual moments
- **Distinguishing Features**: Unique props, clothing, accessories
- **Particle Effects**: Special visual effects needed
- **Environmental Props**: Objects that accumulate or scatter

## Personality & Satirical Design
### Core Personality
- **Fatal Flaw**: Drives character interactions
- **Running Gag**: Sustainable across encounters
- **Party Recognition**: Specific reactions to each party member
- **Voice Direction**: How they should sound when voiced

### Cultural Context
- **World Integration**: How they fit in satirical world
- **Cross-World References**: Using satirical names only

## Game Mechanics
### Advanced Integration
- **Behavioral Memory**: What they remember about player
- **Easter Egg Hooks**: Opportunities for hidden content
- **Analytics Tracking**: Social media and engagement metrics
- **Audio Integration**: Specific sound effects and music cues

## Implementation Specifications
### Technical Requirements
- **Performance Optimization**: Platform-specific considerations
- **Audio Integration**: Specific file names and effects
- **Animation Schedule**: Precise timing for all states
- **Sprite Mapping Details**: Coordinates, particle effects, color variants

### Marketing Integration
- **Screenshot Moments**: Viral potential identification
- **Social Sharing**: Built-in quote-worthy content

## JSON Implementation Checklist
- [ ] **Theme distribution verified** (not over-represented)
- [ ] **City-specific cultural elements included**
- [ ] **Seedy underbelly vice/scam clearly defined**
- [ ] Core NPC data file updated
- [ ] Dialogue tree file updated  
- [ ] Sprite mapping file updated
- [ ] Cross-file consistency verified
- [ ] Performance optimization confirmed
```

**This validation system ensures every character maintains world integrity while maximizing satirical impact and runtime performance!**

### **⚠️ CRYPTO WARNING - CRITICAL**
- [ ] **Crypto elements ONLY if already established** in existing character description or specifically requested by user
- [ ] **NO automatic crypto assumptions** - crypto is minor gag used sparingly (2% of game maximum)  
- [ ] **Focus on city-specific cultural exploitation instead** (party tourism, food scams, cultural pretension)
- [ ] **Target aging frat bro exploitation and tourist scams** - NOT tech culture unless character specifically calls for it
- [ ] **DEFAULT: Assume NO crypto involvement** unless explicitly stated in source material