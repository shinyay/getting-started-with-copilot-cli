# Quick Notes — Sample Application

A CLI note-taking app for workshop exploration.
This app has **intentional issues** — bugs, missing features, TODOs, and
refactoring opportunities — specifically designed for planning exercises.

## Files

| File | Purpose |
|------|---------|
| `notes.py` | CLI entry point and command handling |
| `storage.py` | File-based note persistence (JSON) |
| `models.py` | Note data model and validation |
| `search.py` | Full-text search across notes |
| `export.py` | Export notes to Markdown and HTML |
| `config.py` | Configuration constants |

## Usage

```bash
python notes.py add "Meeting notes" --tags meeting,work
python notes.py list
python notes.py show 1
python notes.py search "meeting"
python notes.py edit 1 --title "Updated title"
python notes.py delete 1
python notes.py export --format markdown --output notes.md
python notes.py stats
```

## Known Issues (for workshop use)

This application has intentional issues for planning practice:
- 🐛 Bugs that need fixing
- 📝 TODO comments marking incomplete features
- 🏗️ Code that should be refactored
- 🧪 Missing test coverage
- 📖 Missing documentation

Participants should **plan** fixes using `/plan`, not implement them directly.
