# 📐 brainrot report 666 — Creative Department Naming Convention

---

## File Naming Format

```
{DEPT}-{EPISODE}-{TYPE}-{descriptor}-v{VERSION}.{ext}
```

### Examples

| File | Dept | What it is |
|------|------|------------|
| `GFX-EP003-LOWERTHIRD-hostname-v1.png` | graphics | Lower third for EP003 |
| `GFX-EP003-TITLECARD-intro-v2.mp4` | graphics | Animated title card |
| `THUMB-EP003-YT-clickbait-topic-v1.jpg` | thumbnails | YouTube thumbnail |
| `THUMB-EP003-IG-story-cover-v1.png` | thumbnails | Instagram story |
| `SB-EP003-COLDOPEN-park-scene-v1.md` | storyboards | Cold open storyboard |
| `SB-EP003-SEG1-interview-setup-v1.pdf` | storyboards | Segment 1 storyboard |
| `SCRIPT-EP003-DRAFT-v1.md` | scripts | First draft script |
| `SCRIPT-EP003-FINAL-v3.md` | scripts | Final approved script |
| `SCRIPT-EP003-OUTLINE-v1.md` | scripts | Episode outline |

---

## Department Prefixes

| Department  | Prefix  |
|-------------|---------|
| graphics    | `GFX`   |
| storyboards | `SB`    |
| thumbnails  | `THUMB` |
| scripts     | `SCRIPT`|

---

## Episode IDs

Format: `EP` + 3-digit zero-padded number

```
EP001, EP002, EP003 ... EP099, EP100
```

---

## Type Tags

### Graphics
| Tag | Meaning |
|-----|---------|
| `LOWERTHIRD` | Lower third / name tag |
| `TITLECARD` | Title card graphic |
| `ENDCARD` | End screen / end card |
| `OVERLAY` | Screen overlay |
| `TRANSITION` | Transition graphic |
| `INFOGRAPHIC` | Data viz / infographic |
| `GRAPHIC` | Generic graphic |

### Thumbnails
| Tag | Meaning |
|-----|---------|
| `YT` | YouTube (1280×720) |
| `IG` | Instagram Feed (1080×1080) |
| `STORY` | Instagram/TikTok Story (1080×1920) |
| `TT` | TikTok cover |

### Storyboards
| Tag | Meaning |
|-----|---------|
| `COLDOPEN` | Cold open sequence |
| `SEG1–SEGn` | Numbered segment |
| `OUTRO` | Outro sequence |
| `FULL` | Full episode storyboard |

### Scripts
| Tag | Meaning |
|-----|---------|
| `OUTLINE` | Episode outline/rundown |
| `DRAFT` | Draft script |
| `FINAL` | Final approved script |
| `REVISED` | Revised after review |

---

## Versioning

Always increment version on changes. Never overwrite.

```
-v1  initial
-v2  revised
-v3  final changes
```

---

## Folder Structure

```
creative/
├── graphics/
│   ├── EP001/
│   ├── EP002/
│   └── incoming/    ← unsorted / new assets
├── storyboards/
│   ├── EP001/
│   └── EP002/
├── thumbnails/
│   ├── EP001/
│   └── EP002/
└── scripts/
    ├── episode-script-template.md
    ├── episode-outline-template.md
    ├── generate-script.py
    ├── lint-script.sh
    ├── track-assets.py
    └── batch-rename.sh
```

---

## Automation

```bash
# Set up folder structure
./scripts/batch-rename.sh --setup

# Preview renames for EP003
./scripts/batch-rename.sh --dry-run all EP003

# Apply renames for EP003
./scripts/batch-rename.sh --rename all EP003

# Lint a script before sending to review
./scripts/lint-script.sh scripts/SCRIPT-EP003-DRAFT-v1.md --strict

# Scan and generate asset manifest
python3 scripts/track-assets.py

# Generate a new script with AI
python3 scripts/generate-script.py \
  --episode EP003 \
  --title "Your Episode Title" \
  --topic "What this episode is about" \
  --runtime 6
```

---

*brainrot report 666 — secretly ethical campaign*
