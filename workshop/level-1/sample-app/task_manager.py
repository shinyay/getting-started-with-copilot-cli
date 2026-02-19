"""Core business logic for task CRUD operations."""

import json
from pathlib import Path
from typing import Optional

from config import TASKS_FILE, MAX_TASKS, PRIORITY_MAP
from models import Task, TaskEncoder


class TaskManager:
    """Manages task persistence and CRUD operations."""

    def __init__(self, filepath: Path = TASKS_FILE):
        self._filepath = filepath
        self._tasks: list[Task] = []
        self._next_id: int = 1
        self._load()

    def _load(self):
        """Load tasks from the JSON file."""
        if not self._filepath.exists():
            self._tasks = []
            self._next_id = 1
            return

        try:
            with open(self._filepath, "r") as f:
                data = json.load(f)

            self._tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
            self._next_id = data.get("next_id", 1)

            # Reconcile next_id with actual max
            if self._tasks:
                max_id = max(t.id for t in self._tasks)
                if self._next_id <= max_id:
                    self._next_id = max_id + 1
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not parse {self._filepath}: {e}")
            self._tasks = []
            self._next_id = 1

    def _save(self):
        """Persist tasks to the JSON file."""
        data = {
            "version": 1,
            "next_id": self._next_id,
            "tasks": [t.to_dict() for t in self._tasks],
        }
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(self._filepath, "w") as f:
            json.dump(data, f, indent=2, cls=TaskEncoder)

    def add(self, title: str, priority: str = "medium",
            due_date: Optional[str] = None, tags: Optional[list[str]] = None) -> Task:
        """Create and persist a new task."""
        if len(self._tasks) >= MAX_TASKS:
            raise RuntimeError(f"Task limit reached ({MAX_TASKS})")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            priority=priority,
            due_date=due_date,
            tags=tags or [],
        )
        self._tasks.append(task)
        self._next_id += 1
        self._save()
        return task

    def get(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self, status: Optional[str] = None,
                   priority: Optional[str] = None,
                   sort_by: str = "priority") -> list[Task]:
        """List tasks with optional filtering and sorting."""
        result = self._tasks[:]

        if status:
            result = [t for t in result if t.status == status]
        if priority:
            result = [t for t in result if t.priority == priority]

        if sort_by == "priority":
            result.sort(key=lambda t: (t.priority_rank, t.id))
        elif sort_by == "due_date":
            result.sort(key=lambda t: (t.due_date or "9999-12-31", t.id))
        elif sort_by == "created":
            result.sort(key=lambda t: t.created_at)
        elif sort_by == "id":
            result.sort(key=lambda t: t.id)

        return result

    def complete(self, task_id: int) -> Task:
        """Mark a task as done."""
        task = self.get(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} not found")
        if task.status == "done":
            raise ValueError(f"Task #{task_id} is already completed")
        task.complete()
        self._save()
        return task

    def delete(self, task_id: int) -> Task:
        """Remove a task permanently."""
        task = self.get(task_id)
        if not task:
            raise ValueError(f"Task #{task_id} not found")
        self._tasks = [t for t in self._tasks if t.id != task_id]
        self._save()
        return task

    def stats(self) -> dict:
        """Return summary statistics."""
        total = len(self._tasks)
        by_status = {}
        by_priority = {}
        overdue = 0

        for t in self._tasks:
            by_status[t.status] = by_status.get(t.status, 0) + 1
            by_priority[t.priority] = by_priority.get(t.priority, 0) + 1
            if t.is_overdue:
                overdue += 1

        return {
            "total": total,
            "by_status": by_status,
            "by_priority": by_priority,
            "overdue": overdue,
        }
