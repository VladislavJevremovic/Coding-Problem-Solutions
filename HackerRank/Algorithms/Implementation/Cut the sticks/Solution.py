# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# HackerRank: Cut the sticks


def cut_the_sticks(arr: list[int]) -> list[int]:
    """Repeatedly record stick count, then cut every stick by the current shortest."""
    # Time: O(n^2)   Space: O(n)
    result: list[int] = []
    sticks = sorted((x for x in arr if x > 0), reverse=True)
    while sticks:
        result.append(len(sticks))
        shortest = sticks[-1]
        sticks = [x - shortest for x in sticks if x - shortest > 0]
    return result


def test() -> None:
    assert cut_the_sticks([5, 4, 4, 2, 2, 8]) == [6, 4, 2, 1]
    assert cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]) == [8, 6, 4, 1]
    # Edge: all equal -> one cut removes everything
    assert cut_the_sticks([3, 3, 3]) == [3]
    # Edge: empty
    assert cut_the_sticks([]) == []
