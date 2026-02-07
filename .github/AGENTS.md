# Copilot Coding Agent — Workshop Repository

## Agent Identity

You are working on an **educational workshop repository** that teaches GitHub
Copilot CLI. Every contribution must maintain pedagogical quality — changes should
help developers learn more effectively. Read `.github/copilot-instructions.md`
for full repository context, structure, and the intentional bug catalog.

## Skills

### 1. Workshop Content Development

Create, extend, or refine workshop exercises and cheat sheets.

- Follow the 12-exercise-per-level format strictly
- Use the exercise template: Goal → Steps → Key Concept → Checkpoint
- Maintain cross-references between levels and the main README
- Ensure self-assessment rubrics (12 items, 1–3 scale, 36 max) align with exercises

### 2. Sample App Engineering

Build educational sample applications with intentional, discoverable defects.

- Design code that demonstrates specific Copilot CLI capabilities
- Plant bugs that are realistic but discoverable through guided exploration
- Create test suites with deliberate failures for test-fix workflow exercises
- Keep Python apps stdlib-only; TypeScript apps use Express + Jest

### 3. Documentation Maintenance

Keep the learning guide, curriculum overview, and references accurate.

- Update `README.md` level tables when exercises change
- Update `workshop/README.md` navigation and skill progression
- Maintain consistency between level READMEs and cheat sheets
- Ensure "Unlike Level N-1..." comparison paragraphs exist in each level

### 4. Repository Infrastructure

Maintain GitHub Actions, issue templates, and agent configuration.

- Workshop branch creation workflow (`.github/workflows/workshop-branch.yml`)
- Issue form templates for workshop management
- Agent instruction files (this file, copilot-instructions.md, path-specific)

## Commit Message Format

```
<type>: <concise description>

<optional body with details>
```

| Type | Use For | Example |
|------|---------|---------|
| `workshop` | New or modified exercises, cheat sheets | `workshop: add Level 9 — Team Collaboration` |
| `sample-app` | Sample application code changes | `sample-app: add rate limiter to L6 shortener` |
| `docs` | README, guides, non-exercise docs | `docs: update learning path for Level 9` |
| `ci` | GitHub Actions workflows | `ci: add workshop setup verification step` |
| `config` | Agent definitions, templates, repo config | `config: add path-specific Python instructions` |
| `refine` | Cross-cutting consistency improvements | `refine: standardize checkpoint wording across levels` |
| `fix` | Bug fixes in infrastructure (NOT sample apps) | `fix: workshop branch workflow label handling` |

## Pull Request Standards

Every PR must:

1. **Describe what changed and why** — link to the relevant issue if applicable
2. **Verify exercise numbering** — sequential 1–12, no gaps or duplicates
3. **Check cross-references** — if a level changed, the main README table must match
4. **Align self-assessment** — rubric items must equal exercise count (12)
5. **Preserve intentional bugs** — never fix sample app defects (see catalog in copilot-instructions.md)

## Adding a New Level

When creating Level N:

1. `workshop/level-N/README.md` — 12 exercises with full structure
2. `workshop/level-N/CHEATSHEET.md` — categorized quick-reference tables
3. `workshop/level-N/sample-app/` — unique application (different from all other levels)
4. Add "Unlike Level N-1..." comparison paragraph in sample app introduction
5. Update `workshop/README.md` — navigation table, skill progression, time estimates
6. Update `README.md` — Level N section with 12-row exercise table
7. Self-assessment: 12 items, 1–3 scale, 36 max, ready threshold ≥ 30

## Prohibited Actions

- ❌ Fix intentional bugs in sample apps (see full catalog in copilot-instructions.md)
- ❌ Reduce exercise count below 12 per level
- ❌ Change the scoring system (1–3 scale, 36 max, 30+ = ready)
- ❌ Add external dependencies to Python sample apps (Levels 1–6 use stdlib only)
- ❌ Commit real secrets (Level 8's production.env has fake values — keep them fake)
- ❌ Remove or rename existing sample-app files without updating exercise references
- ❌ Modify the workshop-branch.yml workflow without verifying label handling
