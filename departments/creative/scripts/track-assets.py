#!/usr/bin/env python3
"""Scan creative asset folders, validate names, and build an asset manifest.

Run from anywhere. Flags invalid names, skipped versions, assets filed under
the wrong episode folder, and thumbnails with the wrong pixel size.

  python3 track-assets.py                 # print summary
  python3 track-assets.py --episode EP003 # one episode only
  python3 track-assets.py --write         # also write ASSET_MANIFEST.json
  python3 track-assets.py --strict        # exit 1 if any problem is found
"""

import argparse
import json
import struct
import sys
from collections import defaultdict
from datetime import datetime, timezone

from naming import CREATIVE_DIR, EPISODE_RE, PREFIXES, THUMB_SIZES, check_name

SKIP = {".gitkeep", ".DS_Store"}
SKIP_DIRS = {"__pycache__"}
MANIFEST = CREATIVE_DIR / "ASSET_MANIFEST.json"


def image_size(path):
    """Width/height of a PNG or JPEG, or None. Stdlib only."""
    try:
        with open(path, "rb") as f:
            head = f.read(26)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                return struct.unpack(">II", head[16:24])
            if head[:2] == b"\xff\xd8":
                f.seek(2)
                while True:
                    marker = f.read(2)
                    if len(marker) < 2 or marker[0] != 0xFF:
                        return None
                    seglen = struct.unpack(">H", f.read(2))[0]
                    if 0xC0 <= marker[1] <= 0xCF and marker[1] not in (0xC4, 0xC8, 0xCC):
                        f.read(1)
                        h, w = struct.unpack(">HH", f.read(4))
                        return w, h
                    f.seek(seglen - 2, 1)
    except (OSError, struct.error):
        pass
    return None


def scan(episode=None):
    assets, problems = [], []
    for folder, prefix in PREFIXES.items():
        base = CREATIVE_DIR / folder
        if not base.is_dir():
            continue
        for path in sorted(p for p in base.rglob("*") if p.is_file() and p.name not in SKIP and not SKIP_DIRS & set(p.parts)):
            rel = path.relative_to(CREATIVE_DIR).as_posix()
            if path.suffix == ".md" and path.parent == base and not path.name.startswith(prefix + "-"):
                continue  # templates like episode-script-template.md
            if path.suffix == ".py" or path.suffix == ".sh":
                continue
            parsed, issues = check_name(path.name)
            if parsed and parsed.prefix != prefix:
                issues.append(f"prefix {parsed.prefix} does not belong in {folder}/ (expects {prefix})")
            parent = path.parent.name
            if parsed and EPISODE_RE.match(parent) and parent != parsed.episode:
                issues.append(f"filed under {parent} but named for {parsed.episode}")
            if parsed and parsed.prefix == "THUMB" and parsed.type in THUMB_SIZES:
                size = image_size(path)
                if size and size != THUMB_SIZES[parsed.type]:
                    issues.append("size %dx%d, expected %dx%d" % (*size, *THUMB_SIZES[parsed.type]))
            if episode and parsed and parsed.episode != episode:
                continue
            if episode and not parsed and episode not in rel:
                continue
            assets.append({
                "path": rel,
                "episode": parsed.episode if parsed else None,
                "type": parsed.type if parsed else None,
                "descriptor": parsed.descriptor if parsed else None,
                "version": parsed.version if parsed else None,
                "bytes": path.stat().st_size,
                "valid": not issues,
            })
            problems += [(rel, i) for i in issues]
    # skipped versions: v1, v3 with no v2
    groups = defaultdict(list)
    for a in assets:
        parsed, _ = check_name(a["path"].rsplit("/", 1)[-1])
        if parsed:
            groups[(a["path"].split("/")[0],) + parsed.series_key].append(parsed.version)
    for key, versions in groups.items():
        missing = sorted(set(range(1, max(versions) + 1)) - set(versions))
        if missing:
            label = "-".join(k for k in key[1:] if k)
            problems.append((key[0] + "/" + label, "missing version(s): " + ", ".join(f"v{v}" for v in missing)))
    return assets, problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episode", help="limit to one episode, e.g. EP003")
    ap.add_argument("--write", action="store_true", help=f"write {MANIFEST.name}")
    ap.add_argument("--strict", action="store_true", help="exit 1 if problems are found")
    args = ap.parse_args()
    if args.episode and not EPISODE_RE.match(args.episode):
        ap.error("episode must look like EP003")

    assets, problems = scan(args.episode)
    by_ep = defaultdict(int)
    for a in assets:
        by_ep[a["episode"] or "(unparsed)"] += 1

    print(f"{len(assets)} asset(s) in {CREATIVE_DIR}")
    for ep in sorted(by_ep):
        print(f"  {ep}: {by_ep[ep]}")
    for rel, issue in problems:
        print(f"  ! {rel}: {issue}")
    print(f"{len(problems)} problem(s)")

    if args.write:
        manifest = {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"), "assets": assets}
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"wrote {MANIFEST.relative_to(CREATIVE_DIR.parent.parent)}")
    return 1 if (args.strict and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
