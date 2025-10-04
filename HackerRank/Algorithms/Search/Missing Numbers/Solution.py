# https://www.hackerrank.com/challenges/missing-numbers/problem
# HackerRank: Missing Numbers


def missingNumbers(arr: list[int], brr: list[int]) -> list[int]:
    """Return the sorted distinct values whose count in brr exceeds that in arr."""
    # Time: O(n log n)   Space: O(n)
    d: dict[int, int] = {}

    for b in brr:
        if b not in d:
            d[b] = 0
        d[b] += 1

    for a in arr:
        if a not in d:
            d[a] = 0
        d[a] -= 1

    return sorted([k for k, v in d.items() if v != 0])


def test():
    # brr has two 204s and two 206s that arr lacks once each.
    arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
    # brr counts: 203:2,204:3,205:3,206:3,207:1,208:1
    # arr counts: 203:2,204:2,205:2,206:2,207:1,208:1
    # leftover:   204:1,205:1,206:1
    assert missingNumbers(arr, brr) == [204, 205, 206]
    # Identical multisets -> nothing missing.
    assert missingNumbers([1, 2, 3], [1, 2, 3]) == []
    # One extra element in brr.
    assert missingNumbers([7], [7, 7]) == [7]
