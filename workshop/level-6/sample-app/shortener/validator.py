"""URL validation utilities."""

import re
from shortener.config import MAX_URL_LENGTH, ALLOWED_SCHEMES


def is_valid_url(url: str) -> bool:
    """Return True if url looks like a valid HTTP/HTTPS URL."""
    if not url or not isinstance(url, str):
        return False
    if len(url) > MAX_URL_LENGTH:
        return False
    pattern = re.compile(
        r"^(https?://)?"
        r"([a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,}"
        r"(:\d{1,5})?"
        r"(/[^\s]*)?$"
    )
    return bool(pattern.match(url))


def has_valid_scheme(url: str) -> bool:
    """Return True if url starts with an allowed scheme."""
    if not url or not isinstance(url, str):
        return False
    return any(url.startswith(f"{scheme}://") for scheme in ALLOWED_SCHEMES)


def normalize_url(url: str) -> str:
    """Normalize a URL: add scheme if missing, strip trailing slash."""
    if not url:
        return url
    url = url.strip()
    if not has_valid_scheme(url):
        url = f"https://{url}"
    # Strip trailing slash for consistency (except bare domain)
    if url.count("/") > 2 and url.endswith("/"):
        url = url.rstrip("/")
    return url


def validate_and_normalize(url: str) -> tuple:
    """Validate and normalize a URL.

    Returns:
        (normalized_url, error_message) — (url, None) if valid, (None, reason) if invalid.
    """
    if not url or not isinstance(url, str):
        return (None, "URL must be a non-empty string")

    normalized = normalize_url(url)

    if not is_valid_url(normalized.replace("https://", "").replace("http://", "")):
        return (None, f"Invalid URL format: {url}")

    if len(normalized) > MAX_URL_LENGTH:
        return (None, f"URL exceeds maximum length of {MAX_URL_LENGTH} characters")

    return (normalized, None)
