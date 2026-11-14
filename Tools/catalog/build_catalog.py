#!/usr/bin/env python3
"""Build the living catalogue of Eurobound content (bead Eurobound-yore).

Reads the design docs, the engine data, the art folders and the open beads,
and writes one Markdown file per category plus catalog.json into docs/catalog/.

    python -I Tools/catalog/build_catalog.py

Standard library only. Nothing here writes descriptions: every summary is a
line copied from the doc or data file it names. See README.md in this folder.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import quote

HEADER_NOTE = "do not edit by hand; run Tools/catalog/build_catalog.py"
SKIP_DIRS = {"legacy", "world design", "templates", "png_assets", "sprites",
             "sprite_mapping", "__pycache__", ".git"}
NOT_A_CITY = {"shared"}
BEAD_PREFIX = "Eurobound-"
SUMMARY_MAX = 220
NO_SUMMARY = "no summary in doc"

ITEM_GROUPS = [
    ("consumable", "Consumables"),
    ("equipment", "Equipment"),
    ("permanent", "Permanent items"),
    ("key_quest", "Key and quest items"),
    ("junk", "Junk"),
    ("nft", "NFTs"),
    ("opener", "Bottle openers"),
    ("stamp", "Passport stamps"),
    ("signature_beer", "Signature beers"),
    ("other", "Other (type not recognised)"),
]

SYSTEMS = [
    ("battle", "Battle"),
    ("levelling", "Levelling"),
    ("intoxication", "Intoxication"),
    ("economy_shops", "Economy and shops"),
    ("inventory_equipment", "Inventory and equipment"),
    ("clock_rest", "Clock and rest"),
    ("navigation", "Navigation"),
    ("quests_flags", "Quests and flags"),
    ("icq_dialogue", "ICQ and dialogue"),
    ("couchsurfing", "Couchsurfing"),
    ("brewery_tour", "Brewery tour"),
    ("minigames", "Minigames"),
    ("save_load", "Save and load"),
    ("menus", "Menus"),
    ("travel", "Travel"),
    ("audio", "Audio"),
    ("other", "Other"),
]

# First match wins. Used only when seeding game_elements.json from the audit.
SYSTEM_RULES = [
    (r"travel between cities", "travel"),
    (r"save and load", "save_load"),
    (r"title screen|field menu|settings", "menus"),
    (r"sound|music|audio", "audio"),
    (r"minigame", "minigames"),
    (r"brewery", "brewery_tour"),
    (r"couchsurf", "couchsurfing"),
    (r"dialogue|wi-fi|icq and|and icq", "icq_dialogue"),
    (r"flags|quest", "quests_flags"),
    (r"walking|navigation", "navigation"),
    (r"clock|^rest$", "clock_rest"),
    (r"inventory|equipment|junk", "inventory_equipment"),
    (r"intoxication|hangover", "intoxication"),
    (r"\bxp\b|clout|level", "levelling"),
    (r"wallet|shop|token|shitcoin|airdrop|nft", "economy_shops"),
    (r"turns|bravado|abilit|combo|taunt|status|enemy|boss|battle|encounter",
     "battle"),
]

TITLE_PREFIX = re.compile(
    r"^(NPC Profile|Item Definition|Villain Profile|Enemy Profile|Sidequest|"
    r"Side Quest|Quest|NFT|Signature Beer|Location|Status Effect|Ability)"
    r"\s*[:—-]\s*", re.I)


# ---------------------------------------------------------------- helpers

def norm(value):
    """Lower-case ASCII key: 'Jiří the Commuter' -> 'jiri_the_commuter'."""
    text = unicodedata.normalize("NFKD", str(value))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def name_key(name):
    return norm(re.sub(r"\([^)]*\)", " ", str(name)))


def squash(value):
    key = norm(value)
    if key.startswith("the_"):
        key = key[4:]
    return key.replace("_", "")


def pretty(slug):
    return re.sub(r"[_\s]+", " ", str(slug)).strip().title()


def read_text(path):
    with open(path, "r", encoding="utf-8-sig", errors="replace") as handle:
        return handle.read()


def clean(value):
    """Strip Markdown decoration and bracketed source notes from a field."""
    text = re.sub(r"\[[^\]]*\]", " ", str(value))
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text).strip(" \t|-")
    return text.strip()


def shorten(text, limit=SUMMARY_MAX):
    text = re.sub(r"\s+", " ", str(text)).strip()
    if len(text) > limit:
        text = text[:limit - 1].rstrip() + "…"
    return text


def md_field(text, *labels):
    """Value of a '- **Label**: value' line (or a | **Label** | value | row)."""
    for label in labels:
        pattern = re.compile(
            r"^[ \t>]*(?:[-*•][ \t]+)?\|?[ \t]*\*\*" + re.escape(label) +
            r"(?::\*\*|\*\*[ \t]*:|\*\*[ \t]*\|)[ \t]*(.+?)[ \t]*\|?[ \t]*$",
            re.I | re.M)
        match = pattern.search(text)
        if match and clean(match.group(1)):
            return match.group(1).strip()
    return ""


def md_id(text, *labels):
    raw = md_field(text, *labels)
    if not raw:
        return ""
    tick = re.search(r"`([^`]+)`", raw)
    if tick:
        return tick.group(1).strip()
    words = clean(raw).split()
    # A bare word counts only if it looks like an id, not "OPEN QUESTION" or "TBD".
    if words and re.fullmatch(r"[a-z0-9]+(?:[_.\-][a-z0-9]+)+", words[0]):
        return words[0]
    return ""


def md_title(text, fallback=""):
    for line in text.splitlines()[:40]:
        match = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if match:
            return clean(TITLE_PREFIX.sub("", match.group(1).strip()))
    for line in text.splitlines()[:10]:
        if line.strip():
            first = line.strip()
            if len(first) <= 80 and not first.startswith(("-", "*", "|", ">")):
                return clean(first)
            break
    return fallback


HONORIFICS = {"the", "dr", "mr", "mrs", "ms", "chef", "herr", "frau", "old",
              "doktor", "professor", "madame", "monsieur", "dj"}


def clean_name(raw, title=""):
    """A display name without the notes some docs append to the field."""
    name = clean(str(raw).split("|")[0])
    if len(name) > 45:
        cuts = [name.find(mark) for mark in (" (", ". ", " : ", ": ")]
        cuts = [c for c in cuts if c >= 3]
        if cuts:
            name = name[:min(cuts)].strip()
    if len(name) > 60 and title and len(title) < len(name):
        name = title
    quoted = re.match(r'^["“](.+)["”]$', name)
    if quoted:
        name = quoted.group(1).strip()
    return name or clean(title)


def fuzzy_key(value):
    """Name key that ignores honorifics, 'the' and punctuation."""
    words = [w for w in norm(re.sub(r"\([^)]*\)", " ", str(value))).split("_")
             if w and w not in HONORIFICS]
    return "".join(words)


def id_core(identifier, cities=()):
    """'publandia_npc_orla_brennan_01' -> 'orla_brennan'."""
    core = re.sub(r"_0*1$", "", norm(identifier))
    if "npc_" in core:
        core = core.split("npc_", 1)[1]
    for city in cities:
        if core.startswith(norm(city) + "_"):
            core = core[len(norm(city)) + 1:]
    return core


def md_tagline(text):
    """First single-line italic near the top: the doc's own tagline."""
    for line in text.splitlines()[:45]:
        stripped = line.strip()
        match = re.match(r"^\*(?![\s*])(.+?)\*(?!\*)(.*)$", stripped)
        if match:
            return shorten(clean(match.group(1) + match.group(2)))
    return ""


