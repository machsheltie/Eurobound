# Jakub's Restroom Scene — Absinthe Arcade (v2)

**Status:** PROPOSED Scene Draft v2 (Gemini)  
**Location:** Absinthe Arcade Restroom Screen (`aa_screen_restroom`)  
**Trigger:** First visit to the restroom after 01:00 (`debaucheryville_clocktower_arcade_01`)  
**Characters:** Lord Pilsner, Chadwick, Bradley, Jakub "Tokens" Dvořák (Token Attendant), Tomáš "Two-Fifty" (Voice over intercom)  
**Flags / State:** One-shot flag `jakub_restroom_discovered`.  

---

## Staging & Setup

The door pushes open with a groan. Under flickering cold fluorescent tubes and green Art Nouveau wall tiles, a tarnished bronze statue of the Green Fairy spreads her wings over the sinks. Both of her outstretched bronze forearms hold jumbo rolls of industrial 1-ply toilet paper.

Cradled horizontally across her arms is Jakub "Tokens" Dvořák. He is wearing his red-and-white candy-striped work shirt, black apron pinned with mandatory corporate flair, and key lanyard. One shoe is missing. An empty absinthe glass with a slotted spoon sits on the toilet cistern. He is snoring softly, reeking of wormwood and black licorice.

---

## Scene Script

```dialogue
[SCENE START]

(The bros stumble in. Pilsner stops dead with genuine respect. Bradley pokes the bronze wing. Chadwick whips out his phone.)

LORD PILSNER
Look at that. High class. In America you pass out in a stall and someone steals your shoes. Over here, the decor cradles you.

BRADLEY
That statue's got insane traps. Look at her lats. Holding up a whole dude and two rolls of paper without spotting. Respect.

CHADWICK
Dude, this goes so hard. I’m filming this right now. If I put techno over this, we hit ten thousand views by morning.

LORD PILSNER
Shh. Don't crowd him. He's doing European union business. 

(Pilsner goes to yank a strip of toilet paper off the statue's right wrist. Jakub stirs, eyes cemented shut, a green-tinted drool bubble forming on his lip.)

JAKUB
(Slurred, reflexively chipper)
...One SOV, one token... don't squeeze the wings, sir... she's a professional...

BRADLEY
(Pokes Jakub’s ribs)
Hey bro. Skee-ball machine ate my coin and spit out an old peanut. Hit the lever for me.

JAKUB
(Eyes still shut, nuzzling into the bronze chest)
...Always hit her on the left side... like people... left hip, orange spit... two tokens for the roll...

LORD PILSNER
Genius. The guy runs customer service while he's unconscious. That’s work ethic.

CHADWICK
Dude, ask him if he wants to be in my video. Bro, thumbs up for the camera!

JAKUB
(Snaps bolt upright, eyes still completely glued shut, customer-service voice blaring at top volume)
WELCOME TO THE ABSINTHE ARCADE! TOKENS ARE ONE SOV! TOILET PAPER IS COMPLIMENTARY FOR THE FIRST WIPE!

(Jakub instantly goes limp and crashes back across the bronze arms, snoring again.)

BRADLEY
Nice pipes. Solid diaphragm projection.

(A plastic pin pops off Jakub's apron and clicks onto the floor by Bradley's sneaker.)

[INTERACTION / PICKUP]
Bradley grabs the pin off the wet tile.
Item Received: "ASK ME ABOUT TOKENS" Pin (Junk Item)

(The ceiling speaker pops and crackles with dry feedback. Bartender Tomáš’s monotone drone buzzes out of the grill.)

TOMÁŠ (V.O.)
(Over intercom)
Tokens. Toilet.

JAKUB
(In his sleep, smiling)
...Already here, boss... she loves me...

LORD PILSNER
Man's living the dream. Let's go win some plastic crap.

(The bros stumble back out toward the arcade floor. Jakub remains asleep in the Fairy's arms.)
[SCENE END]
```

---

## Rewards & Microcopy

### Item: "ASK ME ABOUT TOKENS" Pin
- **Item ID:** `jakub_tokens_flair_pin`
- **Item Type:** Junk Item (Held in Inventory / Valueless)
- **Purchase / Sale Price:** 0 SOVS (Unsellable garbage)
- **Inspect Line (MA Dark Satire rule):**
  > *"A dented tin badge crusty with dried anise and teenage acne sebum. Pinned onto twenty-three shirts before this one; fourteen of those guys died of liver failure behind the DDR cabinet."* (30 words)

---

## Continuity & Verification
- **Word / Line Count:** ~25 dialogue lines. Fast, punchy, lands and leaves.
- **Tone Check:** Bros are pure, earnest, un-self-aware doofuses. No clever metaphors, no zip codes, no art-history references, no fake sophistication. They admire Jakub, misunderstand European hospitality, obsess over traps/muscles and techno view counts.
- **Canon Fixes:** Toilet paper rolls on both arms; skee-ball machine instead of air hockey; no real-world city/place names.
