# Math Utilities Library — Level 5 Sample App

A small math library used to practice **running commands through Copilot CLI**.

## Structure

```
mathlib/
├── calculator.py    ← Arithmetic operations (2 bugs → 2 failing tests)
├── statistics.py    ← Statistical functions (2 bugs → 2 failing tests)
├── converter.py     ← Unit conversions (clean — all tests pass)
└── validator.py     ← Input validation (2 bugs → 2 failing tests)

tests/
├── test_calculator.py
├── test_statistics.py
├── test_converter.py
└── test_validator.py

scripts/
├── demo.py          ← Demonstration script
└── benchmark.py     ← Performance benchmark
```

## Quick Commands

```bash
# Run all tests
make test

# Run linter
make lint

# Run a specific test file
make test-file FILE=tests/test_calculator.py

# Run demo
make demo

# Run everything (lint + test)
make all
```

## Known Issues (for workshop exercises)

There are **6 intentional test failures** and **several lint warnings** planted for
Level 5 exercises. Participants will use Copilot CLI to discover, interpret, and fix them.

### Reset

```bash
git checkout -- workshop/level-5/sample-app/
```
