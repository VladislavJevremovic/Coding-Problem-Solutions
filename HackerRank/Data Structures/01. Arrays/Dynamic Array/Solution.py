# https://www.hackerrank.com/challenges/dynamic-array/problem
# HackerRank: Dynamic Array


def dynamic_array(n, queries):
    """Route each query into one of n buckets via a running xor'd index, appending or reading."""
    # Time: O(q)   Space: O(n + total appended)  (q = number of queries)
    r = []
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    for query in queries:
        (c, x, y) = (query[0], query[1], query[2])
        if c == 1:
            seq_list[(x ^ last_answer) % n].append(y)
        elif c == 2:
            seq = seq_list[(x ^ last_answer) % n]
            size = len(seq)
            last_answer = seq[y % size]
            r.append(last_answer)

    return r


def test():
    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1],
    ]
    # See module reasoning: type-2 queries yield 7 then 3.
    assert dynamic_array(2, queries) == [7, 3]
    # No type-2 queries -> no answers recorded.
    assert dynamic_array(1, [[1, 0, 9], [1, 0, 8]]) == []
    # Single bucket, last_answer stays 0 so xor is identity.
    assert dynamic_array(1, [[1, 0, 42], [2, 0, 0]]) == [42]
