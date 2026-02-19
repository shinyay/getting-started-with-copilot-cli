# Level 6: Workflow — The Full Plan → Execute → Review Cycle

> **Risk level:** 🟠 Medium — You will perform complete development workflows: building features, fixing multi-file bugs, refactoring, writing tests, and updating documentation — all through Copilot.

## Learning Objectives

By the end of this level, you will be able to:

1. Execute the full **plan → implement → test → diff → review** cycle for a new feature
2. Debug multi-file bugs using systematic investigation workflows
3. Discover and fill test coverage gaps
4. Plan and execute safe refactors with regression verification
5. Generate and verify documentation from code
6. Perform code review workflows on changes
7. Execute time-pressured hotfixes with minimal-change discipline
8. Build features and their tests in a single coordinated workflow
9. Translate vague requirements into concrete implementations
10. Run the end-to-end Issue → Plan → Implement → Test → Review workflow
11. Recover when a workflow goes wrong mid-cycle
12. Analyze and improve your own workflow efficiency

---

## Prerequisites

- [ ] Completed **Levels 1–5** (all individual skills)
- [ ] Comfortable with: `@`, `/plan`, `/diff`, `/review`, `!` shell escapes
- [ ] Comfortable approving writes and bash commands
- [ ] Python 3.8+ with `pytest` installed

### Environment Setup

```bash
cd workshop/level-6/sample-app
pip install -r requirements.txt
make test   # Should see all tests pass (existing tests don't cover the bugs)
```

---

## About the Sample App

Level 6 uses a **URL Shortener CLI** — a realistic multi-module Python application with intentional issues that require different workflow approaches to resolve.

> Unlike Level 5's math library (focused on running tests and linters), this app is designed for **complete workflow practice**: it has a multi-file bug (stats wrong after delete), test coverage gaps (validator.py untested), a feature gap (expiration), and duplicated logic — each requiring a different workflow to resolve.

```
sample-app/
├── shortener/
│   ├── cli.py           ← CLI entry (DUPLICATION: has its own _quick_validate)
│   ├── store.py         ← URL storage (BUG: delete doesn't update stats)
│   ├── hasher.py        ← Code generation (clean)
│   ├── validator.py     ← URL validation (UNTESTED — zero tests)
│   ├── stats.py         ← Statistics (BUG: wrong after delete)
│   └── config.py        ← Configuration (FEATURE GAP: expiry defined but unused)
├── tests/
│   ├── test_store.py    ← Good coverage
│   ├── test_hasher.py   ← Good coverage
│   ├── test_stats.py    ← Incomplete (missing after-delete test)
│   └── (test_validator.py is MISSING)
├── Makefile
└── requirements.txt
```

### Intentional Issues Summary

| # | Type | Description | Files Involved |
|---|------|-------------|----------------|
| 1 | **Multi-file bug** | Stats are wrong after deleting URLs | `store.py` + `stats.py` |
| 2 | **Test gap** | `validator.py` has zero test coverage | `validator.py` |
| 3 | **Feature gap** | URL expiration config exists but isn't implemented | `config.py` + `store.py` |
| 4 | **Duplication** | URL validation duplicated in `cli.py` and `validator.py` | `cli.py` + `validator.py` |
| 5 | **Test gap** | Stats after-delete scenario untested | `test_stats.py` |

### Safety Net

```bash
git checkout -- workshop/level-6/sample-app/
```

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **90–120 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Feature: Add URL Expiration | 12 min |
| 2 | Bug Hunt: Stats Wrong After Delete | 10 min |
| 3 | Test Gap: Write Tests for validator.py | 8 min |
| 4 | Refactor: Extract Duplicated Validation | 8 min |
| 5 | Documentation: Update README from Code | 7 min |
| 6 | Code Review Simulation | 8 min |
| 7 | Hotfix: Critical Bug Under Pressure | 7 min |
| 8 | Feature + Tests Together | 10 min |
| 9 | Vague Requirements → Implementation | 8 min |
| 10 | End-to-End: Issue → Plan → Code → Test → Review | 12 min |
| 11 | Recovery: When a Workflow Goes Wrong | 7 min |
| 12 | Workflow Retrospective | 5 min |

