# The Great Döner Debate — tablet restage + Kavarna options

**Primary writer: Kimi (Jobs 1–2). Requested reviewer: Gemini — Tony's chatspeak, Big Wim's replacement line, joke-explanation audit, and whether any Kavarna option spends the Döner reveal.**

**Status: PROPOSED replacement text, not applied.** Canon source `design/quests/general_quests/greatdonerdebate.md` is read-only and is not edited. Identical text also exists at `design/Quests/greatdonerdebate.md` and in legacy copies; the moderator owns any sweep.

**Author rulings applied (2026-11-11):** never a physical Tony; big, silent, unnamed goon; tablet at face height like a hostage photo; screen BLANK first, then the familiar ICQ "Uh-oh!", then the blurred/voice-changed video; Oakleys legible through the blur; deep, slowed, pitch-shifted voice with lowercase ICQ subtitles; the Kavarna goon is held until after this scene.

**Global speaker convention for the whole branch:** every `Tony420:` line from the goon's entrance to the end of Outcome C is **(tablet, subtitled)** — blurred video, changed voice, lowercase ICQ spelling. The goon never speaks, never reacts, and never gets a name. His only acting is holding the tablet up.

---

## JOB 1 — exact old → new replacements

### R1 — the "They all taste like shame" confrontation (canon lines ~373–400)

**OLD:**

```
*The door creaks open slowly. Tony420 himself walks in — 
a pale, hoodie-clad figure who has clearly never seen sunlight.*

Tony420: "yo"

Lord Pilsner: "...Tony? You're... real?"

Tony420: "in the flesh lol
well
mostly flesh
haven't been outside in a while"

Big Wim: "Who is this child in my establishment?"

Tony420: "i'm the one who asked the question
and u said they ALL taste like shame
which was based honestly
but now ur here
eating
with ENTHUSIASM"

*Tony420 holds up a phone showing the original ICQ poll*

Tony420: "u gotta pick now
for real this time
no shame option
just... truth"
```

**NEW:**

```
*The door creaks open slowly. A huge man walks in, stops, 
and holds up a tablet at face height, like a hostage photo. 
The screen is blank.*

*ICQ: "Uh-oh!"*

*The screen lights up: Tony420, heavily blurred, Oakleys 
perfectly visible through the blur.*

Tony420 (tablet, subtitled): "yo"

Lord Pilsner: "...Tony? You're... real?"

Tony420 (tablet, subtitled): "in the flesh lol
well
mostly flesh"

Big Wim: "You bring a man to hold your phone?"

Tony420 (tablet, subtitled): "im the 1 who asked the question
and u said they ALL taste like shame
which was based honestly
but now ur here
eating
with ENTHUSIASM"

*The tablet switches to the original ICQ poll. The goon 
tilts it toward the bros.*

Tony420 (tablet, subtitled): "u gotta pick now
4 real this time
no shame option
just... truth"
```

**What changed and why:**
- The reveal is now a two-beat entrance: a body with a dead screen, then the "Uh-oh!", then the face. The bros meet him for the first time exactly as the author staged it, and Pilsner's canon "...Tony? You're... real?" survives untouched because it is now the player asking a blurred video whether it exists.
- "in the flesh lol / well / mostly flesh" survives verbatim. It is now literally true of the goon and not of Tony; nobody in the scene notices, and no line explains it. "haven't been outside in a while" is cut — it belonged to the pale-hoodie body description, and the remaining three lines land harder without it.
- Big Wim's "Who is this child in my establishment?" is the only non-Tony line that stops making sense (there is no child). His replacement keeps his register: a warm, enormous man objecting to the catering arrangement rather than to the criminal on the screen. He is not scared, not suspicious, and does not explain the gag.
- The poll beat is preserved mechanically: the same original ICQ poll appears on the tablet, the goon presents it, and the same "u gotta pick now" demand follows. No phone appears in Tony's nonexistent hands.
- `i'm` → `im`, `for real` → `4 real`: the author's "not that eloquent, late-90s chatspeak" ruling. The remaining lines are canon wording.

### R2 — Outcome C, the slow zoom (canon lines ~539–541)

**OLD:**

```
*Slow zoom on Tony420's face (he's still there somehow)*

Tony420: "bro just invented döner diplomacy
this is either galaxy brain or smooth brain
honestly can't tell"
```

**NEW:**

```
*Slow zoom on the tablet. The goon has not moved. 
The blur has not improved.*

Tony420 (tablet, subtitled): "bro just invented döner diplomacy
this is either galaxy brain or smooth brain
honestly can't tell"
```

Tony's three lines are unchanged canon. The zoom now lands on the same image the player has been looking at for the whole scene, held by a man who has never moved. No line remarks on it.

### R3 — Implementation Notes, the reveal requirement (canon line ~651)

**OLD:**

```
- Tony420 appearing "in the flesh" should feel like a major reveal
```

**NEW:**

