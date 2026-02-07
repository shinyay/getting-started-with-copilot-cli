"""Tests for converter module — all tests pass (baseline)."""

import pytest
from mathlib.converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    km_to_miles, miles_to_km,
    meters_to_feet, feet_to_meters,
    kg_to_pounds, pounds_to_kg,
    bytes_to_kb, kb_to_mb, mb_to_gb,
)


class TestTemperature:
    def test_c_to_f_boiling(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_c_to_f_freezing(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_f_to_c_boiling(self):
        assert fahrenheit_to_celsius(212) == 100

    def test_f_to_c_freezing(self):
        assert fahrenheit_to_celsius(32) == 0

    def test_c_to_k_zero(self):
        assert celsius_to_kelvin(0) == 273.15

    def test_k_to_c_zero(self):
        assert kelvin_to_celsius(273.15) == 0

    def test_roundtrip_c_f(self):
        original = 37.5
        assert abs(fahrenheit_to_celsius(celsius_to_fahrenheit(original)) - original) < 1e-9


class TestDistance:
    def test_km_to_miles(self):
        assert abs(km_to_miles(1.60934) - 1.0) < 0.01

    def test_miles_to_km(self):
        assert abs(miles_to_km(1.0) - 1.60934) < 0.01

    def test_m_to_ft(self):
        assert abs(meters_to_feet(1.0) - 3.28084) < 0.01

    def test_ft_to_m(self):
        assert abs(feet_to_meters(3.28084) - 1.0) < 0.01


class TestWeight:
    def test_kg_to_lb(self):
        assert abs(kg_to_pounds(1.0) - 2.20462) < 0.01

    def test_lb_to_kg(self):
        assert abs(pounds_to_kg(2.20462) - 1.0) < 0.01


class TestData:
    def test_bytes_to_kb(self):
        assert bytes_to_kb(1024) == 1.0

    def test_kb_to_mb(self):
        assert kb_to_mb(1024) == 1.0

    def test_mb_to_gb(self):
        assert mb_to_gb(1024) == 1.0
