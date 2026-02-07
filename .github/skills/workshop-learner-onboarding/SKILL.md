---
name: workshop-learner-onboarding
description: Guide for helping learners set up their environment and get started with the Copilot CLI workshop. Use this when someone asks about getting started, setup, prerequisites, which level to start at, or how to use this workshop.
---

# Workshop Learner Onboarding

Help learners verify their environment and choose the right starting point for the Copilot CLI workshop.

## Environment Verification

Check these prerequisites and report a status table:

### Required Tools

| Tool | Required For | Minimum Version | Check Command |
|------|-------------|----------------|---------------|
| GitHub CLI (`gh`) | All levels | 2.x | `gh --version` |
| Copilot CLI | All levels | Any | `copilot --version` |
| Python | Levels 1–6 | 3.8+ | `python3 --version` |
| Git | All levels | 2.x | `git --version` |

### Optional Tools

| Tool | Required For | Check Command |
|------|-------------|---------------|
| Node.js 18+ | Level 7 only | `node --version` |
| npm | Level 7 only | `npm --version` |

### Authentication

Run `gh auth status` to verify:
- GitHub authentication is active
- Copilot access is available (requires Copilot Pro, Pro+, Business, or Enterprise)

## Choosing a Starting Level

Based on the learner's experience, recommend a starting level:

| Experience Level | Start At | Rationale |
|-----------------|----------|-----------|
| **New to Copilot entirely** | Level 1 | Build foundation from zero risk |
| **Used Copilot in IDE, new to CLI** | Level 1 (skim) → Level 3 | Familiar with AI assist, need CLI-specific skills |
| **Basic CLI experience** | Level 4 or 5 | Ready for write operations and command execution |
| **Want to optimize workflow** | Level 7 | Focus on customization and configuration |
| **Need automation/delegation** | Level 8 | Advanced permissions and agent delegation |

## Workshop Structure Overview

- **96 exercises** across 8 levels (12 per level)
- **Estimated time**: 9–13 hours total (1–2 hours per level)
- **Each level has**: README.md (exercises), CHEATSHEET.md (quick reference), sample-app/ (hands-on code)
- **Safety**: Levels 1–3 are read-only (no risk). Level 4+ involves file modifications.
- **Reset**: `git checkout workshop/level-N/sample-app/` restores any level's app to original state

## Quick Smoke Test

After setup, verify Copilot CLI works:

```bash
# Start Copilot CLI in the repo directory
copilot

# Then ask:
# "What is this repository about? List the workshop levels."
```

If Copilot responds with information about the 8-level learning path, the setup is complete.

## Curriculum Map

```
Level 1: Observe    → Read files, navigate, understand safety gates
Level 2: Understand → Ask questions, trace architecture, get explanations
Level 3: Plan       → Create implementation plans, evaluate approaches
Level 4: Create     → Make first changes, approve edits, use /diff and /review
Level 5: Execute    → Run tests, fix failures, lint, TDD workflow
Level 6: Workflow   → Full Plan→Execute→Review cycles, complete SDLC
Level 7: Customize  → Custom instructions, MCP, context optimization
Level 8: Advanced   → Permissions, sessions, automation, Coding Agent delegation
```

## Resources

- Main guide: `README.md` (root of repository)
- Curriculum overview: `workshop/README.md`
- Per-level cheat sheets: `workshop/level-N/CHEATSHEET.md`
- Agent configuration examples: `.github/copilot-instructions.md`, `.github/AGENTS.md`
