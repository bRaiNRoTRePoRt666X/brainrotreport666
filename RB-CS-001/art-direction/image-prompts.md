# Image Prompts — RB-CS-001

## Prompt Architecture

### Global Prompt Fragments (Prepend to all prompts)

#### Style Fragment
```
[Style definition: e.g., Cinematic, Neo-noir, Cyberpunk, Gritty realism, Anime aesthetic, etc.]
```

#### Quality Fragment
```
[Quality modifiers: e.g., 8k, highly detailed, masterpiece, sharp focus, professional lighting, volumetric lighting, ray tracing, octane render]
```

#### Technical Fragment
```
[Technical specs: e.g., --ar 16:9 --v 6 --style raw --q 2 --stylize 750]
```

#### Negative Prompt (Global)
```
[Global negative: ugly, deformed, noisy, blurry, low quality, distortion, artifacts, watermark, text, signature, bad anatomy, extra limbs, missing limbs, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, poorly drawn face, poorly drawn hands, missing fingers, extra fingers, fused fingers, too many fingers, mutated hands, poorly drawn feet, missing toes, extra toes, fused toes, too many toes, mutated feet]
```

---

## Character Prompts

### [Character Name] — Base Prompt
```
[Character description: age, gender, ethnicity, build, distinguishing features, hair, eyes, skin tone] wearing [outfit description], [style fragment], [quality fragment], [lighting fragment], [composition fragment] [technical fragment]
```

### [Character Name] — Expression Variants
| Expression | Prompt Addition |
|---|---|
| Neutral | |
| Angry | |
| Sad | |
| Happy | |
| Fearful | |
| Surprised | |
| Determined | |
| Confused | |

### [Character Name] — Pose Variants
| Pose | Prompt Addition |
|---|---|
| Standing Neutral | |
| Walking | |
| Running | |
| Sitting | |
| Combat Stance | |
| Interacting with [Prop] | |

---

## Environment Prompts

### [Location Name] — Establishing Shot
```
[Environment description: architecture, scale, materials, atmosphere, time of day, weather], [camera: wide angle, low angle, aerial, etc.], [style fragment], [quality fragment], [lighting fragment] [technical fragment]
```

### [Location Name] — Key Angles
| Angle | Prompt |
|---|---|
| [Name] | |
| [Name] | |
| [Name] | |

### [Location Name] — Detail Shots
| Detail | Prompt |
|---|---|
| [Element] | |
| [Element] | |

---

## Scene-Specific Prompts

### Scene 1: [Description]
#### Shot 1.1 — [Description]
```
[Full prompt for this specific shot]
```

#### Shot 1.2 — [Description]
```
[Full prompt for this specific shot]
```

### Scene 2: [Description]
#### Shot 2.1 — [Description]
```
[Full prompt for this specific shot]
```

*Continue for all scenes/shots*

---

## Thumbnail Prompts

### Option A — [Concept]
```
[Thumbnail-specific prompt: high contrast, readable at small scale, emotional hook]
```

### Option B — [Concept]
```
[Thumbnail-specific prompt]
```

### Option C — [Concept]
```
[Thumbnail-specific prompt]
```

---

## Prompt Testing Log

| Prompt ID | Variant | Seed | Result | Rating (1-5) | Notes |
|---|---|---|---|---|---|
| | | | [Link] | | |
| | | | [Link] | | |
| | | | [Link] | | |

---

## Approved Seeds (Locked for Consistency)

| Asset | Seed | Model/Version | Date Locked |
|---|---|---|---|
| [Character Name] | | | |
| [Location Name] | | | |
| [Hero Prop] | | | |

---

## Prompt Evolution Notes
- [Date]: [Change made and why]
- [Date]: [Change made and why]