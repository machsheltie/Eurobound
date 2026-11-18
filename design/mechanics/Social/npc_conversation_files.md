# NPC conversation files (the hand-in format)

Bead Eurobound-04t2. Author ruling 2026-11-15 (Desk 04t2-q1): the Arcade's talk box (`DialogueBox`) is the one talk box for the whole game; writers hand in each NPC's conversation as a data file, the way ICQ messages are handed in; the Dialogue Manager add-on is switched off.

This document is the format only. It says nothing about what any NPC says.

## Where a file goes

`game/assets/data/npcs/conversations/<npc_id>.json`, one file per NPC. `npc_id` is snake_case and must match the file name.

## Shape

Modelled on `icq_hotspot_messages.json`: a `_source` note, then records with an `id`, `lines`, flag lists and a `source`.

```json
{
  "_source": "where the writers' round is recorded",
  "npc_id": "snake_case_id",
  "speaker": "Name shown on the box",
  "start": "id of the first node",
  "nodes": [
    {
      "id": "node_id",
      "speaker": "optional, overrides the header for this node",
      "lines": ["one box per string, in order"],
      "set_flags": {"flag_id": true},
      "next": "node id, or omit/empty to end",
      "choices": [
        {"text": "option label", "next": "node id or empty to end",
         "requires_flags": ["all must be set"], "blocks_flags": ["none may be set"],
         "set_flags": {"flag_id": true}}
      ],
      "source": "design doc path:line"
    }
  ]
}
```

Rules:

- `lines` is one `DialogueBox.say(speaker, line)` call per string. At least one, none blank.
- A node ends the talk, goes to `next`, or offers `choices` (two or more; one choice is a `next`). Never both `next` and `choices`.
- `set_flags` is the ruled write shape (flag id to value, non-empty object), applied when the node is reached (node) or the choice is picked (choice).
- `requires_flags` and `blocks_flags` hide a choice, as in the ICQ queue.
- Every `next` and `start` names a node in the same file. Node ids are unique.
- Fields not listed here are kept by the reader in `extra` and ignored. Each new field needs an author ruling before the game acts on it. Items, currency and shop hooks are not part of this format yet.

## Code and checks

- Reader: `game/core/npc_conversation.gd` (`NpcConversation`). Reads and reports problems; repairs nothing. `DataRepo.get_dialogue_tree(npc_id)` returns its conversation, or `{}` with errors pushed when the file is missing or has problems. Nothing is loaded at startup, so an empty folder is fine.
- Validator: `Tools/validate_data.py`, `check_conversation`, runs on every file in that folder (same rules as the reader, plus the file name must match `npc_id`).
- Tests: `game/tests/unit/test_npc_conversation.gd`, with a placeholder fixture in `game/tests/fixtures/conversations/`.
- Walker: `game/core/conversation_walker.gd` (`ConversationWalker`, Eurobound-r1qf), tests in `game/tests/unit/test_conversation_walker.gd`. No NPC is wired to it yet.

## Switching off the Dialogue Manager add-on (reversible)

Removed from `game/project.godot`: the autoload `DialogueManager="*res://addons/dialogue_manager/dialogue_manager.gd"` and `res://addons/dialogue_manager/plugin.cfg` in `[editor_plugins] enabled`. The folder `game/addons/dialogue_manager/` stays. To switch it back on, re-add those two entries (or tick it in Project Settings > Plugins). Nothing outside the add-on referenced it.
