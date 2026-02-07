#!/usr/bin/env python3
"""Demo script — showcases the math utilities library."""

from mathlib.calculator import add, subtract, multiply, divide, power, factorial
from mathlib.statistics import mean, median, mode, std_dev
from mathlib.converter import celsius_to_fahrenheit, km_to_miles, kg_to_pounds
from mathlib.validator import validate_data


def main():
    print("=" * 60)
    print("  Math Utilities Library — Demo")
    print("=" * 60)

    # Calculator
    print("\n📐 Calculator")
    print(f"  add(2, 3)        = {add(2, 3)}")
    print(f"  subtract(10, 4)  = {subtract(10, 4)}")
    print(f"  multiply(3, 7)   = {multiply(3, 7)}")
    print(f"  divide(15, 4)    = {divide(15, 4)}")
    print(f"  power(2, 10)     = {power(2, 10)}")
    print(f"  factorial(6)     = {factorial(6)}")

    # Statistics
    data = [4, 8, 15, 16, 23, 42]
    print(f"\n📊 Statistics (data = {data})")
    print(f"  mean    = {mean(data):.2f}")
    print(f"  median  = {median(data)}")
    print(f"  std_dev = {std_dev(data):.2f}")

    # Converter
    print("\n🔄 Conversions")
    print(f"  100°C → {celsius_to_fahrenheit(100)}°F")
    print(f"  42 km → {km_to_miles(42):.2f} miles")
    print(f"  70 kg → {kg_to_pounds(70):.2f} lbs")

    # Validator
    print("\n✅ Validation")
    good = [1, 2, 3, 4, 5]
    bad = [1, "two", 3]
    for dataset in [good, bad]:
        is_valid, msg = validate_data(dataset)
        status = "VALID" if is_valid else f"INVALID — {msg}"
        print(f"  {dataset!r:30s} → {status}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
