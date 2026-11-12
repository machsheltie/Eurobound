# PROPOSAL — author to kill/swap; not canon

## The Golden Cutlet: 8-enemy roster + The Schnitzel King fight (draft)

> **Status.** Agent draft for bead Eurobound-p1y, written 2026-11-12 because the author asked
> (Production Desk `Eurobound-p1y-q1`, verbatim): *"Have an agent draft a fresh 8-enemy roster plus
> the King's fight for me to kill/swap"*. **Nothing here is canon until the author rules.** Every
> enemy can be killed, swapped for one from the Swap Bench, or renamed.
>
> **No numbers.** HP, damage, turn counts, drop rates and SOVS amounts are left to the balancing
> pass. Where a gimmick needs a number, it says so in words.
>
> **Canon this draft must not break** (from `the_schnitzel_king.md` and `NEXT_WORK.md:28`): The
> Golden Cutlet is a massive, tacky, multi-level "authenticity" tourist-trap tavern
> (Medieval-Times-meets-beer-hall), with fake medieval armor, aggressive tourist exploitation, forced
> audience participation and trap doors. The bros hold a group-bought **VIP Cultural Heritage Pass**
> (Chadwick's idea) that promises **Free Unlimited Beer & Traditional Feasting**; its fine print
> binds them to the **Heritage Trial** in the basement vaults before a drop is poured. The vaults
> hold real battles. When the bros try to back out and demand their drinks, **the King enforces the
> contract**. His costume is absurdly expensive and **genuinely authentic**, the one real thing in
> the building, and he takes living history far too seriously. The Holographic Charizard QR is in
> the Pass's fine print, so it is not a drop from any fight here.
>
> **Naming.** All eleven names (eight plus the Swap Bench) were checked against the repo
> (`grep -ri` over `design/`, `docs/`, `game/assets/data/`) and the canon index (keyword mode). No
> exact matches. Names I dropped because they were too close to existing canon: "Crowd-Work Crier"
> (Publandia's *The Crier*), "Crowd-Work Herald" (Sinfonia's Herald, Herr Ankündiger), "Complimentary
> Brigade" (Publandia's *Morning Shame Brigade*), anything with "Overhang" (Shamsterdam's *Meester
> Overhang*), and "Jester" (Publandia).
>
> **Player-facing text** uses "the Heritage Trial" only. The author's dictated "Traditional
> Austrian Heritage Trial" stays internal (real place name); the in-game name is still open in the
> King's profile.

---

## How each enemy maps onto `enemy_template.md`

Every enemy below would become one doc in `design/worlds/sinfonia/enemies/` (PROPOSED folder, per
the template) and fill these fields from this draft:

