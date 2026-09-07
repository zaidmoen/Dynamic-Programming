"""Fibonacci implementations that introduce the two core DP styles."""

from functools import lru_cache


def fibonacci_memoized(n: int) -> int:
    """Return F(n) with top-down memoization.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def solve(value: int) -> int:
        if value < 2:
            return value
        return solve(value - 1) + solve(value - 2)

    return solve(n)


def fibonacci_tabulated(n: int) -> int:
    """Return F(n) with bottom-up, constant-space tabulation.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


if __name__ == "__main__":
    for index in range(11):
        print(f"F({index}) = {fibonacci_tabulated(index)}")
