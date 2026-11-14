#!/usr/bin/env python3
"""Read the Claude Notes queue (notes sent from Blender by claude_notes.py).

  python Tools/blender_notes/list_notes.py                 pending notes, a few lines each
  python Tools/blender_notes/list_notes.py --all           pending and done
  python Tools/blender_notes/list_notes.py show <id>       one note in full (JSON)
  python Tools/blender_notes/list_notes.py done <id> -m "what was changed"
  python Tools/blender_notes/list_notes.py reopen <id>

<id> may be any unique part of the note id (the last 4 characters are enough).
Add --queue <folder> to read a queue somewhere else. Standard library only.
"""
import argparse
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_QUEUE = os.environ.get("CLAUDE_NOTES_QUEUE") or os.path.join(HERE, "queue")


def load(folder):
    notes = []
    if not os.path.isdir(folder):
        return notes
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(folder, name)
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError) as exc:
            print("! unreadable note %s: %s" % (path, exc), file=sys.stderr)
            continue
        data["_path"] = path
        notes.append(data)
    notes.sort(key=lambda n: (n.get("created", ""), n.get("id", "")))
    return notes


def fmt_vec(values):
    return "(" + ", ".join("%.3g" % v for v in values) + ")"


def describe_objects(note):
    parts = []
    for obj in note.get("objects", [])[:4]:
        sel = obj.get("selection")
        if sel:
            parts.append("%s [%d/%d faces, %d/%d verts]" % (
                obj["name"], sel["faces"]["count"], sel["faces"]["total"],
                sel["vertices"]["count"], sel["vertices"]["total"]))
        else:
            parts.append("%s (%s)" % (obj["name"], obj.get("type", "?")))
    extra = len(note.get("objects", [])) - 4 + note.get("objects_not_listed", 0)
    if extra > 0:
        parts.append("+%d more" % extra)
    return "; ".join(parts) if parts else "nothing selected (whole scene)"


def print_note(note, folder):
    flags = []
    if note.get("blend_path") is None:
        flags.append("FILE NEVER SAVED")
    elif note.get("blend_dirty") and not note.get("blend_saved_on_send"):
        flags.append("unsaved changes when sent: ids may not match the file on disk")
    status = "" if note.get("status") == "pending" else "  [%s]" % note.get("status")
    print("[%s] %s  %s%s" % (note["id"], note.get("created", "?")[:16].replace("T", " "),
                             note.get("mode", "?"), status))
    print("  note:  %s" % note.get("note", ""))
    print("  on:    %s" % describe_objects(note))
    print("  blend: %s%s" % (note.get("blend_path") or "(none)",
                           ("  !! " + "; ".join(flags)) if flags else ""))
    box = note.get("selection_bbox_world")
    shot = note.get("screenshot")
    shot_text = os.path.join(os.path.dirname(note["_path"]), shot).replace("\\", "/") if shot else "none"
    print("  bbox:  %s   screenshot: %s" % (
        ("%s to %s" % (fmt_vec(box["min"]), fmt_vec(box["max"]))) if box else "none", shot_text))
    if note.get("resolution"):
        print("  done:  %s" % note["resolution"])


def find(folder, needle, include_done):
    notes = load(folder)
    if include_done:
        notes += load(os.path.join(folder, "done"))
    hits = [n for n in notes if needle in n["id"]]
    if len(hits) != 1:
        sys.exit("%s notes match '%s'%s" % (
            "No" if not hits else len(hits), needle,
            "" if not hits else ": " + ", ".join(n["id"] for n in hits)))
    return hits[0]


def move(note, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    source = note.pop("_path")
    source_folder = os.path.dirname(source)
    target = os.path.join(target_folder, os.path.basename(source))
    temp = target + ".tmp"
    with open(temp, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(note, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    os.replace(temp, target)
    os.remove(source)
    shot = note.get("screenshot")
    if shot and os.path.isfile(os.path.join(source_folder, shot)):
        os.replace(os.path.join(source_folder, shot), os.path.join(target_folder, shot))
    return target


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Read the Claude Notes queue.")
    parser.add_argument("command", nargs="?", default="list", choices=["list", "show", "done", "reopen"])
    parser.add_argument("id", nargs="?")
    parser.add_argument("-m", "--message", default="", help="what was done (for 'done')")
    parser.add_argument("--all", action="store_true", help="also list finished notes")
    parser.add_argument("--queue", default=DEFAULT_QUEUE, help="queue folder (default: %(default)s)")
    args = parser.parse_args()
    folder = os.path.abspath(args.queue)
    done_folder = os.path.join(folder, "done")

    if args.command == "list":
        pending = load(folder)
        for note in pending:
            print_note(note, folder)
        if args.all:
            for note in load(done_folder):
                print_note(note, folder)
        print("%d pending note%s in %s" % (len(pending), "" if len(pending) == 1 else "s",
                                           folder.replace("\\", "/")))
        return

    if not args.id:
        parser.error("'%s' needs a note id" % args.command)

    if args.command == "show":
        note = find(folder, args.id, include_done=True)
        path = note.pop("_path")
        print(json.dumps(note, indent=1, ensure_ascii=False))
        print("# file: %s" % path.replace("\\", "/"))
    elif args.command == "done":
        note = find(folder, args.id, include_done=False)
        note["status"] = "done"
        note["done_at"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        note["resolution"] = args.message
        print("done: %s -> %s" % (note["id"], move(note, done_folder).replace("\\", "/")))
    elif args.command == "reopen":
        notes = [n for n in load(done_folder) if args.id in n["id"]]
        if len(notes) != 1:
            sys.exit("%d finished notes match '%s'" % (len(notes), args.id))
        note = notes[0]
        note["status"] = "pending"
        print("reopened: %s -> %s" % (note["id"], move(note, folder).replace("\\", "/")))


if __name__ == "__main__":
    main()
