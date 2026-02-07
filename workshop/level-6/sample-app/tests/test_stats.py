"""Tests for stats module — INCOMPLETE (doesn't test after-delete scenario)."""

import pytest
from unittest.mock import patch
from shortener.store import shorten, expand, delete
from shortener.stats import get_stats, get_summary


@pytest.fixture(autouse=True)
def temp_data_dir(tmp_path):
    """Use a temporary directory for all data files."""
    urls_file = str(tmp_path / "urls.json")
    stats_file = str(tmp_path / "stats.json")
    with patch("shortener.store.URLS_FILE", urls_file), \
         patch("shortener.store.STATS_FILE", stats_file), \
         patch("shortener.stats.STATS_FILE", stats_file):
        yield tmp_path


class TestGetStats:
    def test_empty(self):
        stats = get_stats()
        assert stats["total_created"] == 0
        assert stats["active_urls"] == 0

    def test_after_shorten(self):
        shorten("https://example.com", custom_code="stat01")
        stats = get_stats()
        assert stats["total_created"] == 1
        assert stats["active_urls"] == 1

    def test_after_expand(self):
        shorten("https://example.com", custom_code="stat02")
        expand("stat02")
        stats = get_stats()
        assert stats["total_expanded"] == 1

    # NOTE: test_after_delete is MISSING — this is an intentional test gap.
    # The multi-file bug (stats wrong after delete) is not caught by existing tests.


class TestGetSummary:
    def test_returns_string(self):
        summary = get_summary()
        assert isinstance(summary, str)
        assert "Statistics" in summary

    def test_contains_all_fields(self):
        shorten("https://example.com", custom_code="sum001")
        summary = get_summary()
        assert "Total created" in summary
        assert "Active URLs" in summary
