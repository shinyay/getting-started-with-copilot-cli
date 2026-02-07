#!/usr/bin/env bash
# Scaffold the directory structure for a new workshop level.
# Usage: ./scaffold.sh <level_number> "<level_title>"
# Example: ./scaffold.sh 9 "Team Collaboration"
set -euo pipefail

LEVEL_NUM="${1:?Usage: scaffold.sh <level_number> \"<level_title>\"}"
LEVEL_TITLE="${2:?Usage: scaffold.sh <level_number> \"<level_title>\"}"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LEVEL_DIR="${REPO_ROOT}/workshop/level-${LEVEL_NUM}"

if [[ -d "${LEVEL_DIR}" ]]; then
  echo "❌ Directory already exists: ${LEVEL_DIR}"
  exit 1
fi

echo "📁 Creating Level ${LEVEL_NUM}: ${LEVEL_TITLE}"

mkdir -p "${LEVEL_DIR}/sample-app"

# README.md scaffold
cat > "${LEVEL_DIR}/README.md" << 'HEREDOC_README'
# Level LEVEL_NUM: LEVEL_TITLE

> **Risk level:** 🟡 TODO — Set the appropriate risk level and description.

## Learning Objectives

By the end of this level, you will be able to:

1. TODO: Objective matching Exercise 1
2. TODO: Objective matching Exercise 2
3. TODO: Objective matching Exercise 3
4. TODO: Objective matching Exercise 4
5. TODO: Objective matching Exercise 5
6. TODO: Objective matching Exercise 6
7. TODO: Objective matching Exercise 7
8. TODO: Objective matching Exercise 8
9. TODO: Objective matching Exercise 9
10. TODO: Objective matching Exercise 10
11. TODO: Objective matching Exercise 11
12. TODO: Objective matching Exercise 12

---

## Prerequisites

- [ ] Completed **Levels 1–PREV_LEVEL** (all prior skills)
- [ ] Copilot CLI installed and working
- [ ] TODO: Add level-specific prerequisites

---

## About the Sample App

TODO: Describe the sample application.

Unlike Level PREV_LEVEL's [previous app], this level's app [what makes it different].

---

## Exercise 1: TODO Title

### Goal
TODO: One sentence.

### Steps

**1.1** TODO: First step

### ✅ Checkpoint
TODO: Verification.

---

<!-- Repeat for Exercises 2–12 -->

## Self-Assessment

Rate yourself on each skill (1 = need review, 2 = mostly comfortable, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|-------|---|---|---|
| 1 | TODO: Skill from Exercise 1 | ○ | ○ | ○ |
| 2 | TODO: Skill from Exercise 2 | ○ | ○ | ○ |
| 3 | TODO: Skill from Exercise 3 | ○ | ○ | ○ |
| 4 | TODO: Skill from Exercise 4 | ○ | ○ | ○ |
| 5 | TODO: Skill from Exercise 5 | ○ | ○ | ○ |
| 6 | TODO: Skill from Exercise 6 | ○ | ○ | ○ |
| 7 | TODO: Skill from Exercise 7 | ○ | ○ | ○ |
| 8 | TODO: Skill from Exercise 8 | ○ | ○ | ○ |
| 9 | TODO: Skill from Exercise 9 | ○ | ○ | ○ |
| 10 | TODO: Skill from Exercise 10 | ○ | ○ | ○ |
| 11 | TODO: Skill from Exercise 11 | ○ | ○ | ○ |
| 12 | TODO: Skill from Exercise 12 | ○ | ○ | ○ |

**Total: ___/36**

- **30–36:** Ready for the next level
- **20–29:** Review exercises where you scored 1
- **Below 20:** Revisit this level before proceeding
HEREDOC_README

# Replace placeholders
sed -i "s/LEVEL_NUM/${LEVEL_NUM}/g" "${LEVEL_DIR}/README.md"
sed -i "s/LEVEL_TITLE/${LEVEL_TITLE}/g" "${LEVEL_DIR}/README.md"
sed -i "s/PREV_LEVEL/$((LEVEL_NUM - 1))/g" "${LEVEL_DIR}/README.md"

# CHEATSHEET.md scaffold
cat > "${LEVEL_DIR}/CHEATSHEET.md" << HEREDOC_CHEAT
# Level ${LEVEL_NUM} Cheat Sheet: ${LEVEL_TITLE}

## Core Commands

| Command / Pattern | Purpose | Example |
|-------------------|---------|---------|
| TODO | TODO | TODO |

## Workflow Patterns

| Pattern | When to Use | Steps |
|---------|-------------|-------|
| TODO | TODO | TODO |

## Tips & Gotchas

| Tip | Why It Matters |
|-----|---------------|
| TODO | TODO |
HEREDOC_CHEAT

# sample-app README
cat > "${LEVEL_DIR}/sample-app/README.md" << HEREDOC_APP
# Level ${LEVEL_NUM} Sample App: TODO App Name

## Overview
TODO: Describe the application.

## How to Run
\`\`\`bash
# TODO: Add run instructions
\`\`\`

## File Structure
\`\`\`
sample-app/
  README.md    # This file
  TODO         # Add file listing
\`\`\`
HEREDOC_APP

echo "✅ Scaffolded: ${LEVEL_DIR}"
echo "   ├── README.md        (12-exercise template with TODOs)"
echo "   ├── CHEATSHEET.md    (category template)"
echo "   └── sample-app/"
echo "       └── README.md    (app description template)"
echo ""
echo "Next steps:"
echo "  1. Design and create the sample application in sample-app/"
echo "  2. Fill in the 12 exercises in README.md"
echo "  3. Complete the CHEATSHEET.md categories"
echo "  4. Update workshop/README.md and the main README.md"
