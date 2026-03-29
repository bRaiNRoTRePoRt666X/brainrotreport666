# Branch Protection Rules

## Main Branch Protection

**Branch:** `main`

### Protection Settings (Configure on GitHub)

Go to: **Settings → Branches → Add branch protection rule**

| Setting | Value |
|---------|-------|
| Branch name pattern | `main` |
| Require a pull request before merging | ✅ Yes |
| Require approvals | ✅ Yes (1 reviewer) |
| Dismiss stale pull request approvals | ✅ Yes |
| Require review from Code Owners | ✅ Yes |
| Require status checks to pass | ✅ Yes |
| Require branches to be up to date | ✅ Yes |
| Require conversation resolution | ✅ Yes |
| Require signed commits | ✅ Recommended |
| Do not allow bypassing | ✅ Yes (except admins) |

### Status Checks Required

| Check | Purpose |
|-------|---------|
| `validate-episode-metadata` | Validate episode JSON schemas |
| `check-ethics-compliance` | Verify ethics checklists complete |
| `lint-scripts` | Lint shell scripts |

### CODEOWNERS

Protected branches require review from designated owners before merging.

---

## Branching Strategy

### Long-Lived Branches

| Branch | Purpose | Protected |
|--------|---------|-----------|
| `main` | Production-ready content | ✅ Yes |
| `develop` | Integration branch for episodes | ✅ Yes |
| `archive/*` | Archived episode versions | ❌ No |

### Feature Branches (Episodes)

| Pattern | Purpose | Example |
|---------|---------|---------|
| `episode/*` | Individual episode production | `episode/EP001` |
| `campaign/*` | Multi-episode campaigns | `campaign/q1-2026` |
| `hotfix/*` | Urgent fixes | `hotfix/fix-credits` |

### Department Branches (Optional)

| Pattern | Purpose | Example |
|---------|---------|---------|
| `dept/*` | Department-specific work | `dept/creative-scripts` |

---

## Workflow

```
feature/episode/*          develop              main
      │                       │                   │
      ├────── PR ────────────►│                   │
      │                       │                   │
      │                       ├────── PR ───────►│
      │                       │                   │
      │                       │    (squash merge) │
```

### Episode Development Flow

1. **Create episode branch** from `develop`:
   ```bash
   git checkout develop
   git checkout -b episode/EP001
   ```

2. **Work on episode** through production stages:
   - Creative → Production → Post → Distribution
   - Commit at each handoff

3. **Open PR to `develop`** when episode is ready:
   ```bash
   git push origin episode/EP001
   # Create PR on GitHub: episode/EP001 → develop
   ```

4. **Merge to `develop`** after approval

5. **Batch episodes** and PR to `main` weekly:
   ```bash
   # Create PR: develop → main
   # Requires ethics review + approval
   ```

---

## Commit Message Conventions

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | When to use |
|------|-------------|
| `feat` | New episode, feature |
| `fix` | Bug fix, correction |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Restructuring |
| `test` | Adding tests |
| `chore` | Maintenance, config |

### Scopes

- `episode/EP###` — Specific episode
- `creative`, `production`, `post-production`, `distribution`
- `analytics`, `legal`, `community`, `finance`
- `workflow`, `metadata`, `docs`

### Examples

```
feat(episode/EP001): add script draft for intro segment

- Complete hook (first 5 seconds)
- Add call-to-action
- Include source citations

Ethics: [x] Fact-checked
```

```
fix(legal-compliance): update disclaimer template

Add FTC disclosure requirements for affiliate links

Fixes: #42
```

```
docs(departments): update creative SOP

Clarify thumbnail A/B testing process
```

---

## GitHub Settings to Enable

### Repository Settings

1. **Settings → General**
   - [x] Allow squash merging
   - [x] Allow merge commits
   - [x] Allow rebase merging
   - [x] Delete head branch after merge (default)

2. **Settings → Actions**
   - [x] Allow all actions and reusable workflows
   - [x] Require workflow approval for outside collaborators

3. **Settings → Code and automation**
   - [x] Set default branch to `main`
   - [x] Require branch up to date before merging

---

## Enforcement

### Automated Checks

- GitHub Actions validate:
  - Episode metadata schema
  - Ethics checklist completion
  - Script linting
  - Documentation links

### Manual Review

- Legal-compliance sign-off required for:
  - All episodes before publishing
  - Contract changes
  - Policy updates

- Ethics review required for:
  - New campaign launches
  - Sensitive content
  - Community guidelines changes
