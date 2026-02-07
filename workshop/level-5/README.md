# Level 5: Execute — Run Commands Through Copilot

> **Risk level:** 🟡 Medium — Copilot will run shell commands (tests, linters, scripts) on your behalf. Always read `bash` tool invocations before approving.

## Learning Objectives

By the end of this level, you will be able to:

1. Let Copilot discover available commands in a project (Makefile, scripts)
2. Run test suites through Copilot and interpret structured failure output
3. Use the **test → interpret → fix → re-run** feedback loop
4. Run linters through Copilot and fix violations systematically
5. Execute scripts (demo, benchmark) and discuss output with Copilot
6. Inspect the runtime environment through Copilot
7. Chain multiple commands in a single Copilot session
8. Handle command failures and error output
9. Use Test-Driven Development (TDD) with Copilot
10. Let Copilot autonomously loop through test → fix → re-run cycles
11. Understand `bash` tool safety and when to deny execution
12. Build the muscle memory for command-driven development

---

## Prerequisites

- [ ] Completed **Levels 1–4** (navigation, understanding, planning, first changes)
- [ ] Comfortable approving write operations and using `/diff`
- [ ] Python 3.8+ with `pytest` and `flake8` installed

### Environment Setup

```bash
cd workshop/level-5/sample-app
pip install -r requirements.txt
```

Verify:

```bash
python -m pytest --version
python -m flake8 --version
```

---

## About the Sample App

Level 5 uses a **Math Utilities Library** — a proper Python package with tests, linting, scripts, and a Makefile.

> Unlike Levels 3–4's note-taking CLI (focused on writing and planning), this app is designed for **command execution**: it has a `pytest` test suite with 6 intentional failures, `flake8` lint warnings, a `Makefile` with 10 targets, and benchmark scripts — everything you need to practice running commands through Copilot.

```
sample-app/
├── mathlib/
│   ├── __init__.py
│   ├── calculator.py      ← Arithmetic (bugs: divide-by-zero, negative exponent)
│   ├── statistics.py      ← Stats (bugs: median even-length, mode always first)
│   ├── converter.py       ← Unit conversions (clean — all tests pass)
│   └── validator.py       ← Validation (bugs: is_positive(0), is_integer(str))
├── tests/
│   ├── test_calculator.py ← 2 failing tests
│   ├── test_statistics.py ← 2 failing tests
│   ├── test_converter.py  ← All passing (19 tests)
│   └── test_validator.py  ← 2 failing tests
├── scripts/
│   ├── demo.py            ← Demo script
│   └── benchmark.py       ← Performance benchmark
├── Makefile               ← Command reference (make test, make lint, ...)
├── setup.cfg              ← Flake8 config
└── requirements.txt
```

### Intentional Failures

| # | File | Bug | Failing Test |
|---|------|-----|-------------|
| 1 | `calculator.py` | `divide(1, 0)` returns `None` instead of raising `ValueError` | `test_divide_by_zero_raises` |
| 2 | `calculator.py` | `power(2, -1)` returns `0` instead of `0.5` | `test_negative_exponent` |
| 3 | `statistics.py` | `median([1,2,3,4])` returns `3` instead of `2.5` | `test_even_length` |
| 4 | `statistics.py` | `mode([1,2,2,3])` returns `1` instead of `2` | `test_basic` |
| 5 | `validator.py` | `is_positive(0)` returns `True` instead of `False` | `test_zero_is_not_positive` |
| 6 | `validator.py` | `is_integer("hello")` crashes instead of returning `False` | `test_string_returns_false` |

### Lint Issues

- `calculator.py`: Unused imports (`math`, `os`), line too long (docstring)
- `calculator.py`: Missing docstring on `absolute()`

### Safety Net

```bash
git checkout -- workshop/level-5/sample-app/
```

---

## Workshop Structure

This level contains **12 exercises**. Estimated time: **75–100 minutes**.

| Exercise | Topic | Time |
|----------|-------|------|
| 1 | Command Discovery | 5 min |
| 2 | Running the Full Test Suite | 7 min |
| 3 | Interpreting Test Output | 7 min |
| 4 | The Test → Fix → Re-run Loop | 10 min |
| 5 | Running the Linter | 7 min |
| 6 | The Lint → Fix → Re-lint Loop | 7 min |
| 7 | Script Execution & Discussion | 7 min |
| 8 | Environment Inspection | 5 min |
| 9 | Chained Commands | 7 min |
| 10 | Handling Command Failures | 7 min |
| 11 | Test-Driven Development | 10 min |
| 12 | The Autonomous Fix Loop | 10 min |