def md_first_prose(text):
    """For docs with no '##' structure: the first prose line after the title."""
    if re.search(r"^##\s", text, re.M):
        return ""
    seen_title = False
    for line in text.splitlines()[:30]:
        stripped = line.strip()
        if not stripped:
            continue
        if not seen_title:
            seen_title = True
            continue
        if stripped.startswith(("#", "|", ">", "---", "```")):
            continue
        return shorten(clean(re.sub(r"^[-*•]\s+", "", stripped)))
    return ""


def md_summary(text, fallback_fields=()):
    tagline = md_tagline(text)
    if tagline:
        return tagline
    for label in fallback_fields:
        value = clean(md_field(text, label))
        if value:
            return shorten(value)
    return md_first_prose(text)


def find_dir(root, *parts):
    """Resolve a repo-relative folder case-insensitively. '' if missing."""
    current = root
    rel = []
    for part in parts:
        try:
            names = os.listdir(current)
        except OSError:
            return ""
        hit = next((n for n in names if n.lower() == part.lower()
                    and os.path.isdir(os.path.join(current, n))), None)
        if hit is None:
            return ""
        current = os.path.join(current, hit)
        rel.append(hit)
    return "/".join(rel)


def walk(root, rel, exts):
    """Yield repo-relative posix paths under rel with one of the extensions."""
    if not rel:
        return
    base = os.path.join(root, rel)
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d.lower() not in SKIP_DIRS)
        for filename in sorted(filenames):
            if filename.lower().endswith(exts):
                full = os.path.join(dirpath, filename)
                yield os.path.relpath(full, root).replace(os.sep, "/")


def stem_of(rel_path):
    return os.path.splitext(os.path.basename(rel_path))[0]


class Context:
    """Everything the collectors share: root, problems, cities, indexes."""

    def __init__(self, root):
        self.root = root
        self.problems = []
        worlds = find_dir(root, "design", "worlds")
        self.worlds = worlds
        self.cities = []
        if worlds:
            for name in sorted(os.listdir(os.path.join(root, worlds))):
                if (os.path.isdir(os.path.join(root, worlds, name))
                        and name.lower() not in NOT_A_CITY
                        and name.lower() not in SKIP_DIRS):
                    self.cities.append(name)
        self.data = find_dir(root, "game", "assets", "data")
        self.assets = find_dir(root, "game", "assets")
        self._tokens = {}

    def text(self, rel):
        try:
            return read_text(os.path.join(self.root, rel))
        except OSError as error:
            self.problems.append({"path": rel, "error": str(error)})
            return ""

    def json(self, rel):
        try:
            return json.loads(read_text(os.path.join(self.root, rel)))
        except (OSError, ValueError) as error:
            self.problems.append({"path": rel, "error": shorten(error, 160)})
            return None

    def exists(self, rel):
        return bool(rel) and os.path.exists(os.path.join(self.root, rel))

    def data_files(self, *subdirs):
        if not self.data:
            return []
        found = []
        for sub in subdirs:
            target = self.data + "/" + sub
            full = os.path.join(self.root, target)
            if os.path.isfile(full):
                found.append(target)
            elif os.path.isdir(full):
                found.extend(walk(self.root, target, (".json",)))
        return found

    def engine_tokens(self, *subdirs):
        """Normalised keys and short string values found in engine data."""
        cache_key = "|".join(subdirs)
        if cache_key not in self._tokens:
            tokens = set()
            for rel in self.data_files(*subdirs):
                payload = self.json(rel)
                if payload is not None:
                    _collect_tokens(payload, tokens)
            self._tokens[cache_key] = tokens
        return self._tokens[cache_key]

    def art_stems(self, *subdirs):
        stems = set()
        if not self.assets:
            return stems
        for sub in subdirs:
            base = os.path.join(self.root, self.assets, sub)
            for _dirpath, _dirnames, filenames in os.walk(base):
                for filename in filenames:
                    if filename.lower().endswith((".import", ".gitkeep", ".uid")):
                        continue
                    stem = norm(os.path.splitext(filename)[0])
                    stems.add(re.sub(r"_(128|256|512|1024)$", "", stem))
        return stems

    def location_art(self):
        """squash(folder) -> True for location folders that hold any art."""
        found = set()
        base_rel = (self.assets + "/worlds") if self.assets else ""
        base = os.path.join(self.root, base_rel)
        if not base_rel or not os.path.isdir(base):
            return found
        for city in os.listdir(base):
            city_dir = os.path.join(base, city)
            if not os.path.isdir(city_dir):
                continue
            for slug in os.listdir(city_dir):
                folder = os.path.join(city_dir, slug)
                if not os.path.isdir(folder):
                    continue
                for _dirpath, _dirnames, filenames in os.walk(folder):
                    if any(not f.lower().endswith((".import", ".gitkeep", ".uid"))
                           for f in filenames):
                        found.add((norm(city), squash(slug)))
                        break
        return found


def _collect_tokens(node, tokens):
    if isinstance(node, dict):
        for key, value in node.items():
            tokens.add(norm(key))
            _collect_tokens(value, tokens)
    elif isinstance(node, list):
        for value in node:
            _collect_tokens(value, tokens)
    elif isinstance(node, str) and 0 < len(node) <= 80:
        tokens.add(norm(node))
        tokens.add(name_key(node))


def id_variants(identifier):
    key = norm(identifier)
    if not key:
        return set()
    out = {key}
    trimmed = re.sub(r"_\d+$", "", key)
    out.add(trimmed)
    for value in (key, trimmed):
        if value.startswith("item_"):
            out.add(value[5:])
    out.discard("")
    return out


def new_row(category, name, city="", **extra):
    row = {
        "category": category, "name": clean(name), "id": "", "city": city,
        "area": "", "kind": "", "summary": "", "doc": "", "sources": [],
        "design_doc": False, "engine_data": False, "art": None,
        "open_beads": [], "flags": [], "keys": set(),
    }
    row.update(extra)
    return row


class Bucket:
    """Rows of one category, merged when two sources name the same thing."""

    def __init__(self):
        self.rows = []
        self.index = {}

    def add(self, row, merge_keys):
        merge_keys = [k for k in merge_keys if k and not k.endswith(":")]
        for key in merge_keys:
            if key in self.index:
                target = self.index[key]
                _merge(target, row)
                for other in merge_keys:
                    self.index.setdefault(other, target)
                return target
        self.rows.append(row)
        for key in merge_keys:
            self.index[key] = row
        return row


def _merge(target, row):
    row_is_md = row["doc"].lower().endswith(".md")
    target_is_md = target["doc"].lower().endswith(".md")
    if row_is_md and not target_is_md:
        for field in ("name", "doc", "summary", "kind", "area"):
            if row[field]:
                target[field] = row[field]
    alt_ids = target.setdefault("alt_ids", [])
    for other in [row["id"]] + row.get("alt_ids", []):
        if (other and target["id"] and norm(other) != norm(target["id"])
                and other not in alt_ids):
            alt_ids.append(other)
    for field in ("id", "area", "kind", "summary", "doc", "city"):
        if not target[field] and row[field]:
            target[field] = row[field]
    for source in row["sources"]:
        if source not in target["sources"]:
            target["sources"].append(source)
    target["keys"] |= row["keys"]
    target["design_doc"] = target["design_doc"] or row["design_doc"]
    for key, value in row.items():
        if key not in target:
            target[key] = value


def art_match(candidates, stems):
    for cand in candidates:
        if len(cand) < 4:
            continue
        for stem in stems:
            if (stem == cand or stem.startswith(cand + "_")
                    or cand.startswith(stem + "_")):
                return True
    return False


def json_entries(payload, list_keys):
    if not isinstance(payload, dict):
        return
    for key in list_keys:
        value = payload.get(key)
        if isinstance(value, list):
            for entry in value:
                if isinstance(entry, dict):
                    yield key, entry


def first_str(entry, *keys):
    for key in keys:
        value = entry.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


# ---------------------------------------------------------------- collectors

