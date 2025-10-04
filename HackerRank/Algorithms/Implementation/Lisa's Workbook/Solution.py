# HackerRank: Lisa's Workbook
import math


def workbook(n: int, k: int, arr: list[int]) -> int:
    """Walk every page, counting those whose number falls in its problem range."""
    # Time: O(total pages)   Space: O(1)
    # A problem is "special" when its problem number equals the (global) page
    # it appears on. Pages hold at most k problems each.
    special = 0
    page = 0
    for problem_count in arr:
        pages_in_chapter = math.ceil(problem_count / k)
        for p in range(pages_in_chapter):
            page += 1
            first = p * k + 1
            last = min((p + 1) * k, problem_count)
            if first <= page <= last:
                special += 1
    return special


def test() -> None:
    # Classic sample: 5 chapters, k=3
    assert workbook(5, 3, [4, 2, 6, 1, 10]) == 4
    # Single chapter, one problem on page 1 -> special
    assert workbook(1, 5, [1]) == 1
    # k larger than problems, page 1 holds problems 1..2 -> problem 1 special
    assert workbook(1, 100, [2]) == 1
    # Edge: empty
    assert workbook(0, 5, []) == 0