---

## Exercise 1: Feature — Add URL Expiration

### Goal
Build a complete feature from scratch using the full plan → implement → test → diff → review cycle.

### Context

The `config.py` already defines `DEFAULT_EXPIRY_HOURS = 0`, but expiration is never checked. URLs should optionally expire after a given number of hours.

### Steps

**1.1** Investigate the current state:

```
@ shortener/config.py
@ shortener/store.py

What expiration-related code already exists? What's missing to make URLs expire?
```

**1.2** Plan the feature:

```
/plan Add URL expiration support:
1. store.shorten() should accept an optional expiry_hours parameter
2. The entry should store an "expires_at" ISO timestamp (or null if no expiry)
3. store.expand() should check if the URL has expired before returning it
4. If expired, expand() should raise a KeyError with message "Short code 'X' has expired"
5. store.list_all() should include an "expired" boolean for each entry
6. Don't change the CLI yet — just the store module
```

**1.3** Review the plan critically:

```
Does this plan handle:
- URLs with expiry_hours=0 (no expiration)?
- Edge case: expand exactly at expiration time?
- Existing URLs that were created before this feature (no expires_at field)?
```

**1.4** Implement the feature:

> Approve the edits to `store.py`. Watch which functions are modified.

**1.5** Write tests for the new feature:

```
Add tests to test_store.py for URL expiration:
- test_shorten_with_expiry: shorten with expiry_hours=1 stores expires_at
- test_expand_not_expired: expand a non-expired URL works normally
- test_expand_expired: expand an expired URL raises KeyError
- test_no_expiry_default: shorten without expiry_hours has no expires_at
```

**1.6** Run the tests:

```
Run make test and verify all tests pass, including the new ones.
```

**1.7** Review everything:

```
/diff
```

```
/review Does the expiration feature handle all edge cases? 
Are the tests comprehensive?
```

### Key Concept: The Feature Workflow

```
1. INVESTIGATE  — understand current state (@ files)
2. PLAN         — /plan with specific requirements
3. REVIEW PLAN  — challenge edge cases before coding
4. IMPLEMENT    — approve edits
5. TEST         — write + run tests
6. DIFF         — verify changes match plan
7. REVIEW       — AI quality assessment
```

### ✅ Checkpoint
You built a feature using the complete 7-step workflow.

---

## Exercise 2: Bug Hunt — Stats Wrong After Delete

### Goal
Debug a multi-file bug using systematic investigation — the most realistic debugging workflow.

### Steps

**2.1** Reproduce the bug first:

```
Create 3 shortened URLs, delete 1, then show stats.
What does stats report for "total_created" and "active_urls"?
Is the math correct?
```

> 💡 The stats might look correct by coincidence in simple cases. Push harder:

```
Now create 2 more URLs, delete 2, and check stats again.
Does "deleted_urls" still match reality?
```

**2.2** Start the investigation:

```
@ shortener/stats.py
@ shortener/store.py

How does get_stats() calculate "deleted_urls"? 
Trace the data flow: where does "total_created" come from? 
Is it ever decremented?
```

**2.3** Identify the root cause:

```
The delete() function in store.py removes the URL from urls.json 
but doesn't update stats.json. Is that the full picture, or is there 
a deeper design issue?
```

**2.4** Plan the fix:

```
/plan Fix the stats-after-delete bug. Two options:
Option A: Track deletions explicitly (add "total_deleted" counter)
Option B: Don't derive "deleted" from arithmetic — count from source of truth

Which is more robust? Plan the better approach.
```

**2.5** Implement the fix:

> Approve edits. The fix should touch `store.py` (the `delete` function) and possibly `stats.py`.

**2.6** Write a regression test:

```
Add test_stats_after_delete to test_stats.py:
1. Create 3 URLs
2. Delete 1
3. Assert stats show total_created=3, active_urls=2, deleted_urls=1
4. Create 2 more
5. Delete 1
6. Assert stats show total_created=5, active_urls=3, deleted_urls=2
```

**2.7** Run tests and review:

```
Run make test. Then /diff. Then /review.
```

