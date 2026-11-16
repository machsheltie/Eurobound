# Bottoms Down plates: for the author's Photoshop fix

You asked for Bottoms Down to go into your Monday Photoshop folder (Eurobound Desk card `asset-team-qc-bottoms_down-cleanup`, answer A, 2026-11-15; bead Eurobound-g579). The design passes blind review. These spots are what the clean-up round couldn't fix: automatic fills kept making new artefacts.

## Files

All plates are 2560x1440. They come from the asset-team worktree branch `worktree-agent-a4183eadfc06dcad5`, commit ba615521.

- `bottoms_down_ext_day.png`, `bottoms_down_ext_night.png`: the exterior plates to fix.
- `bottoms_down_ext_front_elevation_day.png`: the straight-on elevation. It is here so you can check it; the review didn't flag it.
- `bottoms_down_int_day.png`, `bottoms_down_int_night.png`: the main room (sawdust floor, bottle wall behind the bar).
- `bottoms_down_int_back_room_day.png`, `bottoms_down_int_back_room_night.png`: the back room (portraits, bare bulb, bottle shelves left and right).

The review sheets are on the same branch:
- `dev/asset_team/reviews/bottoms_down_ext_review.jpg`
- `dev/asset_team/reviews/bottoms_down_int_review.jpg`

## The spots (blind review, cleanup round, `dev/asset_team/reviews/qc_log.jsonl`)

1. **Exterior, left neighbour wall** (day and night): the alley wall on the left, roughly the left fifth of the plate. It still reads as repeating cloned brick. There is a tinted patch where the old chevron was, with a faint translucent arch on top. It should read as one plain, dirty neighbour wall.
2. **Exterior, right edge** (day and night): a thin mirrored strip runs down the far right edge. It should continue the wall or drainpipe naturally.
3. **Back room, bottle labels** (day and night): some labels on the left and right shelves still carry scrawl that looks like writing. There are flat pasted-looking patches, and a mirrored chevron at the right edge. Labels should be blank or plain smudged paper, with no pseudo-text.
4. **Main room, bottle labels** (day and night): the label rows on the bottle wall behind the bar show blotchy pseudo-text. At night they also show a few number-like smudges. Same fix: blank or plainly smudged labels.

Keep day and night registered to each other, pixel for pixel. Everything outside these spots should stay as it is.

## When done

Save over the files in this folder and tell the asset team (via the Eurobound Desk). The team then:
1. copies them into `game/assets/worlds/shamsterdam/bottoms_down/`, together with the branch's exterior props and `placement.json`;
2. runs the final blind A2;
3. commits to main.
