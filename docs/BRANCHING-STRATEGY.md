# Branching Strategy

## Overview

This document defines the branching model for the brainrotreport666 production repository.

## Branch Types

### Protected Branches

| Branch | Purpose | Merge From |
|--------|---------|------------|
| `main` | Production-ready, published content | `develop` only |
| `develop` | Integration branch, active episodes | `episode/*` branches |

### Feature Branches

| Pattern | Purpose | Lifetime |
|---------|---------|----------|
| `episode/EP###` | Single episode production | Days to weeks |
| `campaign/name` | Multi-episode campaigns | Weeks to months |
| `hotfix/description` | Urgent fixes | Hours to days |

### Example Branch Names

```
episode/EP001-intro-to-campaign
episode/EP042-community-feedback
campaign/q1-2026-launch
campaign/ethics-review-2026
hotfix/fix-episode-credits
hotfix/update-disclaimers
```

## Workflow

### Starting a New Episode

```bash
# 1. Ensure you're on develop with latest changes
git checkout develop
git pull origin develop

# 2. Create episode branch
git checkout -b episode/EP001

# 3. Work through production stages
#    - Creative: scripts, storyboards
#    - Production: footage, audio
#    - Post: editing, QC
#    - Distribution: publish prep
```

### Episode Handoffs

At each department handoff, commit your changes:

```bash
git add departments/creative/
git commit -m "feat(episode/EP001): creative handoff complete

- Script approved by legal
- Storyboard finalized
- Thumbnails ready

Ethics: [x] Review passed"

git push origin episode/EP001
```

### Completing an Episode

```bash
# 1. Open PR on GitHub: episode/EP001 → develop
# 2. Request review from department leads
# 3. Address feedback
# 4. Merge when approved (squash merge)

# 5. Delete branch after merge
git branch -d episode/EP001
git push origin --delete episode/EP001
```

### Publishing to Main

Weekly or batch basis:

```bash
# 1. Create PR: develop → main
# 2. Include episode changelog
# 3. Require ethics review approval
# 4. Merge with squash or rebase
```

## Branch Protection

### Main Branch Rules

- ✅ Require pull request
- ✅ Require 1 approval
- ✅ Require status checks pass
- ✅ Require branch up to date
- ✅ Require conversation resolution
- ✅ Dismiss stale approvals
- ✅ No force pushes
- ✅ No deletions

### Develop Branch Rules

- ✅ Require pull request
- ✅ Require 1 approval
- ✅ Require status checks pass
- ✅ No force pushes

## Conflict Resolution

1. **Pull latest** from target branch
2. **Rebase** your feature branch
3. **Resolve conflicts** locally
4. **Test** changes
5. **Force push** (only on feature branches)

```bash
git checkout episode/EP001
git fetch origin
git rebase origin/develop
# Resolve conflicts...
git add <resolved files>
git rebase --continue
git push --force-with-lease origin episode/EP001
```

## Emergency Hotfixes

For urgent fixes to published content:

```bash
# 1. Branch from main
git checkout main
git checkout -b hotfix/fix-credits

# 2. Make minimal fix
git commit -m "fix(episode/EP042): correct attribution credit"

# 3. PR to main (expedited review)
# 4. After merge, cherry-pick to develop
git checkout develop
git cherry-pick <hotfix-commit-hash>
git push origin develop
```

## Archive Strategy

Old episode branches can be archived:

```bash
# Create archive branch (optional)
git checkout -b archive/episode/EP001 episode/EP001
git push origin archive/episode/EP001

# Delete original
git push origin --delete episode/EP001
```

## Quick Reference

| Action | Command |
|--------|---------|
| Start episode | `git checkout develop && git checkout -b episode/EP###` |
| Push episode | `git push origin episode/EP###` |
| Update from develop | `git fetch && git rebase origin/develop` |
| Complete episode | Create PR: `episode/EP###` → `develop` |
| Publish batch | Create PR: `develop` → `main` |
| Hotfix | `git checkout main && git checkout -b hotfix/*` |
