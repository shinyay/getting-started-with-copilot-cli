"""Input validation utilities."""


def is_number(value) -> bool:
    """Return True if value is a number (int or float), False otherwise."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


# BUG: returns True for zero — should return False
def is_positive(value) -> bool:
    """Return True if value is a positive number (strictly greater than zero)."""
    if not is_number(value):
        return False
    return value >= 0  # BUG: should be value > 0 (zero is not positive)


def is_negative(value) -> bool:
    """Return True if value is a negative number."""
    if not is_number(value):
        return False
    return value < 0


def is_in_range(value, low, high) -> bool:
    """Return True if low <= value <= high."""
    if not all(is_number(v) for v in [value, low, high]):
        return False
    return low <= value <= high


# BUG: crashes on string input instead of returning False
def is_integer(value) -> bool:
    """Return True if value is an integer or a float with no fractional part."""
    # BUG: should check is_number(value) first
    return value == int(value)  # BUG: crashes if value is a string — int("hello") raises ValueError


def is_even(value) -> bool:
    """Return True if value is an even integer."""
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    return value % 2 == 0


def is_odd(value) -> bool:
    """Return True if value is an odd integer."""
    if not isinstance(value, int) or isinstance(value, bool):
        return False
    return value % 2 != 0


def is_non_empty_list(value) -> bool:
    """Return True if value is a non-empty list."""
    return isinstance(value, list) and len(value) > 0


def validate_data(data) -> tuple:
    """Validate a data list for statistical operations.

    Returns:
        (is_valid, error_message) — (True, None) if valid, (False, reason) if not.
    """
    if not isinstance(data, list):
        return (False, "Input must be a list")
    if len(data) == 0:
        return (False, "List must not be empty")
    for i, item in enumerate(data):
        if not is_number(item):
            return (False, f"Item at index {i} is not a number: {item!r}")
    return (True, None)
