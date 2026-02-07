"""Unit conversion functions."""


# --- Temperature ---

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius."""
    return k - 273.15


# --- Distance ---

def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371


def meters_to_feet(m: float) -> float:
    """Convert meters to feet."""
    return m * 3.28084


def feet_to_meters(ft: float) -> float:
    """Convert feet to meters."""
    return ft / 3.28084


# --- Weight ---

def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462


def pounds_to_kg(lb: float) -> float:
    """Convert pounds to kilograms."""
    return lb / 2.20462


# --- Data ---

def bytes_to_kb(b: int) -> float:
    """Convert bytes to kilobytes."""
    return b / 1024


def kb_to_mb(kb: float) -> float:
    """Convert kilobytes to megabytes."""
    return kb / 1024


def mb_to_gb(mb: float) -> float:
    """Convert megabytes to gigabytes."""
    return mb / 1024
