# 🎬 Episode Production — Work in Progress

> Current episode development tracking

---

## 📍 Current Status

| Episode | Stage | Department | Progress |
|---------|-------|------------|----------|
| EP001 | TBD | TBD | 🟡 Not started |

---

## 🔄 Active Episode Workflow

```
┌─────────────┐
│  INCOMING   │  ← New episode requests go here
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   CREATIVE  │  Scripts → Storyboards → Graphics → Thumbnails
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PRODUCTION │  Footage → Audio → Assets → Logs
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    POST     │  Edit → VFX → Color → Audio → QC
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  DISTRIBUT  │  YouTube → Instagram → TikTok
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PUBLISHED  │  Live on all platforms
└─────────────┘
```

---

## 📁 Episode File Structure

```
episodes/
├── incoming/           # New episode requests
│   └── EP001-request.md
├── in-progress/        # Active production
│   └── EP001/
├── review/             # Awaiting approval
├── ready/              # Approved, scheduled
├── published/          # Live episodes
└── archived/           # Completed

metadata/episodes/
└── EP001.json          # Episode tracking data

departments/creative/scripts/
└── EP001-script.md     # Episode script

shared/handoffs/
└── EP001_*_to_*.log    # Handoff records
```

---

## ✅ Pre-Production Checklist

Before starting episode production:

- [ ] Episode ID assigned (e.g., EP001)
- [ ] Episode title and description defined
- [ ] Metadata file created from template
- [ ] Initial creative brief documented
- [ ] Ethics review scheduled

---

## 🚀 Quick Start — New Episode

### 1. Create Episode Branch

```bash
git checkout develop
git checkout -b episode/EP001
```

### 2. Initialize Episode Files

```bash
# Copy metadata template
cp metadata/episodes/template.json metadata/episodes/EP001.json

# Create episode folder
mkdir -p episodes/in-progress/EP001
```

### 3. Update Metadata

Edit `metadata/episodes/EP001.json`:
```json
{
  "episode": {
    "id": "EP001",
    "title": "Your Episode Title",
    "status": "in-progress"
  }
}
```

### 4. Start Creative Phase

```bash
# Create script file
touch departments/creative/scripts/EP001-draft.md

# Create storyboard folder
mkdir -p departments/creative/storyboards/EP001
```

### 5. Commit Initial Setup

```bash
git add metadata/episodes/EP001.json
git add departments/creative/scripts/EP001-draft.md
git commit -m "feat(episode/EP001): initialize episode production

- Title: [Your Title]
- Status: Creative phase started
- Assigned: [Your name]"
git push origin episode/EP001
```

---

## 📋 Department Handoff Checklist

### Creative → Production

- [ ] Script complete and approved
- [ ] Storyboard finalized
- [ ] Graphics assets ready
- [ ] Thumbnails designed
- [ ] Ethics review passed
- [ ] Handoff log created

### Production → Post-Production

- [ ] All footage captured
- [ ] Audio recorded and synced
- [ ] Files organized
- [ ] Production log complete
- [ ] Best takes marked
- [ ] Safety check signed

### Post-Production → Distribution

- [ ] Final export complete
- [ ] QC passed
- [ ] Metadata complete
- [ ] Disclosures added
- [ ] Compliance verified
- [ ] Handoff approved

---

## 🔧 Useful Commands

```bash
# View current branch
git branch

# Switch to episode branch
git checkout episode/EP001

# Update from develop
git fetch origin && git rebase origin/develop

# Create handoff log
./scripts/workflow/handoff.sh EP001 creative production

# Run ethics check
./scripts/reports/campaign-ethics.sh EP001

# Push changes
git push origin episode/EP001
```

---

## 📞 Need Help?

- **Workflow questions:** See `docs/BRANCHING-STRATEGY.md`
- **Ethics guidelines:** See `docs/ethics/campaign-principles.md`
- **Department SOPs:** See `docs/departments/`
- **Handoff process:** See `docs/workflows/handoff-process.md`

---

## 📅 Production Schedule

| Week | Episode | Phase | Target Date |
|------|---------|-------|-------------|
| 1 | EP001 | Creative | TBD |
| 2 | EP001 | Production | TBD |
| 3 | EP001 | Post | TBD |
| 4 | EP001 | Publish | TBD |

---

**Last updated:** 2026-03-29
**Status:** 🟡 Ready for new episode
