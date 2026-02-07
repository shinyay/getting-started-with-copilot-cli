"""Data models and validation for tasks."""

from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from typing import Optional
import json

from config import PRIORITY_MAP, VALID_STATUSES, DATE_FORMAT, DATETIME_FORMAT


@dataclass
class Task:
    id: int
    title: str
    status: str = "pending"
    priority: str = "medium"
    due_date: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().strftime(DATETIME_FORMAT))
    completed_at: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Validate fields after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if len(self.title) > 200:
            raise ValueError(f"Task title too long ({len(self.title)} chars, max 200)")
        if self.status not in VALID_STATUSES:
            raise ValueError(f"Invalid status: {self.status}")
        if self.priority not in PRIORITY_MAP:
            raise ValueError(f"Invalid priority: {self.priority}")
        if self.due_date:
            self._validate_due_date()

    def _validate_due_date(self):
        """Validate and normalize the due date format."""
        try:
            parsed = datetime.strptime(self.due_date, DATE_FORMAT)
            self.due_date = parsed.strftime(DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format: {self.due_date} (expected {DATE_FORMAT})")

    @property
    def is_overdue(self) -> bool:
        """Check if the task is past its due date."""
        if not self.due_date or self.status == "done":
            return False
        due = datetime.strptime(self.due_date, DATE_FORMAT).date()
        return date.today() > due

    @property
    def priority_rank(self) -> int:
        """Numeric priority for sorting (lower = more urgent)."""
        return PRIORITY_MAP.get(self.priority, 99)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task from a dictionary."""
        # Handle legacy data that may not have all fields
        known_fields = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in known_fields}
        return cls(**filtered)

    def complete(self):
        """Mark this task as done."""
        self.status = "done"
        self.completed_at = datetime.now().strftime(DATETIME_FORMAT)

    def __str__(self):
        status_icon = {"pending": "○", "in_progress": "◑", "done": "●"}
        icon = status_icon.get(self.status, "?")
        overdue = " ⚠️ OVERDUE" if self.is_overdue else ""
        due = f" (due: {self.due_date})" if self.due_date else ""
        return f"[{icon}] #{self.id} [{self.priority}] {self.title}{due}{overdue}"


class TaskEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles Task objects."""
    def default(self, obj):
        if isinstance(obj, Task):
            return obj.to_dict()
        return super().default(obj)
