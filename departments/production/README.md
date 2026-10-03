# Production

Captures all raw footage and audio. Full role, KPIs and tools: [`docs/departments/production.md`](../../docs/departments/production.md).

| Folder | Holds |
|--------|-------|
| `raw-footage/` | Main camera, B-roll and screen recordings |
| `audio/` | Voice and location audio |
| `assets/` | Props, locations, talent and equipment records |
| `logs/` | Per-episode production logs (Markdown): timecodes, takes, issues |

## Handoffs
- **In:** from Creative, with an approved script, storyboard, graphics and ethics sign-off.
- **Out, to Post-Production:** all footage captured, audio synced and cleaned, files named and organized, production log complete, best takes marked, releases collected.

Record it with `./scripts/workflow/handoff.sh EP### production post-production` from the repo root.

## Conventions
- Rights clearance happens at this handoff. Collect releases from talent and confirm licenses for any third-party material before handing on.
- Video and audio files are gitignored. Git holds the production logs and asset records, not the media.
