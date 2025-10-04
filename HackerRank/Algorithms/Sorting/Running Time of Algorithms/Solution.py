# https://www.hackerrank.com/challenges/running-time-of-algorithms/problem
# HackerRank: Running Time of Algorithms


def running_time(arr: list[int]) -> int:
    """Run insertion sort and return the number of shifts performed."""
    # Time: O(n^2)   Space: O(n)
    a = list(arr)
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        p = i
        while p > 0 and a[p - 1] > key:
            shifts += 1
            a[p] = a[p - 1]
            p -= 1
        a[p] = key
    return shifts


def test() -> None:
    # [2,1,3,1,2] -> shifts: classic HackerRank sample answer is 4.
    assert running_time([2, 1, 3, 1, 2]) == 4
    # Already sorted -> no shifts.
    assert running_time([1, 2, 3, 4, 5]) == 0
    # Reverse sorted of length 4 -> 1+2+3 = 6 shifts.
    assert running_time([4, 3, 2, 1]) == 6
    # Edge case: single element -> no shifts.
    assert running_time([7]) == 0
