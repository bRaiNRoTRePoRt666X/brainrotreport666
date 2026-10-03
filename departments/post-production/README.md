# Post-Production

Turns raw footage into publishable episodes. Full role, KPIs and tools: [`docs/departments/post-production.md`](../../docs/departments/post-production.md).

| Folder | Holds |
|--------|-------|
| `editing/` | Assembly and fine cuts, pacing and continuity notes |
| `vfx/` | Effects, motion graphics, compositing |
| `color/` | Correction and grading, LUTs |
| `audio/` | Dialogue editing, mixing, loudness |
| `sound-design/` | SFX, music, ambience |
| `qc/` | Technical, platform and ethics checks |

The final export goes to `episodes/ready/` as MP4 (H.264).

## Handoffs
- **In:** from Production, with footage, synced audio and the production log complete.
- **Out, to Distribution:** final export done, QC passed, all versions rendered, metadata complete, legal compliance verified.

Record it with `./scripts/workflow/handoff.sh EP### post-production distribution` from the repo root.

## Conventions
- QC includes ethics verification: no deceptive editing, no unlicensed music or footage, sponsor and affiliate disclosures present.
- Video, audio and editor project files (`.prproj`, `.aep`, `.drx`, `.fcpxml`) are gitignored. Keep notes, QC reports and edit decision text here.
