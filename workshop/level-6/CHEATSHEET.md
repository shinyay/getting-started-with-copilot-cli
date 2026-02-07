# Level 6 Cheat Sheet — Complete Workflows

## The 7 Workflow Types

| Workflow | When to Use | Core Steps |
|----------|-------------|------------|
| **Feature** | New functionality | Investigate → Plan → Implement → Test → Diff → Review |
| **Bug Fix** | Something broken | Reproduce → Investigate → Root Cause → Plan → Fix → Regression Test |
| **Test Gap** | Missing coverage | Discover → Analyze → Plan → Write Tests → Run → Review |
| **Refactor** | Code smell | Identify → Plan → Baseline Tests → Refactor → Verify → Review |
| **Documentation** | Docs ≠ Code | Audit → Plan → Update → Verify Examples → Review |
| **Hotfix** | Urgent fix | Minimal Change → Test → Small Diff → Deploy |
| **Requirements** | Vague ask | Clarify → Decide → Plan → Implement → Validate |

## Feature Workflow Template

```
1. @ relevant-files          ← Investigate current state
2. /plan [feature spec]      ← Create the plan
3. "Does this handle X?"     ← Challenge edge cases
4. Approve edits             ← Implement
5. Write + run tests         ← Verify correctness
6. /diff                     ← Check what changed
7. /review                   ← AI quality assessment
```

## Bug Fix Workflow Template

```
1. Reproduce the bug         ← Confirm it exists
2. @ file1 @ file2           ← Read involved files
3. "Trace the data flow"     ← Follow the logic
4. /plan Fix [description]   ← Plan the fix
5. Approve edits             ← Implement
6. Write regression test     ← Prevent recurrence
7. make test && /diff        ← Verify everything
```

## Refactoring Checklist

```
□ Identified the duplication/smell
□ Ran tests BEFORE (baseline green)
□ Plan changes structure only, NOT behavior
□ Implemented refactoring
□ Ran tests AFTER (same green)
□ /diff shows only structural changes
□ /review confirms behavioral equivalence
```

## Hotfix Rules

| Rule | Why |
|------|-----|
| Change ≤ 5 lines | Minimal risk |
| One concern only | No sneaking in features |
| Test immediately | No manual-only verification |
| `/diff` must be tiny | If big, something went wrong |

## Code Review Angles

```
# Correctness
/review Does this code do what it's supposed to?

# Security
/review Are there any unvalidated inputs or injection risks?

# Testing
/review Are all new code paths covered by tests?

# Performance
/review Any obvious inefficiencies or N+1 patterns?

# Maintainability
/review Will future developers understand these changes?
```

## Recovery Decision Tree

```
Mistake discovered
    │
    ├── Small, isolated → FIX FORWARD (patch it)
    │
    ├── Wrong approach → REVERT ALL (git checkout -- .)
    │
    ├── One bad file → SELECTIVE REVERT (git checkout -- file.py)
    │
    └── Half done, half good → SELECTIVE REVERT bad parts only
```

## Common Prompts

```
# Investigation
@ store.py @ stats.py  Trace how stats are calculated after delete.

# Feature planning
/plan Add [feature] with these requirements: 1. ... 2. ... 3. ...

# Interleaved development
Implement search() in store.py. Then write tests for it. Then run tests.

# Vague requirements
"What questions should I ask the stakeholder about this requirement?"

# Multi-angle review
/review Focus on: security, testing coverage, and edge cases.

# Commit message
Write a conventional commit message for these changes referencing Issue #42.
```

## The Complete SDLC in One Copilot Session

```
Issue → Investigate → Plan → Implement → Test → Diff → Review → Commit
```

## Sample App Issues

| # | Type | Files | Description |
|---|------|-------|-------------|
| 1 | Bug | `store.py` + `stats.py` | Stats wrong after delete (counter not decremented) |
| 2 | Test gap | `validator.py` | Zero tests — module completely untested |
| 3 | Feature gap | `config.py` + `store.py` | Expiration defined but not implemented |
| 4 | Duplication | `cli.py` + `validator.py` | URL validation exists in two places |
| 5 | Test gap | `test_stats.py` | After-delete scenario not tested |

## Tips

- **Investigate before every workflow** — even hotfixes need 10 seconds of reading
- **Test before AND after refactoring** — same tests, same results = safe
- **Interleave tests with implementation** — catches bugs at each step
- **Hotfix ≠ hack** — minimal doesn't mean careless
- **Reflect after every major workflow** — the meta-skill that improves everything
