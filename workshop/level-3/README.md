# Level 3: Plan — Think Before Acting

> **Risk level:** 🟢 Zero — Plans don't modify files. You create, review, refine, and reject plans without any code being written.

## Learning Objectives

By the end of this level, you will be able to:

1. Enter plan mode and create implementation plans with `/plan`
2. Read plans critically — assess scope, completeness, and risk
3. Refine plans through iterative conversation
4. Reject plans and explain why — plans don't commit you to anything
5. Create plans for different task types (bug fix, feature, refactoring, documentation)
6. Add constraints to plans ("don't change X", "use pattern Y")
7. Plan multi-file changes and understand their cross-file impact
8. Request alternative approaches and compare them
9. Plan from user stories and requirements
10. Use plans as a pre-implementation review tool
11. Understand when plan mode vs interactive mode is appropriate
12. Build the habit of always planning before implementing

---

## Prerequisites

- [ ] Completed **Level 1** and **Level 2**
- [ ] Comfortable with `@`, `!`, `/help`, `/model`, `/context`, `/compact`
- [ ] Can map dependencies, trace execution, and identify patterns (Level 2 skills)

---

## About the Sample App

Level 3 uses a **Quick Notes CLI** — a note-taking app with **intentional issues**.

> Unlike Level 2's clean, well-structured Bookmark API, this app has **8 bugs and 8 TODOs** deliberately embedded. You won't fix them here — you'll discover and plan fixes. Level 4 is where you execute those plans.

```
sample-app/
├── notes.py        ← CLI entry point and command handling
├── storage.py      ← JSON file-based persistence
├── models.py       ← Note data model and validation
├── search.py       ← Full-text search (with known bugs)
├── export.py       ← Markdown and HTML export (with XSS bug)
├── config.py       ← Configuration constants
└── requirements.txt
```

### Intentional Issues Planted (for planning practice)

| Type | Location | Issue |
|------|----------|-------|
| 🐛 Bug | `search.py` | Case-sensitive search — "Python" doesn't find "python" |
| 🐛 Bug | `models.py` | Tags not normalized (no lowercase, no strip) |
| 🐛 Bug | `storage.py` | No error handling for corrupted JSON |
| 🐛 Bug | `export.py` | HTML export has XSS vulnerability (no escaping) |
| 🐛 Bug | `export.py` | Newlines in body not converted to `<br>` in HTML |
| 🐛 Bug | `notes.py` | List doesn't sort pinned notes first |
| 🐛 Bug | `notes.py` | Edit bypasses validation (can set empty title) |
| 🐛 Bug | `storage.py` | No thread safety for concurrent writes |
| 📝 TODO | `config.py` | No config file support (~/.quicknotes.toml) |
| 📝 TODO | `search.py` | No search operators (tag:X, title:"Y") |
| 📝 TODO | `search.py` | No relevance scoring |
| 📝 TODO | `search.py` | No match highlighting |
| 📝 TODO | `export.py` | No PDF/JSON export |
| 📝 TODO | `export.py` | No export filtering by tag |
| 📝 TODO | `notes.py` | No import/archive/merge commands |
| 📝 TODO | `models.py` | No individual tag format validation |

