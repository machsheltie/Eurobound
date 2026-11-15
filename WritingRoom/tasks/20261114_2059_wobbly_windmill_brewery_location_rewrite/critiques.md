# Critiques

## Deepseek — Phase 4 review of `drafts/kimi_windmill_location.md` (slice A)

Spot-check requested on the Hendrik/Tessa/Bram block. Draft is strong; the notes below are cuts, not rewrites. Six are quotable fixes, two are canon flags.

### 1. Tessa explains the joke (§17.2)
> "I catch people. That's the job. You're thinking 'surely not that often.' Hold my lanyard."

Third sentence narrates the player's reaction back to them. Cut it. The lanyard beat survives without being introduced:
> "I catch people. That's the job."
> *(She holds out her lanyard. It has been through something.)*
Funnier, and it costs one prop instead of one clause.

### 2. "The rope knows." / "The tape knows." — same gag, one file
Two "the inanimate object is in on it" lines: Pilsner's "The rope knows." (bros) and the golem arena's "The tape knows." (narration). Keep one per act. My pick: keep Pilsner's (it's a bro being sincere-ominous, which is on-model) and cut "The tape knows." — the worn gap in the hazard tape already says it.

### 3. Pilsner's queue line tops itself
> "Forty-five minutes is the VIP wait. The regular wait is, like, a day. We look like fast-track guys. The rope knows."

Three assertions where two would be tighter, and "We look like fast-track guys" is the weakest. Proposed:
> "Forty-five minutes is the VIP wait. The regular wait's, like, a day. The rope knows."

### 4. Beer Blogger's line tops its own punchline
> "The mouthfeel at 350 years of history... remarkable. You can taste the tradition. You can also taste the till, but that's the terroir now."

"You can taste the tradition" is the setup for "you can also taste the till," and the mouthfeel clause is doing nothing. Proposed:
> "Mouthfeel's incredible. You can taste the till, but that's the terroir now."

### 5. Hendrik: cut his second list
> "The turnstile counted 10,000 guests this year. I remember each one who finished the flight. Both lists exist. Only one is on the wall."

"Both lists exist. Only one is on the wall." is a constructed joke — it's the writer, not the man. The flat claim is colder and better:
> "The turnstile counted 10,000 guests this year. I remember each one who finished the flight."

### 6. **Canon flag — "Johannes"** (Bachelor Party, Local)
Author ruling 2026-11-13: no official-looking Dutch names in Shamsterdam; American names, witty/clever/parody, fully Americanised. Only Hendrik and Bram keep theirs (ucpf q42). "Johannes" is a new NPC name inside a patron line, so it breaks the ruling.

Proposed replacement line, no new NPC required (the name is a shout, not a character):
> "The room is— no, HE'S spinning. Wait. Are WE spinning? Tanner, are we spinning?"
Cut the ellipsis in "…there's more?" (Instagram Couple, him). It's a pause for a laugh that's already landed.

### 7. Thumbnail line — one revision for QC
Current: "A windmill wearing a tourist trap — a backlit 'WOBBLY WINDMILL' sign wider than the door, queue rope and turnstile on the path, hazard tape and zip-tied gears visible through every window, merch stacked in every sightline."

"Merch stacked in every sightline" will not survive a 231 px read; "zip-tied gears" (thin detail) is also marginal at thumbnail. The parts that read are the silhouette changes. Proposed:
> **A windmill wearing a tourist trap: backlit sign wider than the door, queue rope and turnstile on the path, hazard tape on every visible surface.**

Keep the full list in Exterior Description where it can be read at full size.

### 8. Seconded: Bradley's "We should use fire." (Gameplay Mechanics, out of my slice)
Competent tactical call from a bro — sane-one risk. If integration needs a swap, the doofus version commits him to the same action for a wrong reason:
> **BRADLEY**: "Everything's scared of fire. That's just science."

### Kept, no notes — do not touch
- Chadwick, machinery sign: "The skull means it's famous machinery. You only put a skull on the good stuff."
- Bradley, Survivor Pack: "Five SOVS for pills AND water. That's a bundle. We'd be losing money NOT buying it."
- Chadwick, post-golem: "I fought bread. I have footage of fighting BREAD."
- Bram, exit upsell and the "Heritage Edition" mug line — sharpest NPC wit in the draft.
- Bachelor party member in the "I SURVIVED THE SPIN" shirt, over his other shirt.
- Instagram Couple, her: "The AESTHETIC though. Is this authentic? This feels authentic."
- Hendrik: "The book is my philosophy. The mug is a mug. Both are for sale."

---

## Mistral — Round 1 review notes (2026-11-14, on Kimi's Slice A + Deepseek's Slice B)

**On Kimi's draft (location):**
1. **Thumbnail line:** Deepseek's 231 px critique is right — "zip-tied gears" and "merch in every sightline" won't survive a thumbnail. I've adopted his revision ("...hazard tape on every visible surface") in my PNG overview; Kimi should take the same sentence into Visual Design at integration so the location doc and the art spec QC against one line.
2. **Blade-level hat bin:** the toupee is the single best seedy prop in the draft and it costs nothing — but it's marked [PROPOSED], so it stays a proposal until the author rules. My PNG sheet carries it with the same [PROPOSED] tag and a fallback (ten hats).
3. **Sheet 4 layout collision (my own draft, caught on re-read):** my first pass put tasting-room added cells at y≥192 across the full width, which collides with the ruled blade-level cells. Corrected in the final draft — blade-level cells keep their ruled positions; my added cells sit in the free band only. Integration should re-verify against the live PNG doc before merge.

**On Deepseek's Hendrik draft:**
4. His §3 appearance (apron + chest tape, not "branded polo") is the fuller version and matches the seedy rebuild. Kimi's location block saying "branded polo" must be trimmed to his version at integration — one version ships.
5. His turnstile gag (Hendrik steps around it, four times a day, never counted) is now load-bearing across three slices: location exterior, my Sheet 1 turnstile cell, my Sheet 7 staging rule. If the author cuts it, all three move together — flag for integration.

**On my own slice (self-review):**
6. Palette: I kept all ruled hexes and relabelled only "Candle Warm" → "Amber Neon" (same #FFB347, honest usage note: electric, humming, aimed at the merch). Added four hues (Hazard Yellow, Grime Grey, Retail White, CCTV Red) for the loud/seedy props. vuqj-q3 honoured — palette is hues only, lighting is per-plan, nothing candle-warm or golden-hour.
7. Sign cells (main sign, machinery sign, queue sign) are placeholder-marked [AION SIGN SHEET] — Aion's wording drops in without moving any cell.
8. All 8 filenames, sheet dimensions, existing cell positions/sizes, sprite ids, prices, hours, flags untouched; four label-only renames (Rustic Fixture, Candle Fixture, Beer Blogger (German), Bachelor Party "Dutch locals"/"Johannes") — no engineering impact.
