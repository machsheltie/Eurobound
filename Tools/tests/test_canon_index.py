"""Tests for Tools/canon_index/canon_index.py. Run: python -I -m unittest discover Tools/tests"""
import contextlib
import importlib.util
import io
import tempfile
import types
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("canon_index", REPO / "Tools" / "canon_index" / "canon_index.py")
ci = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ci)


class BuildSkipTest(unittest.TestCase):
    def test_build_vanished_file_is_skipped_with_warning(self):
        # Arrange: one good file and one listed file that does not exist
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            root = Path(tmp)
            (root / "design").mkdir()
            good = root / "design" / "good.md"
            good.write_text("# Good\n\nhello canon\n", encoding="utf-8")
            ghost = root / "design" / "ghost.md"
            saved = (ci.ROOT, ci.DB_PATH, ci.source_files)
            ci.ROOT, ci.DB_PATH = root, root / "db" / "canon.db"
            ci.source_files = lambda: [good, ghost]
            out, err = io.StringIO(), io.StringIO()
            try:
                # Act
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    ci.cmd_build(types.SimpleNamespace(full=True, no_embed=True))
                db = ci.connect()
                paths = {r[0] for r in db.execute("SELECT path FROM files")}
                db.close()
            finally:
                ci.ROOT, ci.DB_PATH, ci.source_files = saved
        # Assert
        self.assertEqual(paths, {"design/good.md"})
        self.assertEqual(err.getvalue().count("warning: skipped design/ghost.md"), 1)


if __name__ == "__main__":
    unittest.main()
