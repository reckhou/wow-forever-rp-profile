"""Build the skill's lore folder (zones and bosses, one Markdown file each) from the Spoken add-on's data.

Abbreviations: AI = artificial intelligence; CC BY-SA = Creative Commons Attribution-ShareAlike licence;
Forever = World of Warcraft: Forever; Lupa = the Python binding to Lua used here to read Spoken's data files.

Usage (from the project root):
    python -I scripts/build_spoken_lore.py --spoken private-local/spoken-wow --out references/lore

Input: a clone of https://github.com/rusty-key/spoken-wow (data files only are read; they are Lua tables).
  addons/Spoken_Places/Data/enUS/Zones.lua and Subzones.lua   zone and subzone lore
  addons/Spoken_Bosses/Data/Bosses.lua and Stories.lua        boss names (in Forever's order) and stories
  addons/Spoken/Data/Dungeons.lua                             dungeon names and the place that tells their story
  pipelines/places/tools/seed/camelot-areas.json              every area name Forever's client can report (its AreaTable)
  pipelines/places/tools/seed/forever-places.json             Forever's renamed places and places no player can reach
Output (under --out):
  world.md                         Azeroth, Kalimdor and Eastern Kingdoms
  zones/<zone-slug>.md             one file per zone, or dungeon, that Forever has and that has lore text
  bosses/<dungeon-slug>/<boss-slug>.md   one file per boss that has a story
  ATTRIBUTION.md                   licence and credit
  MANIFEST.md                      what was written and what was left out, and why
A zone, subzone or boss is kept only when it is enabled in Forever, which here means Forever's own AreaTable names it.
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(f"private-local/tools-py{sys.version_info.major}{sys.version_info.minor}")))

# The world and the two great continents are not areas, so Forever's AreaTable does not name them. They go into one
# file, world.md.
WORLD_MAPS = (947, 1414, 1415)  # Azeroth, Kalimdor, Eastern Kingdoms
LICENCE_LINE = "Text adapted from Warcraft Wiki (CC BY-SA 4.0), through the Spoken add-on's data (MIT)."
BUILD_NOTE = "Which places exist in Forever: its AreaTable, build {build}."


def normalise_key(text):
    """Spoken's area key: lower case, apostrophes dropped, a leading 'the' dropped, other runs made one space."""
    text = text.lower().replace("'", "").replace("’", "")
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    return re.sub(r"^the ", "", text)


