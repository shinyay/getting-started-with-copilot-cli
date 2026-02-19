"""Output formatters for task display."""

from typing import Optional
from config import COLORS


def format_table(tasks: list, show_color: bool = True) -> str:
    """Format tasks as an aligned text table."""
    if not tasks:
        return "No tasks found."

    headers = ["ID", "Status", "Priority", "Title", "Due Date", "Tags"]
    rows = []

    for t in tasks:
        status_icon = {"pending": "○", "in_progress": "◑", "done": "●"}.get(t.status, "?")
        overdue_mark = " ⚠️" if t.is_overdue else ""
        tags_str = ", ".join(t.tags) if t.tags else ""

        row = [
            f"#{t.id}",
            f"{status_icon} {t.status}",
            t.priority,
            t.title[:50] + ("…" if len(t.title) > 50 else ""),
            (t.due_date or "-") + overdue_mark,
            tags_str,
        ]

        if show_color:
            color = COLORS.get("done" if t.status == "done" else t.priority, "")
            reset = COLORS["reset"]
            row = [f"{color}{cell}{reset}" for cell in row]

        rows.append(row)

    # Calculate column widths (strip ANSI for width calculation)
    import re
    ansi_re = re.compile(r"\033\[[0-9;]*m")

    def visible_len(s):
        return len(ansi_re.sub("", s))

    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], visible_len(cell))

    def pad(s, width):
        return s + " " * (width - visible_len(s))

    # Build output
    lines = []
    header_line = " | ".join(pad(h, widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append("-+-".join("-" * w for w in widths))

    for row in rows:
        lines.append(" | ".join(pad(cell, widths[i]) for i, cell in enumerate(row)))

    return "\n".join(lines)


def format_json(tasks: list) -> str:
    """Format tasks as JSON."""
    import json
    return json.dumps([t.to_dict() for t in tasks], indent=2)


def format_csv(tasks: list) -> str:
    """Format tasks as CSV."""
    import csv
    import io

    output = io.StringIO()
    if not tasks:
        return ""

    fieldnames = ["id", "status", "priority", "title", "due_date", "created_at", "completed_at", "tags"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    for t in tasks:
        d = t.to_dict()
        d["tags"] = ";".join(d.get("tags", []))
        writer.writerow({k: d.get(k, "") for k in fieldnames})

    return output.getvalue()


def format_tasks(tasks: list, fmt: str = "table", color: bool = True) -> str:
    """Route to the appropriate formatter."""
    formatters = {
        "table": lambda: format_table(tasks, show_color=color),
        "json": lambda: format_json(tasks),
        "csv": lambda: format_csv(tasks),
    }

    formatter = formatters.get(fmt)
    if not formatter:
        raise ValueError(f"Unknown format: {fmt}. Supported: {list(formatters.keys())}")

    return formatter()
