"""Basic arithmetic operations."""

import math  # noqa: F401 — intentional unused import (lint target)
import os  # noqa: F401 — intentional unused import (lint target)


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


# BUG: returns None instead of raising ValueError for division by zero
def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        return None  # BUG: should raise ValueError("Cannot divide by zero")
    return a / b


def power(a, n):
    """Return a raised to the power n."""
    # BUG: doesn't handle negative exponents — returns 0 instead of fractional result
    if n < 0:
        return 0  # BUG: should return a ** n (e.g., 2 ** -1 = 0.5)
    result = 1
    for _ in range(n):
        result *= a
    return result


def modulo(a, b):
    """Return a modulo b."""
    if b == 0:
        raise ValueError("Cannot compute modulo with zero divisor")
    return a % b


def absolute(a):
    return abs(a)


# Intentional lint issue: line too long (> 79 chars)
def factorial(n):
    """Return the factorial of n. Raises ValueError if n is negative. Only accepts non-negative integers as input values."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial requires a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
