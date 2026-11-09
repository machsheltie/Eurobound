extends Node

class_name DialogueController

var event_data = {}
var completed_flags := {}

func load_events_from_file(path: String):
    var file = FileAccess.open(path, FileAccess.READ)
    event_data = JSON.parse_string(file.get_as_text())
    file.close()

func get_event_by_npc(npc_id: String) -> Dictionary:
    for entry in event_data:
        if entry.has("npc_id") and entry["npc_id"] == npc_id:
            return entry
    return {}

func apply_outcome(npc_id: String, choice: String = "") -> void:
    var event = get_event_by_npc(npc_id)
    if event == {}:
        return

    var result = {}
    if event.has("choice_outcome") and choice != "":
        if choice == "success":
            result = event["choice_outcome"]["success"]
        else:
            result = event["choice_outcome"]["fail"]
    elif event.has("outcome"):
        result = event["outcome"]

    if result.has("effect"):
        print("Effect applied:", result["effect"])

    if result.has("flag"):
        completed_flags[result["flag"]] = true
