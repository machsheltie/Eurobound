# Item Definition: Bottle Opener Keychain

*"Bottle Opener Keychain (16 Different Breweries)" — for opening beers with maximum jingling and zero class*

## 📋 Item Identity
- **Item ID**: `bottle_opener_keychain`
- **Display Name**: Bottle Opener Keychain
- **Internal Name**: The pre-loaded frat-bro keyring — ONE container item that every earned brewery opener clips onto [source: design/quests/general_quests/brewerytour.md L33-34]
- **Item Type**: Hybrid (Permanent Cosmetic + Quest Container)
- **Rarity**: Common origins (bros treat it as Legendary)
- **Source**: The Blarney Trap, Publandia — GRANTED the instant the bros order the special beer for the first time, together with The Blarney Trap's opener and the Brewery Passport Book [source: design/quests/general_quests/brewerytour.md L27-42]

---

## 🎭 The Deception

### What The Item Actually Is
A single, well-worn keyring the bros have been adding to for years — a jangling mass of cheap dive-bar giveaway bottle openers, half of them already tarnished before they ever left home. It already carried mementos from a lifetime of blackout drinking before Europe ever entered the picture: collected from spring break trips to ⚠ AUTHOR-REVIEW: Blackout Bay and Hangover Shores, and picked up at fake-tropical chain bars like ⚠ AUTHOR-REVIEW: Señor Sloppy's. In Publandia it gets its 16th-country upgrade: one opener earned per brewery, all sixteen, across four cities.

