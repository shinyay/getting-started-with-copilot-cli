"""Usage statistics for the URL shortener."""

from shortener.config import STATS_FILE
from shortener.store import _read_stats, count


def get_stats() -> dict:
    """Return usage statistics.

    Returns a dict with:
        - total_created: Total URLs ever created (from stats file)
        - total_expanded: Total expand operations
        - active_urls: Current number of active URLs
        - deleted_urls: Estimated number of deleted URLs

    BUG: deleted_urls is calculated as total_created - active_urls.
    But total_created is never decremented on delete, so after
    creating 5 URLs and deleting 2, it shows:
        total_created=5, active=3, deleted=2 ← correct coincidentally
    However, if you create 5, delete 2, create 1 more:
        total_created=6, active=4, deleted=2 ← correct
    The real bug is that total_created doesn't mean "currently stored"
    and using it to derive "deleted" is fragile. A better approach
    would be to track deletions explicitly.
    """
    stats = _read_stats()
    active = count()

    total_created = stats.get("total_created", 0)
    total_expanded = stats.get("total_expanded", 0)

    return {
        "total_created": total_created,
        "total_expanded": total_expanded,
        "active_urls": active,
        "deleted_urls": total_created - active,
    }


def get_summary() -> str:
    """Return a human-readable stats summary."""
    s = get_stats()
    lines = [
        "URL Shortener Statistics",
        "=" * 30,
        f"  Total created:  {s['total_created']}",
        f"  Total expanded: {s['total_expanded']}",
        f"  Active URLs:    {s['active_urls']}",
        f"  Deleted URLs:   {s['deleted_urls']}",
    ]
    return "\n".join(lines)
