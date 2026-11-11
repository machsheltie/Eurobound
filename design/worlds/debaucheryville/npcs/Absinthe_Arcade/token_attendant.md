# NPC Profile: The Token Attendant (name PROPOSED — NEEDS AUTHOR RULING)

*"WELCOME to the Absinthe Arcade! Tokens are one SOV! Toilet paper is complimentary!"* (PROPOSED)

> **Source and status.** The author designed this NPC in round v25 (2026-11-11). His words, verbatim, are canon:
> **"token attendant should be an employee who is also dressed in tgi fridays esque clothes and flare and goes
> around fixing stuck ticket machines, dealing with issues with the token exchange machines, and has the
> unfortunate secondary job of servicing the bathrooms. He gets caught by the bros in the bathroom sleeping in
> the arms of one of the statues that's been repurposed as a toilet paper holder, passed out from drinking too
> much absinthe"** **[CANON — author]**. He is a **separate person from the prize-counter bartender** **[CANON —
> author, round v25]**. The existing roster line "cheerfully unashamed of the exchange rate, treats every obvious
> ripoff as hospitality" (`absinthe_arcade_npcs.json`, 2026-11-02 package) is kept. Everything else in this file
> (name, dialogue, scene staging, the statue's design, schedule, which bathroom) is a Claude draft:
> **PROPOSED — NEEDS AUTHOR RULING.**

## 📋 NPC Identity
- **NPC ID**: `debaucheryville_npc_arcade_token_attendant_01` (existing roster ID, kept)
- **Display Name**: **PROPOSED — NEEDS AUTHOR RULING.** Options (all grepped across `design/`, `game/assets/`, `docs/`: zero hits):
  1. **Out of Order Ota**: named for the OUT OF ORDER sign he hangs on every broken machine. The bros find the same sign hung on his own lanyard in the bathroom.
  2. **Jammin' Jarda**: he clears ticket jams. His flair includes a button that says JAMMIN'. He thinks it is about the machines.
  3. **Thirty-Seven Pieces**: he wears thirty-seven pieces of flair, Brian's number from *Office Space*, the overachiever the bartender's fifteen is a protest against. The bros call him by the count. He corrects them when he adds one.
- **Internal Name**: the Token Attendant
- **Role**: Machine fixer (stuck ticket machines, the TOKENS HERE exchange) **[CANON — author]** / bathroom attendant **[CANON — author]** / discovery scene
- **Associated Quest**: None. The bathroom discovery is a one-off scene (PROPOSED)
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), the token exchange (`aa_node_token_exchange`) and wherever a ticket machine has jammed
- **Secondary Appearances**: the Arcade bathroom **[CANON — author]**. Which bathroom, and whether it is a screen, is an open question (see the end of this file)

---

## 🎭 Core Concept

### What They're Actually Doing
He is the Arcade's everything-else guy. The bartender got the bar. He got the token machine that eats SOVS, every ticket dispenser that jams mid-payout, and **the toilets** **[CANON — author]**. Management dressed him in the same TGI Fridays-style flair as the bar staff **[CANON — author]**, so he unclogs the bathroom in a candy-stripe shirt and twenty-odd buttons that say things like ASK ME ABOUT TOKENS (PROPOSED). Unlike the bartender, he has made his peace with all of it. He is cheerful. He is unashamed of the exchange rate. He treats every ripoff as hospitality (existing roster). He is also, by the end of his shift, **passed out on absinthe in the arms of a bathroom statue that holds the toilet paper** **[CANON — author]**.

### What Bros Believe
- **Lord Pilsner** thinks a man who drinks absinthe at work, in the building, on the clock, is a European aristocrat of leisure, and wants his job.
- **Chadwick** thinks the flair is merch and asks how many followers you need to get sponsored by a token machine.
- **Bradley** thinks the man has a key to every machine in the building, and that this makes him the most powerful person in Debaucheryville. He keeps trying to make friends with the keys.

### The Comedy Gap
The bros see a legend living the dream. The player sees a man whose job is fixing the machines that rob the bros and then cleaning up after the bros, who copes by drinking the house product until a statue has to hold him. Nobody in the scene thinks anything is wrong, him least of all.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Mid-20s to early 30s (PROPOSED) |
| Build | Wiry; moves at a jog between jammed machines (PROPOSED) |
| Height | Average |
| Energy | Chipper, sweaty, quietly drunk by midnight |

