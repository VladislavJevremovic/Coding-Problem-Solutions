# https://www.hackerrank.com/challenges/find-digits/problem
# HackerRank: Find Digits
def find_digits(n: int) -> int:
    """Count nonzero digits of n that divide n evenly."""
    # Time: O(d)   Space: O(d)  (d = number of digits in n)
    return sum(1 for ch in str(n) if ch != "0" and n % int(ch) == 0)


def test() -> None:
    assert find_digits(12) == 2
    assert find_digits(1012) == 3  # 1, 1, 2 divide 1012; 0 skipped
    assert find_digits(1024) == 3  # 1, 2, 4 all divide 1024; 0 skipped
    assert find_digits(24) == 2