### Key Concept: The Bug Investigation Workflow

```
1. REPRODUCE     — confirm the bug exists with concrete steps
2. INVESTIGATE   — trace data flow across files
3. ROOT CAUSE    — identify the exact source (not just symptoms)
4. PLAN FIX      — consider multiple approaches
5. IMPLEMENT     — fix the root cause
6. REGRESSION    — write a test that catches this specific bug
7. VERIFY        — run all tests to check for side effects
```

### ✅ Checkpoint
You debugged a multi-file bug using systematic investigation and added a regression test.

---

## Exercise 3: Test Gap — Write Tests for validator.py

### Goal
Discover untested code and fill the gap with comprehensive tests.

### Steps

**3.1** Discover the gap:

```
List all test files in tests/. Which source modules in shortener/ 
have corresponding test files? Which don't?
```

**3.2** Analyze what needs testing:

```
@ shortener/validator.py

List every public function, its parameters, return type, 
and the edge cases that should be tested.
```

**3.3** Plan the test file:

```
/plan Create tests/test_validator.py with test cases for:
- is_valid_url: valid URLs, invalid URLs, empty, None, too long
- has_valid_scheme: http, https, ftp (invalid), missing scheme
- normalize_url: adds https://, strips trailing slash, handles empty
- validate_and_normalize: valid input, invalid input, empty string, None
```

**3.4** Implement the tests:

```
Create tests/test_validator.py with all the planned test cases.
```

**3.5** Run the tests:

```
Run make test-file FILE=tests/test_validator.py
```

**3.6** Check if any tests fail:

> If some tests fail, it could mean there are bugs in `validator.py` that the tests discovered!

**3.7** Review test quality:

```
/review Are the tests in test_validator.py comprehensive? 
What edge cases might be missing?
```

### Key Concept: Test-First Discovery

Writing tests for untested code often **reveals bugs** that were hidden because no tests exercised those code paths. This is different from TDD (where tests come first) — here you're retro-fitting tests and discovering issues.

### ✅ Checkpoint
You filled a test coverage gap and potentially discovered hidden bugs.

---

## Exercise 4: Refactor — Extract Duplicated Validation

### Goal
Plan and execute a refactoring that removes duplicated code, verified by the test suite.

### Steps

**4.1** Identify the duplication:

```
@ shortener/cli.py
@ shortener/validator.py

Show me the duplicated URL validation logic. 
What's in cli.py's _quick_validate that overlaps with validator.py?
```

**4.2** Plan the refactoring:

```
/plan Refactor cli.py to use validator.py instead of its own _quick_validate:
1. Import validate_and_normalize from validator
2. Replace _quick_validate() calls with validate_and_normalize()
3. Remove _quick_validate() function entirely
4. Ensure error messages remain user-friendly
```

**4.3** Run existing tests BEFORE the refactor:

```
Run make test and save the test count as the baseline.
```

**4.4** Implement the refactoring:

> Approve edits to `cli.py` only. The refactoring should NOT touch `validator.py`.

**4.5** Run tests AFTER the refactor:

```
Run make test. Same number of tests should pass. No new failures.
```

**4.6** Verify with `/diff`:

```
/diff
```

> Check: only `cli.py` should be modified. `validator.py` should be untouched.

**4.7** Review the refactoring:

```
/review Does the refactored cli.py have the same behavior as before? 
Any edge case where the new validation differs from the old _quick_validate?
```

### Key Concept: Safe Refactoring

```
1. IDENTIFY     — find duplication or code smell
2. PLAN         — specify what changes and what stays the same
3. BASELINE     — run tests before to establish "green"
4. REFACTOR     — change structure, not behavior
5. VERIFY       — same tests, same results
6. REVIEW       — confirm behavioral equivalence
```

> 💡 **The test suite is your safety net for refactoring.** If all tests pass after the refactor, behavior is preserved. This is why filling test gaps (Exercise 3) should come before refactoring.

### ✅ Checkpoint
You executed a safe refactoring with test-verified behavioral preservation.

---

## Exercise 5: Documentation — Update README from Code

