# Orchestrator notes (main session)
Board artifact: https://claude.ai/artifact/VL4cpwGqCj21sjVMBCMa4M  (source: dev/aa_team/aa_team_board.html, state helper desk_state.py)
On author Submit: page sends a comment to Claude ("AUTHOR SUBMITTED ANSWERS ...") then republishes itself. Before any local republish, Artifact read the live page and merge (author answers live in the page state).
Agents (SendMessage ids):
- mason  E1 STOPPED 2026-10-29 (stalled after Blender crash). mason-2 E1 opus/xhigh a909da4189adc338d (headless)
- glazier E2 opus/high  a3b9b51734db89edf  (headless, Tripo/Chrome allowed)
- neon   E3 opus/high   abcba08881365f9a7  (headless)
E4 -> neon (opus high) 2026-10-29. Queued: E5 mural+surface (opus high), E6 street kit (sonnet high)
Question routing: Q-001 mason, Q-002 glazier, Q-003/Q-004 E5, Q-005/Q-006 E6.
Gallery: upload compare PNGs with Artifact publish asset:true url=<board>, add to state.gallery {element,title,url,caption,date}.
Author answers 2026-10-28 20:36: Q-001 A (mansard per sheet) -> mason; Q-002 A sash stands -> glazier (glazing split re-asked as Q-009);
Q-003 B (procedural peeling shader = starting layer, author corrects by hand); Q-004 mural source = references/Exterior/muralreference.png (panel 1 clean artwork; Q-010 asks fit/upscale);
Q-005 B (corner sign reads TOKENS / REGRETS); Q-006 A (Clocktower Plaza sign IN, on Arcade left corner).
Author note: references/Exterior/texture.jpg (1254px seamless peeling limestone) is THE main building texture -> E5.
Dormer windows added to glazier scope.
