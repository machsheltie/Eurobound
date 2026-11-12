# Sinfonia Ambient System: The Royal Jingles

**Status:** Canon — author ruling (2026-08-01). Sinfonia-wide ambient system.
**Purpose:** Establish, without a single line of exposition, that König Klaus (Crown & Cask) is not well thought of by his own people — so that the `KING KLAUS` stall nameplate at Stadtpark lands as a joke the player assembles themselves.

---

## What It Is

As the player walks through Sinfonia, ordinary townspeople occasionally **sing** a single line under their breath. The line appears as floating text above the NPC, wrapped in music notes to denote singing:

> ♪ Heavy rains, heavy taxes, heavy sits the head... ♪

**No interaction. No dialogue box. No prompt.** The player does not talk to these NPCs and cannot trigger the lines deliberately. They simply happen, in passing, the way you overhear a stranger humming.

---

## 🔒 THE ONE INVIOLABLE RULE

**A jingle must NEVER name König Klaus, and must never name Klaus at all.**

The lines refer to "the head", "him", "the crown", "the guy running the gate" — never the man. This is the entire mechanism:

- A player who never connects the dots hears grumbly folk songs about a vaguely rubbish monarch. Fine. Atmospheric.
- A player who has been listening walks up to a horse stall in Stadtpark, reads a polished brass plate that says **KING KLAUS**, and the whole petty picture snaps together at once — with zero exposition.

The moment a jingle says "Klaus", the Stadtpark payoff dies and the player is being told a joke instead of finding one. **Never name him.**

Corollary: the jingles must also never mention a horse.

---

## The Canonical Jingles (author-written — use verbatim)

| # | Line |
|---|------|
| 1 | ♪ Heavy rains, heavy taxes, heavy sits the head... ♪ |
| 2 | ♪ The weather's cold, the soup is thin, and the palace walls are closing in... ♪ |
| 3 | ♪ Gold on his finger, gold on his floor, but never a coin makes it past the front door. ♪ |
| 4 | ♪ Long live the crown, long live the state... shame about the guy running the gate. ♪ |

These four are canon and must not be reworded.

## Additional Jingles (drafted in-voice — cull freely)

Written to match the established register: folk-song meter, gentle rhyme, weary rather than angry, always oblique. Marked separately so the author can approve, cut, or rewrite without touching the canonical four.

| # | Line |
|---|------|
| 5 | ♪ He counts the crowns, he counts them twice, and still the bread is twice the price. ♪ |
| 6 | ♪ A feast up there, a fast down here, and both of them go on all year. ♪ |
| 7 | ♪ Sing for the king, sing loud and long — he can't hear a word of it anyway. ♪ |
| 8 | ♪ The throne is gilt, the roof is tin, and one of them is leaking in. ♪ |
| 9 | ♪ We asked for less, he gave us more... of the thing we didn't ask him for. ♪ |
| 10 | ♪ Bless the crown and bless the throne, and bless whoever sits there... eventually. ♪ |
| 11 | ♪ Two things fall on Sinfonia's poor: the rain, and everything else. ♪ |
| 12 | ♪ He rules the barrels, he rules the hall, and hasn't drawn a pint at all. ♪ |

*(Line 12 lands harder if the player has already met König Klaus at Crown & Cask and seen that he does no actual brewing.)*

---

## 🪧 The Royal Decree Sign (Enforcement Layer)

**Placement:** mounted on a gilded post directly beside the main entrance checkpoint into Sinfonia (Grand Entrance District). The player passes it on arrival — **before** they have heard a single jingle.

**Visual:** a ridiculously ornate, over-gilded wooden sign. The royal crest sits at the top with far too much fanfare. The lower half is crammed with tiny, frantic text and aggressive royal-red wax seals — the visual language of a man who kept adding clauses.

### Sign Text (inspectable)

```
[ROYAL DECREE NO. 402-B]

BY ORDER OF HIS MOST SPLENDID AND FLAWLESS MAJESTY, KÖNIG KLAUS

Singing, humming, or rhyming about His Majesty is strictly FORBIDDEN
```

### Why this is the keystone

The sign does the setup work no dialogue is allowed to do:

1. **It proves the singing is widespread.** Nobody legislates against a thing that isn't happening. Decree **402-B** implies 401 previous decrees and at least one prior revision of this one.
2. **It establishes the target before the player meets him.** The decree names König Klaus. The jingles never will — they don't have to, because the sign already did.
3. **It is instantly, visibly ignored.** Townspeople sing within earshot of it. The first jingle a player hears after reading this sign lands as defiance rather than flavor.

### Rules

