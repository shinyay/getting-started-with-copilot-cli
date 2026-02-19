# Level 3 — Quick Reference Card

## Plan Mode Commands

| Command | Purpose |
|---------|---------|
| `/plan <description>` | Create an implementation plan |
| `Shift+Tab` | Cycle between modes (Interactive → Plan → ...) |
| Follow-up message | Refine the current plan |
| "No" / "Reject" | Reject the plan and redirect |

## Plan Refinement Workflow

```
/plan [broad task]
  ↓
"Too broad — focus on X and Y only"
  ↓
"Add constraint: don't change Z"
  ↓
"Also include: testing/docs step"
  ↓
"Show me the final plan"
```

## The 8-Point Plan Review Checklist

| # | Check | Question |
|---|-------|----------|
| 1 | **Scope** | Is every step necessary? Is anything missing? |
| 2 | **Order** | Are steps sequenced correctly? |
| 3 | **Risk** | What's the worst that could happen? |
| 4 | **Testing** | How do we verify it works? |
| 5 | **Reversibility** | Can we undo if something breaks? |
| 6 | **Constraints** | Does it respect existing architecture? |
| 7 | **Migration** | What about existing data? |
| 8 | **Edge cases** | What unusual inputs could break it? |

## Constraint Types

| Type | Example |
|------|---------|
| **API preservation** | "Don't change the function signature" |
| **File scope** | "Only modify export.py" |
| **Technology** | "Standard library only" |
| **Size** | "Maximum 30 lines of changes" |
| **Compatibility** | "Existing data must still load" |
| **Performance** | "Must handle 10,000 notes" |

## Planning by Task Type

| Task | Key Principles |
|------|---------------|
| **Bug fix** | Minimal change, consider migration, test the fix |
| **New feature** | Define interface first, implement bottom-up, verify with acceptance criteria |
| **Refactoring** | Tests before refactoring, incremental steps, no behavior change |
| **Documentation** | Generate from code, verify against implementation |

## Rejection Patterns

| Type | Template |
|------|----------|
| **Too broad** | "Only focus on X, not Y and Z" |
| **Wrong approach** | "Don't rewrite — just add error handling" |
| **Out of scope** | "This is a CLI app, not a web app" |
| **Partial** | "Keep steps 1–3, remove 4–5" |
| **Wrong priority** | "Fix bugs first, then add features" |

## Multi-File Change Order

```
Safest: Bottom-up
  config.py → models.py → storage.py → notes.py
  (Lower layers first, wire up last)
  
Riskiest: All-at-once
  (Only when changes are tightly coupled)
```

## Comparing Alternative Plans

| Criteria | Plan A | Plan B | Plan C |
|----------|--------|--------|--------|
| Complexity | ? | ? | ? |
| User value | ? | ? | ? |
| Implementation time | ? | ? | ? |
| Risk level | ? | ? | ? |
| Maintainability | ? | ? | ? |

## Exercises at a Glance

| # | Exercise | Key Skill |
|---|----------|-----------|
| 1 | Your First Plan | `/plan` basics, plan structure |
| 2 | Reading Plans Critically | 6-point evaluation checklist |
| 3 | Refining Plans | Iterative narrowing through conversation |
| 4 | Rejecting Plans | Saying no with reasons |
| 5 | Planning Bug Fixes | Minimal fix, migration, backward compat |
| 6 | Planning Features | Scope, interface, steps, testing |
| 7 | Planning Refactoring | Test-first, incremental, behavior-preserving |
| 8 | Planning with Constraints | Bounding plans for focus |
| 9 | Multi-File Changes | Implementation order, coordination |
| 10 | Comparing Alternatives | Decision matrix, tradeoff evaluation |
| 11 | Planning from Requirements | User stories → plans, bug reports → plans |
| 12 | Plan Review as a Skill | The complete 8-point checklist |
