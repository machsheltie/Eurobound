# The Absinthium Taproom

*A surrealist absinthe den where gravity feels inconsistent, mirrors reflect alternate versions of yourself, and the bartender insists the wormwood lawsuits were "greatly exaggerated"*

## Location Identity
- **Location ID**: debaucheryville_brewery_absinthium_taproom_01
- **Display Name**: The Absinthium Taproom
- **Bohemian Alias**: "Absintová Komnata"
- **Satirical Subtitle**: "Not Recommended for Those Prone to Introspection"
- **World Location**: Debaucheryville
- **Area Zone**: Hidden behind the Absinthe Arcade (north end)
- **Location Type**: Mind-Bending Microbrewery / Brewery Tour Location #1 / Puzzle Dungeon / Reality Distortion Zone

## Access & Requirements
### Entry Conditions
- **Time Restrictions**: 8 PM - 4 AM (the Green Fairy only appears after dark)
  - *Author ruling 2026-11-13 (Desk `orch-vanek-q6-hours`):* "Yes: only 20:00-04:00; the bar's empty otherwise". Dr. Vaněk is at the bar only 20:00-04:00 game time.
- **Stat Requirements**: None, but Confusion resistance recommended
- **Item Requirements**: The Bottle Opener Keychain from The Blarney Trap (the one keychain; required to collect ANY opener, author ruling v43 `bp_publandia_gates`) and The Absinthium Taproom Bottle Opener (required for the stamp and the signature brew)
- **Previous Location Requirements**: Must find entrance through Absinthe Arcade
- **Special Conditions**: Hidden entrance behind glowing green velvet curtain

