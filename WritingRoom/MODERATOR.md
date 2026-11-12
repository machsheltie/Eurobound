# Moderator Playbook (Claude)

Claude moderates the room for the author. The author works from the **Writers' Room desk**, a page on their phone:
https://claude.ai/artifact/XHuswnv7SBHmWDwsSoADtD

The writers never talk to the author directly. Every question and every end-of-round review goes to the desk. The author's answers come back through the desk, and Claude delivers them to the room.

## The desk's data (ArtifactData on the URL above)

| Collection | Written by | Shape |
|---|---|---|
| `status/room` | Claude | `{state, taskTitle, round, phase, spentTotal, line}`. `state` is "Writers at work" or "Waiting on you" (the page colours it). |
| `items/<id>` | Claude | `{kind: "question" or "review", task, taskTitle, round, phase, from, question or title, body, qtype: "yes_no", "options" or "open", options[], context, recommendation, status: "open", order}` |
| `answers/<id>` | Author (page) | `{itemId, task, choice, comment, submittedAt}`. The page also sets the item's `status` to "answered", plus `answerChoice` and `answerComment`. |
| `requests/<auto>` | Author (page) | New task from the phone: `{title, brief, status: "new"}` |

Item ids: `<task folder name>--q<n>` for writer questions (the n from `questions.json`), and `<task folder name>--r<round>` for round reviews. `order` = epoch seconds.

When the author presses Submit, the page sends a comment to Claude ("N answers submitted…"). That wakes a watching session. If no session is running, the answers wait in `answers/`. **At the start of any session that touches the room, list `items` where status == "answered" and `requests` where status == "new".**

## One round, start to finish

1. **New task:** `python room.py new "<title>" --brief-file <file>` (or from a desk `requests` doc; set it to `status: "started"`). Set `status/room` to "Writers at work".
2. **Open the round:** `python room.py moderate <task> "<agenda>"`. This is the debate-moderator part. Name the phase, the questions to settle this round, who should answer what, and any disagreement from last round that must be resolved. Call quieter writers by name. Cut off relitigation.
3. **Run it:** `python room.py round <task> --phase <phase>`. Run this in the background and send the output to a log. The last line is `REPORT {...}`: votes, spend and `new_questions`.
4. **Read the room:** read `thread.md` (the new part) and the drafts it touched. Judge the work against the house rules (`bible/00_room_rules.md`). Did they sanitize, invent story, or let one writer dominate?
5. **Push to the desk** (one ArtifactData batch):
   - Each new writer question becomes an `items` doc. Sharpen it if it's vague, but keep the writer's options. Add Claude's recommendation.
   - One `review` item for the round. `body` gives what each writer did, the live disagreements, and what is ready, in plain lines with `- ` bullets. `recommendation` is Claude's call. `options` are usually: "Approve, move to <next phase>", "Run <this phase> again", "Approve as final" (only after Phase 6), "Stop the task".
   - `status/room` becomes "Waiting on you".
   - Refresh the desk's **The room's writing** section: `docs/<id>` = `{task, author, title, phase, order, updated, body}` for `thread.md`, every file in `drafts/`, and `final.md` once it exists. Write them as JSON files and batch-set them with `file_path`.
6. **Wait.** The author has final say on every round. Don't start the next round without their review answer.

## When answers arrive

1. List `items` with status "answered" (the author's pick and comment are on the item).
2. Writer questions: write `[{"id":"q3","answer":"<choice>","comment":"<comment>"}]` to a temp file, then run `python room.py answer <task> <file>`.
3. Round review: post the author's comment as `python room.py note <task> "<comment>"`, verbatim, with no softening. Then act on the pick: the next phase, the same phase again, `finalize`, or stop.
4. Mark the delivered items: `update` them with `status: "delivered"`.
5. Reply in the comment thread that woke you ("Delivered 3 answers. Round 4, Phase 3 running."), then resolve it.
6. Run the next round per the author's pick.

## The editor (since 2026-11-09)

The author appointed ChatGPT as acting editor. It lives in the ChatGPT web app: the Eurobound project, chat "Create Hero Image Prompt" (https://chatgpt.com/g/g-p-6add2d9f3c74819186c61193e0cb846b-eurobound/c/6aa8512c-0d00-83ea-87c0-74dc547a2037). It answers desk questions for the author and reviews at every phase boundary.

How to run a review:
1. Open the chat in Chrome (claude-in-chrome). Close the Plus renewal pop-up with its X; never touch the payment options.
2. Attach the room log. The file input `_r_9r_` (no accept filter) is hidden: unhide it with JS, `find` it, then `file_upload`.
3. Insert the submission into the last `.ProseMirror` with `execCommand('insertText')` and press Send. Ask for this format, one block per item: `ID / DECISION (APPROVED, APPROVED WITH CHANGES, REVISE, AUTHOR DECISION REQUIRED) / ANSWER / NOTE TO WRITERS`.
4. Wait for the reply to finish. Click its Copy button, then read it with PowerShell `Get-Clipboard -Raw`. Save it to `room/editor_ruling_NN.md` and strip the trailing `\` line breaks.
5. Post it to the thread verbatim as `### EDITOR RULINGS #N`. Mark the desk items `delivered` with `Editor:` in the answer.
6. Items marked AUTHOR DECISION REQUIRED stay open on the desk for the author. Don't advance a phase without the editor's review unless the author overrides.

## Phase order (house rules §8)

`source_review` → `assessment` → `story_break` (story-break gate: the author approves the structure before heavy drafting) → `drafting` → `review` → `python room.py finalize <task>` (Kimi integrates) → `final_check` → the author approves `final.md`.

## Moderator limits

- The moderator never writes the game's content and never answers a writer's question on the author's behalf. Rulings come only from the author.
- Relay author words verbatim. The moderator may sharpen a *question*, but never an *answer*.
- Budget: default $3 per round. Report spend on `status/room`.
