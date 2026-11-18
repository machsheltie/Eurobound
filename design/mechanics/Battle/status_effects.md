Eurobound Status Effects & Conditions
POSITIVE STATUS EFFECTS ✨
"Liquid Confidence"
    • +3 Charm, +2 Bravado, -1 Accuracy 
    • Duration: 3-5 turns 
    • Source: Alcohol items, certain party scenarios 
    • Description: "Feeling invincible and irresistibly charming" 
"Gains Bro"
    • +2 Attack, +1 Intimidation 
    • Duration: 2 turns 
    • Source: Muscle Milk, protein supplements 
    • Description: "Feeling swole and ready to flex on haters" 
"Hydrated for Once"
    • Immunity to "Hangover," +1 HP regen per turn 
    • Duration: Until next alcohol consumption 
    • Source: Actually drinking water (rare) 
    • Description: "A miraculous state of proper bodily function" 
"Manic" (Four Loko Effect)
    • +3 Speed, -2 Accuracy, double actions per turn 
    • Duration: 2 turns, followed by "Crash" 
    • Source: Four Loko (Original Recipe) 
    • Description: "Heart racing, vision blurring, feeling unstoppable" 
"Heart Palpitations"
    • +1 Priority next turn, -1 HP per turn 
    • Duration: 3 turns 
    • Source: Sextuple Espresso 
    • Description: "Your heart beats in morse code: S.O.S." 
"Hardcore Gamer"
    • +2 Speed, +1 Crit chance, -1 HP per turn 
    • Duration: 2 turns 
    • Source: BAWLS Guarana 
    • Description: "Committed to the grind, ignoring basic human needs" 

NEGATIVE STATUS EFFECTS 💀
"Hungover"
    • -2 to all stats, -1 HP per turn, 25% chance to skip turn 
    • Duration: 3-5 turns 
    • Cure: Time, Advil, greasy food 
    • Rulings (author, 2026-11-13, Eurobound Desk 64vo-q1, q6): "all stats" means "The six combat stats: offense, defense, speed, charm, luck, grit". While Sugar Rush Hour or Gush-Locked hides it: "Pause: the timer stops while hidden and picks up again when it returns"
    • Description: "Everything hurts and the sun is your enemy" 
"Sloppy"
    • -3 Accuracy, 15% chance to hit allies 
    • Duration: 1-2 turns 
    • Source: Mystery Beer, excessive drinking 
    • Description: "Hand-eye coordination has left the building" 