def slug(text):
    """File name stem for a place or boss. The RPMaster app makes the same slug from a name, so a change here breaks it."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower().replace("'", "").replace("’", "")).strip("-")


def forever_filter(area_names, places):
    """Return (names, renamed, not_on_forever). names: normalised AreaTable names of Forever.
    renamed: key the lore keeps -> True when Forever's own spelling is in the table.
    not_on_forever: {uiMapID: {key, ...}} of places the lore lists that no Forever player can reach."""
    names = {normalise_key(n) for n in area_names}
    renamed = {}
    for forever_spelling, info in places.get("renamed", {}).items():
        if normalise_key(forever_spelling) in names:
            renamed[info["key"]] = info.get("why", "")
    blocked = {int(m): set(keys) for m, keys in places.get("notOnForever", {}).items()}
    return names, renamed, blocked


def in_forever(key, map_id, names, renamed, blocked):
    if key in blocked.get(map_id, set()):
        return False
    return key in names or key in renamed


def lua_to_python(value):
    """Plain Python for a Lua table: an array part [1], [2]... and a dict part."""
    if hasattr(value, "items"):
        out = {}
        for k, v in value.items():
            out[k if not isinstance(k, float) else int(k)] = lua_to_python(v)
        return out
    return value


def as_list(table):
    """The array part of a converted Lua table, in order."""
    return [table[k] for k in sorted(k for k in table if isinstance(k, int))]


def load_lua_data(path, runtime_cls, namespace_name):
    """Run a Spoken data file with no operating system or file access. Returns (namespace table, globals)."""
    lua = runtime_cls(register_eval=False, register_builtins=False)
    lua.execute("local compile = loadstring; function __run(code, ...) return assert(compile(code, '=data'))(...) end")
    for name in ("os", "io", "package", "dofile", "loadfile", "require", "debug"):
        lua.execute(f"{name} = nil")
    captured = {}

    def register(_self, language, kind, data):
        captured[(language, kind)] = lua_to_python(data)

    namespace = lua.eval("{}")
    namespace["ShouldLoadLanguage"] = lambda _self, language: True
    namespace["RegisterLoreData"] = register
    code = Path(path).read_text(encoding="utf-8")
    lua.globals().__run(code, namespace_name, namespace)
    return captured, lua.globals()


def read_places(spoken):
    from lupa.lua51 import LuaRuntime
    base = Path(spoken) / "addons" / "Spoken_Places" / "Data" / "enUS"
    zones = load_lua_data(base / "Zones.lua", LuaRuntime, "Spoken_Places")[0][("enUS", "zones")]
    subzones = load_lua_data(base / "Subzones.lua", LuaRuntime, "Spoken_Places")[0][("enUS", "subzones")]
    return {int(k): v for k, v in zones.items()}, {int(k): v for k, v in subzones.items()}


def read_global(path, global_name):
    from lupa.lua51 import LuaRuntime
    return lua_to_python(load_lua_data(path, LuaRuntime, "Spoken")[1][global_name])


def text_of(entry):
    """The lore text of a zone or subzone entry, or '' when it is only a placeholder."""
    if entry.get("pending"):
        return ""
    return (entry.get("full") or entry.get("short") or "").strip()


def render_zone(zone_name, zone_entry, subs, dungeon_bosses=None, dungeon_path=None):
    """Markdown for one zone: its overview, then one section for each enabled subzone."""
    out = [f"# {zone_name}", ""]
    if dungeon_path:
        out += [f"This is a dungeon or raid. Its bosses each have a file under `{dungeon_path}`.", ""]
    zone_text = text_of(zone_entry) if zone_entry else ""
    if zone_text:
        out += [zone_text, ""]
    for name, entry in subs:
        out += [f"## {name}", "", text_of(entry), ""]
    if dungeon_bosses:
        out += ["## Bosses, in Forever's order", ""]
        out += [f"{i}. {b}" for i, b in enumerate(dungeon_bosses, 1)]
        out += [""]
    out += ["---", LICENCE_LINE]
    sources = sorted({e.get("source") for e in ([zone_entry] if zone_entry else []) + [s for _, s in subs] if e and e.get("source")})
    if sources:
        out += ["Sources: " + ", ".join(sources)]
    return "\n".join(out) + "\n"


def render_world(entries):
    """Markdown for the world file: one section for each world map that has text."""
    out = []
    sources = []
    for name, entry in entries:
        out += [f"## {name}", "", text_of(entry), ""]
        if entry.get("source"):
            sources.append(entry["source"])
    out += ["---", LICENCE_LINE, "Sources: " + ", ".join(sorted(sources))]
    return "\n".join(out) + "\n"


def render_boss(boss_name, dungeon_name, order, total, story):
    return "\n".join([f"# {boss_name}", "", f"A boss of {dungeon_name}, number {order} of {total} in Forever's order.", "",
                      story.strip(), "", "---", LICENCE_LINE, ""])


def build(spoken, out_dir):
    spoken = Path(spoken)
    seed = spoken / "pipelines" / "places" / "tools" / "seed"
    camelot = json.loads((seed / "camelot-areas.json").read_text(encoding="utf-8"))
    places = json.loads((seed / "forever-places.json").read_text(encoding="utf-8"))
    names, renamed, blocked = forever_filter(camelot["names"], places)
    zones, subzones = read_places(spoken)
    dungeons = read_global(spoken / "addons" / "Spoken" / "Data" / "Dungeons.lua", "SpokenDungeons")["dungeons"]
    bosses = read_global(spoken / "addons" / "Spoken_Bosses" / "Data" / "Bosses.lua", "SpokenBosses")["maps"]
    stories = read_global(spoken / "addons" / "Spoken_Bosses" / "Data" / "Stories.lua", "SpokenBossStories")

    out_dir = Path(out_dir)
    for sub in ("zones", "bosses"):
        shutil.rmtree(out_dir / sub, ignore_errors=True)
        (out_dir / sub).mkdir(parents=True, exist_ok=True)
    report = {"world_written": [], "zones_written": [], "zones_not_forever": [], "zones_no_text": [], "subz_total": 0, "subz_written": 0,
              "subz_not_forever": [], "subz_no_text": 0, "dungeon_files": [], "boss_files": 0, "boss_no_story": []}
    used_slugs = {}

    def claim(file_slug, label):
        if file_slug in used_slugs:
            raise SystemExit(f"Two lore files want the name '{file_slug}': {used_slugs[file_slug]} and {label}")
        used_slugs[file_slug] = label

    world_entries = []
    for map_id in WORLD_MAPS:
        if map_id in zones and text_of(zones[map_id]):
            world_entries.append((zones[map_id]["name"], zones[map_id]))
            report["world_written"].append(zones[map_id]["name"])
    (out_dir / "world.md").unlink(missing_ok=True)
    if world_entries:
        (out_dir / "world.md").write_text(render_world(world_entries), encoding="utf-8", newline="\n")

    for map_id in sorted(zones):
        if map_id in WORLD_MAPS:
            continue
        entry = zones[map_id]
        zone_name = entry["name"]
        zone_ok = normalise_key(zone_name) in names
        subs_all = subzones.get(map_id, {})
        kept = []
        for key, sub in sorted(subs_all.items(), key=lambda kv: kv[1].get("name", kv[0])):
            report["subz_total"] += 1
            if not text_of(sub):
                report["subz_no_text"] += 1
                continue
            if not in_forever(key, map_id, names, renamed, blocked):
                report["subz_not_forever"].append(f"{zone_name}: {sub.get('name', key)}")
                continue
            kept.append((sub.get("name", key), sub))
        if not zone_ok:
            report["zones_not_forever"].append(f"{zone_name} (map {map_id}; {len(kept)} subzones with text skipped)")
            continue
        if not text_of(entry) and not kept:
            report["zones_no_text"].append(f"{zone_name} (map {map_id})")
            continue
        claim(slug(zone_name), f"zone {zone_name}")
        (out_dir / "zones" / f"{slug(zone_name)}.md").write_text(render_zone(zone_name, entry, kept), encoding="utf-8", newline="\n")
        report["zones_written"].append(f"{zone_name}: {1 if text_of(entry) else 0} overview, {len(kept)} subzones")
        report["subz_written"] += len(kept)

    for map_id in sorted(set(dungeons) | set(bosses)):
        d = dungeons.get(map_id)
        if not d or 1 not in d:
            continue
        dungeon_name = d[1]
        blist = as_list(bosses.get(map_id, {}))
        boss_dir = f"bosses/{slug(dungeon_name)}"
        story_ref = d.get("story")
        story_entry = subzones.get(int(story_ref[1]), {}).get(story_ref[2]) if story_ref else None
        have_story = [b for b in blist if stories.get(map_id, {}).get(b["key"])]
        for i, b in enumerate(blist, 1):
            text = stories.get(map_id, {}).get(b["key"])
            if not text:
                report["boss_no_story"].append(f"{dungeon_name}: {b[1]}")
                continue
            target = out_dir / boss_dir
            target.mkdir(parents=True, exist_ok=True)
            (target / f"{slug(b[1])}.md").write_text(render_boss(b[1], dungeon_name, i, len(blist), text[1]), encoding="utf-8", newline="\n")
            report["boss_files"] += 1
        sub_in = []
        if story_entry and text_of(story_entry) and in_forever(story_ref[2], int(story_ref[1]), names, renamed, blocked):
            sub_in = [(story_entry.get("name", story_ref[2]), story_entry)]
        if sub_in or have_story:
            claim(slug(dungeon_name), f"dungeon {dungeon_name}")
            (out_dir / "zones" / f"{slug(dungeon_name)}.md").write_text(
                render_zone(dungeon_name, None, sub_in, [b[1] for b in blist], boss_dir if have_story else None),
                encoding="utf-8", newline="\n")
            report["dungeon_files"].append(dungeon_name)

    (out_dir / "ATTRIBUTION.md").write_text(attribution(camelot["build"]), encoding="utf-8", newline="\n")
    (out_dir / "MANIFEST.md").write_text(manifest(report, camelot["build"]), encoding="utf-8", newline="\n")
    return report


def attribution(build):
    return f"""# Attribution