### Clothing
- **Uniform**: TGI Fridays-esque **[CANON — author]**: PROPOSED red-and-white striped work shirt, black apron with a coin pouch full of tokens, black pants, a lanyard heavy with machine keys.
- **Flair** **[CANON — author]**: PROPOSED buttons and pins covering both braces and the apron bib: ASK ME ABOUT TOKENS, 1 SOV = 1 FUN!, a pin of a toilet roll he got from management for "going above and beyond", a smiley face with green eyes, a Tamagotchi clipped to the strap (dead).
- **Accessories**: a ticket-jam hook, a rubber mallet and a plunger, carried as one bundle (PROPOSED). An absinthe slotted spoon tucked behind the name tag like a pen (PROPOSED).
- **Footwear**: Non-slip work shoes. One of them comes off in the bathroom scene (PROPOSED).

### Distinguishing Features (PROPOSED)
- Fixes every jam the same way: one smack on the left side of the machine
- Answers every question with the price of tokens first
- Gets greener in the face as the night goes on (palette shift by hour)
- Smiles through absolutely everything

### Sprite Notes
128x128 semi-realistic per `design/style_guides/character_sprite_pipeline.md`. The read is **stripes + flair + key lanyard + plunger**: the same dress code as the bartender with the opposite posture (upright, eager, moving). Movable NPC sprite, never painted into room art (ruling 2026-11-09). The bathroom scene needs a separate pose: asleep, cradled across the statue's arms, flair glinting, one shoe off.

---

## 🧠 Personality

### Archetype
**The Cheerful Lifer** — the employee who does every job nobody else will, in mandatory flair, and is upbeat about all of it because the alternative is noticing. He sells the worst exchange rate in the city with a host's smile, clears ticket jams with genuine joy, scrubs the bathroom without complaint, and quietly drinks absinthe from the bar's back stock to keep the smile on. He does not consider himself a drunk. He considers himself "on break, recurring".

### Personality Traits (PROPOSED)
| Trait | Description |
|-------|-------------|
| Hospitable | Treats a 1-SOV token as a personal gift to the customer |
| Unashamed | Thinks the exchange rate is a feature (existing roster) |
| Handy | Can fix any machine with one hit, if it's on the left |
| Loyal to the building | Talks about the machines like coworkers, the statues like family |
| Quietly hammered | Functional until about 02:00, then horizontal |

### Internal Monologue (PROPOSED)
> "Three jams, one clog, a guy who tried to pay the token machine in Pokémon cards. Great night. Quick one in the bathroom and I'll take the left-side ticket machine at two."

### Motivation
Keep the machines running so the tokens keep flowing, keep the bathroom usable so the customers keep drinking, and keep himself just drunk enough to find both of those things delightful.

---

## 💬 Dialogue (all PROPOSED unless marked)

### Approach/Greeting
**At the TOKENS HERE machine**:
> "Welcome! One SOV, one token! The machine sets the rate. I just love it."

**Bros complain about the rate**:
> "Outside it's one SOV for nothing. In here it's one SOV for a token. That's infinity percent better."

### Key Interaction Dialogue — Machine Trouble
*A ticket dispenser jams mid-payout. He jogs over, already smiling.*

**Bradley**: "It ate my tickets, bro. I won those."

**Token Attendant** (delighted):
> "She's just shy." *(smacks the left side once; tickets pour out)* "Left side. Always the left side. Like people."

*The token machine takes a 20-SOV note and dispenses nothing.*

**Lord Pilsner**: "Your machine just mugged me."

**Token Attendant**:
> "It's holding your tokens somewhere safe. Inside it. You can visit them." *(smacks the left side; 20 tokens clatter out)* "See? It missed you."

### The Bathroom Discovery — scene beats
*Author's beat **[CANON — author]**: the bros catch him in the bathroom, asleep in the arms of one of the statues that's been repurposed as a toilet-paper holder, passed out from drinking too much absinthe. Staging, trigger, statue design and lines below are PROPOSED.*

1. **Trigger (PROPOSED):** the first time the bros go into the Arcade bathroom after 01:00. He is not at the token machine; the OUT OF ORDER sign is hanging on the token machine instead.
2. **Reveal (PROPOSED):** the bathroom door swings open on a bronze Art Nouveau statue, a Green Fairy with spread wings, holding her arms out in front of her like she's offering something. She was once offering something. Now a toilet roll is threaded on one forearm and the Token Attendant is lying across both, cradled like a bride carried over a threshold, snoring. One shoe is off. An empty absinthe glass with a slotted spoon balanced on it sits on the cistern. His flair catches the light. He has hung an OUT OF ORDER sign on his own lanyard.
3. **The bros react (PROPOSED).** Nobody is disgusted, nobody is worried:
   > **Lord Pilsner:** "Gentlemen. That man found love in Europe. Last time a woman held me like that, she charged by the hour. He's getting it for free. Respect the hustle."
   > **Bradley:** "She's holding him AND the paper. That's a load-bearing woman. Respect."
   > **Chadwick:** "Chat. Chat. It's a Renaissance painting. It's a Renaissance painting in a toilet. Clip it."