You'll **plan** how to fix/implement these — but you won't execute the plans (that's Level 4).

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **60–90 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Your First Plan | 5 min |
| 2 | Reading Plans Critically | 7 min |
| 3 | Refining Plans Through Conversation | 7 min |
| 4 | Rejecting Plans | 5 min |
| 5 | Planning a Bug Fix | 7 min |
| 6 | Planning a New Feature | 7 min |
| 7 | Planning a Refactoring | 7 min |
| 8 | Planning with Constraints | 5 min |
| 9 | Planning Multi-File Changes | 7 min |
| 10 | Comparing Alternative Plans | 7 min |
| 11 | Planning from Requirements | 5 min |
| 12 | Plan Review as a Skill | 5 min |

---

## Exercise 1: Your First Plan

### Goal
Enter plan mode and create your first implementation plan. Observe the structure and detail of what Copilot produces.

### Steps

**1.1** Navigate to the sample app and launch Copilot:

```bash
cd workshop/level-3/sample-app
copilot
```

**1.2** Create your first plan with the `/plan` slash command:

```
/plan Fix the case-sensitive search bug in search.py
```

**1.3** Observe the plan structure. Copilot should produce something like:

> **Plan:**
> 1. Modify `search.py` `_matches()` function
> 2. Convert both the query and the search targets to lowercase
> 3. Ensure existing behavior is preserved for exact matches
> 4. Test the fix

**1.4** **Do NOT approve the plan.** Just read it. Notice:
- Which files it proposes to change
- What order it proposes to make changes
- Whether it mentions testing
- Whether it mentions edge cases

**1.5** Ask a follow-up question about the plan:

```
What edge cases should this plan consider?
```

### Key Concept: Plan Mode

| Aspect | Detail |
|--------|--------|
| **How to enter** | `/plan <description>` or switch mode with `Shift+Tab` |
| **What it produces** | A step-by-step implementation plan |
| **Does it modify files?** | **No** — plans are proposals, not actions |
| **Can you reject it?** | Yes — just say no or ask for a different approach |
| **When to use** | Before any multi-step change, refactoring, or feature |

### ✅ Checkpoint
You can create a plan with `/plan` and read its structure.

---

## Exercise 2: Reading Plans Critically

### Goal
Develop the skill of evaluating whether a plan is **complete, safe, and well-scoped**.

### Steps

**2.1** Create a plan for a more complex task:

```
/plan Add HTML escaping to the export.py HTML output to fix the XSS vulnerability
```

**2.2** Evaluate the plan using this checklist:

| Criteria | Question to Ask |
|----------|----------------|
| **Completeness** | Does the plan cover ALL places where user input is rendered as HTML? |
| **Safety** | Could this plan break existing functionality? |
| **Scope** | Does the plan change only what's necessary, or does it over-reach? |
| **Testing** | Does the plan include verification steps? |
| **Dependencies** | Does the plan account for imports or libraries needed? |
| **Order** | Are the steps in the right sequence? |

**2.3** Ask Copilot to self-evaluate:

```
Review your own plan. Are there any gaps?
What could go wrong if we followed this plan exactly?
```

**2.4** Ask about what the plan does NOT cover:

```
This plan fixes HTML escaping in titles and bodies. 
But what about tags? Are they also rendered unescaped?
```

### Key Concept: The Plan Review Checklist

Always evaluate plans against these 6 criteria before approving. This is the skill that prevents bad implementations.

### ✅ Checkpoint
You can read a plan and identify what's missing, what's risky, and what needs refinement.

---

## Exercise 3: Refining Plans Through Conversation

### Goal
Learn to iterate on plans — making them better through conversation before any code is written.

### Steps

**3.1** Start with a broad plan:

```
/plan Make the search feature more robust and useful
```

**3.2** The plan will likely be vague. Narrow it down:

```
The plan is too broad. Focus only on two things:
1. Make search case-insensitive
2. Add support for tag-specific search with "tag:python" syntax
Don't change anything else.
```

**3.3** Copilot should produce a refined plan. Now add a constraint:

```
Good, but I want the tag:python syntax to work WITHOUT changing the CLI argument parsing.
The search function itself should detect the "tag:" prefix in the query string.
```

**3.4** Add a quality requirement:

```
Also add a step to update the docstring in search.py to document the new tag: syntax.
```

**3.5** Ask for the final consolidated plan:

```
Summarize the refined plan as a numbered list of concrete steps.
```

### Key Concept: Plan Refinement Workflow

```
/plan [broad task]
  ↓
"Too broad — focus on X and Y only"
  ↓
"Add constraint: don't change Z"
  ↓
"Also include: documentation update"
  ↓
"Show me the final plan"
```

> 💡 **Each refinement makes the plan more precise.** The goal is to have a plan so clear that implementation becomes mechanical.

### ✅ Checkpoint
You can take a vague plan and refine it through 3–4 rounds of conversation into a precise, scoped plan.

---

## Exercise 4: Rejecting Plans

### Goal
Learn to say no — reject plans that are wrong, over-scoped, or use the wrong approach.

### Steps

**4.1** Create a plan that you'll intentionally reject:

```
/plan Rewrite the entire storage.py to use SQLite instead of JSON
```

**4.2** Reject it with a reason:

```
No, that's too big a change. The JSON storage works fine for this use case.
I only want to add error handling for corrupted JSON files — nothing else.
```

**4.3** Copilot should propose a new, narrower plan. Evaluate it.

**4.4** Try another rejection scenario:

```
/plan Add a web UI for the notes app
```

Reject:

```
No, this is a CLI app and should stay a CLI app. 
Instead, plan how to improve the CLI output formatting — 
add color coding for tags and bold for pinned notes.
```

**4.5** Practice partial rejection — keep some steps, remove others:

```
/plan Add import, archive, and merge commands to notes.py
```

Then:

```
I like the import and archive commands, but merge is too complex for now. 
Remove the merge command from the plan and keep just import and archive.
```

### Key Concept: Rejection Is a Planning Skill

| Rejection Type | Example |
|---|---|
| **Too broad** | "Only focus on X, not Y and Z" |
| **Wrong approach** | "Don't rewrite — just add error handling" |
| **Out of scope** | "This is a CLI app, not a web app" |
| **Partial** | "Keep steps 1–3, remove steps 4–5" |
| **Wrong priority** | "Fix the bugs first, then add features" |

> 💡 **Rejecting bad plans is more valuable than accepting mediocre ones.** The ability to say "no, because..." is what separates effective planning from letting AI drive.

### ✅ Checkpoint
You can reject plans with clear reasons and redirect Copilot to a better approach.

---

## Exercise 5: Planning a Bug Fix

### Goal
Create a precise, minimal plan for fixing a specific bug.

### Steps

**5.1** First, understand the bug (use Level 2 skills):

```
@ models.py

The comment says tags are not normalized. Explain the bug:
what currently happens, what should happen, and what user behavior triggers it?
```

**5.2** Now plan the fix:

```
/plan Fix the tag normalization bug in models.py. Tags should be lowercased 
and stripped on creation. Make sure this doesn't break existing notes that 
might have mixed-case tags in the JSON file.
```

**5.3** Evaluate the plan for the **migration problem**:

```
Your plan normalizes tags on creation. But what about existing notes in notes.json 
that already have mixed-case tags? Should the plan include a migration step?
What are the tradeoffs of migrating vs not migrating?
```

**5.4** Ask for the minimal fix:

```
What is the absolute minimum change needed to fix this bug? 
Show the smallest possible plan — one or two steps max.
```

### Key Concept: Bug Fix Planning Principles

1. **Understand before planning** — always reproduce/explain the bug first
2. **Minimal change** — fix the bug without refactoring everything
3. **Consider data migration** — existing data might have the bug baked in
4. **Consider backwards compatibility** — will the fix break anything?

### ✅ Checkpoint
You can plan a bug fix that's minimal, considers migration, and doesn't break existing behavior.

---

## Exercise 6: Planning a New Feature

### Goal
Plan a new feature from scratch — covering design, implementation steps, and verification.

### Steps

**6.1** Plan a search operators feature:

```
/plan Add search operator support to search.py so users can type:
- "tag:python" to search by tag only
- "title:meeting" to search by title only  
- Plain text searches title, body, and tags (current behavior)
```

**6.2** Evaluate the plan for completeness:

```
Does your plan cover:
1. Parsing the operator prefix from the query string?
2. Handling multiple operators in one query (e.g., "tag:python title:meeting")?
3. What happens with malformed operators like "tag:" (empty value)?
4. Updating the help text in notes.py?
```

**6.3** Ask about the interface contract:

```
Before planning the implementation, let's agree on the interface:
- What should the function signature look like?
- Should search_notes() handle operator parsing, or should there be a new function?
- Should operators be case-sensitive? Should "TAG:python" work?
```

**6.4** Get the final plan:

```
Now give me the complete implementation plan with:
1. Which files to modify
2. What to add to each file
3. In what order
4. How to test it manually
```

### Key Concept: Feature Planning Workflow

```
1. Define the user-facing behavior (what does the user see?)
2. Agree on the interface contract (function signatures, data flow)
3. Plan the implementation steps (which files, what changes)
4. Plan the verification (how to test)
```

### ✅ Checkpoint
You can plan a feature with clear scope, interface contracts, implementation steps, and verification.

---

## Exercise 7: Planning a Refactoring

### Goal
Plan a structural improvement that changes the code without changing behavior.

### Steps

**7.1** Identify a refactoring opportunity:

```
@ notes.py

The main() function handles all commands in a long if/elif chain. 
This is a code smell. What pattern would be better?
```

**7.2** Plan the refactoring:

```
/plan Refactor notes.py to use a command handler pattern instead of the if/elif chain.
Each command should be a separate function registered in a dictionary.
The behavior must be identical — no user-facing changes.
```

**7.3** Challenge the plan on behavior preservation:

```
How can we verify that this refactoring doesn't change any behavior?
What test strategy would catch regressions?
Since there are no tests currently, should the plan include adding tests BEFORE refactoring?
```

**7.4** Ask about the refactoring order:

```
What's the safest order to do this refactoring?
Should we:
a) Write tests first, then refactor?
b) Refactor first, then add tests?
c) Refactor one command at a time?

Which approach minimizes the risk of breaking something?
```

### Key Concept: Refactoring Plans Are Special

| Rule | Why |
|------|-----|
| **No behavior change** | Refactoring changes structure, not function |
| **Tests first** | You need tests to prove behavior is preserved |
| **Incremental** | One change at a time, verify after each |
| **Reversible** | If something breaks, you can revert one small change |

### ✅ Checkpoint
You can plan a refactoring with test-first strategy, incremental steps, and behavior preservation.

---

## Exercise 8: Planning with Constraints

### Goal
Learn to add constraints that bound what the plan can and cannot do.

### Steps

**8.1** Plan with an API preservation constraint:

```
/plan Add input validation for individual tag format in models.py.
Tags should only allow lowercase letters, numbers, and hyphens.

CONSTRAINT: Do not change the Note class constructor signature.
CONSTRAINT: Do not change any code in notes.py.
CONSTRAINT: Existing notes with invalid tags should still load (don't crash on read).
```

**8.2** Verify the plan respects the constraints:

```
Check your plan against the constraints I gave you.
Does any step violate "do not change notes.py"?
Does any step break loading of existing notes with invalid tags?
```

**8.3** Add a technology constraint:

```
/plan Add JSON export support to export.py.

CONSTRAINT: Use only the Python standard library — no external packages.
CONSTRAINT: The JSON export must be valid input for a future "import" command.
CONSTRAINT: Maximum 30 lines of new code.
```

**8.4** Add a time/scope constraint:

```
/plan Improve the HTML export to fix the XSS bug and handle newlines.

CONSTRAINT: This should be completable in under 20 lines of changes.
If it requires more, simplify the approach.
```

### Key Concept: Constraint Types

| Constraint | Example |
|---|---|
| **API preservation** | "Don't change the function signature" |
| **File scope** | "Only modify export.py — nothing else" |
| **Technology** | "Standard library only" |
| **Size** | "Maximum 30 lines of new code" |
| **Compatibility** | "Existing data must still load" |
| **Performance** | "Must handle 10,000 notes without slowdown" |

> 💡 **Constraints make plans better by bounding them.** An unconstrained plan often over-scopes. Constraints force focus.

### ✅ Checkpoint
You can add constraints to plans and verify the plan respects them.

---

## Exercise 9: Planning Multi-File Changes

### Goal
Plan changes that span multiple files and understand the coordination required.

### Steps

**9.1** Plan a cross-cutting feature:

```
/plan Add a "last modified" sort option to the list command.
This requires changes to:
- config.py (add sort options constant)
- notes.py (add --sort argument to list command)  
- storage.py (add sorted listing capability)

Show me which files change in which order and why that order matters.
```

**9.2** Ask about the dependency order:

```
If I implement these changes in the wrong order, which combinations would 
cause import errors or runtime failures?
What's the safest implementation order — bottom-up or top-down?
```

**9.3** Plan a larger cross-file change:

```
/plan Add a complete "archive" feature:
- Notes can be archived (hidden from default list, but not deleted)
- Archived notes can be restored
- "list --archived" shows archived notes
- "stats" includes archive count

Show me every file that needs to change and what changes in each.
```

**9.4** Evaluate the coordination:

```
Your plan modifies 4+ files. If I implement changes to storage.py but not yet to notes.py,
will the app still work? Or do all changes need to land simultaneously?
```

### Key Concept: Multi-File Planning

| Strategy | When to Use |
|---|---|
| **Bottom-up** (models → storage → notes) | App stays runnable after each step |
| **Top-down** (notes → storage → models) | You see the UI first, then wire it |
| **All-at-once** | Changes are tightly coupled — partial state breaks things |

> 💡 **The safest approach is usually bottom-up** — add capabilities to lower layers first, then wire them into upper layers. The app stays functional at every step.

### ✅ Checkpoint
You can plan multi-file changes, identify the safe implementation order, and understand coordination risks.

---

## Exercise 10: Comparing Alternative Plans

### Goal
Request multiple approaches to the same problem and evaluate their tradeoffs.

### Steps

**10.1** Ask for two different approaches:

```
I want to fix the corrupted JSON error handling in storage.py.
Give me TWO different plans:

Plan A: Minimal — just wrap the read in try/except and return empty data
Plan B: Robust — add backup files, corruption detection, and automatic recovery

For each, list: steps, pros, cons, and complexity.
```

**10.2** Compare them:

```
Compare Plan A and Plan B:
- Which is faster to implement?
- Which is safer for user data?
- Which is easier to test?
- Which would you recommend for a personal tool vs a team tool?
```

**10.3** Try a three-way comparison:

```
I want to improve the search. Give me THREE approaches:

Plan A: Just make it case-insensitive (minimal fix)
Plan B: Add search operators (tag:, title:) but keep simple implementation
Plan C: Add a proper search index for fast full-text search

Compare all three on: complexity, user value, implementation time, and maintainability.
```

**10.4** Make a decision:

```
Based on the comparison, I want to combine Plan A and Plan B — 
case-insensitive search with basic operators.
Create a single consolidated plan from those two approaches.
```

### Key Concept: Decision Matrix

| Criteria | Plan A | Plan B | Plan C |
|----------|--------|--------|--------|
| Complexity | Low | Medium | High |
| User value | Low | Medium | High |
| Implementation time | Short | Medium | Long |
| Risk | Low | Low | Medium |

> 💡 **Always compare at least 2 approaches before committing.** The best solution is often a combination.

### ✅ Checkpoint
You can request multiple approaches, compare them systematically, and make informed decisions.

---

## Exercise 11: Planning from Requirements

### Goal
Translate user stories and requirements into implementation plans.

### Steps

**11.1** Start from a user story:

```
/plan 
User story: "As a user, I want to export only notes with a specific tag, 
so that I can share my work notes without including personal ones."

Acceptance criteria:
- export --tag work exports only notes tagged "work"
- export --tag work --format html produces valid HTML with only matching notes
- If no notes match, the export file should contain a "No notes found" message
```

**11.2** Evaluate completeness against the acceptance criteria:

```
Check your plan against each acceptance criterion. 
Does the plan explicitly cover ALL three criteria?
Are there any criteria that would pass by accident vs being explicitly implemented?
```

**11.3** Plan from a bug report:

```
/plan
Bug report: "When I edit a note with --title '' (empty string), the note 
saves successfully but then crashes when I try to list notes because the 
display code can't handle an empty title."

Steps to reproduce:
1. python notes.py add "Test note"
2. python notes.py edit 1 --title ""  
3. python notes.py list  ← crash

Fix this so that step 2 rejects the empty title with a clear error message.
```

**11.4** Plan from a technical requirement:

```
/plan
Technical requirement: "The storage layer must handle corrupted JSON files 
gracefully. If the file can't be parsed, the system should:
1. Log a warning
2. Create a backup of the corrupted file (e.g., notes.json.corrupt)
3. Start with empty data
4. NOT crash or lose the corrupted file"
```

### Key Concept: Requirements → Plans

| Requirement Type | Planning Approach |
|---|---|
| **User story** | Map acceptance criteria to implementation steps |
| **Bug report** | Reproduce → root cause → fix → verify steps |
| **Technical spec** | Map each requirement to specific code changes |
| **Performance** | Benchmark → identify bottleneck → optimize → re-benchmark |

### ✅ Checkpoint
You can translate user stories, bug reports, and technical specs into concrete implementation plans.

---

## Exercise 12: Plan Review as a Skill

### Goal
Consolidate everything into a repeatable plan review workflow that you'll use in every future level.

### Steps

**12.1** Create a plan for the most complex task you can think of:

```
/plan Add a complete "notebook" feature to Quick Notes:
- Notes belong to notebooks (default: "general")
- Users can create, list, and switch notebooks
- Each notebook has its own notes.json file
- Export can target a specific notebook
- Search can span all notebooks or just the current one
```

**12.2** Review the plan using the **complete review checklist**:

```
Review your own plan against all of these criteria:

SCOPE: Is every step necessary? Is anything missing?
ORDER: Are steps in the right sequence? Would a different order be safer?
RISK: What could go wrong? What's the blast radius of each step?
TESTING: How would we verify each step works?
REVERSIBILITY: Can we undo each step if it breaks something?
CONSTRAINTS: Does it respect the existing architecture?
MIGRATION: What happens to existing notes.json files?
EDGE CASES: What about empty notebooks? Duplicate names? Special characters?
```

**12.3** Force yourself to find 3 problems with the plan:

```
Find at least 3 weaknesses, gaps, or risks in your plan. Be harsh.
```

**12.4** Refine based on the review:

```
Address the 3 issues you found. Show me the revised plan.
```

**12.5** Compress and retain the planning skill:

```
/compact
```

Then:

```
Summarize the key principles of good planning in 5 bullet points, 
based on everything we practiced today.
```

### The Complete Plan Review Checklist

Use this for every plan in Level 4 and beyond:

| # | Check | Question |
|---|-------|----------|
| 1 | **Scope** | Is every step necessary? Is anything missing? |
| 2 | **Order** | Are steps sequenced correctly? Safe implementation order? |
| 3 | **Risk** | What's the worst that could happen? Blast radius? |
| 4 | **Testing** | How do we verify the plan worked? |
| 5 | **Reversibility** | Can we undo if something breaks? |
| 6 | **Constraints** | Does it respect existing architecture and APIs? |
| 7 | **Migration** | What about existing data? |
| 8 | **Edge cases** | What unusual inputs or states could break it? |

### ✅ Checkpoint
You have a repeatable plan review workflow and can find weaknesses in any plan.

---

## 🏆 Level 3 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Create plans with `/plan` | ☐ | ☐ | ☐ |
| 2 | Read plans critically (completeness, safety, scope) | ☐ | ☐ | ☐ |
| 3 | Refine plans through iterative conversation | ☐ | ☐ | ☐ |
| 4 | Reject plans with clear reasons | ☐ | ☐ | ☐ |
| 5 | Plan bug fixes (minimal, migration-aware) | ☐ | ☐ | ☐ |
| 6 | Plan new features (scope, interface, steps, testing) | ☐ | ☐ | ☐ |
| 7 | Plan refactorings (behavior-preserving, test-first) | ☐ | ☐ | ☐ |
| 8 | Add and verify constraints on plans | ☐ | ☐ | ☐ |
| 9 | Plan multi-file changes with safe ordering | ☐ | ☐ | ☐ |
| 10 | Compare alternative approaches systematically | ☐ | ☐ | ☐ |
| 11 | Translate requirements/stories into plans | ☐ | ☐ | ☐ |
| 12 | Review plans using the complete checklist | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 4
- **22–29:** Review exercises 7–12 once more
- **Below 22:** Repeat with different tasks on the same codebase

---

## Key Takeaways

1. **Always plan before implementing** — `/plan` costs nothing and saves hours
2. **Plans are proposals, not commitments** — reject freely and often
3. **Refine through conversation** — 3–4 rounds of narrowing beats one shot
4. **Constraints make plans better** — unconstrained plans over-scope
5. **Compare alternatives** — never commit to the first approach
6. **Review every plan** — use the 8-point checklist before approving
7. **Bottom-up is safest for multi-file** — lower layers first, wire up last
8. **The best plan is the smallest one that works** — minimal > comprehensive

---

## What's Next

**Level 4: Create — Make Your First Changes** is where plans become reality. You'll approve plans and watch Copilot implement them, learning the approval flow, `/diff`, and `/review` in the process.

→ Continue to `workshop/level-4/README.md`
