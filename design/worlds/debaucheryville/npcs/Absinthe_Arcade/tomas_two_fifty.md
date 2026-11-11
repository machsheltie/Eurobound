# NPC Profile: Tomáš "Two-Fifty" (the Prize Counter Bartender)

*"Hey, Grandpa... you forgot to settle your tab. Maybe it's just the dementia."* **[CANON — author]**

> **Source and status.** The author designed this NPC in the ChatGPT chat "Absinthe Arcade Exterior Design".
> Lines and beats marked **[CANON — author]** are the author's words. Lines marked **[CANON — approved draft]**
> come from the ChatGPT draft the author approved ("Yes!!! That's exactly it!!! ... The rest between him and
> the bros is perfection."). Everything else in this file is a Claude draft and is
> **PROPOSED — NEEDS AUTHOR RULING**, including every unmarked line, the name tag, the schedule,
> the animations and the sprite notes. **Name ruled 2026-11-11 (round v28):** Tomáš "Two-Fifty" **[CANON — author]**.

## 📋 NPC Identity
- **NPC ID**: `debaucheryville_npc_tomas_two_fifty_01` (was the working ID `debaucheryville_npc_prize_bartender_01`; renamed round v28)
- **Display Name**: **Tomáš "Two-Fifty"** **[CANON — author, ruled 2026-11-11 round v28]**
- **Internal Name**: Tomáš, the prize-counter bartender
- **Role**: Bartender / Prize Redemption counter operator / tab collector / quest reactor
- **Associated Quest**: Grandpa Provides, `debaucheryville_sidequest_grandpa_provides_01` (see `design/quests/debaucheryville/grandpa_provides.md`)
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), the prize section built into the broken end of the cracked-absinthe-bottle bar (`aa_node_bottle_bar`, Prize Redemption counter `prize_redemption_counter`), Debaucheryville
- **Secondary Appearances**: wherever the bros' next game is (the tab), the Arcade's front door (the tab, again)

> **Roster — RULED (round v25, 2026-11-11):** this bartender and the Token Attendant, **Jakub "Tokens" Dvořák**
> (`debaucheryville_npc_arcade_token_attendant_01`, `jakub_tokens_dvorak.md`), are **separate people**. The bartender
> runs the bar and the prize counter; the Token Attendant fixes the ticket and token machines and services the
> bathrooms. The 2026-11-10 round also lists "the bartender, bouncers and a
> birthday party" from the author's ChatGPT chat "create hero image prompt" as hall NPCs; this file assumes
> that bartender is this one.

---

## 🎭 Core Concept

### What They're Actually Doing
He is a bartender. He wants to pour drinks, ring up drinks, and be tipped on drinks. Management bolted a carnival prize booth onto the end of his bar, dressed him to match it, and made him the man who trades sticky orange tickets for wax lips. Every grown man who walks up holding a fistful of tickets instead of a drink order costs him a tip. He serves them anyway, slowly, with his whole face. **[CANON — author: "He looks bored and annoyed when people show up wanting to exchange tokens for prizes instead of order a drink and should be passive aggressive kind of surly over it and bored acting."]**

When the bros finally do give him something, it is the **Promise-ish Ring** (a five-ticket plastic ring, ruled name round v28), as a tip, for handing them their prizes. **[CANON — author]** He gets his revenge by doing the one thing a bartender loves most: running a tab on somebody else's name.

### What Bros Believe
- **Lord Pilsner** thinks they have a rapport. The man laughs at nothing Pilsner says, which Pilsner reads as "dry European humor that only respects the real ones."
- **Chadwick** thinks the striped blazer is ironic streetwear and asks where he got it, twice.
- **Bradley** thinks the prize counter is the VIP section, because it is roped off by a strand of plastic flags.

### The Comedy Gap
The bros think a man in a carnival costume is there to entertain them. He is there to sell drinks and he hates the costume more than they will ever hate anything. The satire target is the Dave & Buster's / TGI Fridays model of forced-fun hospitality: mandatory flair, mandatory cheer, a whole adult bar demoted to a ticket booth. He refuses the cheer and keeps the flair, because the flair is in his contract.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 20s to mid-30s (PROPOSED) |
| Build | Average, slouched against the bar like it owes him money |
| Height | Average |
| Energy | Bored. Annoyed. Unhurried |

