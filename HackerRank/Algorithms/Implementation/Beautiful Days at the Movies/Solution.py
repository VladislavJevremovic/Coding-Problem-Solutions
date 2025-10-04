# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# HackerRank: Beautiful Days at the Movies
def beautiful_days(i: int, j: int, k: int) -> int:
    """Count days in [i, j] where |day - reverse(day)| is divisible by k."""
    # Time: O((j - i) * d)   Space: O(d)  (d = digits per day)
    return sum(1 for day in range(i, j + 1) if abs(day - int(str(day)[::-1])) % k == 0)


def test() -> None:
    assert beautiful_days(20, 23, 6) == 2  # 20 and 22
    assert beautiful_days(13, 45, 3) == 33