---

## Exercise 1: Command Discovery

### Goal
Let Copilot discover what commands are available — before you run anything.

### Steps

**1.1** Navigate to the sample app and launch Copilot:

```bash
cd workshop/level-5/sample-app
copilot
```

**1.2** Ask Copilot to discover available commands:

```
What commands can I run in this project? Check the Makefile, requirements.txt, and any scripts.
```

**1.3** Observe how Copilot reads the Makefile:

> Copilot will use `view` or `cat` to read the Makefile, then summarize available targets. Watch which tools it uses — these are read-only and safe.

**1.4** Ask for a dependency check:

```
What dependencies does this project need? Are they installed?
```

**1.5** Ask Copilot to explain the project structure:

```
Describe the test structure. How many test files are there? What do they test?
```

### Key Concept: Discovery Before Execution

**Always ask Copilot to discover before executing.** This pattern:
1. Reads Makefile/package.json/scripts to find commands
2. Checks dependencies and environment
3. Gives you a map before you start running things

> 💡 Notice: steps 1.2–1.5 only used **read-only tools** (view, grep, ls). No bash execution yet.

### ✅ Checkpoint
You know what commands are available and what the test structure looks like.

---

## Exercise 2: Running the Full Test Suite

### Goal
Let Copilot run the test suite and present structured results.

### Steps

**2.1** Ask Copilot to run the tests:

```
Run the full test suite with make test
```

**2.2** Watch the approval prompt:

```
🔧 Tool: bash
   Command: cd /path/to/sample-app && make test
   [Allow] [Deny] [Allow for session]
```

> ⚠️ **This is a `bash` tool call.** Read the command carefully. `make test` runs `pytest` — safe. Choose **Allow**.

**2.3** Observe the output Copilot shows you:

> Copilot should display the full pytest output, then provide a summary: how many passed, how many failed, which ones failed.

**2.4** Ask Copilot for a structured summary:

```
Summarize the test results as a table: test name, status (pass/fail), and failure reason if applicable.
```

**2.5** Compare with raw output — run it yourself:

```
!make test
```

### Key Concept: Copilot as Command Interpreter

Copilot doesn't just run commands — it **interprets the output**:
- Parses test framework output (pytest, jest, etc.)
- Identifies patterns (which tests fail, common error types)
- Provides structured summaries
- Suggests next steps

This is more valuable than raw terminal output.

### ✅ Checkpoint
You can run the test suite through Copilot and get a structured interpretation of results.

---

## Exercise 3: Interpreting Test Output

### Goal
Go deeper into test failure interpretation — understand not just *which* tests fail, but *why*.

### Steps

**3.1** Ask for failure analysis:

```
For each failing test, explain:
1. What the test expects
2. What the code actually does
3. Why there's a mismatch
4. Which line in the source code is the root cause
```

**3.2** Focus on one specific failure:

```
Explain the test_divide_by_zero_raises failure in detail. 
Show me the test code and the relevant source code side by side.
```

**3.3** Ask Copilot to rank failures by severity:

```
Rank the 6 failing tests by severity:
- Which ones are bugs (wrong behavior)?
- Which ones are crashes (exceptions)?
- Which ones are security-relevant?
```

**3.4** Ask Copilot to identify patterns:

```
Are there any common patterns among the failing tests? 
Do multiple bugs share a similar root cause?
```

**3.5** Ask for a fix priority recommendation:

```
If I can only fix 3 of the 6 bugs today, which 3 should I prioritize and why?
```

### Key Concept: Structured Failure Analysis

| Analysis Type | Prompt Pattern |
|--------------|----------------|
| **What** failed | "Summarize the test results" |
| **Why** it failed | "Explain the mismatch between expected and actual" |
| **Where** the root cause is | "Show me the source line causing this failure" |
| **How severe** | "Rank failures by severity" |
| **What order** to fix | "Prioritize the fixes" |

### ✅ Checkpoint
You can do deep failure analysis — not just see red/green, but understand root causes and priorities.

---

## Exercise 4: The Test → Fix → Re-run Loop

### Goal
Fix bugs one at a time, re-running tests after each fix to verify progress.

### Steps

**4.1** Start with the simplest bug — `is_positive(0)` returns `True`:

```
Fix the is_positive bug in validator.py — zero should not be considered positive. 
Then re-run only the validator tests to verify.
```

**4.2** Watch the execution chain:

