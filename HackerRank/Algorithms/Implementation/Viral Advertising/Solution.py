# https://www.hackerrank.com/challenges/strange-advertising/problem
# HackerRank: Viral Advertising
def viral_advertising(n: int) -> int:
    """Simulate n days: half of shares like it, each liker reshares to three more."""
    # Time: O(n)   Space: O(1)
    shared = 5
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


def test() -> None:
    assert viral_advertising(1) == 2
    assert viral_advertising(2) == 5
    assert viral_advertising(3) == 9
    assert viral_advertising(5) == 24
