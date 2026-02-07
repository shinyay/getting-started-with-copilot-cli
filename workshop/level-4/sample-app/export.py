"""Export notes to Markdown and HTML formats."""

from models import Note
from config import EXPORT_FORMATS


def export_notes(notes: list[Note], fmt: str = "markdown") -> str:
    """Export a list of notes to the specified format.

    TODO: Add support for filtering (e.g., export only notes with tag "work")
    TODO: Add support for custom templates
    """
    if fmt not in EXPORT_FORMATS:
        raise ValueError(f"Unsupported format: {fmt}. Use one of: {EXPORT_FORMATS}")

    if fmt == "markdown":
        return _to_markdown(notes)
    elif fmt == "html":
        return _to_html(notes)
    return ""


def _to_markdown(notes: list[Note]) -> str:
    """Convert notes to Markdown format."""
    lines = ["# Quick Notes Export", ""]

    for note in notes:
        lines.append(f"## {note.title}")
        lines.append("")
        if note.tags:
            lines.append(f"**Tags:** {', '.join(note.tags)}")
            lines.append("")
        if note.body:
            lines.append(note.body)
            lines.append("")
        lines.append(f"*Created: {note.created_at}*")
        if note.updated_at:
            lines.append(f"*Updated: {note.updated_at}*")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def _to_html(notes: list[Note]) -> str:
    """Convert notes to HTML format.

    BUG: No HTML escaping — if a note title contains <script>, it will be
    rendered as HTML, creating an XSS vulnerability in the exported file.
    """
    parts = [
        "<!DOCTYPE html>",
        "<html><head><title>Quick Notes Export</title>",
        "<style>",
        "  body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }",
        "  .note { border-bottom: 1px solid #eee; padding: 16px 0; }",
        "  .tags { color: #666; font-size: 0.9em; }",
        "  .meta { color: #999; font-size: 0.8em; }",
        "</style>",
        "</head><body>",
        "<h1>Quick Notes Export</h1>",
    ]

    for note in notes:
        parts.append('<div class="note">')
        # BUG: Title and body are not HTML-escaped
        parts.append(f"  <h2>{note.title}</h2>")
        if note.tags:
            parts.append(f'  <p class="tags">Tags: {", ".join(note.tags)}</p>')
        if note.body:
            # BUG: Newlines in body are not converted to <br> or <p> tags
            parts.append(f"  <p>{note.body}</p>")
        parts.append(f'  <p class="meta">Created: {note.created_at}</p>')
        if note.updated_at:
            parts.append(f'  <p class="meta">Updated: {note.updated_at}</p>')
        parts.append("</div>")

    parts.append("</body></html>")
    return "\n".join(parts)


# TODO: Add PDF export support
# TODO: Add JSON export support (for backup/restore)
