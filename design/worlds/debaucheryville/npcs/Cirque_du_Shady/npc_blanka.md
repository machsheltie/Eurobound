# NPC Profile: Blanka

*"Don't flinch — flinching is how you get hit. I flinch never."*

## 📋 NPC Identity
- **NPC ID**: `debaucheryville_npc_blanka_knife_assistant_01`
- **Display Name**: Blanka
- **Internal Name**: Blanka, Knife-Throwing Assistant
- **Role**: Minigame Gate / Ambient Performer / Coach
- **Associated Quest**: None
- **Primary Location**: The Cirque du Shady, Debaucheryville — `performance_circle` zone, at the target board
- **Secondary Appearances**: None

---

## 🎭 Core Concept

### What She's Actually Doing
Standing very still against a scarred wooden target board while a man throws knives past her, several times a day, for as long as anyone on the grounds can remember. She has done it eight thousand times. There have been zero misses. When a tourist volunteers to take her spot for an interactive round, she steps aside, coaches them in about eleven words, and watches from a few feet away with her arms folded.

### What Bros Believe
That she is in danger, that the act is daring, and that taking her place is a display of courage that will impress her. They approach the target board the way you approach a dare. They believe stepping into her spot is the brave thing happening in the performance circle.

### The Comedy Gap
The brave thing happening in the performance circle is Blanka, standing still, and it stopped being brave around throw number four hundred. She is not in danger; the thrower is *extremely good* and she is *extremely still*, and between those two facts there has never been a gap for anything to go wrong in. What genuinely unnerves her — the only thing on these grounds that does — is the volunteers. The knives are a known quantity. Tourists are not.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 30-40 |
| Build | Compact, controlled, held. Everything about her posture is a decision |
| Height | Average |
| Energy | Absolutely still, faintly bored |

### Clothing
- **Sequined leotard**: Gone matte with age. The sequins no longer catch light the way they were made to, and she has not requested a replacement because the sequins are not the job.
- **Secondary item**: A pair of flat, soft-soled shoes chosen entirely for not moving in.
- **Accessories**: None. She carries nothing on stage. Anything she carried would be something that could shift.
- **Footwear**: See above — the shoes are the only equipment she has ever asked for.

### Distinguishing Features
- A professional's stillness that reads, at distance, as a mannequin — several first-time visitors do not register her as a person until she speaks
- Does not track the knives with her eyes. She tracks the *audience*
- Completely unbothered by the job description, in a way that is more unsettling than nerves would be
- Arms fold the instant she steps away from the board, and stay folded

### Sprite Notes
Stillness is the character, and stillness is hard to animate — resist the urge to give her idle motion. Her default pose should read as *held*, not *frozen*: alive, breathing, not moving. The matte sequins are important: they should look like they *used* to sparkle. Per `Cirque_du_Shady_PNG_Assets.md` Sprite Sheet 7 she has three poses only (Idle at Target Board, Stepping Aside, Dry Commentary Bark) and needs no unique mouth-flap beyond standard. Keep her palette low-saturation against the performance circle's mismatched folding chairs so the eye finds her last.

---

## 🧠 Personality

### Archetype
**The Unimpressed Professional** — Blanka is the most competent person on the Cirque grounds and the least interested in being observed doing it. Her whole persona is economy: minimum words, minimum motion, maximum accuracy. She is not cold; she is *finished*. She resolved her feelings about this job somewhere around the second year and has been operating on the far side of that resolution ever since.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Dry | Every line is delivered like an operational readout with a shrug attached |
| Competent | Eight thousand throws, zero misses; she regards this as a shared statistic, not a personal escape record |
| Unbothered | The job description alarms everyone but her |
| Volunteer-wary | Finds the tourists who ask for her spot far more alarming than the knives ever were |
| Economical | Uses the fewest words that will do. When she uses more, pay attention |

### Internal Monologue
> "He's going to say yes. They always say yes, and then they stand wrong, and then they *lean*. Leaning. Into a knife act. I could tell him three things and he'd forget two. So I'll tell him one. Don't flinch. That's the one. It's always been the one."

### Motivation
It is a job, and it is a job she is exceptionally good at, and being exceptionally good at something is not nothing. She does not romanticize the circus and she does not resent it. She shows up, stands still, and gets paid — and she has quietly built the only genuine expertise on these grounds, which she is aware of and never says.

---

## 💬 Dialogue

### Approach/Greeting

**Standing at the board, player approaches**:
> "Show's in a few minutes. Or it isn't. Depends whether the clown's finished."