"Confused"
    • Picks a random target from everyone on the field except the user. Ruled: round v27 `ef4_confused_stun`, "Confused: each action targets someone at random, never the actor" (docs/superpowers/NEXT_WORK.md:570; game/battle/battle_rulings.gd:27-28). Engine: every single-target hit, bro or enemy, re-rolls its target from all targetable units on both sides except the user, allies included; with nobody else left the action lands on no one (game/battle/battle_core.gd:1014-1025, called at :945, :1620, :1694). Confused is checked before Sloppy, so a Confused unit never takes Sloppy's 15% ally roll as well (:1016, :1027). Battle id `confused`, a negative status (:20)
    • Duration: 2 battle turns when Green Fairy Confusion is carried in from the field. Ruled: round v43 "Field statuses carry into battle" (NEXT_WORK.md:747) and round v44 `b_confusion_battle = 2turns`, "Field Confusion lasts 2 turns in battle" (NEXT_WORK.md:795; game/core/field_status.gd:101-104, :114-123). Every fight-data source also gives 2 turns (`status_turns`, debaucheryville_arcade_battle.json). From any other source: PENDING (Foam Fighter's length is Eurobound Desk Eurobound-tcip-q1 R1). Re-applying it sets the counter to the new length (battle_core.gd:1122): engine behaviour, not ruled
    • Source (ruled): Croc Monsieur's "Still or Sparkling, Monsieur?" (review round 2026-11-09, NEXT_WORK.md:456-458; game/assets/data/enemies/debaucheryville_arcade_battle.json:58-63). Mirror Chad "Confuses you if not beaten in 3 turns" (round v44, NEXT_WORK.md:776; "Exactly Like Your Father", debaucheryville_arcade_battle.json:844-849). Green Fairy Confusion carried from the field, e.g. the Absinthe Lager's 30% risk to the drinker (game/assets/data/items/consumables.json:82; game/core/game_state.gd:106-108). Sugar Rush Hour and Gush-Locked cancelling each other (author, Eurobound Desk Eurobound-4ug-q7, 2026-11-13: "Use the existing Confused status"; not yet in the engine, status_effects.json:113 still reads pending, Eurobound-rry7)
    • Source (in the engine's fight data, from approved villain docs and the round v44 Taproom proposal): Super Turbo Hyper Jarmila's "Revised Input Sheet" (debaucheryville_arcade_battle.json:589-599); the Green Fairy Wisp's "Confusion Breath", one bro or all, 40% (:893-915)
    • Source (written in docs, not ruled): PENDING. Foam Fighter (design/mechanics/Battle/status_entries/foam_fighter.md; Eurobound-tcip-q1), the Late-Night Kebab Stand's random status (design/worlds/debaucheryville/Late-Night Kebab Stand.md:110), Vanessa in Couchsurfing Chronicles (Eurobound Desk Eurobound-w7nx-q1)
    • Resistance: Reality Anchor, party-wide, blocks 10% of applications. Ruled: round v43 `fs_reality_anchor = block` (NEXT_WORK.md:751; field_status.gd:94-98), party-wide in round v44 (NEXT_WORK.md:794), and in battle too (author, Eurobound Desk orch-reality-anchor-battle, 2026-11-12: "Yes, 10% block in battle too"; battle_core.gd:1113-1115). "Neon Photogenic" badge: +5% resistance, permanently, that badge only (Brewery Tour rulings 2026-08-04, NEXT_WORK.md:134; design/quests/debaucheryville/brewerytourdebaucheryville.md:381-385); not built. The Neon Nightmare gives Confusion immunity for its battle (brewerytourdebaucheryville.md:344-345; Eurobound Desk Eurobound-picf-q1, "ruled as written, not built", game/assets/data/skills/status_effects.json:484). Fight data: Croc Monsieur, Mirror Chad and the Green Fairy Wisp are immune (debaucheryville_arcade_battle.json:8-11, :810-813, :859-861); Jarmila resists 75% (:544-546), Accounts Receivable 50% (:786-788)
    • Cure: the Revision Sticker, Jarmila's 30% rare drop (super_turbo_hyper_jarmila.md:162, approved 2026-11-09; consumables.json:93-100; battle_core.gd:302-305). Any other cure, and whether the fight's end clears it: PENDING
    • Icon: a twist puzzle cube whose colours won't line up, red debuff border (author, Eurobound Desk du51-wr1, 2026-11-15, NEXT_WORK.md:918; design/ux/battle_hud_icon_pictures.md:24)
    • Field form and name: PENDING (Eurobound Desk Eurobound-mb38-q1). The engine treats the field status Green Fairy Confusion (reversed movement and scrambled dialogue choices, a random 30 s to 3 min, round v43, NEXT_WORK.md:748) as the one that becomes `confused` in battle (field_status.gd:121-123); the quest calls the Absinthe Lager's effect "Confused" (brewerytourdebaucheryville.md:90), its item doc "Green Fairy Confusion" (design/items/brewery_tour/beer_absinthium_taproom_item.md:12). No ruling says whether they are one status or two
    • Description: PENDING (no flavour line written)
"Embarrassed"
    • -20% ATK, drains 2 Bravado a turn, locks Bravado-cost moves and Ultimates, and blocks Taunt (Flex and Item still allowed). Ruled: round v27, "Embarrassed is -20% ATK, -2 Bravado a turn, and locks Bravado-cost moves and Ultimates" (docs/superpowers/NEXT_WORK.md:569); author, Eurobound Desk g0jr-q3, 2026-11-17, "Embarrassed blocks Taunt on top of its v27 effects, not Flex or Item" (NEXT_WORK.md:948). Same wording as design/mechanics/Battle/bravado.md:21. Engine: game/battle/battle_rulings.gd:13-16 (EMBARRASSED_ATK, EMBARRASSED_DRAIN), battle_unit.gd:166-167, battle_core.gd:239, :522, :883-884. This replaces the list's old "-2 Charm, -1 Confidence, can't use 'Bravado' abilities"
    • Duration: 2 turns in battle (round v28, NEXT_WORK.md:583; battle_rulings.gd:39-41). In the field: 60 game-minutes unless the source's own doc writes another length (Desk Eurobound-jsd0-q1, NEXT_WORK.md:961; per source below), carried into a fight for 2 turns, 10% shorter per resistance point (round v44, NEXT_WORK.md:782-785; game/core/field_status.gd:100-107, :768-777). This replaces the list's old "2-3 turns"
    • Source (battle): villain moves in the fight data (game/assets/data/enemies/debaucheryville_arcade_battle.json) and combo backfires (game/assets/data/skills/combos.json:28, :78)
    • Source (field, round v44): the shame timer, a failed QTE and the hostel witness, 60 game-minutes each (round v44, NEXT_WORK.md:782-785; field_status.gd:108-112)
    • Source (field, the other sources stand): author, Eurobound Desk Eurobound-jsd0-q1, 2026-11-18, "They stand. A length written in the doc stands (the debate's 30 min); otherwise the standard 60 game-minutes (same rule as battle in Round v28)" (NEXT_WORK.md:961). Each lasts the length its own doc writes; a doc that writes none gets 60 game-minutes:
        ◦ Losing the Café Existenz debate: 30 game-minutes, written in its docs (design/worlds/sinfonia/cafe_existenz.md:161; design/worlds/sinfonia/npcs/Cafe_Existenz/npc_maximilian_von_grubelstein.md:159, :273)
        ◦ The Black Tie Backroom, "Cleaned Out" ejection and second offense: 60 game-minutes, no length written (design/worlds/sinfonia/the_black_tie_backroom.md:39, :255)
        ◦ Red Light Shame in Shamsterdam: 60 game-minutes, no length written (design/worlds/shamsterdam/shamsterdam.md:279)
        ◦ The Suspicious Twins couchsurf outcome: 60 game-minutes, no length written (design/worlds/debaucheryville/npcs/Cirque_du_Shady/suspicious_twins_polina_paulina.md:184, :275)
        ◦ The Velvet Curtain Club influencer exposé: 60 game-minutes, no length written (design/worlds/debaucheryville/velvet_curtain_club.md:316, :462; game/assets/data/locations/debaucheryville/debaucheryville_environmental.json, embarrassed_from_social_failures)
        ◦ Social failures and wardrobe malfunctions (this list's general line): 60 game-minutes
    • Engine: the default field length is status_effects.json `default_duration.clock_minutes` = 60. apply_embarrassed (game/core/field_status.gd, Eurobound-glbd) reads that default, takes a per-source length (EMBARRASSED_SOURCE_MINUTES: the debate's 30) and accepts every source above; only the three round v44 sources have a trigger built, the others have none yet
    • Description: "Wishing you could disappear into the crowd" 
"Grease Fingers"
    • -2 Accuracy, can't use tech items 
    • Duration: Until washed or 4 turns 
    • Source: Fast food, greasy snacks 
    • Description: "Everything slips from your butter-coated hands" 
"Broke AF"
    • Cannot buy items, -1 Confidence in battle 
    • Duration: Until earning money 
    • Source: Overspending, getting scammed 
    • Description: "Your wallet echoes when you shake it" 
"Tourist Trap Victim"
    • Pay 2x for all items at shops, certain NPCs mock you 
    • Duration: Rest at hotel or visit 3 different areas 
    • Source: Falling for obvious scams 
    • Description: "You might as well wear a sign that says 'ROB ME'" 
"Port-O-Cologne"
    • -3 Charm with all NPCs, vendors add a "smell tax" (+25% prices), romance dialogue locked, NPCs step away, fly particle effect follows you 
    • Duration: Until paid shower at hostel or spa visit 
    • Source: Being launched into the Bacchanus in a loaded port-o-potty (Bacchanus Beach Beatdown loss) 
    • Special: Swimming in the Bacchanus to "rinse off" REFRESHES the duration 
    • Description: "You smell like second place" 
"The Herp"
    • -2 Charm with all NPCs, romance and couchsurf attempts auto-trigger the target NPC's characterized rejection scene, rare involuntary "Groin Blurts" interrupt any dialogue ("DOES ANYONE HAVE A BAG OF FROZEN PEAS?!" / "IT'S JUST A RASH, I SWEAR!"), subtle waist-level heat-shimmer particle follows you, NPCs visibly step back 
    • Duration: Permanent. Never cured — only suppressed while `item_gold_circle_coin` is equipped (any one bro suppresses the whole party; unequip and the shimmer returns on all three) 
    • Source: The scripted outbreak at the Bohemian Riviera `night_party_zone` (`night_event_outbreak_01`, `debaucheryville_sidequest_nothing_is_getting_through_01`); Věra refuses every standard cure — "Euromemeian strains require cinematic-grade containment." 
    • Special: All three bros carry it simultaneously, always. No temporary suppressant exists anywhere in the game. The waist-level shimmer REUSES the Bohemian Riviera effects atlas asset `heat_shimmer.png` — no new particle asset 
    • Description: "It's poison ivy. There was DEFINITELY foliage at that beach party" 

NEUTRAL/SITUATIONAL EFFECTS ⚖️
"Food Poisoning"
    • -2 HP per turn in battle, 50% chance to lose turn 
    • Duration: 5-8 battles or until cured 
    • Source: Sketchy street food, expired items 
    • Description: "Your digestive system has declared war" 
"Lost AF"
    • Cannot access fast travel, certain areas locked until finding map/directions 
    • Duration: Until getting directions from NPC or finding landmark 
    • Source: Wandering drunk, ignoring obvious signs 
    • Description: "Everything looks the same when you're this confused" 
"Reputation Ruined"
    • Certain NPCs refuse service, some shops won't sell to you 
    • Duration: Until leaving current city/area 
    • Source: Public embarrassment, causing scenes 
    • Description: "Word travels fast in small Euromemeian districts" 
"Caffeine Crash"
    • -1 to all stats in battle, move speed reduced in overworld 
    • Duration: 10 minutes real time or until consuming caffeine 
    • Source: Energy drink effects wearing off 
    • Description: "Your body demands payment for that artificial energy" 

COMBO STATUS EFFECTS 🔄
"Blackout Drunk"
    • Combines "Liquid Confidence" + "Sloppy" + memory loss 
    • Special: Battle ends, wake up in random location with random items missing 
    • Source: Excessive alcohol consumption 
    • Description: "The last thing you remember was ordering 'just one more'" 
"Crash" (Post-Manic)
    • -3 to all stats, 75% chance to skip turn 
    • Duration: 3 turns 
    • Source: After "Manic" effect ends 
    • Also follows "Sugar Rush Hour" (STRAWBERRY SHORTCAKE SPEEDCAKES™)
    • Rulings (author, 2026-11-13, Eurobound Desk 64vo-q1, q2, q3, q7): "all stats" means "The six combat stats: offense, defense, speed, charm, luck, grit". Outside a fight: "Battle only: Crash waits for the next fight and runs its turns there". Stacked: "Stacks last longer: more Crash turns per stack; one drink per Cottonmouth stack" (turns per stack are not ruled; each stack adds the Duration above once). After Sugar Rush Hour and Gush-Locked cancel, Crash and Cottonmouth: "Both still hit, right after the cancel"
    • Description: "What goes up must come crashing down" 
"Existential Crisis"
    • All abilities become "Question Life Choices" (does nothing) 
    • Duration: 2 turns or until ally uses "Snap Out of It" ability 
    • Source: "Reality Check" enemy attacks, enemy taunts about age/life choices ("You're nearly 40 and wearing JNCO jeans!") 
    • Description: "What am I doing with my life?" 
