# 🎓 Copilot CLI Workshop — Complete Learning Path

A progressive 8-level curriculum for mastering GitHub Copilot CLI, from
first launch to advanced automation and delegation.

## Curriculum Overview

```
Level 1   Level 2    Level 3    Level 4    Level 5    Level 6     Level 7      Level 8
Observe → Understand → Plan → Create → Execute → Workflow → Customize → Advanced
  🟢        🟢         🟢      🟡       🟡        🟠         🟢          🔴
 read     ask & learn  think   write    run cmds   full cycle  configure   automate
 only     code Q&A    before   first    tests &    plan→test   instruct.   delegate
                      coding   edits    linters    →review     MCP/ctx     agent/CI
```

## Quick Navigation

| Level | Title | Exercises | App | Time |
|-------|-------|:---------:|-----|------|
| [**1**](level-1/README.md) | Observe — Read-Only Exploration | 12 | Python Task Manager CLI | 45–60 min |
| [**2**](level-2/README.md) | Understand — Ask Questions & Get Explanations | 12 | Python Bookmark Manager API | 60–80 min |
| [**3**](level-3/README.md) | Plan — Think Before Acting | 12 | Python Quick Notes CLI (with bugs) | 60–80 min |
| [**4**](level-4/README.md) | Create — Make Your First Changes | 12 | Quick Notes CLI (writable copy) | 60–90 min |
| [**5**](level-5/README.md) | Execute — Run Commands Through Copilot | 12 | Python Math Utilities (pytest) | 75–100 min |
| [**6**](level-6/README.md) | Workflow — Full Plan → Execute → Review Cycle | 12 | Python URL Shortener CLI | 90–120 min |
| [**7**](level-7/README.md) | Customize — Make Copilot Work Your Way | 12 | TypeScript Event API (Express) | 75–100 min |
| [**8**](level-8/README.md) | Advanced — Permissions, Sessions & Delegation | 12 | Multi-service DevOps Toolkit | 90–120 min |

**Total: 96 exercises across 8 levels — estimated 9–13 hours**

## Skill Progression

```
  Risk Level    🟢 None ─────────────────────────────────── 🔴 High awareness
  Autonomy      Human reads ────────────────── Human + AI ── AI proposes
  Tools         view, grep ── @ context ── /plan ── edit ── bash ── -p/-s ── agent
  Scope         One file ──── Multi-file ── Project ── Multi-service ── CI/CD
```

| Level | New Skills Introduced |
|-------|----------------------|
| **1** | Launch, `@` context, `!` shell escape, `/help`, tool approval basics |
| **2** | Deep questioning, architecture tracing, pattern recognition, prompt crafting |
| **3** | `/plan`, plan evaluation, critical reading, rejection, multi-file planning |
| **4** | Allow/Deny/Session approval, `/diff`, `/review`, `git checkout --` revert |
| **5** | `bash` tool, test → fix → re-run loop, lint cycle, TDD, autonomous fix loop |
| **6** | Full SDLC cycle, multi-file debugging, refactoring, hotfix, code review |
| **7** | `.github/copilot-instructions.md`, `.copilotignore`, MCP, session mgmt |
| **8** | `--allow-tool`, `--deny-url`, `-p`/`-s`, Coding Agent, CI/CD, SDK/ACP |

## Sample App Progression

Each level uses a **distinct sample application** of increasing complexity:

| Level | Application | Language | Why This App |
|-------|-------------|----------|-------------|
| **1** | Task Manager CLI | Python | Simple, readable — focus on tool navigation |
| **2** | Bookmark Manager API | Python | Layered architecture — focus on understanding code |
| **3** | Quick Notes CLI | Python | 8 intentional bugs — focus on discovering & planning |
| **4** | Quick Notes CLI *(copy of L3)* | Python | Same bugs, now you fix them — continuity from L3 |
| **5** | Math Utilities Library | Python | pytest + flake8 + Makefile — focus on command execution |
| **6** | URL Shortener CLI | Python | Multi-file bug + test gaps — focus on full workflows |
| **7** | Event API | TypeScript | Express + conventions — focus on configuration |
| **8** | DevOps Toolkit | JS + Python | Multi-service + scripts — focus on automation |

## Each Level Contains

```
workshop/level-N/
├── README.md          ← 12 exercises with detailed steps
├── CHEATSHEET.md      ← Quick reference card for the level's skills
└── sample-app/        ← Hands-on code (unique per level)
```

## How to Use This Workshop

### Self-Paced (Individual)
1. Start at Level 1, complete all 12 exercises
2. Take the self-assessment at the end of each level
3. Score ≥ 83% → proceed to the next level
4. Score < 60% → go back and repeat key exercises
5. Aim for 1–2 levels per session

### Team Workshop (Facilitated)
| Format | Levels to Cover | Duration |
|--------|----------------|----------|
| **Quick intro** (new users) | Levels 1–2 | 2 hours |
| **Core skills** (daily use) | Levels 1–5 | 4–5 hours |
| **Full training** (power users) | Levels 1–8 | 9–13 hours (2 days) |
| **Advanced only** (experienced) | Levels 6–8 | 4–6 hours |

### Safety

Every level has a **safety net**:

```bash
# Reset any level's sample app to original state
git checkout -- workshop/level-N/sample-app/
```

Levels 1–3 are **read-only** — no risk of breaking anything.

## Prerequisites

- GitHub account with Copilot subscription
- Copilot CLI installed (`npm install -g @anthropic-ai/claude-code` or similar)
- Terminal (macOS Terminal, iTerm2, Windows Terminal, or Linux terminal)
- Git installed and configured
- Python 3.8+ (Levels 1–6)
- Node.js 18+ (Level 7)

## Getting Started

```bash
cd workshop/level-1
cat README.md
# Read the instructions, then:
copilot
```
