# Status Effect Entry: "[Status Name]"

*"[In-game description line, exactly as it plays]"*

> **Template Version 1.0 — created 2026-11-11 at the author's request; pending author review**

<!--
HOW TO USE THIS TEMPLATE
This is an ENTRY SPEC for the status-effect registry, not one file per status. Every
status lives as one entry in:

  design/mechanics/Battle/status_effects.md   (the master list)

and, once its schema is ruled, one key in:

  game/assets/data/skills/status_effects.json  (currently empty: {"status_effects": {}})

Why this exists: location, NPC and item docs coin statuses freely, and the registry is
empty, so names collide and duplicate. Before coining a status ANYWHERE, grep the
master list. If a status already does the job, use it. A new status needs this entry and
an author ruling (new statuses are a mechanics change).

Rules that apply while filling it in:
- Read .claude/CLAUDE.md and the eurobound-satire-voice skill first.
- Alcohol and drug statuses: read design/mechanics/intoxication_law.md and
  design/narrative/bros_choose_debauchery.md and complete the Intoxication Review.
- Stat names match the engine: max_hp, max_bravado, offense, defense, speed, charm,
  luck, grit. Joke stats ("+5 Tourist Vibes") stay in the description; map the real
  effect onto an engine stat or a named mechanic, or mark it PROPOSED.
- Every effect value, duration and rule needs an author ruling. Anything drafted
  without one is marked PROPOSED, in the field itself.
- Replace every [bracketed placeholder]. Delete this comment block and the template
  version line before adding the entry to the master list. In the master list, use
  the existing bullet shape shown in "Master List Entry" below.
-->

## 📋 Status Identity
- **Display Name**: "[Status Name]" (funny and unique across the game; grep the repo, including item and NPC names)
- **Status ID**: `[status_name_snake_case]` (the key in `status_effects.json`)
- **Polarity**: [Positive / Negative / Neutral-Situational] — matches the master list section it goes in
- **Category**: [Intoxication / Food / Social / Hygiene / Money / Scripted-Permanent / Other]
- **Scope**: [Battle only / Overworld only / Both]
- **Applies To**: [One bro / whole party / enemy]

---

## 🎭 The Gap

| Question | Answer |
|----------|--------|
| **What the bros think it is** | [In their words. They are never afraid, disgusted or self-aware.] |
| **What it actually does** | [Plain mechanics] |
| **Why it's funny** | [Internal only. Never explained in player-facing text.] |

---

## 📊 Effects

| Effect | Value | Notes |
|--------|-------|-------|
| [Stat delta, e.g. `charm`] | [+/-X] | |
| [Turn-skip chance] | [X%] | |
| [Ally-hit chance] | [X%] | |
| [HP per turn] | [+/-X] | |
| [Lockout, e.g. "can't use Bravado abilities"] | [—] | |
| [Overworld effect: prices, NPC reactions, dialogue locks, particles] | [Value] | |

### Duration
- **Length**: [X turns / X–Y turns / until event / permanent]
- **Ends When**: [Timer / rest / item / location / never]

### Sources
| Source | Type | File |
|--------|------|------|
| [Item, enemy move, scene, location] | [Consumable / enemy / scripted / environmental] | `[path]` |

### Cures
| Cure | Notes |
|------|-------|
| [Item, rest, time, location] | [What it costs; "never" for scripted-permanent statuses] |

### Stacking & Interaction Rules
| Rule | Value |
|------|-------|
| **Reapplied while active** | [Refresh / Extend / Escalate / Blocked] |
| **Escalates into** | [Next status, if any] |
| **Follow-up status** | [e.g. "Manic" → "Crash"] |
| **Immunity granted / blocked** | [Statuses it prevents or is prevented by] |

| Existing Status | What Happens |
|-----------------|--------------|
| [Status] | [Interaction] |

---

## 🍺 Intoxication Review

