"""Tests for calculator module."""

import pytest
from mathlib.calculator import (
    add, subtract, multiply, divide, power, modulo, absolute, factorial
)


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_mixed_signs(self):
        assert add(-1, 3) == 2

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zeros(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive_result(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_zeros(self):
        assert subtract(0, 0) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_floats(self):
        assert abs(multiply(1.5, 2.0) - 3.0) < 1e-9


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_division(self):
        assert abs(divide(7, 2) - 3.5) < 1e-9

    # FAILING TEST — divide(1, 0) returns None, but test expects ValueError
    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)

    def test_negative_division(self):
        assert divide(-10, 2) == -5.0


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    # FAILING TEST — power(2, -1) returns 0, but should return 0.5
    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_power_of_one(self):
        assert power(7, 1) == 7


class TestModulo:
    def test_basic_modulo(self):
        assert modulo(10, 3) == 1

    def test_even_division(self):
        assert modulo(10, 5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError):
            modulo(10, 0)


class TestAbsolute:
    def test_positive(self):
        assert absolute(5) == 5

    def test_negative(self):
        assert absolute(-5) == 5

    def test_zero(self):
        assert absolute(0) == 0


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_five(self):
        assert factorial(5) == 120

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_float_raises(self):
        with pytest.raises(ValueError):
            factorial(3.5)