> Copilot should:
> 1. Edit `validator.py` (change `>=` to `>`)
> 2. Run `make test-file FILE=tests/test_validator.py`
> 3. Report the results

**4.3** Verify with `/diff`:

```
/diff
```

> Only `validator.py` should have changed. The change should be a single character: `>=` → `>`.

**4.4** Fix the next bug — `is_integer("hello")` crashes:

```
Fix the is_integer bug in validator.py — it crashes on string input. 
Add a type check before the comparison. Then re-run the validator tests.
```

**4.5** Check: are both validator bugs now fixed?

```
!make test-file FILE=tests/test_validator.py
```

> Expected: all validator tests pass now.

**4.6** Now fix the `divide` bug:

```
Fix the divide function in calculator.py — it should raise ValueError for division by zero, not return None.
Re-run the calculator tests to verify.
```

**4.7** Verify progress — how many failures remain?

```
Run the full test suite and tell me: how many tests fail now compared to the original 6?
```

> Expected: 3 failures remaining (median, mode, power).

### Key Concept: The Fix Loop

```
              ┌──────────────┐
              │  Run tests   │
              └──────┬───────┘
                     │
              ┌──────▼───────┐
         ┌────│ All passing? │────┐
         │    └──────────────┘    │
        YES                       NO
         │                        │
    ┌────▼────┐            ┌──────▼──────┐
    │  Done!  │            │ Pick 1 bug  │
    └─────────┘            └──────┬──────┘
                                  │
                           ┌──────▼──────┐
                           │  Fix the    │
                           │  source     │
                           └──────┬──────┘
                                  │
                           ┌──────▼──────┐
                           │  Re-run     │
                           │  tests      │──────→ (back to top)
                           └─────────────┘
```

> 💡 **Fix one bug at a time.** Re-run after each fix. This way, if a fix introduces a new failure, you know exactly which change caused it.

### ✅ Checkpoint
You can execute the test → fix → re-run loop and track progress across iterations.

---

## Exercise 5: Running the Linter

### Goal
Run the linter through Copilot and understand static analysis output.

### Steps

**5.1** Run the linter:

```
Run make lint and explain the output
```

**5.2** Watch the approval and observe the output:

> Copilot should show flake8 warnings with file, line number, and error code.

**5.3** Ask for categorization:

```
Categorize the lint warnings:
- Which are unused imports?
- Which are style issues (line length)?
- Which are missing docstrings?
```

**5.4** Ask about severity:

```
Which of these lint warnings could be actual bugs vs. just style issues?
```

**5.5** Compare linting vs testing:

```
If the linter catches issues that tests don't, and tests catch issues the linter doesn't,
what's the value of running both? Give me a concrete example from this codebase.
```

### Key Concept: Linter Output Structure

| flake8 Code | Category | Risk Level |
|-------------|----------|------------|
| F401 | Unused import | 🟢 Low — cleanup |
| E501 | Line too long | 🟢 Low — style |
| D103 | Missing docstring | 🟡 Medium — docs |
| E302 | Expected blank lines | 🟢 Low — style |

> 💡 Linters find **potential issues** that don't cause test failures. They catch maintenance problems before they become bugs.

### ✅ Checkpoint
You can run linters through Copilot, categorize warnings, and understand the value of static analysis.

---

## Exercise 6: The Lint → Fix → Re-lint Loop

### Goal
Fix lint violations one category at a time, re-running the linter after each batch.

### Steps

**6.1** Fix unused imports first:

```
Remove the unused imports in calculator.py (math and os). 
Then re-run the linter to see how many warnings remain.
```

**6.2** Verify the import removal didn't break anything:

```
Run make test-file FILE=tests/test_calculator.py to confirm tests still pass after removing imports.
```

> ⚠️ This is a crucial check: removing an import that looks unused but is actually needed (e.g., imported for side effects) would break tests.

**6.3** Fix the line-too-long issue:

```
Fix the E501 line-too-long warning in calculator.py by wrapping the long docstring.
Re-run the linter.
```

**6.4** Fix the missing docstring:

```
Add a docstring to the absolute() function in calculator.py.
Re-run the linter.
```

**6.5** Final lint check:

```
!make lint
```

> Expected: zero warnings from `mathlib/`.

**6.6** Run the full test suite to confirm nothing broke:

```
!make all
```

> `make all` runs both lint and test — confirming everything is clean after lint fixes.

### Key Concept: Lint Fix Strategy

