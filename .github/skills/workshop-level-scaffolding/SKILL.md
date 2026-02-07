---
name: workshop-level-scaffolding
description: Guide for creating a complete new workshop level in the Copilot CLI learning path. Use this when asked to create, scaffold, or add a new level to the workshop curriculum.
---

# Workshop Level Scaffolding

When creating a new workshop level, follow this complete process to ensure consistency with the existing 8-level curriculum.

## Directory Structure

Each level requires this exact structure:

```
workshop/level-N/
  README.md          # 12 exercises with full structure
  CHEATSHEET.md      # Categorized quick-reference tables
  sample-app/        # Unique hands-on application
    README.md        # App description, usage, file listing
    ...              # Application source files
```

Use the scaffold script in this skill's directory to create the initial structure:

```bash
.github/skills/workshop-level-scaffolding/scaffold.sh <level_number> "<level_title>"
```

## Step-by-Step Process

### 1. Analyze the Curriculum

Before creating anything, read:
- `workshop/README.md` — curriculum overview, app progression, skill matrix
- The previous level's README.md — understand where learners are coming from
- At least 2 other level READMEs — internalize the format and voice

### 2. Design the Sample App

Create a **unique** application that:
- Is different from all existing apps (L1: task manager, L2: bookmark API, L3/L4: notes CLI, L5: math lib, L6: URL shortener, L7: TypeScript event API, L8: DevOps toolkit)
- Matches the level's complexity position in the progression
- Contains intentional bugs/issues appropriate for the level's teaching goals (if applicable)
- Has a clear entry point and can be understood by reading (without necessarily running it)

### 3. Write the Level README

Must include these sections in order:
1. **Title**: `# Level N: Theme — Subtitle`
2. **Risk level callout**: Blockquote with appropriate emoji (🟢🟡🟠🔴🔵)
3. **Learning Objectives**: Numbered list, 12 items matching the 12 exercises
4. **Prerequisites**: Checklist referencing prior levels
5. **About the Sample App**: Description with "Unlike Level N-1..." comparison paragraph
6. **12 Exercises**: Full format (Goal → Steps → Key Concept → Checkpoint)
7. **Self-Assessment**: 12 items, 1–3 scale, 36 max, 30+ = ready
8. **Key Takeaways**: 6–10 bullet points summarizing the level
9. **What's Next**: Preview of the following level

### 4. Write the Cheat Sheet

`CHEATSHEET.md` organized by category with tables:

```markdown
# Level N Cheat Sheet: Theme

## Category Name

| Command / Pattern | Purpose | Example |
|-------------------|---------|---------|
| `/command` | What it does | `usage example` |
```

### 5. Update Cross-References

After creating the level:
- Update `workshop/README.md` — navigation table, skill progression, time estimates
- Update `README.md` — add Level N section with 12-row exercise table
- Verify the progression narrative still flows logically

## Quality Checklist

Before considering the level complete:

- [ ] Exactly 12 exercises with sequential numbering (1–12)
- [ ] Every exercise has: Goal, Steps, Key Concept (at least 8 of 12), Checkpoint
- [ ] Self-assessment has 12 items matching exercises, 1–3 scale
- [ ] Sample app is unique and different from all other levels
- [ ] "Unlike Level N-1..." comparison paragraph exists
- [ ] Main README and workshop/README.md updated
- [ ] All Copilot prompts in fenced code blocks (no language tag)
- [ ] Horizontal rules between exercises
- [ ] Risk level callout matches the level's position
- [ ] Cheat sheet categories reflect exercise topics