def collect_locations(ctx):
    bucket = Bucket()
    other_docs = []
    for city in ctx.cities:
        city_rel = ctx.worlds + "/" + city
        city_dir = os.path.join(ctx.root, city_rel)
        for filename in sorted(os.listdir(city_dir)):
            rel = city_rel + "/" + filename
            if not filename.lower().endswith(".md"):
                continue
            text = ctx.text(rel)
            loc_id = md_id(text, "Location ID")
            if not loc_id:
                other_docs.append({"city": pretty(city), "doc": rel,
                                   "title": md_title(text, stem_of(rel))})
                continue
            title = md_title(text, pretty(stem_of(rel)))
            name = clean_name(md_field(text, "Display Name"), title) or title
            row = new_row("locations", name, pretty(city), id=loc_id, doc=rel,
                          sources=[rel], design_doc=True,
                          area=shorten(clean(md_field(text, "Area Zone")), 80),
                          kind=shorten(clean(md_field(text, "Location Type")), 80),
                          summary=md_summary(text, ("Satirical Subtitle",)))
            row["keys"] = id_variants(loc_id) | {name_key(name), norm(stem_of(rel))}
            bucket.add(row, ["id:" + norm(loc_id), "name:%s:%s" % (city, name_key(name))])
        for rel in walk(ctx.root, find_dir(ctx.root, *city_rel.split("/"), "core"), (".json",)):
            payload = ctx.json(rel)
            if not isinstance(payload, dict):
                continue
            loc_id = first_str(payload, "location_id")
            name = first_str(payload, "display_name", "name") or pretty(stem_of(rel))
            row = new_row("locations", name, pretty(city), id=loc_id, doc=rel,
                          sources=[rel], design_doc=True,
                          area=pretty(first_str(payload, "zone")),
                          kind=pretty(first_str(payload, "location_type")),
                          summary=shorten(first_str(payload, "satirical_subtitle")))
            slug = re.sub(r"_core$", "", norm(stem_of(rel)))
            row["keys"] = id_variants(loc_id) | {name_key(name), slug}
            merge = ["id:" + norm(loc_id), "name:%s:%s" % (city, name_key(name))]
            legacy = payload.get("legacy_location_ids")
            if isinstance(legacy, list):
                merge += ["id:" + norm(x) for x in legacy if isinstance(x, str)]
            bucket.add(row, merge)
    tokens = ctx.engine_tokens("locations", "world_data/Maps.json")
    art = ctx.location_art()
    for row in bucket.rows:
        row["engine_data"] = bool(row["keys"] & tokens)
        squashed = {squash(k) for k in row["keys"]}
        row["art"] = any((norm(row["city"]), s) in art for s in squashed)
        if not row["doc"].lower().endswith(".md"):
            row["flags"].append("no location doc (companion JSON only)")
    for folder in ("interactables",):
        shared = find_dir(ctx.root, *(ctx.worlds.split("/") + ["shared", folder])) if ctx.worlds else ""
        for rel in walk(ctx.root, shared, (".md",)):
            other_docs.append({"city": "Shared", "doc": rel,
                               "title": md_title(ctx.text(rel), stem_of(rel))})
    return bucket.rows, other_docs


def collect_npcs_and_villains(ctx):
    npcs = Bucket()
    villains = Bucket()
    for city in ctx.cities:
        npc_dir = find_dir(ctx.root, *(ctx.worlds.split("/") + [city, "npcs"]))
        for rel in walk(ctx.root, npc_dir, (".md",)):
            text = ctx.text(rel)
            if md_id(text, "Villain ID", "Enemy ID"):
                _add_villain_doc(ctx, villains, rel, text, city)
                continue
            npc_id = md_id(text, "NPC ID")
            title = md_title(text, pretty(stem_of(rel)))
            name = clean_name(md_field(text, "Display Name"), title) or title
            folder = os.path.basename(os.path.dirname(rel))
            area = "" if folder.lower() == "npcs" else pretty(folder)
            row = new_row("npcs", name, pretty(city), id=npc_id, doc=rel,
                          sources=[rel], design_doc=True, area=area,
                          kind=shorten(clean(md_field(text, "Role")), 80),
                          summary=md_summary(text, ("Title",)))
            stem = re.sub(r"^npc_", "", norm(stem_of(rel)))
            row["keys"] = id_variants(npc_id) | {name_key(name), stem,
                                                 name_key(md_title(text, ""))}
            row["keys"].discard("")
            fuzzy = {fuzzy_key(name), fuzzy_key(stem), fuzzy_key(clean_name(title)),
                     fuzzy_key(id_core(npc_id, ctx.cities)),
                     fuzzy_key(clean(md_field(text, "Full Name")))}
            npcs.add(row, ["id:" + norm(npc_id), "doc:" + rel.lower(),
                           "name:%s:%s" % (city, name_key(name))] +
                     ["fz:%s:%s" % (city, f) for f in sorted(fuzzy) if len(f) >= 6])
        for rel in walk(ctx.root, npc_dir, (".json",)):
            payload = ctx.json(rel)
            if not isinstance(payload, dict):
                continue
            place = first_str(payload, "location_name") or pretty(
                os.path.basename(os.path.dirname(rel)))
            for list_key, entry in json_entries(payload, ("npcs", "ambient_npcs")):
                name = first_str(entry, "display_name", "name")
                npc_id = first_str(entry, "npc_id", "group_id", "id")
                if not name and not npc_id:
                    continue
                ambient = list_key == "ambient_npcs"
                kind = "ambient group" if ambient else shorten(
                    pretty(first_str(entry, "role", "npc_type")), 80)
                row = new_row("npcs", name or pretty(npc_id), pretty(city),
                              id=npc_id, doc=rel, sources=[rel], design_doc=True,
                              area=place, kind=kind, ambient=ambient,
                              summary=shorten(first_str(entry, "description", "concept", "summary",
                                                        "personality", "appearance")))
                row["keys"] = id_variants(npc_id) | {name_key(row["name"])}
                profile = first_str(entry, "profile").lower()
                merge = ["id:" + norm(npc_id)]
                if profile:
                    merge.append("doc:" + profile)
                merge.append("name:%s:%s%s" % (city, name_key(row["name"]),
                                                ":" + norm(place) if ambient else ""))
                if not ambient:
                    fuzzy = {fuzzy_key(row["name"]),
                             fuzzy_key(id_core(npc_id, ctx.cities))}
                    merge += ["fz:%s:%s" % (city, f) for f in sorted(fuzzy)
                              if len(f) >= 6]
                npcs.add(row, merge)
    tokens = ctx.engine_tokens("npcs", "locations", "world_data/events")
    stems = ctx.art_stems("characters/npcs")
    for row in npcs.rows:
        row.setdefault("ambient", False)
        if row["doc"].lower().endswith(".md"):
            row["ambient"] = False
        row["engine_data"] = bool(row["keys"] & tokens)
        row["art"] = art_match(row["keys"], stems)
        if not row["doc"].lower().endswith(".md"):
            row["flags"].append("ambient group, JSON only" if row["ambient"]
                                else "no profile doc (companion JSON only)")
    return npcs.rows, villains


def _add_villain_doc(ctx, bucket, rel, text, city):
    is_enemy = bool(md_id(text, "Enemy ID")) and not md_id(text, "Villain ID")
    ident = md_id(text, "Villain ID", "Enemy ID")
    title = clean_name(md_title(text, pretty(stem_of(rel))))
    name = clean_name(md_field(text, "Display Name"), title) or title
    tier = clean(md_field(text, "Tier", "Encounter Family"))
    kind = ("Enemy" if is_enemy else "Villain") + (": " + tier if tier else "")
    area = clean(md_field(text, "Primary Location", "Zone / Encounter Table"))
    row = new_row("enemies_and_villains", name, pretty(city), id=ident, doc=rel,
                  sources=[rel], design_doc=True, kind=shorten(kind, 80),
                  area=shorten(area, 90), summary=md_summary(text))
    stem = re.sub(r"^(villain|enemy)_", "", norm(stem_of(rel)))
    row["keys"] = id_variants(ident) | {name_key(name), stem}
    bucket.add(row, ["id:" + norm(ident), "name:%s:%s" % (city, name_key(name))])


