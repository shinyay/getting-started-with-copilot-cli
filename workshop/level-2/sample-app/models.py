"""Data models and validation for bookmarks."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional
from urllib.parse import urlparse

from config import Config
from errors import ValidationError


@dataclass
class Bookmark:
    id: int
    url: str
    title: str
    description: str = ""
    tags: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: Optional[str] = None
    visit_count: int = 0
    is_archived: bool = False

    def __post_init__(self):
        self.url = self.url.strip()
        self.title = self.title.strip()
        self.description = self.description.strip()
        self.tags = [t.strip().lower() for t in self.tags if t.strip()]
        self._validate()

    def _validate(self):
        """Validate all fields."""
        if not self.url:
            raise ValidationError("URL is required", field="url")
        if not self._is_valid_url(self.url):
            raise ValidationError(f"Invalid URL: {self.url}", field="url")
        if not self.title:
            raise ValidationError("Title is required", field="title")
        if len(self.title) > Config.MAX_TITLE_LENGTH:
            raise ValidationError(
                f"Title too long ({len(self.title)}/{Config.MAX_TITLE_LENGTH})",
                field="title",
            )
        if len(self.tags) > Config.MAX_TAGS_PER_BOOKMARK:
            raise ValidationError(
                f"Too many tags ({len(self.tags)}/{Config.MAX_TAGS_PER_BOOKMARK})",
                field="tags",
            )
        for tag in self.tags:
            if len(tag) > Config.MAX_TAG_LENGTH:
                raise ValidationError(f"Tag too long: '{tag}'", field="tags")
            if not tag.replace("-", "").replace("_", "").isalnum():
                raise ValidationError(
                    f"Tag contains invalid characters: '{tag}'", field="tags"
                )

    @staticmethod
    def _is_valid_url(url: str) -> bool:
        """Check if a string is a valid HTTP(S) URL."""
        try:
            result = urlparse(url)
            return result.scheme in ("http", "https") and bool(result.netloc)
        except Exception:
            return False

    @property
    def domain(self) -> str:
        """Extract the domain from the URL."""
        return urlparse(self.url).netloc

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Bookmark":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in known}
        return cls(**filtered)

    def touch(self):
        """Record a visit and update timestamp."""
        self.visit_count += 1
        self.updated_at = datetime.utcnow().isoformat()

    def archive(self):
        """Mark as archived."""
        self.is_archived = True
        self.updated_at = datetime.utcnow().isoformat()

    def unarchive(self):
        """Restore from archive."""
        self.is_archived = False
        self.updated_at = datetime.utcnow().isoformat()

    def __str__(self):
        status = "📦" if self.is_archived else "🔖"
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"{status} #{self.id} {self.title} ({self.domain}){tags_str}"
