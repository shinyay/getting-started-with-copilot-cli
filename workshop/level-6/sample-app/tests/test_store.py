"""Tests for store module."""

import json
import os
import pytest
import tempfile
from unittest.mock import patch
from shortener.store import shorten, expand, delete, list_all, count


@pytest.fixture(autouse=True)
def temp_data_dir(tmp_path):
    """Use a temporary directory for all data files."""
    urls_file = str(tmp_path / "urls.json")
    stats_file = str(tmp_path / "stats.json")
    with patch("shortener.store.URLS_FILE", urls_file), \
         patch("shortener.store.STATS_FILE", stats_file), \
         patch("shortener.config.URLS_FILE", urls_file), \
         patch("shortener.config.STATS_FILE", stats_file):
        yield tmp_path


class TestShorten:
    def test_creates_entry(self):
        result = shorten("https://example.com")
        assert "code" in result
        assert result["url"] == "https://example.com"
        assert "created_at" in result

    def test_custom_code(self):
        result = shorten("https://example.com", custom_code="abc123")
        assert result["code"] == "abc123"

    def test_duplicate_code_raises(self):
        shorten("https://example.com", custom_code="abc123")
        with pytest.raises(ValueError, match="already exists"):
            shorten("https://other.com", custom_code="abc123")

    def test_deterministic_code(self):
        r1 = shorten("https://unique1.com")
        r2 = shorten("https://unique2.com")
        assert r1["code"] != r2["code"]


class TestExpand:
    def test_returns_url(self):
        result = shorten("https://example.com", custom_code="test01")
        url = expand("test01")
        assert url == "https://example.com"

    def test_not_found_raises(self):
        with pytest.raises(KeyError, match="not found"):
            expand("nonexistent")

    def test_increments_access_count(self):
        shorten("https://example.com", custom_code="count1")
        expand("count1")
        expand("count1")
        expand("count1")
        entries = list_all()
        entry = [e for e in entries if e["code"] == "count1"][0]
        assert entry["access_count"] == 3


class TestDelete:
    def test_deletes_entry(self):
        shorten("https://example.com", custom_code="del001")
        assert delete("del001") is True
        assert count() == 0

    def test_not_found_returns_false(self):
        assert delete("nonexistent") is False


class TestListAll:
    def test_empty(self):
        assert list_all() == []

    def test_returns_all(self):
        shorten("https://a.com", custom_code="aaa001")
        shorten("https://b.com", custom_code="bbb001")
        entries = list_all()
        assert len(entries) == 2
        codes = {e["code"] for e in entries}
        assert codes == {"aaa001", "bbb001"}


class TestCount:
    def test_empty(self):
        assert count() == 0

    def test_after_shorten(self):
        shorten("https://example.com", custom_code="cnt001")
        assert count() == 1
