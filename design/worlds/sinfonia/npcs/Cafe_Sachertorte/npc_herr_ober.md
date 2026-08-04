# NPC Profile: Herr Ober

*"In thirty years of service, I have never... a HORSE. A HORSE ate the Sachertorte."*

## 📋 NPC Identity
- **NPC ID**: `sinfonia_npc_herr_ober_01`
- **Display Name**: Herr Ober
- **Internal Name**: Herr Ober, Head Waiter. **"Herr Ober" is not a name — it is a form of address.** It means, literally, *Mr. Waiter*: what a guest calls the man at the head of the floor when the guest does not know him and is not expected to. **He has no first name in this game, in any file, in any line, ever.** Nobody at Café Sachertorte knows it. Two of the four current staff assume "Ober" is his surname. He has never corrected anyone and does not intend to. Any file, line, or asset that assigns him a personal name is wrong and must be corrected against this profile.
- **Role**: Head Waiter / Cultural Gatekeeper / Debt Collector / Service Interface / Quest Victim
- **Associated Quest**: `sinfonia_sidequest_fiaker_fiasco_01` ("The Fiaker Fiasco") — Phase 2, `fiaker_fiasco_cafe_phase`
- **Primary Location**: Café Sachertorte (`sinfonia_kaffeehaus_cafe_sachertorte_01`), Kaffeehaus Row, Sinfonia — the floor, between the service counter and the cake display
- **Secondary Appearances**: The café's front doorway (post-quest, 24-hour closure, drinking openly); Opera Backstage (may pursue the party for payment mid-chase); Kaffeehaus Row street (delivering the debt figure to neighbouring establishments, which is how the gossip system learns it)

---

## 🎭 Core Concept

### What He's Actually Doing

He is running a floor. Twenty-five tables, one display case, four staff, eleven hours a day, and a room that has been trading on the year 1843 since before he was born. He seats people by a system: window seating is real estate and goes to regulars; Charm 3+ gets a proper table; Charm 1+ at least keeps you away from the restroom. He knows every price on the menu, including the three that are not printed on it, and he applies all of them.

The condescension is a job function and he was trained into it. Making a tourist feel slightly uncultured is what makes the tourist order the 18 Sovs slice instead of the 12 Sovs Gugelhupf, and the house has understood this since the 1950s. He is very good at it. He does not enjoy it. It is the part of the work he would drop first if the till allowed.

He also drinks. Not much and not visibly — the staff break room has schnapps bottles that are perfectly visible through the window if the player looks, and he takes his in the four-minute gap between the lunch clear-down and Kaffeeklatsch. Everyone on staff knows. Nobody has ever said anything, because he has never once been drunk on the floor and the bow tie has never once been crooked.

Then a horse eats 340 Sovs of his café and the entire apparatus falls off him in about nine seconds.

### What Bros Believe

Lord Pilsner believes he has met the final boss of European sophistication and has entered a contest of wills. Chadwick believes the man is "in character," that this is an act the café makes him do, and that a big enough tip will break him and reveal the cool guy underneath. Bradley has read the menu correctly, is the only one who has, and is quietly ordering the Gugelhupf because it is 12 Sovs.

After the rampage they believe the 340 Sovs is a negotiating position.

### The Comedy Gap

Everything Herr Ober says to them is true. The recipe *is* unchanged since 1832. The price of the coffee they are complaining about *has not changed since 2019*. The bill *is* 340 Sovs and it is itemised and every line of it is correct. He is not scamming anybody — the hidden charges are printed, in tiny elegant font, on a menu he will hand over the instant it is requested, and he corrects pronunciation because that is what the house pays him to do.

The bros hear a villain. The player, if they look at the menu, gets the whole truth on their first visit.

And then the joke inverts and stays inverted: the most refined man in Kaffeehaus Row is reduced to screaming a compound German noun at a Lipizzan with icing on its face, and the game never lets him fully recover his footing again. There is no cruelty in it. He is the one person in the scene who did nothing wrong.

### The Name

He is addressed as "Herr Ober" by every character in the game, without exception, in every scene, forever. The player never learns his name. Once — exactly once, in the chaos, in German, in the kitchen doorway — Chef Konrad (`sinfonia_npc_kitchen_staff_01`) uses it, and the dialogue box renders it as a blank the width of a word. It is never spoken again and never explained. If the player interacts with Chef Konrad afterwards about it, Konrad says only: *"That is not for you."*

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 40s; reads a decade older, and the decade is exhaustion, not years |
| Build | Thin, ramrod posture, moves with precise efficiency; never hurries and is never late |
| Height | Tall, and uses it — he serves from a height that requires the seated guest to look up |
| Energy | Immaculate fatigue; a man holding a room up with his own spine |

