# QWEN.md — Project Context

## Project Overview

**brainrotreport666** (self-titled) is a **secretly ethical campaign production system** — a multi-department periodical content creation framework designed for producing video content with integrity. The project operates as an organized repository for managing episode production workflows across 8 departments while maintaining ethical standards behind the scenes.

### Core Mission
- Create compelling, engaging content while maintaining transparency, consent, fair compensation, accuracy, and positive community impact
- Operate with structured departmental handoffs and ethics compliance at every stage

### Project Type
**Non-code project** — This is a content production management system using shell scripts for workflow automation. It organizes documentation, metadata templates, and department coordination rather than traditional software development.

---

## Directory Structure

```
brainrotreport666/
├── departments/              # 8 production departments
│   ├── creative/             # Scripts, storyboards, graphics, thumbnails
│   ├── production/           # Raw footage, audio, assets, logs
│   ├── post-production/      # Editing, VFX, color, audio, QC
│   ├── distribution/         # YouTube, Instagram, TikTok, scheduling
│   ├── analytics/            # Performance metrics, audience, growth
│   ├── legal-compliance/     # Contracts, rights, privacy, ethics
│   ├── community/            # Engagement, moderation, feedback
│   └── finance/              # Budgets, invoices, revenue, expenses
│
├── episodes/                 # Episode pipeline stages
│   ├── incoming/             # New episode requests
│   ├── in-progress/          # Active production
│   ├── review/               # Awaiting approval
│   ├── ready/                # Approved, scheduled
│   ├── published/            # Live episodes
│   └── archived/             # Completed episodes
│
├── scripts/                  # Automation scripts
│   ├── workflow/             # handoff.sh (department transfers)
│   └── reports/              # campaign-ethics.sh (compliance reports)
│
├── docs/                     # Documentation
│   ├── departments/          # Per-department SOPs
│   ├── workflows/            # Process documentation
│   └── ethics/               # Ethical guidelines & principles
│
├── metadata/                 # Structured tracking data
│   ├── episodes/             # Episode JSON templates
│   ├── departments/          # Department tracking
│   └── campaigns/            # Campaign metadata
│
├── shared/                   # Cross-department resources
│   ├── handoffs/             # Inter-department transfer logs
│   ├── brand/                # Brand guidelines & assets
│   ├── templates/            # Reusable templates
│   └── resources/            # Shared assets
│
├── assets/                   # General assets
├── logs/                     # System logs
├── tmp/                      # Temporary files
└── config/                   # Configuration (if needed)
```

---

## Episode Workflow

Episodes progress through a structured pipeline:

```
INCOMING → CREATIVE → PRODUCTION → POST-PRODUCTION → REVIEW → READY → PUBLISHED → ARCHIVED
```

### Department Flow

| Stage | Department | Key Deliverables |
|-------|------------|------------------|
| Creative | creative/ | Scripts, storyboards, graphics, thumbnails |
| Production | production/ | Raw footage, audio recordings, production logs |
| Post-Production | post-production/ | Edited video, VFX, color grade, audio mix, QC |
| Distribution | distribution/ | Platform uploads, scheduling, SEO |
| Analytics | analytics/ | Performance tracking, reports |
| Community | community/ | Engagement, moderation, feedback collection |

### Supporting Departments (All Stages)
- **legal-compliance/** — Ethics review, contracts, rights, privacy compliance
- **finance/** — Budget tracking, invoices, revenue/expenses

---

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, mission, workflow diagrams, ethical principles |
| `scripts/workflow/handoff.sh` | Department transfer script with checklists |
| `scripts/reports/campaign-ethics.sh` | Ethics compliance report generator |
| `metadata/episodes/template.json` | Episode metadata schema (all departments tracked) |
| `docs/ethics/campaign-principles.md` | Core ethical framework and red lines |
| `docs/workflows/handoff-process.md` | Handoff procedure documentation |
| `docs/departments/*.md` | Individual department SOPs and KPIs |
| `.gitignore` | Excludes media files, logs, temp files, secrets |

---

## Usage

### Creating a New Episode
```bash
# Episode files are organized in episodes/incoming/
# Use the metadata template: metadata/episodes/template.json
```

### Department Handoff
```bash
./scripts/workflow/handoff.sh <episode-id> <from-dept> <to-dept>
# Example: ./scripts/workflow/handoff.sh EP001 creative production
```

### Generate Ethics Report
```bash
./scripts/reports/campaign-ethics.sh [episode-id]
```

### Weekly Schedule
| Day | Focus |
|-----|-------|
| Mon | Creative (scripts, storyboards) |
| Tue-Wed | Production (recording, capture) |
| Thu-Fri | Post-Production (edit, QC) |
| Sat | Legal + Community (review, engagement) |
| Sun | Distribution (publish, promote) |

---

## Ethical Framework

The project operates under **6 secretly ethical principles**:

1. **Transparency** — Clear disclaimers, honest messaging, verifiable sources
2. **Consent & Privacy** — Written releases, privacy-respecting data collection
3. **Fair Compensation** — Documented rates, timely payments, no exploitation
4. **Accuracy & Truth** — Multi-source verification, fact vs. opinion clarity
5. **Positive Impact** — Community benefit, no harmful stereotypes
6. **Sustainability** — Reasonable schedules, team wellness, resource efficiency

### Red Lines (Never Cross)
- No doxxing or revealing private information
- No harassment or targeted attacks
- No misinformation/disinformation
- No exploitation of vulnerable populations
- No undisclosed paid promotions
- No stolen or unlicensed content
- No manipulative dark patterns

---

## Metadata Schema

Episodes are tracked via JSON in `metadata/episodes/` with fields for:
- Episode info (id, title, status, timestamps)
- Per-department status (assigned personnel, deliverables, completion flags)
- Ethics checklists (phase-by-phase approval)
- Handoff history
- Analytics data (views, engagement per platform)

---

## Conventions

### File Organization
- Each department has subdirectories matching its function
- Episode IDs follow format: `EP###` (e.g., EP001, EP002)
- Handoff logs named: `{EP_ID}_{from_dept}_to_{to_dept}.log`

### Documentation Style
- Markdown for all documentation
- Department docs include: role, responsibilities, deliverables table, handoff requirements, tools, KPIs
- Ethics checklists embedded in workflow stages

### Git Conventions
- Media files excluded via `.gitignore` (video, audio, large images)
- Logs and temp files excluded
- Brand assets in `shared/brand/` are git-tracked exceptions

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| Scripting | Bash (workflow automation) |
| Writing | Google Docs, Notion, Markdown |
| Design | Photoshop, GIMP, Figma, Storyboarder |
| Video | DaVinci Resolve, Premiere, OBS |
| Audio | Zoom, Rode, Shure hardware |
| Cameras | Sony, Canon, iPhone |

---

## Notes for AI Assistant

- This is a **production management system**, not a software codebase
- Focus on **workflow coordination**, **documentation**, and **ethics compliance**
- When helping with episodes, reference the `metadata/episodes/template.json` schema
- Department handoffs require checklist completion — see `scripts/workflow/handoff.sh`
- Ethics review is mandatory at every stage — see `docs/ethics/campaign-principles.md`
- The `.gitignore` is intentionally permissive for creative work but excludes large media files
