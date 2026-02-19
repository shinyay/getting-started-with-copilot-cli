"""Business logic layer — orchestrates validation, storage, and tag management."""

from typing import Optional

from config import Config
from models import Bookmark
from repository import BaseRepository
from errors import (
    NotFoundError,
    DuplicateError,
    LimitExceededError,
    ValidationError,
)


class BookmarkService:
    """Encapsulates business rules for bookmark management."""

    def __init__(self, repository: BaseRepository):
        self._repo = repository

    def create_bookmark(
        self,
        url: str,
        title: str,
        description: str = "",
        tags: list[str] | None = None,
    ) -> Bookmark:
        """Create a new bookmark with duplicate URL detection."""
        if self._repo.count() >= Config.MAX_BOOKMARKS:
            raise LimitExceededError(
                f"Bookmark limit reached ({Config.MAX_BOOKMARKS})"
            )

        # Check for duplicate URL
        existing = self._find_by_url(url.strip())
        if existing:
            raise DuplicateError(
                f"URL already bookmarked as #{existing.id}: {existing.title}"
            )

        bookmark = Bookmark(
            id=0,  # Will be assigned by repository
            url=url,
            title=title,
            description=description,
            tags=tags or [],
        )
        return self._repo.save(bookmark)

    def get_bookmark(self, bookmark_id: int) -> Bookmark:
        """Retrieve a bookmark by ID."""
        bookmark = self._repo.get(bookmark_id)
        if not bookmark:
            raise NotFoundError(f"Bookmark #{bookmark_id} not found")
        return bookmark

    def list_bookmarks(
        self,
        tag: Optional[str] = None,
        domain: Optional[str] = None,
        include_archived: bool = False,
        sort_by: str = "created",
    ) -> list[Bookmark]:
        """List bookmarks with optional filtering and sorting."""
        if tag:
            bookmarks = self._repo.find_by_tag(tag)
        elif domain:
            bookmarks = self._repo.find_by_domain(domain)
        else:
            bookmarks = self._repo.list_all()

        if not include_archived:
            bookmarks = [b for b in bookmarks if not b.is_archived]

        sort_keys = {
            "created": lambda b: b.created_at,
            "title": lambda b: b.title.lower(),
            "visits": lambda b: -b.visit_count,
            "domain": lambda b: b.domain,
        }
        key_fn = sort_keys.get(sort_by, sort_keys["created"])
        bookmarks.sort(key=key_fn)

        return bookmarks

    def delete_bookmark(self, bookmark_id: int) -> Bookmark:
        """Permanently remove a bookmark."""
        return self._repo.delete(bookmark_id)

    def visit_bookmark(self, bookmark_id: int) -> Bookmark:
        """Record a visit (increment counter, update timestamp)."""
        bookmark = self.get_bookmark(bookmark_id)
        bookmark.touch()
        return self._repo.update(bookmark)

    def archive_bookmark(self, bookmark_id: int) -> Bookmark:
        """Move a bookmark to the archive."""
        bookmark = self.get_bookmark(bookmark_id)
        if bookmark.is_archived:
            raise ValidationError("Bookmark is already archived")
        bookmark.archive()
        return self._repo.update(bookmark)

    def restore_bookmark(self, bookmark_id: int) -> Bookmark:
        """Restore a bookmark from the archive."""
        bookmark = self.get_bookmark(bookmark_id)
        if not bookmark.is_archived:
            raise ValidationError("Bookmark is not archived")
        bookmark.unarchive()
        return self._repo.update(bookmark)

    def get_all_tags(self) -> dict[str, int]:
        """Return all tags with their usage count."""
        tag_counts: dict[str, int] = {}
        for bookmark in self._repo.list_all():
            for tag in bookmark.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        return dict(sorted(tag_counts.items(), key=lambda x: -x[1]))

    def get_stats(self) -> dict:
        """Return aggregate statistics."""
        bookmarks = self._repo.list_all()
        total = len(bookmarks)
        archived = sum(1 for b in bookmarks if b.is_archived)
        domains = {}
        for b in bookmarks:
            domains[b.domain] = domains.get(b.domain, 0) + 1
        top_domains = sorted(domains.items(), key=lambda x: -x[1])[:10]

        return {
            "total": total,
            "active": total - archived,
            "archived": archived,
            "total_visits": sum(b.visit_count for b in bookmarks),
            "unique_tags": len(self.get_all_tags()),
            "unique_domains": len(domains),
            "top_domains": dict(top_domains),
        }

    def _find_by_url(self, url: str) -> Optional[Bookmark]:
        """Find a bookmark by exact URL match."""
        for bookmark in self._repo.list_all():
            if bookmark.url == url:
                return bookmark
        return None
