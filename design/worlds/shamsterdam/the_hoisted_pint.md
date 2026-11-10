# The Hoisted Pint

*Leaning since 1689. Load-bearing since never.*

> **Doc status (2026-11-10).** Built from `design/templates/location_validation_template.md`.
> **APPROVED (author, Round v23, `docs/superpowers/NEXT_WORK.md`):** the name and the concept in
> "Approved Concept" below. **Everything else in this doc is `PROPOSED — NEEDS AUTHOR RULING`**:
> the location ID, the tour challenge, the beer, the opener, the stamp, the selfie, the brewmaster,
> the lawyer, every price and every line of dialogue not quoted in the approved concept. The
> "Author Rulings Needed" table at the bottom lists each one for a one-pass approval.

## Approved Concept (author canon — do not alter)

A brewery packed into a canal house one and a half metres wide and six storeys tall, leaning at
the same angle as its customers. The stairs are too narrow for a keg or a grown man, so both go up
the front of the building in a cargo net on the old gable hoist hook, while canal-boat tours below
take pictures. Lord Pilsner calls the net "VIP bottle service", Chadwick films the ascent as his
"Jackass tribute", Bradley rides it four more times because nobody asked him to pay for the first
one. The building next door is narrower, and the owner has a lawyer.

**Satire target:** leaning canal houses that break every fire code, sold as charm.

---

## Location Identity
- **Location ID**: `shamsterdam_canalring_hoisted_pint_01` — PROPOSED — NEEDS AUTHOR RULING
- **Display Name**: The Hoisted Pint
- **Satirical Subtitle**: "Leaning Since 1689. Load-Bearing Since Never." — PROPOSED — NEEDS AUTHOR RULING
- **World Location**: Shamsterdam
- **Area Zone**: Canal Ring Promenade (the leaning-canal-house district) — PROPOSED — NEEDS AUTHOR RULING
- **Location Type**: Brewery Tour Location #3 / Vertical Micro-Dungeon / Structural Concern

---

## Access & Requirements — PROPOSED — NEEDS AUTHOR RULING

### Entry Conditions
- **Time Restrictions**: 14:00 - 02:00. The hoist stops at 02:00 because the brewmaster's arms do.
  Getting down after 02:00 is the customer's business.
- **Stat Requirements**: None. The net takes anyone who fits. Everyone fits.
- **Item Requirements**: The Blarney Trap Bottle Opener (Publandia) — required for ANY brewery tour
  location (standing tour rule, `design/quests/general_quests/brewerytour.md`)
- **Previous Location Requirements**: None
- **Special Conditions**: The ground-floor door opens onto a staircase 41 cm wide. It is decorative.

### Exit Conditions
- **Normal Exit**: Down the front, in the net. There is no other way down.
- **Completion Requirements**: Complete "The Front Way Up" (below)
- **Failure States**: Party wipe in the net = lowered to the pavement, Hoist Fee charged again,
  30-minute lockout while the brewmaster "re-tensions the rope"
- **Progressive Unlocks**: Sixth-floor brewhouse access (only reachable through the window),
  brewmaster selfie, The Hoisted Pint Bottle Opener, Load-Bearing Tripel on the menu

---

## Visual Design — PROPOSED — NEEDS AUTHOR RULING

### Exterior Description
- **Approach**: Canal-side pavement between two bike racks. Look up. Keep looking up.
- **Structure**: A brick gable house 1.5 m wide and six storeys tall, built in 1689, leaning 7° out
  over the canal. The lean was deliberate in 1689 so hoisted cargo would clear the windows. It has
  been enthusiastic since.
- **Entrance**: A ground-floor door that opens onto the 41 cm staircase. Beside it, the real
  entrance: a cargo net lying on the pavement under a hook on a beam at the top of the gable.
