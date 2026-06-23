"""Benchmark script for measuring float formatting performance.

This script measures the time required to format a large list of floating‑point numbers
using the standard Python formatting (f‑strings) and, if available, the {fmt} library
via its Python bindings. The script is intended to be run on a machine with a free GPU,
but it does not require any GPU‑specific code – the GPU can be used by the {fmt}
bindings if they leverage CUDA.

Environment variables:
    BENCH_ITERATIONS – number of iterations (default: 100_000)
    BENCH_WARMUP    – number of warm‑up iterations (default: 10_000)

The script prints a short report with the average time per iteration for each method.
"""

import os
import time
from typing import List

# Configuration from environment variables
ITERATIONS = int(os.getenv("BENCH_ITERATIONS", "100000"))
WARMUP = int(os.getenv("BENCH_WARMUP", "10000"))

# Generate test data: a list of random floats
import random
random.seed(0)
values: List[float] = [random.random() * 1e6 for _ in range(ITERATIONS + WARMUP)]

def benchmark_fstring(vals: List[float]) -> float:
    """Benchmark Python f‑string formatting.
    Returns the average time per iteration in microseconds.
    """
    # Warm‑up
    for v in vals[:WARMUP]:
        _ = f"{v:.6f}"
    start = time.perf_counter()
    for v in vals[WARMUP:]:
        _ = f"{v:.6f}"
    elapsed = time.perf_counter() - start
    return (elapsed / ITERATIONS) * 1e6

# Optional: use {fmt} if the Python bindings are installed.
# The bindings are typically imported as `import fmt`.
try:
    import fmt  # type: ignore
    HAVE_FMT = True
except Exception:
    HAVE_FMT = False


def benchmark_fmt(vals: List[float]) -> float:
    """Benchmark {fmt} library formatting (if available).
    Returns the average time per iteration in microseconds.
    """
    if not HAVE_FMT:
        raise RuntimeError("{fmt} Python bindings not available")
    # Warm‑up
    for v in vals[:WARMUP]:
        _ = fmt.format("{:.6f}", v)
    start = time.perf_counter()
    for v in vals[WARMUP:]:
        _ = fmt.format("{:.6f}", v)
    elapsed = time.perf_counter() - start
    return (elapsed / ITERATIONS) * 1e6


def main() -> None:
    print(f"Benchmarking float formatting ({ITERATIONS} iterations, {WARMUP} warm‑up)" )
    fstring_time = benchmark_fstring(values)
    print(f"Python f‑string average time: {fstring_time:.2f} µs per iteration")
    if HAVE_FMT:
        fmt_time = benchmark_fmt(values)
        print(f"{{fmt}} average time: {fmt_time:.2f} µs per iteration")
    else:
        print("{fmt} Python bindings not found – skipping {fmt} benchmark.")


if __name__ == "__main__":
    main()
