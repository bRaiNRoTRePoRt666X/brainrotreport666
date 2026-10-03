# Creative

Concepts, scripts and designs every episode. Full role, KPIs and tools: [`docs/departments/creative.md`](../../docs/departments/creative.md). File naming rules: [`NAMING_CONVENTION.md`](NAMING_CONVENTION.md).

| Folder | Prefix | Holds |
|--------|--------|-------|
| `scripts/` | `SCRIPT` | Outlines, drafts, final scripts (Markdown), plus the Python tools below |
| `storyboards/` | `SB` | Visual planning, shot lists, timing |
| `graphics/` | `GFX` | Lower thirds, title cards, overlays |
| `thumbnails/` | `THUMB` | Per-platform thumbnails and A/B variants |

Files are named `{PREFIX}-EP###-{TYPE}[-descriptor]-v#.ext`. Never overwrite a file: bump the version.

## Tools
Run from `departments/creative/scripts/` (they import `naming.py` from there). Python 3, standard library only.

```bash
# New script or outline skeleton; picks the next free version
python3 generate-script.py --episode EP003 --title "Title" --topic "About" --runtime 6
python3 generate-script.py --episode EP003 --title "Title" --topic "About" --type OUTLINE

# Check a script before review (--strict also fails on TODOs and unchecked ethics items)
python3 lint-script.py SCRIPT-EP003-DRAFT-v1.md --strict

# Validate names, find missing versions and wrong thumbnail sizes, write a manifest
python3 track-assets.py [--episode EP003] [--write] [--strict]
```

`NAMING_CONVENTION.md` also describes `batch-rename.sh` and two script templates. These are not built yet.

## Handoff to Production
Script approved by `legal-compliance`, storyboard reviewed, graphics ready, thumbnail drafts complete, ethics checklist signed. Then run `./scripts/workflow/handoff.sh EP### creative production` from the repo root.

## Content rules
Scripts, titles and thumbnail text follow the Red Lines in [`docs/ethics/campaign-principles.md`](../../docs/ethics/campaign-principles.md): disclose sponsors and affiliates, source factual claims, no deceptive framing, only licensed assets.

Image, PSD and other binary files are gitignored. Git holds scripts and storyboard text; keep design files in shared storage.