- **Signage**:
  - Hand-painted board on the gable: "THE HOISTED PINT — BREWED SIX STOREYS UP — EST. 1689"
  - Brass plaque by the net: "HOIST FEE 5 SOVS PER LIFT. PAY THE HOOK."
  - Green FIRE EXIT sign on every floor, each arrow pointing out the window at the hook
  - Framed in the ground-floor window: the building's fire-safety certificate, dated 1689
- **Atmosphere**: Creaking rope, a winch ratchet six floors up, a canal-boat guide's PA drifting
  up from the water
- **Environmental Context**: Next door, a house 1.2 m wide. In its fifth-floor window, a man in a
  suit, at a desk, facing the street, taking notes.

### Interior Visuals — one room per floor, every room 1.5 m wide
- **Ground — The Hoist Desk**: a stool, a cash tin nobody watches, the net, a coil of spare rope
  labelled "SPARE ROPE (1974)"
- **First — The Mash Tun**: the tun is taller than the room and pokes up through a hole in the
  ceiling into the floor above. Visible through the window from the net.
- **Second — Fermentation**: three fermenters on wedges so they stand plumb in a building that
  doesn't. One is a bathtub.
- **Third — The Tap Room**: four bar stools in single file, front to back, like a bobsled team. The
  bar runs the length of the room. The person at the back pays for everyone because nobody can
  get past him.
- **Fourth — Bottling**: a capping machine bolted to the wall. The floor's only toilet is a bucket on
  a second, smaller hook. It goes down the front like everything else, past the tour boats, at
  boat-deck height. The boats photograph it too.
- **Fifth — The Office**: a desk facing the window, and directly across the gap, the lawyer's desk
  facing back. 212 letters in a stack. All of them came and went by hook.
- **Sixth — The Brewhouse and Winch**: the copper kettle, the brewmaster's bed, the hoist winch, and
  the building's one fire extinguisher, hoisted up in 1974 and never brought down
- **Atmospheric Effects**: everything inside hangs 7° off true. Pictures, lamps, the beer in the glass.
- **Hidden Areas**: on floor 4, a scratched tally on the window frame counting every customer who
  rode the net. Bradley's ride count is added to it during the quest.