def collect_enemies(ctx, bucket):
    for city in ctx.cities:
        for sub in ("villains", "enemies"):
            folder = find_dir(ctx.root, *(ctx.worlds.split("/") + [city, sub]))
            for rel in walk(ctx.root, folder, (".md",)):
                text = ctx.text(rel)
                if md_id(text, "Villain ID", "Enemy ID"):
                    _add_villain_doc(ctx, bucket, rel, text, city)
    for sub in ("villains", "enemies"):
        folder = find_dir(ctx.root, "design", sub)
        for rel in walk(ctx.root, folder, (".md",)):
            text = ctx.text(rel)
            if md_id(text, "Villain ID", "Enemy ID"):
                _add_villain_doc(ctx, bucket, rel, text, clean(md_field(text, "City")) or "General")
    known = set()
    for row in bucket.rows:
        known |= row["keys"]
    engine_only = {}
    for rel in ctx.data_files("enemies"):
        payload = ctx.json(rel)
        if not isinstance(payload, dict):
            continue
        world = first_str(payload, "world_name") or stem_of(rel).split("_")[0]
        for group in ("enemies", "villains"):
            entries = payload.get(group)
            if not isinstance(entries, dict):
                continue
            for key, entry in entries.items():
                if not isinstance(entry, dict):
                    continue
                name = first_str(entry, "display_name", "name") or pretty(key)
                if norm(key) in known or name_key(name) in known:
                    continue
                row = engine_only.get(norm(key))
                if row is None:
                    row = new_row("enemies_and_villains", name, pretty(world),
                                  id=key, doc=rel, sources=[], kind="Engine entry",
                                  summary=shorten(first_str(entry, "battle_intro", "intro_bark")))
                    row["keys"] = {norm(key), name_key(name)}
                    row["flags"].append("in engine data, no villain or enemy doc of its own")
                    engine_only[norm(key)] = row
                    bucket.rows.append(row)
                if rel not in row["sources"]:
                    row["sources"].append(rel)
    tokens = ctx.engine_tokens("enemies")
    stems = ctx.art_stems("characters/enemies")
    for row in bucket.rows:
        row["engine_data"] = bool(row["keys"] & tokens)
        row["art"] = art_match(row["keys"], stems)
    return bucket.rows


def item_group(type_text, stem="", ident=""):
    stem, ident = norm(stem), norm(ident)
    text = " " + norm(type_text).replace("_", " ") + " "
    if "nft" in stem.split("_") or " nft " in text or ident.startswith("nft_"):
        return "nft"
    if stem.startswith("beer_") or ident.startswith("beer_") or " signature beer " in text:
        return "signature_beer"
    if stem.startswith("opener_") or ident.startswith("opener_") or " opener " in text:
        return "opener"
    if stem.startswith("stamp_") or ident.startswith("stamp_") or " stamp " in text:
        return "stamp"
    if " junk " in text or "_junk_" in "_" + ident + "_":
        return "junk"
    if " permanent " in text:
        return "permanent"
    if re.search(r" (equipment|weapon|armor|armour|wearable|cosmetic|accessory) ", text):
        return "equipment"
    if re.search(r" (key|quest|document|collectible|currency|lore|curio) ", text):
        return "key_quest"
    if re.search(r" (consumable|food|drink|drug|vape|throwable) ", text):
        return "consumable"
    return "other"


def guess_city(ctx, rel, text):
    parts = [p.lower() for p in rel.split("/")]
    for city in ctx.cities:
        if city.lower() in parts or (city.lower() + "_items") in parts:
            return pretty(city)
    explicit = clean(md_field(text, "City"))
    head = explicit or " ".join(
        md_field(text, label) for label in
        ("Source", "Brewed By", "Brewery", "Location", "Found", "Acquired", "Acquisition"))
    for city in ctx.cities:
        if re.search(r"\b" + re.escape(city) + r"\b", head, re.I):
            return pretty(city)
    return "General"


def collect_items(ctx):
    bucket = Bucket()
    md_files = list(walk(ctx.root, find_dir(ctx.root, "design", "items"), (".md",)))
    json_files = []
    items_root = find_dir(ctx.root, "design", "items")
    if items_root:
        for filename in sorted(os.listdir(os.path.join(ctx.root, items_root))):
            if filename.lower().endswith(".json"):
                json_files.append(items_root + "/" + filename)
    for city in ctx.cities:
        folder = find_dir(ctx.root, *(ctx.worlds.split("/") + [city, "items"]))
        md_files += list(walk(ctx.root, folder, (".md",)))
        json_files += list(walk(ctx.root, folder, (".json",)))
    for rel in md_files:
        if "/docs/" in rel.lower():
            continue
        text = ctx.text(rel)
        ident = md_id(text, "Item ID", "NFT ID", "Token ID")
        if not ident and not stem_of(rel).lower().endswith("_item"):
            continue
        title = md_title(text, pretty(stem_of(rel)))
        name = clean_name(md_field(text, "Display Name"), title) or title
        type_text = clean(md_field(text, "Item Type", "Type", "Category"))
        stem = norm(stem_of(rel))
        row = new_row("items", name, guess_city(ctx, rel, text), id=ident, doc=rel,
                      sources=[rel], design_doc=True, kind=shorten(type_text, 70),
                      group=item_group(type_text, stem, ident),
                      summary=md_summary(text, ("Style", "Opener", "Stamp Face",
                                                "Description", "Internal Name")))
        bare = re.sub(r"_(nft_)?item$", "", stem)
        row["keys"] = id_variants(ident) | {name_key(name), bare}
        bucket.add(row, ["id:" + k for k in sorted(id_variants(ident))])
    for rel in json_files:
        payload = ctx.json(rel)
        if not isinstance(payload, dict):
            continue
        if "item_id" in payload:
            entries = [("items", payload)]
        else:
            entries = list(json_entries(payload, ("items", "quest_items",
                                                  "discoverable_items", "achievement_items")))
        for _list_key, entry in entries:
            ident = first_str(entry, "item_id", "id")
            name = first_str(entry, "display_name", "name")
            if not ident and not name:
                continue
            type_text = first_str(entry, "item_type", "type", "category")
            row = new_row("items", name or pretty(ident), guess_city(ctx, rel, ""),
                          id=ident, doc=rel, sources=[rel], design_doc=True,
                          kind=pretty(type_text), group=item_group(type_text, "", ident),
                          summary=shorten(first_str(entry, "description", "flavor_text",
                                                    "tagline", "effect")))
            row["keys"] = id_variants(ident) | {name_key(row["name"])}
            bucket.add(row, ["id:" + k for k in sorted(id_variants(ident))])
    known = set()
    for row in bucket.rows:
        known |= row["keys"]
    for rel in ctx.data_files("items", "nft"):
        payload = ctx.json(rel)
        if not isinstance(payload, dict):
            continue
        file_stem = norm(stem_of(rel))
        pairs = []
        for key, value in payload.items():
            if isinstance(value, dict):
                pairs += [(k, v) for k, v in value.items() if isinstance(v, dict)]
            elif isinstance(value, list):
                pairs += [(first_str(v, "id", "item_id"), v) for v in value
                          if isinstance(v, dict)]
        for key, entry in pairs:
            name = first_str(entry, "display_name", "name") or pretty(key)
            if not key or id_variants(key) & known or name_key(name) in known:
                continue
            if "nft" in rel.lower() or "vault" in file_stem:
                group = "nft"
            elif file_stem.startswith("consumable"):
                group = "consumable"
            elif file_stem.startswith("equipment"):
                group = "equipment"
            else:
                group = item_group(first_str(entry, "item_class", "item_type"), "", key)
                if group == "other":
                    group = "key_quest"
            summary = first_str(entry, "description")
            if not summary and isinstance(entry.get("copy"), dict):
                summary = first_str(entry["copy"], "tagline")
            city = pretty(first_str(entry, "city")) or "General"
            row = new_row("items", name, city, id=key, doc=rel, sources=[rel],
                          kind="Engine entry", group=group, summary=shorten(summary))
            row["keys"] = id_variants(key) | {name_key(name)}
            row["flags"].append("in engine data, no item doc of its own")
            known |= row["keys"]
            bucket.rows.append(row)
    tokens = ctx.engine_tokens("items", "nft", "brewery_tour")
    stems = ctx.art_stems("items")
    for row in bucket.rows:
        row["engine_data"] = bool(row["keys"] & tokens)
        row["art"] = art_match(row["keys"] | {"item_" + k for k in row["keys"]}, stems)
    return bucket.rows