### Clothing **[CANON — author: striped blazer, black pants, goofy hat, name tag, TGI Fridays-type tacky swag]**
- **Striped blazer**: Candy-stripe carnival-booth blazer, red and white (colours PROPOSED), sleeves pushed up to the elbow as the only act of rebellion the dress code allows.
- **Black pants**: Plain black work pants. The one item of clothing he chose.
- **Goofy hat** (PROPOSED design): a straw carnival boater with a hatband made of a strip of real arcade tickets, and a little spring-mounted foam star on top that bobs every time he sighs. He sighs a lot. The star never rests.
- **Name tag**: Oversized, plastic, says the ruled name (see Display Name). PROPOSED extra line under the name: **TRAINEE**. He has worked here nine years.
- **Accessories**: TGI Fridays-style flair: buttons and pins all over the blazer lapels (ASK ME ABOUT OUR PRIZES, I ♥ TICKETS, a smiley face, a pin of a pint glass he has turned upside down).

### Distinguishing Features
- Exhales through his nose before answering anything about prizes
- Wipes the same spot on the bar for the whole conversation
- Lights up by about two percent when somebody orders a drink, then drops back down
- Never runs. Never hurries. Appears anyway, which reads as faintly supernatural (PROPOSED: he is always exactly where the bros are heading)

### Sprite Notes
128x128 semi-realistic per `design/style_guides/character_sprite_pipeline.md`. The read at thumbnail size is **stripes + hat + slouch**: the brightest, happiest costume in the building on the least happy body in it. The face carries the joke (half-lidded, unimpressed, mouth flat) and must stay readable at depth-curve scale behind the bar. The foam star on the hat is a secondary-motion element; it bobs on every sigh frame. Movable NPC sprite, never painted into room art (ruling 2026-11-09).

---

## 🧠 Personality

### Archetype
**The Reluctant Carny** — a real bartender trapped in a novelty job. He has decided the dignified response to a humiliating uniform is to do the absolute minimum inside it, at full surliness, without ever technically breaking a rule. He is passive-aggressive, not aggressive: he will hand you the wax lips. He will hand you the wax lips so slowly that you understand everything he thinks of you.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Bored | Treats every prize redemption as the four-hundredth of his shift, because it is |
| Passive-aggressive | Says "sure" in a way that means "no," and "great" in a way that means "I will remember this" |
| Surly about tickets | Considers tickets a currency worth nothing that is also sticky |
| Alive only for drinks | A real drink order is the only thing that briefly reanimates him |
| Petty, patient | Will wait an entire night to hand a man a bill he did not agree to, and enjoy every second |

### Internal Monologue (PROPOSED)
> "Five tickets. He's going to count them out loud. He's counting them out loud. Of course he is."

### Motivation
Tips. The prize counter pays none. The bros are the first customers all week to hand him something he can turn into money, and that something is a bar tab with a forty-year-old man's face on it.

---

## 💬 Dialogue

### Approach/Greeting (PROPOSED)
**Bros walk up holding tickets**:
> "...You know this is a bar. There's a whole bar. Right here. Behind the wax lips."

**Bros still holding tickets**:
> "Tickets. Great. My favourite currency. Worth nothing, and sticky."

### Key Interaction Dialogue — The Tip **[CANON — author beat]**
*The bros redeem the Promise-ish Ring (5 tickets, junk shelf). He hands it over.* **[CANON — author]**

**Tomáš** (flat) **[CANON — author]**:
> "What... no tip?"

*The bros confer. They hand him the ring they just bought. He sighs and rolls his eyes* **[CANON — author]** *while the bros act like they just did him a favour.* **[CANON — author]**

*(No bro lines: the favour is played as action only. Round v28 stripped the proposed lines.)*

