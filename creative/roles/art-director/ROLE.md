# Art Director — COLDSTORY

## Role Definition

The Art Director owns the visual language of the story. They take the creative concept/script and turn it into a consistent visual world across all production touchpoints.

---

## Scope of Authority

| Domain | Responsibility |
|---|---|
| **Graphics** | Visual style, brand consistency, asset standards |
| **Character Appearance** | Design, proportions, color, wardrobe, distinguishing features |
| **Locations & Environments** | Architecture, atmosphere, set dressing, spatial logic |
| **Scene Composition** | Camera angles, framing, visual hierarchy, focal points |
| **Lighting / Mood** | Lighting schemes, color temperature, shadow design, emotional tone |
| **Color Palette** | Master palette, scene palettes, character/location assignments |
| **Wardrobe / Props** | Design specs, material callouts, continuity tracking |
| **Thumbnail Visual Direction** | Concept, composition, hook, brand alignment |
| **AI Image-Generation Prompts** | Prompt architecture, seed locking, quality control |
| **Visual Continuity** | Cross-scene consistency, asset reuse, version control |

---

## Key Distinctions

| Role | Question They Answer |
|---|---|
| **Creative Director** | *What are we saying?* (Concept, theme, narrative intent) |
| **Art Director** | *What should it look like?* (Visual language, style, aesthetics) |
| **Director** | *How do we stage/capture it?* (Blocking, pacing, performance, coverage) |
| **Editor** | *How do we assemble the final experience?* (Rhythm, structure, final polish) |

---

## Deliverables

### Per Episode (RB-CS-XXX/art-direction/)
- `visual-bible.md` — Master reference for the episode's visual identity
- `characters.md` — Character designs, palettes, wardrobe, prompt templates
- `environments.md` — Location designs, lighting, materials, prompt templates
- `color-lighting.md` — Master palettes, scene lighting setups, grading targets
- `props-wardrobe.md` — Prop/wardrobe specs, variations, production tracking
- `image-prompts.md` — Prompt library, tested seeds, evolution log

### Per Series (creative/art-direction/)
- `visual-bibles/` — Series-level visual bible, style guides
- `character-design/` — Master character sheets, turnarounds, expression charts
- `environments/` — Key location master designs
- `color-palettes/` — Series palette system, usage rules
- `lighting/` — Lighting philosophy, reference library
- `props/` — Hero prop master designs
- `wardrobe/` — Costume master designs
- `composition/` — Composition templates, camera language
- `prompts/` — Global prompt fragments, negative prompts, technical specs

---

## Workflow

### Pre-Production
1. **Align with Creative Director** — Receive concept, themes, emotional targets
2. **Develop Visual Bible** — Establish rules before any asset generation
3. **Design Characters/Locations** — Create master designs with prompt templates
4. **Define Color & Lighting** — Lock palettes and lighting schemes per scene
5. **Spec Props/Wardrobe** — Detail hero assets with variations
6. **Build Prompt Library** — Test and lock seeds for consistency
7. **Review with Director** — Ensure visual plan serves staging needs

### Production
1. **Asset Generation Oversight** — Review all generated assets against bible
2. **Continuity Checks** — Verify cross-scene consistency daily
3. **Prompt Iteration** — Refine prompts based on output quality
4. **Approval Gates** — Sign off on hero assets before downstream use

### Post-Production
1. **Final Consistency Pass** — Verify all shots match visual bible
2. **Color Grading Reference** — Provide grading targets to Editor/Colorist
3. **Archive** — Lock final prompts, seeds, and approved assets

---

## Collaboration Interfaces

| Collaborator | Handoff | Receive |
|---|---|---|
| Creative Director | Visual bible for approval | Concept, themes, reference |
| Director | Composition templates, lighting plans | Blocking, coverage needs |
| Storyboard Artist | Visual reference, composition guides | Storyboard feedback |
| Graphic Designer | Style guides, asset specs | Graphic asset review |
| Motion Designer | Color/lighting specs, asset library | Motion tests |
| Thumbnail Designer | Visual hook direction, brand specs | Thumbnail concepts |
| Writer | Visual feasibility feedback | Script updates |
| Editor | Grading targets, continuity notes | Edit feedback |

---

## Quality Standards

- **Zero "Generative Drift"** — No asset enters pipeline without Art Director review
- **Seed Locking** — Hero characters/locations use locked seeds
- **Prompt Versioning** — All prompt changes logged with reason
- **Visual Bible as Law** — Deviations require Art Director approval
- **Cross-Episode Consistency** — Series-level bibles override episode decisions

---

## Tools & References

- **Primary:** Midjourney / Stable Diffusion / Flux / ComfyUI
- **Reference Management:** PureRef, Milanote, or Figma
- **Color:** Adobe Color, Coolors, custom palette files
- **Version Control:** Git (this repo) for all prompt/asset tracking