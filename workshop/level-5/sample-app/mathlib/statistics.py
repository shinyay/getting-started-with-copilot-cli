"""Statistical functions for numerical data."""

from typing import List, Optional


def mean(data: List[float]) -> float:
    """Return the arithmetic mean of data."""
    if not data:
        raise ValueError("Cannot compute mean of empty list")
    return sum(data) / len(data)


# BUG: median of even-length list is wrong — uses integer division instead of averaging
def median(data: List[float]) -> float:
    """Return the median value of data."""
    if not data:
        raise ValueError("Cannot compute median of empty list")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        # BUG: should return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]  # BUG: wrong for even-length lists
    return sorted_data[mid]


# BUG: mode returns first element instead of most frequent
def mode(data: List[float]) -> float:
    """Return the most frequently occurring value in data."""
    if not data:
        raise ValueError("Cannot compute mode of empty list")
    # BUG: should count frequencies and return the most common
    return data[0]  # BUG: always returns first element


def variance(data: List[float], population: bool = True) -> float:
    """Return the variance of data.

    Args:
        data: List of numbers.
        population: If True, compute population variance (N). If False, sample variance (N-1).
    """
    if not data:
        raise ValueError("Cannot compute variance of empty list")
    avg = mean(data)
    squared_diffs = [(x - avg) ** 2 for x in data]
    divisor = len(data) if population else (len(data) - 1)
    if divisor == 0:
        raise ValueError("Sample variance requires at least 2 data points")
    return sum(squared_diffs) / divisor


def std_dev(data: List[float], population: bool = True) -> float:
    """Return the standard deviation of data."""
    return variance(data, population) ** 0.5


def data_range(data: List[float]) -> float:
    """Return the range (max - min) of data."""
    if not data:
        raise ValueError("Cannot compute range of empty list")
    return max(data) - min(data)


def percentile(data: List[float], p: float) -> float:
    """Return the p-th percentile of data (0 <= p <= 100)."""
    if not data:
        raise ValueError("Cannot compute percentile of empty list")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100)
    f = int(k)
    c = f + 1
    if c >= len(sorted_data):
        return sorted_data[f]
    return sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f])
