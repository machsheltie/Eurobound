extends CanvasLayer

@onready var label = $PopupFrame/MessageLabel
@onready var close_button = $PopupFrame/CloseButton

func show_icq_message(sender: String, text: String, avatar_path: String):
    $PopupFrame/Avatar.texture = load(avatar_path)
    label.text = text
    $PopupSound.play()
    show()
    close_button.connect("pressed", Callable(self, "hide"))