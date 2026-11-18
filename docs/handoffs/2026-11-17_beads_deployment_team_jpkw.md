# Handoff: Beads Deployment Team, Eurobound-jpkw handoff format, mobile names and relay (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned one task: finish Eurobound-jpkw (P1). **Done. Bead closed. This window can be cleared.** Nothing is running.

## What was done

1. **Handoff format**, now in `Tools/orchestrator/README.md`, new section "Handoffs and window names". It is based on today's handoffs and covers:
   - the file path `docs/handoffs/<date>_<window_slug>_<task>.md`, with the window name first;
   - the sections: what was done, checks, committed/uncommitted with the file list, and open/next with the beads;
   - the rules: verbatim answers, no local paths, and a SendMessage to the orchestrator at the end.

   The intro of that README now points to the section.
2. **Mobile window names.** A claude-code-guide agent checked the docs (code.claude.com/docs/en/sessions.md, remote-control.md, cli-reference.md):
   - `/rename <name>` or `claude --name <name>` sets a session title, which the Claude app's Code tab and claude.ai/code show for Remote Control sessions.
   - The title survives a bare `/clear` (not `/clear <name>`).
   - Renaming from the app also renames it in the CLI (v2.1.221+).
   - No environment variable sets it.

   This is written into the README, along with the backstop that every handoff and cross-window message starts with the window name. Agents can't type slash commands, so the author has to do it: Desk card `beads-deployment-team-window-names-mobile` (window "Beads Deployment Team", `relayed: false`, no bead, non-blocking) asks whether they'll `/rename` each window.
3. **Relay.** The README now records:
   - the relay lives in the Production Desk Orchestrator window (a Desk watch with auto-replies, plus a :17/:47 fallback cron);
   - both are session-only, and the cron expires after 7 days;
   - a restart must re-arm the watch and the cron, then run one catch-up pass over answered/unrelayed questions and new playtest notes.
4. **Found and fixed in the same README:** the line "`hooks.py` ... is not installed" was stale. `pre-bash` and `post-bash` have been in `.claude/settings.json` since 2026-11-14, per `HOOKS_PROPOSAL.md`; the SessionStart check is still not installed.
5. jpkw is closed with the evidence, and the bead page is synced.

## Uncommitted (this task)

- `Tools/orchestrator/README.md`
- this handoff

## Next

When the author answers the window-names card, relay the answer. If they choose /rename, nothing else is needed from agents.