### Goal
Generate accurate documentation from the actual code state.

### Steps

**5.1** Audit the current README:

```
@ sample-app/README.md
@ shortener/cli.py

Compare the README's "Usage" section with what the CLI actually supports.
Are there any commands in the README that don't exist in the code? 
Any commands in the code that aren't documented?
```

**5.2** Plan the documentation update:

```
/plan Update sample-app/README.md to accurately reflect the current CLI:
1. Fix the usage examples to match actual argparse commands
2. Add the "info" command (undocumented)
3. If we added expiration in Exercise 1, document it
4. Update the structure diagram to reflect current files
```

**5.3** Implement the update:

> Approve edits to `sample-app/README.md`.

**5.4** Verify accuracy:

```
For each CLI command in the updated README, verify it actually works 
by running the command through Copilot.
```

**5.5** Review:

```
/review Is the README accurate? Are all examples actually runnable?
```

### Key Concept: Documentation Workflow

```
1. AUDIT       — compare docs vs code (find drift)
2. PLAN        — list what needs updating
3. UPDATE      — regenerate from code truth
4. VERIFY      — run every example in the docs
5. REVIEW      — check accuracy and completeness
```

> 💡 **Code changes should always trigger doc updates.** After every feature or fix, ask: "Does the README still match the code?"

### ✅ Checkpoint
You can audit, update, and verify documentation in a systematic workflow.

---

## Exercise 6: Code Review Simulation

### Goal
Practice the code review workflow — reviewing changes as if they were a pull request.

### Steps

**6.1** First, make sure you have some changes from previous exercises:

```
!git diff --stat
```

> If you've reset, intentionally make some changes first:
> ```
> Fix the is_positive(0) bug in validator.py if it exists, 
> and add a docstring to the generate_code function in hasher.py.
> ```

**6.2** Start the review process:

```
/review
```

**6.3** Ask for a structured review:

```
Review the current changes as if this were a pull request. For each file:
1. Summarize what changed
2. Rate the change quality (good/needs-work/concern)
3. List any issues found
4. Suggest improvements
```

**6.4** Ask for specific review angles:

```
Review the changes from a security perspective. 
Are there any inputs that aren't validated? Any potential injection points?
```

```
Review the changes from a testing perspective. 
Are all new code paths covered by tests?
```

```
Review the changes from a maintainability perspective. 
Will future developers understand these changes?
```

**6.5** Ask for an approval decision:

```
Based on your review, would you approve this PR, request changes, 
or request more information? Explain your reasoning.
```

### Key Concept: Multi-Angle Review

| Review Angle | What to Check |
|-------------|---------------|
| **Correctness** | Does the code do what it's supposed to? |
| **Security** | Are inputs validated? Any injection risks? |
| **Testing** | Are new paths covered by tests? |
| **Performance** | Any obvious inefficiencies? |
| **Maintainability** | Will others understand this code? |
| **Completeness** | Is anything missing (docs, tests, error handling)? |

### ✅ Checkpoint
You can perform multi-angle code reviews using Copilot.

---

## Exercise 7: Hotfix — Critical Bug Under Pressure

### Goal
Execute a minimal-change fix when time pressure demands speed and precision.

### Steps

**7.1** Reset to a clean state:

```
!git checkout -- .
```

**7.2** Set the scenario — a "production" report came in:

```
URGENT: When a user expands a deleted short code, the error message leaks 
internal information (it shows "Short code 'X' not found" which confirms 
the code format is valid). 

We need to change the error to a generic "URL not found" for all invalid 
or deleted codes. This is a security hardening fix.

CONSTRAINT: Change as few lines as possible. This is a hotfix.
```

**7.3** Implement with minimal changes:

```
Fix the error message in store.py's expand() function. 
Change "Short code '{code}' not found" to "URL not found".
Change ONLY this one message. Don't refactor anything else.
```

**7.4** Verify the change is truly minimal:

```
/diff
```

> Expected: exactly **one line** changed in `store.py`.

**7.5** Check for test impact:

```
Run make test. Are any tests broken by this message change?
```

> If a test checks the exact error message, it will fail. Fix that test too — but note this as a second change.