### Clothing
- **Traditional black waiter's vest**: The uniform of the house, unchanged in cut since the 1930s. Brushed nightly. He owns three and rotates them so that no one ever sees a worn one.
- **White shirt with subtle monogram**: The monogram is the café's, not his. This is the single most important costume detail in the profile — the only initials on his person belong to the building.
- **Black bow tie**: Hand-tied, perfectly. Never a clip. It is straight in every sprite state in the game including `fury` and including `defeat`.
- **Pristine white apron**: Pristine until Gustav. Post-quest it carries a faint apricot-glaze stain at hip height that never comes out and that he has stopped trying to remove.
- **Accessories**: Pocket watch on a chain — checked, not consulted; he knows the time. A silver tray that he balances one-handed while doing something else with the other. A folded order pad he almost never writes on, because he does not need to.
- **Footwear**: Black, soft-soled, silent on marble. Resoled four times. The café floor eats shoes.

### Distinguishing Features
- **The pause.** He puts a beat in front of the honest word and lets the guest hear their own order come back at them. "You would like... 'a coffee.'" The pause is the whole character.
- Thin, precise moustache, trimmed to a standard nobody has asked for.
- Perpetual slight frown that is not disapproval — it is a man doing arithmetic on a floor plan.
- Corrects pronunciation reflexively, gently, mid-sentence, and then continues as though he has not.
- Under stress the English goes first and the German arrives at full volume, and the transition takes no time at all.
- Post-quest: touches the corner of the cake display case with two fingers each time he passes it. He is checking that it is still there.

### Sprite Notes

He is not a snob and must never be drawn as one. Draw a professional who is tired: the posture is immaculate and the eyes are not. The comedy comes entirely from the distance between his composure and what is happening in front of him, so his default state must be genuinely, unmockably dignified — if he looks silly at rest, the rampage frames have nothing to break.

