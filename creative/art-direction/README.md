# Art Direction Workspace — COLDSTORY

## Structure

```
creative/art-direction/
├── visual-bibles/       # Series-level visual bibles & style guides
├── character-design/    # Master character sheets, turnarounds, expressions
├── environments/        # Key location master designs
├── color-palettes/      # Series palette system, usage rules
├── lighting/            # Lighting philosophy, reference library
├── props/               # Hero prop master designs
├── wardrobe/            # Costume master designs
├── composition/         # Composition templates, camera language
└── prompts/             # Global prompt fragments, negatives, tech specs
```

## Episode Structure

Each episode gets its own art-direction folder:

```
RB-CS-XXX/
└── art-direction/
    ├── visual-bible.md       # Episode master reference
    ├── characters.md         # Character designs + prompt templates
    ├── environments.md       # Location designs + prompt templates
    ├── color-lighting.md     # Palettes + lighting setups per scene
    ├── props-wardrobe.md     # Prop/wardrobe specs + production tracking
    └── image-prompts.md      # Prompt library + tested seeds
```

## Workflow

1. **Series-level first** — Populate `creative/art-direction/` with master references
2. **Episode-level inherits** — Episode files reference and extend series masters
3. **Lock before generate** — All prompt templates and seeds approved before asset generation
4. **Version everything** — Git tracks all prompt evolution and approval decisions

## Naming Conventions

- Files: `kebab-case.md`
- Prompt IDs: `CHR-{name}-{variant}`, `ENV-{name}-{angle}`, `SCN-{num}-{shot}`
- Seeds: `SEED-{asset}-{version}`
- Assets: `{type}-{id}-{variant}.{ext}`

## Approval Gates

| Gate | Required Approvals |
|---|---|
| Visual Bible | Art Director + Creative Director |
| Character/Location Masters | Art Director + Director |
| Color/Lighting Plan | Art Director |
| Prompt Library (Seeds Locked) | Art Director |
| Episode Package Complete | Art Director + Creative Director + Director |

## Quick Links

- [Art Director Role Definition](../roles/art-director/ROLE.md)
- [Creative Department Overview](../README.md)