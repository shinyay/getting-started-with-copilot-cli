"""Configuration and constants for the task tracker."""

import os
from pathlib import Path

# Storage
DATA_DIR = Path(os.environ.get("TASK_DATA_DIR", "."))
TASKS_FILE = DATA_DIR / "tasks.json"
MAX_TASKS = 1000

# Priority levels (lower number = higher priority)
PRIORITY_MAP = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

# Status values
STATUS_PENDING = "pending"
STATUS_IN_PROGRESS = "in_progress"
STATUS_DONE = "done"
VALID_STATUSES = [STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_DONE]

# Display
DEFAULT_FORMAT = "table"
SUPPORTED_FORMATS = ["table", "json", "csv"]
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Colors (ANSI)
COLORS = {
    "critical": "\033[91m",  # Red
    "high": "\033[93m",      # Yellow
    "medium": "\033[96m",    # Cyan
    "low": "\033[92m",       # Green
    "done": "\033[90m",      # Gray
    "reset": "\033[0m",
}
