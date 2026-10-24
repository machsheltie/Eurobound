# MIDI corruptor effect logic
func corrupt_midi(file):
    print("Corrupting MIDI: " + file)
    return file.replace(".mid", "_corrupted.mid")