| Strategy | When to Use |
|----------|-------------|
| Fix by category (all unused imports, then all line-length) | When there are many warnings of the same type |
| Fix by file (all warnings in one file) | When warnings are concentrated in one file |
| Fix most critical first | When some warnings indicate potential bugs |
| Always re-run tests after lint fixes | Removing "unused" imports can break code |

### ✅ Checkpoint
You can systematically fix lint violations while keeping tests green.

---

## Exercise 7: Script Execution & Discussion

### Goal
Run scripts through Copilot and use the output as a conversation topic.

### Steps

**7.1** Run the demo script:

```
Run the demo script: make demo
```

**7.2** Discuss the output:

```
The demo shows divide(15, 4) = 3.75. Is that correct? 
What about the median and mode values — are they correct given the data?
```

> 💡 Since we may have already fixed some bugs, the output should reflect those fixes. If not, discuss what's still wrong.

**7.3** Run the benchmark:

```
Run make benchmark and explain the results.
Which function is the fastest? Which is the slowest? Why?
```

**7.4** Ask for performance insights:

```
Why is factorial(20) so much slower than add(100, 200)?
What's the algorithmic complexity of each?
```

**7.5** Ask Copilot to suggest improvements:

```
Based on the benchmark results, which function would benefit most from optimization?
What optimization would you suggest?
```

**7.6** Run a modified benchmark:

```
Run the benchmark with only 1000 iterations: python scripts/benchmark.py 1000
Compare the timing with the default 10000 iterations.
```

### Key Concept: Script Output as Context

When Copilot runs a script, the output becomes **part of the conversation context**. This lets you:
- Ask follow-up questions about the output
- Compare runs with different parameters
- Use results to drive further development decisions

### ✅ Checkpoint
You can run scripts through Copilot and turn output into actionable discussion.

---

## Exercise 8: Environment Inspection

### Goal
Use Copilot to inspect and diagnose the runtime environment.

### Steps

**8.1** Ask Copilot to check the environment:

```
Check my Python environment:
- Python version
- pytest version
- flake8 version
- Where Python is installed
- What OS am I on?
```

**8.2** Ask about compatibility:

```
Is my Python version compatible with all the type hints used in this project?
```

**8.3** Check installed packages:

```
List all installed Python packages related to testing. 
Are there any additional testing tools I should install?
```

**8.4** Ask about project configuration:

```
Read setup.cfg and explain the flake8 configuration.
What's the max line length? What directories are excluded?
```

**8.5** Diagnose a hypothetical issue:

```
If pytest fails with "ModuleNotFoundError: No module named 'mathlib'", what would be the cause?
How would you fix it?
```

### Key Concept: Environment as Context

Copilot can diagnose environment issues by:
- Running `python --version`, `which python`, `pip list`
- Reading config files (`setup.cfg`, `pyproject.toml`, `Makefile`)
- Checking `$PATH`, working directory, virtual environments
- Comparing expected vs actual versions

> 💡 Many "my code doesn't work" problems are actually environment problems. Copilot can diagnose these faster than manual troubleshooting.

### ✅ Checkpoint
You can use Copilot for environment inspection and compatibility checking.

---

## Exercise 9: Chained Commands

### Goal
Let Copilot execute multiple commands in sequence to accomplish a multi-step task.

### Steps

**9.1** Ask for a clean build + test:

```
Clean the project, run the linter, then run all tests. 
Report the result of each step.
```

> Observe: Copilot should run `make clean`, `make lint`, then `make test` — either as separate commands or chained with `&&`.

**9.2** Ask for a targeted investigation:

```
Find all functions in mathlib/ that don't have docstrings,
then run the linter to confirm which ones flake8 catches.
```

**9.3** Ask for a comparison across test files:

```
Run each test file individually and show me a summary:
- test_calculator.py: X passed, Y failed
- test_statistics.py: X passed, Y failed
- test_converter.py: X passed, Y failed
- test_validator.py: X passed, Y failed
```

**9.4** Ask for a conditional chain:

```
Run the linter. If there are zero warnings, run the full test suite.
If there are warnings, list them and don't run tests yet.
```

**9.5** Observe the execution pattern:

```
How many separate bash commands did you run in this session so far?
Could any of them have been combined?
```

### Key Concept: Command Chaining Patterns

| Pattern | Example | When to Use |
|---------|---------|-------------|
| **Sequential** | `make clean && make test` | Steps depend on prior results |
| **Independent** | Run lint, then separately run tests | Steps are unrelated |
| **Conditional** | "If lint passes, run tests" | Second step depends on first's success |
| **Fan-out** | Run 4 test files individually | Need per-file results |

