# https://www.hackerrank.com/challenges/recursion-fibonacci-numbers/problem
# HackerRank: Recursion - Fibonacci Numbers


def fibonacci(n: int) -> int:
    """Iterate the recurrence, keeping the last two values to build fib(n)."""
    # Time: O(n)   Space: O(1)
    if n < 2:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def test() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(10) == 55