### What The Bros Believe It Is
"This is basically a drinking résumé you can wear. Sixteen breweries, four countries, zero regrets. You see a guy's keychain, you know his whole life story — and ours says LEGEND."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A — never sold. GRANTED on the Publandia special-beer order trigger (author ruling 2026-08-04) [source: design/quests/general_quests/brewerytour.md L27-34] |
| **Actual Value** | A handful of cheap, mismatched giveaway openers — marginal Sovs at most |
| **Resale Value** | 0 Sovs (worthless, and quest-critical besides) |
| **Can Be Sold** | No |
| **Can Be Dropped** | No (permanent quest container) |
| **Can Be Traded** | No |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Mismatched metals accumulated over years — "authentic" brass that's really spray-painted zinc, tarnished gold-tone, brushed chrome, aged bronze, whatever each brewery handed over |
| **Size** | One heavy-duty steel keyring, growing more crowded with every brewery cleared (up to 16 openers) |
| **Closure** | Clipped to a belt loop, permanently, cargo shorts and all |
| **Text/Markings** | None uniform — every attached opener carries its own inscription (see each opener's own item doc in `design/items/brewery_tour/`) |
| **Sound** | Constant, unmistakable jingling — the whole point and the whole problem |

*(No per-character color variants — per the master spec, the keychain is ONE shared party item, not one per bro [source: design/quests/general_quests/brewerytour.md L33-34]. No Degradation Over Time table — the keychain doesn't degrade, it accumulates; a decay table would misrepresent it.)*

---

## 📊 Stats & Effects

### Direct Stats
```
Party Prep:          +3 (a keychain full of tools for a trip full of problems)
Bro Credibility:     +1 (undeniable proof of drinking tourism)
Airport Security:    -1 (TSA does not find "sixteen bottle openers" reassuring)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **Bartender Recognition** | European bartenders offer better prices and exclusive local brews because "you clearly know your beer" |
| **Beer Credential Gate** | Certain pub NPCs won't talk to you until you've got "proper beer credentials" to flash |
| **Cultural Buffs** | ⚠ AUTHOR-REVIEW: In the Prostoberg/Lagerovia areas, locals treat you with noticeably more respect |
| **Constant Jingling** | Audible cringe on every single step — carries especially well in a quiet European cathedral |

### What It Does NOT Do
- ❌ Reduce the jingling. Ever.
- ❌ Get you through airport security quietly
- ❌ Stop weighing down the cargo shorts
- ❌ Become unnecessary just because twist-off caps exist

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change
Once granted, the keychain is permanently clipped to a belt loop and visible/audible for the rest of the game. It cannot be removed, hidden, or silenced — every opener earned across the 16-brewery tour attaches to it and stays.

### Sprite Implementation
- **Visibility**: Always visible, clipped at the hip/belt loop
- **Layer**: Accessory overlay, waist layer
- **Animation**: Jingles and sways with movement; newly earned openers appear on the ring as they're collected
- **Audio**: Constant low jingle SFX loop while equipped — louder and more mortifying in quiet interior spaces (cathedrals, libraries, museums)

### Peak Frat Bro Cringe
- Jangles loudly with every step — collected from spring break trips to ⚠ AUTHOR-REVIEW: Blackout Bay and Hangover Shores
- Weighs down their cargo shorts
- Makes noise in every quiet European cathedral
- "Dude, I got this one at ⚠ AUTHOR-REVIEW: Señor Sloppy's!"
- Still using it even though twist-offs exist
- Each opener tells a story of regrettable decisions

---

## 🗣️ NPC Reactions

### When NPCs Notice The Keychain
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| European Bartenders | Offer better prices and exclusive local brews because "you clearly know your beer" | "We're basically locals now" |
| Gatekept Pub NPCs | Won't talk to you without "proper beer credentials" | *bros just flash the keychain like a badge* |
| Debaucheryville Locals | ⚠ AUTHOR-REVIEW: "Ah, you have the One True Pils opener! You understand REAL beer, not American water!" | "We're basically beer sommeliers now" |
| Prostoberg Locals | ⚠ AUTHOR-REVIEW: Beer-festival NPCs treat you like family instead of tourists | "We've been adopted" |
| Abbeyvale Monks | ⚠ AUTHOR-REVIEW: The Brothers of Our Lady of Perpetual Hops actually let you into their secret brewery areas | "We're basically monks now" *(they are not)* |
| Publandia Pub Crawl Guides | Offer you the "locals only" route | "VIP treatment, obviously" |

### Callback Dialogue Throughout Game
**Chadwick** (admiring the collection):
> "Bro, remember when we got this one at that sketchy beach bar?"

**Bradley** (reminiscing):
> "Dude, that's where you hooked up with that girl with the fake ID!"

**Lord Pilsner** (declaring intent):
> "Gentlemen, our European adventure demands we add to this legendary collection!"

---

## 🔗 Quest Integration

### Source Quest
- **Quest Family**: Brewery Tour (16 breweries, 4 cities × 4) [source: design/quests/general_quests/brewerytour.md L12]
- **Quest Giver**: Seamus, owner of The Blarney Trap
- **Location**: The Blarney Trap, Publandia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| The entire Brewery Tour sidequest | The one-time trigger: ordering the special beer at The Blarney Trap, Publandia [source: design/quests/general_quests/brewerytour.md L27-31] |
| Each brewery's stamp, brewmaster selfie, opener, and signature beer | Completing that brewery's challenge while carrying the keychain [source: design/quests/general_quests/brewerytour.md L45-58] |
| Better bartender pricing and exclusive local brews | Simply possessing the keychain, anywhere in Europe |

### Achievement
None directly on this item — see `brewery_passport_book_item.md` for "Continental Beer Master" and "Photogenic Drinker." The "Key Collector" achievement (own-all-openers) was ruled DEAD as redundant under the earned-opener model, 2026-08-05 [source: docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md, Salvage 28 ruling].

---

## 🎬 Key Story Moments

### The Trigger (Acquisition)
*At The Blarney Trap, Publandia, the bros order the special beer for the first time — the one-time event that opens the entire tour.* [source: design/quests/general_quests/brewerytour.md L27-31]

The keychain, The Blarney Trap's opener, and the Brewery Passport Book change hands together in that single moment. Before this order, no brewery anywhere will hand over a stamp, sell a signature beer, or part with an opener — the tour does not exist for the player until this fires. [source: design/quests/general_quests/brewerytour.md L40-42]

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: Small fixed accessory overlay (belt/hip clip) — the engine renders one keychain silhouette; the individual dangling openers are the 16 sprites specified in `design/items/brewery_tour/opener_*_item.md`
- **Memory**: Minimal (simple overlay + looping ambient jingle SFX)
- **Animation**: Syncs with movement, no additional frames needed beyond the base jingle-sway loop

### Performance Impact
- Negligible additional draw calls
- Persistent low-priority ambient audio loop while equipped (must not compete with combat/dialogue audio)
- No particle effects or dynamic lighting requirements

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ✅ |
| Acquisition (grant trigger) documented | ✅ |
| Stats and effects specified | ✅ |
| Visual specifications complete | ✅ |
| NPC reactions documented | ✅ |
| Quest integration clear | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| 16-brewery count used throughout | ✅ |
| No real-world place or brand names remain | ✅ |

---

## 📝 Development Notes

- **Degradation Over Time section omitted** — the keychain accumulates (openers added across the 16-brewery tour) rather than degrading; a decay table would misrepresent it, per this task's omit-what-doesn't-fit instruction.
- **Per-Character Variants section omitted** — the keychain is ONE shared party item, not per-bro [source: design/quests/general_quests/brewerytour.md L33-34].
- **Distinction From Equipment section omitted** — no equippable counterpart exists for this item.
- **Six real-world references replaced** with author-approved parody stand-ins, per the Gap 21–26 ruling (2026-08-05, batch-reviewed): a Mexican spring-break resort → Blackout Bay; a Florida spring-break beach strip → Hangover Shores; a real chain party bar → Señor Sloppy's; a real German beer-festival city → Prostoberg; a real monastic brewing tradition and its home country → Abbeyvale/the Brothers of Our Lady of Perpetual Hops; a real legendary lager brand and its home country → Lagerovia/The One True Pils. All flagged ⚠ AUTHOR-REVIEW inline above; every one of these is a background-flavor reference only, not a new visitable location. [source: docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md Gap Manifest #21-26 and Rulings]
- Purchase language fully retired: this item is never bought, never a Pint-Off reward — granted once, on the trigger, full stop [source: design/quests/general_quests/brewerytour.md L27-34].
