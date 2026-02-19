"""Unit tests for the bookmark service layer."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from service import BookmarkService
from repository import InMemoryRepository
from errors import NotFoundError, DuplicateError, ValidationError


@pytest.fixture
def service():
    repo = InMemoryRepository()
    return BookmarkService(repo)


class TestCreateBookmark:
    def test_create_basic(self, service):
        b = service.create_bookmark(url="https://example.com", title="Example")
        assert b.id == 1
        assert b.url == "https://example.com"
        assert b.title == "Example"

    def test_create_with_tags(self, service):
        b = service.create_bookmark(
            url="https://python.org", title="Python", tags=["python", "language"]
        )
        assert b.tags == ["python", "language"]

    def test_duplicate_url_raises(self, service):
        service.create_bookmark(url="https://example.com", title="First")
        with pytest.raises(DuplicateError, match="already bookmarked"):
            service.create_bookmark(url="https://example.com", title="Second")

    def test_ids_increment(self, service):
        b1 = service.create_bookmark(url="https://one.com", title="One")
        b2 = service.create_bookmark(url="https://two.com", title="Two")
        assert b1.id == 1
        assert b2.id == 2


class TestGetBookmark:
    def test_get_existing(self, service):
        created = service.create_bookmark(url="https://example.com", title="Test")
        found = service.get_bookmark(created.id)
        assert found.url == created.url

    def test_get_missing_raises(self, service):
        with pytest.raises(NotFoundError):
            service.get_bookmark(999)


class TestListBookmarks:
    def test_list_empty(self, service):
        assert service.list_bookmarks() == []

    def test_list_filters_archived(self, service):
        service.create_bookmark(url="https://one.com", title="Active")
        b2 = service.create_bookmark(url="https://two.com", title="Archived")
        service.archive_bookmark(b2.id)

        active = service.list_bookmarks(include_archived=False)
        all_bookmarks = service.list_bookmarks(include_archived=True)
        assert len(active) == 1
        assert len(all_bookmarks) == 2

    def test_list_filter_by_tag(self, service):
        service.create_bookmark(url="https://one.com", title="One", tags=["python"])
        service.create_bookmark(url="https://two.com", title="Two", tags=["go"])
        result = service.list_bookmarks(tag="python")
        assert len(result) == 1
        assert result[0].title == "One"


class TestVisitBookmark:
    def test_visit_increments_count(self, service):
        b = service.create_bookmark(url="https://example.com", title="Test")
        assert b.visit_count == 0
        updated = service.visit_bookmark(b.id)
        assert updated.visit_count == 1


class TestArchiveRestore:
    def test_archive_and_restore(self, service):
        b = service.create_bookmark(url="https://example.com", title="Test")
        archived = service.archive_bookmark(b.id)
        assert archived.is_archived
        restored = service.restore_bookmark(b.id)
        assert not restored.is_archived

    def test_archive_already_archived_raises(self, service):
        b = service.create_bookmark(url="https://example.com", title="Test")
        service.archive_bookmark(b.id)
        with pytest.raises(ValidationError, match="already archived"):
            service.archive_bookmark(b.id)


class TestStats:
    def test_stats_empty(self, service):
        s = service.get_stats()
        assert s["total"] == 0

    def test_stats_with_data(self, service):
        service.create_bookmark(url="https://one.com", title="One", tags=["a"])
        service.create_bookmark(url="https://two.com", title="Two", tags=["a", "b"])
        b3 = service.create_bookmark(url="https://three.com", title="Three")
        service.archive_bookmark(b3.id)

        s = service.get_stats()
        assert s["total"] == 3
        assert s["active"] == 2
        assert s["archived"] == 1
        assert s["unique_tags"] == 2
