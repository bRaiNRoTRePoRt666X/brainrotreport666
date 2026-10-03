#!/usr/bin/env python3
"""Lint a script before sending it to review.

  python3 lint-script.py SCRIPT-EP003-DRAFT-v1.md
  python3 lint-script.py path/to/script.md --strict

Errors always fail (exit 1). --strict also fails on warnings, including
leftover TODO placeholders, so use it before handoff to legal-compliance.
"""

import argparse
import re
import sys
from pathlib import Path

from naming import SCRIPT_SECTIONS, check_name

NONE_RE = re.compile(r"\bnone\b", re.I)


def sections(text):
    """Map '## Heading' -> body text."""
    parts = re.split(r"^## +(.+?) *$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def lint(path):
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8")

    parsed, problems = check_name(path.name)
    if parsed and parsed.prefix != "SCRIPT":
        problems.append("not a SCRIPT file")
    errors += [f"filename: {p}" for p in problems]
    if parsed and parsed.episode not in text.split("\n", 1)[0]:
        warnings.append(f"title line does not mention {parsed.episode}")

    secs = sections(text)
    is_outline = bool(parsed and parsed.type == "OUTLINE")
    for name in SCRIPT_SECTIONS:
        if name not in secs:
            (warnings if is_outline else errors).append(f"missing section: ## {name}")

    disc = secs.get("Disclosures", "")
    if "Disclosures" in secs and not re.search(r"sponsor", disc, re.I):
        errors.append("Disclosures must state sponsor status (write 'None' if none)")
    if "Disclosures" in secs and not re.search(r"affiliate", disc, re.I):
        errors.append("Disclosures must state affiliate status (write 'None' if none)")

    src = secs.get("Sources", "")
    if "Sources" in secs and not re.search(r"^\s*(\d+\.|[-*])\s+\S", src, re.M):
        errors.append("Sources is empty")
    elif "Sources" in secs and NONE_RE.search(src) and not re.search(r"https?://", src):
        warnings.append("Sources says none; make sure the script makes no factual claims")

    unchecked = re.findall(r"^- \[ \] (.+)$", secs.get("Ethics Checklist", ""), re.M)
    if unchecked:
        warnings.append(f"{len(unchecked)} unchecked ethics item(s)")
    todos = [n for n, line in enumerate(text.splitlines(), 1) if "TODO" in line]
    if todos:
        warnings.append(f"{len(todos)} TODO placeholder(s), first at line {todos[0]}")
    if re.search(r"\bsponsored by\b|\buse code\b|\baffiliate link\b", text, re.I) and not re.search(
        r"sponsor|affiliate", disc, re.I
    ):
        errors.append("promotional language found but Disclosures does not cover it")
    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", type=Path)
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()
    if not args.file.is_file():
        ap.error(f"{args.file} not found")

    errors, warnings = lint(args.file)
    for e in errors:
        print(f"error:   {e}")
    for w in warnings:
        print(f"warning: {w}")
    print(f"{args.file.name}: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
