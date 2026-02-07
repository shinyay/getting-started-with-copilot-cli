---
name: sample-app-development
description: Guide for developing or modifying sample applications in the Copilot CLI workshop. Use this when editing, creating, or reviewing code in any workshop level's sample-app directory. Critical for preserving intentional bugs planted for teaching exercises.
---

# Sample App Development

Workshop sample apps are **educational code** — not production applications. They are designed
for learners to explore with Copilot CLI. Every edit must preserve pedagogical integrity.

## 🚫 Intentional Bug Catalog — DO NOT FIX

These bugs are **deliberately planted** for teaching exercises. Fixing them breaks the curriculum.

### Level 3/4 — Quick Notes CLI (`workshop/level-3/sample-app/`, `workshop/level-4/sample-app/`)

| # | Bug | What It Looks Like |
|---|-----|--------------------|
| 1 | Off-by-one in display | Note numbering starts at wrong index |
| 2 | Missing `strip()` on search | Whitespace in search input causes no results |
| 3 | No duplicate-ID check | Adding a note with existing ID silently overwrites |
| 4 | Broken export encoding | UTF-8 BOM issue in exported files |
| 5 | Delete removes wrong note | Index vs ID confusion in delete logic |
| 6 | Priority filter inverted | High priority filter returns low priority items |
| 7 | Empty-title accepted | No validation prevents blank note titles |
| 8 | Stats double-count on edit | Edit operation increments counter incorrectly |

### Level 5 — Math Utilities (`workshop/level-5/sample-app/`)

| # | Bug | Location |
|---|-----|----------|
| 1 | `divide(x, 0)` returns None | `mathlib/calculator.py` — should raise ValueError |
| 2 | Negative exponent wrong | `mathlib/calculator.py` — `power(-2)` returns 0 not 0.5 |
| 3 | Median off-by-one | `mathlib/statistics.py` — even-length list calculation |
| 4 | Mode returns first element | `mathlib/statistics.py` — not most frequent |
| 5 | `is_positive(0)` returns True | `mathlib/validator.py` — zero edge case |
| 6 | `is_integer(str)` crashes | `mathlib/validator.py` — missing try/except |
| 7 | Unused imports | Multiple files — `import math`, `import os` |
| 8 | Missing docstring | `mathlib/` — `absolute()` function |

### Level 6 — URL Shortener (`workshop/level-6/sample-app/`)

| # | Issue | Impact |
|---|-------|--------|
| 1 | Delete doesn't decrement stats | `store.py` + `stats.py` — multi-file bug |
| 2 | `test_validator.py` missing | Zero test coverage for validator module |
| 3 | No URL expiration | Feature entirely absent |
| 4 | Code duplication | Repeated patterns across store operations |
| 5 | Incomplete test assertions | Existing tests don't verify enough |

## When Editing Sample App Code

1. **Check the bug catalog above** before changing any file listed
2. **New code should work correctly** — intentional bugs are curated, not random
3. **If adding a new intentional bug**, document it in the level's README exercise list AND update `.github/copilot-instructions.md`
4. **Do NOT add comments** that give away bug locations (discovery is the exercise)

## Language-Specific Standards

### Python (Levels 1–6)
- Python 3.8+ compatible
- **Standard library only** — zero external dependencies
- Clear docstrings on public functions and classes
- `snake_case` for functions/variables, `PascalCase` for classes
- Tests use `unittest` (no pytest)

### TypeScript (Level 7)
- TypeScript 5.x strict mode, ES2020 target
- Express 4.x, Jest for testing
- `AppError` class for error handling
- `ApiResponse<T>` wrapper for API responses

### Multi-language (Level 8)
- Node.js API + Python worker
- Bash scripts with `set -euo pipefail`
- Level 8's `config/production.env` has **fake secrets** — keep them fake

## Sample App Design Principles

- **Clarity over cleverness** — learners need to read and understand the code
- **Realistic structure** — mirror real-world project layouts
- **Discoverable complexity** — bugs and patterns should be findable through guided exploration
- **Self-contained** — each app runs independently without external services