### ✅ Checkpoint
You can orchestrate multi-step command sequences through Copilot.

---

## Exercise 10: Handling Command Failures

### Goal
Learn how Copilot handles and recovers from command failures — exit codes, errors, crashes.

### Steps

**10.1** Intentionally introduce a syntax error:

```
Add a syntax error to calculator.py — put "def broken(" on its own line (no body).
Then run the tests.
```

**10.2** Observe Copilot's response to the import error:

> Copilot should:
> 1. Notice the test run failed (not just test failures, but an import error)
> 2. Identify it as a syntax error, not a logic bug
> 3. Point to the exact file and line

**10.3** Let Copilot fix it:

```
Fix the syntax error you just introduced and re-run the tests.
```

**10.4** Now test a runtime error — run a non-existent make target:

```
Run "make nonexistent" — what happens?
```

> Copilot should show the error and explain that the target doesn't exist.

**10.5** Test with an invalid Python command:

```
Run "python -c 'import nonexistent_module'"
```

**10.6** Ask Copilot to distinguish error types:

```
What's the difference between:
1. A test failure (assertion error)
2. A test error (exception during test)
3. A collection error (import/syntax error)
4. A command failure (non-zero exit code)
Give me an example of each from what we've seen.
```

### Key Concept: Error Taxonomy

| Error Type | Exit Code | Meaning | Copilot Response |
|------------|-----------|---------|-----------------|
| Test failure | 1 | Assertion didn't hold | Shows failing assertion + expected vs actual |
| Test error | 1 | Exception during test | Shows traceback + root cause |
| Collection error | 2 | Import/syntax error | Shows which file has the error |
| Command not found | 127 | Missing tool | Suggests installation |
| Permission denied | 126 | Can't execute | Suggests chmod or path fix |

### ✅ Checkpoint
You can distinguish error types and let Copilot diagnose and recover from each.

---

## Exercise 11: Test-Driven Development (TDD)

### Goal
Write a failing test first, then let Copilot implement the code to make it pass.

### Steps

**11.1** Start by reverting any changes:

```
!git checkout -- .
```

**11.2** Plan a new feature:

```
/plan Add a "clamp" function to calculator.py that constrains a value to a min/max range:
- clamp(5, 1, 10) → 5 (within range)
- clamp(-3, 0, 100) → 0 (below min, return min)
- clamp(150, 0, 100) → 100 (above max, return max)
```

**11.3** Write the test FIRST:

```
Create a test class TestClamp in tests/test_calculator.py with these test cases:
- test_within_range: clamp(5, 1, 10) == 5
- test_below_min: clamp(-3, 0, 100) == 0
- test_above_max: clamp(150, 0, 100) == 100
- test_at_min: clamp(0, 0, 100) == 0
- test_at_max: clamp(100, 0, 100) == 100
Don't implement the function yet — just the tests.
```

**11.4** Run the tests — they should fail:

```
Run make test-match K=clamp — the tests should fail because clamp doesn't exist yet.
```

**11.5** Now implement the function:

```
Implement the clamp function in calculator.py to make all the tests pass.
Then re-run the clamp tests.
```

**11.6** Verify:

```
Run make test-match K=clamp
```

> All clamp tests should pass now.

**11.7** Check no regressions:

```
Run the full test suite to make sure the new function didn't break anything else.
```

**11.8** Review the TDD cycle:

```
/diff
```

```
/review
```

### Key Concept: TDD with Copilot

```
1. Write tests first    ← You define the behavior
2. Run tests (RED)      ← Confirm tests fail
3. Implement code       ← Copilot writes the implementation
4. Run tests (GREEN)    ← Confirm tests pass
5. /diff + /review      ← Verify quality
```

> 💡 **TDD with Copilot is powerful** because:
> - You define the contract (tests)
> - Copilot provides the implementation
> - Tests verify correctness automatically
> - No ambiguity about what "done" looks like

### ✅ Checkpoint
You can use TDD with Copilot: write failing tests, let Copilot implement, verify green.

---

## Exercise 12: The Autonomous Fix Loop

### Goal
Let Copilot autonomously fix all remaining bugs in a single session — the ultimate command execution exercise.

### Steps

**12.1** Reset to a clean state:

```
!git checkout -- .
```

**12.2** Give Copilot the autonomous directive:

```
Run the full test suite. For each failing test:
1. Identify the root cause in the source code
2. Fix the bug
3. Re-run the tests
4. Repeat until all tests pass

After each fix, show me the /diff so I can track progress.
```

