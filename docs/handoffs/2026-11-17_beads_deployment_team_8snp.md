# Handoff: Beads Deployment Team, Eurobound-8snp rest points (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned one task: Eurobound-8snp, the rest points. **Done. This window can be cleared.** Nothing is running.

## What was done

1. **Build bead filed: Eurobound-vxa4** (open, gameplay-programmer, medium; discovered-from 8snp), for a cold reader. It builds the first rest point, the 12-Bed Mixed Dorm at Hostel "Midnight Checkout" at 12 SOVS (rule 15). Its description cites:
   - rules 10-16 of `docs/superpowers/specs/2026-11-15-rest-points-and-rules-proposal.md`;
   - `GameClock.rest` (`game/core/game_clock.gd:64`) and `rest_events.gd`;
   - save-at-the-bed through `SaveSystem.save_with_picker` (`save_system.gd:81`, rule 14, no autosave).

   Points it records:
   - **Paying:** booking pays through `GameState.can_afford` and `spend_sovs` (`game_state.gd:135, :139`), so it does NOT need the deferred shop runtime (Eurobound-it49).
   - **Restore:** stays blank or pending until N2 is ruled. N2 will be Desk card `Eurobound-8snp-q3`, posted after q2. "Groggy" (N5) is not applied.
   - **G4:** the hostel is not in the game. If no scene exists, build the booking, bed and rest logic plus tests first, with a stand-in, and ask the orchestrator for the art. The art follows the asset workflow; the Desk already has `asset-team-audit-hostel_midnight_checkout`.
   - **Lines:** they come only from the docs; any gap goes to the Desk.
2. **Desk card `Eurobound-8snp-q2`** (window "Beads Deployment Team", `relayed: false`) asks N1, the hostel prices. Options: the five rooms 12/16/20/28/45 SOVS (recommended: it is the detailed room table) or the three bookings 12/35/45 SOVS, or a note. Before posting, I checked the Desk: the only 8snp card was q1 (answered).
3. **Queue comment on 8snp** with N2-N7 and G1-G6, in order, with spec line refs and cross-links: N6 ties to p0j and p1jn, N7 may already be on 5kf4, G5 ties to w7nx, and G4 and G6 are not questions. One card at a time, ids q3 onward.
4. **8snp is blocked** with the comment "Waiting on Eurobound Desk Eurobound-8snp-q2: ...".
5. The bead page is synced.

## Uncommitted

Only this handoff.

## Next for whoever takes the name

When q2 is answered:
1. Relay it verbatim to 8snp.
2. Record it in the ledger.
3. Post N2 as `Eurobound-8snp-q3` from the queue comment. Eurobound-vxa4's restore waits on it.
