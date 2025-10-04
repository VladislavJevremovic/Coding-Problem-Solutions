# https://www.hackerrank.com/challenges/drawing-book/problem
# HackerRank: Drawing Book
def page_count(n: int, p: int) -> int:
    """Return the smaller of the flips needed from the front versus the back."""
    # Time: O(1)   Space: O(1)
    from_front = p // 2
    from_back = n // 2 - p // 2
    return min(from_front, from_back)


def test() -> None:
    assert page_count(6, 2) == 1
    assert page_count(5, 4) == 0
    assert page_count(6, 5) == 1  # page 5 is on the last sheet, 1 flip from the back