**12.3** Watch the execution chain:

> Copilot should enter a loop:
> 1. `make test` → 6 failures
> 2. Fix bug #1 → `make test` → 5 failures
> 3. Fix bug #2 → `make test` → 4 failures
> 4. ... continue until 0 failures

**12.4** Approve each step carefully:

> You'll see multiple approval prompts for `edit` and `bash` tools. For each:
> - **Edit approvals:** Read the file name and verify it's the right file for the bug being fixed
> - **Bash approvals:** Verify the command is `make test` or similar test commands

**12.5** Track progress — after each loop iteration, note:

| Iteration | Failures Before | Bug Fixed | Failures After |
|-----------|----------------|-----------|----------------|
| 1 | 6 | ? | 5 |
| 2 | 5 | ? | 4 |
| ... | ... | ... | ... |
| 6 | 1 | ? | 0 |

**12.6** Final verification:

```
!make all
```

> Both lint and tests should be clean.

**12.7** Review all changes:

```
/diff
```

```
/review Are all 6 bug fixes correct? Any fix that might have unintended side effects?
```

**12.8** Reflect on the experience:

```
How many total bash commands did you run in this exercise? 
How many edit operations? 
What was the total time for the autonomous loop?
```

### Key Concept: Autonomous Execution

The autonomous fix loop demonstrates Copilot's **agentic behavior**:

```
┌─────────────────────────────────────────┐
│            Autonomous Loop              │
│                                         │
│  Run tests ──→ Parse output             │
│       ↑              │                  │
│       │        Identify failure         │
│       │              │                  │
│       │        Read source code         │
│       │              │                  │
│       │        Fix the bug              │
│       │              │                  │
│       └──────────────┘                  │
│                                         │
│  Each step requires YOUR APPROVAL       │
│  You remain in control at every step    │
└─────────────────────────────────────────┘
```

> 💡 **You are always in the loop.** Copilot proposes each action, you approve it. The "autonomous" part is that Copilot decides *what* to do next — you decide *whether* to let it.

### ✅ Checkpoint
You've experienced Copilot's autonomous fix loop — the most powerful command execution pattern.

---

## 🏆 Level 5 Self-Assessment

Rate yourself on each skill (1 = shaky, 3 = confident):

| # | Skill | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Discover available commands before running | ☐ | ☐ | ☐ |
| 2 | Run tests through Copilot and interpret results | ☐ | ☐ | ☐ |
| 3 | Analyze test failures (what/why/where/severity) | ☐ | ☐ | ☐ |
| 4 | Execute the test → fix → re-run loop | ☐ | ☐ | ☐ |
| 5 | Run linters and categorize warnings | ☐ | ☐ | ☐ |
| 6 | Fix lint violations without breaking tests | ☐ | ☐ | ☐ |
| 7 | Run scripts and discuss output with Copilot | ☐ | ☐ | ☐ |
| 8 | Inspect environment through Copilot | ☐ | ☐ | ☐ |
| 9 | Chain multiple commands in sequence | ☐ | ☐ | ☐ |
| 10 | Distinguish and handle error types | ☐ | ☐ | ☐ |
| 11 | Use TDD with Copilot (test-first) | ☐ | ☐ | ☐ |
| 12 | Guide Copilot through an autonomous fix loop | ☐ | ☐ | ☐ |

**Scoring:**
- **30–36:** Ready for Level 6
- **22–29:** Repeat exercises 4, 11, and 12 with different bugs
- **Below 22:** Go back to Level 4 for more write practice, then retry

---

## Key Takeaways

1. **Discover before executing** — read Makefiles and configs before running commands
2. **The `bash` tool is the most powerful and most dangerous** — always read the command
3. **Copilot interprets output, not just shows it** — ask for structured summaries
4. **Fix one bug at a time** — re-run tests after each fix to catch regressions
5. **Lint fixes can break code** — always re-run tests after removing "unused" imports
6. **TDD with Copilot is a superpower** — you define behavior, Copilot implements
7. **The autonomous loop works** — but you approve every step
8. **Different errors need different responses** — test failure ≠ syntax error ≠ import error
9. **Script output is conversation context** — use it to drive further decisions
10. **Chain commands for efficiency** — `make clean && make lint && make test`

---

## What's Next

**Level 6: Workflow — The Full Plan → Execute → Review Cycle** combines everything from Levels 1–5 into complete development workflows: building features from scratch, debugging production-like issues, and using Copilot as a true development partner.

→ Continue to `workshop/level-6/README.md`
