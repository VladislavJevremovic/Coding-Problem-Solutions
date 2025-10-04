# https://www.hackerrank.com/challenges/zig-zag-sequence/problem
# HackerRank: Zig Zag Sequence
from typing import List


def find_zig_zag_sequence(a: List[int]) -> List[int]:
    """Rearrange into a zig-zag: ascending to the middle (the max), then descending."""
    # Time: O(n log n)   Space: O(n)
    a = sorted(a)
    n = len(a)
    mid = (n + 1) // 2 - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st, ed = mid + 1, n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1
    return a


def test() -> None:
    assert find_zig_zag_sequence([2, 3, 5, 1, 4]) == [1, 2, 5, 4, 3]
    assert find_zig_zag_sequence([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 7, 6, 5, 4]
