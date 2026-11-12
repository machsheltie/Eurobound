# Couchsurf Host Entry: [Host Display Name]

*"[The host's signature line]" - [Host Display Name]*

> **Template Version 1.0 — created 2026-11-11 at the author's request; pending author review**

<!--
HOW TO USE THIS TEMPLATE
This is an ENTRY SPEC, not a standalone file. Each couchsurf host is one entry inside
its city's Chronicles doc:

  design/quests/[city]/couchsurfingchronicles[city].md

The binding rules live in design/quests/general_quests/couchsurfingchronicles.md
("🔀 THE FOUR STATES", author ruling 2026-08-03). Read it first. Worked examples:
The Understudy in design/quests/sinfonia/couchsurfingchroniclessinfonia.md, and any host
in design/quests/debaucheryville/couchsurfingchroniclesdebaucheryville.md.

- The host also needs an NPC profile (NPC_Profile_Template.md). The SCENE LINES live
  here, in the Chronicles entry, and never in the profile; the profile cross-references
  this entry.
- Every host gets all four states. The only exception is QUEEN Riviéra Renata (the
  source of the Herp), who has no four-state treatment.
- Sex happens and is never shown: implication, cutaway, morning-after wreckage only.
  No nudity. Nobody relocates.
- Host identity, scene content, buffs/debuffs, durations and collectibles need an author
  ruling. Anything you draft that the author has not ruled on is marked PROPOSED.
- Couchsurfing is part of an optional side quest; never signpost skipping a host as a mistake.
- Replace every [bracketed placeholder]. Paste only the "🛏️ Host Entry" section into the
  Chronicles doc. The checklist, warnings, status and history sections below it are for
  the writer's review and stay out of the Chronicles doc.
- Keep the bold field labels and the four-state headings exactly as here.
-->

## 🛏️ Host Entry (paste this section into the Chronicles doc)

### **[N]. [Host Display Name]**

**NPC:** "[Host Display Name]" — [one-line identity]
**NPC ID / Profile:** `[city]_npc_[name]_01` — `design/worlds/[city]/npcs/[Location_Name]/[npc_file].md` [or "profile still owed"]
**Location:** [Venue — specific spot, City — parody names only]

**Where You Meet [Her/Him/Them]:** [The invitation trigger: where the bros meet the host and what they must do, finish or avoid to be invited to crash. Include any instant-fail condition.]

**Enhanced Morning Scene:** [The morning after. What the bros wake up to, what the host is doing, the one specific useful or useless thing the host gives them. Sex is implied, never shown.]

**Enhanced Bro Delusion Dialogue:**
- **Lord Pilsner:** *"[Line — never afraid, never disgusted, never self-aware]"*
- **Chadwick:** *"[Line]"*
- **Bradley:** *"[Line]"*

**Result:**
- **[Buff or debuff name]** [effect, e.g. +2 Charm] for [duration] — [permanent / timed]
- **[Status]** [effect and duration; statuses from `design/mechanics/Battle/status_effects.md`, or new and PROPOSED via `status_effect_template.md`]
- **SOVS change:** [+/- X SOVS, or "none"]
- **Collectible: [Funny, unique name]** — [what it is; it gets inspect microcopy]

