---
mode: "agent"
description: "Verify that intentional sample app bugs are preserved and match the documented catalog"
---

# Verify Intentional Bugs

Audit sample applications to confirm all intentional bugs documented in
`.github/copilot-instructions.md` are still present and working as designed.

## Bug Catalog

Read the "Never Auto-Fix Intentional Bugs" section in `.github/copilot-instructions.md`
for the authoritative list. Then verify each bug exists in the source code.

## Verification Process

For each level with intentional bugs (Levels 3, 4, 5, 6):

### Level 3/4 — Quick Notes CLI (8 bugs)

Check `workshop/level-3/sample-app/` and `workshop/level-4/sample-app/`:

| # | Bug | File to Check | What to Look For |
|---|-----|--------------|-----------------|
| 1 | Off-by-one in display | app.py or display logic | Index starting at 0 instead of 1, or vice versa |
| 2 | Missing strip() on search | Search function | User input not trimmed before comparison |
| 3 | No duplicate-ID check | Add function | No validation that ID already exists |
| 4 | Broken export encoding | Export function | UTF-8 BOM or encoding issue |
| 5 | Delete wrong note | Delete function | Index vs ID confusion |
| 6 | Priority filter inverted | Filter/sort logic | Condition flipped |
| 7 | Empty-title accepted | Add/create function | No validation for empty strings |
| 8 | Stats double-count | Edit/stats function | Counter incremented incorrectly |

### Level 5 — Math Utilities (6 test failures + lint issues)

Check `workshop/level-5/sample-app/`:

| # | Bug | File to Check | What to Look For |
|---|-----|--------------|-----------------|
| 1 | divide(x, 0) returns None | mathlib/calculator.py | Should raise ValueError |
| 2 | Negative exponent wrong | mathlib/calculator.py | power(-2) returns 0 instead of 0.5 |
| 3 | Median off-by-one | mathlib/statistics.py | Even-length list median calculation |
| 4 | Mode returns first element | mathlib/statistics.py | Not finding most frequent |
| 5 | is_positive(0) returns True | mathlib/validator.py | Zero edge case |
| 6 | is_integer(str) crashes | mathlib/validator.py | Missing try/except |
| 7 | Unused imports | Multiple files | `import math`, `import os` not used |
| 8 | Missing docstring | mathlib/ | `absolute()` function lacks docstring |

### Level 6 — URL Shortener (5 issues)

Check `workshop/level-6/sample-app/`:

| # | Issue | What to Check |
|---|-------|--------------|
| 1 | Delete doesn't decrement stats | store.py delete() + stats.py |
| 2 | Missing test_validator.py | tests/ directory |
| 3 | No URL expiration | Feature entirely absent |
| 4 | Code duplication | Repeated patterns across store operations |
| 5 | Incomplete test assertions | Existing test files |

## Output Format

```markdown
## Bug Verification Report

### Level 3/4: Quick Notes CLI
| # | Bug | Status | Evidence |
|---|-----|--------|----------|
| 1 | Off-by-one display | ✅ Present / ❌ Fixed / ⚠️ Modified | Line X in file.py |
...

### Level 5: Math Utilities
...

### Level 6: URL Shortener
...

### Summary
- Total bugs cataloged: 19+
- Still present: X
- Missing/fixed: X (⚠️ NEEDS ATTENTION)
- Modified but equivalent: X
```

If any bugs are missing, flag them prominently — these are essential for teaching exercises.
