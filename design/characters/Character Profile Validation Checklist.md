# Character Profile Validation Checklist & Templates

## 🚨 **MANDATORY PRE-SUBMISSION CHECKLIST**

**Use this checklist for EVERY character profile before implementation:**

---

### **📝 World Consistency Validation**

- [ ] **NO real city names used** (Prague, Vienna, Dublin, etc.)
- [ ] **Satirical world names used consistently** (Debaucheryville, Sinfonia, Publandia)
- [ ] **Cross-world references use satirical names**
- [ ] **Cultural elements referenced generically** ("Bohemian traditions" not "Czech traditions")
- [ ] **Tourist references use world names** ("Debaucheryville tourist" not "Prague tourist")

### **📋 Markdown Profile Completeness**

#### **Identity Block**
- [ ] **NPC ID follows naming convention**: `world_area_type_##`
- [ ] **Display Name and Nickname clearly defined**
- [ ] **World Location and Area Zone specified**
- [ ] **Character Type matches satirical archetype**

#### **Satirical Design**
- [ ] **Archetype clearly defined and unique**
- [ ] **Satirical Target is specific and focused**
- [ ] **Humor Style consistent with game tone**
- [ ] **Catchphrase is memorable and character-specific**
- [ ] **Roast Vulnerability provides comedy potential**
- [ ] **Fatal Flaw drives character interactions**
- [ ] **Running Gag sustainable across multiple encounters**

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
- [ ] **All markdown personality elements reflected in JSON**
- [ ] **Detailed backstory data included**
- [ ] **Visual specifications match markdown descriptions**
- [ ] **Animation timing numerically specified**
- [ ] **Party recognition system fully implemented**

#### **Technical Implementation**
- [ ] **Behavioral flags match character psychology**
- [ ] **Audio clips planned and named consistently**
- [ ] **Sprite optimization settings specified**
- [ ] **Performance considerations addressed**

#### **Analytics Integration**
- [ ] **Screenshot moments identified for social media**
- [ ] **Interaction events tracked for UX insights**
- [ ] **Social sharing triggers maximize viral potential**

---

### **🎭 Character Consistency Matrix**

**Use this matrix to ensure character uniqueness:**

| Character | Archetype | Primary Satirical Target | Humor Style | Fatal Flaw |
|-----------|-----------|-------------------------|-------------|------------|
| Vlad the Validator | Crypto Bro Bouncer | Blockchain + Door Policy | Deadpan Contradictions | Crypto Evangelism |
| Crypto Clown | Failed Influencer | Crypto Desperation + Performance | Manic Overcompensation | Sales Pitch Everything |
| [Next Character] | [Unique Archetype] | [Specific Target] | [Distinct Style] | [Character Flaw] |

**❌ REJECT if:**
- Two characters share the same archetype
- Satirical targets overlap significantly  
- Humor styles are too similar
- Fatal flaws don't drive unique interactions

---

### **💬 Dialogue Quality Standards**

#### **Catchphrase Requirements**
- [ ] **Under 12 words for readability**
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
- ❌ **Any real city names (Prague, Vienna, Dublin)**
- ❌ **Specific real venues or landmarks**
- ❌ **Real politicians or celebrities by name**

---

### **🖥️ Performance & Assets Checklist**

#### **Dialogue Readability**
- [ ] **All text readable at desktop resolutions**
- [ ] **No single dialogue line exceeds 280 characters**
- [ ] **Font size considerations documented**
- [ ] **High contrast mode compatibility noted**

#### **Interaction Design**
- [ ] **Interaction zones minimum 48px diameter**
- [ ] **Animation performance optimized for 30fps minimum**
- [ ] **Audio files compressed for reasonable install size**
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
4. **Desktop Readiness**: Interaction targets and performance considered
5. **Marketing Potential**: Screenshot/sharing opportunities identified

---

### **🚫 AUTOMATIC REJECTION CRITERIA**

**Immediately reject character profiles that contain:**
- Real world city names anywhere in text
- Identical archetypes to existing characters  
- Dialogue longer than dialogue box limits
- No clear satirical purpose or target
- Missing technical implementation details
- Cultural references that could cause legal issues

---

### **✅ APPROVAL WORKFLOW**

1. **Self-Review**: Creator runs through full checklist
2. **Peer Review**: Second person validates world consistency
3. **Technical Review**: Implementation feasibility confirmed
4. **Cultural Sensitivity**: External review if needed
5. **Final Approval**: Character ready for JSON conversion

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
- **Animation Timing**: Specific intervals in seconds
- **Color Specifications**: Hex codes for key colors
- **Desktop Considerations**: Interaction zone sizes, readability

### Visual Characteristics  
- **Satirical Visual Elements**: What makes satire obvious
- **Social Media Potential**: Screenshot-worthy visual moments

## Personality & Satirical Design
### Core Personality
- **Fatal Flaw**: Drives character interactions
- **Running Gag**: Sustainable across encounters
- **Party Recognition**: Specific reactions to each party member

### Cultural Context
- **World Integration**: How they fit in satirical world
- **Cross-World References**: Using satirical names only

## Game Mechanics
### Advanced Integration
- **Behavioral Memory**: What they remember about player
- **Easter Egg Hooks**: Opportunities for hidden content
- **Analytics Tracking**: Social media and engagement metrics

## Implementation Specifications
### Technical Requirements
- **Performance Optimization**: Desktop-specific considerations
- **Audio Integration**: Specific file names and effects
- **Animation Schedule**: Precise timing for all states

### Marketing Integration
- **Screenshot Moments**: Viral potential identification
- **Social Sharing**: Built-in quote-worthy content
```

**This validation system ensures every character maintains world integrity while maximizing satirical impact and performance!**