> Author ruling (2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy." Couchsurf collectibles are exactly that kind of item.

**Intoxication Hook (only if the night involves drinking or drugs that carry into the morning):** [Name the status and ladder step (Buzzed → Beer Goggles → Shitfaced → Catastrophe) or drug status, per `design/mechanics/intoxication_law.md` and `design/narrative/bros_choose_debauchery.md`. No free advantage: a morning buff is paid for by a cost. Delete this line if it does not apply.]

**Location-Specific Roasting:** [Internal. What the bros think they found versus what the host actually is.]

**Satire Angle:** [Internal. One or two sentences. Never surfaces in player-facing text.]

#### **🔀 Four-State Routing — [Host Display Name]**

*Authority: `design/quests/general_quests/couchsurfingchronicles.md` → "🔀 THE FOUR STATES". **The lines live here.** Flag: `[npc_snake_name]_refused_while_infected`. NPC ID `[city]_npc_[name]_01`; the profile cross-references this block rather than restating it.*

**Binding for all four states:** [Any rule from the entry above that holds in every state, e.g. an instant-fail condition. Delete if none.]

**STATE 1 — CLEAR** *(never caught `the_herp`)*
Plays the entry above exactly as authored. Full payload.

**STATE 2 — INFECTED** *(`the_herp` active, `item_gold_circle_coin` not equipped)* — **no payload; sets `[npc_snake_name]_refused_while_infected = true`**

*[Stage direction.]*

**[Host Display Name]** *([delivery note])*:
> "[The refusal, in the host's own established voice. Characterized and funny, never preachy, never a lecture. No generic refusal exists.]"

*Bro rationalisation, immediately after:*
- **Lord Pilsner:** *"[Line — the bros absorb none of it]"*
- **Chadwick:** *"[Line]"*
- **Bradley:** *"[Line]"*

**STATE 3 — SUPPRESSED, CLEAN** *(Coin equipped, flag false)*
**Plays exactly as State 1.** No callback, no reference, no acknowledgement. Full payload.

**STATE 4 — SUPPRESSED, CALLBACK** *(Coin equipped, flag true)* — **sting only, then resolves normally**

**[Host Display Name]** *([delivery note])*:
> "[One sting callback about last time. Never a second refusal; never blocks the entry.]"

**From here the entry runs the Enhanced Morning Scene and Result block above exactly as authored.** *Payload is awarded once: a host completed before infection gives the scene, not duplicate rewards.*

**Quest Flags Set:**
| Flag | Set When |
|------|----------|
| `chronicles_entry_completed_[npc_id]` (the Chronicles flag, one bool per NPC; routing lists use it, never a per-venue `_couchsurf_completed` flag. Author, 2026-11-12, Eurobound-9jza) | [State 1, 3 or 4 resolves] |
| `[npc_snake_name]_refused_while_infected` | State 2 plays |
| `[other flag]` | [Condition] |

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Host name funny and unique across the game | ☐ |
| NPC profile exists or is listed as owed, and cross-references this entry | ☐ |
| Invitation trigger and Morning Scene written | ☐ |
| One delusion line per bro | ☐ |
| Result block: buffs/debuffs with durations, SOVS change, collectible | ☐ |
| Collectible has funny inspect microcopy | ☐ |
| All four states written (Renata excepted) | ☐ |
| State 2 is in the host's voice, funny, never preachy | ☐ |
| State 4 is one sting, then resolves; never a second refusal | ☐ |
| Flags named `<npc>_refused_while_infected` and listed | ☐ |
| Sex implied only; no nudity | ☐ |
| Intoxication hook done (if it applies) | ☐ |
| No real city or place names in player-facing text | ☐ |
| Every unruled field marked PROPOSED | ☐ |
| Bros never afraid, disgusted or self-aware | ☐ |

---

## 🚫 Warnings & Restrictions

### Content
- [ ] No narrator, disclaimer, moral framing, or any device that explains the joke; nothing winks at the player
- [ ] Full-strength MA satire; no sanitized version, no safe-build swap. The only ceiling is no nudity
- [ ] Satire is sharp and specific — the bros' delusion AND the city's culture are both fair game (author ruling 2026-08-03: no punch-direction rules)
- [ ] Hosts are never boring, corporate or professional; each one is running their own angle
- [ ] The bros are never afraid, disgusted, self-aware or scam-aware. Hosts may be as disgusted as they like
- [ ] No mascots: a host never sends a pet, puppet or companion object along with the bros
- [ ] Funny, unique names; no real place names in player-facing text; real brands, products and songs keep their real names

### Money & Crypto
- [ ] All money is SOVS ("40 SOVS", "1 SOV"); never euros, the € glyph or koruna
- [ ] Crypto content conforms to `design/economy/economy_system.md`; coins only from `design/economy/shitcoin_master_pool.md`

---

## 🔧 Development Status

- **Status**: [Concept / Drafted / Reviewed / Implemented]
- **Entry Location**: `design/quests/[city]/couchsurfingchronicles[city].md`
- **NPC Profile**: `design/worlds/[city]/npcs/[Location_Name]/[npc_file].md` [or "owed"]

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Initial entry | [name] |

---

*Template Version 1.0 — created 2026-11-11 at the author's request; pending author review. Field set drawn from the 2026-11-11 template audit (section B2), `design/quests/general_quests/couchsurfingchronicles.md` ("THE FOUR STATES"), and the Debaucheryville and Sinfonia Chronicles entries, which already carry the four-state routing. Publandia and Shamsterdam entries still need it.*
