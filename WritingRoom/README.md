# The Writing Room

Four staff writers, run through OpenRouter, working together on tasks you assign.

| Writer | OpenRouter model |
|---|---|
| Kimi | `moonshotai/kimi-k3.1-pro` (default finalizer) |
| Gemini | `google/gemini-3.8-flash` |
| GLM | `z-ai/glm-5.3-flashx` |
| Aion | `aion-labs/aion-3.5` |

## Moderated mode (the normal way)

Claude moderates the room, and you work from your phone on the **Writers' Room desk**:
https://claude.ai/artifact/XHuswnv7SBHmWDwsSoADtD

- **Desk:** writers' questions arrive as cards, with yes/no or options and a comment box. At the end of every round, you get a review card and the final say.
- **Submit:** saves your answers and pings Claude, who delivers them to the room and runs the next round.
- **New tasks:** can be sent from the desk too.

Claude follows `MODERATOR.md`. The commands below still work if you want to run the room by hand without a moderator.

## Giving them a task (unmoderated)

From this folder (or double-click `room.bat` for a prompt):

```
python room.py go "Write 12 bartender barks for the Absinthe Arcade. Use design/templates/NPC_Profile_Template.md for anyone new."
```

That creates `tasks/<date>_<slug>/` and runs the room. Longer briefs: put them in a file and use
`python room.py new "Title" --brief-file my_brief.md`, then `python room.py run <task>`.

## How a task runs

1. **Rounds.** Each round, every writer takes a turn (the starting writer rotates). On a turn a writer can read anything in the Eurobound repo, search it (for example, to check a name isn't taken), write files inside the task folder, log questions for you, and vote on whether the work is done. Then they post to the shared thread, which the others read on their next turn.
2. **Round 1** pitches and splits the work. **Middle rounds** draft, give notes, and revise. **The last round** converges.
3. The task stops early when all four vote done in the same round. Then the **finalizer** (Kimi by default) writes `final.md`.

## What you read afterwards

| File | What it is |
|---|---|
| `final.md` | The deliverable |
| `thread.md` | The whole room conversation |
| `drafts/` | Each writer's working files |
| `questions_for_author.md` | Things only you can decide. The writers leave `[AUTHOR DECISION NEEDED]` gaps instead of inventing story. |
| `log.jsonl` | Every model call with token counts and cost |

## Steering them

```
python room.py note <task> "Aion's bartender is the keeper. Kill the rest of the pun names. More menace."
python room.py run <task> --rounds 2
```

Your note lands in the thread as **AUTHOR NOTE**, which outranks anything the room agreed. `<task>` can be any unique part of the folder name.

Other options:
- `--writers Kimi,GLM` runs only those writers.
- `--rounds N` sets the number of rounds (default 3).
- `--budget 1.50` caps spend in USD for that run (default $3). When the cap is hit, the room pauses; `run` again to continue.
- `python room.py status` lists every task, its state, and its spend.
- `python room.py ping` checks that all four writers answer.

## What they know

Every turn, each writer gets the following as their standing instructions:
- `bible/00_room_rules.md`, the house rules: how to collaborate, and never inventing story.
- The content, template, ask-the-author and canon sections of `.claude/CLAUDE.md`, read live, so your edits there reach them automatically.
- `design/narrative/Synopsis.md`, read live.
- The `eurobound-satire-voice` skill, read live from your Claude skills folder.

To give them more standing knowledge, drop another `.md` file into `bible/`. To swap a model, raise token limits or change the finalizer, edit `room_config.json`. You can write your audition notes on each writer in `writers/`.

## Setup notes

- The API key lives in `.env`, which is gitignored and never committed. The writers can't read it.
- Writers can write **only** inside their task folder. They can read anything in the repo except `.git` and `.env`.
- Python 3 standard library only, so nothing to install.
