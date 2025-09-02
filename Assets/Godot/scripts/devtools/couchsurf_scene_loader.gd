extends Node

@export var dialogue_controller: Node

func trigger_couchsurf_scene(npc_id: String):
    if dialogue_controller == null:
        push_error("DialogueController not assigned.")
        return

    var event = dialogue_controller.get_event_by_npc(npc_id)
    if event == {}:
        print("No couchsurfing event found for:", npc_id)
        return

    print("Triggering scene:", event.get("morning_scene", "???"))

    # You can insert visual scene change / choice prompt here
    # Example decision:
    if event.has("choice_outcome"):
        var simulate_choice := "success"  # or "fail"
        dialogue_controller.apply_outcome(npc_id, simulate_choice)
    else:
        dialogue_controller.apply_outcome(npc_id)