### Bottle Opener Requirement
- **Prerequisite**: The Bottle Opener Keychain from The Blarney Trap — "you have to have the keychain from the blarney trap to collect any opener. none can be gotten without it" (author ruling v43 `bp_publandia_gates`, 2026-11-12)
- **Location-Specific Opener**: The Absinthium Taproom Bottle Opener
- **Design**: Cracked absinthe glass with Green Fairy silhouette emerging, bottle opener as the glass stem
- **Material**: Emerald-tinted metal with iridescent "oil slick" finish
- **Inscription**: "I Saw Myself"
- **Acquired**: Complete the Mirror Maze navigation puzzle. EARNED ONLY: "The opener must be earned, cannot be bought." (author ruling v41–42). ~~OR purchase for 22 SOVS~~ (dead)
- **Special Feature**: Surface appears to shift colors in different lighting (lenticular effect)
- **Check Point**: Dr. Vaněk checks for the Bottle Opener Keychain (tour access, ruling v43) AND this opener (stamp/beer access)
- **Without the Keychain**: Cannot participate in brewery tour at all
- **Without Absinthium Opener**: Can explore and complete puzzle, but cannot receive stamp or purchase Absinthe Lager until opener acquired
  - *Author ruling 2026-11-13 (Desk `orch-vanek-q5-backfill`):* "Yes: he hands it over the first time they come back with the keychain". Opener backfill: holding the keychain without his opener, the party is handed the opener once. His line for it is not yet written (Writers' Room).

**Dr. Vaněk's Opener Check**:
- *With the Keychain, No Absinthium Opener*: ~~"Seamus's network extends even here. You have quest access. Now earn YOUR opener — complete my maze, or pay 22 SOVS. Then we discuss stamps and signature brews."~~ **STRUCK (offers the dead 22 SOVS purchase path; ruling v41–42). Replacement line: the Writers' Room writes it (author ruling v44 `vanek_check_lines` = trim); the opener item doc salvages "Excellent. Complete my maze." as ambient.**
- *With Both Openers*: "The cracked glass. You've navigated the mirrors. Either way, you've committed. The Absinthe Lager awaits. Prepare for... introspection." (author ruling v44 `vanek_check_lines` = trim: the clause "— or paid for the privilege" is cut; nothing else changed. Note for the Writers' Room: "Either way" now has no second way.)
- *Without the Keychain*: "No Publandia key, no brewery tour access. The Continental Trail has protocols. Return when properly credentialed."

### Exit Conditions
- **Normal Exit**: Through the curtain (if you can find it again)
- **Dungeon Exit**: Complete the mirror navigation puzzle
- **Completion Requirements**: Reach the bar, survive the Green Fairy Wisp
- **Failure States**: "Lost in Reflection" returns to Arcade entrance
- **Progressive Unlocks**: "Reality Anchor" status after completing navigation puzzle without Confusion

## Visual Design
### Exterior Description (Hidden Entrance)
- **Location**: Behind a glowing green velvet curtain at the north end of Absinthe Arcade
- **Visible Cues**: Vapor seeps under the curtain and swirls in impossible patterns
- **Signage**: Small brass plaque reads: "Not recommended for those prone to introspection."
- **Sound**: Faint, distorted music that seems to come from everywhere and nowhere
- **Atmosphere**: The green glow pulses like breathing, beckoning
- **Environmental Context**: Most arcade patrons don't notice it; those who do hesitate

### Interior Layout — The Distortion Den

**The Entry Veil (Transition Zone)**
- The moment you peel back the curtain
- Vapor hits your face "like regret in your 30s"
- Reality begins to bend
- Last chance to turn back (you won't)

**The Mirror Maze (Navigation Puzzle)**
- Room appears to extend infinitely in all directions
- Mirrors line every surface — walls, ceiling, floor fragments
- Some mirrors are portals (teleport to different sections)
- Some mirrors are traps (reverse controls, apply Confusion)
- Some mirrors show your reflection... doing things you're not doing
- Navigation requires identifying the "true" path vs. illusions

**The Main Hall (The Impossible Room)**
- Central space where geometry fails
- Furniture appears mirrored or misaligned from itself
- Chairs exist at angles that shouldn't support sitting
- Tables tilt but drinks don't spill (or do they?)
- Floating candlelight drifts without pattern
- Green spectral mist rolls across the floor

**The Bar (The Cracked Bottle)**
- Bar counter shaped like a massive cracked absinthe bottle
- Glowing green liquid constantly drips from the crack into a void below
- The void has no bottom (don't look too long)
- Dr. Vaněk's domain
- Where the signature brew is served
- Stamp station for Brewery Passport

**The Gallery of Selves (Patron Area)**
- Tables scattered through impossible space
- Portraits on walls that sometimes blink
- Whispered conversations from half-visible figures
- Where couchsurfing opportunity exists
- Where Mirror Chad spawns

### The Mirror Portal System
| Mirror Type | Visual Cue | Effect |
|-------------|------------|--------|
| True Mirror | Subtle gold frame | Passage to next section |
| Portal Mirror | Rippling surface | Teleport to random section |
| Trap Mirror | Your reflection smiles first | Reverses controls (30 sec) |
| Confusion Mirror | Shows you older/younger | Applies "Green Fairy Confusion" |
| Truth Mirror | Shows you clearly | Reveals all mirror types for 10 sec |

**Navigation Solution**: Find and use Truth Mirror, then navigate to True Mirrors only

### Technical Specifications
- **Color Palette**: Primary: Absinthe Green (#7FFF00), Accent: Void Black (#0D0D0D), Background: Mist Silver (#C0C0C0), Reality Fracture Purple (#9400D3)
- **Lighting Setup**: Floating candles, green glow from below, flickering reality
- **Particle Systems**: Green mist (extensive), mirror shimmer, reality fracture effects, floating dust
- **Animation Elements**: Mirror reflections moving independently, furniture shifting, dripping void liquid
- **Performance Optimization**: Simplified mirror effects, reduced mist density, static furniture option

## Satirical Design
### Theme & Vibe
**Core Concept**: The Absinthium Taproom is a surrealist nightmare of absinthe culture taken to its logical extreme. Where absinthe tourists go expecting "the Green Fairy experience," they find a place where that experience is LITERAL — reality bends, reflections have opinions, and the bartender's lab coat suggests this might all be an experiment you didn't consent to.

### Cultural Targets
- **Primary Satirical Focus**: Absinthe mysticism, "mind-expanding" tourism
- **Secondary Targets**: Pseudo-scientific drink culture, the Green Fairy myth
- **Cultural Specificity**: Debaucheryville's absinthe bar scene, Eastern European experimental venues
- **Humor Approach**: Taking absinthe's hallucinogenic reputation literally
- **Sensitivity Considerations**: Satirizes marketing myths, not addiction or substance abuse

### Buffoon Delusion Scenarios
**What bros THINK is happening**: Cool absinthe bar with trippy vibes

**What is ACTUALLY happening**: Reality distortion zone with actual navigation hazards

**The Taproom journey**:
1. "Dude, there's a CURTAIN. It's GLOWING. We HAVE to go in."
2. *vapor hits face*
3. "Whoa, this place is— wait, which way did we come from?"
4. *reflection winks*
5. "Did my reflection just— bro, are you seeing this?"
6. *Mirror Chad appears*
7. "Why does my evil twin know about my commitment issues?"

## Gameplay Mechanics
### Navigation Puzzle System

**Mirror Maze Structure**:
- 5 sections connected by mirrors
- Each section has 4-6 mirrors
- 1 True Mirror per section (correct path)
- 2-3 Portal Mirrors (random teleport)
- 1-2 Trap Mirrors (control reversal/Confusion)
- 1 Truth Mirror per section (reveals types for 10 sec)

**"Reality Anchor" Achievement**:
- Complete navigation puzzle without triggering Confusion
- Reward: Permanent +10% Confusion resistance

### Mirror Chad Encounter
**Mirror Chad**
- **Type**: Hallucination Enemy / Mini-Boss
- **Appearance**: Your own sprite, but mirrored and distorted
- **Combat**: Must defeat in 3 turns or he applies "Confused"
- **Dialogue**:
  - Turn 1: "You ever think maybe you're the problem, bro?"
  - Turn 2: "Everyone you've annoyed? They remember. They ALL remember."
  - Turn 3: "You're exactly like your father. Think about it."

**Bros' Mirror Chad Dialogue**:
- **Lord Pilsner's Mirror**: "You peaked in college. Everything since has been a long, sad encore."
- **Chadwick's Mirror**: "Nobody watches your content. The algorithm hates you. It's personal."
- **Bradley's Mirror**: "You're not the smart one. You're the one who talks like he is."

### Green Fairy Wisp Boss
**Boss Phases**:

*Phase 1 — The Tease (100-66% HP)*
- Single Wisp, "Confusion Breath": 40% chance to apply Confused
- "You sought me, and now you've found me. Was it worth it?"

*Phase 2 — The Split (66-33% HP)*
- Splits into 3 Wisps (2 illusions, 1 real)
- "Which version of yourself would you prefer?"

*Phase 3 — The Reckoning (33-0% HP)*
- Room distortion increases, control reversal possible
- Final attack: "The Truth" — shows player a vision

**Rewards**:
- "Green Fairy Essence" (consumable, guaranteed Confusion but +30 Bravado)
- Stamp eligibility

## Brewery Tour System Integration

### Tour Position
- **City**: Debaucheryville
- **Slot**: 1 of 4 (First location)
- **Brewery Type**: Actual microbrewery (produces own signature beer)
- **Dungeon Type**: Puzzle-based (mirror navigation)

### Stamp Details — The Absinthium Seal
- **Design**: Green fairy silhouette trapped inside cracked absinthe glass
- **Ink Color**: Shifting emerald (appears to move in certain light)
- **Inscription**: "I Saw Myself"
- **Position**: Slot 1 on Debaucheryville passport page

**Stamp Animation**:
1. Green mist particles gather on page
2. Mist swirls into fairy shape
3. Glass outline materializes around fairy
4. Crack appears with ethereal chime
5. Stamp solidifies with flash

**Unlock Conditions** (ALL required):
- Complete mirror navigation puzzle (reach the bar)
- Defeat OR survive Green Fairy Wisp encounter
- Purchase Absinthe Lager from Dr. Vaněk
- Present the Bottle Opener Keychain (from The Blarney Trap; ruling v43)

**Dr. Vaněk's Stamp Speech**:
"Congratulations. You've seen yourself. Not everyone does — some people navigate the mirrors without ever looking INTO them. You looked. The stamp is proof. The memory is punishment. Or reward. The distinction is philosophical."

### Signature Beer — Absinthe Lager
| Attribute | Value |
|-----------|-------|
| Style | Absinthe-infused lager (legally questionable) |
| ABV | 8.5% |
| HP Restoration | — |
| Bravado Restoration | +15 |
| Buff | None |
| Debuff Risk | 30% "Green Fairy Confusion" to USER |
| Price | 12 SOVS |
| Brewed By | The Absinthium Taproom (in-house) |

**Flavor Text**: "It's not a bug, it's a feature. The disorientation means it's working."

**Unique Properties**:
- Only signature beer designed to potentially debuff the user
- Confusion effect matches the location's theme
- Can be strategically used to trigger Confusion-based achievements

**Dr. Vaněk's Serving Dialogue**:
- "The Absinthe Lager. My signature creation. The green fairy is IN the beer. Metaphorically. And slightly literally."
- "You may experience mild disorientation. This is intentional. If you DON'T feel disoriented, tell me immediately — I need to adjust the formula."
- "30% confusion chance. 100% authenticity. Those are better odds than reality offers."

### Selfie Spot — Floating Absinthe Chalice
- **Location**: Behind the bar, floating inexplicably
- **Standard Photo**: Player with floating chalice, green mist swirling
- **Special Variant**: "The Research Subject" — With Dr. Vaněk (complete his survey)

### Cross-Brewery Dialogue
**To The Tap Dat Vault**:
- Dr. Vaněk: "Vapor brewing. Interesting. Insufficiently disorienting for my tastes, but the rhythm integration shows creativity."

**To Three-Crown Keg Haus**:
- Dr. Vaněk: "They brew with tradition. I brew with transcendence. Both create altered states. Theirs just smells worse."

**To Ye Olde B.R.E.W. Lab**:
- Dr. Vaněk: "Algorithms? I manipulate PERCEPTION. Much more interesting than random number generators pretending to be intelligent."

## NPCs & Characters
### Dr. Miloš Vaněk (Proprietor)
- **Role**: Bartender, chemist, researcher, reality architect
- **Appearance**: 50s Bohemian man, lab coat over vest, monocle, perpetually taking notes
- **Background**: Former chemistry professor, "left academia to pursue practical applications"
- **Philosophy**: "The Green Fairy is a metaphor. I've simply made the metaphor... tangible."

**Key Dialogue**:
- "We used to use actual wormwood, until the lawsuits. Now we use... alternatives."
- "I am not a 'mad scientist.' I am a 'methodologically adventurous beverage engineer.' There's paperwork."
- "People pay for 'experiences' now. I provide feelings. Specifically, confusion and mild existential dread. It's very popular."

### The Bros' Reactions
- **Lord Pilsner** (entering): "Dude. DUDE. This place is INCREDIBLE. Why is there three of you?"
- **Chadwick**: "There's not three of me. There's three of YOU."
- **Lord Pilsner**: "...that's worse. That's definitely worse."

- **Bradley** (navigating): "I'm keeping a mental map of the mirror positions. I'm... unsure which of me is mapping."
- **Dr. Vaněk**: "Fascinating. May I take notes?"

### Couchsurfing Integration
**Host**: "The Philosopher" — a regular who's been here so long they might be part of the furniture

**Stay Effects**:
- Rest partially restores HP/Bravado (50%)
- "Existentially Rested" status: +5 INT, -5 Bravado (2 hours)
- Morning dialogue: "Did you dream, or did the room dream you?"

### Status Effects (Location-Specific)
- **"Green Fairy Confusion"**: Reversed controls, random dialogue choices (30 sec - 3 min)
- **"Saw Yourself"**: -5 Bravado, introspective dialogue options unlocked (1 hour)
- **"Reality Anchor"**: +10% Confusion resistance (permanent, if achieved)
- **"Existentially Rested"**: +5 INT, -5 Bravado (from couchsurfing, 2 hours)

## System Integration
### Cross-Location Dependencies
- **Absinthe Arcade**: Physical entrance, thematic connection
- ~~**Shadow Exchange**: Bottle Opener sold here~~ (dead: openers are earned, never sold; ruling v41–42 and 2026-08-04)
- **Cirque du Shady**: Thematic overlap (surrealism, disorientation)
- **ICQ Network**: Dr. Vaněk occasionally posts "research findings"

### Quest Integration
- **"The Green Fairy"**: Main quest to find and complete the Taproom
- **"Vaněk's Survey"**: Optional research participation (rewards: the Participant Wristband and the "The Research Subject" selfie; full text in "Vaněk's Survey" below)
- **"Mirror, Mirror"**: Defeat Mirror Chad without taking damage
- **"Reality Anchor"**: Complete puzzle without Confusion

### Vaněk's Survey (APPROVED, author 2026-11-13, Eurobound Desk 4ti-q1 "Approve all 6 and the opener/closer", 4ti-q2 "B: selfie + Participant Wristband")

Optional research participation. Consent is recorded (`vanek_survey_consented`). For each question the player picks one bro answer; every answer is accepted, none is right, and none changes a stat. Vaněk gives the same reply whichever answer is picked. Drafted by Claude (author route, orch-vanek-q2).

**Opener** (Vaněk, clipboard out): "Participation is voluntary. Leaving is also voluntary. Nobody has done it yet."

1. **Vaněk:** "On a scale of one to ten, how many of you are there right now?"
   - **Bro answers:** "Three" / "Ten" / "Which ones count?"
   - **Vaněk (any answer):** "Consistent with the control group. The control group is a mirror."
2. **Vaněk:** "When you looked into the mirrors, who looked back?"
   - **Bro answers:** "Me, but hotter" / "My dad" / "Nobody, I was busy"
   - **Vaněk (any answer):** "Noted. He usually does."
3. **Vaněk:** "Describe the green fairy in one word."
   - **Bro answers:** "Hot" / "Mean" / "Mom?"
   - **Vaněk (any answer):** "Everyone says the third one eventually."
4. **Vaněk:** "How many drinks have you had tonight?"
   - **Bro answers:** "Like four" / "What counts as a drink" / "I don't count, I'm not a nerd"
   - **Vaněk (any answer):** "I will write 'like four.' I always write 'like four.'"
5. **Vaněk:** "Any side effects?"
   - **Bro answers:** "My teeth feel loud" / "I can taste the color green" / "None, I'm built different"
   - **Vaněk (any answer):** "'Built different.' Third time this week. I've added it to the list of symptoms."
6. **Vaněk:** "Final question. Do you consent to this survey?"
   - **Bro answers:** "Yes" / "What survey" / "Yeah bro"
   - **Vaněk (any answer):** "Retroactive consent. The ethics board will be thrilled. The ethics board is me."

**Closer** (Vaněk): "Thank you. Your data will be used for science, or for my memoirs. The distinction is philosophical."

**Reward (4ti-q2, option B):** the "The Research Subject" selfie variant, plus the **Participant Wristband**, a hospital-style band (junk item). Inspect: "SUBJECT 0417. ALLERGIES: NONE KNOWN. DO NOT RESUSCITATE WITHOUT CONSENT FORM." Item doc: `design/items/debaucheryville_items/participant_wristband_item.md` (4ti-q3: "B (chosen for science), no effect, can't sell"); engine key `participant_wristband` in `game/assets/data/items/key_items.json`.

### Achievement Track
- **Found the Curtain**: "Curious" — you noticed
- **Completed Navigation**: "Oriented" — against all odds
- **Defeated Mirror Chad**: "Self-Aware" — painfully
- **Defeated Green Fairy Wisp**: "Fairy Slayer" — mythology defeated
- **Reality Anchor**: "Grounded" — Confusion-free completion
- **Got the Stamp**: "Absinthium Certified" — you saw yourself

## Audio Design
### Environmental Audio
- **Navigation Maze**: Distorted echoes, whispered voices, mirror shimmer sounds
- **Main Hall**: Impossible ambient tones, glass dripping into void
- **Bar Area**: Liquid pouring, Dr. Vaněk's pen scratching, Green Fairy hum
- **Music Style**: Ambient, dissonant, occasionally beautiful, never quite right

## Implementation Specifications
### Technical Requirements
- **Asset List**: Arcade curtain, mirror maze (5 sections), main hall, bar, Gallery of Selves, mirror types (5), Dr. Vaněk, patrons, Mirror Chad, Green Fairy Wisp, green mist effects
- **Performance Budget**: 60 FPS target, max 15 draw calls, 40MB memory
- **Platform Considerations**: Simplified mirror effects, reduced mist, static candles option

### Development Timeline
- **Asset Creation**: 10 hours
- **Implementation Phase**: 12 hours (navigation puzzle, Mirror Chad, boss fight, brewery tour integration)
- **Testing Requirements**: Puzzle clarity, boss balance, Confusion timing, stamp triggers
- **Polish Phase**: 6 hours

## Quality Assurance Checklist
- [x] **World consistency verified** (Debaucheryville specific)
- [x] **Cultural specificity confirmed** (Debaucheryville absinthe scene)
- [x] **Satirical targets appropriate** (Absinthe mysticism, not substance abuse)
- [x] **Gameplay value established** (Puzzle, boss, brew reward)
- [x] **Original content preserved** (All mechanics, NPCs, dialogue)
- [x] **Brewery tour integration complete** (stamp, signature beer, bottle opener check, selfie spot)

---

## PNG Asset Requirements Summary

### Environment Art (14 PNGs)
- curtain_entrance.png - 256x384 - Glowing green veil
- mirror_maze_section.png - 384x384 x5 - Puzzle areas
- main_hall_impossible.png - 512x512 - Central space
- bar_cracked_bottle.png - 384x256 - Dr. Vaněk's domain
- gallery_of_selves.png - 384x384 - Patron area
- void_drip.png - 128x256 - Endless fall
- floating_candles.png - 192x192 - Drifting light
- green_mist_layer.png - 512x128 - Floor atmosphere
- blinking_portraits.png - 256x192 - Wall decorations
- mirror_true.png - 96x192 - Gold frame
- mirror_portal.png - 96x192 - Rippling surface
- mirror_trap.png - 96x192 - Smiling reflection
- mirror_confusion.png - 96x192 - Age-shifted image
- mirror_truth.png - 96x192 - Clear reveal

### Character Sprites (10 PNGs)
- dr_vanek_bar.png - 64x96 - Taking notes
- dr_vanek_expressions.png - 64x96x3 - Clinical interest variants
- half_visible_patron.png - 64x96 - Translucent regular
- the_philosopher.png - 64x96 - Couchsurfing host
- mirror_chad_base.png - 64x96 - Player-mirrored hostile
- mirror_chad_speaking.png - 64x96x3 - Insult poses
- green_fairy_wisp_p1.png - 96x128 - Phase 1
- green_fairy_wisp_p2.png - 96x128x3 - Split phase
- green_fairy_wisp_p3.png - 128x160 - Final phase
- player_reflection_wrong.png - 64x96 - Moving independently

### Item/UI Sprites (12 PNGs)
- absinthe_lager_bottle.png - 32x64 - Signature brew
- absinthe_lager_glass.png - 32x48 - Served version
- cracked_mirror_shard.png - 24x24 - Mirror Chad drop
- green_fairy_essence.png - 24x32 - Boss consumable
- reality_anchor_badge.png - 48x48 - Achievement item
- vanek_survey_form.png - 32x48 - Research participation
- floating_chalice.png - 48x64 - Selfie prop
- stamp_absinthium.png - 64x64 - Brewery passport stamp
- stamp_absinthium_animation.png - 64x64x5 - Mist swirl sequence
- bottle_opener_absinthium.png - 48x48 - Cracked glass with fairy design
- bottle_opener_absinthium_shift.png - 48x48 - Color shift lenticular variant
- navigation_ui.png - 192x192 - Maze progress
- confusion_indicator.png - 64x64 - Status active

---

*The Absinthium Taproom: Brewery Tour Location 1 of 4 in Debaucheryville. Where the Green Fairy isn't a metaphor. Where your reflection has opinions about your life choices. Where Dr. Vaněk takes notes on your existential crisis and calls it "research." The lawsuits were greatly exaggerated. The disorientation is intentional. The stamp proves you saw yourself — and you're still here. Congratulations. The confusion means it's working.*