### Prize Redemption barks (PROPOSED)
| Trigger | Line |
|---------|------|
| Junk-tier prize | "Thirty-five tickets. For a hand. Sure. I'll get the hand." |
| "Better"-tier prize | "Two and a half thousand tickets. That's seven hundred SOVS in tokens. That's ninety drinks. I would have poured you ninety drinks. I want you to sit with that." |
| Bros ask about the whistle | "The whistle is gone. I removed the whistle." (the 15-ticket whistle he regrets, **[CANON — approved draft]** as a shelf item) |
| Not enough tickets | "You're eleven tickets short. Go punch a frog. They pay out." |
| Bros order a drink instead | *(two percent brighter)* "Finally. A customer." |
| Bros order a drink, then ask for prizes too | "And there it went." |

### Orders to Jakub **[CANON — author, round v28]**
The bartender orders the Token Attendant around. When he sends Jakub "Tokens" Dvořák to service the bathroom:
> **Tomáš**: "Tokens. Toilet."

### The Tab (at the next game) **[CANON — author + approved draft]**
*APPROVED (round v25): he appears beside whatever the bros head to next, as they head to it, holding the bill: **40 SOVS** for five test tubes. The tab does not grow. He clearly enjoys this, after being tipped a cheap plastic ring.* **[CANON — author]**

**Tomáš** **[CANON — author]**:
> "Hey, Grandpa... you forgot to settle your tab. Maybe it's just the dementia."

**Lord Pilsner** **[CANON — approved draft]**: "I offered to buy ONE girl ONE drink."

**Tomáš** **[CANON — approved draft]**: "And yet you inspired so much joy."

**Lord Pilsner** **[CANON — approved draft]**: "I'm not paying for all of these."

*Across the room, Cara's group raises their test tubes.* **GIRLS** **[CANON — approved draft]**: "GRANDPA GUY!"

**Tomáš** **[CANON — approved draft]**: "You've built a legacy."

### If Player Declines **[CANON — approved draft]**
> "Okay."

*He walks away.* **Lord Pilsner**: "See? You just gotta stand your ground."

### At the Door **[CANON — approved draft; door lines APPROVED round v25]**
*Still in the striped blazer, still bored, standing beside the exit.*
> "Forgot something."

- **Pay** → **Tomáš**: "Grandpa provides." *(Pilsner dies inside.)* (The bartender says it; approved with the door lines, round v25.)
- **Refuse** → *sigh.* "Gentlemen?" → **Accounts Receivable** step in → "Our guests are experiencing a billing dispute." → battle. After the bros win and flee, from the doorway: **"Service charge."** (all **[CANON — approved draft]**). The service charge is a flat **10 SOVS**; the open tab is then 50 SOVS, greeted with "Tab's open" on every visit, no second fight (APPROVED round v25).

### Callback Dialogue (Return Visits)
| State | Line |
|-------|------|
| Tab unpaid (fled) | "Tab's open." **[APPROVED round v25]** |

---

## 📅 Schedule & Location (PROPOSED)
| Time | Location | Activity |
|------|----------|----------|
| 14:00–20:00 | Bar / prize counter | Wiping, sighing, redeeming tickets at quarter speed |
| 20:00–02:00 | Bar / prize counter | Peak shift; Cara's group present; the tab event runs here |
| 02:00–04:00 | Bar | Last call; reanimated by drink orders |
| 04:00–14:00 | Offscreen | — |

### Positioning Notes
- Fixed behind the prize section of the bar; the counter is at bro waist height (ruling 2026-11-09).
- During the tab event he leaves the bar to stand beside the next cabinet the bros approach, or beside the front door.

---

