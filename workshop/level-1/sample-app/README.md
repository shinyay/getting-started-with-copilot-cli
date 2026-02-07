# Task Tracker — Sample Application

A minimal CLI task tracker for workshop exploration.
This app is intentionally simple but has enough structure for Copilot CLI to analyze.

## What it does

- Add, list, complete, and delete tasks
- Tasks are stored in a local JSON file (`tasks.json`)
- Supports priority levels and due dates

## Files

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point and argument parsing |
| `task_manager.py` | Core business logic (CRUD operations) |
| `models.py` | Data models and validation |
| `formatter.py` | Output formatting (table, JSON, CSV) |
| `config.py` | Configuration and constants |
| `requirements.txt` | Dependencies |

## Usage

```bash
python main.py add "Buy groceries" --priority high --due 2026-02-14
python main.py list
python main.py list --status pending --format table
python main.py complete 1
python main.py delete 1
```
