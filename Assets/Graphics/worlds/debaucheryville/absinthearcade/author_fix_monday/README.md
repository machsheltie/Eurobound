# Arcade Hall clean plate: for the author's Photoshop fix

The author asked for these files in one folder so they can fix two spots in Photoshop (Desk card `asset-team-qc-arcade-hall-31a-r3`, bead Eurobound-fbqk). Wiring the hall cut-outs waits for this fix.

## Files
- `clean_hall_day.png`, `clean_hall_night.png`, `clean_hall_emit.png`: the clean plates to fix. These are the hall with the cabinets removed. They are 3.1a round 3, from the asset-team worktree branch `worktree-agent-ada783cbf789ee2ee`, commit 1b35196d.
- `before_hall_day.png`, `before_hall_night.png`, `before_hall_emit.png`: the original hall with the cabinets painted in, for reference.
- `before_clean_pieces_sheet.jpg`: before, clean, and pieces back on, for day and night, plus 2x crops of the arch foot.

## The two spots
1. **The arch's diagonal grey stone strip.** It is right of centre, at the foot of the right arch pillar, behind the claw cabinet: about x2400-2680, y1150-1350 in the full-size plate. The fill turned it into a long diagonal slab that ends in a soft stub against the pillar. It should read as plain floor tiles, or as a short threshold that stops cleanly under the cabinet's footprint.
2. **The soft refilled floor.** It is where the foosball table and skee-ball stood: about x700-1120, y740-940. The tiles there are softer than the original tiles around them, and there is a faint dark smear beside the red pole at about x745-790, y800-840.

Please fix day and night. The glow (emit) plate only needs a change if a fix touches a lit area. The night plate should stay registered to the day plate, pixel for pixel. Everything outside these two spots should stay as it is.

## When done
Save over the `clean_hall_*.png` files in this folder and tell the asset team (via the Eurobound Desk). The team copies them into `game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/` and hands them to the Arcade window for wiring under bead fbqk.

## Also in this folder
- `bottoms_down/`: Bottoms Down (Shamsterdam) exterior and interior plates, with their spots listed in `bottoms_down/README.md` (Desk card `asset-team-qc-bottoms_down-cleanup`, bead Eurobound-g579).
