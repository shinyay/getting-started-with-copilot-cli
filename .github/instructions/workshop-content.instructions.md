---
applyTo: "workshop/**/*.md"
---

# Workshop Content — Markdown Instructions

## File Types

| File | Purpose | Structure |
|------|---------|-----------|
| `README.md` | 12 exercises per level | Goal → Steps → Key Concept → Checkpoint |
| `CHEATSHEET.md` | Quick-reference card | Categorized tables with commands and patterns |

## Exercise Format

Every exercise must follow this structure:

```markdown
## Exercise N: Title

### Goal
One sentence: what the learner will achieve.

### Steps

**N.1** Step description:

(fenced code block with Copilot prompt — no language tag)

> Expected: what should happen.

**N.2** Next step...

### Key Concept: Name

Brief explanation of the underlying concept.

### ✅ Checkpoint
One sentence confirming the learner achieved the goal.
```

## Formatting Rules

- Exercise headers: `## Exercise N: Title` (H2)
- Subsections: `### Goal`, `### Steps`, `### Key Concept`, `### ✅ Checkpoint` (H3)
- Step numbering: `**N.M**` — bold, N = exercise number, M = step within exercise
- Copilot prompts the user should type: fenced code blocks with **no** language tag
- Shell commands: fenced code blocks with `bash` language tag
- Code output: fenced code blocks with appropriate language tag
- Tips: `> 💡` prefix
- Warnings: `> ⚠️` prefix
- Cross-references: `> 📋` prefix
- Horizontal rules (`---`) between exercises

## Self-Assessment Section

Must appear at end of every level README:

- Section header: `## Self-Assessment`
- Numbered list of 12 items (one per exercise)
- Scoring: 1 = need review, 2 = mostly comfortable, 3 = confident
- Total: `/36`
- Ready for next level: **30–36** (83%+)
- Include guidance for scores below threshold

## Cheat Sheet Format

Organize by category with pipe-delimited tables:

```markdown
## Category Name

| Command / Pattern | Purpose | Example |
|-------------------|---------|---------|
| `/command` | What it does | `usage example` |
```

## Cross-Reference Conventions

- Reference other levels: "See **Level N: Theme**" or link to `../level-N/README.md`
- Reference main README: link to `../../README.md`
- Reference cheat sheet: "See this level's [CHEATSHEET.md](./CHEATSHEET.md)"
- "What's Next" section at end should preview the next level's theme
