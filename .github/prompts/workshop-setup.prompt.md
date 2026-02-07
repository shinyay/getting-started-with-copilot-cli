---
mode: "agent"
description: "Verify workshop environment setup and guide learner through prerequisites"
---

# Workshop Setup Verification

Help a learner verify their environment is ready for the Copilot CLI workshop.

## Step 1: Check Prerequisites

Run these checks and report results:

```bash
# GitHub CLI
gh --version

# Copilot CLI
copilot --version 2>/dev/null || gh copilot --version 2>/dev/null

# Python (needed for Levels 1–6)
python3 --version

# Node.js (needed for Level 7)
node --version 2>/dev/null

# Git
git --version
```

Report a table:

| Tool | Required For | Status | Version |
|------|-------------|--------|---------|
| GitHub CLI (`gh`) | All levels | ✅/❌ | X.Y.Z |
| Copilot CLI | All levels | ✅/❌ | X.Y.Z |
| Python 3.8+ | Levels 1–6 | ✅/❌ | X.Y.Z |
| Node.js 18+ | Level 7 | ✅/⚠️ Optional | X.Y.Z |
| Git | All levels | ✅/❌ | X.Y.Z |

## Step 2: Verify Authentication

```bash
gh auth status
```

Check that the user is authenticated and has Copilot access.

## Step 3: Verify Repository Structure

Confirm the workshop directory exists and has all 8 levels:

```bash
ls workshop/level-*/README.md
```

## Step 4: Recommend Starting Point

Based on the learner's experience level, suggest where to start:

- **New to Copilot CLI**: Start at Level 1 (Observe)
- **Used Copilot in IDE but not CLI**: Start at Level 1, skim quickly, dive deep at Level 3
- **Comfortable with CLI basics**: Start at Level 4 (Create) or Level 5 (Execute)
- **Want to optimize workflow**: Jump to Level 7 (Customize)

## Step 5: Quick Smoke Test

Verify Copilot CLI actually works by checking it can read the repository:

```
Ask Copilot: "What is this repository about? List the files in the root directory."
```

If this works, the learner is ready.

## Output

Provide a clear summary:
- ✅ Ready / ❌ Not ready (with fix instructions for each failing check)
- Recommended starting level
- Estimated time to complete the full workshop (9–13 hours)
- Link to `workshop/README.md` for the curriculum overview
