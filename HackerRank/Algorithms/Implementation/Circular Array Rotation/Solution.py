# https://www.hackerrank.com/challenges/circular-array-rotation/problem
# HackerRank: Circular Array Rotation
from typing import List


def circular_array_rotation(a: List[int], k: int, queries: List[int]) -> List[int]:
    """Map each query index back to its pre-rotation source index (q - k) mod n."""
    # Time: O(q)   Space: O(1)  (q = number of queries)
    n = len(a)
    k %= n
    # After rotating right by k, element at index q came from index (q - k) mod n.
    return [a[(q - k) % n] for q in queries]


def test() -> None:
    assert circular_array_rotation([3, 4, 5], 2, [1, 2]) == [5, 3]
    assert circular_array_rotation([1, 2, 3], 0, [0, 1, 2]) == [1, 2, 3]
    assert circular_array_rotation([1, 2, 3, 4], 4, [0, 3]) == [1, 4]
