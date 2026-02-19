"""Configuration for URL Shortener."""

import os

# Storage
DATA_DIR = os.environ.get("SHORTENER_DATA_DIR", ".")
URLS_FILE = os.path.join(DATA_DIR, "urls.json")
STATS_FILE = os.path.join(DATA_DIR, "stats.json")

# Short codes
CODE_LENGTH = 6
CODE_CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789"

# Validation
MAX_URL_LENGTH = 2048
ALLOWED_SCHEMES = ("http", "https")

# Expiration (feature gap — not yet implemented)
DEFAULT_EXPIRY_HOURS = 0  # 0 = no expiration
