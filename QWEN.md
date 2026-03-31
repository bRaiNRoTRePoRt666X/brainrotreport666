# Project Context: brainrotreport666 (self-titled)

## Project Overview

**brainrot report 666** is a multi-department periodical content production system operating as a **"secretly ethical campaign"** — creating compelling video content while maintaining integrity, transparency, and positive impact.

This is a **content production management repository** organized around a departmental workflow system for creating, producing, and distributing episodic content across multiple platforms (YouTube, Instagram, TikTok).

### Key Characteristics

- **Type:** Content Production Management System (non-code project)
- **Structure:** Branch-based with each department/content type as a separate branch
- **Mission:** Ethical content creation with full compliance tracking
- **Platforms:** YouTube, Instagram, TikTok

---

## Branch Structure

This repository uses a **branch-per-directory** structure where each major content category lives on its own branch:

| Branch | Contents |
|--------|----------|
| `main` | Root files only: `.gitignore`, `README.md`, `QWEN.md`, `ls.txt` |
| `assets` | General assets and media placeholders |
| `departments` | 8 department working directories (creative, production, post-production, etc.) |
| `docs` | Documentation (departments, workflows, ethics) |
| `episodes` | Episode workflow pipeline (incoming, in-progress, review, ready, published, archived) |
| `logs` | System logs and episode drafts |
| `metadata` | Structured JSON data for episodes, departments, campaigns |
| `scripts` | Automation scripts (workflow, reports) |
| `shared` | Cross-department resources (templates, brand, handoffs) |
| `tmp` | Temporary files |

---

## Episode Workflow

Episodes progress through a structured pipeline:

```
INCOMING → CREATIVE → PRODUCTION → POST-PRODUCTION → REVIEW → READY → PUBLISHED → ARCHIVED
```

### Department Handoffs

Each handoff requires:
1. Deliverables completion
2. Quality standards met
3. Documentation updated
4. Ethics compliance verified
5. Next department notified

**Handoff Script:**
```bash
./workflow/handoff.sh <episode-id> <from-dept> <to-dept>
# Example: ./workflow/handoff.sh EP001 creative production
```

---

## Key Files & Artifacts

| File | Branch | Purpose |
|------|--------|---------|
| `README.md` | `main` | Project overview, mission, workflow diagrams |
| `episodes/template.json` | `metadata` | Episode metadata schema |
| `ethics/campaign-principles.md` | `docs` | Core ethical principles and checklist |
| `workflows/handoff-process.md` | `docs` | Department handoff procedures |
| `workflow/handoff.sh` | `scripts` | Bash script for department handoffs |
| `reports/campaign-ethics.sh` | `scripts` | Ethics compliance report generator |

---

## Ethical Framework

The project operates under **6 secretly ethical principles**:

1. **Transparency** — Clear disclaimers, honest messaging
2. **Consent** — Proper releases, privacy compliance
3. **Fair Compensation** — Documented payments, fair rates
4. **Accuracy** — Fact-checking, source verification
5. **Positive Impact** — Community benefit, no exploitation
6. **Sustainability** — Reasonable schedules, team wellness

### Red Lines (Never Cross)
- No doxxing or revealing private information
- No harassment or targeted attacks
- No misinformation or disinformation
- No exploitation of vulnerable populations
- No undisclosed paid promotions
- No stolen or unlicensed content
- No manipulative dark patterns

---

## Usage Patterns

### Working with Branches

```bash
# Switch to a specific content branch
git checkout departments

# Make changes and commit
git add <files>
git commit -m "Update department files"

# Push to remote
git push origin departments

# Switch back to main
git checkout main
```

### Creating a New Episode

1. Checkout episodes branch: `git checkout episodes`
2. Create episode folder in `incoming/`
3. Use metadata template from `metadata` branch
4. Move through workflow stages via handoff scripts

### Department Workflow

```bash
# Checkout scripts branch
git checkout scripts

# Run handoff
./workflow/handoff.sh EP001 creative production

# Switch to departments branch to work on content
git checkout departments
```

---

## Production Schedule

| Day | Department | Focus |
|-----|------------|-------|
| Mon | Creative | Scripts, storyboards |
| Tue-Wed | Production | Recording, capture |
| Thu-Fri | Post-Production | Edit, QC |
| Sat | Legal + Community | Review, engagement |
| Sun | Distribution | Publish, promote |

---

## Git Conventions

- **Main branch**: Clean, only root configuration files
- **Content branches**: Each major directory is a separate branch
- **Media files**: Excluded via `.gitignore` (mp4, mov, wav, mp3, png, jpg, etc.)
- **Secrets**: Strictly excluded (env files, keys, credentials)

### Branch Naming
- Lowercase directory names: `assets`, `departments`, `docs`, etc.
- Episode branches: `episode/EP001`, `episode/EP002`, etc.

---

## Related Documentation

- `README.md` (main branch) — Full project overview with visual workflow diagrams
- `docs/ethics/campaign-principles.md` (docs branch) — Detailed ethical framework
- `docs/departments/` (docs branch) — Individual department documentation
- `docs/workflows/handoff-process.md` (docs branch) — Handoff procedures

---

## Notes for AI Assistants

- This is a **content production management** project with branch-based organization
- Focus on **workflow organization**, **ethics compliance**, and **documentation**
- When helping with scripts, maintain the existing Bash style (set -e, clear output)
- Respect the ethical framework in all suggestions
- Media files are intentionally git-ignored
- Episode IDs follow pattern: `EP001`, `EP002`, etc.
- Always check which branch you're on before making changes