**7.6** Review the hotfix:

```
/review This is a hotfix. Is the change minimal? Does it accomplish the goal?
Are there any unintended side effects?
```

### Key Concept: Hotfix Discipline

| Principle | Why |
|-----------|-----|
| **Minimal change** | Less risk, easier to review, faster to deploy |
| **One concern only** | Don't sneak in refactors or features |
| **Test immediately** | Hotfixes bypass normal review — tests catch mistakes |
| **Diff must be small** | If `/diff` shows more than expected, something went wrong |

### ✅ Checkpoint
You can execute disciplined minimal-change hotfixes.

---

## Exercise 8: Feature + Tests Together

### Goal
Build a feature and its tests in a single coordinated workflow — not feature-then-tests, but interleaved.

### Steps

**8.1** Plan a new feature with integrated tests:

```
/plan Add a "search" command to the CLI that finds URLs containing a keyword:
- Search across both short codes and original URLs
- Case-insensitive
- Return matching entries

For EACH implementation step, include the corresponding test.
The plan should alternate: implement step → test step → implement step → test step.
```

**8.2** Implement step 1 — the search function in `store.py`:

```
Add a search(keyword) function to store.py that searches 
across codes and URLs case-insensitively.
```

**8.3** Test step 1 immediately:

```
Add test_search to test_store.py:
- test_search_by_code: finds by code substring
- test_search_by_url: finds by URL substring
- test_search_case_insensitive: case doesn't matter
- test_search_no_results: returns empty list
Run the search tests.
```

**8.4** Implement step 2 — wire into CLI:

```
Add a "search" subcommand to cli.py that calls store.search() 
and displays results.
```

**8.5** Test the CLI integration:

```
Run the CLI search command:
!python -m shortener.cli shorten https://github.com --code git001
!python -m shortener.cli shorten https://google.com --code goo001
!python -m shortener.cli search "git"
```

**8.6** Run full test suite and review:

```
Run make test. Then /diff. Then /review.
```

### Key Concept: Interleaved Development

```
Traditional:          Interleaved:
1. Implement all      1. Implement step A
2. Test all           2. Test step A
                      3. Implement step B
                      4. Test step B
                      5. ...
```

> 💡 **Interleaved catches bugs earlier.** If step B's implementation breaks step A's tests, you catch it immediately — not after implementing everything.

### ✅ Checkpoint
You can build features with interleaved implementation and testing.

---

## Exercise 9: Vague Requirements → Implementation

### Goal
Translate ambiguous stakeholder requirements into a concrete, testable implementation.

### Steps

**9.1** Here's the "requirement" from a stakeholder:

```
A stakeholder says: "We need the URL shortener to have some kind of 
rate limiting. Users shouldn't be able to shorten too many URLs too fast."

Translate this into specific, testable requirements:
- What exactly should be limited? (requests per minute? per hour? per user?)
- What happens when the limit is exceeded?
- Where should the limit be enforced?
- How should it be configured?
```

**9.2** Copilot should ask clarifying questions. Answer them:

> This is intentionally vague. You'll need to make decisions.

**9.3** Create a concrete plan:

```
/plan Based on our discussion, implement rate limiting:
- Limit: max N URLs per minute (configurable via config.py)
- Scope: global (not per-user, since there's no auth)
- Enforcement: in store.shorten()
- Behavior: raise ValueError("Rate limit exceeded") when over limit
- Storage: track timestamps of recent shorten() calls in a list
```

**9.4** Implement and test:

> Follow the full cycle: implement → test → diff → review.

**9.5** Validate against the original requirement:

```
Does our implementation satisfy the stakeholder's requirement of 
"users shouldn't be able to shorten too many URLs too fast"?
What ambiguities remain?
```

### Key Concept: Requirements Refinement Workflow

```
1. RECEIVE vague requirement
2. ASK clarifying questions (with Copilot helping identify gaps)
3. DECIDE on specifics
4. PLAN concrete implementation
5. IMPLEMENT + TEST
6. VALIDATE against original requirement
```

> 💡 **Copilot is excellent at identifying ambiguities.** Ask it: "What questions would you ask the stakeholder about this requirement?"

