# Jakub's Restroom Scene — Absinthe Arcade

**Status:** PROPOSED Scene Draft (Gemini)  
**Location:** Absinthe Arcade Restroom Screen (`aa_screen_restroom`)  
**Trigger:** First visit to the restroom after 01:00 (`debaucheryville_clocktower_arcade_01`)  
**Characters:** Lord Pilsner, Chadwick, Bradley, Jakub "Tokens" Dvořák (Token Attendant), Tomáš "Two-Fifty" (Voice over intercom)  
**Flags / State:** One-shot flag `jakub_restroom_discovered`.  

---

## Staging & Setup

The door pushes open with a groan. Under flickering cold fluorescent tubes and green Art Nouveau wall tiles, a tarnished bronze statue of the Green Fairy spreads her wings over the sinks. Originally sculpted to offer an opulent absinthe bowl to fin-de-siècle patrons, her outstretched bronze forearms have been repurposed: a industrial roll of 1-ply toilet paper hangs from her left wrist.

Cradled horizontally across her arms like an Art Nouveau pietà is Jakub "Tokens" Dvořák. He is wearing his red-and-white candy-striped work shirt, black apron pinned with thirty-seven pieces of mandatory corporate flair, and key lanyard. One non-slip work shoe is missing. An empty absinthe glass with a slotted spoon balanced across the rim sits on the toilet cistern. He is snoring softly, smelling intensely of wormwood and star anise.

---

## Scene Script

```dialogue
[SCENE START]

(The bros enter. Pilsner stops dead. Bradley squints at the statue's joints. Chadwick already has his phone out.)

LORD PILSNER
Behold, gentlemen. Old World romance. Last time a woman held me with that kind of devotion, my credit card company called to verify the zip code.

BRADLEY
Look at the core stability. Load-bearing bronze woman cradling a 160-pound lifer AND the two-ply. That’s pure ergonomic symmetry.

CHADWICK
Dude, it’s a Renaissance masterwork in an arcade crapper. The aesthetic is insane. I'm putting a sepia filter on this and tagging the Louvre.

LORD PILSNER
Give the working class their dignity, Chad. The man is on sabbatical. 

(Pilsner reaches past Jakub to pull off three squares of toilet paper. Jakub stirs, eyes cemented shut, a green-tinted drool bubble forming on his bottom lip.)

JAKUB
(Slurred, reflexively chipper)
...One SOV, one token... don't squeeze the wings, sir... she's a professional...

BRADLEY
(Taps Jakub’s shoulder)
Yo, chief. You got the master key for the air hockey table? Puck got jammed in some kid’s slushie.

JAKUB
(Eyes still shut, nuzzling into the bronze bosom)
...Always hit her on the left side... like people... left hip, orange spit... two tokens for the roll...

LORD PILSNER
See? True hospitality. He’s running the register in his subconscious. A born entrepreneur.

CHADWICK
Wait, ask him if he’s verified. If you die in a bronze fairy’s arms on the clock, do you get a blue checkmark?

JAKUB
(Suddenly snaps bolt upright, eyes still completely glued shut, customer-service voice ringing out at 100% projection)
WELCOME TO THE ABSINTHE ARCADE! TOKENS ARE ONE SOV! TOILET PAPER IS COMPLIMENTARY FOR THE FIRST WIPE!

(Jakub instantly collapses back limp across the bronze arms, snoring again.)

BRADLEY
That’s impressive respiratory recovery. 

(From his pinned apron, a piece of loose plastic flair pops off and clatters onto the wet linoleum near Bradley's sneaker.)

[INTERACTION / PICKUP]
Bradley scoops up the fallen pin.
Item Received: "ASK ME ABOUT TOKENS" Pin (Junk Item)
```

---

## Endings (Choose One)

### Ending A: The Intercom (FAVOURITE)
*Short, punchy, connects to Tomáš and arcade authority, leaves him right there.*

```dialogue
(The ceiling speaker crackles to life with harsh, dry feedback. Bartender Tomáš’s monotone drone echoes off the urinals.)

TOMÁŠ (V.O.)
(Over intercom)
Tokens. Toilet.

JAKUB
(In his sleep, smiling peacefully)
...Already here, boss... she loves me...

LORD PILSNER
(Solemn nod)
Leave the man to his bride. Come, boys. Glory awaits at the skee-ball.

(The bros exit. Jakub remains perfectly nested in bronze wings.)
[SCENE END]
```

### Ending B: The Tucking-In
*Pure bro rationalization; treating an employee passing out on toilet paper as a noble sacred duty.*

```dialogue
BRADLEY
He’s losing body heat. You sleep on metal without a thermal wrap, your lats lock up by dawn.

(Bradley takes three feet of rough industrial toilet paper off the Fairy's arm and neatly drapes it across Jakub’s chest like a dinner napkin.)

BRADLEY
Hydrate and elevate, king. 

LORD PILSNER
Gentlemen, tiptoe. We are in the presence of greatness.

(The bros quietly back out of the restroom.)
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

## Continuity & Implementation Notes
- **One-Shot Flag:** `jakub_restroom_discovered = true`.
- **Reader Hook:** If player visits Tomáš at the bar after this scene, Tomáš does not care, but if spoken to Jakub at the token booth on subsequent nights, Jakub denies ever having been horizontal.
- **Tone Check:** Zero moralizing, zero disgust. Bros treat him with awe and envy.
