"""Configuration constants for Quick Notes."""

import os

# Storage
DATA_DIR = os.environ.get("NOTES_DATA_DIR", ".")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")

# Limits
MAX_NOTES = 10000
MAX_TITLE_LENGTH = 200
MAX_BODY_LENGTH = 50000
MAX_TAGS_PER_NOTE = 20

# Search
SEARCH_MIN_QUERY_LENGTH = 2

# Export
EXPORT_FORMATS = ["markdown", "html"]
DEFAULT_EXPORT_FORMAT = "markdown"

# Display
PREVIEW_LENGTH = 80
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# TODO: Add support for configuring via a config file (~/.quicknotes.toml)
# TODO: Add support for multiple notebooks (separate data files)