def collect_quests(ctx):
    bucket = Bucket()
    quests_root = find_dir(ctx.root, "design", "quests")
    for rel in walk(ctx.root, quests_root, (".md",)):
        text = ctx.text(rel)
        ident = md_id(text, "Quest ID")
        sub = rel[len(quests_root) + 1:].split("/")[:-1]
        folder = "/".join(sub)
        city = "General"
        for known_city in ctx.cities:
            if known_city.lower() in [s.lower() for s in sub]:
                city = pretty(known_city)
        if city == "General" and folder and "general" not in folder.lower():
            city = folder
        title = clean_name(md_title(text, pretty(stem_of(rel))))
        name = clean_name(md_field(text, "Quest Name"), title) or title
        row = new_row("quests", name, city, id=ident, doc=rel, sources=[rel],
                      design_doc=True,
                      kind=shorten(clean(md_field(text, "Quest Type", "Type")), 70),
                      area=shorten(clean(md_field(text, "Location", "Primary Location")), 80),
                      summary=md_summary(text, ("Satirical Subtitle", "Premise")))
        row["keys"] = id_variants(ident) | {name_key(name), norm(stem_of(rel))}
        bucket.add(row, ["id:" + norm(ident), "doc:" + rel.lower()])
    known = set()
    for row in bucket.rows:
        known |= row["keys"]
    log_tokens = ctx.engine_tokens("quest_log")
    for rel in ctx.data_files("quests", "quest_log"):
        payload = ctx.json(rel)
        entries = []
        if isinstance(payload, dict) and "quest_id" in payload:
            entries = [payload]
        elif isinstance(payload, dict) and isinstance(payload.get("quests"), list):
            entries = [e for e in payload["quests"] if isinstance(e, dict)]
        for entry in entries:
            ident = first_str(entry, "quest_id", "id")
            name = first_str(entry, "display_name", "name") or pretty(ident)
            if id_variants(ident) & known or name_key(name) in known:
                continue
            row = new_row("quests", name, pretty(first_str(entry, "city")) or "General",
                          id=ident, doc=rel, sources=[rel], kind="Engine entry",
                          summary=shorten(first_str(entry, "satirical_subtitle")))
            row["keys"] = id_variants(ident) | {name_key(name)}
            row["flags"].append("in engine data, no quest doc")
            known |= row["keys"]
            bucket.rows.append(row)
    tokens = ctx.engine_tokens("quests", "quest_log")
    for row in bucket.rows:
        row["engine_data"] = bool(row["keys"] & tokens)
        row["in_quest_log"] = bool(row["keys"] & log_tokens)
    return bucket.rows


def parse_status_doc(text):
    """Rows from the master status list: '"Name"' lines and their bullets."""
    found = []
    section = ""
    current = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        head = re.match(r'^["“](.+?)["”]\s*(\(.*\))?\s*$', stripped)
        if head and not line.startswith((" ", "\t")):
            current = {"name": head.group(1).strip(), "section": section,
                       "summary": "", "line": number}
            found.append(current)
            continue
        letters = [ch for ch in stripped if ch.isalpha()]
        if (letters and not line.startswith((" ", "\t"))
                and sum(ch.isupper() for ch in letters) >= 0.8 * len(letters)
                and len(letters) >= 6):
            section = re.sub(r"[^A-Za-z &/-]", "", stripped).strip().capitalize()
            current = None
            continue
        desc = re.match(r"^[•*-]?\s*Description:\s*(.+)$", stripped)
        if current is not None and desc and not current["summary"]:
            current["summary"] = shorten(desc.group(1).strip().strip('"“” '))
    return found


def parse_ability_doc(text):
    """Rows from 'Core Abilities:' lists and '<Bro> — <Style> (...)' lists."""
    found = []
    bullet = re.compile(r"^\s*[•*-]\s+(.+?)\s+—\s+(.+)$")
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        block = []
        start = index
        while index < len(lines) and lines[index].strip():
            block.append(lines[index])
            index += 1
        index += 1
        if not block:
            continue
        header = block[0].strip()
        whole = re.match(r"^([^•*-].*?)\s+—\s+(.+?)\s*\(.+\)\s*$", header)
        owner = re.split(r"\s+\(|\s+—", header)[0].strip()
        collecting = bool(whole)
        for offset, line in enumerate(block):
            stripped = line.strip()
            if stripped.lower() == "core abilities:":
                collecting = True
                continue
            match = bullet.match(line)
            if not match:
                if not whole and collecting and offset:
                    collecting = False
                continue
            if collecting:
                name = match.group(1).strip()
                ultimate = bool(re.search(r"\(ultimate\)", name, re.I))
                name = re.sub(r"\s*\(ultimate\)", "", name, flags=re.I)
                found.append({"name": name, "owner": owner,
                              "kind": "Ultimate" if ultimate else "Ability",
                              "summary": shorten(match.group(2)),
                              "line": start + offset + 1})
    return found


def collect_status_and_abilities(ctx):
    rows = []
    known = set()
    battle = find_dir(ctx.root, "design", "mechanics", "battle")
    status_doc = battle + "/status_effects.md" if battle else ""
    if ctx.exists(status_doc):
        for item in parse_status_doc(ctx.text(status_doc)):
            row = new_row("status_effects_and_abilities", item["name"], "Status effects",
                          doc=status_doc, sources=[status_doc], design_doc=True,
                          kind=item["section"] or "Status effect",
                          summary=item["summary"], line=item["line"])
            row["keys"] = {name_key(item["name"])}
            rows.append(row)
    ability_doc = battle + "/battle_system.md" if battle else ""
    if ctx.exists(ability_doc):
        seen = {}
        for item in parse_ability_doc(ctx.text(ability_doc)):
            key = name_key(item["name"])
            if key in seen:
                continue
            row = new_row("status_effects_and_abilities", item["name"], "Abilities",
                          doc=ability_doc, sources=[ability_doc], design_doc=True,
                          kind="%s (%s)" % (item["kind"], item["owner"]),
                          summary=item["summary"], line=item["line"])
            row["keys"] = {key}
            seen[key] = row
            rows.append(row)
    for row in rows:
        known |= row["keys"]
    for rel, group_key, label in (
            (ctx.data + "/skills/status_effects.json", "status_effects", "Status effects"),
            (ctx.data + "/skills/party_abilities.json", "abilities", "Abilities")):
        if not ctx.data or not ctx.exists(rel):
            continue
        payload = ctx.json(rel)
        entries = payload.get(group_key) if isinstance(payload, dict) else None
        if not isinstance(entries, dict):
            continue
        for key, entry in entries.items():
            if not isinstance(entry, dict):
                continue
            name = first_str(entry, "display_name", "name") or pretty(key)
            if norm(key) in known or name_key(name) in known:
                for row in rows:
                    if row["keys"] & {norm(key), name_key(name)}:
                        row["keys"] |= {norm(key), name_key(name)}
                continue
            row = new_row("status_effects_and_abilities", name, label, id=key,
                          doc=rel, sources=[rel], kind="Engine entry",
                          summary=shorten(first_str(entry, "description", "battle_text")))
            row["keys"] = {norm(key), name_key(name)}
            row["flags"].append("in engine data, not in the design list")
            rows.append(row)
    tokens = ctx.engine_tokens("skills")
    for row in rows:
        row["engine_data"] = bool(row["keys"] & tokens)
    return rows


