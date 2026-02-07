"""Tests for statistics module."""

import pytest
from mathlib.statistics import (
    mean, median, mode, variance, std_dev, data_range, percentile
)


class TestMean:
    def test_basic(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_single_value(self):
        assert mean([42]) == 42.0

    def test_negative(self):
        assert mean([-1, -2, -3]) == -2.0

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mean([])


class TestMedian:
    def test_odd_length(self):
        assert median([3, 1, 2]) == 2

    # FAILING TEST — median([1, 2, 3, 4]) returns 3, but should return 2.5
    def test_even_length(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_single(self):
        assert median([5]) == 5

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            median([])


class TestMode:
    # FAILING TEST — mode([1, 2, 2, 3]) returns 1, but should return 2
    def test_basic(self):
        assert mode([1, 2, 2, 3]) == 2

    def test_single(self):
        assert mode([7]) == 7

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mode([])


class TestVariance:
    def test_population(self):
        result = variance([2, 4, 4, 4, 5, 5, 7, 9])
        assert abs(result - 4.0) < 1e-9

    def test_sample(self):
        result = variance([2, 4, 4, 4, 5, 5, 7, 9], population=False)
        assert abs(result - 4.571428571428571) < 1e-6

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            variance([])


class TestStdDev:
    def test_basic(self):
        result = std_dev([2, 4, 4, 4, 5, 5, 7, 9])
        assert abs(result - 2.0) < 1e-9


class TestDataRange:
    def test_basic(self):
        assert data_range([1, 5, 3, 9, 2]) == 8

    def test_single(self):
        assert data_range([5]) == 0

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            data_range([])


class TestPercentile:
    def test_50th(self):
        result = percentile([1, 2, 3, 4, 5], 50)
        assert result == 3.0

    def test_0th(self):
        assert percentile([1, 2, 3], 0) == 1.0

    def test_100th(self):
        assert percentile([1, 2, 3], 100) == 3.0

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            percentile([1, 2], 150)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            percentile([], 50)
