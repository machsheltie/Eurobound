# Ability Definition: [Ability Name]

*"[Satirical tagline or in-character boast capturing the delusion]" — [who says this, e.g. the bro himself, mid-brag]*

<!--
HOW TO USE THIS TEMPLATE
This template is for COMBAT ABILITIES: the Bravado-fueled special moves and Ultimates
the three bros use in battle (see party_abilities.json for the live data and
design/mechanics/Battle/bravado.md for the system these plug into). It covers both
halves of an ability — the engine fields that get typed verbatim into
game/assets/data/skills/party_abilities.json, and the design material an author needs
to actually picture and write the move.

Replace every [bracketed placeholder] with real content. Delete this comment block
before publishing the finished ability doc. Keep all H2 section headers (with emoji)
and table column shapes exactly as they appear here.

Money, if any appears (e.g. a Cover Charge → Bravado conversion), is always SOVS.
Bravado is the only spendable combat resource here — there is no SP in this codebase.
-->

## 📋 Ability Identity
- **Ability ID**: `[ability_name_snake_case]` (e.g. `foam_cyclone`, `beer_pong_meteor` — this is the exact key under `abilities` in `party_abilities.json`)
- **Display Name**: [Ability Name] (e.g. "Foam Cyclone")
- **Owner**: [Lord Pilsner / Chadwick / Bradley]
- **Bravado Style**: [Keg-Fu (Lord Pilsner) / Bro-Mancy (Chadwick) / Frat-Sorcery (Bradley)]
- **Skill Tree Branch**: [Branch name from the owning bro's sheet, e.g. "Barroom Tactics," or "N/A — Ultimate"]
- **Ability Type**: [Special Move / Ultimate]
- **Source**: [How it's learned — starting kit, skill tree unlock at level X, personal quest reward, item-set bonus]

---

## ⚙️ Engine Fields

These map 1:1 onto the ability's entry in `game/assets/data/skills/party_abilities.json`. Fill every row — an author who completes this table has handed the engine everything it needs.

| Field | Value |
|-------|-------|
| **`ability id`** (JSON key) | `[ability_name_snake_case]` |
| **`display_name`** | "[Ability Name]" |
| **`bravado_cost`** | [integer, e.g. 4] |
| **`power_multiplier`** | [float, e.g. 1.8] |
| **`battle_text`** | "[Line using `{user}` for name substitution, e.g. "{user} unleashes a Foam Cyclone, blinding everyone in a five-foot radius, self included."]" |
| **`is_ultimate`** | [true / false] |

**Note**: `bravado_cost` spends the bro's Bravado meter, not SP — SP does not exist in this codebase. Costs should feel proportionate to the move's theatrics: a cheap basic special (e.g. `roast_line` at 4) versus a full Ultimate, which should cost meaningfully more of the meter it's gated behind.

---

## 🥊 Bravado Gating

Bravado has four bands, defined in `game/core/game_state.gd`: **zero** = 0, **low** = 1–25, **mid** = 26–70, **high** = 71–100.

- **Minimum Bravado Band Required**: [zero / low / mid / high]
- **If this is an Ultimate**: Ultimates are locked out at **zero** and **low** — they require **mid or higher**, enforced in `game/battle/battle_manager.gd`. Do not spec an Ultimate with a lower minimum band; it will not fire.
- **What zero Bravado means for this move**: nothing catastrophic. Zero Bravado does NOT cause collapse, knockout, or forced retreat — that's HP's job, not this meter's. It only means Bravado cannot be spent: the bro keeps fighting, throwing basic attacks like a civilian, until he earns some hype back. [If this ability has a specific "can't afford it" line, note it here, e.g. Chadwick muttering "I... can't do the selfie stick combo right now, bro."]

---

## 🎭 What It's Satirizing
[Name the specific target — vice-tourism grift, influencer culture, gym-bro toxic positivity, absinthe mysticism, whatever. Be specific: not "toxic masculinity" in the abstract, but the exact delusional behavior this move performs. E.g.: Foam Cyclone satirizes the guy at the bar who thinks spilling his pint in a wide arc reads as intimidating rather than as a liability the bartender now has to mop.]

---

## 🎬 What It Looks Like On Screen
- **Windup**: [The pose, prop, or ritual before the move fires — e.g. Lord Pilsner cracking his knuckles on a pint glass that was not designed for that]
- **Execution / VFX**: [The actual animation and effect — froth clouds, ring-light flare, protein-shake burp cone, whatever the move's signature visual is]
- **Audio cue**: [SFX or voice line that plays, e.g. an air horn, a Nokia ringtone, a crowd "OOOOH"]
- **Band-based flourish** (optional): [How the move visibly escalates at High Bravado vs. how it looks sadder and smaller at Low — per bravado.md, High Bravado gets "special visuals (beer glow, crowd cheering)," Low gets "weak quips"]

---

## 💥 When It Fails
Every move that can miss, whiff, or backfire needs its failure state written — the comedy lives here as much as in the success case.

- **Failure trigger**: [Miss chance, a specific bad roll, a regional condition from bravado.md's regional interactions, an "Embarrassed" status proc, etc. — e.g. "10% chance he trips while posting"]
- **What happens**: [The specific, embarrassing consequence — not "the attack misses," but what it looks like when it misses. E.g.: the Solo cup flash blind hits an ally instead, or Bradley's Alpha Elbow Drop connects but also flattens him.]
- **Mechanical consequence** (if any): [Self-damage, Bravado drain, a status effect applied to the user, wasted turn, etc.]

---

## 🗣️ Battle Text Variants
The `battle_text` field above is the baseline. List any additional lines the ability needs — these live in the same data entry or an adjacent variants block, not as separate JSON fields unless the engine schema supports it.

| Context | Line |
|---------|------|
| **Success** | "[Line — this is the `battle_text` value above]" |
| **Failure** | "[Line for the whiff/backfire case]" |
| **Regional variant (optional)** | "[If this move gets a flavor twist in a specific city, per bravado.md's regional spell variants — e.g. Charm of the Bro Code fizzling in Publandia because locals don't know what a frat is]" |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Ability ID is snake_case and matches the `party_abilities.json` key exactly | ☐ |
| All six engine fields specified (`ability id`, `display_name`, `bravado_cost`, `power_multiplier`, `battle_text`, `is_ultimate`) | ☐ |
| `battle_text` uses `{user}` for name substitution | ☐ |
| Minimum Bravado band stated; Ultimates require mid or higher | ☐ |
| Zero-Bravado behavior described correctly (no collapse/knockout — only "can't spend it") | ☐ |
| Satirical target is specific, not generic | ☐ |
| Failure state written, not just a miss percentage | ☐ |
| Bro is never afraid or disgusted, even in failure | ☐ |
| Bro is never self-aware or scam-aware about how ridiculous the move looks | ☐ |
| No narrator, disclaimer, or moral framing anywhere in the flavor text | ☐ |
| All money references (if any) are in SOVS | ☐ |
| Name is unique across the game | ☐ |

---

## 📝 Development Notes
- [Any sprite/animation dependency — new frames needed, existing rig reused]
- [Any status effect this move applies or requires that needs its own spec]
- [Balance note — how this compares in cost/power to the bro's other moves at the same tier]
- [Easter egg or callback idea]
- [Anything blocked on an author ruling — damage numbers, targeting, or a failure state not yet decided]

---

*Template is a floor, not a ceiling, per CLAUDE.md — add sections a specific ability needs (e.g. a multi-hit breakdown, an item-set synergy note) rather than cramming it into the wrong field.*