### ✅ Checkpoint
You can refine vague requirements into tested implementations.

---

## Exercise 10: End-to-End — Issue → Plan → Code → Test → Review

### Goal
Execute the complete software development lifecycle in one exercise — from an issue description to a reviewed, tested implementation.

### Steps

**10.1** Here's the "Issue":

```
ISSUE #42: Add import/export functionality

As a user, I want to:
- Export all my shortened URLs to a JSON file (for backup)
- Import URLs from a JSON file (for restore)

Acceptance criteria:
- Export writes to a specified file path
- Import reads from a file path and adds URLs (skipping duplicates)
- Import should report how many URLs were added vs skipped
- Both operations should be available as CLI commands
```

**10.2** Plan from the issue:

```
/plan Implement Issue #42 — Import/Export functionality:

Phase 1: Core functions in store.py
- export_all(file_path) → writes JSON file
- import_from(file_path) → returns (added_count, skipped_count)

Phase 2: CLI commands in cli.py
- "export" subcommand with --output flag
- "import" subcommand with --input flag

Phase 3: Tests
- test_export_creates_valid_json
- test_import_adds_new_urls
- test_import_skips_duplicates
- test_import_returns_counts
- test_roundtrip_export_import
```

**10.3** Implement Phase 1 (core functions):

```
Implement export_all and import_from in store.py.
```

**10.4** Test Phase 1:

```
Write and run tests for export_all and import_from.
```

**10.5** Implement Phase 2 (CLI):

```
Add export and import subcommands to cli.py.
```

**10.6** Integration test Phase 2:

```
Test the full roundtrip via CLI:
!python -m shortener.cli shorten https://example.com --code exp001
!python -m shortener.cli shorten https://test.com --code exp002
!python -m shortener.cli export --output backup.json
!cat backup.json
!python -m shortener.cli import --input backup.json
```

**10.7** Full review:

```
/diff
```

```
/review This implements Issue #42. Does it meet all acceptance criteria?
- Export to JSON file ✓?
- Import with duplicate skipping ✓?
- Reports added vs skipped counts ✓?
- CLI commands for both ✓?
```

**10.8** Write the commit message:

```
Write a conventional commit message for this change 
that references Issue #42.
```

### Key Concept: The Complete SDLC

```
Issue → Plan → Implement → Test → Diff → Review → Commit Message
  │       │        │         │      │       │          │
  │       │        │         │      │       │          └─ Traceability
  │       │        │         │      │       └─ Quality gate
  │       │        │         │      └─ Verification
  │       │        │         └─ Correctness proof
  │       │        └─ The actual code
  │       └─ Thinking before doing
  └─ Where it all starts
```

### ✅ Checkpoint
You completed the full software development lifecycle in one exercise.

---

## Exercise 11: Recovery — When a Workflow Goes Wrong

### Goal
Learn to recover when a plan goes sideways — the essential production skill.

### Steps

**11.1** Start a deliberately flawed implementation:

```
Add a "purge" command that deletes ALL URLs at once. 
Implement it by deleting the urls.json file.
```

**11.2** Realize the mistake — test it:

```
Create some URLs, then run purge. Now check stats.
```

> The stats file is now inconsistent — it still shows total_created but the URLs are gone.

**11.3** Diagnose the problem:

```
/diff — What exactly changed?
```

```
What's wrong with the purge implementation? 
It deleted the file but didn't reset stats. 
What other side effects could file deletion cause?
```

**11.4** Decide: fix forward or revert?

```
Should we fix the purge implementation (fix forward) 
or revert everything and start over (revert)?
What are the trade-offs?
```

**11.5** Practice both approaches:

**Fix forward:**
```
Fix the purge command: instead of deleting the file, 
write an empty JSON object and reset the stats.
```

**Then revert:**
```
!git checkout -- .
```

**Start over with a better approach:**
```
/plan Implement a "purge" command properly:
1. Clear all entries from urls.json (write empty dict, don't delete file)
2. Reset stats counters
3. Print confirmation with count of deleted URLs
4. Add a --confirm flag (refuse to purge without it)
```

