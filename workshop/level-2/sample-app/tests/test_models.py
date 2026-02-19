"""Unit tests for bookmark models."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Bookmark
from errors import ValidationError


class TestBookmarkCreation:
    def test_valid_bookmark(self):
        b = Bookmark(id=1, url="https://example.com", title="Example")
        assert b.id == 1
        assert b.url == "https://example.com"
        assert b.title == "Example"
        assert b.tags == []
        assert b.visit_count == 0
        assert not b.is_archived

    def test_with_tags(self):
        b = Bookmark(id=1, url="https://example.com", title="Test", tags=["python", "testing"])
        assert b.tags == ["python", "testing"]

    def test_strips_whitespace(self):
        b = Bookmark(id=1, url="  https://example.com  ", title="  Test  ")
        assert b.url == "https://example.com"
        assert b.title == "Test"

    def test_empty_url_raises(self):
        with pytest.raises(ValidationError, match="URL is required"):
            Bookmark(id=1, url="", title="Test")

    def test_invalid_url_raises(self):
        with pytest.raises(ValidationError, match="Invalid URL"):
            Bookmark(id=1, url="not-a-url", title="Test")

    def test_ftp_url_raises(self):
        with pytest.raises(ValidationError, match="Invalid URL"):
            Bookmark(id=1, url="ftp://files.example.com/doc", title="FTP")

    def test_empty_title_raises(self):
        with pytest.raises(ValidationError, match="Title is required"):
            Bookmark(id=1, url="https://example.com", title="")

    def test_long_title_raises(self):
        with pytest.raises(ValidationError, match="Title too long"):
            Bookmark(id=1, url="https://example.com", title="x" * 301)

    def test_too_many_tags_raises(self):
        with pytest.raises(ValidationError, match="Too many tags"):
            Bookmark(id=1, url="https://example.com", title="Test", tags=[f"tag{i}" for i in range(11)])

    def test_invalid_tag_chars_raises(self):
        with pytest.raises(ValidationError, match="invalid characters"):
            Bookmark(id=1, url="https://example.com", title="Test", tags=["good", "bad tag!"])


class TestBookmarkProperties:
    def test_domain_extraction(self):
        b = Bookmark(id=1, url="https://docs.python.org/3/library/", title="Python Docs")
        assert b.domain == "docs.python.org"

    def test_touch_increments_visits(self):
        b = Bookmark(id=1, url="https://example.com", title="Test")
        assert b.visit_count == 0
        b.touch()
        assert b.visit_count == 1
        assert b.updated_at is not None

    def test_archive_and_restore(self):
        b = Bookmark(id=1, url="https://example.com", title="Test")
        assert not b.is_archived
        b.archive()
        assert b.is_archived
        b.unarchive()
        assert not b.is_archived

    def test_str_representation(self):
        b = Bookmark(id=42, url="https://example.com", title="My Site", tags=["web"])
        s = str(b)
        assert "#42" in s
        assert "My Site" in s
        assert "example.com" in s

    def test_to_dict_roundtrip(self):
        b = Bookmark(id=1, url="https://example.com", title="Test", tags=["a", "b"])
        d = b.to_dict()
        b2 = Bookmark.from_dict(d)
        assert b.url == b2.url
        assert b.title == b2.title
        assert b.tags == b2.tags