- **Reading the sign is optional and must never be forced.** No prompt, no tutorial pointer, no quest marker. It is scenery that rewards the curious.
- **No guard ever enforces it.** Checkpoint guards do not react to singing, ever. If asked about the decree they change the subject — the ban's total non-enforcement is the joke.
- **No NPC ever references the decree out loud.** Nobody says "you know singing about the king is banned, right?" The player connects the sign to the singing themselves or not at all.
- **A jingle may fire while the player stands at the sign.** Do not suppress it; that proximity is the single best comedic beat in the system. Cooldowns still apply.
- The decree number and the wax seals should reward zooming: the tiny text is a clause-stack of exceptions, sub-provisions, and penalties that nobody has read.

### Placement note
`sinfonia.md` establishes a **Grand Entrance District** with guard inspection checkpoints. The sign belongs there, on the arrival path, positioned so it is passed rather than sought. If multiple entrances exist, it goes on the main/first-visit one only — one sign, not a set.

---

## Display Rules

| Property | Spec |
|----------|------|
| Presentation | Floating text above the NPC's head, no box, no portrait, no name label |
| Delimiters | Always wrapped in `♪ ... ♪` — this is what marks it as *sung* rather than spoken |
| Interaction | **None.** Not interruptible, not triggerable, not repeatable on demand |
| Trigger | Proximity — fires when the player passes within range of an eligible ambient NPC |
| Duration | ~3.5 seconds on screen, then fades |
| Player control | Cannot be dismissed early; does not pause movement or block input |

### Frequency & Cooldowns
The fastest way to ruin this is to over-serve it. It should feel like a coincidence the player noticed, not a system.

- **Global cooldown:** no jingle fires within 90 seconds of the previous one, anywhere in the city.
- **Per-NPC:** an individual townsperson sings at most once per visit to a zone.
- **Chance:** ~15% roll on eligible proximity triggers, after cooldown passes.
- **No-repeat window:** the same line may not fire twice within a single play session until the pool has been exhausted; then reshuffle.
- **Never during:** combat, cutscenes, active dialogue, quest-critical sequences, or the Fiaker Fiasco finale.

### Who Sings
- **Eligible:** generic Sinfonia ambient townspeople — market-goers, street sweepers, laundry-carriers, café passers-by, queue-standers.
- **Not eligible:** any named NPC, any vendor mid-transaction, any quest-giver, opera staff on duty, and **König Klaus himself or anyone inside Crown & Cask**.
- Singers never acknowledge that they sang. If the player approaches one afterward, their normal ambient dialogue plays with no reference to it.

---

## Tone Direction

- **Weary, not seditious.** These are people complaining about weather and prices in the same breath — the king is just one more thing it rains on. Nobody is organizing a revolt.
- **Affectionate fatalism.** The Sinfonia register: overly refined city, quietly falling apart, everyone too polite to say so directly. Singing it sideways is exactly how these people would complain.
- **Never cruel, never political.** The satire targets a pompous man who does no work, not a system, a nation, or a real institution.
- **Melody:** all lines should scan to the same simple folk tune so a player recognizes the *shape* of it by the third one, even with different words. The recognition of the tune is half the payoff.

---

## Integration

| Connects to | How |
|-------------|-----|
| **Crown & Cask** (König Klaus) | The target of every jingle. He is never named and never hears one. If asked about the songs directly he changes the subject to brewing. |
| **Stadtpark Gustav's Refuge** (`KING KLAUS` stall nameplate) | The payoff. Jingles are the setup layer; the plate is the punchline. See the Easter Egg section in `stadtpark_gustavs_refuge.md`. |
| **Fiaker Fiasco** (canon note) | Full origin of the horse's name lives in `Design/Quests/Location Specific/Sinfonia/fiaker_fiasco.md` → "Canon Note: Why the Horse Is Called Klaus". |
| **Spoken counterpart** | Locals also drop the deadpan spoken line "Better than the other one" when praising Klaus the horse. Sung jingles and that spoken line are two halves of the same running gag — never deliver both in the same scene. |

---

## Accessibility

- Floating text must meet the game's standard contrast and minimum type size; it is decorative but readable.
- Because the lines are *sung*, provide a subtitle/caption representation consistent with the game's audio-cue policy — the ♪ delimiters must survive into any caption track so deaf and hard-of-hearing players get the "this is singing" information, not just the words.
- Never the only carrier of critical information: the jingles are pure flavor and setup. No quest, item, or progression may depend on having read one.
- Respect any "reduce ambient text" or reduced-distraction setting by lowering frequency rather than removing the system.

---

## Implementation Notes

- Data-drive the pool (a simple string list + weights) so lines can be added or cut without code changes.
- Reshuffle-bag selection rather than pure random, to avoid the same line appearing twice in five minutes.
- Assign the tune once and reuse it; the audio is one short motif with different word counts, not twelve compositions.
- Log which lines a player has seen if you ever want an achievement for hearing all of them — but do **not** surface a checklist in the UI. Counting them kills them.