4. **The toilet paper (PROPOSED):** the roll is on the arm under his head. Lord Pilsner reaches for it.
   > **Token Attendant** *(eyes shut, smiling)*: "Two tokens."
   > **Lord Pilsner:** "For toilet paper?"
   > **Token Attendant** *(asleep)*: "...left side... always hit her on the left side..."
5. **Waking him (PROPOSED):** pressing the button on him again snaps him straight into service voice without opening his eyes:
   > **Token Attendant:** "WELCOME to the Absinthe Arcade! Tokens are one SOV! Toilet paper is complimentary!" *(pause)* "...For now."
   > **Token Attendant:** "If you see a green lady, she's with me." *(He nuzzles the statue and is asleep again.)*
6. **Exit (PROPOSED):** the bros leave him there.
   > **Lord Pilsner:** "He works here, drinks here, sleeps here. That's not a job, boys. That's a lifestyle brand."
   > **Bradley:** "I'm gonna be that guy one day."
   > **Chadwick:** "You're already that guy. You're just not in the arms of anything."

### Post-Interaction (PROPOSED)
**Back at the token machine, any later visit**:
> "Welcome! One SOV, one token!" *(beat)* "I was inspecting the dispenser."

### If Player Declines / Alternative Path (PROPOSED)
If the bros never go into the bathroom after 01:00, the scene never plays. He is at the token machine every visit with no idea anyone has missed anything.

