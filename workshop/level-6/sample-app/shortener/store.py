"""JSON-based URL storage."""

import json
import os
from datetime import datetime, timezone
from shortener.config import URLS_FILE, STATS_FILE
from shortener.hasher import generate_code


def _read_urls() -> dict:
    """Read the URL mapping file."""
    if not os.path.exists(URLS_FILE):
        return {}
    try:
        with open(URLS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def _write_urls(data: dict) -> None:
    """Write the URL mapping file."""
    with open(URLS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def _read_stats() -> dict:
    """Read the stats file."""
    if not os.path.exists(STATS_FILE):
        return {"total_created": 0, "total_expanded": 0}
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"total_created": 0, "total_expanded": 0}


def _write_stats(stats: dict) -> None:
    """Write the stats file."""
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)


def _increment_stat(key: str) -> None:
    """Increment a stat counter."""
    stats = _read_stats()
    stats[key] = stats.get(key, 0) + 1
    _write_stats(stats)


def shorten(url: str, custom_code: str = None) -> dict:
    """Create a shortened URL entry.

    Args:
        url: The original URL to shorten.
        custom_code: Optional custom short code. If None, one is generated.

    Returns:
        dict with 'code', 'url', 'created_at' keys.

    Raises:
        ValueError: If the short code already exists.
    """
    urls = _read_urls()

    code = custom_code if custom_code else generate_code(url)

    if code in urls:
        raise ValueError(f"Short code '{code}' already exists")

    entry = {
        "url": url,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "access_count": 0,
    }
    urls[code] = entry
    _write_urls(urls)

    # BUG: increments total_created in stats, but delete() does NOT decrement it.
    # This causes stats to show wrong "total active" count after deletions.
    _increment_stat("total_created")

    return {"code": code, "url": url, "created_at": entry["created_at"]}


def expand(code: str) -> str:
    """Look up the original URL for a short code.

    Returns:
        The original URL string.

    Raises:
        KeyError: If the short code does not exist.
    """
    urls = _read_urls()
    if code not in urls:
        raise KeyError(f"Short code '{code}' not found")

    # Update access count
    urls[code]["access_count"] = urls[code].get("access_count", 0) + 1
    _write_urls(urls)

    _increment_stat("total_expanded")

    return urls[code]["url"]


def delete(code: str) -> bool:
    """Delete a shortened URL entry.

    Returns:
        True if deleted, False if not found.
    """
    urls = _read_urls()
    if code not in urls:
        return False

    del urls[code]
    _write_urls(urls)

    # BUG: does NOT decrement "total_created" in stats.
    # stats.py will report wrong counts because it trusts total_created
    # to reflect the current number of active URLs.

    return True


def list_all() -> list:
    """Return all shortened URL entries as a list of dicts."""
    urls = _read_urls()
    result = []
    for code, entry in urls.items():
        result.append({
            "code": code,
            "url": entry["url"],
            "created_at": entry.get("created_at", "unknown"),
            "access_count": entry.get("access_count", 0),
        })
    return result


def get_entry(code: str) -> dict:
    """Get a single URL entry by code.

    Raises:
        KeyError: If not found.
    """
    urls = _read_urls()
    if code not in urls:
        raise KeyError(f"Short code '{code}' not found")
    entry = urls[code].copy()
    entry["code"] = code
    return entry


def count() -> int:
    """Return the number of stored URLs."""
    return len(_read_urls())