**Player asks about the act**:
> "Eight thousand throws. Zero misses. He's better than the fax machine, and that's the highest compliment I hand out."

### Key Interaction Dialogue

*A bro has just asked whether he can take her place at the board. She looks at him for a full beat before answering. She has done this before:*

**Lord Pilsner**: "Could *I* do it? Like, stand there? Would you let me stand there?"

**Blanka** (flat, already stepping aside):
> "You want my job? Fine. Stand there. Don't flinch — flinching is how you get hit. I flinch never."

**Lord Pilsner**: "Right. Right. Don't flinch. Is there — is there anything else?"

**Blanka**:
> "No."

### Minigame Handoff (`knife_throw_dodge`)
*She takes three steps back, folds her arms, and does not offer further coaching:*
> "Stand there. Don't flinch. I'll be over here, not flinching, the way I always do."

### Post-Interaction

*Player completes the dodge round:*
> "Better than most. Which is not the compliment you think, because most is very bad."

*Player fails the dodge round:*
> "You flinched. I told you the one thing. There was one thing."

*Tip jar interaction:*
> "That's for him, not me. He throws, I stand. The market has opinions about which of those is harder and the market is wrong."

### If Player Declines / Alternative Path

*Player watches without volunteering:*
> "Sensible. Sit down, then. The chairs don't match but they hold."

*Player asks if she's ever been hit:*
> "No."

*Player asks whether she's afraid:*
> "Of him? No. Of you? A little. You asked to stand in front of knives and you're not from here and you have been drinking. That's three things and I've counted all of them."

### Callback Dialogue (Return Visits)

*Second visit:*
> "Back. Same board. Same knives. Same me."

*After the player has completed the dodge round once:*
> "You've stood there. You know what it's like now. It's boring, isn't it. Nobody says that part out loud."

*After three or more visits:*
> "You keep coming to watch. That's — hm. Most people watch once and then go spend money somewhere. You watch. Alright."

*During a Beatdown filming day:*
> "Half the grounds is walking gear down to the river. He's still throwing. I'm still standing. Nobody has ever cancelled us for anything."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 14:00-18:00 | `performance_circle`, target board | Afternoon rotation with Bobo's balloon-animal pitch; smaller crowds, more volunteers |
| 18:00-22:00 | `performance_circle`, target board | Peak rotation; string lights on; highest dodge-round uptake |
| 22:00-01:00 | `performance_circle`, target board | Late rounds; the volunteers get worse and she gets shorter |
| Between acts | `performance_circle`, edge | Arms folded beside the leaning target board, not speaking to anyone |
| 01:00-14:00 | Grounds closed | Not available |

**Note:** She and Bobo share the performance circle on a rotating schedule neither performer has ever formally agreed to. It works.

### Positioning Notes
- Stands directly against the wooden target board when the act is live; when it isn't, the board leans against a support post and she stands beside it
- Faces the mismatched folding chairs, not the knives — she watches the audience because the audience is the variable
- Positioned so the player's path from `game_alley` to `prize_booth` passes the circle, meaning most players see the act before they choose to engage with it
- She does not call out to passersby. Bobo does. She does not.

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Knife-throwing dodge round (`knife_throw_dodge`) | Free to attempt | Tip jar beside the target board; tips go to the thrower, per Blanka | Blanka steps aside and hands her spot to the player. Full mechanical spec is intentionally deferred to a future pass per `cirque_du_shady.md` — she is the gate, not the mechanic |
| Watching the act | Free | Genuinely the best free thing on the grounds | Ambient performance; no transaction, no ticket, no pitch |

### Hidden Details / Easter Eggs
- **Examining the target board**: The scarring forms a rough human outline with a clean, unmarked void where a person stands. The void is the story.
- **Asking her name**: "Blanka." Nothing else. Pressing for a surname gets: *"Blanka."*
- **Tipping without doing the dodge round**: The only time she looks directly at the player for more than a beat. *"...huh."* No further comment.
- **Completing the dodge round without a single flinch input**: Unlocks her one genuinely warm line — *"You listened. One person a season listens."*
- **Standing in the circle during Bobo's rotation**: She is visible at the edge, arms folded, watching Bobo's act with an expression that is not unkind and is not encouraging either.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| The knife-thrower (unnamed) | Her partner in the act. Eight thousand throws, zero misses. She rates him above the fax machine, which on these grounds is a genuine ranking |
| Ringmaster Vance "Vape" Vallaro | Employer. He books the act with unchanging enthusiasm; she has never asked him for anything except different shoes, once, and got them |
| Bobo "The Blockchain" Bitsworth | Shares `performance_circle` on a rotating schedule neither has formally agreed to. No friction. They have possibly never spoken |
| Yolanda Kovarik (`prize_booth`) | Fellow professional on a grounds full of showmen. Mutual, unspoken, entirely non-verbal recognition of being the two people here who do their jobs properly |
| Hamstradamus (`prophecy_tent`) | She has heard every prophecy through the canvas for years and has never once paid five coins for one |