### Technical Specifications
- **Color Palette**: Primary: Canal Brick (#8C3B2A), Accent: Hoist Rope (#C8A165), Background: Canal
  Green (#3E5B4A), Gable White (#F2EDE4)
- **Lighting Setup**: Late-afternoon sun raking down the facade; each window glows a different
  warmth; the sixth floor lit by the kettle burner
- **Particle Systems**: Rope fibre, brick dust when the net hits the wall, camera flashes from the
  boats, a geranium falling from a sill
- **Animation Elements**: Net sway (pendulum, amplitude driven by the balance minigame), winch
  rotation, tour boats passing on a loop, the lawyer's pen
- **Performance Optimization**: The facade is one tall scene; interiors are window cut-outs seen
  from the net, so only the sixth floor is a full room

---

## Satirical Design — PROPOSED — NEEDS AUTHOR RULING (the target itself is approved)

### Theme & Vibe
**Core Concept**: A building that breaks every fire code ever written and charges admission for
it. The staircase cannot carry a person, the fire exit is a hook, the extinguisher lives on the
only floor nobody can reach, and the whole thing leans over a canal at the angle of a man three
beers in. Every one of these facts is printed in the visitor leaflet as charm. The bros, who
arrived at the same angle, consider it the most relatable building in the city.

**The Irony**: The tour boats sell the leaning houses as a postcard. The Hoisted Pint sells the
postcard back to them, live, with three middle-aged men swinging in it.

### Cultural Targets
- **Primary Satirical Focus**: Leaning canal houses that break every fire code, sold as charm
- **Secondary Targets**: Canal-boat tourism that photographs the city instead of entering it;
  neighbour-versus-neighbour property law where the dispute is eleven centimetres of air
- **Cultural Specificity**: Narrow gable houses, front-wall hoist beams, the canal-boat tour circuit
- **Humor Approach**: Total sincerity. The brewmaster thinks the building is perfect. The lawyer
  thinks it's a crime. The bros think it's VIP.
- **Sensitivity Considerations**: Targets the "charm" sales pitch and tourist gawking. No real
  building, no real person.

### Seedy Underbelly Elements
- **Primary Vice**: Charging a Hoist Fee to ride the fire exit
- **City-Specific Comedy Operations**: The canal-boat companies time their loops to pass under the
  net. The brewery gets no cut. The brewery has never asked.
- **Buffoon Exploitation**: Three men who paid to be cargo
- **Comedy of Errors**: The net clears every window by the width of a beer belly, fully loaded
- **Consequence System**: Load-Bearing Tripel's "Listing" status (below)

### Buffoon Delusion Scenarios
**What bros THINK is happening**: VIP bottle service. A private lift to an exclusive top-floor
brewery, with an audience. Chadwick is shooting his Jackass tribute.

**What is ACTUALLY happening**: They are being winched up a fire hazard like a sofa, by one man, while forty
boat tourists photograph their undersides.

**How impaired are they**: Moderately on the way up. Comprehensively on the way down.

**Obvious signs they ignore**:
- The FIRE EXIT signs all point at the hook
- The net has a weight limit plate. The weight limit is "SOME"
- The hoist rope is the same rope as the "SPARE ROPE (1974)"
- The lawyer next door is writing down their names
- Every boat guide below says "and here we see, again, the tourists"

**How locals play along**: The boat guides narrate the bros as a landmark. The brewmaster waves
from the top like a ship's captain.

### Social Media Potential
- **Screenshot Opportunities**: The net halfway up with three bros and a keg; the bobsled tap room;
  the stamp landing crooked
- **Quotable Moments**: "VIP bottle service." / "If it fits, it lifts."
- **Easter Eggs**: Chadwick's ascent footage is titled with a real 2000s stunt-show reference
  (Jackass, per the approved concept); the tally on floor 4
- **Viral Content Hooks**: The boat tourists' photos of the bros appear in the Shamsterdam
  Memories album, taken from below, unflattering

---

## Gameplay Mechanics — PROPOSED — NEEDS AUTHOR RULING

### Brewery Tour Flow
1. **Order the special beer** at the Hoist Desk (Load-Bearing Tripel). It cannot be served on the
   ground floor. It is brewed on the sixth. This triggers the challenge.
2. **Pay the Hoist Fee** (5 SOVS per lift, into the cash tin nobody watches)
3. **The Front Way Up** (challenge, below)
4. **Sixth floor**: stamp, selfie, opener, beer unlocked
5. **The descent**: the net, again. Bradley takes it four more times.

### Tour Challenge: "The Front Way Up"
Micro-dungeon in the standard Debaucheryville shape (obstacle → mini-mob → boss), turned
vertical. The whole challenge happens in the net, on the outside of the building.

**1. Obstacle — The Lift (storeys 1-3).** Balance minigame. The net swings as the brewmaster cranks
from the top; the player shifts the three bros' weight to keep the swing in rhythm with the 7°
lean. Too far in: the net hits the facade (brick dust, a geranium drops on a tour boat, small HP
loss). Too far out: the net swings over the canal and the boat below cheers. A keg rides in the
net with them and counts as dead weight, nothing more.

**2. Mini-mob — Canal Boat Paparazzi (storey 3).** A tour boat stops dead beneath the net. Battle,
fought from inside the net.
- **Enemies**: 3-5 Canal Boat Paparazzi (boat tourists with phones on selfie sticks)
- **Attacks**: "Flash" (applies Bleary: −Accuracy), "Selfie Stick Poke" (low damage, pushes the net
  off-balance), "Zoom In" (applies Embarrassed to the bro whose underside is in frame)
- **Gimmick**: The boat drifts. Every two turns a fresh boat replaces it at full strength until the
  party wins a round fast enough to clear the boat before the next one arrives.

**3. Boss — Meester Overhang (storey 5).** The neighbour's lawyer, at his desk in the narrower
house's fifth-floor window, level with the net. He has filed 212 complaints that The Hoisted Pint
leans 11 cm into his client's airspace. The bros are now inside those 11 cm.
- **Boss ID**: `shamsterdam_boss_meester_overhang`
- **Attacks**:
  - "Airspace Violation" — damage scales with how far the net has swung toward his window
  - "Billable Hour" — removes 6 SOVS from the wallet each turn he isn't interrupted (refunded on victory)
  - "Notice of Default" — drains Bravado from the whole party
  - "Precedent of 1689" — AoE; reads aloud from a document older than the building
- **Weakness**: Swinging the net INTO his window. Each full swing is a hit; the bros enjoy every one.
- **Defeat**: The 11 cm becomes 1.5 m with three bros and a keg in it. He closes his shutters and
  files an appeal. The appeal is lowered past them on his own small hook.
- **Bros' combat lines (approved-concept lines in quotes are canon; the rest proposed)**:
  - **Lord Pilsner**: "VIP bottle service." / "Sir, we are the bottle."
  - **Chadwick**: his "Jackass tribute," narrated: "Jackass tribute, take one. No stunt double. No stairs. No permit."
  - **Bradley**: "Is he billing us? I haven't paid for anything yet."

**Completion**: The brewmaster drags the net in through the sixth-floor window. Rewards land at once
per the master spec: stamp, selfie, opener, Load-Bearing Tripel unlocked.

**Post-completion (approved-concept beat)**: Bradley rides the net down and back up four more
times. Nobody asked him to pay for the first one, so he doesn't pay for these. The Hoist Fee tin
stays empty. The floor-4 tally gains five marks.

### Consumable: Load-Bearing Tripel
**Type**: Alcoholic Beverage / Brewery Tour Signature Beer
- **Style**: Tripel, 9.5% ABV, fermented at 7° in a bathtub on the second floor
- **Price**: 9 SOVS (lowered to the pavement in a bucket after completion; send the money up first)
- **Brewed By**: The Hoisted Pint

| Effect | Value |
|--------|-------|
| HP Restore | +45 |
| Buff | "Load-Bearing" — +20% Defense for 3 turns |
| Drawback | "Listing" — stacks once per serving (see below) |
| Special | Can't be set down on a level surface. It slides to the low side. |

**Flavor Text**: "Fermented at the same angle as the building. Drinks at the same angle as you."

**"Listing" status (intoxication law 10-point review)**
1. **Source**: Load-Bearing Tripel
2. **Immediate effect**: The bro's sprite leans 7° per stack; −10% Evasion per stack
3. **Escalation**: At 3 stacks the bro tips over at the end of his turn and loses the next turn
4. **Player-facing cues**: Lean angle on the sprite; a small spirit-level icon whose bubble drifts
5. **Player control**: Overworld walking drifts toward the nearest canal edge while Listing
   (stops at the railing; never drops the party in the water)
6. **Duration/recovery**: 5 turns in battle; 60 seconds on the overworld; cleared by rest
7. **Comedic consequence**: The bros list in formation, all at the building's angle, and match it
8. **Status interactions**: Stacks with The Shakes and Bleary; counts toward Buzzed → Beer Goggles
   escalation once the alcohol tiers have numbers
9. **Technical dependencies**: Sprite rotation per character; overworld drift vector toward a
   tagged edge; a turn-skip hook in battle
10. **Further author approval**: Yes — the whole status is proposed

### Bottle Opener: The Hoisted Pint Bottle Opener
- **Design**: A brass gable hoist hook. The throat of the hook is the opener. A twist of tarred
  rope for the keychain loop.
- **Inscription**: "If It Fits, It Lifts."
- **Acquired**: Completing "The Front Way Up" only. Per the master spec, openers are earned, not
  bought, so it has no price.
- **Special Feature**: Hangs off the keychain at 7°. It will not hang straight.

### Passport Stamp
- **Design**: A leaning canal-house silhouette with a hook at the top. The page has a printed
  straight guide box; the stamp lands 7° off it, every time.
- **Ink**: Canal Green
- **Animation**: The stamp is lowered on a string from the sixth-floor window onto the open
  passport. Thud. The string goes back up.
- **Stamp speech** (the brewmaster, shouting down): "STAMPED! MIND THE HOOK!"

### Selfie Spot: The Gable Shot
(Pilsner's line "VIP bottle service" stays his line. It isn't used as the selfie's name because
"VIP bottle service" is already a Velvet Curtain Club bit in Debaucheryville.)
- **Staging**: The gable, after completion. The brewmaster leans out of the sixth-floor window with
  one hand on the winch. The bros hang in the net at window height. Lord Pilsner holds a lit
  bottle-service sparkler the brewmaster lowered to him on the bucket hook. A tour boat sits in the
  bottom of the frame with forty phones pointing up.
- **NPC reactions when shown the album**: Canal-boat guides anywhere in Shamsterdam: "You were on
  my tour." Club bouncers elsewhere: they wave the bros through as bottle-service regulars.

### Price List
| Item | Price |
|------|-------|
| Hoist Fee (per lift, up or down) | 5 SOVS |
| House Lager (tap room) | 4 SOVS |
| Load-Bearing Tripel | 9 SOVS |
| Net-Burn Balm (Hoist Desk) | 3 SOVS |

### Bravado Interactions
- **Gain**: A clean lift with no facade hits; beating Meester Overhang by swinging into his window;
  the sparkler selfie
- **Lose**: Hitting the facade three times; asking where the stairs are; paying the Hoist Fee in
  front of Bradley; on the descent with 2+ Listing stacks, Lord Pilsner's stomach gives out at the
  fourth storey and lands on the deck of a passing tour boat. The boat applauds. Pilsner bows from
  the net and calls it "the encore."

### Economic & Quest Integration
- **Shop Functionality**: Tap room (floor 3, post-completion), bucket service to the pavement
- **Currency Accepted**: SOVS, sent up first
- **Quest Hub Role**: Brewery Tour Location #3 of 4 for Shamsterdam; feeds the city's Legendary
  Hangover, "Canal Courage"
- **Objective Location**: Shamsterdam brewery tour (city quest file not yet written)

---

## NPCs — PROPOSED — NEEDS AUTHOR RULING (sketches only; no profile files yet)

### Brewmaster Thijs
- **Role**: Brewmaster, winch operator, the only person on the sixth floor
- **Appearance**: Huge, cheerful, flour-and-hop-dusted, braces, a red face permanently framed in a
  window 1.5 m wide
- **Background**: Walked up the 41 cm staircase in 1991 as a 58 kg apprentice. The beer turned out
  well. He has not fitted back down it since 1996 and has not been to street level since. Everything
  he needs comes up on the hook. He considers this the best decision he has ever made.
- **Personality**: Calls every defect charm. Speaks entirely in shouts down the facade.
- **Key Dialogue (proposed)**:
  - "WELCOME TO THE HOISTED PINT! STAIRS ARE DECORATIVE! GET IN THE NET!"
  - "FIRE CODE? The fire code is for buildings that stand up straight."
  - "IF IT FITS, IT LIFTS! You fit! Lovely!"
  - *to the lawyer, every day*: "GOOD MORNING, MEESTER! STILL LEANING!"
- **Selfie role**: Leaning out of the sixth-floor window, one hand on the winch

### Meester Overhang
- **Role**: Boss of the challenge. Lawyer for the owner of the narrower house next door.
- **Appearance**: Grey three-piece suit, desk lamp, fountain pen, a ruler marked to the millimetre
- **Personality**: He has billed the same eleven centimetres for thirty years and intends to bill
  them for thirty more
- **Key Dialogue (proposed)**: "You are trespassing in my client's air." / "Every swing is a separate
  incident." / "I will see you in court. I will see you in court from here, at this desk."

### Atmospheric NPCs
- **The Canal-Boat Guide**: PA microphone, narrates the bros as a landmark from the water
- **The Boat Tourists**: the Canal Boat Paparazzi out of combat; they applaud each lift

---

## Audio Design — PROPOSED — NEEDS AUTHOR RULING
- **Ambient Soundscape**: Rope creak, winch ratchet, canal water, boat PA, bike bells on the pavement
- **Music Style**: Accordion waltz that slows as the net climbs and speeds up on the way down
- **Interactive Audio**: Brick thud on facade hits, the bucket hook's squeak, the stamp's thud
- **Satirical Stingers**: A boat-horn toot every time the net clears a window
- **Character Voice Direction**: Thijs shouts everything; Overhang never raises his voice

---

## Connected Locations
- **Directly Adjacent**: Canal Ring Promenade; the narrower house next door (exterior only)
- **Quest-Connected**: The Wobbly Windmill Brewery, Bottoms Down, The Mad Monarch's Wit-tea Party
  (Shamsterdam brewery tour); The Blarney Trap (Publandia, tour access opener)

---

## Implementation Specifications — PROPOSED — NEEDS AUTHOR RULING

### Technical Requirements
- **Asset List**: Tall facade scene with six window cut-outs; sixth-floor room; cargo net (three
  bros + keg); tour boat loop; the narrower house and its fifth-floor window; Thijs; Meester
  Overhang; Canal Boat Paparazzi; stamp, opener and beer icons. PNG asset doc to follow on approval
  (`PNG_Assets/the_hoisted_pint_png_assets.md`).
- **Animation Requirements**: Net pendulum, winch, boat loop, sprite lean for Listing
- **Performance Budget**: 60 FPS, max 16 draw calls
- **Platform Considerations**: Desktop; accessibility toggle to reduce net sway and Listing tilt

### State Tracking
```
hoisted_pint_state:
  - challenge_completed: bool
  - facade_hits: int
  - overhang_defeated: bool
  - hoist_fee_paid_count: int
  - bradley_free_rides: int      # reaches 4 in the approved beat
  - opener_acquired: bool
  - stamp_acquired: bool
  - selfie_taken: bool
```

---

## Quality Assurance Checklist
- [x] No real city names in player-facing text
- [x] Prices in whole SOVS
- [x] Bros never afraid, disgusted, self-aware or scam-aware
- [x] No mascots (the keg is a keg)
- [x] Names grepped for uniqueness on 2026-11-10: Load-Bearing Tripel, If It Fits It Lifts,
      Meester Overhang, Canal Boat Paparazzi, Thijs, The Front Way Up, Listing
- [x] No crypto elements
- [ ] Author rulings on every PROPOSED item (table below)

## Author Rulings Needed
| # | Item | Proposal |
|---|------|----------|
| 1 | Location ID / zone | `shamsterdam_canalring_hoisted_pint_01`, Canal Ring Promenade |
| 2 | Tour challenge | "The Front Way Up": net balance lift → Canal Boat Paparazzi → boss Meester Overhang (the neighbour's lawyer) |
| 3 | Signature beer | Load-Bearing Tripel, 9.5%, 9 SOVS, +45 HP, +Defense, "Listing" drawback |
| 4 | Opener | Brass gable hoist hook, inscription "If It Fits, It Lifts.", earned only |
| 5 | Stamp | Leaning canal house struck 7° off the guide box, Canal Green ink, lowered on a string |
| 6 | Selfie | "The Gable Shot": bros in the net with a sparkler, Thijs at the window, tour boat below |
| 7 | Brewmaster | Thijs, who walked up as an apprentice in 1991 and hasn't fitted back down since 1996 |
| 8 | Prices | Hoist Fee 5, House Lager 4, Tripel 9, Net-Burn Balm 3 (SOVS) |