**11.6** Implement the better version.

### Key Concept: Recovery Strategies

| Situation | Best Strategy |
|-----------|--------------|
| Small mistake, easy to fix | **Fix forward** — patch the issue |
| Fundamental approach is wrong | **Revert and start over** — new plan |
| Multiple files corrupted | **Git checkout** — nuclear reset |
| Partially done, rest is good | **Selective revert** — `git checkout -- file` on broken files |

### ✅ Checkpoint
You can diagnose workflow failures and choose the right recovery strategy.

---

## Exercise 12: Workflow Retrospective

### Goal
Analyze your workflow across all exercises and identify areas for improvement.

### Steps

**12.1** Ask Copilot to summarize your session:

```
Look at all the changes in this session (/diff or !git diff).
How many files did we modify? How many functions did we add or change?
What was the overall scope of work?
```

**12.2** Analyze workflow patterns:

```
Across all exercises today, what was our most common workflow pattern?
Did we always follow plan → implement → test → review?
Where did we skip steps? Was that appropriate?
```

**12.3** Identify efficiency opportunities:

```
Where did we spend the most time? Were any steps redundant?
Could we have combined any exercises or done things in a different order?
```

**12.4** Rate your confidence on each workflow:

| Workflow | Confidence (1-5) |
|----------|:-:|
| Feature development | ? |
| Bug investigation & fix | ? |
| Test gap filling | ? |
| Refactoring | ? |
| Documentation update | ? |
| Code review | ? |
| Hotfix | ? |
| Requirements refinement | ? |

**12.5** Identify your top 3 improvement areas:

```
Based on the exercises, what are the 3 areas where I should improve?
What specific practice would help for each?
```

**12.6** Plan your Level 7 readiness:

```
Am I ready for Level 7 (Customize — MCP Servers & Context Optimization)?
What remaining gaps should I address first?
```

### ✅ Checkpoint
You've reflected on your workflow and identified specific improvement areas.

---

## 🏆 Level 6 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Build a feature using the full plan→implement→test→review cycle | ☐ | ☐ | ☐ |
| 2 | Debug multi-file bugs with systematic investigation | ☐ | ☐ | ☐ |
| 3 | Discover and fill test coverage gaps | ☐ | ☐ | ☐ |
| 4 | Execute safe refactoring with test verification | ☐ | ☐ | ☐ |
| 5 | Generate accurate documentation from code | ☐ | ☐ | ☐ |
| 6 | Perform multi-angle code reviews | ☐ | ☐ | ☐ |
| 7 | Execute minimal-change hotfixes | ☐ | ☐ | ☐ |
| 8 | Build features with interleaved testing | ☐ | ☐ | ☐ |
| 9 | Refine vague requirements into implementations | ☐ | ☐ | ☐ |
| 10 | Execute the complete SDLC: issue → plan → code → test → review | ☐ | ☐ | ☐ |
| 11 | Recover from failed workflows (fix forward vs revert) | ☐ | ☐ | ☐ |
| 12 | Analyze and improve your own workflow efficiency | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 7
- **22–29:** Repeat exercises 1, 2, and 10 with different features/bugs
- **Below 22:** Go back to Level 5 for more command execution practice

---

## Key Takeaways

1. **Every workflow starts with investigation** — understand before acting
2. **Plan before implement** — even for hotfixes, think for 10 seconds before coding
3. **Tests are your safety net** — for refactoring, for features, for bug fixes
4. **The diff is your truth** — always check what actually changed
5. **Review from multiple angles** — correctness, security, testing, maintainability
6. **Hotfixes demand discipline** — minimal change, immediate test, small diff
7. **Interleaved > sequential** — test as you build, not after
8. **Vague requirements need refinement** — ask questions before planning
9. **Recovery is a skill** — know when to fix forward vs revert
10. **Reflect on your workflow** — the meta-skill that improves all other skills

---

## What's Next

**Level 7: Customize — MCP Servers & Context Optimization** teaches you to extend Copilot with external tools (MCP servers), optimize context window usage, and configure Copilot for your specific workflow.

→ Continue to `workshop/level-7/README.md`
