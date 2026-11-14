# Installs (or updates) the Claude Notes addon into Blender and points it at this
# repo's queue folder. Run with Blender closed:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background --python Tools/blender_notes/install_addon.py
#
# or double-click install.bat in this folder.
import os
import sys

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE = "claude_notes"
QUEUE = os.path.join(HERE, "queue")


def main():
    bpy.ops.preferences.addon_install(filepath=os.path.join(HERE, MODULE + ".py"), overwrite=True)
    bpy.ops.preferences.addon_enable(module=MODULE)
    addon = bpy.context.preferences.addons.get(MODULE)
    if addon is None:
        print("CLAUDE_NOTES_INSTALL: FAILED (addon did not enable)")
        sys.exit(1)
    addon.preferences.queue_dir = QUEUE
    os.makedirs(QUEUE, exist_ok=True)
    bpy.ops.wm.save_userpref()
    print("CLAUDE_NOTES_INSTALL: OK, Blender %s, queue %s" % (bpy.app.version_string, QUEUE))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("CLAUDE_NOTES_INSTALL: FAILED (%s)" % exc)
        sys.exit(1)
