---
name: workshop-content-review
description: Guide for reviewing or auditing workshop content quality. Use this when asked to review, audit, validate, or check the quality of workshop exercises, levels, or the overall curriculum.
---

# Workshop Content Review

Use this 20-point checklist to audit any workshop level for quality and consistency.

## Audit Process

1. Read the target level's README.md, CHEATSHEET.md, and sample-app/
2. Score each item below: ✅ (pass), ⚠️ (minor issue), ❌ (failure)
3. Generate a structured report

## Checklist

### Structure (5 checks)

| # | Check | What to Verify |
|---|-------|---------------|
| 1 | File presence | README.md, CHEATSHEET.md, and sample-app/ all exist |
| 2 | Exercise count | Exactly 12 exercises numbered 1–12 |
| 3 | Exercise format | Each has `## Exercise N: Title`, `### Goal`, `### Steps`, `### ✅ Checkpoint` |
| 4 | Step numbering | All steps use `**N.M**` format consistently |
| 5 | Section separators | Horizontal rules (`---`) between every exercise |

### Content Quality (5 checks)

| # | Check | What to Verify |
|---|-------|---------------|
| 6 | Learning objectives | 12 objectives listed, each matching one exercise |
| 7 | Prerequisites | Section exists with actionable checklist items |
| 8 | App comparison | "Unlike Level N-1..." paragraph in About the Sample App |
| 9 | Key Concepts | At least 8 of 12 exercises include `### Key Concept` |
| 10 | Copilot prompts | User-typed prompts in fenced code blocks with NO language tag |

### Self-Assessment (3 checks)

| # | Check | What to Verify |
|---|-------|---------------|
| 11 | Item count | Self-assessment has exactly 12 items |
| 12 | Scoring system | Uses 1–3 scale, shows /36 total |
| 13 | Ready threshold | States 30–36 as ready for next level |

### Cross-References (3 checks)

| # | Check | What to Verify |
|---|-------|---------------|
| 14 | Main README | Exercise table in README.md matches actual exercises |
| 15 | Workshop README | `workshop/README.md` navigation table includes this level |
| 16 | Cheat sheet | CHEATSHEET.md categories reflect exercise topics |

### Sample App (4 checks)

| # | Check | What to Verify |
|---|-------|---------------|
| 17 | Uniqueness | App is different from all other levels |
| 18 | App README | sample-app/README.md exists with description and usage |
| 19 | Bug documentation | If app has intentional bugs, they're in copilot-instructions.md |
| 20 | Code references | Exercise steps reference actual files that exist in sample-app/ |

## Report Format

```markdown
## Level N Audit Report

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | File presence | ✅ | All files present |
| 2 | Exercise count | ✅ | 12 exercises found |
...

### Summary
- ✅ Passed: X/20
- ⚠️ Warnings: X/20
- ❌ Failed: X/20

### Fixes Required
1. [If any failures, list specific fixes needed]

### Recommendations
1. [Optional improvements that would enhance quality]
```

## Cross-Level Consistency

When reviewing, also verify these curriculum-wide standards:
- All levels use the same voice (second-person, action-oriented)
- Difficulty progresses logically from the previous level
- No duplicate exercise concepts across levels (each level teaches NEW skills)
- The "What's Next" section accurately previews the following level
