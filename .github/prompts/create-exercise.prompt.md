---
mode: "agent"
description: "Generate a new exercise following the workshop's standard format and conventions"
---

# Create a New Exercise

You are adding a new exercise to an existing workshop level.

## Target

Add **Exercise {{exercise_number}}** to **Level {{level_number}}** at
`workshop/level-{{level_number}}/README.md`.

**Exercise topic:** {{topic}}

## Context

Before writing, read:
1. The level's existing README.md to understand the progression and voice
2. The level's sample-app/ to reference realistic file paths and code
3. `.github/instructions/workshop-content.instructions.md` for format rules

## Exercise Template

Generate the exercise following this exact structure:

```markdown
---

## Exercise {{exercise_number}}: {{Title}}

### Goal
One sentence describing what the learner will achieve.

### Steps

**{{exercise_number}}.1** Description of first step:

(Copilot prompt in fenced code block — no language tag)

> Expected: Description of what Copilot should respond with.

**{{exercise_number}}.2** Description of next step:

(Next prompt or action)

...continue with 4–8 substeps...

### Key Concept: {{Concept Name}}

2–4 sentence explanation of the underlying idea this exercise teaches.
Include a practical tip or comparison table if helpful.

### ✅ Checkpoint
One sentence confirming what the learner should now be able to do.
```

## Rules

- Reference real files from the level's sample-app (use actual paths and function names)
- Copilot prompts should be realistic — things a developer would actually ask
- Include expected output descriptions so learners can verify they're on track
- Build on skills from earlier exercises in this level
- The exercise should take 5–15 minutes to complete
- If this is Exercise 12, consider making it a capstone that combines multiple skills

## After Creation

Remind the user to:
1. Update the Learning Objectives list to include this exercise
2. Add a self-assessment item for this exercise
3. Update the main README.md exercise table for this level
4. Verify exercise numbering is still sequential