# ---------------------------------------------------------------- beads

def load_beads(root):
    """Every bead from bd, or (None, reason) when bd cannot be read."""
    exe = shutil.which("bd")
    if not exe:
        return None, "bd not found on PATH"
    try:
        done = subprocess.run([exe, "list", "--all", "--json"], cwd=root,
                              capture_output=True, timeout=180)
        text = done.stdout.decode("utf-8", errors="replace")
        start = text.find("[")
        beads = json.loads(text[start:]) if start >= 0 else None
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        return None, "bd failed: " + shorten(error, 120)
    if not isinstance(beads, list):
        return None, "bd returned no list"
    return beads, ""


def open_bead_blobs(beads):
    blobs = []
    for bead in beads or []:
        if not isinstance(bead, dict) or bead.get("status") == "closed":
            continue
        blob = " ".join(str(bead.get(field) or "") for field in
                        ("title", "description", "acceptance_criteria", "notes"))
        blobs.append((str(bead.get("id", "")), blob.lower()))
    return blobs


def attach_beads(rows, blobs):
    for row in rows:
        if row.get("ambient"):
            continue
        terms = []
        name = row["name"].lower()
        if len(name) >= 8 or (len(name) >= 6 and " " in name):
            terms.append(name)
        ident = row["id"].lower()
        if len(ident) >= 8:
            terms.append(ident)
        if row["doc"].lower().endswith(".md") and not row.get("line"):
            terms.append(row["doc"].lower())
        hits = []
        for bead_id, blob in blobs:
            for term in terms:
                if term in blob and re.search(
                        r"(?<![a-z0-9_])" + re.escape(term) + r"(?![a-z0-9_])", blob):
                    hits.append(bead_id)
                    break
        row["open_beads"] = sorted(set(hits))


# ---------------------------------------------------------------- game elements

def seed_from_audit(ctx, audit_rel):
    """Turn the mechanics gap audit's tables into the game_elements seed."""
    text = ctx.text(audit_rel)
    systems = {sid: [] for sid, _title in SYSTEMS}
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if cells and cells[0].lower() == "mechanic":
            in_table = len(cells) == 8
            continue
        if not in_table or set(stripped) <= set("|-: "):
            continue
        if len(cells) != 8:
            ctx.problems.append({"path": audit_rel,
                                 "error": "table row is not 8 cells: " + cells[0]})
            continue
        mechanic, design, rulings, code, tests, data, left, beads = cells
        system = "other"
        for pattern, target in SYSTEM_RULES:
            if re.search(pattern, mechanic, re.I):
                system = target
                break
        bead_ids = []
        for token in re.split(r"[,;]", re.sub(r"\([^)]*\)", "", beads.replace("*", ""))):
            token = token.strip()
            if re.fullmatch(r"[a-z0-9]{2,6}(\.\d+)?", token) and token != "none":
                bead_ids.append(BEAD_PREFIX + token)
        systems[system].append({
            "name": mechanic.replace("**", ""),
            "designed": design, "rulings_open": rulings, "code": code,
            "tests": tests, "data": data, "whats_left": left.replace("**", ""),
            "beads": bead_ids,
            "design_files": _resolve(ctx, design, ["design/", ""], ""),
            "code_files": _resolve(ctx, code, ["game/", ""], ""),
            "test_files": _resolve(ctx, tests, ["game/tests/unit/", "game/tests/"], ".gd"),
            "data_files": _resolve(ctx, data, ["game/assets/data/", ""], ""),
        })
    return {
        "_source": audit_rel,
        "_note": ("Seed for docs/catalog/game_elements_status.md. Text cells are "
                  "the audit's own words; edit them here when a row changes. "
                  "File lists and bead ids are checked live on every build."),
        "systems": [{"id": sid, "title": title, "elements": systems[sid]}
                    for sid, title in SYSTEMS if systems[sid] or sid != "other"],
    }


def _game_scripts(ctx):
    """basename -> paths of the game's own .gd files (addons and tests left out)."""
    if not hasattr(ctx, "_scripts"):
        index = {}
        for rel in walk(ctx.root, find_dir(ctx.root, "game"), (".gd",)):
            if "/addons/" in rel or "/tests/" in rel:
                continue
            index.setdefault(os.path.basename(rel), []).append(rel)
        ctx._scripts = index
    return ctx._scripts


def _resolve(ctx, cell, prefixes, suffix):
    found = []
    last_dir = ""
    last_path = ""
    for token in re.findall(r"`([^`]+)`", cell):
        token = re.sub(r":\d+(-\d+)?$", "", token.strip())
        if not token or " " in token:
            continue
        candidates = [prefix + token + suffix for prefix in prefixes]
        if last_dir:
            candidates.append(last_dir + "/" + token + suffix)
        if token.startswith("_") and last_path:
            base, ext = os.path.splitext(last_path)
            candidates.insert(0, base + token + ext)
        if "/" not in token and token.endswith(".gd"):
            matches = _game_scripts(ctx).get(token, [])
            if len(matches) == 1:
                candidates.append(matches[0])
        for candidate in candidates:
            candidate = candidate.rstrip("/")
            if ctx.exists(candidate):
                if candidate not in found:
                    found.append(candidate)
                full = os.path.join(ctx.root, candidate)
                last_dir = candidate if os.path.isdir(full) else os.path.dirname(candidate)
                last_path = candidate
                break
    return found


def _presence(ctx, paths):
    present = [p for p in paths if ctx.exists(p)]
    return len(present), len(paths), [p for p in paths if p not in present]


def build_game_elements(ctx, seed, beads, beads_note):
    by_id = {}
    for bead in beads or []:
        if isinstance(bead, dict) and bead.get("id"):
            by_id[str(bead["id"])] = bead
    systems = []
    for system in (seed or {}).get("systems", []):
        rows = []
        for element in system.get("elements", []):
            row = {"name": element.get("name", ""),
                   "whats_left": element.get("whats_left", ""),
                   "data": element.get("data", "")}
            for label, text_key, files_key in (
                    ("designed", "designed", "design_files"),
                    ("built", "code", "code_files"),
                    ("tested", "tests", "test_files")):
                text = element.get(text_key, "")
                paths = element.get(files_key, []) or []
                have, total, missing = _presence(ctx, paths)
                if re.match(r"\s*(none|no)\b", text, re.I):
                    state = "no"
                elif total and have == total:
                    state = "yes"
                elif total and have:
                    state = "partly"
                elif total:
                    state = "files missing"
                else:
                    state = "see note"
                row[label] = {"state": state, "note": text, "files_found": have,
                              "files_listed": total, "missing": missing}
            rulings = element.get("rulings_open", "")
            if re.match(r"\s*none\b", rulings, re.I):
                ruled = "yes"
            elif re.match(r"\s*yes\b", rulings, re.I):
                ruled = "no"
            else:
                ruled = "partly"
            row["ruled"] = {"state": ruled, "note": rulings}
            data_have, data_total, data_missing = _presence(
                ctx, element.get("data_files", []) or [])
            row["data_files_found"] = data_have
            row["data_files_listed"] = data_total
            row["data_missing"] = data_missing
            row["beads"] = []
            for bead_id in element.get("beads", []):
                bead = by_id.get(bead_id)
                if bead is not None:
                    status = str(bead.get("status", "unknown"))
                elif beads is None:
                    status = "unknown"
                else:
                    status = "not found"
                row["beads"].append({"id": bead_id, "status": status,
                                     "title": str((bead or {}).get("title", ""))})
            open_ids = [b["id"] for b in row["beads"]
                        if b["status"] not in ("closed", "not found", "unknown")]
            row["open_beads"] = open_ids
            left = row["whats_left"].strip().lower()
            if left.startswith("nothing"):
                row["status"] = "complete"
            elif row["beads"] and beads is not None and not open_ids:
                row["status"] = "all beads closed; re-check this row"
            elif row["built"]["state"] == "no":
                row["status"] = "not built"
            else:
                row["status"] = "partly built"
            rows.append(row)
        systems.append({"id": system.get("id", ""), "title": system.get("title", ""),
                        "rows": rows})
    return systems


