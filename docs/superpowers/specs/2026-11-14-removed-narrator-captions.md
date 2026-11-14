# Removed narrator captions (Eurobound-hvea)

Author ruling on the bead page, 2026-11-13, verbatim: "On-screen captions: banned, remove them all and quote them for me".

Every caption below was removed from the data on 2026-11-14. The text is verbatim. Nothing was written to replace it.
No copy of either file exists under `game/assets/data/` or `Assets/Data/`; the only copies in the main tree were the two design files below. No loader read these keys.

Total removed: 14 (10 narrator captions, 4 borderline).

## Narrator captions

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `events[2] (event_id janek_thrown_answer).post_event_effects[0] (effect staging_line, target post_janek_thrown_answer).value`

  > Janek Sýkora had not choked. Janek Sýkora had briefly stopped participating, which is a different thing, and which is available to anyone who does not need the prize.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_entering`

  > A landlocked country's beach resort, built entirely out of confidence and trucked-in sand.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_key_moment`

  > The sentence was never finished. It was, however, finished for him, by physics, which had been waiting patiently for its turn to speak.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_signing_forms`

  > Three men signed away their likeness, their dignity, and their right to legal recourse in perpetuity across all media known and not yet invented. Two of them did it while flexing. The third did it on behalf of the other two, which is not how that works, and which Petra noted for the record, twice, out loud.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_second_port_o_potty_impact`

  > There is a specific sound a portable toilet makes when it strikes a river at forty kilometers an hour, and the network had, over twenty-two seasons, come to think of it as their theme music.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_walk_of_shame`

  > They walked the length of the Bohemian Riviera in a language they could not speak, being told exactly what had happened to them, in detail, by children — and arrived at their hostel believing they had been applauded.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_prize_podium_win`

  > A hamster in a wizard hat and a beach-appropriate speedo pinned a plastic star to a man's chest, and told him the truth about his future in capital letters, and he did not hear a word of it, because the star was shiny and the crowd was loud and he was, at long last, being looked at.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_janek_thrown_answer`

  > Janek Sýkora had not choked. Janek Sýkora had briefly stopped participating, which is a different thing, and which is available to anyone who does not need the prize.

- File: `design/worlds/debaucheryville/interactions/cirque_du_shady_interactions.json`
  JSON path: `staging_notes.on_key_moment`

  > The ticket booth's sign says 'everything else extra' in plain English before they've paid for anything, and it changes nothing about what a bro chooses to believe he's walking into.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `events[1] (event_id beatdown_gauntlet).sequence[2] (phase launch_two_q7_mid_sentence, speaker staging).dialogue`

  > The sentence was never finished. It was, however, finished for him, by physics, which had been waiting patiently for its turn to speak.

## Borderline

These read more like factual staging than narration. They sat in the same `staging_notes` blocks, and the ruling was to remove them all, so they were removed too.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_disqualification`

  > House rules. No devices in the toilet. Chadwick's stream ends on the splash and the VOD auto-saves.

- File: `design/worlds/debaucheryville/interactions/bohemian_riviera_interactions.json`
  JSON path: `staging_notes.on_exit`

  > The catapult stays. It is never dismantled. Between filming days it is simply there, on a beach, roped off with hazard tape.

- File: `design/worlds/debaucheryville/interactions/cirque_du_shady_interactions.json`
  JSON path: `staging_notes.on_entering`

  > Gilded Square cobblestones give way to trampled grass and sawdust well before the gate itself is visible - the smell arrives first.

- File: `design/worlds/debaucheryville/interactions/cirque_du_shady_interactions.json`
  JSON path: `staging_notes.on_exit`

  > The dome is visible from streets away, faded red-and-cream, and has clearly not moved, in any literal sense, in a very long time.

## Note on the duplicates

The Janek line appeared twice in `bohemian_riviera_interactions.json`: once in `staging_notes.on_janek_thrown_answer` and once as a `staging_line` effect on the `events` entry. Both were removed. That event's `post_event_effects` list is now empty.

The "sentence was never finished" line also appeared twice: in `staging_notes.on_key_moment` and as a `dialogue` value with `speaker: "staging"` on the second-launch phase. Both were removed. That phase keeps its description, animation and audio fields.
