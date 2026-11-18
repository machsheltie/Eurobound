# Handoff: Beads Deployment Team, `bd ready` triage (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned this one task: triage the `bd ready` queue so dead beads stop being dispatched. **Done. This window can be cleared.** Nothing is running.

## What was done

When the task started, `bd ready` listed 98 beads. While it ran, four of them left the queue because other windows changed them (c8xn, 1nwj, jmii, o2yv) and four new ones arrived (ioxj, nvif, rm6q, x3lw). Each of the 98 now in the queue was checked against its description, its comments, every Eurobound Desk card for it, the old bead-page `answers` collection, and the repo where needed.

| Case | Count | What changed |
|---|---|---|
| (a) truly agent-ready | 49 (2 of them epics) | Nothing. Every one already had `agent:` and `effort:` labels. |
| (b) needs the author | 15 | Set to blocked or deferred, with a waiting comment. One new Desk card. |
| (c) answer already in | 26 | A comment quoting the answer verbatim and naming the next action. Left open for dispatch. |
| (d) done or superseded | 5 | Closed, with the evidence in the reason. |
| Parked (waits on unbuilt work, not the author) | 3 | Deferred, with a reopen condition. |

### (b) needs the author: 15

- **New Desk card:** `Eurobound-jlzw-q1` (window "Production Desk Orchestrator", `relayed: false`). It asks who sets the rarity, sell value and drop chance for the 10 Golden Cutlet junk items. No card or bead had asked this before. The bead is blocked, has `author-ruling`, and has `metadata.ask`.
- **The author's own work (blocked):** p7n6.2 and p7n6.3, the Chadwick and Bradley rebuilds.
- **Waits on the author's first use (blocked):** nhxz.4, the Blender notes addon.
- **Waits on an existing open card (blocked):** objf waits on `Eurobound-p7n6.6-q5`. nvif was already blocked on `Eurobound-nvif-q1`.
- **Writers' Room jobs held by the OpenRouter top-up, Desk `Eurobound-xnpg-wr1` (blocked):** 40tc, 1n2u, lq6g, m6rc, y3r5 and nu0k. The `author-ruling` label came off 1n2u and lq6g, because their answers are in.
- **Deferred by the author until the items are generated:** it49, j45c and zf6e.

### Parked: 3

- ioe1 waits until beat-venue battles exist.
- iflo waits until Steam work starts.
- fjdk waits for a Shamsterdam food vendor scene. When one exists, ask the author which bro buys at a vendor.

### (d) closed: 5

- 9z3u: the author's picks are saved in `design/narrative/inspirations.md` and `design/style_guides/key_art_cover_and_loadscreens.md`.
- u5i: answered by `u5i-q1`, and the Writers' Room task was cancelled.
- nhxz.9: the cabinet trial was approved and merged at 1e403bf4.
- xvfg: the ids were merged and "Je mi 7!" was applied.
- 952g: the icons were promoted, but **not committed**.

### (c) answer in, next action on the bead: 26

9tz9, 04t2, f3tq, 7nbx, b10l, b8yo, wqui, dyez, 8snp, 028k, rras, du51, dg5p, ms3r, 4ynh, p1y, w5ra, w7nx, lei5, 9tb7, ysi, g40c, tcip, ezmn, 8ia and 64mz. ms3r already had a verbatim-answer and next-step comment, so nothing was added there. The `author-ruling` label came off 9tz9.

Notable findings:

- **f3tq:** all 14 drunk-rules answers are on the Desk, but none is in the ledger. The proposal still reads as unruled. Recording them is the next step.
- **7nbx:** the answer was never applied. The trigger line now lives at `design/quests/shamsterdam/great_doner_debate_shamsterdam.md:15`, because Eurobound-0xz split the file.
- **dyez:** the author was right that the Desk covered it (`ucpf-q13`, "Terminal Chaos"). What's left is the `centraal_station` ids in the tunnel JSONs and `voetgangerstunnel.md:146`.
- **Desk answers never acted on:** the author asked for these to go to the Desk ("send each / send options / send it with the diff"), and none was ever posted: w5ra, w7nx, 9tb7, lei5 and ysi.
- **64mz:** the author's answer on the velvet wristband icon ("Keep the shipped icon as is") conflicts with the later QC re-gate fail. The orchestrator should decide which stands.

## Ranked dispatch list (sent to the Production Desk Orchestrator)

Ranked on priority, value to the Debaucheryville slice, whether it unblocks other work, and size. The (a) and (c) beads are both dispatchable.

1. 9tz9 (c): make the Velvet Curtain Club data match the wristband docs.
2. 04t2 (c): dialogue consolidation. It unblocks rras and b8yo.
3. f3tq (c): put the 14 drunk-rules answers in the ledger.
4. 59b9, d4i6, pg9a, j9ru (a, P1): Arcade rework cut-outs, through the Asset team.
5. jpkw (a, P1): write the handoff format into `Tools/orchestrator/README.md`.
6. 7nbx, b10l, b8yo, wqui, dyez (c): small text and data fixes.
7. eaiq (a): final district diagram for approval.
8. spr0 (a): wire the approved Backpack Girl script.
9. 3ddh (a): Club Flyers quest JSON. The Quest Log format was ruled under wn1f.
10. z3ec (a): UI scale check at 1920x1080.
11. 8snp, 028k (c): follow-on proposals and numbers cards.
12. rras (c): apply the audit. Do it after 04t2.
13. du51 (c): redo the HUD badge trial.
14. dg5p (c): Vaněk repaint.
15. ms3r (c): shrink the joystick.
16. h9k1 (a): wet-T-shirt wardrobe plan on the Desk.
17. qfu (a): lowercase the git paths, as approved.
18. 0vsu (a): companion files, Shamsterdam first.
19. 4ynh (c): next Desk card (group 9).
20. p1y (c): Golden Cutlet venue doc.
21. Desk-posting jobs (c): w5ra, w7nx, lei5, 9tb7, ysi, g40c, tcip.
22. ezmn (c): PNG spec conversion.
23. 8ia (c): LFS track rules. Commit only on the author's ask.
24. 64mz (c): orchestrator call on the velvet wristband icon.
25. Quick (a) wins: ny6e, zaqu, wpb6, m1uo, 0161, 1nvh, aw81, 8b28, ioxj, rm6q, q9bw, jsd0.
26. Remaining (a), engine work: k3qa, 81oy, 7rdd, d7m1, j94r, 4med, 4jln, gora.
27. Remaining (a), art and docs: ssv5, iux4, sjoc, lyvh, koq3, w2ig, 1av7, 4nx3, zx7u, nven, xsw1, c5rq, 1d2b, 4akz (only files other windows have edited remain), x3lw.

Don't dispatch the epics nhxz and 31uj. They are containers.

## Synced and committed

- The bead page was synced once at the end (6 docs, then `sync_check.py --ack`).
- Nothing was committed in this task. The only file it adds is this handoff.
- Earlier in this window, at the author's request, the ledger entries were committed as d7bda677.

## Next for whoever takes the name

There is nothing left on this task. When `Eurobound-jlzw-q1` is answered, relay it to the bead, set the bead back to open, and remove `author-ruling`.
