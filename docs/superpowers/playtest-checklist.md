# Vertical Slice Playtest Checklist

Run `godot --path .` and verify each item. Re-run after any change to core systems.

## Boot & Title
- [ ] Project opens to the title screen, no errors in console
- [ ] Continue is greyed out when no save exists (delete `%APPDATA%\Godot\app_userdata\Eurobound\saves\slot1.json` to test)
- [ ] New Game starts in Clocktower Plaza

## Overworld
- [ ] WASD and arrow keys both move Lord Pilsner
- [ ] All four plaza edges block movement
- [ ] The camera follows the player

## Dialogue (blue rectangle = Vlad)
- [ ] E near Vlad opens dialogue; player cannot move while it is open
- [ ] Text types out; pressing E mid-type completes it instantly
- [ ] "[Show NFT Screenshot]" option is HIDDEN (you lack the item)
- [ ] Choosing options walks to follow-up nodes; the tree ends cleanly
- [ ] After closing, movement works again

## Battle (red square = Feral Segway Tourist)
- [ ] Touching it opens the battle screen
- [ ] Bash deals damage and the enemy hits back
- [ ] Roast Line costs 4 SP; refuses when SP is too low
- [ ] Item heals (after winning once, you carry a Lukewarm Kebab)
- [ ] Run sometimes flees, sometimes fails
- [ ] Winning shows XP/gold/drop and returns you to your plaza position
- [ ] Losing returns you with 1 HP (no crash)

## Save / Load
- [ ] Esc pauses; Resume unpauses
- [ ] Save shows "Saved!"; Quit to Title enables Continue
- [ ] Continue restores position, HP/SP/XP, gold, inventory, and flags
- [ ] Quit the app entirely, relaunch, Continue still works

## Data integrity
- [ ] `python Tools/validate_data.py` exits clean
- [ ] Breaking a JSON file on purpose makes the game fail LOUDLY at boot (then revert)
