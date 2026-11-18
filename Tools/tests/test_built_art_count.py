"""Tests for Tools/data_validation/built_art_count.py.
Run: python -I -m unittest discover -s Tools/tests -p test_built_art_count.py
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "built_art_count", REPO / "Tools" / "data_validation" / "built_art_count.py")
bac = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bac)

SUFFIX = bac.SPEC_SUFFIX


class BuiltArtCountTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._old_repo = bac.REPO
        bac.REPO = self.root
        specs = self.root / "design" / "worlds" / "debaucheryville" / "PNG_Assets"
        specs.mkdir(parents=True)
        for name in ("Absinthe_Arcade", "Absinthium_Taproom", "Bohemian_Trap",
                     "Euro_Ink_4_Less", "Nowhere_Yet"):
            (specs / f"{name}{SUFFIX}").write_text("spec", encoding="utf-8")
        art = self.root / "game" / "assets" / "worlds" / "debaucheryville"
        self._touch(art / "euro_ink_4_less" / "exterior", "a_ext_day.png", "a_ext_night.png",
                    "a_ext_day.png.import")
        self._touch(art / "euro_ink_4_less" / "interior", "a_int_day.png")
        self._touch(art / "the_bohemian_trap" / "exterior", "b_ext_day.png")
        self._touch(art / "absinthe_arcade" / "exterior" / "props", "p1.png", "p2.png")
        self._touch(art / "absinthe_arcade" / "interior" / "taproom", "t_day.png", "t_night.png")
        staged = art / "absinthe_arcade" / "interior" / "staged"
        self._touch(staged, ".gdignore", "s1.png")
        self._touch(staged / "deeper", "s2.png")
        self._touch(art / "orphan_place" / "exterior", "o.png")

    def tearDown(self):
        bac.REPO = self._old_repo
        self._tmp.cleanup()

    @staticmethod
    def _touch(folder: Path, *names: str) -> None:
        folder.mkdir(parents=True, exist_ok=True)
        for n in names:
            (folder / n).write_bytes(b"")

    def rows(self):
        result = bac.audit("debaucheryville")
        return {r["spec"][: -len(SUFFIX)]: r for r in result["rows"]}, result

    def test_built_art_ext_and_int_folders_counts_split_without_import_files(self):
        rows, _ = self.rows()
        r = rows["Euro_Ink_4_Less"]
        self.assertEqual((r["exterior"], r["interior"], r["total"]), (2, 1, 3))
        self.assertEqual(r["kind"], "ext+int")

    def test_built_art_the_prefixed_folder_matches_spec(self):
        rows, _ = self.rows()
        self.assertEqual(rows["Bohemian_Trap"]["total"], 1)
        self.assertEqual(rows["Bohemian_Trap"]["kind"], "ext only")

    def test_built_art_gdignore_folder_reported_staged_not_counted(self):
        rows, _ = self.rows()
        r = rows["Absinthe_Arcade"]
        self.assertEqual((r["exterior"], r["interior"], r["staged"]), (2, 2, 2))

    def test_built_art_side_room_spec_counts_arcade_subfolder(self):
        rows, _ = self.rows()
        r = rows["Absinthium_Taproom"]
        self.assertEqual((r["kind"], r["total"]), ("side room", 2))

    def test_built_art_missing_folder_is_none_and_orphan_listed(self):
        rows, result = self.rows()
        self.assertEqual(rows["Nowhere_Yet"]["kind"], "none")
        self.assertEqual(result["unmatched_folders"], ["orphan_place"])


if __name__ == "__main__":
    unittest.main()
