# aa_bible_cam solve and E1 checks

Scripts that solved `aa_bible_cam` from the daytime bible and that measure the model against it. Plain Python 3 with numpy and Pillow (`<venv python>`); none of them need Blender.

- `lines_bible.py` traces the bible's facade line features at full resolution into `lines_bible.json`, using `edges.py`.
- `solve_camera.py lines_bible.json` fits focal length, pitch, yaw and roll to the vertical and horizontal line families. The principal point is the image centre and the horizon is pinned at y=4000 (x=600). The result is `cam_solve.json`, scaled on the 4.4 m doorway with X=0 on the arch axis. It is copied into `manifest.json -> bible_camera`, and `../bible_camera.py` builds the camera from that.
- `bible_cam.py` is the solved camera as a pinhole in bible pixels: `proj`, `ray`, `to_plane_y`, `to_plane_x`.
- `residuals.py [--render r.png] [--out r.json] [--debug d.png]` reports model-vs-bible residuals per feature, in px at 5248 wide. The gate is 1% of the width.
- `compare.py overlay|side|edges` makes the comparison sheets.

`../publish_interfaces.py` writes `dev/aa_team/interfaces.json` from `manifest.json`.
