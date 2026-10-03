#!/usr/bin/env python3
"""Generate a script or outline skeleton for an episode.

Writes SCRIPT-EP###-DRAFT-vN.md (or OUTLINE) into departments/creative/scripts/.
Never overwrites: if a version exists, the next free version is used.

  python3 generate-script.py --episode EP003 --title "Title" \
      --topic "What it is about" --runtime 6
  python3 generate-script.py --episode EP003 --title "T" --topic "X" --type OUTLINE
"""

import argparse
import re
import sys
from datetime import date

from naming import CREATIVE_DIR, EPISODE_RE

SCRIPTS_DIR = CREATIVE_DIR / "scripts"
WORDS_PER_MIN = 150
HOOK_SECONDS = 5


def mmss(seconds):
    return f"{int(seconds) // 60}:{int(seconds) % 60:02d}"


def next_version(episode, kind):
    taken = [
        int(m.group(1))
        for p in SCRIPTS_DIR.glob(f"SCRIPT-{episode}-{kind}-v*.md")
        if (m := re.search(r"-v(\d+)\.md$", p.name))
    ]
    return max(taken, default=0) + 1


def body_segments(runtime_min, count):
    """Split the time after the hook and before the CTA evenly across segments."""
    total = runtime_min * 60
    cta = min(20, total // 6)
    avail = total - HOOK_SECONDS - cta
    each = avail // count
    start = HOOK_SECONDS
    for i in range(1, count + 1):
        end = start + each if i < count else total - cta
        yield i, start, end
        start = end
    return


def render(args, version):
    total = args.runtime * 60
    cta_start = total - min(20, total // 6)
    lines = [
        f"# SCRIPT-{args.episode}-{args.type}-v{version}: {args.title}",
        "",
        f"- **Episode:** {args.episode}",
        f"- **Topic:** {args.topic}",
        f"- **Runtime target:** {args.runtime} min (~{args.runtime * WORDS_PER_MIN} words)",
        f"- **Created:** {date.today().isoformat()}",
        "- **Status:** " + args.type.lower(),
        "",
        "## Hook",
        f"`0:00 - 0:{HOOK_SECONDS:02d}`",
        "",
        "TODO: first line that earns the next 5 seconds. No claim here that the body can't back up.",
        "",
        "## Body",
        "",
    ]
    for i, start, end in body_segments(args.runtime, args.segments):
        lines += [
            f"### Segment {i}: TODO title",
            f"`{mmss(start)} - {mmss(end)}`",
            "",
            "- **Point:** TODO",
            "- **Visual / B-roll:** TODO",
            "- **Claim needing a source:** TODO (cite in Sources)",
            "",
        ]
    lines += [
        "## Call to Action",
        f"`{mmss(cta_start)} - {mmss(total)}`",
        "",
        "TODO",
        "",
        "## Sources",
        "",
        "Every factual claim above needs a link or citation here.",
        "",
        "1. TODO",
        "",
        "## Disclosures",
        "",
        "- Sponsors / paid promotion: TODO (write `None` if none)",
        "- Affiliate links: TODO (write `None` if none)",
        "- AI-generated or licensed assets used: TODO",
        "",
        "## Ethics Checklist",
        "",
        "- [ ] Claims fact-checked and sourced",
        "- [ ] No deceptive editing or misleading framing",
        "- [ ] Sponsors and affiliates disclosed",
        "- [ ] All assets licensed or original",
        "- [ ] Reviewed by legal-compliance",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episode", required=True, help="e.g. EP003")
    ap.add_argument("--title", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--runtime", type=int, default=6, help="minutes (default 6)")
    ap.add_argument("--segments", type=int, default=3, help="body segments (default 3)")
    ap.add_argument("--type", choices=["DRAFT", "OUTLINE"], default="DRAFT")
    args = ap.parse_args()

    if not EPISODE_RE.match(args.episode):
        ap.error("episode must look like EP003")
    if args.runtime < 1 or args.segments < 1:
        ap.error("runtime and segments must be at least 1")
    if args.runtime * 60 < HOOK_SECONDS + 30 + args.segments * 5:
        ap.error("runtime too short for that many segments")

    version = next_version(args.episode, args.type)
    out = SCRIPTS_DIR / f"SCRIPT-{args.episode}-{args.type}-v{version}.md"
    out.write_text(render(args, version), encoding="utf-8")
    print(f"wrote {out.relative_to(CREATIVE_DIR.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
