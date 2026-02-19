#!/usr/bin/env python3
"""Benchmark script — measures function execution time."""

import time
import sys
from mathlib.calculator import factorial, power, add
from mathlib.statistics import mean, variance, std_dev


def bench(name, func, *args, iterations=10000):
    """Run func(*args) for `iterations` times and report timing."""
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    elapsed = time.perf_counter() - start
    per_call = elapsed / iterations * 1_000_000  # microseconds
    print(f"  {name:30s}  {iterations:>8,} calls  {elapsed:.4f}s  ({per_call:.2f} µs/call)")


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

    print("=" * 80)
    print(f"  Benchmark — {n:,} iterations per function")
    print("=" * 80)

    data_small = list(range(10))
    data_large = list(range(1000))

    print("\n📐 Calculator")
    bench("add(100, 200)", add, 100, 200, iterations=n)
    bench("power(2, 16)", power, 2, 16, iterations=n)
    bench("factorial(10)", factorial, 10, iterations=n)
    bench("factorial(20)", factorial, 20, iterations=n)

    print("\n📊 Statistics (10 items)")
    bench("mean(10 items)", mean, data_small, iterations=n)
    bench("variance(10 items)", variance, data_small, iterations=n)
    bench("std_dev(10 items)", std_dev, data_small, iterations=n)

    print("\n📊 Statistics (1000 items)")
    bench("mean(1000 items)", mean, data_large, iterations=n)
    bench("variance(1000 items)", variance, data_large, iterations=n)
    bench("std_dev(1000 items)", std_dev, data_large, iterations=n)

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