### Callback Dialogue (Return Visits) (PROPOSED)
| State | Line |
|-------|------|
| After the discovery, bros mention the statue | "Her name's not important. She's a professional." |
| After the discovery, Bradley asks about the keys | "These open every machine in the building. And one heart." |
| Tab open (Cara's 21st, fled) | "I don't do tabs. I do tokens. Tokens don't remember you." |
| The token machine with 0 SOVS | INSUFFICIENT CREDITS *(ruled; he gives it two thumbs up)* |

---

## 📅 Schedule & Location

### Primary Schedule (PROPOSED)
| Time | Location | Activity |
|------|----------|----------|
| 10:00–18:00 | TOKENS HERE machine (`aa_node_token_exchange`) | Selling tokens, clearing jams |
| 18:00–01:00 | Hall, roaming between machines | Clearing ticket jams; bathroom rounds on the hour |
| 01:00–04:00 | The Arcade bathroom | Asleep in the statue's arms **[CANON beat]** |
| 04:00–10:00 | Offscreen | — |

### Positioning Notes
- Home spot is the token machine, near Backpack Girl's floor nest on the primary route (v8 positions).
- He moves to whichever ticket dispenser jams (skee-ball, foosball, DDR, cabinets): one visible jog-and-smack per jam (PROPOSED).

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Tokens (TOKENS HERE machine) | 1 SOV each **[ruled 2026-11-10]** | 1 token | Arcade currency |
| Unjam a ticket machine | Free | — | Releases stuck tickets (PROPOSED flavour) |
| Toilet paper | "Two tokens" (asleep, PROPOSED gag, not a real charge) | — | No mechanic |

### Hidden Details / Easter Eggs (PROPOSED)
- Examine the statue in the bathroom: *"A bronze Green Fairy, arms held out. A toilet roll hangs on her left forearm. She has the expression of a woman who agreed to hold one thing."*
- Examine the empty glass on the cistern: *"An absinthe glass, a slotted spoon, no sugar cube. He skipped the sugar. A professional."*

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Prize Bartender (`prize_counter_bartender.md`) | Separate employee **[CANON — author]**. Same flair rules. The bartender got the bar; he got the toilets. He doesn't seem to mind. The bartender minds for him |
| Arcade Employee (`absinthe_arcade_npcs.json`) | Also listed as floor staff who resets machines. See open question 3 |
| Backpack Girl Who Never Left | Sits beside his token machine every night. He gives her the tokens the machine spits out by accident (PROPOSED) |
| The Green Fairy statue | It's complicated (PROPOSED) |

### Territory / Social Dynamics
- He is the only staff member who goes into the bathroom.
- Every cabinet villain doc already names him as the man who sells the tokens that release them; that stays.

---

## 🔄 Recurring Appearances

### Within Debaucheryville
- Token machine on every Arcade visit.
- Jam-clearing runs during any ticket game.
- The bathroom scene, once.

### In Other Cities
None (PROPOSED).

### Evolution Through Game
After the discovery he never mentions it and denies it if asked. The statue's toilet roll is always full afterwards (PROPOSED).

---

## 🎬 Animation States (PROPOSED)

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| count_tokens | Counting tokens into the apron pouch | 40% |
| tap_price_board | Taps 1 SOV = 1 TOKEN, proudly | 30% |
| flair_adjust | Straightens a button | 20% |
| hiccup_green | A small green hiccup (after 22:00) | 10% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| jog_to_machine | A ticket machine jams |
| left_side_smack | Clears the jam |
| sleep_in_statue_arms | The bathroom scene **[CANON beat]** |
| sleep_service_voice | Waking line, eyes still closed |

### Sprite States
| State | When Used |
|-------|-----------|
| on_shift | Token machine / roaming |
| asleep_statue | Bathroom, 01:00–04:00 |

---

## 🎯 Quest Integration
- **Quest**: none. The bathroom discovery is a standalone scene (PROPOSED).
- **Items Acquired From This NPC**: tokens (1 SOV each).

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The bathroom door opening on the statue holding him and the toilet roll.
2. "Two tokens." with his eyes shut.
3. Chadwick filming the "Renaissance painting".

---

## 🗣️ Voice Direction
- **Accent**: PROPOSED: local, bright, sing-song host voice.
- **Tone**: game-show cheer for tokens; tender for the machines; the same game-show cheer, slurred, from the statue.
- **Delivery**: "WELCOME to the Absinthe Arcade!" is a reflex. It comes out at full volume even when he's asleep.

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ (uniform canon; details PROPOSED) |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ PROPOSED |
| Schedule & location specified | ✅ PROPOSED; bathroom location open |
| Connections to other NPCs | ✅ |
| Recurring appearances planned | ✅ |
| Animation states defined | ✅ PROPOSED |
| Quest integration documented | ✅ none |
| Sprite notes for artists | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ they want his life |
| World consistency (city names) | ✅ no real places; real brands (TGI Fridays, *Office Space*, Tamagotchi, Pokémon) keep real names |
| Name unique | ✅ all three options grep clean |

---

## ❓ Open Questions for the Author
1. **Name:** Out of Order Ota / Jammin' Jarda / Thirty-Seven Pieces.
2. **Which bathroom?** The Arcade has no public-restroom screen. The hall art (v8f) and the interior manifest show no restroom door and no statue; the only Arcade bathroom in the design files is the hidden **Claw Machine Maintenance Closet Restroom** (`design/World Design/Debaucheryville/clawmachinemaintenanceclosetrestroom.md`), a mop-closet-sized room behind the broken DDR's 3-token unlock, with no statue. Options: (a) put the statue and the scene in that closet restroom; (b) a new public Arcade restroom screen (needs art and a hall exit); (c) another existing screen.
3. **Overlap with the Arcade Employee:** the roster's Arcade Employee (`debaucheryville_npc_arcade_employee_01`) is floor staff who resets machines. Does the Token Attendant now own machine fixing, with the Arcade Employee kept for the club-flyer and claw-win reactions, or are they merged?
4. **The statue:** a bronze Green Fairy (draft) or something else? One statue, or several ("one of the statues")?
5. **Scene trigger:** first bathroom visit after 01:00 (draft), or tied to something else?
6. **Every line of dialogue** in this file is a draft for approval.

---

## 📝 Development Notes
- The bathroom scene needs a bathroom screen (see open question 2) and a statue prop with the toilet roll.
- He is an NPC drinking, not the bros, so the intoxication-law review is not triggered.
- The INSUFFICIENT CREDITS screen on the token machine at 0 SOVS is ruled (round v25).

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] No crypto content
- [x] The bros are never scam-aware
- [x] Nothing winks

### Satirical Target Verification
- [x] Satire is sharp and specific: forced-fun barcade flair culture and the staff who absorb it
- [x] NPC is never boring, corporate or professional
- [x] Humor is witty, never a hedge

---

## 🔧 Development Status
- **Status**: Drafted (author's design canon; name, lines, staging PROPOSED)
- **Profile File Location**: `design/worlds/debaucheryville/npcs/Absinthe_Arcade/token_attendant.md`
- **Registered In**: `absinthe_arcade_npcs.json` — **Yes** (existing entry, description updated 2026-11-11)
- **Sprite Sheet**: `token_attendant.png` (named in the roster; not yet specced). Needs an extra asleep-in-statue pose

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-11 | Initial profile from the author's round v25 design | Claude draft for machsheltie |
