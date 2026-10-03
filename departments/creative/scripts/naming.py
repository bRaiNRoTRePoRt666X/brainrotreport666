"""Shared naming-convention rules for the creative department.

Spec: departments/creative/NAMING_CONVENTION.md
Format: {PREFIX}-{EPISODE}-{TYPE}[-{descriptor}]-v{VERSION}.{ext}
"""

import re
from dataclasses import dataclass
from pathlib import Path

CREATIVE_DIR = Path(__file__).resolve().parent.parent

# folder -> prefix
PREFIXES = {
    "graphics": "GFX",
    "storyboards": "SB",
    "thumbnails": "THUMB",
    "scripts": "SCRIPT",
}

# prefix -> allowed type tags (SEG# handled separately)
TYPES = {
    "GFX": {"LOWERTHIRD", "TITLECARD", "ENDCARD", "OVERLAY", "TRANSITION", "INFOGRAPHIC", "GRAPHIC"},
    "THUMB": {"YT", "IG", "STORY", "TT"},
    "SB": {"COLDOPEN", "OUTRO", "FULL"},
    "SCRIPT": {"OUTLINE", "DRAFT", "FINAL", "REVISED"},
}

# Pixel sizes from the convention doc (width, height).
THUMB_SIZES = {"YT": (1280, 720), "IG": (1080, 1080), "STORY": (1080, 1920)}

EPISODE_RE = re.compile(r"^EP\d{3}$")
NAME_RE = re.compile(
    r"^(?P<prefix>[A-Z]+)-(?P<episode>EP\d{3})-(?P<type>[A-Z0-9]+)"
    r"(?:-(?P<descriptor>[a-z0-9]+(?:-[a-z0-9]+)*))?"
    r"-v(?P<version>\d+)\.(?P<ext>[A-Za-z0-9]+)$"
)


@dataclass(frozen=True)
class ParsedName:
    prefix: str
    episode: str
    type: str
    descriptor: str
    version: int
    ext: str

    @property
    def series_key(self):
        """Everything except the version: files with the same key are versions of one asset."""
        return (self.prefix, self.episode, self.type, self.descriptor)


def valid_type(prefix, tag):
    if tag in TYPES.get(prefix, ()):
        return True
    return prefix == "SB" and re.fullmatch(r"SEG[1-9][0-9]*", tag) is not None


def check_name(filename):
    """Return (ParsedName | None, [problems]). Empty problems means valid."""
    m = NAME_RE.match(filename)
    if not m:
        return None, ["does not match {PREFIX}-EP###-{TYPE}[-descriptor]-v#.ext"]
    d = m.groupdict()
    parsed = ParsedName(d["prefix"], d["episode"], d["type"], d["descriptor"] or "", int(d["version"]), d["ext"].lower())
    problems = []
    if parsed.prefix not in TYPES:
        problems.append(f"unknown prefix {parsed.prefix!r} (expected one of {', '.join(sorted(TYPES))})")
    elif not valid_type(parsed.prefix, parsed.type):
        problems.append(f"type {parsed.type!r} is not valid for {parsed.prefix}")
    if parsed.version < 1:
        problems.append("version must start at v1")
    if parsed.prefix != "SCRIPT" and not parsed.descriptor:
        problems.append("missing descriptor")
    return parsed, problems


def episode_ids(creative_dir=CREATIVE_DIR):
    """Episode IDs that have a folder in any asset department."""
    found = set()
    for folder in PREFIXES:
        base = creative_dir / folder
        if base.is_dir():
            found.update(p.name for p in base.iterdir() if p.is_dir() and EPISODE_RE.match(p.name))
    return sorted(found)


# Sections every script must contain, in order. Shared by generate-script.py and lint-script.py.
SCRIPT_SECTIONS = [
    "Hook",
    "Body",
    "Call to Action",
    "Sources",
    "Disclosures",
    "Ethics Checklist",
]
