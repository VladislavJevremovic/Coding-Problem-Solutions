# https://www.hackerrank.com/challenges/jesse-and-cookies/problem
# HackerRank: Jesse and Cookies

from heapq import heapify, heappop, heappush


def cookies(k, A):
    """Min-heap greedily combines the two least-sweet cookies until the minimum reaches k."""
    # Time: O(n log n)   Space: O(n)
    heap = list(A)
    heapify(heap)

    op_count = 0
    while heap and heap[0] < k:
        if len(heap) < 2:
            return -1
        c1 = heappop(heap)
        c2 = heappop(heap)
        heappush(heap, (1 * c1) + (2 * c2))
        op_count += 1

    return op_count


def test():
    # Classic HackerRank sample: expected 2 operations.
    assert cookies(7, [1, 2, 3, 9, 10, 12]) == 2
    # Already satisfied -> zero operations.
    assert cookies(5, [5, 6, 7]) == 0
    # Impossible: a single cookie below k can never be combined.
    assert cookies(10, [1]) == -1
    # Impossible: two cookies combine but can't reach k.
    assert cookies(100, [1, 1]) == -1
    # Two cookies that do reach the threshold in one op: 1 + 2*2 = 5 >= 4.
    assert cookies(4, [1, 2]) == 1
