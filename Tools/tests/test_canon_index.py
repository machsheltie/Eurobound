"""Tests for Tools/canon_index/canon_index.py. Run: python -I -m unittest discover Tools/tests"""
import contextlib
import importlib.util
import io
import sqlite3
import tempfile
import types
import unittest
from pathlib import Path

import numpy as np

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


class _FakeModel:
    device = "fake"

    def encode(self, texts, normalize_embeddings=True):
        import numpy as np

        return np.array([[float(len(t) % 7), 1.0, 2.0] for t in texts], dtype=np.float32)


class InterruptedMatrixWriteTest(unittest.TestCase):
    """Eurobound-sfbn: a build that dies in write_matrix must be repaired by the next build."""

    def _build(self, **kw):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ci.cmd_build(types.SimpleNamespace(full=False, no_embed=False))
        return out.getvalue()

    def test_canon_index_failed_matrix_write_next_build_repairs_matrix(self):
        # Arrange: tiny corpus, fake embedder
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            root = Path(tmp)
            (root / "design").mkdir()
            doc = root / "design" / "a.md"
            doc.write_text("# A\n\nfirst canon line\n", encoding="utf-8")
            saved = (ci.ROOT, ci.DB_PATH, ci.source_files, ci.load_model, ci.write_matrix)
            ci.ROOT, ci.DB_PATH = root, root / "db" / "canon.db"
            ci.source_files = lambda: [doc]
            ci.load_model = lambda: _FakeModel()
            real_write = ci.write_matrix

            def dying_write(db):
                raise sqlite3.OperationalError("disk I/O error")

            try:
                # Act 1: first build embeds and commits chunks, then write_matrix dies
                ci.write_matrix = dying_write
                with self.assertRaises(sqlite3.OperationalError):
                    self._build()
                ci.write_matrix = real_write
                matrix, _ = ci.matrix_paths()
                self.assertFalse(matrix.exists())
                # Act 2: nothing changed on disk, yet the next build must repair the matrix
                self._build()
                db = ci.connect()
                n = db.execute("SELECT COUNT(*) FROM chunks WHERE emb IS NOT NULL").fetchone()[0]
                ids = np.load(ci.matrix_paths()[1])
                current = ci.matrix_is_current(db)
                # Act 3: a stale matrix (ids file torn / marker missing) is also detected and redone
                db.execute("DELETE FROM meta WHERE key='matrix_sig'")
                db.commit()
                self.assertFalse(ci.matrix_is_current(db))
                self._build()
                repaired = ci.matrix_is_current(db)
                db.close()
            finally:
                ci.ROOT, ci.DB_PATH, ci.source_files, ci.load_model, ci.write_matrix = saved
        # Assert
        self.assertGreater(n, 0)
        self.assertEqual(len(ids), n)
        self.assertTrue(current)
        self.assertTrue(repaired)


if __name__ == "__main__":
    unittest.main()
