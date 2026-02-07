---
applyTo: "workshop/level-{1,2,3,4,5,6}/sample-app/**/*.py"
---

# Python Sample App Instructions (Levels 1–6)

## Purpose

These are **educational sample applications** for Copilot CLI workshop exercises.
Code clarity and discoverability are prioritized over optimization. Learners
explore these apps using Copilot CLI to practice navigation, understanding,
planning, editing, and command execution.

## Style

- Python 3.8+ compatible (no walrus operator `:=` in core logic)
- **Standard library only** — zero external dependencies (no pip install required)
- Clear docstrings on all public functions and classes
- Type hints encouraged but not mandatory
- `snake_case` for functions and variables, `PascalCase` for classes
- Maximum line length: 100 characters (relaxed for readability)
- Prefer explicit over implicit — spell out logic for learners to follow

## Intentional Bugs — DO NOT FIX

Specific sample apps contain bugs planted for workshop exercises.
See `.github/copilot-instructions.md` for the complete catalog per level.

Rules when editing these files:
- **Preserve all existing intentional bugs** unless explicitly modifying one
- New code you add should work correctly (bugs are curated, not random)
- If adding a new intentional bug, document it in the level's README exercise list
- Comment intentional bugs with `# BUG:` only if the exercise instructs learners to
  find them via comments — otherwise leave them uncommented (discovery is the exercise)

## File Structure Conventions

```
sample-app/
  README.md          # What the app does, how to run it, known issues
  app.py / main.py   # Main entry point
  *.py               # Feature modules (flat structure for simple apps)
  models/            # Data models (for layered apps like Level 2)
  tests/             # Test files: test_*.py using unittest
  data/              # JSON files for persistence (no databases)
```

## Testing Conventions

- Use `unittest` module (no pytest dependency)
- Test files: `test_<module>.py` or `tests/test_<module>.py`
- Class-based tests: `class Test<Feature>(unittest.TestCase)`
- Intentional test failures should be realistic — the kind of bug a developer
  would actually encounter (not obvious syntax errors)

## Documentation in Sample Apps

- `README.md` at sample-app root: app description, usage, file listing
- Docstrings: one-line summary for simple functions, multi-line for complex ones
- Inline comments: only where the logic is non-obvious
- Do not add comments that give away intentional bugs