```
- Tony420's first appearance must stay a major reveal: the goon enters with a BLANK tablet at face height, the ICQ "Uh-oh!" plays, and the screen lights up on the blurred, voice-changed Tony (deep, slowed, pitch-shifted; Oakleys visible through the blur; subtitles keep his lowercase ICQ spelling). The goon is big, silent and unnamed, and never speaks for him. Do not show the goon or the tablet anywhere before this scene, including Cyberspace Kavarna — the Kavarna goon is held until after the Döner Debate (author ruling 2026-11-11). Tony420 has no body sprite and no walk cycle; only the goon moves.
```

**Scope note:** Outcomes A and B keep `Tony420 (via ICQ popup)` as written. Those are phone messages, not in-person beats, so they need no tablet staging.

### R4 — profile sync note (for the moderator, not a player-facing line)

`npc_tony420.md` "In Person (the goon and the tablet)" still quotes the superseded body lines ("in the flesh lol / well / mostly flesh / haven't been outside in a while", "The goon holds the tablet up so Tony can show the original ICQ poll") and its Development Notes list the same canon lines as needing a sync pass. Once R1–R3 are approved, that section should be replaced with the NEW block above, and the "Big Wim's line / slow zoom" caveat deleted. The same profile's Kavarna rows (goon at the rented terminal, repurposed sprite slot, goon animation list) conflict with the hold-the-goon ruling until after Shamsterdam; see Job 2.

---

## JOB 2 — Kavarna options

**The constraint:** Debaucheryville comes before Shamsterdam. Katka has staked out Tony's rented terminal for three years from the chair on its right, Dmitri rents it to him at full price, and her Tony420 File / Operation Script Kiddie has to keep working — without the bros ever seeing a goon or a tablet before the Döner Debate. All three options below keep the sting entirely on ICQ and the wallet, which is where the location file already puts it ("Expose Tony420's fake crypto wallet scheme through ICQ infiltration").

### Option A — the warm chair (RECOMMENDED)

The terminal is always empty and always logged in: ICQ open on Tony420's handle, a chair that is warm, a desktop full of wallet files. Katka has spent three years documenting a man who has never once been in the chair while she watched.

> **Katka:** "Three years I watch that chair. Nobody sits. The wallet never logs off. Either he is the best criminal in Debaucheryville or the chair is doing it."

Why this one: it preserves her entire character — her intel stays perfect, her one wrong conclusion stays wrong in a new way — and it turns the later Döner reveal into a retroactive punchline for the player without her or the bros ever learning anything. It also gives the bros a physical seat to sit at for the ICQ sting.

### Option B — remote desktop, full price

The terminal runs a remote-desktop window to somewhere else; Dmitri rents the machine, the chair and the power outlet to Tony at full price and considers this a completely normal tenancy.

> **Dmitri:** "He rents terminal. What he does on terminal is his business. ...He is not here. He is never here. Three Sovs."

Why this one: it makes Dmitri the joke instead of Katka, and it explains the rent without inventing any new tech beyond the cafe's existing Windows 98 period hardware — a remote session is exactly the kind of thing this room would be running badly. Weakest of the three on Katka's three-year stakeout, since "he is never here" is a fact she would already have.

### Option C — the chair is rented too

The seat is never empty because somebody is always sitting in it: a rotating cast of silent patrons renting the same terminal by the hour, none of them Tony, all of them told to keep the ICQ window open. The bros can pay one of them for the chair and find only the wallet.

> **Katka:** "Different man every night. Same wallet. I have four handles, three years, and eleven men who all paid Dmitri separately. Do not ask me which one is Tony. I will get upset."

Why this one: it gives the room live bodies and a playable social-engineering route to the terminal, and it keeps the goon unused — these are ordinary hourly patrons, not his muscle. Risk: the "eleven men" gag sits close to Miss Morphine's established "at least three physical people" mystery, so it needs to stay a rental roster, never an identity mystery.

**Shared note for all three:** nothing at the Kavarna shows a tablet, a blurred video, a voice changer or a big silent man before the Döner Debate. After the Debate, the held goon-and-tablet staging can move into the terminal slot per the profile.

---

## Self-audit (§17 + the no-explanation directive)

- No narrator, no "little did they know", no character diagnosing the staging. The blank-screen → "Uh-oh!" → blur sequence is animation and sound, not description of what it means.
- Pilsner's "real?" line is canon and is the only bro reaction; no Chadwick or Bradley line was added to top it. "Mostly flesh" is left to do its own work.
- Big Wim gets one replacement line, not a bit. He does not call the goon a goon, does not mention crime, and does not explain that Tony is a video.
- The Outcome C zoom no longer says "he's still there somehow", which was the old text explaining its own joke; the unmoving goon carries it.
- Kavarna option A's Katka line ends on her wrong theory rather than on the answer. Option C's line ends on her being upset, which is her established register when the facts stop cooperating.
- Cut in drafting: a Chadwick line about the production values; a Bradley line about the goon's bench press; a second Big Wim line about the tablet's warranty. All three topped an already-landed joke.
