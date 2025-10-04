# https://www.hackerrank.com/challenges/maximum-element/problem
# HackerRank: Maximum Element


class MaxStack:
    """Stack pairing each value with the running max so max() is O(1)."""

    # push: O(1)   pop: O(1)   max: O(1)   Space: O(n)

    def __init__(self):
        self._stack = []

    def push(self, x):
        current_max = self._stack[-1][1] if self._stack else 0
        self._stack.append((x, max(x, current_max)))

    def pop(self):
        return self._stack.pop()[0]

    def max(self):
        return self._stack[-1][1]

    def __len__(self):
        return len(self._stack)


def process_queries(queries):
    """Drive a MaxStack over [1,x]=push / [2]=pop / [3]=record-max queries."""
    # Time: O(q)   Space: O(n)  (q = number of queries, n = max stack depth)
    stack = MaxStack()
    out = []
    for query in queries:
        c = query[0]
        if c == 1:
            stack.push(query[1])
        elif c == 2:
            stack.pop()
        elif c == 3:
            out.append(stack.max())
    return out


def test():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.max() == 3
    assert s.pop() == 3
    assert s.max() == 2
    s.push(5)
    assert s.max() == 5

    # Query-driven interface matching the HackerRank sample.
    queries = [
        [1, 97],
        [2],
        [1, 20],
        [2],
        [1, 26],
        [1, 20],
        [2],
        [3],
        [1, 91],
        [3],
    ]
    # After pushes/pops: stack holds [26], max 26; then push 91, max 91.
    assert process_queries(queries) == [26, 91]

    # Maximum is unaffected by smaller subsequent pushes.
    assert process_queries([[1, 10], [1, 3], [3], [2], [3]]) == [10, 10]
