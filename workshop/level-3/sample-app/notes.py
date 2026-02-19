#!/usr/bin/env python3
"""Quick Notes CLI — entry point and command handling."""

import argparse
import sys

from models import Note
from storage import NoteStorage
from search import search_notes
from export import export_notes
from config import EXPORT_FORMATS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="quicknotes",
        description="A simple CLI note-taking app.",
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # add
    p_add = sub.add_parser("add", help="Add a new note")
    p_add.add_argument("title", help="Note title")
    p_add.add_argument("--body", "-b", default="", help="Note body")
    p_add.add_argument("--tags", "-t", default="", help="Comma-separated tags")
    p_add.add_argument("--pin", action="store_true", help="Pin this note")

    # list
    p_list = sub.add_parser("list", help="List all notes")
    p_list.add_argument("--tag", help="Filter by tag")
    p_list.add_argument("--pinned", action="store_true", help="Show only pinned notes")

    # show
    p_show = sub.add_parser("show", help="Show a note in full")
    p_show.add_argument("id", type=int, help="Note ID")

    # edit
    p_edit = sub.add_parser("edit", help="Edit a note")
    p_edit.add_argument("id", type=int, help="Note ID")
    p_edit.add_argument("--title", help="New title")
    p_edit.add_argument("--body", "-b", help="New body")
    p_edit.add_argument("--tags", "-t", help="New comma-separated tags (replaces all)")
    p_edit.add_argument("--pin", action="store_true", help="Pin this note")
    p_edit.add_argument("--unpin", action="store_true", help="Unpin this note")

    # delete
    p_del = sub.add_parser("delete", help="Delete a note")
    p_del.add_argument("id", type=int, help="Note ID")

    # search
    p_search = sub.add_parser("search", help="Search notes")
    p_search.add_argument("query", help="Search query")

    # export
    p_export = sub.add_parser("export", help="Export notes")
    p_export.add_argument("--format", "-f", choices=EXPORT_FORMATS, default="markdown")
    p_export.add_argument("--output", "-o", help="Output file (default: stdout)")

    # stats
    sub.add_parser("stats", help="Show statistics")

    # TODO: Add "import" command to restore from exported files
    # TODO: Add "archive" command to move notes to an archive
    # TODO: Add "merge" command to combine two notes

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    storage = NoteStorage()

    try:
        if args.command == "add":
            tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []
            note = Note(id=0, title=args.title, body=args.body, tags=tags, is_pinned=args.pin)
            saved = storage.add(note)
            print(f"✅ Created: {saved}")

        elif args.command == "list":
            notes = storage.list_all()

            if args.tag:
                notes = [n for n in notes if args.tag in n.tags]
            if args.pinned:
                notes = [n for n in notes if n.is_pinned]

            # BUG: No sorting — pinned notes should appear first
            if not notes:
                print("No notes found.")
            else:
                for note in notes:
                    print(f"  {note}  —  {note.preview}")

        elif args.command == "show":
            note = storage.get(args.id)
            if not note:
                print(f"❌ Note #{args.id} not found.", file=sys.stderr)
                sys.exit(1)
            print(f"{'📌 ' if note.is_pinned else ''}#{note.id} {note.title}")
            print(f"Tags: {', '.join(note.tags) if note.tags else '(none)'}")
            print(f"Created: {note.created_at}")
            if note.updated_at:
                print(f"Updated: {note.updated_at}")
            print(f"Words: {note.word_count}")
            print("---")
            print(note.body or "(empty)")

        elif args.command == "edit":
            note = storage.get(args.id)
            if not note:
                print(f"❌ Note #{args.id} not found.", file=sys.stderr)
                sys.exit(1)
            if args.title is not None:
                note.title = args.title
            if args.body is not None:
                note.body = args.body
            if args.tags is not None:
                note.tags = [t.strip() for t in args.tags.split(",") if t.strip()]
            if args.pin:
                note.is_pinned = True
            if args.unpin:
                note.is_pinned = False
            # BUG: Validation is not re-run after editing fields
            # A user could set title="" via --title "" and bypass the check
            storage.update(note)
            print(f"✅ Updated: {note}")

        elif args.command == "delete":
            note = storage.delete(args.id)
            print(f"🗑️  Deleted: {note}")

        elif args.command == "search":
            notes = storage.list_all()
            results = search_notes(notes, args.query)
            if not results:
                print(f"No notes matching '{args.query}'.")
            else:
                print(f"Found {len(results)} note(s):")
                for note in results:
                    print(f"  {note}  —  {note.preview}")

        elif args.command == "export":
            notes = storage.list_all()
            output = export_notes(notes, fmt=args.format)
            if args.output:
                with open(args.output, "w") as f:
                    f.write(output)
                print(f"✅ Exported {len(notes)} notes to {args.output}")
            else:
                print(output)

        elif args.command == "stats":
            s = storage.stats()
            print(f"Total notes:  {s['total']}")
            print(f"Pinned:       {s['pinned']}")
            print(f"Total words:  {s['total_words']}")
            print(f"Unique tags:  {s['unique_tags']}")
            if s["tags"]:
                print("Top tags:")
                for tag, count in list(s["tags"].items())[:10]:
                    print(f"  {tag}: {count}")

    except (ValueError, RuntimeError) as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
