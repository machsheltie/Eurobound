# Handoff: Writing Room, Desk cards for seven triaged beads (2026-11-17)

**Window name: Writing Room** (formerly eurobound-2b; it moderates `WritingRoom/`). Task, assigned by the Production Desk Orchestrator: post Desk cards for Eurobound-w5ra, w7nx, lei5, 9tb7, ysi, g40c and tcip. Source: `docs/handoffs/2026-11-17_beads_deployment_team_ready_triage.md`. **Done. This window can be cleared.** Nothing is running.

## The key finding

The author had already answered every one of the seven beads on the old bead page (2026-11-12 to 11-16). A card asking "how do you want this handled" would make them answer twice. So a card went up only where the author's answer asked for one. For the rest, the bead now records why no card was posted.

## Posted (window "Writing Room", `relayed: false`)

| Desk doc | Bead | What it asks |
|---|---|---|
| Eurobound-w5ra-q1 | w5ra | The Hemp Museum's alternative name, which is the real museum's (`the_hemp_museum.md:9`) |
| Eurobound-w5ra-q2 | w5ra | "El Aviva" in Big Wim's kapsalon story (`npc_big_wim.md:105`, `kapsalon_koning.md:302`) |
| Eurobound-w5ra-q3 | w5ra | "Nataniël Gomes", a real private person (`npc_big_wim.md:69`, `:105`, `:269`, `:462`) |
| Eurobound-w7nx-q1 | w7nx | Retire, rebuild or leave the stale Couchsurfing engine file. The card carries the diff the author asked for. |

### Notes on the posted cards

- **w5ra:**
  - The author said "Send each to me at the Desk", so the leftovers went up as three cards, one per real name.
  - The GGD decal and the "Oranje Editie" condoms are already gone, so they got no card.
  - Mechanical cleanup is still open on the bead and needs no author: the Proeflokaal residue in the economy spec at `:180`, the two real-place PNG filenames in `stroopwafel_cart.md:349-350`, and the stale WILHELMUS note at `npc_big_wim.md:456`.
- **w7nx:**
  - The bead's description was partly wrong. The Vanessa crystal quiz and the lost 25 SOVS are still in the current design.
  - What is really stale: SP where the design now says Bravado, the trigger and flags for failing the quiz, no four-state routing, and no Renata.

## Not posted, and why

- **lei5, 9tb7, ysi, g40c:** the author already asked for drafted options. Examples: ysi, "give me some options to choose from please"; 9tb7, "send options".
  - Drafting is the room's job, so they joined the room's OpenRouter batch, which waits on Desk `xnpg-wr1`. The batch is listed in `docs/handoffs/2026-11-15_eurobound_2b.md`.
  - All four are blocked, each with a comment saying this.
- **tcip:** the author answered "Keep both; run the intoxication-law review and interview me for the numbers".
  - The next step is game-designer work: run the 10-point review in `design/mechanics/intoxication_law.md` on Foam Fighter, and write both docs from `design/templates/` with every number PENDING.
  - Only after that do the number questions go to the Desk. Left open for dispatch, with a comment.

## Done

- w5ra and w7nx are blocked, each with a "Waiting on Eurobound Desk" comment.
- The bead page is synced and acked.

## Uncommitted (this task)

```
docs/handoffs/2026-11-17_writing_room_desk_cards.md
docs/handoffs/2026-11-15_eurobound_2b.md   (queued-batch list extended)
```

Commit only when the author asks.
