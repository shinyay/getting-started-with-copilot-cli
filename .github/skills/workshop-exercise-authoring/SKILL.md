---
name: workshop-exercise-authoring
description: Guide for creating or editing workshop exercises in the Copilot CLI learning path. Use this when asked to write, add, modify, or extend exercises in any workshop level.
---

# Workshop Exercise Authoring

When creating or editing exercises for this Copilot CLI workshop, follow these standards precisely.

## Exercise Structure

Every exercise must contain these sections in order:

```markdown
## Exercise N: Title

### Goal
One sentence describing what the learner will achieve.

### Steps

**N.1** First step description:

```
Copilot prompt the learner should type (no language tag on this fence)
```

> Expected: Description of what Copilot should respond with or do.

**N.2** Next step description:
...continue with 4–8 substeps...

### Key Concept: Concept Name
2–4 sentence explanation of the underlying idea. Include a table or tip if helpful.

### ✅ Checkpoint
One sentence confirming what the learner can now do.
```

## Formatting Rules

1. **Headers**: Exercise title is H2 (`##`), subsections are H3 (`###`)
2. **Step numbering**: `**N.M**` — bold, N = exercise number, M = step within exercise
3. **Copilot prompts** (what users type): Fenced code blocks with **no language tag**
4. **Shell commands**: Fenced code blocks with `bash` language tag
5. **Expected output**: Use `> Expected:` blockquotes or fenced blocks with language tags
6. **Tips**: `> 💡` prefix — **Warnings**: `> ⚠️` prefix — **References**: `> 📋` prefix
7. **Separators**: Horizontal rule (`---`) between exercises
8. **Tables**: Use for comparisons, options, structured information

## Content Guidelines

- Reference **real files** from the level's `sample-app/` (use actual paths and function names)
- Copilot prompts should be **realistic** — things a developer would actually ask
- Include **expected output** so learners can verify they're on track
- Build on skills from **earlier exercises** in this level (progressive difficulty)
- Each exercise should take **5–15 minutes** to complete
- Always explain **WHY**, not just HOW — teach the underlying principle

## Exercise Count and Numbering

- Every level has exactly **12 exercises**, numbered 1–12
- If adding an exercise, renumber subsequent exercises
- Update these when exercise count changes:
  - Learning Objectives list (must match exercise count)
  - Self-Assessment (must have one item per exercise)
  - Main README exercise table for this level
  - `workshop/README.md` if total count changes

## Self-Assessment Alignment

Each exercise maps to one self-assessment item:
- Scoring: 1 (need review), 2 (mostly comfortable), 3 (confident)
- Total: 12 items × 3 points = 36 max
- Ready for next level: 30–36 (83%+)