The zone, subzone, dungeon and boss texts in this folder are adapted from Warcraft Wiki (https://warcraft.wiki.gg),
published under the Creative Commons Attribution-ShareAlike 4.0 licence (https://creativecommons.org/licenses/by-sa/4.0/).
They come through the data files of the Spoken add-on (https://github.com/rusty-key/spoken-wow, MIT licence), which
cleaned and rewrote them. The boss and dungeon stories draw on Blizzard's Adventure Guide text as well. The games'
names and the underlying content belong to Blizzard Entertainment.

Because of the share-alike term, these files stay under CC BY-SA 4.0 wherever they are copied. Each file names its
sources. The files are generated by `scripts/build_spoken_lore.py`; do not edit them by hand.

{BUILD_NOTE.format(build=build)}
"""


def manifest(report, build):
    def listing(title, items):
        return [f"## {title} ({len(items)})", ""] + ([f"- {i}" for i in items] or ["- none"]) + [""]

    lines = ["# Lore folder manifest", "",
             "Generated by `scripts/build_spoken_lore.py`. " + BUILD_NOTE.format(build=build), "",
             f"- Zone and dungeon files: {len(report['zones_written']) + len(report['dungeon_files'])} "
             f"({len(report['zones_written'])} zones, {len(report['dungeon_files'])} dungeons)",
             f"- Subzone sections written: {report['subz_written']} of {report['subz_total']} subzones in Spoken's data",
             f"- Boss files: {report['boss_files']}", ""]
    lines += listing("World file (world.md)", report["world_written"])
    lines += listing("Zones written", report["zones_written"])
    lines += listing("Dungeons written", report["dungeon_files"])
    lines += listing("Zones left out: not in Forever's AreaTable", report["zones_not_forever"])
    lines += listing("Zones left out: no lore text yet", report["zones_no_text"])
    lines += [f"## Subzones left out: no lore text yet ({report['subz_no_text']})", ""]
    lines += listing("Subzones left out: not enabled in Forever", report["subz_not_forever"])
    lines += listing("Bosses left out: no story yet", report["boss_no_story"])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--spoken", required=True, help="path to a clone of rusty-key/spoken-wow")
    parser.add_argument("--out", required=True, help="the lore folder to write, e.g. references/lore")
    args = parser.parse_args(argv)
    report = build(args.spoken, args.out)
    print(f"zones {len(report['zones_written'])}, dungeons {len(report['dungeon_files'])}, subzone sections "
          f"{report['subz_written']}/{report['subz_total']}, boss files {report['boss_files']}")


if __name__ == "__main__":
    main()
