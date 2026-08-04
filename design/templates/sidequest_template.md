# Sidequest Template - Eurobound

## 📋 Quest Identity
- **Quest ID:** `[city]_sidequest_[name]_01`
- **Display Name:** "[Quest Name]"
- **Satirical Subtitle:** "[Tagline that captures the cringe]"
- **Quest Giver:** [NPC Name] @ [Location] — `[npc_id]`, profile: `[path to NPC profile doc]`
  - **Cover Identity:** [Who they present themselves as to the bros]
  - **True Identity:** [What they actually are / the angle they're running]
- **City:** [Debaucheryville / Publandia / Sinfonia / Shamsterdam]
- **Quest Type:** [Fetch / Escort / Gauntlet / Minigame / Social / Dungeon / Collection] · **Tier:** [CORE / FULL / STRETCH]
- **Recommended Level / Difficulty:** [1-10] / [Trivial / Moderate / Brutal]
- **Repeatable:** [No / Yes — reward throttling and non-repeating dialogue specified below]
- **Estimated Duration:** [X minutes]

> **All side quests are optional.** (Standing rule — never gate main progression behind one.)

---

## 🎭 Core Premise

### The Setup
**What the bros THINK is happening:**
> [Their delusional interpretation]

**What is ACTUALLY happening:**
> [The reality players can see]

**Why it's funny:**
> [The satirical target and comedy mechanism]

---

## 🎯 Satirical Targets
- **Primary Target:** [Main thing being mocked]
- **Secondary Targets:** [Other cringe elements]
- **Cultural Specificity:** [City-specific humor]
- **Y2K/Era References:** [Period-appropriate cringe if applicable]

---

## 📖 Quest Structure

### Quest Initiation
**Trigger:** [How the quest starts]
**Location:** [Where it begins]
**NPC Dialogue:**
> [Quest giver's pitch - should sound like opportunity to bros, obvious scam to players]

**Bros' Reaction:**
- **Lord Pilsner:** "[His take]"
- **Chadwick:** "[His take]"
- **Bradley:** "[His take]"

---

### Quest Stages (linear structure)

<!--
STRUCTURE: use whichever fits — linear Stages, a Binary Path Choice, or both (stages that
lead into a branch). Delete the section you don't use. Not every quest branches: collection
quests, gauntlets, and dungeon descents are linear; a quest built on a player decision
(e.g. Bradley's wedding ring) uses paths.
-->

**Stage 1: [Name]**
- **Objective:** [What the player does]
- **Location:** [Where]
- **Key beat:** [Dialogue moment, encounter, or reveal]

**Stage 2: [Name]**
- **Objective:** [What the player does]
- **Location:** [Where]
- **Key beat:** [Dialogue moment, encounter, or reveal]

**Stage 3: [Name]**
- **Objective:** [What the player does]
- **Location:** [Where]
- **Key beat:** [Dialogue moment, encounter, or reveal]

---

### Standard Rewards (granted regardless of path)
- **SOVS:** [X SOVS]
- **Clout:** [X]
- **Item:** [Item name] — [Effect/description]
- **Stat Change:** [+/- Bravado/Charm/etc.]
- **Status/Title:** [Any status effects or titles gained]
- **Unlocks:** [Any content unlocked]

---

### Binary Path Choice

#### PATH A: [Choice Name]
**What bros think they're doing:**
> [Their delusion]

**What they're actually doing:**
> [Reality]

**Execution Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Key Dialogue/Moments:**
> [Memorable lines and scenes]

**NPC Reactions:**
- **[NPC Type]:** "[Reaction highlighting bros' absurdity]"
- **[NPC Type]:** "[Another reaction]"

**Rewards:**
- **Item:** [Item name] - [Effect/description]
- **Stat Change:** [+/- Bravado/Charm/etc.]
- **Status:** [Any status effects or titles gained]
- **Unlocks:** [Any content unlocked]

---

#### PATH B: [Choice Name]
**What bros think they're doing:**
> [Their delusion]

**What they're actually doing:**
> [Reality]

**Execution Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Key Dialogue/Moments:**
> [Memorable lines and scenes]

**NPC Reactions:**
- **[NPC Type]:** "[Reaction]"
- **[NPC Type]:** "[Reaction]"

**Rewards:**
- **Item:** [Item name] - [Effect/description]
- **Stat Change:** [+/- Bravado/Charm/etc.]
- **Status:** [Any status effects or titles gained]
- **Unlocks:** [Any content unlocked]

---

## 🌍 Environmental Integration

### City Changes After Completion
- [How the city visually changes based on quest completion]
- [NPCs that reference the quest afterward]
- [Persistent visual elements]

### NPC Callbacks
- **[Location]:** "[NPC references quest events]"
- **[Location]:** "[Another callback]"

### Easter Eggs
- [Hidden details related to quest]

---

## 💬 Key Dialogue Moments

### Bros' Delusional Commentary
**Lord Pilsner:**
> "[Quote that shows his specific brand of idiocy]"

**Chadwick:**
> "[Quote showing his social media/content obsession]"

**Bradley:**
> "[Quote showing his confidently wrong 'intelligence']"

<!-- NO commentary section exists here by design. There is no narrator and no in-world
substitute for one. Nothing observes, frames, contextualizes, or explains the joke — not a
voice, not a sign, not a knowing NPC aside. The scene happens; the player gets it. -->

---

## 🔗 Quest Connections

### Prerequisites
- [Any required prior quests]
- [Required items or stats]

### Unlocks
- [Quests this enables]
- [Locations this opens]
- [Items that become available]

### Cross-References
- [Related quests in same city]
- [Related quests in other cities]
- [Recurring characters involved]

---

## 🖥️ Screenshot & Sharing Moments

### Screenshot Moments
1. [Key visual moment worth capturing]
2. [Another shareable moment]
3. [Peak cringe screenshot opportunity]

### Social Sharing Hooks
- [Why players would share this]
- [Hashtag potential]

---

## 🎬 POST-CREDITS SCENE REWARD

### Scene Title: "[Title]"
### Unlock Condition: Complete [Path A / Path B / Either Path]
### Duration: [X seconds/minutes]

**SETTING:**
> [Where and when - usually "back home" months later]

**SCENE:**
```
[Full screenplay-style scene showing the ACTUAL aftermath of the bros' 
delusions crashing into reality. This is where we show:
- What really happened as a result of their actions
- How their "victory" was actually embarrassing
- NPCs' true opinions of them
- The gap between their memory and reality]
```

**THE PUNCHLINE:**
> [Final joke/image that drives it home]

**PLAYER REWARD:**
- Scene added to "Memories" gallery
- [Any bonus unlocks for collecting all scenes]

---

## 🏆 Completion Achievement
- **Achievement Name:** "[Achievement Name]"
- **Public Description:** "[What players see in the achievement list]"
- **Hidden Description:** "[The humiliating truth, revealed on unlock]"
- **Unlock Condition:** [Path A / Path B / Either / All stages]

---

## ⚙️ Technical Implementation

### Quest Flags
Namespaced `city.venue.event` strings (PRD §11). Flags are write-once booleans unless prefixed `counter.`. Every flag listed here must be registered in `data/quests/flags.json`.

| Flag | Type | Set when | Read by |
|------|------|----------|---------|
| `[city.venue.event]` | bool / counter | [What sets it] | [What checks it — scenes, NPCs, other quests] |
| `[city.venue.event]` | bool / counter | [What sets it] | [What checks it] |

### Data & Scene Dependencies
- **Data files touched:** [JSON files this quest reads or requires entries in]
- **Scenes/nodes required:** [New scenes, interactables, or triggers]
- **Items granted:** [Item IDs, with their spec doc paths]

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Bros are NEVER self-aware or scam-aware | ☐ |
| Players laugh AT bros, not WITH them | ☐ |
| Scams are obvious to players | ☐ |
| Bros remain confident throughout — never afraid, never disgusted | ☐ |
| City-specific cultural satire | ☐ |
| NO narrator, no moral framing, nothing that explains the joke | ☐ |
| Crypto content conforms to the economy system (SOVS + darknet shitcoin pool); no one-off invented coins | ☐ |
| All prices and rewards in SOVS | ☐ |
| Seedy nightlife underbelly present and shown in full | ☐ |
| Y2K/era-appropriate cringe | ☐ |
| Quest is optional (never gates main progression) | ☐ |
| Quest flags registered in `data/quests/flags.json` | ☐ |
| All names unique across the game | ☐ |
| Post-credits scene delivers payoff | ☐ |
| Screenshot-worthy moments | ☐ |

---

## 📝 Development Notes
- [Any implementation considerations]
- [Art asset requirements]
- [Audio/music notes]
- [Testing priorities]

---

*Template Version 2.0 — 2026-08-04: absorbed the retired `quest.md` short form (quest type/tier, repeatable, difficulty, quest-giver cover vs true identity, linear stages, standard rewards, completion achievement, quest flags & technical implementation). Narrator section struck per author ruling; crypto and currency checks aligned to canon. This is the only sidequest template.*
