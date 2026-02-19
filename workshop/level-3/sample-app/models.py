"""Note data model and validation."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

from config import MAX_TITLE_LENGTH, MAX_BODY_LENGTH, MAX_TAGS_PER_NOTE, DATE_FORMAT


@dataclass
class Note:
    id: int
    title: str
    body: str = ""
    tags: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().strftime(DATE_FORMAT))
    updated_at: Optional[str] = None
    is_pinned: bool = False

    def __post_init__(self):
        self.title = self.title.strip()
        self.body = self.body.strip()
        # BUG: Tags are not normalized (not lowercased, not stripped)
        # This causes "Python" and "python" to be treated as different tags
        self._validate()

    def _validate(self):
        if not self.title:
            raise ValueError("Note title cannot be empty")
        if len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title too long ({len(self.title)}/{MAX_TITLE_LENGTH})")
        if len(self.body) > MAX_BODY_LENGTH:
            raise ValueError(f"Body too long ({len(self.body)}/{MAX_BODY_LENGTH})")
        if len(self.tags) > MAX_TAGS_PER_NOTE:
            raise ValueError(f"Too many tags ({len(self.tags)}/{MAX_TAGS_PER_NOTE})")
        # TODO: Validate individual tag format (no spaces, no special chars)

    def touch(self):
        """Update the modified timestamp."""
        self.updated_at = datetime.now().strftime(DATE_FORMAT)

    @property
    def preview(self) -> str:
        """Short preview of the body text."""
        from config import PREVIEW_LENGTH
        if len(self.body) <= PREVIEW_LENGTH:
            return self.body
        return self.body[:PREVIEW_LENGTH] + "..."

    @property
    def word_count(self) -> int:
        """Count words in the body."""
        return len(self.body.split())

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in known}
        return cls(**filtered)

    def __str__(self):
        pin = "📌 " if self.is_pinned else ""
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"{pin}#{self.id} {self.title}{tags_str}"