Priority frames: the `judgment` raised eyebrow (this is the single most-used frame in the location and should be the artist's best work); the `horror` step-backward with both hands rising; the `fury` point at the itemised damage; and the `defeat` slump in front of the emptied display case, which is the frame the game holds on longest. The bow tie is straight in all four. The apron is destroyed in the last two.

Post-quest doorway variant: same sprite, unbuttoned vest, glass in hand, standing in his own front door in daylight during business hours, which for this man is the equivalent of a building on fire.

---

## 🧠 Personality

### Archetype

**The Uniform** — a man who has replaced himself, deliberately and over thirty years, with a role, a posture, and a form of address. He is not hiding a warm secret self behind the disdain; the disdain is a tool he picked up because the house pays for it, and underneath it is not warmth but a genuine, unglamorous, load-bearing professional pride. He is the reason the room works. He has been the reason the room works since 1996. Nobody, including him, considers this to be a life, and he would find the observation vulgar.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Professional pride | Absolute and unironic. He has never let a plate go out wrong. The 340 Sovs wounds him as a failure of the room, not as money. |
| Trained condescension | House policy, applied at scale, and he can turn it up or down by the guest. Never once personal. He does the same routine on a Viennese banker and takes visible satisfaction in it. |
| Quiet snobbery | Genuine, small, and about coffee specifically. He does believe that ordering "a coffee" in a Kaffeehaus is a small act of vandalism, and he is correct. |
| Secret staff schnapps | Four minutes, every afternoon, between clear-down and Kaffeeklatsch. Bottles visible through the break room window. Never on the floor, never slurred, never once late back. |
| Structural loyalty | He will absorb a rude guest, cover a dropped tray, and take the blame in front of the owner. He has never been thanked for any of it and does not expect to be. |

### Internal Monologue

> "Table nine wants the window and table nine has been here twice. Table four has been nursing that Melange for two hours and I will not move him, because in nineteen years he has never once moved. The Americans will order the Sachertorte because I have already made them afraid of the Gugelhupf, which is the better cake, which is the joke, which nobody in this room has ever been told. — The glaze is running on the second tier, someone has left the case light on— *what is—* — is that— that is an *animal*. That is an animal in my— MY CASE. MY CASE. MEIN GOTT—"

### Motivation

He wants the room to be right. That is all of it and it is not small. The floor plan, the seating order, the cake display rotating at the correct speed, the chandelier clean, twenty-five tables turning over at the correct rate — this is a machine he operates, and it is the only thing on earth he is unambiguously excellent at. He is paid poorly for it. He knows the kitchen is paid worse. He has raised this with the owner three times in eleven years, in writing, and has been thanked in writing, three times, and nothing has changed.

The 340 Sovs is not greed. It is the number required to make the room right again.

---

## 💬 Dialogue

### Approach/Greeting

**Any first entry, default — canon, ships verbatim:**
> "Welcome to Café Sachertorte. You have... a reservation?"

**Tourist detected (accent flagged, casual attire) — canon:**
> "Ah. Americans. The... terrace is available. By the restroom."

**Charm 3+ — canon:**
> "Welcome. I have a table by the window. This way, please."

### Key Interaction Dialogue — The Order

*The Order Judgment is the location's core service interaction and fires on every purchase. Canon beats, ship verbatim.*

**Lord Pilsner**: "Yeah, can we get like... a coffee?"

**Herr Ober** *(the pause is the joke and the pause is load-bearing)*:
> "Ah. You would like... 'a coffee.' How... specific."

**Ordering correctly, in German — canon:**
> "Ein Melange. Very good. Perhaps there is hope."

**Ordering the Sachertorte — canon:**
> "The Sachertorte. An excellent choice. Obviously."

**Any American request — canon:**
> "'Iced coffee.' Sir, this is not... a diner."

**Chadwick photographing the cake — canon:**
> "You take PHOTOS of the cake? This is not Instagram. This is Sachertorte."

**Complaining about the price — canon:**
> "The price has not changed since 2019. The quality has not changed since 1832."

**The house line, delivered to anyone who asks whether it is really the original recipe — canon, ships verbatim:**
> "The Sachertorte recipe is unchanged since 1832. Unlike the clientele."

**Insufficient tip — canon:**
> "...I see. Thank you for your... generosity."

### Phase 2 — The Rampage

*Canon chaos sequence. He is facing the wrong way when Gustav enters through the patio door, which is why the umbrella stand goes first. Ships verbatim.*

> "What is—MEIN GOTT! EIN PFERD!"

*Gustav reaches the display, contemplates the twelve cakes with disturbing intelligence, and selects the 85 Sovs whole Sachertorte from the centre pedestal.*

> "NEIN! NEIN! DAS PFERD FRISST DIE TORTE!"

*Two marble tables go. The chandelier does not, by about forty centimetres.*

> "THE TABLES! THE DISPLAY! THIS WILL COST—calculate—340 SOVS!"

*Gustav takes the 22 Sovs Opera Cake slice on his way through the service door. Kitchen sounds. Chef Konrad, in German, in the doorway, uses the name. The box shows a blank.*

**Post-rampage, the itemised bill, delivered in a voice that has nothing left in it — canon, ships verbatim:**
> "340 Sovs. You will pay this. Now. Or I call the Polizei."

**The breakdown, in front of the emptied case, sitting down for the first time in nine years — canon, ships verbatim:**
> "In thirty years of service, I have never... a HORSE. A HORSE ate the Sachertorte."

**On the insurance, later, to nobody — canon, ships verbatim:**
> "Insurance covers 'acts of God.' This is an 'act of HORSE.'"

### The Three Dialogue Options

*The damage tally screen resolves to one of three, all canon:*

**Option 1 — "We'll catch the horse and pay you back!"**
> "You will 'pay me back.' Yes. This is what is said." *(he writes it down, which is worse than shouting)* "340 Sovs. Your names. Your hotel. Go and catch your horse."
> **Result:** Quest continues, debt logged, `cafe_debt_340` active, service refused until cleared.

**Option 2 — "Here's 340 Sovs right now."** *(requires funds)*
> *(long silence; he counts it, twice, at the counter, in front of everyone)* "...Then there is no debt. There is only the horse." *(and, at the door, quietly, the closest thing to warmth he has)* "The Gugelhupf. Next time. It is the better cake. Nobody orders it."
> **Result:** Quest continues, no café debt, and a permanent private line unlocked that most players will never see.

**Option 3 — "That horse doesn't belong to us!"**
> "Then whose—" *(Hans-Jürgen Pferdmann arrives, breathless, and claims it)* "...Pferdmann. Of course. Of *course* it is Pferdmann." *(to the bros, without turning around)* "You are still standing in my café."
> **Result:** Hans-Jürgen takes responsibility; the party's café debt halves to 170 Sovs. Delays the chase by one scene.

### Debt Collection

**Partial payment — canon:**
> "50 Sovs received. You still owe 290 Sovs. I will remember."

**Full payment — canon:**
> "...paid in full. You may return. But I will be watching."

**Returning with the debt unpaid — canon:**
> "You. OUT. Until the 340 Sovs is paid, you are not welcome."

**The refusal-of-service line, in full, at the door, every time:**
> "We do not serve you until bill is paid. This is not personal. It has never once been personal."

### Post-Interaction

*The 24-hour closure. He is in his own doorway, in daylight, with a glass, and does not put it away when the party approaches:*
> "We are closed. Yes. In the afternoon. In the summer." *(he looks at the glass, then at them, and does not pretend)* "Thirty years I do not do this on the street. Today I do it on the street."

*The reopening, "NO HORSES PERMITTED" sign freshly hung above the patio door:*
> "It is a sign. It says no horses. I had it made. A man made it for me and he did not laugh, and I paid him extra for that."

### If Player Declines / Alternative Path

*Leaving without ordering:*
> "Of course. The door is where it was." *(He is already seating someone else. This is the most efficient dismissal in Sinfonia.)*

*Refusing to pay anything at all, repeatedly, across multiple visits:*
> "You misunderstand. I am not angry. I am *filing*." *(The BANNED board goes up on the next visit.)*

### Callback Dialogue (Return Visits)

*Debt cleared, "Valued Patron" active, every subsequent entry:*
> "Ah. The gentlemen who pay." *(a fractional nod; from him this is a standing ovation)* "The window is free."

*Ordering "The Gustav" commemorative cookie, 8 Sovs:*
> "The... Gustav." *(a very long pause)* "It sells forty a day. Forty. The Apfelstrudel sells nine." *(he serves it perfectly)* "I do not wish to discuss it."

*Late game, debt cleared, if the player orders correctly in German three visits running:*
> "You have been practising." *(He does not smile. Something adjacent to it happens and then stops.)* "Sit anywhere."

*Late game, debt unpaid, any Kaffeehaus Row establishment:*
> *(He is not here. The other waiter is, and knows the number.)* "Ah — you are the 340 Sovs. He telephoned."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 08:00–12:00 | Main floor, morning service | Breakfast menu, quiet room, the newspaper holders refilled by hand — his favourite four hours of the day |
| 12:00–14:00 | Main floor, lunch supervision | Peak table turnover; longer waits; he is at his most efficient and least available |
| 14:00–14:04 | Staff break room | The schnapps. Four minutes. Visible through the break room window if the player is looking at the right time. |
| 14:00–17:00 | Main floor, Kaffeeklatsch peak | Maximum pretension, best gossip, the Order Judgment fires most often here |
| 17:00–22:00 | Main floor, evening formal service | Pre-opera and post-opera crowds; formal dress observed; classical recording turned up |
| Quest-active | Main floor → doorway → Opera Backstage | Chaos management, then debt pursuit; may follow the party one location |

### Positioning Notes
- He stands between the service counter and the cake display, facing west, which puts the door in his peripheral vision and the case at his back. **This is why he does not see Gustav enter.** It is the only positioning error he has made in thirty years and the game is built on it.
- He greets from a fixed spot rather than approaching; the guest comes to him, and the walk across the marble is deliberate and is part of the pricing.
- He never sits. Not once, in any pre-quest state. The `defeat` frame is the first time the player sees him seated and it should land as such.
- Post-quest he keeps a sightline to the patio door at all times, including mid-conversation.

---

## 🎒 Inventory / Services

### Menu — Beverages
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Kleiner Brauner (small coffee) | 5 Sovs | Fair for the district | Removes Tired |
| Großer Brauner (large coffee) | 7 Sovs | Fair | Removes Tired, +1 Speed (1 hour) |
| Melange (Sinfonian latte) | 8 Sovs | Fair, and genuinely excellent | Removes Tired, +1 Charm (30 min) |
| Einspänner (whipped cream) | 9 Sovs | Fair | Removes Tired, Removes Thirsty |

### Menu — Cakes & Pastries
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Sachertorte Slice | 18 Sovs | About 6 Sovs of ingredients and 183 years of reputation | +60 HP, Removes Thirsty |
| Apfelstrudel | 14 Sovs | Honest | +40 HP, Removes Hungry |
| Opera Cake | 22 Sovs | The most expensive slice in the case, and the one Gustav takes on the way out | +80 HP, +2 Charm (30 min) |
| Gugelhupf | 12 Sovs | The best value in the building and he knows it | +30 HP, restores small SP |
| **"The Gustav"** (post-quest only) | **8 Sovs** | A chocolate horse-shaped cookie. Forty a day. | +20 HP; +2 Bravado; unlocks achievement "The Gustav" |

### Hidden Charges
| Charge | Amount | Applied When |
|--------|--------|--------------|
| "Historic Table Supplement" | 3 Sovs | Window seating — the good tables, and the charge is printed on the menu in calligraphy the size of a fly |
| "Service Surcharge" | 15% | Every bill, added without explanation, and he will explain it in full detail if asked, at length, until the guest regrets asking |
| "American Tourist Adjustment" | 10% | Accent detection. It is not on the menu. It is on the till, under a different name, and has been since 1974. |

### Service Mechanics
- **Order in German correctly** (pronunciation minigame): small discount, and applies "Cultured Palate" — **+1 Charm for 1 hour**.
- **Fail the order** (or order "a coffee," or ask for iced coffee): applies "Humiliated by Waiter" — **-1 Charm for 30 minutes**. Stacks with nothing. Wears off. He does not remember it; the player does.
- **Café selfie** (+2 Bravado) requires an order first. He will not permit the photograph otherwise and will step into frame to prevent it, which is a better photograph.
- **The 340 Sovs debt gate**: no normal service of any kind until cleared. Installments accepted, **50 Sovs minimum**. Full payment unlocks **"Valued Patron" — +10% discount permanently**.

### Hidden Details / Easter Eggs
- **Examine his pocket watch**: *"Correct to the second. He winds it at 07:40, before the doors. It is the only object on his person that is his."*
- **Examine the monogram on his shirt**: *"The café's initials. Not his. There are no initials of his anywhere in this building."*
- **Examine the staff break room window during 14:00–14:04**: *"Schnapps bottles. Four of them. One is open. The room is empty in three minutes and forty seconds and the glass is washed."*
- **Examine the trophy case**: *"'Best Sachertorte 1952–1999.' The 1999 plaque is the last one. He arrived in 1996."*
- **Examine the framed Emperor Franz Josef letter**: *"Probably fake. He has never said so and never will. It was here before him."*
- **Ask him his name.** He answers, every time, identically: *"Herr Ober."* Ask a fourth time in one conversation and the option greys out permanently for the rest of the game.
- **Post-quest, examine the Wall of Shame**: *"A framed photograph of a horse eating an 85 Sovs cake. The framing is expensive. Someone chose that frame."*

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Gustav (`sinfonia_npc_gustav_horse_01`) | The single defining event of his professional life. Herr Ober will not use the word "horse" casually again for the rest of the game — he says "the animal," and when he must say "horse" he pauses first. |
| Hans-Jürgen Pferdmann (`sinfonia_npc_hans_jurgen_01`) | Knows him by name, bills him by name, and has never once served him. Pferdmann has been refused a table at this café for eleven years and neither man has ever mentioned why. "Fiakermeister" is Pferdmann's TITLE and Herr Ober uses it with full correctness, which from him is a form of contempt and also a form of respect. |
| Chess Master Greta (`sinfonia_npc_cafe_chess_player_01`) | Table fourteen, nineteen years, one Melange. He brings the second cup without being asked. He has never played her. She has never asked him to. |
| The Intellectual (`sinfonia_npc_cafe_intellectual_01`) | Forty years of a single espresso. Herr Ober defends this table against the owner annually and has never told the man he does so. |
| Chef Konrad (`sinfonia_npc_kitchen_staff_01`) | Thirty years side by side; the only person alive who knows his name and the only person who has ever needed it. Uses it exactly once, in the chaos, in German. The box shows a blank. |
| Sous Chef Anna (`sinfonia_npc_kitchen_staff_02`) | Finds him funny. He is aware. He has decided to permit it. She is the only member of staff who gets a real answer out of him and she gets one about twice a year. |
| Regisseur Heinrich Hoffmann (`sinfonia_npc_regisseur_hoffmann_01`) | Two professionals whose institutions were destroyed by the same horse on the same afternoon. They have not met. If the player has both debts active, each mentions "the other one" with total, wordless solidarity. |
| The Poseur (`sinfonia_npc_cafe_poseur_01`) | Herr Ober knows he is a real estate agent. Herr Ober has known for two years. Herr Ober seats him near the window because the philosophy book photographs well from the street. |

### Territory / Social Dynamics
- The floor is his and the owner does not come in before four. The seating order is his invention and predates the current management.
- The kitchen is Konrad's and he does not cross the line, in either direction, ever — the two of them have worked thirty years through a service hatch.
- Kaffeehaus Row's waiters run an informal ledger of bad guests across establishments. He telephones. This is how the debt follows the party to Café Existenz and every other café on the Row.
- He protects his staff from guests and does not protect them from the owner, because he cannot, and this is the quiet failure he carries.

---

## 🔄 Recurring Appearances

### Within Sinfonia
- Café Sachertorte, 08:00–22:00, every day, for the entire game. He is never absent from a shift in any state.
- Opera Backstage, once, mid-chase — he may arrive in pursuit of payment and encounter the Magic Flute disaster in progress, at which point he stops talking entirely and simply looks at it.
- The café doorway, during the 24-hour "TEMPORARILY CLOSED" window, drinking openly.
- Kaffeehaus Row, ambient, delivering the 340 Sovs figure to neighbouring establishments — visible from the street, not interactable, and the gossip system updates immediately afterwards.

### In Other Cities (If Applicable)
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| N/A | — | He does not leave Kaffeehaus Row. He has not taken a full week off since 2011 and the café would not survive it. | — |

### Evolution Through Game

Debt unpaid: hostility, refused service, BANNED board with the party's photographs on it, and the figure known at every café on the Row. Debt in installments: he softens by exactly one degree per payment and states the running balance every time, to the Sov, from memory. Debt cleared: "Valued Patron," the window table, and a man who has decided the matter is closed and genuinely means it.

Across all states, the permanent change is the same: the "NO HORSES PERMITTED" sign, the "SECURED" label on the case, the Wall of Shame photograph, "The Gustav" on the menu at 8 Sovs selling forty a day, and a head waiter who touches the corner of the display case every time he walks past it.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_stillness | Perfect stillness, slight breathing, tray balanced one-handed; 2 frames | 40% |
| floor_scan | Slow sweep of the room, counting tables, doing arithmetic | 25% |
| watch_check | Pocket watch out, glanced at, returned — he already knew | 20% |
| case_touch | Two fingers to the corner of the cake display (post-quest only; replaces watch_check) | 15% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| service | Order placed — precise movements, silver tray, 6 frames, never a wobble |
| judgment | The Order Judgment — raised eyebrow, slight head shake, 3 frames; the location's signature frame |
| horror | Gustav reaches the display — hands to face, step backward, 4 frames |
| fury | The damage tally — pointing, red-faced, gesturing at each itemised line, 6 frames, loops |
| defeat | Post-rampage — slumped, seated, staring at the emptied case, 2 frames, loops |
| ledger_write | Dialogue Option 1 — writes the names down without raising his voice, which lands harder than the shouting |

### Sprite States
| State | When Used |
|-------|-----------|
| floor_default | All service, all judgment, all pre-quest and post-quest floor work — `herr_ober_waiter.png` |
| chaos_apron_ruined | Phase 2 from the cake heist onward, and the 24-hour closure — same sheet, apron-destroyed variant rows |
| doorway_drinking | The 24-hour closure only — same sheet, vest unbuttoned, glass in hand, standing in daylight |

**Sprite sheet:** `herr_ober_waiter.png` (384x288) — six state rows at **48x96** per cell: idle, service, judgment, horror, fury, defeat. (Cell size per `PNG_Assets/cafe_sachertorte_png_assets.md`, which is authoritative and is corroborated by `sprite_mapping/cafe_sachertorte_sprite_mapping.json`.)

---

## 🎯 Quest Integration

### Primary Quest
- **Quest**: The Fiaker Fiasco (`sinfonia_sidequest_fiaker_fiasco_01`) — Phase 2, `fiaker_fiasco_cafe_phase`
- **Role**: Victim, witness, damage assessor, and the quest's economic engine. He converts a horse chase into a number the player has to carry for the rest of Sinfonia.
- **Trigger**: The party follows Gustav from Opera House Plaza; the phase auto-triggers on entry
- **Outcome**: 340 Sovs assessed and itemised; one of three dialogue resolutions; the debt persists across all Sinfonia vendors until cleared

### Quest Gate Function

He gates **all normal café service** behind the 340 Sovs. Not partially — the display case, the menu, the selfie spot, the chess minigame, the rest point, and the status recovery are all closed to the party until the balance is zero. He accepts installments at a **50 Sovs minimum** and will state the exact remaining balance every single time. He gates the "Valued Patron" +10% discount behind payment in full, and the achievement **"Patron of the Arts"** with it.

He gates nothing in the main chase. He never blocks the exit. He follows instead, which is worse.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Itemised Damage Receipt (340 Sovs) | Phase 2 resolution, Options 1 and 3 | Yes | Keepable, examinable; six line items, correct arithmetic, and "Emotional damages — 53 Sovs" |
| "Valued Patron" status | Debt cleared in full | Yes | Permanent +10% discount at Café Sachertorte |
| "The Gustav" cookie | Post-quest, 8 Sovs | No | +20 HP, +2 Bravado; unlocks achievement "The Gustav" |
| "Cultured Palate" | Order in German correctly | No | +1 Charm, 1 hour |
| "Humiliated by Waiter" | Failed order | No | -1 Charm, 30 minutes |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. **The judgment frame.** One raised eyebrow, a 5 Sovs coffee, and three men in cargo shorts.
2. **The horror frame**, timed to Gustav's first bite of the 85 Sovs whole Sachertorte.
3. **The defeat frame** — a seated head waiter, an emptied display case, a chandelier that survived by forty centimetres.
4. **The doorway.** Business hours, sunlight, unbuttoned vest, glass in hand, thirty years of composure gone in one afternoon.
5. **The Wall of Shame**, professionally framed, permanently hung, selling forty cookies a day.

### Meme Potential
- **"MEIN GOTT! DAS PFERD FRISST DIE TORTE!"** — the game's most exportable scream.
- **"Insurance covers 'acts of God.' This is an 'act of HORSE.'"** — an infinitely reusable format.
- **"Ah. You would like... 'a coffee.' How... specific."** — the pause is the meme.
- **"The Sachertorte recipe is unchanged since 1832. Unlike the clientele."**
- **"340 Sovs. You will pay this. Now. Or I call the Polizei."** — universal split-the-bill caption.

---

## 🗣️ Voice Direction

### Accent

Formal German-accented English, Austrian rather than German-German, precise and unhurried. The register is hotel-school, not comedy-Bavarian — this man was trained. The English is better than he lets it be; the slight formality is a choice, not a limitation. Under stress the English does not degrade, it *stops*, and German arrives at full volume with no transition.

### Tone
- **Service**: pleasant, level, and entirely unhurried. Never sneering. The condescension lives in the pauses, not the delivery.
- **The Order Judgment**: the pause does all the work. No emphasis, no smirk, no rise at the end. The guest fills the silence and the guest always makes it worse.
- **The rampage**: full-throat, uncontrolled, genuinely frightened. He is not being funny. It is funny because he is not being funny.
- **The bill**: flat. Utterly flat. He has spent his shouting.
- **The breakdown**: quiet, seated, disbelieving, and played completely straight with no comedy scoring over it.
- **Post-quest**: one degree less composed than before, permanently, and he never gets that degree back.

### Key Delivery Notes
- **Every canon line ships verbatim** and must match `cafe_sachertorte.md` and `cafe_sachertorte_npcs.json` byte-for-byte. The connective staging around them has craft latitude; the quoted lines do not.
- The ellipses are real held beats — a full second, not a breath. "You would like... 'a coffee.'" dies completely if it is rushed.
- **"In thirty years of service, I have never... a HORSE. A HORSE ate the Sachertorte."** is the character's whole arc. Delivered seated, quietly, to nobody, with the second "HORSE" louder than the first and the sentence never actually completing. Silence on both sides.
- He never sounds cruel and never sounds like he is enjoying himself. Everything he says to the bros is true, and the truth is what stings.
- **He never says his own name and there is no line in which he could.** Do not record one. Do not write one.

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

- **CANON — no first name, ever.** "Herr Ober" is a form of address meaning *Mr. Waiter*. No file, line, subtitle, asset filename, or JSON field may assign him a personal name. The one in-fiction utterance of it (Chef Konrad, chaos phase, German) renders as a blank the width of a word and is never explained.
- **CANON — NPC ID**: `sinfonia_npc_herr_ober_01`, matching the existing entry in `cafe_sachertorte_npcs.json`.
- **CANON — the debt is 340 Sovs**, itemised as: patio table 85 Sovs, umbrella stand 15 Sovs, full Sachertorte 85 Sovs, two marble tables 80 Sovs, Opera Cake slice 22 Sovs, "emotional damages" 53 Sovs. Any other total is stale.
- **RESOLVED — author ruling: the whole cake stands.** Gustav eats one whole 85 Sovs Sachertorte, and the 340 Sovs tally depends on it. The old `cafe_sachertorte.md` TikTok line *"THAT HORSE JUST ATE THREE SACHERTORTES! THAT IS 54 Sovs!"* is retired; the quotable is now Chadwick's *"EIGHTY-FIVE SOVS! FOR A CAKE! HE ATE EIGHTY-FIVE SOVS!"*, filmed over Herr Ober's meltdown. 18 Sovs remains the **slice** menu price and nothing else. Do not reintroduce a three-slice reading.
- **RESOLVED — author ruling: one 170 Sovs relief, claimed once.** The 170 Sovs Fiaker insurance payout against the café bill and the dialogue-option-3 halving of the 340 Sovs are **the same relief and are mutually exclusive**. Whichever fires first sets `debt_relief_claimed` and consumes it; the other is then disabled and must not apply. Hans-Jürgen's **500 Sovs Path A contribution is a separate pot and does stack**. Full arithmetic: `Design/Quests/Location Specific/Sinfonia/fiaker_fiasco.md` → "Damage Debt Resolution — Authoritative".
- He must never read as a villain and never as a snob for the audience to look down on. He is the only person in Phase 2 who did nothing wrong, and the satire is aimed at the tourist-extraction *system* he was trained into, never at Austrian café culture, which the file treats as a real trade with real workers.
- His drinking is never played as a punchline and never impairs him on the floor. The break-room window is the only pre-quest evidence; the doorway scene is the only time it is visible, and it is played straight.
- The Gugelhupf being the best cake in the case is a real mechanical fact (12 Sovs, +30 HP, small SP) that he mentions exactly once, on Option 2, and never again. Most players will never see it.
- Do not let him explain the "American Tourist Adjustment" to the bros. They never learn it exists. If the player reads the menu, the player learns it exists, and that is the entire gag.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — none present; the café is Sov-denominated, cash-and-card, and the debt system is a plain ledger
- [x] **NO automatic crypto assumptions** — most NPCs have none, and he is one of them; he would consider it a species of rudeness
- [x] **Coins, kiosks, and certificates come from the master pool** (`design/economy/shitcoin_master_pool.md`) — N/A, no coins invented here
- [x] **The bros are never scam-aware** — they read the 340 Sovs as a negotiating position and the surcharges as a personal attack, and they never once read the menu
- [x] **Nothing winks** — no line of his, and no line about him, signals that any of this is satire
- [x] **Focus on city-specific cultural exploitation instead** — Sinfonia's Kaffeehaus-heritage tourist economy: the 18 Sovs slice, the printed-but-illegible surcharges, and a room trading on 1843

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is three Americans mistaking an honest itemised bill for an ambush; Viennese café service is portrayed as a skilled, underpaid trade
- [x] NPC is savvy entrepreneur, not villain or stereotype — a trained professional applying house policy, who protects his staff, defends a forty-year regular's table, and is the only blameless party in the disaster
- [x] Humor is affectionate mockery, not mean-spirited — his composure is the joke's engine and his collapse is played with real weight; the file mocks the pricing structure, never the man operating it

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Sinfonia/npcs/Cafe_Sachertorte/npc_herr_ober.md`
- **Registered In**: `cafe_sachertorte_npcs.json` — Yes (existing entry `sinfonia_npc_herr_ober_01`; `full_profile` path added this pass)
- **Sprite Sheet**: `herr_ober_waiter.png` (384x288)

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile | Claude (NPC authoring pass, Sinfonia Wave 1) |

---

*Template Version 1.1 — Based on Shady Wristband Guy profile structure. This is the canonical NPC template; the legacy `Character Profiles/Templates/npc_template.md` is retired.*
