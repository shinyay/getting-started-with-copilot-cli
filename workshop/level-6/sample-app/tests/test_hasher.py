"""Tests for hasher module."""

import pytest
from shortener.hasher import generate_code, generate_random_code, is_valid_code
from shortener.config import CODE_LENGTH


class TestGenerateCode:
    def test_returns_string(self):
        code = generate_code("https://example.com")
        assert isinstance(code, str)

    def test_correct_length(self):
        code = generate_code("https://example.com")
        assert len(code) == CODE_LENGTH

    def test_deterministic(self):
        c1 = generate_code("https://example.com")
        c2 = generate_code("https://example.com")
        assert c1 == c2

    def test_different_urls_different_codes(self):
        c1 = generate_code("https://a.com")
        c2 = generate_code("https://b.com")
        assert c1 != c2

    def test_custom_length(self):
        code = generate_code("https://example.com", length=10)
        assert len(code) == 10


class TestGenerateRandomCode:
    def test_correct_length(self):
        code = generate_random_code()
        assert len(code) == CODE_LENGTH

    def test_custom_length(self):
        code = generate_random_code(length=12)
        assert len(code) == 12


class TestIsValidCode:
    def test_valid(self):
        code = generate_code("https://example.com")
        assert is_valid_code(code) is True

    def test_wrong_length(self):
        assert is_valid_code("ab") is False

    def test_invalid_chars(self):
        assert is_valid_code("ABC!!!" ) is False

    def test_empty(self):
        assert is_valid_code("") is False

    def test_none(self):
        assert is_valid_code(None) is False
