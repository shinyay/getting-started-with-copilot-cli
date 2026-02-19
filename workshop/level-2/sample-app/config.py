"""Environment-based configuration for the bookmark manager."""

import os


class Config:
    """Application configuration loaded from environment variables."""

    # Server
    HOST: str = os.environ.get("BM_HOST", "0.0.0.0")
    PORT: int = int(os.environ.get("BM_PORT", "8080"))

    # Storage backend: "file" or "memory"
    STORAGE_BACKEND: str = os.environ.get("BM_STORAGE", "file")
    DATA_FILE: str = os.environ.get("BM_DATA_FILE", "bookmarks.json")

    # Limits
    MAX_BOOKMARKS: int = int(os.environ.get("BM_MAX_BOOKMARKS", "5000"))
    MAX_TITLE_LENGTH: int = 300
    MAX_TAGS_PER_BOOKMARK: int = 10
    MAX_TAG_LENGTH: int = 50

    # Auth (simple token-based)
    AUTH_ENABLED: bool = os.environ.get("BM_AUTH_ENABLED", "false").lower() == "true"
    AUTH_TOKEN: str = os.environ.get("BM_AUTH_TOKEN", "")

    # Logging
    LOG_LEVEL: str = os.environ.get("BM_LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    @classmethod
    def validate(cls) -> list[str]:
        """Return a list of configuration warnings."""
        warnings = []
        if cls.AUTH_ENABLED and not cls.AUTH_TOKEN:
            warnings.append("AUTH_ENABLED is true but AUTH_TOKEN is empty")
        if cls.STORAGE_BACKEND not in ("file", "memory"):
            warnings.append(f"Unknown STORAGE_BACKEND: {cls.STORAGE_BACKEND}")
        if cls.PORT < 1 or cls.PORT > 65535:
            warnings.append(f"Invalid PORT: {cls.PORT}")
        return warnings