# ---------------------------------------------------------------- output

def cell(value):
    return re.sub(r"\s+", " ", str(value)).replace("|", "\\|").strip() or " "


def yes_no(value):
    if value is None:
        return "n/a"
    return "yes" if value else "no"


def doc_link(rel, out_rel, line=None):
    if not rel:
        return ""
    target = os.path.relpath(rel, out_rel).replace(os.sep, "/")
    label = os.path.basename(rel) + (":%d" % line if line else "")
    return "[%s](%s)" % (label.replace("|", "\\|"), quote(target))


def bead_text(ids, limit=6):
    short = [i.replace(BEAD_PREFIX, "") for i in ids]
    if len(short) > limit:
        return ", ".join(short[:limit]) + " +%d more" % (len(short) - limit)
    return ", ".join(short)


def row_status(row):
    if row["design_doc"] and row["engine_data"]:
        return "designed, in engine data"
    if row["design_doc"]:
        return "designed, not in engine data"
    if row["engine_data"]:
        return "engine data only"
    return "unknown"


def find_duplicates(all_rows):
    groups = {}
    for row in all_rows:
        if row.get("ambient"):
            continue
        key = name_key(row["name"])
        if key:
            groups.setdefault(key, []).append(row)
    duplicates = []
    for key in sorted(groups):
        rows = groups[key]
        if len(rows) < 2:
            continue
        categories = {r["category"] for r in rows}
        duplicates.append({
            "name": rows[0]["name"],
            "scope": "same category" if len(categories) < len(rows) else "across categories",
            "entries": [{"category": r["category"], "city": r["city"],
                         "name": r["name"], "id": r["id"], "doc": r["doc"]} for r in rows],
        })
    return duplicates


def header(title, stamp):
    return ["> Generated %s; %s." % (stamp, HEADER_NOTE), "", "# " + title, ""]


def table(rows, out_rel, group_label, extra=()):
    head = ["Name", group_label, "Kind", "Detail", "Doc", "Design doc",
            "Engine data", "Art"] + [label for label, _key in extra] + ["Open beads", "Flags"]
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for row in rows:
        cells = [row["name"], row["area"], row["kind"], row["summary"],
                 doc_link(row["doc"], out_rel, row.get("line")),
                 yes_no(row["design_doc"]), yes_no(row["engine_data"]), yes_no(row["art"])]
        cells += [yes_no(row.get(key)) for _label, key in extra]
        cells += [bead_text(row["open_beads"]), "; ".join(row["flags"])]
        lines.append("| " + " | ".join(cell(c) for c in cells) + " |")
    return lines + [""]


def duplicates_section(duplicates, category, out_rel):
    mine = [d for d in duplicates if any(e["category"] == category for e in d["entries"])]
    lines = ["## Duplicate names", ""]
    if not mine:
        return lines + ["None found in this category.", ""]
    lines += ["Every name in the game must be unique. Each line is one name that "
              "appears more than once. \"Across categories\" can be one thing "
              "listed in two places; check before renaming.", ""]
    for dup in mine:
        places = "; ".join("%s / %s (%s)" % (e["category"], e["city"] or "no city",
                                             doc_link(e["doc"], out_rel) or "no doc")
                           for e in dup["entries"])
        lines.append("- **%s** (%s): %s" % (cell(dup["name"]), dup["scope"], places))
    return lines + [""]


def sort_rows(rows):
    return sorted(rows, key=lambda r: (r["city"].lower(), r["name"].lower(), r["doc"]))


def counts_line(rows):
    total = len(rows)
    return ("%d rows. Design doc: %d. In engine data: %d. Art found: %d. "
            "With open beads: %d. No summary in doc: %d." % (
                total, sum(r["design_doc"] for r in rows),
                sum(r["engine_data"] for r in rows),
                sum(1 for r in rows if r["art"]),
                sum(1 for r in rows if r["open_beads"]),
                sum(1 for r in rows if NO_SUMMARY in r["flags"])))


def render_category(title, category, rows, duplicates, stamp, out_rel, intro,
                    group_label="Area", extra=(), by_group=None, tail=()):
    lines = header(title, stamp) + [intro, "", counts_line(rows), ""]
    if by_group:
        for group_id, group_title in by_group:
            members = sort_rows([r for r in rows if r.get("group") == group_id])
            if not members:
                continue
            lines += ["## %s (%d)" % (group_title, len(members)), ""]
            for member in members:
                member["area"] = member["city"]
            lines += table(members, out_rel, "City", extra)
    else:
        for city in sorted({r["city"] for r in rows}, key=str.lower):
            members = sort_rows([r for r in rows if r["city"] == city])
            lines += ["## %s (%d)" % (city or "No city", len(members)), ""]
            lines += table(members, out_rel, group_label, extra)
    lines += duplicates_section(duplicates, category, out_rel)
    lines += list(tail)
    return "\n".join(lines).rstrip() + "\n"


def state_cell(part, out_rel=None):
    text = part["state"].capitalize()
    if part.get("files_listed"):
        text += " (%d of %d files found)" % (part["files_found"], part["files_listed"])
    if part.get("note"):
        text += ". " + part["note"]
    if part.get("missing"):
        text += " Missing now: " + ", ".join(part["missing"])
    return text


