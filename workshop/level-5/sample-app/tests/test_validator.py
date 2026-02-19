"""Tests for validator module."""

import pytest
from mathlib.validator import (
    is_number, is_positive, is_negative, is_in_range,
    is_integer, is_even, is_odd, is_non_empty_list, validate_data
)


class TestIsNumber:
    def test_int(self):
        assert is_number(5) is True

    def test_float(self):
        assert is_number(3.14) is True

    def test_bool_excluded(self):
        assert is_number(True) is False

    def test_string(self):
        assert is_number("hello") is False

    def test_none(self):
        assert is_number(None) is False


class TestIsPositive:
    def test_positive(self):
        assert is_positive(5) is True

    def test_negative(self):
        assert is_positive(-3) is False

    # FAILING TEST — is_positive(0) returns True, but zero is not positive
    def test_zero_is_not_positive(self):
        assert is_positive(0) is False

    def test_non_number(self):
        assert is_positive("hello") is False


class TestIsNegative:
    def test_negative(self):
        assert is_negative(-5) is True

    def test_positive(self):
        assert is_negative(5) is False

    def test_zero(self):
        assert is_negative(0) is False


class TestIsInRange:
    def test_in_range(self):
        assert is_in_range(5, 1, 10) is True

    def test_at_boundaries(self):
        assert is_in_range(1, 1, 10) is True
        assert is_in_range(10, 1, 10) is True

    def test_out_of_range(self):
        assert is_in_range(11, 1, 10) is False

    def test_non_number(self):
        assert is_in_range("a", 1, 10) is False


class TestIsInteger:
    def test_int(self):
        assert is_integer(5) is True

    def test_float_whole(self):
        assert is_integer(5.0) is True

    def test_float_fractional(self):
        assert is_integer(5.5) is False

    # FAILING TEST — is_integer("hello") crashes instead of returning False
    def test_string_returns_false(self):
        assert is_integer("hello") is False


class TestIsEven:
    def test_even(self):
        assert is_even(4) is True

    def test_odd(self):
        assert is_even(3) is False

    def test_zero(self):
        assert is_even(0) is True

    def test_bool(self):
        assert is_even(True) is False


class TestIsOdd:
    def test_odd(self):
        assert is_odd(3) is True

    def test_even(self):
        assert is_odd(4) is False


class TestValidateData:
    def test_valid(self):
        is_valid, msg = validate_data([1, 2, 3])
        assert is_valid is True
        assert msg is None

    def test_not_list(self):
        is_valid, msg = validate_data("hello")
        assert is_valid is False

    def test_empty(self):
        is_valid, msg = validate_data([])
        assert is_valid is False

    def test_non_numeric_item(self):
        is_valid, msg = validate_data([1, "a", 3])
        assert is_valid is False
        assert "index 1" in msg
