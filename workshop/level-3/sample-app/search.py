"""Full-text search across notes."""

from models import Note


def search_notes(notes: list[Note], query: str) -> list[Note]:
    """Search notes by matching query against title, body, and tags.

    BUG: Search is case-sensitive — searching for "Python" won't find "python"
    TODO: Add support for search operators (tag:python, title:"meeting notes")
    TODO: Add relevance scoring (title matches should rank higher than body matches)
    """
    if not query or len(query) < 2:
        return []

    results = []
    for note in notes:
        if _matches(note, query):
            results.append(note)

    return results


def _matches(note: Note, query: str) -> bool:
    """Check if a note matches the search query."""
    # BUG: This is case-sensitive — see docstring above
    if query in note.title:
        return True
    if query in note.body:
        return True
    for tag in note.tags:
        if query in tag:
            return True
    return False


# TODO: Implement highlight_matches() to show where the query matched
# def highlight_matches(note: Note, query: str) -> dict:
#     """Return matched portions of the note for display."""
#     pass
