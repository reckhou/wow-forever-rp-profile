"""Tests for scripts/build_spoken_lore.py, with a made-up Spoken data tree (no real game data)."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import build_spoken_lore as lore  # noqa: E402


class KeyTest(unittest.TestCase):
    def test_normalise_key_matches_spokens_rule(self):
        self.assertEqual(lore.normalise_key("The Bulwark"), "bulwark")
        self.assertEqual(lore.normalise_key("Sen'jin Village"), "senjin village")
        self.assertEqual(lore.normalise_key("Zul’Farrak"), "zulfarrak")

    def test_slug(self):
        self.assertEqual(lore.slug("Onyxia's Lair"), "onyxias-lair")
        self.assertEqual(lore.slug("Excavation Site: Wetlands"), "excavation-site-wetlands")
        self.assertEqual(lore.slug("The Barrens"), "the-barrens")


class ForeverFilterTest(unittest.TestCase):
    def setUp(self):
        self.names, self.renamed, self.blocked = lore.forever_filter(
            ["Durotar", "The Crossroads", "Legashi Encampment"],
            {"renamed": {"legashi encampment": {"key": "legash encampment", "why": "x"}},
             "notOnForever": {"1447": {"storm cliffs": "instance only"}}})

    def test_area_in_the_table_is_enabled(self):
        self.assertTrue(lore.in_forever("crossroads", 1413, self.names, self.renamed, self.blocked))

    def test_area_missing_from_the_table_is_not(self):
        self.assertFalse(lore.in_forever("moonbrook", 1436, self.names, self.renamed, self.blocked))

    def test_renamed_place_is_kept_under_its_old_key(self):
        self.assertTrue(lore.in_forever("legash encampment", 1447, self.names, self.renamed, self.blocked))

    def test_place_no_player_can_reach_is_not(self):
        names = self.names | {"storm cliffs"}
        self.assertFalse(lore.in_forever("storm cliffs", 1447, names, self.renamed, self.blocked))


ZONES = """local _, SpokenPlaces = ...
if not SpokenPlaces:ShouldLoadLanguage("enUS") then return end
local zones = {
  [1411] = { name = "Durotar", short = "Red land.", full = "Red land. Orcs live here.", source = "https://x/Durotar" },
  [947] = { name = "Azeroth", short = "World.", full = "World.", source = "https://x/Azeroth" },
  [2521] = { pending = true, name = "Zephras Isle", short = "", full = "", source = "" },
}
SpokenPlaces:RegisterLoreData("enUS", "zones", zones)
"""
SUBZONES = """local _, SpokenPlaces = ...
local subzones = {
  [1411] = {
    ["valley of trials"] = { name = "Valley of Trials", short = "Start.", full = "Start. Trials.", source = "https://x/Valley" },
    ["lost cove"] = { name = "Lost Cove", short = "Gone.", full = "Gone.", source = "https://x/Cove" },
    ["empty place"] = { pending = true, name = "Empty Place", short = "", full = "", source = "" },
  },
}
SpokenPlaces:RegisterLoreData("enUS", "subzones", subzones)
"""
DUNGEONS = """SpokenDungeons = { version = 1, dungeons = {
  [36] = { zone = 1411, story = { 1411, "valley of trials" }, "Made-up Mines" },
} }
"""
BOSSES = """SpokenBosses = { version = 1, maps = {
  [36] = {
    { id = 1, ids = { 1 }, key = "old grimtusk", "Old Grimtusk" },
    { id = 2, ids = { 2 }, key = "silent one", "Silent One" },
  },
} }
"""
STORIES = """SpokenBossStories = SpokenBossStories or {}
for map, stories in pairs({
  [36] = { ["old grimtusk"] = { "Grimtusk was a boar.", deDE = "Ein Eber." } },
}) do SpokenBossStories[map] = stories end
"""


def make_tree(root):
    root = Path(root)
    places = root / "addons" / "Spoken_Places" / "Data" / "enUS"
    places.mkdir(parents=True)
    (places / "Zones.lua").write_text(ZONES, encoding="utf-8")
    (places / "Subzones.lua").write_text(SUBZONES, encoding="utf-8")
    (root / "addons" / "Spoken" / "Data").mkdir(parents=True)
    (root / "addons" / "Spoken" / "Data" / "Dungeons.lua").write_text(DUNGEONS, encoding="utf-8")
    (root / "addons" / "Spoken_Bosses" / "Data").mkdir(parents=True)
    (root / "addons" / "Spoken_Bosses" / "Data" / "Bosses.lua").write_text(BOSSES, encoding="utf-8")
    (root / "addons" / "Spoken_Bosses" / "Data" / "Stories.lua").write_text(STORIES, encoding="utf-8")
    seed = root / "pipelines" / "places" / "tools" / "seed"
    seed.mkdir(parents=True)
    (seed / "camelot-areas.json").write_text(json.dumps(
        {"build": "1.0.0.1", "names": ["Durotar", "Valley of Trials", "Empty Place"]}), encoding="utf-8")
    (seed / "forever-places.json").write_text(json.dumps({"renamed": {}, "notOnForever": {}}), encoding="utf-8")


class BuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        make_tree(Path(cls.tmp.name) / "spoken")
        cls.out = Path(cls.tmp.name) / "lore"
        cls.report = lore.build(Path(cls.tmp.name) / "spoken", cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_world_maps_go_to_the_world_file_not_a_zone_file(self):
        text = (self.out / "world.md").read_text(encoding="utf-8")
        self.assertIn("## Azeroth", text)
        self.assertIn("World.", text)
        self.assertIn("CC BY-SA 4.0", text)
        self.assertEqual(self.report["world_written"], ["Azeroth"])

    def test_only_forever_zones_with_text_get_a_file(self):
        self.assertTrue((self.out / "zones" / "durotar.md").exists())
        self.assertFalse((self.out / "zones" / "azeroth.md").exists())  # not an area Forever's table names
        self.assertFalse((self.out / "zones" / "zephras-isle.md").exists())  # no lore text yet

    def test_zone_file_holds_overview_and_enabled_subzones_only(self):
        text = (self.out / "zones" / "durotar.md").read_text(encoding="utf-8")
        self.assertIn("# Durotar", text)
        self.assertIn("Red land. Orcs live here.", text)
        self.assertIn("## Valley of Trials", text)
        self.assertNotIn("Lost Cove", text)  # not in Forever's table
        self.assertNotIn("Empty Place", text)  # no text
        self.assertIn("CC BY-SA 4.0", text)
        self.assertIn("https://x/Valley", text)

    def test_dungeon_file_lists_its_bosses_and_story(self):
        text = (self.out / "zones" / "made-up-mines.md").read_text(encoding="utf-8")
        self.assertIn("1. Old Grimtusk", text)
        self.assertIn("2. Silent One", text)
        self.assertIn("Start. Trials.", text)
        self.assertIn("bosses/made-up-mines", text)

    def test_each_boss_with_a_story_gets_its_own_file(self):
        text = (self.out / "bosses" / "made-up-mines" / "old-grimtusk.md").read_text(encoding="utf-8")
        self.assertIn("number 1 of 2", text)
        self.assertIn("Grimtusk was a boar.", text)
        self.assertNotIn("Eber", text)  # only the English story
        self.assertFalse((self.out / "bosses" / "made-up-mines" / "silent-one.md").exists())
        self.assertEqual(self.report["boss_no_story"], ["Made-up Mines: Silent One"])

    def test_manifest_and_attribution(self):
        self.assertIn("Silent One", (self.out / "MANIFEST.md").read_text(encoding="utf-8"))
        self.assertIn("share-alike", (self.out / "ATTRIBUTION.md").read_text(encoding="utf-8"))

    def test_a_clashing_file_name_stops_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_tree(Path(tmp) / "spoken")
            path = Path(tmp) / "spoken" / "addons" / "Spoken" / "Data" / "Dungeons.lua"
            path.write_text(DUNGEONS.replace("Made-up Mines", "Durotar"), encoding="utf-8")
            with self.assertRaises(SystemExit):
                lore.build(Path(tmp) / "spoken", Path(tmp) / "lore")


if __name__ == "__main__":
    unittest.main()
