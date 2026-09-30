# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Folder-and-docs scaffolding for **brainrot report 666**, a multi-department periodical video series (YouTube, Instagram, TikTok) run as a "secretly ethical campaign". It is not a software project: there is no build, package manager, test suite, or CI. It holds a department directory tree, an episode pipeline of stage folders, process docs, one metadata template, and two Bash scripts. Most folders are empty, held in git by `.gitkeep`.

The default branch is `Brainrotreport666`, not `main`.

"Script" means two things here: an episode screenplay (`departments/creative/scripts/SCRIPT-EP003-DRAFT-v1.md`) or Bash automation (root `scripts/`).

## The docs describe more than exists

`README.md` and `departments/creative/NAMING_CONVENTION.md` were written ahead of the implementation. These are referenced but **do not exist**:

- `scripts/workflow/new-episode.sh`, `scripts/reports/department-status.sh` (README Quick Start)
- `config/`, `.github/workflows/`, `scripts/automation/`, `docs/sop/` (README tree)
- The creative tooling in NAMING_CONVENTION.md: `batch-rename.sh`, `lint-script.sh`, `track-assets.py`, `generate-script.py`, the script/outline templates, and per-episode `EP###/` subfolders

Check that a path exists before telling anyone to run it. If asked to build one of these, treat the doc that describes it as the spec.

## Commands

Scripts use relative paths — run them from the repo root.

```bash
# Record a department handoff -> shared/handoffs/<EP>_<from>_to_<to>.log
./scripts/workflow/handoff.sh EP001 creative production

# Ethics report (currently broken, see below)
./scripts/reports/campaign-ethics.sh

# Checks (no linter or tests are configured). Loop: `bash -n a.sh b.sh` only checks a.sh.
for f in scripts/*/*.sh; do bash -n "$f"; done
python3 -m json.tool metadata/episodes/template.json > /dev/null
```

`handoff.sh` only writes a log: it does not move episode folders or edit metadata, and it overwrites an existing log for the same episode/from/to. It does not validate department names — only `creative`, `production`, `post-production`, and `distribution` get a checklist; any other name yields a log with no checklist.

`campaign-ethics.sh` exits with a syntax error partway through: line 26 (the `DEPARTMENT ETHICS COMPLIANCE` header) is missing its leading `echo "`, which throws off quote pairing so bash reports the error at line 56. Even once fixed, the "RED FLAGS CHECK" section prints hardcoded ✓ lines rather than checking anything, and the `[episode-id]` argument in its usage line is never read.

## Architecture

**Department names are identifiers.** The directory names under `departments/` (hyphenated: `post-production`, `legal-compliance`) are also the `case` branches in `handoff.sh`, the loop list in `campaign-ethics.sh`, the keys in `metadata/episodes/template.json`, and the paths in `docs/departments/*.md`. Renaming or adding a department means updating all of them (plus a `.gitkeep` for each new empty subfolder).

**An episode's state lives in three places, and nothing keeps them in sync:**

1. Its folder under `episodes/<stage>/` — stages run `incoming → in-progress → review → ready → published → archived`.
2. Its metadata, built from `metadata/episodes/template.json` — per-department status and sign-offs, platform IDs, budget, analytics. `episode.status` starts at `incoming`.
3. Its handoff logs in `shared/handoffs/`.

Moving an episode forward means updating each by hand.

**Ethics gates every handoff.** `legal-compliance` and `finance` support all stages; `docs/workflows/handoff-process.md` shows which review gates which handoff. The phase checklist and "Red Lines" in `docs/ethics/campaign-principles.md` are requirements for any content produced here (scripts, titles, SEO copy, thumbnail text): disclose sponsors and affiliates, fact-check claims, no deceptive editing, no unlicensed assets.

## Naming

- Episode IDs: `EP` + zero-padded 3-digit number (`EP001`).
- Creative files: `{PREFIX}-{EPISODE}-{TYPE}-{descriptor}-v{VERSION}.{ext}` with prefixes `GFX`, `SB`, `THUMB`, `SCRIPT`. Type tags and thumbnail sizes are in `departments/creative/NAMING_CONVENTION.md`. Never overwrite a version — bump `-vN`.

## What git tracks

- Binary media is gitignored: video, audio, images, editor projects (`.prproj`, `.aep`, `.drx`, `.fcpxml`), and archives — except `shared/brand/*.png`. Git holds structure, docs, metadata, and text deliverables (e.g. Markdown scripts). Don't force-add media.
- `shared/handoffs/*.log` is **not** ignored — handoff logs created while testing show up as untracked files. Delete them, or run the script in a throwaway clone.
- `logs/*.log`, `logs/*.debug`, and `tmp/*` are ignored; other files in `logs/` (e.g. the dated note `logs/20260329`) are tracked.