## 🎒 Inventory / Services
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Prize Redemption (13-prize catalogue) | 15–2500 tickets | 0–3 SOVS | See `design/World Design/Debaucheryville/items/absinthe_arcade_prize_catalogue.md` |
| Junk shelf (separate from the catalogue; **APPROVED round v25**) | 5–15 tickets | 0 SOVS | No effects. The **Promise-ish Ring** (5 tickets; name ruled round v28), parachute men, temporary tattoos, the whistle he regrets (15 tickets). Catalogue duplicates (sticky hand, vampire teeth, maze puzzle) are off the shelf. Other item names (Writers' Room) and the parachute-men/tattoo prices: PROPOSED — NEEDS AUTHOR RULING |
| Neon test-tube shots | **PROPOSED** (see quest doc) | — | Bar drink; how it plays for the bros, if at all, is an intoxication mechanic and needs the 10-point review first |
| Bar drinks generally | **NEEDS AUTHOR RULING** | — | No Arcade bar price list exists in the design files yet |

### Hidden Details / Easter Eggs (PROPOSED)
- Examine the flair: the upside-down pint pin is the fifteenth piece. He took the fourteenth off on purpose to see if anyone would notice. Nobody noticed. He added the pint.

---

## 🔗 Connections
| NPC | Relationship |
|-----|--------------|
| Cara and her group | His best customers of the night. They order drinks, not prizes |
| Accounts Receivable (`design/worlds/debaucheryville/villains/absinthe_arcade/accounts_receivable.md`) | He says one word ("Gentlemen?") and they appear |
| Jakub "Tokens" Dvořák, the Token Attendant (`jakub_tokens_dvorak.md`) | A separate employee (ruled round v25), same flair dress code. He fixes the machines and cleans the toilets; the bartender pours and judges. Tomáš orders him around: "Tokens. Toilet." **[CANON — author, round v28]** |

---

## 🔄 Recurring Appearances
- Behind the bar on every Arcade visit; dialogue state follows the tab outcome (paid / unpaid).
- No other cities (PROPOSED).

---

## 🎬 Animation States (PROPOSED)
| Animation | Description |
|-----------|-------------|
| idle_wipe | Wipes the same spot on the bar |
| idle_sigh | Long exhale; hat star bobs |
| redeem_slow | Hands a prize over at quarter speed |
| eye_roll | The tip reaction **[CANON beat]** |
| present_tab | Holds the bill out at arm's length |
| point_gentlemen | Two-finger gesture that summons the enforcers |
| drink_perk | The two-percent brighten |

---

## 🎯 Quest Integration
- **Quest**: Grandpa Provides — `design/quests/debaucheryville/grandpa_provides.md`
- **Role**: Bartender who pours the round, tab collector, enforcer summoner
- **Items Acquired From This NPC**: prizes (tickets); none from the quest itself

---

## 🗣️ Voice Direction
- **Accent**: PROPOSED — local, flat, perfect English. He speaks it better than the bros.
- **Tone**: monotone for prizes; one notch of life for drinks; quiet, unmistakable satisfaction for the tab.
- **Delivery**: never raises his voice. "Gentlemen?" is a question asked the way a dentist says "little pinch".

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ (hat, colours, flair PROPOSED) |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ canon beats + PROPOSED barks |
| Schedule & location specified | ✅ PROPOSED |
| Connections to other NPCs | ✅ |
| Animation states defined | ✅ PROPOSED |
| Quest integration documented | ✅ |
| Sprite notes for artists | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| World consistency (city names) | ✅ no real places; real brands (TGI Fridays, *Office Space*) keep real names |
| Name unique | ◐ ruled round v28; the full name is unique, but the first name Tomáš is shared with a Velvet Curtain Club bouncer ("Tomáš and Marek"). Flagged to the author |

---

## 🔧 Development Status
- **Status**: Drafted (canon beats from the author's chat; name ruled round v28; all unmarked content PROPOSED)
- **Profile File Location**: `design/worlds/debaucheryville/npcs/Absinthe_Arcade/tomas_two_fifty.md` (renamed from `prize_counter_bartender.md`, round v28)
- **Registered In**: `absinthe_arcade_npcs.json` — **No** (name ruled round v28; not yet registered)
- **Sprite Sheet**: not yet specced

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-10 | Initial profile from the author's ChatGPT chat "Absinthe Arcade Exterior Design" | Claude draft for machsheltie |
| 2026-11-11 | Round v25: separate from the Token Attendant; tab 40 SOVS, timing, door lines, 10 SOVS service charge, Accounts Receivable, junk shelf approved. Name still open | Claude for machsheltie |
| 2026-11-11 | Round v28: name ruled Tomáš "Two-Fifty" (losing options dropped); file renamed from `prize_counter_bartender.md`; the ring is the Promise-ish Ring, tip beat only (no pinky ring); "Tokens. Toilet." added; proposed tip lines and return-visit lines stripped | Claude for machsheltie |