*Required for alcohol, drug and stimulant statuses. Write "Not intoxicating" and delete the tables otherwise.*

### Alcohol Ladder Position (alcohol only)
- **Step**: [Buzzed / Beer Goggles / Shitfaced / Catastrophe — where this status sits on the ladder in `design/mechanics/intoxication_law.md` Appendix A]

### No Free Advantage (`design/narrative/bros_choose_debauchery.md`)
"Intoxicants do not provide uncomplicated, consequence-free advantages." State the cost: [the drawback, crash, delayed consequence or loss of control that pays for any benefit].

### 10-Point Design Review (`design/mechanics/intoxication_law.md` §8)
| # | Point | Answer |
|---|-------|--------|
| 1 | Source item or drink | [Answer] |
| 2 | Immediate effect | [Answer] |
| 3 | Escalation conditions | [Answer] |
| 4 | Visible player-facing cues | [Answer] |
| 5 | Effect on player control | [Answer — bounded, readable, recoverable] |
| 6 | Duration and recovery | [Answer] |
| 7 | Comedic consequence | [Answer] |
| 8 | Interaction with other established statuses | [Answer] |
| 9 | Technical implementation dependencies | [Answer — flag anything the Godot build cannot do yet as proposed engineering work] |
| 10 | Requires further author approval? | [Yes/No + what] |

---

## 🎨 Visual & Audio Cues

| Cue | Description |
|-----|-------------|
| **Status Icon** | [Size, shape, palette or "not yet specced"] |
| **Sprite / Particle Effect** | [Reuse an existing asset where one exists; name it] |
| **Screen Effect** | [Wobble, blur, tint; give the accessibility alternative] |
| **Sound** | [Cue or "none"] |

---

## 🧾 Master List Entry

The entry as it goes into `design/mechanics/Battle/status_effects.md`, in the file's existing shape:

```
"[Status Name]"
    • [Effects, comma-separated]
    • Duration: [Duration]
    • Source: [Sources]
    • Cure: [Cures]
    • Special: [Stacking/interaction rules, if any]
    • Description: "[In-game description line]"
```

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Master list grepped; no existing status already does this | ☐ |
| Name and ID unique across the game | ☐ |
| Effects use engine stat names or named mechanics (or marked PROPOSED) | ☐ |
| Duration, sources, cures and stacking rules all stated | ☐ |
| Loss of control is bounded, readable and recoverable | ☐ |
| Intoxication review complete (if intoxicating) | ☐ |
| Description line is funny, short, and never explains the joke | ☐ |
| No real city or place names in the description | ☐ |
| Every unruled value marked PROPOSED | ☐ |
| Author ruling recorded for a new status | ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, PSA, moral framing, or any device that explains the joke; the description line never winks at the player
- [ ] Full-strength MA satire; no sanitized version, no safe-build swap, no softened status name. The only ceiling is no nudity
- [ ] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules)
- [ ] No moralizing: a status never punishes the bros because the game has a moral position; it delivers a consequence
- [ ] The bros are never afraid, disgusted or self-aware about a status, even a permanent one
- [ ] Funny, unique name; no real place names in player-facing text; real brands and products keep their real names (Four Loko, BAWLS)
- [ ] No mascots: no status summons or attaches a pet, puppet or companion entity

### Money
- [ ] Any price effect is expressed in SOVS ("+25% prices", "40 SOVS fine", "1 SOV"); never euros, the € glyph or koruna

---

## 📝 Development Notes

- [Engine dependencies: status_effects.json schema is pending an author ruling]
- [Open question for the author]

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Author-Approved / Implemented]
- **Entry Location**: `design/mechanics/Battle/status_effects.md` → [Positive / Negative / Neutral-Situational]
- **Registered In**: `game/assets/data/skills/status_effects.json` [Yes/No — schema pending author ruling]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial entry | [name] |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), the entry shape in `design/mechanics/Battle/status_effects.md`, and `design/mechanics/intoxication_law.md`.*
