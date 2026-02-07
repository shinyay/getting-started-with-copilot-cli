#!/usr/bin/env python3
"""Task Tracker CLI — entry point and argument parsing."""

import argparse
import sys

from task_manager import TaskManager
from formatter import format_tasks
from config import PRIORITY_MAP, VALID_STATUSES, SUPPORTED_FORMATS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="A simple CLI task tracker for managing daily work.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # ── add ──────────────────────────────────────────────────────
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument(
        "--priority", "-p",
        choices=list(PRIORITY_MAP.keys()),
        default="medium",
        help="Priority level (default: medium)",
    )
    add_parser.add_argument("--due", "-d", help="Due date (YYYY-MM-DD)")
    add_parser.add_argument(
        "--tags", "-t", nargs="*", default=[], help="Tags for categorization"
    )

    # ── list ─────────────────────────────────────────────────────
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status", "-s", choices=VALID_STATUSES, help="Filter by status"
    )
    list_parser.add_argument(
        "--priority", "-p", choices=list(PRIORITY_MAP.keys()), help="Filter by priority"
    )
    list_parser.add_argument(
        "--sort", choices=["priority", "due_date", "created", "id"],
        default="priority", help="Sort order (default: priority)"
    )
    list_parser.add_argument(
        "--format", "-f", choices=SUPPORTED_FORMATS,
        default="table", help="Output format (default: table)"
    )
    list_parser.add_argument(
        "--no-color", action="store_true", help="Disable colored output"
    )

    # ── complete ─────────────────────────────────────────────────
    complete_parser = subparsers.add_parser("complete", help="Mark a task as done")
    complete_parser.add_argument("id", type=int, help="Task ID to complete")

    # ── delete ───────────────────────────────────────────────────
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # ── stats ────────────────────────────────────────────────────
    subparsers.add_parser("stats", help="Show task statistics")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    manager = TaskManager()

    try:
        if args.command == "add":
            task = manager.add(
                title=args.title,
                priority=args.priority,
                due_date=args.due,
                tags=args.tags,
            )
            print(f"✅ Created: {task}")

        elif args.command == "list":
            tasks = manager.list_tasks(
                status=args.status,
                priority=args.priority,
                sort_by=args.sort,
            )
            output = format_tasks(tasks, fmt=args.format, color=not args.no_color)
            print(output)

        elif args.command == "complete":
            task = manager.complete(args.id)
            print(f"✅ Completed: {task}")

        elif args.command == "delete":
            task = manager.delete(args.id)
            print(f"🗑️  Deleted: {task}")

        elif args.command == "stats":
            s = manager.stats()
            print(f"Total tasks: {s['total']}")
            print(f"Overdue:     {s['overdue']}")
            print(f"By status:   {s['by_status']}")
            print(f"By priority: {s['by_priority']}")

    except (ValueError, RuntimeError) as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