| Template section | Filled from this draft | Left for later |
|---|---|---|
| 📋 Enemy Identity | Display Name, Enemy ID, City (Sinfonia), Zone (The Golden Cutlet, Heritage Vaults), Encounter Family ("Heritage Vault Staff", PROPOSED), Group Size (in words) | Which vault: open (dungeon layout is the author's) |
| 🎭 Core Concept | What It Actually Is, What The Bros Think It Is, The Comedy Gap | — |
| ⚔️ Moves | Move names, Type, Effect in words, Status Inflicted (master list only) | Weights |
| ⚔️ Weaknesses & Resistances | In words | Percentages |
| ⚔️ Intoxication Hook | On-The-House Wenches only (10-point review outline below) | Thresholds |
| 💬 Battle Text | `battle_intro`, on-defeat line, bro reaction | — |
| 💰 Rewards & Drops | Junk-drop idea (each would need its own item doc and author ruling) | XP, SOVS, drop chance |
| 🎨 Sprite Notes | Battle sprite idea, text markings | Size, palette, filename |
| ⚙️ Engine Entry | Enemy ID, `display_name`, `battle_intro` | All stats; new schema fields (moves, gimmicks) are proposed engineering work |

Statuses used are all from `design/mechanics/Battle/status_effects.md`: Grease Fingers, Embarrassed,
Tourist Trap Victim, Broke AF, Liquid Confidence, Sloppy, Food Poisoning. Anything that is not a
master-list status is described as a gimmick, and is marked **PROPOSED mechanic**.

---

## The roster

### 1. The Triple-Dredged Knight
- **Concept:** a server in vacuum-formed plastic armor that has been floured, egg-washed and
  breadcrumbed, because the menu says everything here is "hand-breaded to order", the staff included.
- **Satirical target:** dinner-theater fake chivalry, and the "hand-made" upcharge on deep-fried
  plastic.
- **Bros think:** he's a real knight. Lord Pilsner wants to be knighted by him.
- **Gimmick (PROPOSED mechanic):** he fights in three coats that come off in order: flour, then egg,
  then crumb. Each coat shrugs off a different kind of attack, so the party has to switch it up as
  the layers come off. Whoever lands a hit on the egg coat gets **Grease Fingers**. Strip all three
  and he's a sweaty man in a plastic breastplate with almost no defense.
- **Template fields:** Identity; Core Concept; Moves (*Crumb Shed*, *Egg Wash*, *Shield of Panko*);
  Weaknesses (shifts per coat); Battle Text; junk drop *Loose Breastplate Crumbs*; Sprite (three
  coat states, one palette swap per coat).
- **Flavor:**
  - `battle_intro`: "A Triple-Dredged Knight clanks forward, shedding crumbs like a dandruff commercial."
  - On defeat: "The Triple-Dredged Knight is down to the plastic. He still has four tables."
  - **Lord Pilsner:** "Kneel me. I mean knight me. Do the sword thing."

### 2. Tableside Thumper
- **Concept:** the man who pounds the schnitzel flat at your table with a mallet, for the
  "experience". The experience is on the bill. Now he's pounding the bros.
- **Satirical target:** performative craftsmanship, the "tableside" surcharge, food as theater.
- **Bros think:** it's a show, and they're the VIP table.
- **Gimmick (PROPOSED mechanic):** a wind-up hitter. He raises the mallet and shouts the count, and
  the audience claps along. Each pound he lands makes the next one louder and harder. If the party
  hits him while the mallet is up, the count resets and he loses the turn. A pound that lands while
  the crowd is cheering inflicts **Embarrassed**.
- **Template fields:** Identity; Core Concept; Moves (*Hand-Pounded*, *Crowd Count-In*, *Surcharge*);
  Weakness (interrupt on wind-up); Battle Text; Sprite (mallet-up telegraph pose, the overworld
  tell); junk drop *Splintered Mallet Head*.
- **Flavor:**
  - `battle_intro`: "Tableside Thumper raises the mallet and asks if anybody's celebrating a birthday."
  - Bark: "HAND-POUNDED! THAT'S A SURCHARGE! HAND-POUNDED!"
  - **Chadwick:** "Get my food in the shot. Get me in the shot. Hit me again, I wasn't filming."

### 3. The Living Asterisk
- **Concept:** a clerk in a tabard printed top to bottom with the VIP Cultural Heritage Pass's fine
  print, in a font nobody has read since the dot-matrix days. He is the terms and conditions, walking.
- **Satirical target:** fine print, VIP packages, "unlimited" offers, click-to-agree contracts.
- **Bros think:** he's the guy who brings the free beer.
- **Gimmick (PROPOSED mechanic):** each turn he reads a new clause aloud, and that clause becomes a
  battle rule until he's beaten. The rules stack. Examples: items cost SOVS to use; whoever bought
  the Pass (Chadwick) can't act on the clause's turn; healing is "a premium add-on". Beating him
  clears every clause at once. Inspecting him shows the clause text.
- **Template fields:** Identity; Core Concept; Moves (*Read Aloud*, *Binding Signature*, *See
  Appendix*); Battle Text (one line per clause); status **Tourist Trap Victim** from *See Appendix*;
  Sprite (text markings: the tabard print, legible on inspect, every word proofread); junk drop
  *Page Two of the Pass*.
- **Flavor (clauses as read):**
  - "'Unlimited' refers to the duration of your obligation, not to the beer."
  - "Traditional Feasting is portioned in accordance with tradition. The tradition was a famine."
  - "By breathing in the Heritage Vaults you consent to be photographed, sung at, and invoiced."
  - **Chadwick:** "I read the whole thing, bro. The top part. Where it says free."

### 4. Voluntold Wrangler
- **Concept:** a Master of Revels in velvet with a long shepherd's hook, whose whole job is
  dragging "volunteers" out of the audience and onstage for the bit.
- **Satirical target:** forced audience participation (canon), the dinner show that makes the
  customer the entertainment.
- **Bros think:** they've been discovered. Finally.
- **Gimmick (PROPOSED mechanic):** he hooks one bro out of the party and onto a little stage, where
  the bro does something "traditional" in a cardboard crown (leads a sing-along, gets pelted with
  bread rolls). The hooked bro loves it and won't come down, so he can't act until the Wrangler is
  beaten or another bro spends a turn booing him off. When he comes down he has **Embarrassed**,
  which he takes as a standing ovation.
- **Template fields:** Identity; Core Concept; Moves (*The Hook*, *Give It Up For*, *Encore*);
  Weakness (beat him and the hooked bro returns at once); Battle Text; Sprite (hook pose plus a
  stage-and-crown overlay for whichever bro is hooked).
- **Flavor:**
  - `battle_intro`: "Voluntold Wrangler scans the room for the man most likely to say yes."
  - **Lord Pilsner (hooked):** "They picked me. Out of everybody. Get the crown on straight, this is going on the Christmas card."
  - **Bradley:** "Can I get picked? Pick me. I'm married, I never get picked."

### 5. Flash Pillory
- **Concept:** a "court photographer" in a ruff who claps tourists into a portable wooden pillory,
  takes their picture, and sells it back to them in a cardboard frame. The photo is free. The frame
  is mandatory.
- **Satirical target:** the souvenir photo upsell at every tourist attraction on earth.
- **Bros think:** it's a photo op. They pose.
- **Gimmick (PROPOSED mechanic):** he locks one bro in the stocks (that bro can use only Social
  moves), and every flash lowers the party's accuracy. Every photo he takes goes on a bill the bros
  pay after the battle unless they buy the prints back; the longer the fight, the bigger the bill.
  His *Proof Sheet* inflicts **Tourist Trap Victim**.
- **Template fields:** Identity; Core Concept; Moves (*Say Schnitzel*, *Lock and Pose*, *Proof
  Sheet*); "Other" reward row for the post-battle print bill (PROPOSED field); Battle Text; Sprite
  (text markings: the frame reads "MY HERITAGE TRIAL" in gold foil); junk drop *Souvenir Frame (Empty)*.
- **Flavor:**
  - `battle_intro`: "Flash Pillory says the photo is free and the frame is not optional."
  - **Lord Pilsner (in the stocks):** "Is this the VIP section?"
  - **Bradley:** "Dear's gonna love this one."
  - On defeat: "Flash Pillory goes down. The camera keeps shooting. Every shot is of the ceiling. You are invoiced for them."

### 6. On-The-House Wenches
- **Concept:** a pack of servers in polyester bodices pushing plastic goblets of "complimentary"
  honey mead that tastes like Robitussin strained through a Renaissance Faire. It's on the house until the bill comes.
- **Satirical target:** the "complimentary" drink that turns up on the tab, and bottomless drinks
  as a business model.
- **Bros think:** free drinks. That's what the Pass promised. It's working.
- **Gimmick (PROPOSED mechanic, intoxication):** they don't fight the bros, they pour for them. The
  bros never refuse a goblet, so every pour pushes a bro up the alcohol escalation: **Buzzed**
  (Liquid Confidence: braver, sloppier) and then **Beer Goggles** (the bro tries to buy the Wenches
  a drink instead of hitting them, and hits his own friends). Nothing is charged after this fight:
  every goblet is chalked on a slate behind the bar, and the slate comes back at the King's defeat
  (see payoff option (b)), so the post-battle bill stays Flash Pillory's gimmick alone. They chant Chumbawamba's "Tubthumping" with every drink in the chorus swapped for mead.
- **Template fields:** Identity; Group Size (a small pack, size to the balancing pass); Core Concept;
  Moves (*Top You Up*, *It's Complimentary*, *Last Orders*); **Intoxication Hook** (see review below);
  status **Sloppy** from *Last Orders*; Battle Text;
  Sprite (goblet-raise pose); junk drop *Plastic Goblet, Sticky*.
- **Flavor:**
  - `battle_intro`: "The On-The-House Wenches are on the house. The mead is not."
  - Battle log: "Bradley accepts the goblet. Bradley accepts the next goblet. Nobody is offering anymore; Bradley is just taking."
  - **Chadwick (Beer Goggles):** "Ladies. Ladies. You wanna see the VIP part of my Pass?"
- **Intoxication law §8 review (concept only; thresholds to the balancing pass):**
  1. Source: the Wenches' "complimentary" mead (an enemy action, not an item).
  2. Immediate effect: one step up the alcohol escalation per goblet.
  3. Escalation: Buzzed, then Beer Goggles; capped at Beer Goggles inside this fight (PROPOSED; Shitfaced and Catastrophe stay with the player's own drinking).
  4. Cues: goblet animation, the bro's sprite flushes, the tier label on his status bar.
  5. Control: at Beer Goggles, a chance his action targets an ally or turns into flirting (the canon Beer Goggles −Accuracy / +Friendly Fire).
  6. Duration and recovery: wears off after battle in the normal way; no lasting control loss.
  7. Comedy: the bros think they're finally getting the Pass's free beer; every goblet is chalked on the slate that comes due when the King falls.
  8. Interactions: stacks with Liquid Confidence and Sloppy; does not trigger Blackout Drunk inside this fight (PROPOSED).
  9. Tech: needs a per-character intoxication tier and an enemy-driven "pour" action (proposed engineering work).
  10. Author approval: needed for the cap, the slate (tab) payoff, and the mechanic itself.

### 7. Method Peasant
- **Concept:** a living-history interpreter in burlap who will not break character, ever, under any
  circumstances, including a fistfight. He has not acknowledged electricity since his shift started.
- **Satirical target:** the "living history" upsell (canon), method acting, authenticity cosplay as
  a service job.
- **Bros think:** he's the busboy. They try to tip him in Pogs.
- **Gimmick (PROPOSED mechanic):** anything invented after his "period" doesn't register. Tech items
  (the Razr, the Game Boy, ICQ) fail against him, and Social moves built on pop culture bounce off
  (he doesn't know what a Backstreet Boy is, and won't). Plain physical hits, thrown food and Lord
  Pilsner's stein work fine. Each time a tech item fails he takes it and bites it.
- **Template fields:** Identity; Core Concept; Moves (*Toil*, *Bite the Cursed Sliver*, *Plague
  Cough*); Immune to tech items and pop-culture Social moves; *Plague Cough* inflicts **Food
  Poisoning**; Battle Text; Sprite; junk drop *Turnip, Bitten*.
- **Flavor:**
  - `battle_intro`: "Method Peasant curses your shoes and asks what year it is, already knowing."
  - Bark (on a tech item): "A cursed sliver! It glows with the devil's ringtone!"
  - On defeat: "Method Peasant dies of plague, as is period-accurate, and clocks out."
  - **Chadwick:** "Bro, he doesn't know what a flip phone is. Show him the camera. Show him the camera, bro."

### 8. Total Plate Eclipse
- **Concept:** a schnitzel pounded so wide it eclipses its plate, its table and most of the room's
  light. It is the house special. It is hostile.
- **Satirical target:** size as authenticity, the hubcap-sized "traditional" portion made for photos,
  food as a tourist dare.
- **Bros think:** lunch. Lord Pilsner has called dibs.
- **Gimmick (PROPOSED mechanic):** while it's up, it hangs over its allies, so hits aimed at the
  other enemies hit the schnitzel instead. It also blocks the light, which lowers the party's
  accuracy. Each hit trims it from the edge, and once it's trimmed enough the allies underneath can be
  targeted again. A bro can spend a turn eating some of it: he heals a little and gets **Grease
  Fingers**, and it shrinks.
- **Template fields:** Identity; Core Concept; Moves (*Eclipse*, *Lemon Wedge to the Eye*, *Grease
  Rain*); Weakness (it shrinks as it's trimmed or eaten); Battle Text; Sprite (sizes per trim
  stage); junk drop *Lemon Wedge, Used*.
- **Flavor:**
  - `battle_intro`: "Turn around. It's still there." (a nod to Bonnie Tyler's "Total Eclipse of the Heart"; two words, not a lyric quote)
  - **Lord Pilsner:** "Dibs. I said dibs in the car."

---

## Swap Bench (alternates the author can swap in)

| Name | One-line concept | Target | Gimmick in plain words |
|---|---|---|---|
| **Authentic Reproduction** | A decorative suit of armor (sticker: "GENUINE ANTIQUE, EST. 2019") with a gap-year backpacker inside working for tips. | Mass-made "antique" decor | Physical hits just ring it like a bell. Social moves talk the backpacker into quitting; he climbs out and leaves, and the empty armor falls over. |
| **Gratuity Included** | A waiter who adds a service charge every turn, then a service charge on the service charge. | Mandatory tipping, compounding fees | His hits get stronger every turn he's alive; beating him early is the whole fight. |
| **Five-Star Shakedown** | A shift manager with a tablet who demands a TripAdvisor review mid-fight. | Review farming and review extortion | The bros happily give him five stars, and every five-star review heals him. A one-star review (a Social move) staggers him. |

---

## The Schnitzel King fight (PROPOSAL)

Consistent with every canon field in `the_schnitzel_king.md`: he is the minor boss, the fight is in
the basement vaults, it starts when the bros try to back out and demand their drinks, he enforces the
contract, and his genuinely authentic, absurdly expensive costume is the one real thing in the
building. Phase triggers are described in words; thresholds go to the balancing pass.

### Pre-fight (canon trigger)
The bros stop at a vault door, wave the Pass and demand the Free Unlimited Beer. The King steps out
of the dark in full brocade and ermine.
- **King (PROPOSED line):** "The Pass is binding in this century and in the six before it. You will
  feast. You will be tried. You will receive no beer before the Trial is complete. Clause nine."
- **Chadwick:** "It says unlimited, dude. Unlimited is, like, the most."

### Phase 1: "Traditional Feasting, As Promised"
- **Concept:** the Pass promised Traditional Feasting, so he delivers it by force. He serves course
  after course at the bros, thrown, flung or slammed down in front of them.
- **Gimmick (PROPOSED mechanic):** his *Course* attacks do damage and inflict **Grease Fingers**. The
  bros love the food. By the end of the phase the whole party is greasy, which looks like pure
  penalty (no tech items) and isn't (see Phase 3).
- **Add (PROPOSED):** the Voluntold Wrangler joins and hooks a bro onstage "for the toast".
- **Bark:** "Eat. The Pass says feasting. The Pass does not say chewing."

### Phase 2: "The Trial Clause"
- **Trigger (in words):** once the King is hurt enough to stop serving.
- **Concept:** he invokes the Heritage Trial proper and starts pulling levers (canon: trap doors).
- **Gimmick (PROPOSED mechanic):** *Trap Door Ruling.* A trap door drops one bro into the vault below,
  out of the fight until he climbs back up on his own. He comes back unbothered, pleased, holding
  something from the floor down there that earlier Pass-holders left behind: a junk item with inspect
  microcopy (each would need its own item doc and an author ruling). Ideas: a VIP lanyard from a
  bachelor party that never came back up, half a pair of lederhosen, a disposable camera with one
  shot left and every other shot of the same groom asleep in a pillory.
- **Add (PROPOSED):** On-The-House Wenches pour for whoever is still standing.
- **Bro (back from the trap door), Bradley:** "There's a whole other bar down there. It's closed. I found this."

### Phase 3: "The Costume Is Real"
- **Trigger (in words):** once he's badly hurt.
- **Concept:** he stops protecting himself and starts protecting the costume. He would rather die
  than let a tourist stain the brocade.
- **Gimmick (PROPOSED mechanic):** every hit from a bro with **Grease Fingers** leaves a stain on the
  costume, and each stain makes the King spend his next turn dabbing it with a napkin and club soda,
  open to everything. Phase 1's grease is now the party's best weapon. The bros don't know why it's
  working; the player does. Grease-free bros can still fight him, just the long way.
- **Barks (PROPOSED):**
  - "That ermine is older than your entire country's opinion of itself."
  - "Do NOT touch the brocade. The brocade outlived three wars and a cruise ship tour group."
  - On a stain: "Club soda. CLUB SODA."

### Defeat (template rule: he loses the fight, never the ego)
- **King (PROPOSED line):** "The Trial... is complete. The Pass is honoured. Your beer. Do not set it
  on the brocade."
- **Open question for the author (not decided here):** what the Free Unlimited Beer turns out to be.
  Options for the author: (a) one "heritage measure" the size of a thimble, refilled without limit;
  (b) a real pour, served with the Wenches' slate: every "complimentary" goblet from the whole dungeon, itemised; (c) the tap is
  "traditional" and doesn't work; (d) the author's own call.
- The Holographic Charizard QR stays on the Pass (canon). It is not a drop from this fight.

### What the King's profile would gain if this is approved
Encounter Type, Phases, Move List names (*Course*, *Trap Door Ruling*, *Guard the Brocade*), Adds,
Arena & Gimmick, Vulnerability window (the stain-dabbing turns), Weak against (Grease Fingers hits),
pre-, mid- and post-battle lines. Stats, rewards and the trigger thresholds stay **OPEN QUESTION
(author)** until the balancing pass.

---

## What the author is being asked
For each of the eight, and for the King's fight: **keep, kill, or swap** (for a Swap Bench entry or
an idea of the author's). Also: the defeat payoff (a/b/c/d above), whether the King takes adds, and
whether the Wenches' intoxication mechanic is approved.

---

## Critic pass (eurobound-adversarial-critic, 2026-11-12)
Fixed before posting: a Lord Pilsner line that leaned on his secret living-with-mom canon (removed;
that reveal is the Mom-call's job); a soft mead description (sharpened); a "homeless guy" read on
Method Peasant that punched at the wrong target (now the bros mistake him for the busboy); a tame
Beer Goggles line (sharpened); two enemies both charging a post-battle bill (the Wenches' tab now
pays off once, at the King's defeat). Checked clean: no real place names in player-facing text,
no narrator or moral framing, bros never afraid, disgusted, clever or self-aware, statuses from the
master list only, no numbers.