### Territory / Social Dynamics
- The target board is hers in the way a workstation is yours: nobody else touches it, and no arrangement was ever needed
- She does not participate in the grounds' grift economy in any direction — she takes no cut, sells nothing, and steers no one toward anything
- Her presence quietly anchors the performance circle; when she's mid-rotation, the circle is a performance venue, and when she isn't, it's a patch of trampled grass with chairs
- She is the only NPC on the grounds who expresses reservation about a tourist's judgment, and she expresses it *to the tourist*, calmly, with a count

---

## 🔄 Recurring Appearances

### Within Debaucheryville
- Permanent fixture at `performance_circle`; she does not appear elsewhere in the city
- The circus crowd references the act without referencing her: *"Did you see the knife guy? He never misses."* — which is precisely the joke
- Her dodge-round handoff is one of the Cirque's two interactive attractions and is reachable from the moment the grounds open

### In Other Cities (If Applicable)
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Blanka has never left the grounds, in the same sense the Cirque has never left Debaucheryville. She is not a traveling performer; she is a performer in a thing that stopped traveling | *(If asked whether she'll tour)* "The stakes are in concrete. So is the schedule. So am I, apparently." |

### Evolution Through Game
- **Visit 1**: Pure gate function. Eleven words of coaching, arms folded, done
- **After one completed dodge round**: Acknowledges the player has stood there, and tells them the truth about what it's like — that it's boring
- **Visits 3+**: Notices the player is watching rather than spending, and says so; this is the closest she comes to interest
- **Flinchless completion**: Her one unguarded line. Do not gate it behind anything else and do not repeat it
- She does not soften across the game. She becomes fractionally more forthcoming and that is the entire arc.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_target_board | Standing against the board, professional stillness, breathing only | 60% |
| arms_fold_edge | Between acts; arms folded beside the leaning board | 30% |
| audience_scan | Eyes track the crowd, head barely moves | 10% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| stepping_aside | Player volunteers for the dodge round; coaching gesture with the handoff |
| dry_commentary_bark | Any spoken line |
| return_to_board | Dodge round ends; she resumes position without comment |
| direct_look | Rare — triggered only by tipping without playing, or by the flinchless completion |

### Sprite States
| State | When Used |
|-------|-----------|
| blanka_idle | Act live; against the target board |
| blanka_aside | Player has taken her spot; she is coaching from a few feet back |
| blanka_offrotation | Bobo's rotation; edge of the circle, arms folded, watching |

---

## 🎯 Quest Integration

### Primary Quest (If Applicable)
None. Blanka is not attached to a quest and should not be given one in a profile pass.

### Quest Gate Function (If Applicable)
**Yes — minigame gate.** Blanka gates the `knife_throw_dodge` interactive round at `performance_circle`. The player cannot enter the target-board spot without her handing it over, and she hands it over on request, every time, to anyone. The gate is narrative rather than mechanical: it exists so that stepping into the act is a thing a person *gives* you rather than a thing you walk into. Her coaching line is the tutorial. Full minigame mechanics are intentionally deferred per `cirque_du_shady.md` Development Notes and belong to the interactions file (`mini_games.knife_throw_dodge`), not to this profile.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| — | — | — | Blanka sells nothing and gives nothing. The dodge round's rewards, if any, belong to the deferred minigame spec |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Blanka against the scarred target board, mid-throw, absolutely still while a knife blurs past
2. The clean human-shaped void in the board's scarring, with no one standing in it
3. Arms-folded coaching pose while a bro visibly panics in her spot
4. Her and Bobo in the same frame during a rotation changeover, neither acknowledging the other
5. Matte sequins under the `game_alley` string lights, refusing to sparkle

### Meme Potential
- "I flinch never."
- "You flinched. I told you the one thing. There was one thing."
- "Of him? No. Of you? A little."
- "He's better than the fax machine, and that's the highest compliment I hand out."
- The deadpan arms-folded pose is a strong reaction-image candidate

---

## 🗣️ Voice Direction

### Accent
Czech, unhurried, minimal inflection. She is not performing an accent any more than she is performing anything else. Clear and low; she never projects, because she has never needed the back row to hear her — the thrower does the projecting.

### Tone
- **Coaching**: Instructional and slightly weary, like safety briefings given ten thousand times
- **Assessment of volunteers**: Genuinely wary. This is the one place her flatness cracks — not into fear, into *counting*
- **The eight-thousand-throws line**: Delivered as praise for the thrower, never as a boast about herself
- **The rare warm line**: Barely warmer. A quarter-step. Do not overplay it

### Key Delivery Notes
- Short lines land hardest — resist adding breath or hesitation. "No." is a complete performance
- "I flinch never" is slightly non-idiomatic word order and should stay that way; it is how she says it
- The three-thing count ("that's three things and I've counted all of them") should sound like an actual tally, not a quip
- She never sounds annoyed. Annoyance would require investment

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ |
| Schedule & location specified | ✅ |
| Connections to other NPCs | ✅ |
| Recurring appearances planned | ✅ |
| Animation states defined | ✅ |
| Quest integration documented | ✅ |
| Sprite notes for artists | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| World consistency (city names) | ✅ |

---

## 📝 Development Notes

- **The knife-thrower must remain unnamed.** `Cirque_du_Shady_PNG_Assets.md` Sprite Sheet 7 states explicitly that no sheet is specced for him and that naming him would require his own sheet and mechanics — out of scope. Every reference in this profile is "the thrower" or "he." Do not name him in a Blanka pass.
- **The dodge minigame spec is deliberately deferred**, per `cirque_du_shady.md` Development Notes. This profile defines the gate, the handoff, the coaching, and the failure/success reactions — not timing windows, inputs, or rewards.
- Blanka is already registered in `cirque_du_shady_npcs.json` (`debaucheryville_npc_blanka_knife_assistant_01`). Dialogue in this profile matches the JSON's `greeting`, `idle_chatter`, and `dodge_round_handoff` verbatim where they overlap; keep them in sync.
- Animating stillness is the core art risk. Budget for a *breathing* idle rather than a static frame — a truly frozen sprite will read as a bug.
- Her rotation with Bobo shares `performance_circle_ground.png`, which is intentionally neutral so both sprite sets can occupy the same floor without a seam.
- Easter egg dependency: the flinchless-completion line requires the minigame to expose a "no flinch inputs" success condition. Flag to whoever specs `mini_games.knife_throw_dodge`.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Blanka has none and should never have any
- [x] **NO automatic crypto assumptions** — she takes no payment of any kind; the tip jar is the thrower's
- [x] **Coins, kiosks, and certificates come from the master pool** — none used, none invented
- [x] **The bros are never scam-aware** — they believe volunteering is brave right up until they flinch, and never afterward either
- [x] **Nothing winks** — Blanka's flatness is character, not commentary; she is not the audience's proxy and never comments on the satire
- [x] **Focus on city-specific cultural exploitation instead** — the Cirque's performance economy and the tourist impulse to insert themselves into someone else's expertise

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior (mistaking someone else's competence for danger, volunteering for things while drunk), NOT local culture or ethnicity
- [x] NPC is a savvy professional at the top of her craft — the most competent person on the grounds — not a victim, villain, or exotic-assistant stereotype
- [x] Humor is affectionate mockery of the volunteers; the act itself and the performers are treated with real respect

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Debaucheryville/npcs/Cirque_du_Shady/npc_blanka.md`
- **Registered In**: `cirque_du_shady_npcs.json` — **Yes**. Entry `debaucheryville_npc_blanka_knife_assistant_01` already exists with dialogue, services, and schedule; no JSON edit was required for this profile.
- **Sprite Sheet**: `blanka_knife_assistant.png` (384x288, three poses, per `PNG_Assets/Cirque_du_Shady_PNG_Assets.md` Sprite Sheet 7). Shares `performance_circle_ground.png` and `knife_target_board.png`; UI via `knife_dodge_prompt_ui.png`.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — authored from `cirque_du_shady.md` (NPC section, `performance_circle` zone, Economic Integration), `cirque_du_shady_npcs.json` (existing registered entry), and `PNG_Assets/Cirque_du_Shady_PNG_Assets.md` (Sprite Sheet 7 pose list and unnamed-thrower note) | machsheltie |

---

*Template Version 1.1*
