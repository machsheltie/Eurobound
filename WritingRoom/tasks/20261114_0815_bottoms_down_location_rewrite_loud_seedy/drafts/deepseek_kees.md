# Slice B draft — npc_kees.md replacement text

**Coverage:** 🎭 Core Concept (all subsections), 👤 Appearance (all subsections), 🧠 Personality (all subsections), 🎒 Inventory / Services → `### Hidden Details / Easter Eggs` **only**, 🔗 Connections (all), 🔄 Recurring Appearances (all). All headings kept verbatim so the integrator can drop text straight in. Everything not in this file stays as-is.
**Reviewer:** Mistral (Slice C) — every prop named here must exist in the PNG doc's Sprite Sheets 1/2/3/6, or be cut. Kimi reviews against Slice A on integration.
**Canon kept verbatim:** all twelve words, "Jenever. Rookie or geezer. Beer also. Choose.", the sanctioned extensions ("Sawdust is there for this. Not the first time. Continue.", "The chair is there.", "Acceptable. Back room is there.", "Seamus."), the twelve-word vocabulary block, every id/slug/flag/price/number, the Blarney Trap gate order, "Wrong."/"Correct." near-identical rule, the 100-Year Barrel never opens.
**Cut from this file:** "Dutch"/"Belgian"/"Irish" wherever a player could read it, "proeflokaal", the "second van der Berg-style ambiguity" aside, and the original internal monologue, which was a paragraph explaining the joke to the reader. (Voice Direction's "Accent: Dutch" is outside my slice — see flag 3.)
**[PROPOSED]** marks a detail that is not in any existing doc. All are props or staging, none are mechanics, numbers, prices, items or names.

---

## 🎭 Core Concept

### What He's Actually Doing
Tending a jenever bar that has not changed because it has not needed to. He fills tulip glasses above the brim so surface tension makes them impossible to lift, and waits to see whether the customer bends to the bar or tries to pick the glass up like a man. He runs a five-glass blind tasting with two words of feedback per round. He checks bottle openers at the door — one from Publandia, one from this building — and he does not make exceptions.

He is also, technically, the man who keeps score. The chalkboard behind him is not decoration; it is a record, it is accurate, and he is the one who updates it. **[PROPOSED]** Pim rings the bell, Kees marks the tally. He does this the way other men take out the rubbish: without ceremony, without malice, and slightly too often.

### What Bros Believe
That this is a challenge and they are winning it.

- **Lord Pilsner** has read the scoreboard and decided it is a leaderboard, and that he is going on it. **Bradley** has read two inches of sawdust as gym flooring and wants to do squats on it. **Chadwick** is filming the ceiling, saying the word "content," and has decided the fall, the bell and the second fall are three separate pieces.

Nobody is frightened. Nobody is disgusted. The room smells like bleach and wet sawdust and they think it smells like somewhere they are about to be great in.

### The Comedy Gap
Kees is not testing anyone. The glass is full because that is how jenever is served. The sawdust is on the floor because things get spilled. The gauntlet is a tasting flight with questions attached. The padding on the beams is there because the ceiling is low and the patrons are not.

The bros walk in and read a personal challenge into a building that has been doing the same four practical things since before their country existed. Kees has never modified his expression for a customer, has never warned one, and does not intend to start.

### The Cross-City Gate
Kees runs the Publandia cross-reference. **The Blarney Trap Bottle Opener is a hard requirement** — without it, no tour, no gauntlet, no stamp, no negotiation. His recognition of it is one word: *"Seamus."* He means Seamus O'Brien, owner of The Blarney Trap. He does not elaborate and has never needed to.

The check happens before he says anything at all. He looks at the opener, then at the player, and the frame chosen for that look is chosen by the inventory, not by the conversation.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 60s |
| Build | Built like the barrel he tends. Forearms from four decades of ceramic jugs. |
| Height | Comfortable under a low ceiling, which is more than can be said for anyone taller than 5'10" |
| Energy | Neutral. Permanently, comprehensively neutral. Nothing in the room requires him to react to it. |
| Silhouette | Barrel. Apron. Jug. At 231px he reads as a shape standing behind a slab, and the slab reads as a bar. That is all he needs to be. |

### Clothing
- **Apron older than most tourists**: Heavy canvas, jenever-stained to a single uniform amber, stiff enough at the hem that it does not move when he turns. The ties are knotted rather than tied, and have been knotted so long the knot has a shape of its own.
- **Collarless shirt, sleeves rolled**: The same one or six identical ones. Nobody has established which. He is not going to say.
- **Accessories**: The ceramic jug, functionally part of his right hand. A cloth folded over the rail that has not been used on the bar in years, because the bar does not need it and he does not want to.
- **Footwear**: Boots, sawdust to the ankle by mid-shift. The sawdust does not come off them. It has been in the boot a long time.

### Distinguishing Features
- **Permanently neutral expression.** Nothing surprises him. Nothing impresses him. Nothing. This is the character and it is also the reason the room has to do all the talking.
- **The pour**: jug raised, glass placed, stream to the brim, surface tension achieved, jug withdrawn, expression unchanged. Three frames, no variation, ten thousand repetitions.
- **The nod**: two frames. It is the highest praise available anywhere in Shamsterdam and most players will never see it.
- **[PROPOSED] His hand goes to the chalk before the order is finished.** Not rudeness. He has done the arithmetic already, the arithmetic is usually right, and on the rare occasion it is wrong he is exactly as unbothered by that.
- **He does not look up at the bell.** Everyone else in the room does. He is already reaching for the chalk.
- His "Wrong." face and his "Correct." face are near-identical **by design**.

### Sprite Notes
Sheet `npc_kees_pim.png` (512×512; 64×96 character frames, 128×128 portraits). Service row at y=0: Idle, Pour Frames 1–3, Nod Frames 1–2, "Wrong.", "Correct." Instruction row at y=96: Demonstrating the Bow, Pointing at Sawdust, Pointing at Chair, Pointing at Back Room, and the **three opener-check frames** (Blarney Trap Only / Both Openers / No Shamrock). Portraits at y=192: Neutral Eternal, and The Nod — *the single frame in the entire game where he approves of you*.

**Critical asset-doc constraints, carried forward:**
- **"Wrong." and "Correct." must be near-identical.** The joke is that his face carries no information, so the gauntlet UI must carry it instead.
- **The three opener-check frames are selected by inventory state before any dialogue plays. The Blarney Trap check happens first and gates everything.**
- **[PROPOSED] He never turns around on camera.** The scoreboard is on the wall behind him. He does not need to look at it and the player does not need him to; the tally is readable over his shoulder in every portrait, which the art gets for free.
- **[PROPOSED] No bell-reaction frame exists and none should be drawn.** Every other sprite in the location gets one. He is the only character in the room who does not turn his head.

---

## 🧠 Personality

### Archetype
**The Bar Itself** — Kees is less a character than a fixture with opinions he does not share. Four hundred years of the same room distilled into twelve words. He is neither warm nor cold; he is *neutral* in a way that reads as either, depending entirely on what the customer brought with him.

He has served more jenever than water in his lifetime and it has removed from him any capacity for surprise. It has not removed his handwriting, which is small, level and very good, and which appears on the board several times an hour.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Absolute neutrality | Not stoicism, not disdain. An actual absence of reaction. He is the only man in the room not performing. |
| Total economy of language | Twelve words. It has been enough and it is enough now. |
| Precision of pour | Above the brim, every time, without measuring. Nobody has ever seen him overfill past the meniscus. |
| Unmoved by failure | "Sawdust is there for this. Not the first time. Continue." There is no judgement in it and there is no comfort in it either. |
| Immovable on the gate | No shamrock, no tour. He will wait. He is very good at waiting. |
| **[PROPOSED]** Keeps the board himself | Pim rings, Kees marks. He has never once got a tally wrong and has never once been asked about one. |
| **[PROPOSED]** Water is free and nobody asks | There is a bottle under the bar. It comes out for the ones in the chair. It goes back. He does not mention it. |

### Internal Monologue
> "Six since the door opened. Pim rang four. The other two did not need the bell, they needed the chair.
> The board says eleven for the week. I do not remember the tenth. I do not need to; the board remembers it, and the board is the record.
> The one at the end of the bar has been coming fifty years and has never been on the board, and he drinks the oldest thing in the building, and I have never worked out how. He is not going to tell me. He has a newspaper.
> The bucket sits on a stool because a man should have somewhere to be proud of. The chair is bolted because a man should not be able to take it home.
> Pim will walk them out at eleven. He always does. I will sweep."

### Motivation
None stated. None inferable. He opens at twelve and closes at eleven and pours what is asked for. The tasting house has been in the family three generations and he is the current arrangement.

He has one preference and it is not a warm one: he would rather they bend than lift. Not out of kindness. The bending ones stay upright, and upright customers order again, and the ones who lift end their evening on his floor with his chalk in their name.

---

## 🎒 Inventory / Services

### Hidden Details / Easter Eggs
- **The 100-Year Barrel**: In the back room. Touched annually, never opened, allegedly. Examine it. Kees will not discuss it. Pim will, at length, and knows nothing.
- **The traditional method diagram**: On the wall, in frame, from the moment the player enters. Three hand-drawn panels and a coffee ring over the third one, which is the panel showing the man in the sawdust. Every customer who spills has walked past it. Examine text confirms it has been there since 1889.
- **[PROPOSED] The board's record**: Thirty-one. Chalked, underlined twice, in a hand that has not changed in decades. It is not a boast. It is a measurement. The `TODAY` column is never empty and the space beneath it has been pre-drawn, so the next mark has somewhere to go.
- **The bottles without labels**: 200+ on the wall, arranged by age — rookie, geezer, fossil, and a fourth section with no label. Ask about the fourth section: "Don't ask." That is the entire response and it is also the section's name.
- **[PROPOSED] The labels over labels**: Several bottles wear a handwritten label pasted over an older handwritten label, which is pasted over a printed one. Nobody has peeled one back. Examine text confirms only that the top label is the newest and the newest one is not new.
- **The newspaper clippings**: Notable patrons across four centuries. Examine them. They are all the same photograph: somebody horizontal, somebody else pointing. Even the frames are the same frame.
- **The spill kit by the door**: mop, scoop, sack of sawdust, and a card reading "SELF SERVE." Examine it. The mop is dry. It has been dry a long time, and nobody has ever used it, and the sawdust is replaced weekly regardless.
- **[PROPOSED] The chair's tag**: the seatbelt bolted to the lawn chair has a luggage tag on it, in marker, with a man's first name on it. Not a patron's name. Not anyone the player will ever meet. Nobody at the bar has ever taken the tag off. [Deliberately no dog, no pet, no mascot: the tag is a luggage tag, and the chair is a chair.]
- **The distance markers on the floor**: painted, radiating out from the bar — "1M — 2M — 3M — PERSONAL BEST." Examine them and Pim, unprompted, tells you the personal best is a lie, and that he was there, and that it was closer to two.
- **The bell**: mounted behind the bar. Examine it and Kees says nothing at all, and the silence has a length to it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Assistant Barkeep Pim | Nephew, "volunteered" into the family business. Restocking, sawdust, ringing the bell, physical support. **Answers every question requiring more than four words.** Kees has never thanked him out loud and has also never hired anyone else. |
| Seamus O'Brien (The Blarney Trap, Publandia) | The cross-city gate. Kees's recognition of the shamrock opener is one word: "Seamus." They have an arrangement neither has ever described. |
| Brewmaster Hendrik (The Wobbly Windmill Brewery) | The other half of the Shamsterdam brewery tour. Mutual respect expressed entirely through stamps. Hendrik on Kees: "He does not stamp. If Kees has stamped you, you have done something." |
| The Regular (Ancient) | Fifty years, same spot, one jenever per hour, exactly, and never once on the board. Potential couchsurf host — Kees translates his mutter into "He says you can stay." |
| Opa Cees (Tram Track Magnets) | **Same first name, different character.** Both are named Cees; one goes by Kees, the family diminutive, and is a bartender in Old Town; the other is Opa Cees, a mechanic on the south side. They have never met and must never be staged together. |
| Maarten (The Salty Swallow) | Same district generation. They nod. That is sufficient. |

### Territory / Social Dynamics
- The bar is Kees's and the room defers to it entirely. Pim manages the floor, the sawdust, the bell, and every sentence longer than four words; Kees manages the pour, the board and the chair.
- The Regular has territorial rights to the end of the bar and has held them for fifty years. Kees has never had to enforce this, does not expect to, and would not enjoy it.
- **[PROPOSED]** The board is public and the board is accurate. That is the only social contract in the building and every regular has signed it without being asked.
- Cross-city: Kees and Hendrik form a two-stamp gate on the Canal Courage passive. Neither can be bypassed. Neither makes exceptions. Both check the same Publandia opener first.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: The opener check. Then the glass, and the choice: bend or lift. Then the chalk, either way.
- **Gauntlet visit**: Five glasses, three rounds, The Concussion, and either "Acceptable" or the chair.
- **Post-gauntlet**: The back room, the nod on entry, and thereafter forever. The board records falls, not successes. He has never explained the distinction and nobody has asked him to.
- **Post-both-breweries**: The Hendrik acknowledgement and the unprompted pour.
- **Late game**: "Welcome," with the glass already filling, and the chalk already in his other hand.

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Publandia | The Blarney Trap | Referenced only. His entire connection to Seamus O'Brien is one word and an arrangement. | "Seamus." |

Kees does not leave the bar. He has not needed to.

### Evolution Through Game
His vocabulary does not expand. What changes is what he does before speaking: the nod on entry, the pour without an order, the jong selected for a specific debuff, the chalk put back down untouched. By the late game Kees is having a full conversation with the player using twelve words and a ceramic jug, and neither party has acknowledged that anything has changed.

---

## Flags for the integrator / reviewer

1. **Kimi's Slice A trims three canon extensions** — "Sawdust." for "Sawdust is there for this. Not the first time. Continue.", "Chair." for "The chair is there.", and shortens "Acceptable. Back room is there." **Restore the first two in `bottoms_down.md`.** "Continue" is the house's entire policy (no shame, get up, next glass). "The chair is there," delivered *not unkindly*, is his only tell in the game and the only thing stopping the location from being a place that hates tourists. "Sawdust." can survive as the walking-past bark.
2. **Bell vs chalk ownership** — Slice A has Pim ringing the bell *and* updating the board; I have Pim ringing and Kees marking. Both can be true; the two files just have to say the same thing. One-word fix at integration.
3. **Voice Direction, "Accent: Dutch, Old Town, low register"** — outside my slice and it is booth direction, not player-facing text, so I left it. If the no-nationality rule covers direction notes too, it becomes "Old Town, low register, minimal." **Author's call, not mine.**
4. **Satirical Target Verification (§ "Dutch jenever culture")** and the QA checklist ("Dutch jenever culture, proeflokaal tradition") are inside template checklist blocks — internal, not player-facing. Flagging for the integrator rather than touching them.
5. **No new names minted.** Every proper noun in this draft already exists in Slice A or in canon. "The fourth section" is a description, not a name.
6. **Nothing mechanical added.** No numbers, prices, hours, statuses, quest beats or flags. The water bottle and the chalk-in-hand are staging; the luggage tag is a prop. If any of them reads as an implementable system to anyone, cut it rather than build it.
7. **I cut my own late-game beat** — an earlier draft of this file had Kees wiping the board clean on the player's last visit. It was a soft moment, which this profile explicitly forbids ("Do not give Kees a backstory reveal, a soft moment, or a late-game monologue"). Not in the draft.
