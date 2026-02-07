---
mode: "agent"
description: "Audit a workshop level for format consistency, exercise count, scoring, and cross-references"
---

# Review Workshop Level

You are performing a quality audit on a workshop level to ensure it meets
the curriculum standards.

## Target

Review **Level {{level_number}}** at `workshop/level-{{level_number}}/`.

## Audit Checklist

Read the level's README.md, CHEATSHEET.md, and sample-app/, then verify each item below.
Report findings as a structured table with ✅ (pass), ⚠️ (minor issue), or ❌ (failure).

### Structure (5 checks)

1. **File presence**: README.md, CHEATSHEET.md, and sample-app/ directory all exist
2. **Exercise count**: Exactly 12 exercises numbered sequentially (Exercise 1 through 12)
3. **Exercise format**: Each exercise has `## Exercise N: Title`, `### Goal`, `### Steps`, `### ✅ Checkpoint`
4. **Step numbering**: Steps use `**N.M**` format (N = exercise number, M = step)
5. **Section separators**: Horizontal rules (`---`) between exercises

### Content Quality (5 checks)

6. **Learning objectives**: Listed at top, count matches exercise count (12)
7. **Prerequisites**: Section exists with actionable checklist
8. **App comparison**: "Unlike Level N-1..." paragraph exists in About the Sample App
9. **Key Concepts**: At least 8 of 12 exercises have a `### Key Concept` section
10. **Copilot prompts**: All user-typed prompts are in fenced code blocks with NO language tag

### Self-Assessment (3 checks)

11. **Item count**: Self-assessment has exactly 12 items
12. **Scoring system**: Uses 1–3 scale with 36 max total
13. **Ready threshold**: States 30–36 as ready for next level

### Cross-References (3 checks)

14. **Main README**: The level's exercise table in `README.md` matches actual exercises
15. **Workshop README**: `workshop/README.md` navigation table includes this level correctly
16. **Cheat sheet alignment**: CHEATSHEET.md categories reflect the level's exercise topics

### Sample App (4 checks)

17. **Uniqueness**: App is different from all other levels' apps
18. **README**: sample-app/README.md exists with description and usage
19. **Intentional bugs** (if applicable): Bugs are documented in `.github/copilot-instructions.md`
20. **Runnable**: App has a clear entry point and can be understood without running

## Output Format

```markdown
## Level {{level_number}} Audit Report

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | File presence | ✅/⚠️/❌ | Details... |
...

### Summary
- Passed: X/20
- Warnings: X/20
- Failed: X/20

### Recommended Fixes
1. ...
```
