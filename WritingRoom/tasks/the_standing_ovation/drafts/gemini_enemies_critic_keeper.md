<!-- Moderator note: copied verbatim from Gemini's Round 4 thread post (thread.md, 2026-11-09 14:47). Gemini hit its tool-step cap before saving; the text is Gemini's, unedited. -->

### 3. Enemy Design: Axed Critic & Keeper of the Rope (f3 & f4 Mandate)

Here are the complete designs for my two assigned enemies, mapping both to the current engine schema and the proposed full design.

```
================================================================================
ENEMY 1: THE AXED CRITIC (Common / Period-Reference Slot)
================================================================================
Location: Opera House Plaza / Alley beside The Standing Ovation (Exterior)
Silhouette: Shabby tweed overcoat, ink-stained fingers, cracked bifocals on a chain, clutching a 2001 issue of 'Sinfonia Arts Weekly' like a riot shield.

[CURRENT ENGINE DATA CANDIDATE]
ID: sinfonia_enemy_axed_critic_01
display_name: "Axed Critic"
max_hp: 42
offense: 9
defense: 4
speed: 7
luck: 3
gold_reward: 6
xp_reward: 16
item_drop: "shredded_broadsheet"
drop_chance: 1.0
battle_intro: "An Axed Critic intercepts you with an unprompted retrospective!"

[PROPOSED FULL COMBAT DESIGN]
Satirical Premise:
A bitter print journalist fired during the 2002 dot-com advertising collapse who still roasts modern street life using late-90s/early-2000s entertainment column clichés. To him, the bros aren't tourists; they are a walking, derivative boy-band reunion that deserves a career-ending zero-star pan.

Combat Roles & Mechanics:
- Role: Fast, verbal debuffer / morale sapper. Inflicts Embarrassed and Existential Crisis.
- Action 1: "Pan the Production" (Single Target). The Critic bellows a syndicated takedown: *"Derivative styling, unearned swagger, zero third-act development!"* Deals 12 Ego Damage and inflicts Embarrassed (3 turns).
- Action 2: "2001 Retrospective" (AoE taunt). *"You look like the clearance rack of an untelevised VMAs pre-show!"* Calls out frosted tips and cargo pockets. Inflicts Existential Crisis (-15% Offense, bros question their cultural relevance for 2 turns).
- Action 3: "Ink-Stained Slander" (Physical). Swipes violently with a fountain pen that leaks indelible black gall-nut ink. Deals 8 physical damage, 30% chance to inflict Blindness/Grease Fingers.

Counterplay & Exploits:
- Counterplay (Roast Line / Bradley): Bradley's genuine athletic analysis confuses him. If Bradley uses Roast Line or comments on the critic's slouch/core weakness, the Critic takes 1.5x Ego Damage (*"Don't critique my posture, you illiterate fullback!"*).
- Mechanical Quirk: If `footage_release_planned` is true in the district, the Critic immediately shifts priority to Chadwick: *"I heard rumors of unedited tape! Give me the syndication rights!"* He becomes Eager to Print (drops defense by 50% seeking an exclusive quote).

================================================================================
ENEMY 2: THE KEEPER OF THE ROPE (Rare / Spatial Observation Slot - Rebuilt per f4)
================================================================================
Location: Venue Foyer / VIP Annex Threshold
Silhouette: Imposing, rigid bouncer in an ill-fitting tuxedo with a brass clip, standing with absolute territorial majesty behind a frayed 4-foot velvet rope suspended between two wobbly brass stanchions.

[CURRENT ENGINE DATA CANDIDATE]
ID: sinfonia_enemy_keeper_of_the_rope_01
display_name: "Keeper of the Rope"
max_hp: 68
offense: 12
defense: 10
speed: 4
luck: 1
gold_reward: 15
xp_reward: 35
item_drop: "decorative_brass_stanchion_clip"
drop_chance: 1.0
battle_intro: "The Keeper of the Rope bars an imaginary VIP boundary!"

[PROPOSED FULL COMBAT DESIGN]
Satirical Premise:
A security guard whose entire personal identity and divine authority rest on a four-foot decorative velvet rope that isn't connected to any wall. The entrance is completely open on both sides; anyone can simply walk around him. But if a bro touches the rope, questions his boundary, or tries to push through, he treats it as a Category 5 diplomatic violation.

Two-Layer System (Per Editor Ruling f4):

Layer 1: Environmental / Non-Combat Bypass
- Observant players see the stanchions sit in the middle of a wide hallway with 10 feet of clear walking space on either side.
- Examine Text: *"A majestic velvet rope guarding three square feet of polished linoleum. You could easily walk three paces to the left."*
- If the player simply walks around the stanchion perimeter, the Keeper glares silently, adjusting his cuffs, and combat NEVER triggers. Zero cost, zero damage.

Layer 2: Interactive Combat Layer (If Rope is Touched / Boundary Challenged)
- The Keeper does not merely stand there; he treats imaginary club protocol as battlefield geometry!
- Trait: "Arbitrary Perimeter" (Passive). At the start of combat, the Keeper plants his rope across the front row. Attackers behind the rope suffer a 40% "Unregistered Patron" damage penalty.
- Skill 1: "Redefine the Velvet" (Zone Manipulation). The Keeper picks up one stanchion and shifts the rope diagonally across the combat field. He announces: *"The front row is now a Private Function!"* Bros caught in that zone cannot select direct physical attacks until they spend an action to "Step Outside the Line" (repositioning turn).
- Skill 2: "Check the Clipboard" (Interrupt / Counter). If a bro targets him without paying respect, the Keeper raises a wooden clipboard: *"You're not on the manifest."* Cancels the incoming action and deals 10 Ego damage.
- Skill 3: "Stern Velvet Whip" (Physical). Snaps the heavy brass clasp of the rope like a bullwhip. Deals 14 damage and knocks the target back.

Counterplay & Nonviolent Resolution:
- Counterplay A (Exposing the Boundary): Using Chadwick's Roast Line (*"Bro, there is no wall to your left!"*) or Pilsner's Bravado (*"I know the guy who bought this fabric!"*) forces the Keeper into existential protocol confusion (*"Regulations state the boundary is conceptual!"*). He spends 2 turns furiously measuring floor tiles, reducing Defense to 0.
- Nonviolent Resolution (The Bribe of Zero Value): Presenting Chadwick's free `PRESS` Napkin or Pilsner's 1998 laminated ID causes the Keeper to inspect the ink under a magnifying glass, murmur *"Your accreditation is dangerously irregular, but the typography is confident,"* unhook the brass latch with grand ceremony, and let the party pass without further violence! Grants full XP and the `decorative_brass_stanchion_clip`.
```

---