def render_game_elements(systems, stamp, seed_rel, source, beads_note):
    lines = header("Game elements: where we are", stamp)
    lines += ["One table per system. The wording comes from `%s` (seeded from "
              "`%s`); the file counts and bead statuses are checked on every "
              "build, so closing a bead or adding a test changes this page." % (
                  seed_rel, source or "the mechanics gap audit"), ""]
    if beads_note:
        lines += ["**Bead statuses are missing from this build:** %s." % beads_note, ""]
    lines += ["## Summary", "",
              "| System | Elements | Complete | Partly built | Not built | Open beads |",
              "|---|---|---|---|---|---|"]
    for system in systems:
        rows = system["rows"]
        open_ids = sorted({b for r in rows for b in r["open_beads"]})
        lines.append("| %s | %d | %d | %d | %d | %d |" % (
            cell(system["title"]), len(rows),
            sum(r["status"] == "complete" for r in rows),
            sum(r["status"] == "partly built" for r in rows),
            sum(r["status"] == "not built" for r in rows), len(open_ids)))
    lines.append("")
    for system in systems:
        lines += ["## " + system["title"], ""]
        if not system["rows"]:
            lines += ["No elements recorded for this system yet. Add them to `%s`."
                      % seed_rel, ""]
            continue
        lines += ["| Element | Status | Designed | Ruled | Built | Tested | Data | "
                  "What's left | Bead ids |", "|---|---|---|---|---|---|---|---|---|"]
        for row in system["rows"]:
            data = row["data"]
            if row["data_files_listed"]:
                data += " (%d of %d files found)" % (row["data_files_found"],
                                                     row["data_files_listed"])
            beads = ", ".join("%s (%s)" % (b["id"].replace(BEAD_PREFIX, ""), b["status"])
                              for b in row["beads"]) or "none"
            ruled = row["ruled"]["state"].capitalize()
            if row["ruled"]["state"] != "yes":
                ruled += ". Open: " + row["ruled"]["note"]
            cells = [row["name"], row["status"], state_cell(row["designed"]), ruled,
                     state_cell(row["built"]), state_cell(row["tested"]), data,
                     row["whats_left"], beads]
            lines.append("| " + " | ".join(cell(c) for c in cells) + " |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def public_row(row):
    out = {key: row[key] for key in ("name", "id", "city", "area", "kind", "summary", "doc")}
    out["status"] = row_status(row)
    out["design_doc"] = row["design_doc"]
    out["engine_data"] = row["engine_data"]
    out["art"] = row["art"]
    out["open_beads"] = row["open_beads"]
    out["flags"] = row["flags"]
    out["sources"] = row["sources"]
    for key in ("group", "line", "in_quest_log", "ambient"):
        if key in row:
            out[key] = row[key]
    return out


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


CATEGORY_TITLES = [
    ("locations", "Locations"),
    ("npcs", "NPCs"),
    ("items", "Items"),
    ("enemies_and_villains", "Enemies and villains"),
    ("quests", "Quests"),
    ("status_effects_and_abilities", "Status effects and abilities"),
]


def build(root, out_rel="docs/catalog", seed_rel="Tools/catalog/game_elements.json",
          beads=None, beads_note="", now=None):
    """Build every catalogue file under root/out_rel. Returns the JSON payload."""
    ctx = Context(root)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")

    locations, other_docs = collect_locations(ctx)
    npcs, villain_bucket = collect_npcs_and_villains(ctx)
    rows = {
        "locations": locations,
        "npcs": npcs,
        "items": collect_items(ctx),
        "enemies_and_villains": collect_enemies(ctx, villain_bucket),
        "quests": collect_quests(ctx),
        "status_effects_and_abilities": collect_status_and_abilities(ctx),
    }
    blobs = open_bead_blobs(beads)
    all_rows = []
    for category_rows in rows.values():
        attach_beads(category_rows, blobs)
        for row in category_rows:
            if not row["summary"] and not row.get("ambient"):
                row["flags"].append(NO_SUMMARY)
            extra_docs = [s for s in row["sources"]
                          if s.lower().endswith(".md") and s != row["doc"]]
            if extra_docs and row["doc"].lower().endswith(".md"):
                row["flags"].append("more than one doc for the same id: also " +
                                    ", ".join(extra_docs))
            if row.get("alt_ids"):
                row["flags"].append("id differs between sources: also " +
                                    ", ".join(row["alt_ids"]))
        all_rows.extend(category_rows)
    duplicates = find_duplicates(all_rows)

    bead_line = ("Open beads are matched by name, id or doc path in the bead text."
                 if not beads_note else
                 "**Open beads are missing from this build:** %s." % beads_note)
    intro = ("Design doc, engine data and art are yes/no from files found in the "
             "repo. Detail is copied from the doc; blank means the doc has no "
             "tagline or description line. " + bead_line)
    out_dir = os.path.join(root, out_rel)

    tail = []
    if other_docs:
        tail = ["## Other docs in the city folders", "",
                "These have no Location ID, so they are not counted as locations.", ""]
        tail += ["- %s: %s (%s)" % (d["city"], cell(d["title"]), doc_link(d["doc"], out_rel))
                 for d in other_docs] + [""]
    write(os.path.join(out_dir, "locations.md"), render_category(
        "Locations", "locations", rows["locations"], duplicates, stamp, out_rel, intro,
        tail=tail))
    write(os.path.join(out_dir, "npcs.md"), render_category(
        "NPCs", "npcs", rows["npcs"], duplicates, stamp, out_rel,
        intro + " Ambient groups are listed but left out of the duplicate check.",
        group_label="Location"))
    write(os.path.join(out_dir, "items.md"), render_category(
        "Items", "items", rows["items"], duplicates, stamp, out_rel, intro,
        by_group=ITEM_GROUPS))
    write(os.path.join(out_dir, "enemies_and_villains.md"), render_category(
        "Enemies and villains", "enemies_and_villains", rows["enemies_and_villains"],
        duplicates, stamp, out_rel, intro, group_label="Where"))
    write(os.path.join(out_dir, "quests.md"), render_category(
        "Quests", "quests", rows["quests"], duplicates, stamp, out_rel, intro,
        group_label="Location", extra=(("In Quest Log", "in_quest_log"),)))
    write(os.path.join(out_dir, "status_effects_and_abilities.md"), render_category(
        "Status effects and abilities", "status_effects_and_abilities",
        rows["status_effects_and_abilities"], duplicates, stamp, out_rel, intro,
        group_label="Area"))

    seed = ctx.json(seed_rel) if ctx.exists(seed_rel) else None
    if seed is None and not ctx.exists(seed_rel):
        ctx.problems.append({"path": seed_rel, "error": "seed file missing"})
    systems = build_game_elements(ctx, seed, beads, beads_note)
    write(os.path.join(out_dir, "game_elements_status.md"), render_game_elements(
        systems, stamp, seed_rel, (seed or {}).get("_source", ""), beads_note))

    payload = {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "Tools/catalog/build_catalog.py",
        "beads_note": beads_note,
        "categories": [{"id": cid, "title": title, "file": cid + ".md",
                        "count": len(rows[cid]),
                        "rows": [public_row(r) for r in sort_rows(rows[cid])]}
                       for cid, title in CATEGORY_TITLES],
        "game_elements": systems,
        "duplicates": duplicates,
        "other_location_docs": other_docs,
        "problems": ctx.problems,
    }
    write(os.path.join(out_dir, "catalog.json"),
          json.dumps(payload, indent=1, ensure_ascii=False) + "\n")
    return payload


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(here)))
    parser.add_argument("--out", default="docs/catalog")
    parser.add_argument("--seed", default="Tools/catalog/game_elements.json")
    parser.add_argument("--beads-json", help="read beads from a file instead of running bd")
    parser.add_argument("--no-beads", action="store_true", help="skip bd")
    parser.add_argument("--seed-from-audit", metavar="MD",
                        help="rewrite the seed file from the audit's tables, then build")
    args = parser.parse_args(argv)
    root = os.path.abspath(args.root)

    if args.seed_from_audit:
        ctx = Context(root)
        seed = seed_from_audit(ctx, args.seed_from_audit.replace(os.sep, "/"))
        write(os.path.join(root, args.seed),
              json.dumps(seed, indent=1, ensure_ascii=False) + "\n")
        print("seed: %d elements written to %s" % (
            sum(len(s["elements"]) for s in seed["systems"]), args.seed))

    beads, note = None, ""
    if args.no_beads:
        note = "bd was skipped (--no-beads)"
    elif args.beads_json:
        try:
            beads = json.loads(read_text(args.beads_json))
        except (OSError, ValueError) as error:
            note = "could not read %s: %s" % (args.beads_json, shorten(error, 80))
    else:
        beads, note = load_beads(root)

    payload = build(root, args.out, args.seed, beads, note)
    for category in payload["categories"]:
        print("%-30s %4d rows" % (category["id"], category["count"]))
    print("%-30s %4d rows in %d systems" % (
        "game_elements", sum(len(s["rows"]) for s in payload["game_elements"]),
        len(payload["game_elements"])))
    print("duplicate names: %d   unreadable files: %d   beads: %s" % (
        len(payload["duplicates"]), len(payload["problems"]),
        note or "%d read" % len(beads or [])))
    print("written to %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
