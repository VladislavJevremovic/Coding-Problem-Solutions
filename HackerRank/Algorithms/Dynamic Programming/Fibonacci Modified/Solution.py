# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# HackerRank: Fibonacci Modified


def fibonacci_modified(t1: int, t2: int, n: int) -> int:
    """t(i) = t(i-2) + t(i-1)**2. Return the n-th term (1-indexed)."""
    # Time: O(n)   Space: O(1)
    a, b = t1, t2
    for _ in range(2, n):
        a, b = b, a + b * b
    return b


def test() -> None:
    # terms: t1=0, t2=1, t3=1, t4=2, t5=5, t6=27, t7=734, ...
    assert fibonacci_modified(0, 1, 3) == 1
    assert fibonacci_modified(0, 1, 4) == 2
    assert fibonacci_modified(0, 1, 5) == 5
    assert fibonacci_modified(0, 1, 6) == 27
    assert fibonacci_modified(0, 1, 7) == 734
    assert fibonacci_modified(0, 1, 10) == 84266613096281243382112
