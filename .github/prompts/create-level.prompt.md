---
mode: "agent"
description: "Create a complete new workshop level with README, CHEATSHEET, and sample-app scaffold"
---

# Create a New Workshop Level

You are creating a new level for the Copilot CLI learning workshop.

## Context

This repository has 8 existing levels (workshop/level-1 through level-8). Each level follows
a strict structure. Read `.github/copilot-instructions.md` for the full repository context,
and `.github/AGENTS.md` for the new-level checklist.

## Your Task

Create **Level {{level_number}}: {{level_title}}** with theme: **{{level_theme}}**

### Step 1: Analyze Existing Levels

Before creating anything, read:
- `workshop/README.md` for the curriculum overview and progression
- The previous level's README.md to understand where learners are coming from
- At least 2 other level READMEs to internalize the format

### Step 2: Design the Sample App

Create a **unique** sample application under `workshop/level-{{level_number}}/sample-app/`:
- Must be different from all existing apps (see workshop/README.md for the app list)
- Complexity should match the level's position in the progression
- Include intentional bugs/issues appropriate for the level's teaching goals
- Add a README.md explaining the app, how to run it, and file structure

### Step 3: Write the Level README

Create `workshop/level-{{level_number}}/README.md` with exactly **12 exercises**:

Each exercise must have:
- `## Exercise N: Title` (H2)
- `### Goal` — one sentence
- `### Steps` — numbered `**N.1**`, `**N.2**`, etc. with Copilot prompts in fenced code blocks
- `### Key Concept: Name` — explanation of the underlying idea
- `### ✅ Checkpoint` — one-sentence verification

Include these sections:
- Learning Objectives (12 items matching exercises)
- Prerequisites
- About the Sample App (with "Unlike Level N-1..." comparison paragraph)
- The 12 exercises
- Self-Assessment (12 items, 1–3 scale, 36 max, ready ≥ 30)
- Key Takeaways
- What's Next (preview of the following level)

### Step 4: Write the Cheat Sheet

Create `workshop/level-{{level_number}}/CHEATSHEET.md`:
- Categorized tables of commands and patterns taught in this level
- Quick-reference format matching existing cheat sheets

### Step 5: Update Cross-References

- Update `workshop/README.md` navigation table, skill progression, and time estimates
- Update the main `README.md` Level section with a 12-row exercise table
- Verify the progression narrative still flows logically

### Quality Checks

Before finishing, verify:
- [ ] Exactly 12 exercises with sequential numbering
- [ ] Self-assessment has 12 items matching exercises
- [ ] Sample app is unique and appropriate for the level
- [ ] "Unlike Level N-1..." paragraph exists
- [ ] Cross-references updated in workshop/README.md and main README.md
- [ ] All Copilot prompts are in fenced code blocks (no language tag)
- [ ] Horizontal rules between exercises
