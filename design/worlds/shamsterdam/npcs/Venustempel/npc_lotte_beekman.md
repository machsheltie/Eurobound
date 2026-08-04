# NPC Profile: Lotte

*"Looking for something specific? We have... everything, really."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_lotte_01`
- **Display Name**: Lotte
- **Internal Name**: Lotte Beekman — gift shop attendant, Venustempel (Museum Mile). Six years on the counter, four of them in the old Roodelicht Row corridor, two in the new shop.
- **Role**: Vendor / Service Provider — museum gift shop attendant. Also the game's primary **Handreiniger** cure vendor.
- **Associated Quest**: None
- **Primary Location**: Venustempel gift shop, Museum Mile, Shamsterdam (`shamsterdam_museumrow_venustempel_01`)
- **Secondary Appearances**: None. Lotte is in the shop. The shop is the exit, so everyone meets her anyway.

---

## 🎭 Core Concept

### What She's Actually Doing

Running the retail end of a museum that is now two museums. Venustempel moved off Roodelicht Row and onto Museum Mile, absorbed a second collection, and reopened as **De Cacaogalerij** (a museum of chocolate phalluses, curated seriously, with placards, artisan makers credited) plus **De Mechanische Vleugel** (the original 1985 material — the Giggling Figure, the mutoscopes, the Marilyn statue, the genuinely real John Lennon erotic sketches, the chastity belts, the 1800s medical diagrams). Entry went from 5 Sovs to 9 Sovs when the chocolate wing opened. Hours are 10:00–23:00. The subtitle on the awning reads *"Giggling Since 1985. Dipping Since 2011."*

Lotte sells the merchandise for both wings out of one shop. Postcards, T-shirts, a licensed and framed John Lennon print, keyrings, fridge magnets, solid chocolate pieces in three cocoa grades, hollow pieces for the budget-conscious, and a boxed set of six graduated sizes called **De Collectie** which is the best-margin item on the floor. She gift-wraps for free, does discreet plain packaging for free, mails internationally for 6 Sovs, and lets anybody at all use the shop toilet whether they bought a ticket or not.

She also stocks **Handreiniger** — a 4 Sovs hand sanitiser in a small bottle moulded in the shape of De Grote Fontein, the four-metre working chocolate fountain outside on the plaza. She recommends it to every customer on the way out. Cheerfully. Sincerely. Every time.

### What Bros Believe

That the gift shop is the punchline and that they are delivering it. Bradley buys the boxed **De Collectie** "as a gag," pays 45 Sovs for the gag, and then will not let Chadwick or Pilsner carry the box, at any point, for any reason, all the way back to the hostel. Chadwick films the shelving and narrates it as a curatorial statement. Lord Pilsner asks whether the chocolate is "real chocolate," in the tone of a man springing a trap. It is real chocolate. Lotte tells him the cocoa percentage — 34% for the milk, 70% for the dark, and she knows both because a customer asked once and she went and found out. He is not listening. He has already turned to Chadwick to say "it's real chocolate."

All three of them decline the Handreiniger. All three of them have been at the fountain.

### The Comedy Gap

**Lotte is not in on the joke.** No knowing looks, no arch delivery, no winks, no pause before a product name. She is a good retail professional having a nice day in a shop she is genuinely proud of. The gift shop is funny *because* she is not being funny — the till rings, the ribbon comes off the spool, the best-seller is a best-seller, the postcards go in the post, and every single item is described with the flat warmth of somebody who has faced it forward on a shelf that morning. The bros arrive braced for a transgressive experience and are instead sold a product, at a price, by a woman asking whether they want it wrapped.

### The Thing She Will Absolutely Tell You About

The move **doubled her floor space**. This is the single best thing that has happened in her working life and she will tell you the square metreage without being asked. The old Roodelicht shop was a corridor — one and a half metres wide, stock on both walls, nowhere to stand, and you wrapped a parcel on your knees behind a till the size of a shoebox. The new shop has an island display in the middle, which she can walk all the way around, and a **wrapping station with a proper counter**. She talks about the shelving with real warmth. It is the only subject on which her professional register slips into pure enthusiasm, and she will circle back to it twice in a long conversation.

### The Bottle Nobody Buys

The Handreiniger sells poorly. Lotte has never connected the product to the fountain, never connected the fountain to anybody's symptoms, and does not know that the museum has a hygiene mechanic wrapped around it. She recommends it because it is a nice product and the bottle is cute. She keeps facing it forward on the counter. It keeps not selling. She is not making a point.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 20s |
| Build | Compact, quick on her feet. Shop-floor movement — she is always two steps into a task before she finishes the sentence about it. |
| Height | Short |
| Energy | Bright, brisk, entirely sincere |

### Clothing
- **Pink apron (uniform)**: Museum-issue, hot pink (#FF69B4) over plain clothes, two front pockets, one holding a pen and one holding scissors. It is the uniform. She wears it correctly and without irony because it is the uniform.
- **Plain shirt and jeans underneath**: Whatever she came to work in. The apron does all the identifying.
- **Accessories**: A length of **gift-wrapping ribbon tied in her hair** — curling ribbon off the spool, changed most days, colour varies. It started as a slow-afternoon habit in the old shop and became a thing people compliment, so it stayed.
- **Footwear**: Flat, worn, comfortable. Thirteen-hour shoes for a thirteen-hour opening.

### Distinguishing Features
- **Faces stock forward constantly.** Mid-conversation, without looking, she will square a row of boxes on the counter. This is the most-used idle in her set.
- **The Handreiniger gesture** — a small two-finger tap on the little fountain-shaped bottle beside the till, executed on every single sale, always accompanied by the same sentence.
- Never breaks from complete normality in any frame. **No knowing looks. No winks. No arch eyebrow.** She is not suppressing anything; there is nothing to suppress.
- Talks about square metreage with visible pleasure. The Floor Space frames are the only place her posture opens up.
- Ribbon-hands — the wrapping animation is fast, practised, and slightly showy in the way of somebody who is good at one specific thing and enjoys it.

### Sprite Notes
Sheet `npc_venustempel_staff.png`. Lotte's existing allocations carry forward from the asset doc: **Portrait (Dialogue) at (256,192), 128×128** — cheerful, pink apron, wrapping ribbon in her hair; **Gift Shop Idle at (384,192), 64×96** — aggressively helpful; **Gift Wrapping at (448,192), 64×96**; **Best Seller Pitch at (0,320)**; **Discreet Packaging at (64,320)** — plain paper, no branding, entirely routine; **Postcard Recommendation at (128,320)**; **"We'll be here when you're ready." at (192,320)**; **High-Contrast Silhouette at (128,416)**.

**New frames required for the Museum Mile relocation.** Note that `npc_venustempel_staff.png` is 512×512 and already densely packed to y=416; the five new frames will need either the Accessibility Reserve Block at (256,416) reclaimed, or the sheet expanded to 512×640 with a new Lotte row at y=512. The frames: *Handreiniger Recommendation* (the two-finger tap on the bottle, the shop's most-repeated animation); *Floor Space Enthusiasm* (both hands out, indicating the room — the single most open pose in her set); *Chocolate Case Presentation* (island display, glass, "solid or hollow?"); *Lennon Print Handling* (she carries the framed print with two hands and turns it to the light); *Mailing Desk* (stamps, customs label, the small stack of pre-printed forms).

**Critical constraint, carried forward from the asset doc and strengthened here: Lotte treats every transaction as completely normal in every frame. No knowing looks, no winks. Her cheerfulness is sincere and that is what makes the gift shop land.** If a single frame implies she finds any of this funny, the shop stops being funny.

---

## 🧠 Personality

### Archetype

**The Sincerely Delighted Retail Professional** — Lotte works in a museum of historical erotica and artisan chocolate genitalia, and to her it is a shop with a stockroom, a rota, a best-seller, and a margin. She is not performing normality; the normality is real. She likes her products, she likes her customers in a general uncomplicated way, she is proud of the new premises, and she wants everybody to leave with something nice and clean hands. She has no second layer. The absence of the second layer is the character.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Aggressively helpful | She will find it. If it is not on the floor she will check the back. If it is not in the back she will tell you when it is in. This is offered at a pace nobody asked for and it is entirely genuine. |
| Not in on the joke | The purchases are purchases, the prices are prices, the products are products. She has never once implied otherwise and structurally cannot. |
| Openly delighted about the floor space | Doubled. She knows the number and she will say the number. The only subject that breaks her retail register. |
| Product-fluent without being a curator | She knows cocoa percentages, shelf life in warm weather, which postcard sells, which keyring breaks. She does not know art history and does not pretend to; for that she points upstairs. |
| Unbothered | Not immune the way Anke is immune — Anke has burned it out over fifteen years. Lotte simply never had the reflex. Nothing has happened at this counter that she considers worth a reaction. |

### Internal Monologue

> "The tall one is going to ask if it is real chocolate, they always do, and it is, thirty-four percent for the milk, and I will tell him and he will not hear it, which is fine. The quiet one has the Collectie under his arm and he has been holding it like a passport since he picked it up, so that is forty-five, and he will want the plain paper. The one with the phone will film the shelves and then ask me where the toilet is. And I will say the toilet is through there, and it is fine, everyone uses it, you do not need a ticket. And then I will show them the Handreiniger because it is four Sovs and the bottle is lovely and nobody ever takes one. Nine metres by six. Fifty-four. The old shop was eleven."

### Motivation

Doing the job well in a shop she is proud of. Lotte is not building toward anything — no secret ambition, no resentment, no art degree she is quietly wasting. She likes retail, she is good at it, and after four years working out of a corridor she has been given an island display, a wrapping station with a proper counter, and twice the square metreage. She wants the shelves faced, the wrapping neat, the mailing to actually arrive, and the customer to have been looked after. That is the whole of it and it is enough.

---

## 💬 Dialogue

### Approach/Greeting

**First entry (the shop is the museum's only exit; entry is unavoidable)**:
> "Hello! Come in, there's room." *(There is. That is a real thing she says, in a real shop that is now large enough for the sentence to be true.)* "Looking for something specific? We have... everything, really."

**Player browses without engaging**:
> "Take your time. Chocolate's on the island in the middle, the old museum things are along the back wall." *(She goes back to facing a shelf. No hovering.)*

**Player enters with 3+ party members**:
> "Oh, a group — go around the island, it's easier than squeezing past. You can go all the way round it." *(Small pleasure, entirely sincere. The island is new.)*

**Late in the evening, 22:00–23:00**:
> "We're open till eleven. You've got time. Nobody's rushing." *(Beat.)* "I'm here anyway, so."

### Key Interaction Dialogue — The Floor Space

**Player asks about the museum moving / asks anything at all about the new location**:

*Floor Space Enthusiasm animation. Both hands out. The only fully open pose she has.*

> "We moved! In the spring. We're on Museum Mile now, with the proper museums." *(Beat.)* "Do you want to know the best part?"

**Player**: "Sure."

**Lotte**:
> "Fifty-four square metres. The old shop was eleven." *(She lets that sit for exactly as long as it deserves, which is not long, and then continues at the same brightness.)* "Eleven. It was a corridor. Stock on both walls, and if two people came in at once one of them had to stand outside. I wrapped everything on my knees behind the till because there was no counter. There was a till and there was a wall."

> "Now there's the island — that one, in the middle, with the glass — and you can walk all the way around it. Customers walk around it. That's the whole thing. They walk around it and they see the other side."

> "And a wrapping station. A proper one, with a counter, and the ribbon is on a rail." *(She indicates the rail. She is not showing off. She simply thinks it is good.)* "Two spools at once. You would not believe the difference."

**If the player asks whether she misses the old district**:
> "No." *(No edge on it at all. It is just the answer.)* "It was a good corridor. This is a shop."

### Key Interaction Dialogue — The Chocolate Line

*Chocolate Case Presentation animation. Island display, glass, the pieces on graduated shelves with the same small printed cards the museum uses upstairs.*

**Player examines the chocolate case**:
> "That's the Cacaogalerij line. Solid or hollow — solid is twelve, hollow is eight. Hollow's lighter, obviously, so it's easier to pack." *(Beat, completely level.)* "I'd say solid if it's warm out. The hollow ones don't love the heat."

**Player asks what happens to the hollow ones in the heat**:
> "They go soft and then they go... structural." *(She does not smile. This is a shipping consideration and she is giving you shipping advice.)* "It's fine in the bag for an hour. It's not fine in a bag for a day."

**Lord Pilsner: "Is this REAL chocolate?"**
> "Yes! It's from the makers upstairs, the ones on the placards." *(Genuinely pleased to be asked; this is her favourite kind of product question.)* "Thirty-four percent for the milk, seventy for the dark, the white's white so it's a different conversation. They temper it properly, that's why the finish is like that." *(She turns a piece so the light catches it.)* "See?"

*Pilsner is not listening. He has already turned around to say "it's real chocolate" to Chadwick.*

**Player asks about De Collectie (the boxed set of six)**:
> "That's our Collectie. Six pieces, graduated sizes, in the box with the ribbon — forty-five." *(Best Seller Pitch animation.)* "This one is our best seller. Good for gifts. People say 'ironic gifts' but they buy two so..." *(She trails off. There is no second half of the sentence. She has moved on to getting one down off the shelf.)*

**Bradley buys the Collectie "as a gag"**:
> "Of course. Wrapped, or as it is?" *(Identical speed, identical warmth, identical to every other sale in the shop.)* "The box is quite nice on its own, if it's a gift."

*He takes it as it is. He carries it himself. He will carry it himself all the way back to the hostel and he will not put it down.*

### Key Interaction Dialogue — The John Lennon Print

*Lennon Print Handling animation. She carries it with two hands and turns it to the light.*

**Player examines the framed print**:
> "Oh — that's my favourite thing in the shop." *(No performance in it whatsoever. She is answering the question honestly.)* "It's the Lennon. Licensed, and framed, thirty-five. The originals are upstairs in the old wing, off to the left, under the small lamp — you can miss them, most people do."

> "People come in and they don't believe it's really him. And then they go up and look, and they come back down, and they buy the print." *(Beat.)* "It's a lovely line. Look at the hand. He was good."

**Player asks if it's really John Lennon**:
> "Really him. There's a whole card about it upstairs." *(Beat.)* "I know it sounds like something a gift shop would say. But it's on the card and the card's the museum's, not mine."

**Player buys the print**:
> "Good." *(She means it. She wraps it in the tissue first, then the paper, and takes longer over it than the price warrants.)* "Corner protectors are in there. Don't let it lean on the glass in your bag."

### Key Interaction Dialogue — Gift Wrapping & Discreet Packaging

**Player selects any item for purchase**:
> "Would you like it wrapped? It's free. We do gift wrapping. No judgment. Very discreet packaging available."

**Player asks what "discreet" means**:
> "Plain brown paper, no branding, nothing printed on it. It just looks like a parcel." *(Discreet Packaging animation. Entirely routine, no lowered voice, no second meaning in any syllable.)* "Most people take the discreet if they're posting it. The festive paper is quite loud."

**Player asks for the loud paper**:
> "Pink, with the Venus on it." *(She is already reaching for it.)* "Some people want everybody to know. That's fine, it's a nice paper."

**Player asks whether she wraps a lot of these**:
> "All day." *(Ribbon, one loop, scissors, curl. Six seconds.)* "It's the best part of the job, honestly. The station's new."

**Player asks about mailing**:
> "We post internationally, that's six Sovs, and I do the customs form for you." *(Postcard Recommendation animation.)* "The postcards are popular. Yes, you can mail them. Yes, people do mail them." *(Beat.)* "The Giggling Figure set is four Sovs for six. That's the one people send to their mothers, for some reason. I don't know."

### Sales Close

*Ringing Up. Then, without fail, the Handreiniger gesture — two fingers, tap, tap, on the little fountain-shaped bottle beside the till.*

> "That's forty-five. Card's fine." *(Tap, tap.)* "And would you like a Handreiniger? It's four Sovs. It's hand gel — look, the bottle's the fountain." *(She turns it so you can see. She is quietly pleased by the bottle. She thinks it is a good little product.)* "People don't take them, but it's lovely, and the bottle's very good."

**If the player buys one**:
> "Oh, good!" *(Genuine, slightly surprised pleasure. It is the only time all day this happens.)* "It's a nice one. Not the sticky kind."

**If the player declines** (this is the overwhelming default):
> "No problem at all." *(She faces the bottle forward again. Same position. Same angle. She does this perhaps forty times a day.)* "Bag or in your pocket?"

**If the player declines a second, third, fourth time on later visits**:
> *(Identical delivery, every time, indefinitely. She never adjusts, never gives up, never comments on the pattern, and has not noticed there is one.)*

### Post-Interaction

> "There you go. Enjoy Shamsterdam." *(Beat.)* "The fountain's just outside if you haven't been — it's free, you don't have to buy anything, everyone has a go."

> "Toilet's through there on the left, if you need it. You don't need a ticket. Everyone uses it." *(She says this to roughly one visitor in three and has never wondered why the number is that high.)*

### If Player Declines / Alternative Path

**Player browses and buys nothing**:
> "That's absolutely fine. Come back if you change your mind — we're here till eleven." *(She returns to the shelf. No follow-up, no disappointment, no second attempt.)*

**Player only uses the toilet and leaves**:
> "You're very welcome. Have a nice evening!" *(Entirely sincere. The toilet is a service she provides and she is glad it was useful.)*

**Player asks whether they can just look**:
> "Please do. There's more room now." *(Beat.)* "You can go round the island."

**Player tries to be shocking about a product**:
> *(She answers the question that was actually asked. Accurately. With the price. And then asks if they would like it wrapped.)*

**Player asks her what she thinks of what the museum sells**:
> "It sells well." *(No irony, no evasion. It is a complete and honest answer and she has no other one.)* "The Collectie is the best of it, margin-wise. And the postcards, because they're four Sovs and people buy four."

### Callback Dialogue (Return Visits)

**Second visit**:
> "You're back! Did the chocolate survive?" *(A real question. She wants the actual answer, for stock-planning reasons.)*

**Third visit onward**:
> "Hello again." *(A small wave with the scissors still in her hand.)* "Anything today, or are you just in for the toilet? Either's fine."

**Return visit after buying the Lennon print**:
> "Did you hang it?" *(Beat, and then, unable to help herself:)* "The hand. Did you see the hand?"

**Return visit while the player has 3+ stacks of Sharing the Love**:
> "You've been at the fountain!" *(Delighted. Not a diagnosis. She has seen the chocolate on his sleeve, that is all.)* "It's good, isn't it. Handreiniger's four Sovs if you want one."

**Return visit after Shamsterdam Stomach has triggered**:
> "You look tired." *(Kind, brief, and completely disconnected from any cause.)* "There's a bench in the old wing, by the diagrams. People sit there."

**Late game**:
> "You've been in more times than the school groups." *(Beat.)* "Come back anytime. We're here since 1985. We'll be here when you're ready."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 09:30–09:59 | Shop floor (pre-open) | Facing stock, restocking the chocolate case from the cold room, tying the day's ribbon in her hair. Not player-accessible; visible through the window. |
| 10:00–13:59 | Counter / island display | Opening trade. School groups, the serious couples, the Cacaogalerij placard-readers. Low volume, long conversations. Her preferred hours. |
| 14:00–17:59 | Counter | Museum Mile peak. Cultural Alibi District foot traffic — people who came for a museum and left through a chocolate shop. Constant wrapping. |
| 18:00–21:59 | Counter / wrapping station | Evening peak. Fountain plaza is busiest, so the shop is busiest. Maximum toilet usage. Maximum Handreiniger recommendations, minimum Handreiniger sales. |
| 22:00–23:00 | Counter | Last hour. Quiet. This is where the floor space conversation and the Lennon conversation are both available at full length. |
| 23:00–10:00 | Closed | The fountain runs anyway. It runs all night. Nobody has ever raised this. |

### Positioning Notes
- Default station is the counter, which is the **wrapping station** — the two are the same object now, and that is the point of the new shop.
- She moves out to the **island display** for any chocolate question, walking round it rather than leaning across it, because walking round it is possible now.
- The shop is the museum's **only exit**. Ground floor → Mechanische Vleugel → Cacaogalerij → gift shop → street. Every visit ends at Lotte's counter. There is no alternate route and there never was, in either building.
- The Handreiniger sits beside the till, faced forward, at the exact spot where a customer's hand goes when they take their card back.
- The toilet door is behind her and to the left, visible from the counter, and she waves people toward it without breaking off a sentence.
- Through the shop window: **De Grote Fontein** on the plaza, four metres of flowing food-grade chocolate, and **Gunter**'s cart *Gunter's Deep Dips* beside it. Both are in frame behind Lotte for the entire location. She has her back to them all day.

---

## 🎒 Inventory / Services

### Items Sold — Legacy Venustempel (De Mechanische Vleugel)
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Giggling Figure postcard set (6) | 4 Sovs | 4 Sovs — fairly priced, well printed | Mailable. Adds "Sent Postcard" flag; recipient NPC reacts in the epilogue. Four Sovs is the price four Sovs should be. |
| "I JUMPED" T-shirt | 22 Sovs | 18 Sovs — standard tourist-tee markup, honest cotton | Wearable cosmetic. Other NPCs read it. Nobody who buys it did not jump. |
| John Lennon sketch print (licensed, framed) | 35 Sovs | 35 Sovs — genuinely licensed, genuinely framed, genuinely good | Collectible / room decor item. **Lotte's personal favourite item in the shop.** She thinks it is beautiful and she is right. Grants +Trivial Knowledge and unlocks the "Did you know John Lennon drew—" dialogue branch permanently. |
| Mutoscope-reel keyring | 6 Sovs | 3 Sovs — it is a keyring | Cosmetic. Small flip animation on examine. Breaks eventually; this is not modelled and does not need to be. |

### Items Sold — De Cacaogalerij (most of her revenue)
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Solid chocolate piece — white / milk / dark | 12 Sovs | 12 Sovs — real artisan chocolate, tempered properly, 34% milk / 70% dark | Consumable. Restores a moderate amount of HP. Survives a warm day in a bag. |
| Hollow chocolate piece | 8 Sovs | 7 Sovs — same chocolate, less of it | Consumable, cheaper, lighter. **Structurally regrettable in heat**: if carried past 22°C in-game for more than two hours it degrades to "Formerly A Hollow Piece," which still restores HP and is no longer presentable as a gift. |
| **De Collectie** — boxed set of six graduated sizes | 45 Sovs | 38 Sovs — a real boxed set, ribbon included | **Best margin in the shop.** Gift item. Bradley buys this "as a gag" and refuses to let anyone else carry it. Occupies two inventory slots and is visible to other NPCs. |
| Fountain-shaped keyring | 5 Sovs | 2.50 Sovs | Cosmetic. Sells constantly. Lotte reorders it more often than anything else on the floor. |
| Fountain fridge magnet | 3.50 Sovs | 1.50 Sovs | Cosmetic. The cheapest thing in the shop and the second-fastest mover. |

### The Hygiene Line
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| **"Handreiniger"** hand sanitiser, in a small bottle moulded as De Grote Fontein | 4 Sovs | 1.80 Sovs — it is hand gel in a novelty bottle, and it is a good hand gel | **Removes 2 stacks of the Sharing the Love status.** Recommended by Lotte to every customer on the way out, cheerfully, sincerely, every time. Almost nobody buys one. |

### Services
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Gift wrapping | Free | Six seconds of expert ribbon work | Cosmetic wrap state on the item. Three papers: festive (pink, Venus print), plain, or the Collectie's own box ribbon. |
| Discreet plain packaging | Free | The reason a lot of these purchases happen at all | Item becomes non-identifiable in inventory; other NPCs will not react to it. |
| International mailing | 6 Sovs | 6 Sovs — postage plus the customs form she fills in herself | Item is removed from inventory and arrives in the epilogue. Postcards mailed this way generate an NPC reaction weeks later. |
| **The shop toilet** | Free | Incalculable | Available to anyone, ticket or no ticket. Restores a small amount of Composure. **The most-used facility on Museum Mile**, for reasons Lotte has never analysed. |

### Hidden Details / Easter Eggs
- **The Handreiniger counter**: The game silently tracks how many times Lotte has recommended the Handreiniger to this player and how many they have bought. The ratio is displayed nowhere during play and surfaces once, in the epilogue, as a single number. She never mentions it because she has never noticed it.
- **The square metreage**: Ask her twice in one conversation and she will give you the same figure with the same pleasure. Ask her on three separate visits and she will still tell you. Fifty-four. The old one was eleven.
- **The Lennon corner protectors**: Buy the print and examine it in inventory. She put corner protectors in without being asked and without charging for them.
- **The cold room**: Behind the counter. If the player asks where the chocolate is kept, she explains the cold room, the rotation, and why the case glass is doubled, in more detail than anyone wants. It is entirely accurate.
- **The framed fine notice**: Not in the shop — it hangs in the lobby, next to the 1985 opening photograph. Gerda Vonk's quarterly violation, framed. Lotte thinks this is a nice piece of shop history and dusts it.
- **The ribbon in her hair**: Changes colour daily on a seven-day cycle. Compliment it and she will tell you which spool it came off and how much of that spool is left.
- **The postcards people send to their mothers**: Genuinely the top-selling postcard. She has noticed and finds it mildly interesting and has drawn no conclusion from it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| **Gunter** (`shamsterdam_npc_gunter_01`, dipping-stick vendor, cart *Gunter's Deep Dips*, fountain plaza) | Cordial, purely logistical, entirely functional. Lotte sends people out to the cart; Gunter sends people in to use Lotte's toilet. They wave. They have never once discussed the fountain. Gunter's cart holds a straight-A hygiene card and he will point at it if asked. |
| **Anke** (ticket seller, fifteen years, deadpan, cross-stitch between customers) | Lotte likes her enormously. Anke's flatness and Lotte's brightness are the museum's two poles, and they are the same position arrived at from opposite directions — Anke burned the reflex out, Lotte never had it. They take breaks together. Anke is teaching her cross-stitch. Lotte is not good at it. |
| **Ruud** (floor attendant, young, professionally neutral, "this is my summer job") | Lotte mothers him slightly. She saves him the broken hollow pieces, tells him to eat something, and covers the floor if he needs five minutes. He is faintly embarrassed by this and accepts all of it. |
| **Gerda Vonk** (municipal hygiene inspector) | Quarterly visits. Gerda ropes the fountain for forty minutes, takes a sample, writes the same violation, and leaves. Lotte thinks Gerda is lovely and always offers her a coffee. Gerda always declines. Lotte always offers. This has now happened eight times. |
| **Femke** (manager, Condomerie Het Gulden Vlies — different district) | Adjacent trade, professional awareness only. Museum retail versus specialist retail. They have never met. Both run counters where the customer is the only awkward party. |
| **The Awkward Truffle** (serious Shamsterdam chocolate shop) | Direct commercial rival since the Cacaogalerij opened. Their chocolatier considers De Grote Fontein an abomination **on tempering grounds** — a fountain holds chocolate at the wrong temperature indefinitely and that is a craft crime — and not on hygiene grounds, which have not occurred to him either. Lotte does not take this personally and **buys her own personal chocolate there.** |
| **Ingrid** (The Tolerance Hostel) | No working relationship. Ingrid is on the museum's photo-album privacy exclusion list, which Lotte does not administer and has never seen. |
| **Lord Pilsner / Chadwick / Bradley** | The gift shop is the unavoidable exit; every visit ends at her counter. Pilsner asks whether the chocolate is real. Chadwick films the shop. Bradley buys the Collectie as a gag and carries it himself. She serves all three at exactly the same speed. |

### Territory / Social Dynamics
- **Museum staff division**: Anke holds the door and the money, Ruud holds the floor and the exhibits, Lotte holds the exit and the till. Three stations, no overlap, no friction. All three cover the toilet question.
- **The plaza handshake**: Lotte → Gunter for skewers, Gunter → Lotte for the toilet. It is the most efficient informal arrangement on Museum Mile and neither of them has ever described it out loud, let alone examined what it implies.
- **Museum Mile is the Cultural Alibi District.** The bros can now honestly say they went to a museum. Lotte is at the end of the museum, holding a ribbon spool, and she is the last thing that happens on the alibi.
- The shop faces the fountain. Lotte has her back to it for thirteen hours a day and always has.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Unavoidable — she is the exit. The greeting, the "everything, really" line, the first Handreiniger recommendation.
- **Every subsequent museum visit**: The shop again, because there is still no other way out. The Handreiniger recommendation fires every single time regardless of history.
- **Any purchase, anywhere in the museum**: Routed through her counter. Ticketing is Anke's; retail is hers.
- **Toilet visits**: Frequently the player's actual reason for entering the building, especially post-fountain. She never comments, never charges, never connects it to anything.
- **Post-fountain re-entry with Sharing the Love stacks**: She notices the chocolate, not the germs. "You've been at the fountain! It's good, isn't it."
- **Post-Shamsterdam Stomach**: One kind, oblivious line about the bench in the old wing.
- **Late game**: The full floor-space conversation, the Lennon conversation, and the 1985 line, all available at length in the 22:00–23:00 window.

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| **None** | **None** | **Lotte has no appearances outside Shamsterdam and never will.** She is a permanent staff member of a fixed building on Museum Mile, she has just been given twice the floor space she used to have, and she has no reason on earth to be anywhere else. The character is defined by being pleased with exactly where she is; putting her in Prague or Publandia would break the only thing she is about. | — |

### Evolution Through Game
Lotte does not change. The Handreiniger stays on the counter, faced forward, at 4 Sovs, and she recommends it in identical words on the first visit and the fifteenth. What changes is the player: the recommendation is background noise on visit one, a running gag by visit four, and — once Sharing the Love has stacked to four and Shamsterdam Stomach is one dip away — the single most useful sentence anybody in Shamsterdam has said to them. She was saying it the whole time. She was never warning anyone. She just likes the bottle.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| lotte_idle | Behind the wrapping-station counter, bright, upright, available | 40% |
| lotte_face_stock | Squares a row of boxes without looking at them. Her signature idle. | 25% |
| lotte_ribbon_curl | Runs a length of ribbon over the scissor blade. Habit, not task. | 20% |
| lotte_handreiniger_face_forward | Adjusts the little fountain bottle back to its exact angle beside the till | 15% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| lotte_greeting | Player enters the shop. "Come in, there's room." |
| lotte_best_seller_pitch | Any question about De Collectie. "People say 'ironic gifts' but they buy two so..." |
| lotte_chocolate_case_presentation | Any chocolate question. Island display, glass, solid-or-hollow. |
| lotte_gift_wrapping (3 frames) | Fold, ribbon, curl. Fast, practised, six seconds. |
| lotte_discreet_packaging | Plain brown paper. Entirely routine. No lowered voice, no change in posture. |
| lotte_lennon_print_handling | Two hands, turns it to the light. The only reverent frame in the shop. |
| lotte_postcard_recommendation | "Yes, you can mail them. Yes, people do mail them." |
| lotte_mailing_desk | Stamps, customs form, the pre-printed stack |
| **lotte_handreiniger_recommendation** | **Every single sale, without exception. Two-finger tap on the bottle. The shop's most-repeated animation.** |
| lotte_floor_space_enthusiasm | The square metreage. Both hands out. Her most open pose. |
| lotte_ringing_up | Transaction close |
| lotte_toilet_gesture | Waves toward the door behind her, mid-sentence, without turning |
| lotte_wave_goodbye | "We'll be here when you're ready." |

### Sprite States
| State | When Used |
|-------|-----------|
| lotte_counter | Default. Wrapping station and till are the same object. |
| lotte_island | Chocolate consultation; she walks round the display rather than leaning across it |
| lotte_portrait | Dialogue close-up, 128×128, (256,192) |
| lotte_high_contrast | Accessibility outline variant marking her as interactive, (128,416) |

---

## 🎯 Quest Integration

### Primary Quest (If Applicable)
- **Quest**: None. Lotte owns no quest and gates no content.
- **Role**: Vendor and **cure vendor**. She is one of three ways out of the Sharing the Love status and the only one that removes two stacks for money.
- **Trigger**: N/A — the shop is the museum's mandatory exit, so the interaction is unavoidable rather than triggered.
- **Outcome**: N/A

### Systems Administered
1. **Retail (both wings).** Legacy Venustempel merchandise and the Cacaogalerij chocolate line out of one till. Chocolate is now the majority of shop revenue and Lotte knows the figure.
2. **The Handreiniger cure.** 4 Sovs, removes **2 stacks** of Sharing the Love. Sits inside the wider germ mechanic she is not aware of and does not administer:
  - **Sharing the Love** is a stacking player-facing status (tiers 1–5+) gained at De Grote Fontein: **+1** per dip, **+2** for a double-dip, **+3** for dipping something already bitten, **+3** for a bare hand, **+5** for leaning into the cascade.
  - **Tier 5 triggers Shamsterdam Stomach**, a day-long debuff.
  - **Cures**: Gunter's 1 SOV hand wipe (**1 stack**), Lotte's 4 Sovs Handreiniger (**2 stacks**), sleeping at The Tolerance Hostel (**2 stacks**).
  - **Lotte never warns, never explains, and never connects symptoms to cause.** She recommends the bottle because it is a nice product. She has never connected it to the fountain.
3. **Gift wrapping / discreet packaging.** Free. Sets a cosmetic state on the item that determines whether other NPCs react to it in the player's hands.
4. **International mailing.** 6 Sovs. Removes the item from inventory and resolves it in the epilogue.
5. **The toilet.** Free, unticketed, universal. Small Composure restore. The most-used facility on Museum Mile.

### Quest Gate Function (If Applicable)
Lotte gates nothing and refuses nobody. She is positioned at a hard chokepoint — the museum's only exit — but she does not block it, charge for it, or comment on anyone passing through it. The chokepoint is architectural, not mechanical: the design intent is that the player *cannot leave without being offered a Handreiniger*, and can always decline.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Handreiniger | Any | Consumable | Removes 2 stacks of Sharing the Love |
| De Collectie (boxed set of six) | Any | Inventory (2 slots) | Gift item, visible to other NPCs, best margin in the shop |
| Solid / hollow chocolate piece | Any | Consumable | HP restore; the hollow piece degrades in heat |
| John Lennon sketch print (framed) | Any | Permanent | +Trivial Knowledge; unlocks the Lennon dialogue branch permanently |
| Giggling Figure postcard set | Any | Consumable if mailed | Mailable; triggers a delayed NPC reaction in the epilogue |
| "I JUMPED" T-shirt | Any | Permanent cosmetic | Wearable; other NPCs read it |
| Fountain keyring / fridge magnet | Any | Permanent cosmetic | Trinket. Sells constantly. |
| Wrapped / discreet packaging state | Any purchase | Cosmetic | Determines whether other NPCs react to the item |

### State Flags Set
- `lotte_met`: boolean
- `lotte_visit_count`: integer
- `handreiniger_offered_count`: integer (increments on every sale, forever)
- `handreiniger_purchased_count`: integer
- `lotte_floor_space_heard`: boolean
- `lotte_lennon_conversation`: boolean
- `lennon_print_owned`: boolean
- `collectie_purchased`: boolean
- `postcard_mailed`: boolean
- `venustempel_toilet_used_count`: integer
- `sharing_the_love_stacks`: integer (owned by the germ system, read by Lotte's shop UI)

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The two-finger Handreiniger tap at the exact moment the player's card comes back — the shop's most-repeated frame, and the one that gets funnier every time it fires
2. Lotte mid-Floor Space Enthusiasm, both hands out, with the chocolate island behind her and De Grote Fontein flowing through the window behind that
3. Bradley at the counter with De Collectie held in both arms like a passport, refusing to hand it over
4. The wrapping station in action: fold, ribbon, curl, six seconds, on a 45 Sovs boxed set of six graduated chocolate phalluses, with a pink Venus-print paper option visible on the rail
5. Lotte holding the framed Lennon print up to the light with genuine affection, in a room that also contains a chocolate fountain keyring display

### Meme Potential
- "Looking for something specific? We have... everything, really."
- "People say 'ironic gifts' but they buy two so..."
- "Fifty-four square metres. The old shop was eleven."
- "It's four Sovs. It's hand gel — look, the bottle's the fountain."
- "Yes, you can mail them. Yes, people do mail them."
- "We're here since 1985. We'll be here when you're ready."
- The Handreiniger declined, faced forward, declined, faced forward, declined, faced forward

---

## 🗣️ Voice Direction

### Accent
Dutch, late twenties, city, fluent and quick English with a light retail lilt. Not the flat Dutch directness of Anke or Femke — Lotte is warmer and faster, the register of somebody who genuinely enjoys talking to strangers about products. Diacritics and Dutch product names (*Handreiniger*, *De Collectie*, *De Cacaogalerij*, *De Mechanische Vleugel*, *De Grote Fontein*) pronounced naturally and without emphasis; they are just the names of things in her shop.

### Tone
- **Greeting**: Bright, welcoming, immediately useful. She gives you a direction in the first ten words.
- **Product description**: Brisk and factual, with the specific enthusiasm of a person who likes their stock. Cocoa percentages delivered exactly like paint colours.
- **The floor space**: The one place she is not in retail register. Slower, warmer, unmistakably proud. This is the character's heart and it should be played completely straight.
- **The Lennon print**: Quiet. Almost tender. "Look at the hand. He was good." — no lift at the end, no sell.
- **The Handreiniger recommendation**: Identical every single time. Same words, same pitch, same warmth, take one thousand. **Never wearier, never more pointed, never a flicker of awareness.**
- **Declines and refusals**: Zero disappointment. Nothing in her voice registers a lost sale as a loss.

### Key Delivery Notes
- **Never arch. Never knowing. Never a smile in the voice that means anything other than a smile.** If Lotte ever sounds like she is enjoying a joke at the customer's expense, the gift shop stops working and starts leering, and the satire's target flips from the bros onto the shop.
- **No pause before any product name.** She says "the Collectie" the way another shop assistant says "the tote bag." The absence of the pause is the whole performance.
- The trailing "...but they buy two so..." genuinely trails. She does not finish it because she has moved on to fetching one, not because she is being sly.
- "We have... everything, really." — the ellipsis is a woman mentally reviewing her stock, not a woman implying anything. Play it as inventory, not innuendo.
- The Handreiniger line must be recorded once and reused verbatim, forever. Do not record variants. Do not let a director add fatigue on take forty. The invariance is the gag.
- She is never a victim, never flustered, never the butt of anything. She is having a good day in a shop she likes.

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

- **HARD CANON: this character is LOTTE.** An earlier cross-reference in `npc_manager_femke.md` records the Venustempel gift shop attendant as "Petra" — that is a name collision with a Debaucheryville character and it is wrong. The correct name is and always was Lotte, as established in `venustempel.md` and in the Venustempel PNG asset doc. The Femke file needs a one-word fix in its Connections table.
- **Lotte is not in on the joke, in any frame, line, or take.** No knowing looks, no winks, no arch delivery, no pause before a product name. This is carried forward verbatim from the asset doc ("Lotte treats every transaction as completely normal in every frame... her cheerfulness is sincere and that is what makes the gift shop land") and it is the single load-bearing constraint on the character. If she reacts, the shop starts leering and the satire inverts onto the staff.
- **The Handreiniger recommendation must fire on every sale, forever, with zero variation.** One recording, reused. No fatigue variants, no escalation, no eventual acknowledgement. The player will notice the pattern; Lotte never will. If she ever comments on it, the running gag dies instantly.
- **She never warns, never explains, and never connects symptoms to cause.** She is a cure vendor who does not know she is a cure vendor. The germ mechanic (Sharing the Love, Shamsterdam Stomach, the three cures) is defined elsewhere and must not be redesigned in this file — Lotte only supplies the 4 Sovs / 2-stack option.
- The floor-space material is the character's emotional centre and must not be played as a joke about a small woman being happy about shelving. She was working out of an eleven-square-metre corridor and now she is not. Fifty-four. It is a genuine professional win and the document treats it as one.
- The **John Lennon sketches are real** — he really drew them, the museum really has them, the print is really licensed. Lotte's affection for the print is correct and should never be undercut. This is the one object in the building with actual artistic merit and the gift shop attendant is the person who noticed.
- The Cacaogalerij collection is **chocolate phalluses**, curated seriously, and the document says so plainly. No euphemism, no leering, no coy substitution in dialogue, UI strings, or item names. The comedy is the till, the margin, the shelf facing, and the postage — not the shape.
- **De Grote Fontein is not Lotte's.** She does not run it, clean it, defend it, or think about it. It is visible through her window all day and she has her back to it. Do not give her a fountain opinion.
- The toilet is free and unticketed and this is authored, not an oversight. It is the most-used facility on Museum Mile and the reason is never stated by anyone.
- Roster JSON does not exist for this location yet. Anke, Ruud, and Gerda Vonk are all unprofiled and should be picked up in the same pass that authors `venustempel_npcs.json`, alongside Gunter (`npc_gunter.md`, profiled).
- Sprite work: five new frames required for the relocation (Handreiniger Recommendation, Floor Space Enthusiasm, Chocolate Case Presentation, Lennon Print Handling, Mailing Desk). Existing Lotte allocations on `npc_venustempel_staff.png` are unchanged and still valid.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — **Lotte has no crypto.** None. Sovs and card only, 3.50 Sovs–45 Sovs. A museum gift shop takes a card.
- [x] **NO automatic crypto assumptions** — this NPC does not earn crypto, has never earned crypto, and none is to be added. There is no kiosk, no QR code, no SOVS signage, and no shitcoin anywhere in the Venustempel gift shop.
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A. No crypto at this location.
- [x] **The bros are never scam-aware** — there is no scam. Every price in the shop is fair, every product is what it says it is, and Bradley paid 45 Sovs for a real boxed set of real chocolate and called it a gag.
- [x] **Nothing winks** — Lotte structurally cannot wink; the asset doc forbids the sprite and this profile forbids the take. No line in this file signals that any of it is satire.
- [x] **Focus on city-specific cultural exploitation instead** — the satire is the Cultural Alibi District: a well-run business selling exactly what tourists want, at fair prices, to people who need to be able to say they went to a museum.

### Satirical Target Verification
- [x] **Targets tourist/frat bro behavior, NOT local culture or ethnicity** — the joke is three grown men who cannot buy chocolate without narrating it, in a shop where the staff and the pricing are entirely reasonable. Dutch matter-of-factness is presented as straightforwardly correct.
- [x] **NPC is savvy entrepreneur, not villain or stereotype** — Lotte is a competent retail professional with real product knowledge, real margins, free services she is not obliged to offer, and a toilet she lets anyone use.
- [x] **Humour is affectionate mockery, not mean-spirited** — Lotte is never flustered, never a victim, and never the punchline. She is having a good day. The worst thing that happens to her in the entire location is that a nice 4 Sovs hand gel does not sell.
- [x] **Adult content handled without leering** — nothing is depicted. The collection is described plainly and repeatedly as what it is, and the entire comic apparatus is retail mundanity: the till, the ribbon rail, the best-seller, the cocoa percentage, the customs form, and the hygiene nobody thinks about.

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Venustempel/npc_lotte_beekman.md`
- **Registered In**: `venustempel_npcs.json` — **No — roster JSON not yet authored for this location.** Registration pending; flagged for the JSON authoring pass alongside Anke, Ruud, Gunter, and Gerda Vonk.
- **Sprite Sheet**: `npc_venustempel_staff.png` — existing allocations at (256,192) portrait, (384,192) idle, (448,192) gift wrapping, (0/64/128/192, 320) extras, (128,416) high-contrast. Five new relocation frames required; see Sprite Notes.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile; authored as part of the Museum Mile relocation. Sourced from `venustempel.md` + `PNG_Assets/Venustempel_PNG_Assets.md`, both of which are being rewritten concurrently for the move from Roodelicht Row to Museum Mile (entry 5 Sovs → 9 Sovs; De Cacaogalerij absorbed; De Grote Fontein added). Name collision resolved: the gift shop attendant is **Lotte**, not the "Petra" recorded in `npc_manager_femke.md`. New: doubled floor space characterisation, the full chocolate line, and the Handreiniger cure-vendor role in the Sharing the Love germ mechanic. | Design |

---

*Template Version 1.1*
