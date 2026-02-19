# Level 5 Cheat Sheet — Command Execution

## Bash Tool Approval

| Command Pattern | Risk | Action |
|----------------|------|--------|
| `make test`, `pytest`, `npm test` | 🟢 Safe | Allow |
| `make lint`, `flake8`, `eslint` | 🟢 Safe | Allow |
| `python script.py`, `node script.js` | 🟡 Read first | Verify what script does |
| `cat`, `ls`, `grep`, `find`, `wc` | 🟢 Safe | Allow for session |
| `pip install`, `npm install` | 🟡 Modifies env | Allow if expected |
| `rm`, `mv`, `chmod` | 🔴 Destructive | Read carefully |
| Anything with `sudo` | 🔴 Elevated | Almost always deny |

## Make Targets (This Project)

```bash
make test            # Run all tests (verbose)
make test-short      # Run tests (short output)
make test-file FILE=tests/test_calculator.py   # One file
make test-match K=divide    # Tests matching keyword
make lint            # Lint mathlib/
make lint-all        # Lint everything
make demo            # Run demo script
make benchmark       # Run benchmark
make all             # lint + test
make clean           # Remove __pycache__, .pyc, .pytest_cache
```

## Prompt Patterns for Command Execution

```
# Discovery
What commands can I run? Check the Makefile.

# Run + interpret
Run make test and summarize the results as a table.

# Targeted run
Run only the calculator tests: make test-file FILE=tests/test_calculator.py

# Fix loop
Fix the divide bug in calculator.py, then re-run the calculator tests.

# Lint + fix
Run the linter. Fix all warnings. Re-run to confirm zero warnings.

# TDD
Write tests for a clamp() function first. Run them (should fail). 
Then implement clamp() and re-run (should pass).

# Autonomous
Run tests. For each failure, fix the bug and re-run. Repeat until all pass.
```

## The Test → Fix → Re-run Loop

```
1. make test          → see failures
2. pick one failure   → read test + source
3. fix the source     → edit one file
4. make test          → verify fewer failures
5. repeat until green
```

## The Lint → Fix → Re-lint Loop

```
1. make lint          → see warnings
2. fix one category   → e.g., all unused imports
3. make test          → confirm no breakage!
4. make lint          → verify fewer warnings
5. repeat until clean
```

## Error Types

| Type | pytest Exit | What It Means |
|------|-------------|---------------|
| PASSED | 0 | All tests pass |
| FAILED | 1 | Assertion error (test logic) |
| ERROR | 1 | Exception during test setup/run |
| COLLECTION ERROR | 2 | Import or syntax error |
| NO TESTS | 5 | No tests found |

## TDD Cycle

```
1. Write test (RED)     → define expected behavior
2. Run test             → confirm it fails
3. Implement code       → let Copilot write it
4. Run test (GREEN)     → confirm it passes
5. /diff + /review      → verify quality
6. Run full suite       → check no regressions
```

## Bug Targets in Sample App

| # | File | Bug | Fix |
|---|------|-----|-----|
| 1 | `calculator.py` | `divide(1,0)` → None | `raise ValueError` |
| 2 | `calculator.py` | `power(2,-1)` → 0 | `return a ** n` |
| 3 | `statistics.py` | `median([1,2,3,4])` → 3 | Average middle two |
| 4 | `statistics.py` | `mode([1,2,2,3])` → 1 | Count frequencies |
| 5 | `validator.py` | `is_positive(0)` → True | `>` not `>=` |
| 6 | `validator.py` | `is_integer("hello")` → crash | Add `is_number()` check |

## Lint Targets

| File | Issue | flake8 Code |
|------|-------|-------------|
| `calculator.py` | `import math` unused | F401 |
| `calculator.py` | `import os` unused | F401 |
| `calculator.py` | Long docstring line | E501 |
| `calculator.py` | `absolute()` no docstring | D103 |

## Tips

- **Always `make test` after lint fixes** — "unused" imports may actually be needed
- **Fix one bug per loop iteration** — easier to track and revert
- **Use `make test-match K=keyword`** for fast iteration on specific bugs
- **Read `bash` commands before approving** — the tool name alone isn't enough
- **TDD = your tests, Copilot's code** — you define behavior, Copilot implements
