# https://www.hackerrank.com/challenges/gemstones/problem
# HackerRank: Gemstones


def gemstones(arr: list[str]) -> int:
    """Return the count of characters present in every string in arr."""
    # Time: O(n)   Space: O(1)
    if not arr:
        return 0
    common = set(arr[0])
    for s in arr[1:]:
        common &= set(s)
    return len(common)


def test() -> None:
    assert gemstones(["abcdde", "baccd", "eeabg"]) == 2  # 'a' and 'b'
    assert gemstones(["abc", "abc", "abc"]) == 3
    assert gemstones(["abc", "xyz"]) == 0
    # Edge case: single rock -> all its distinct chars are gems.
    assert gemstones(["aabbc"]) == 3
