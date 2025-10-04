# https://www.hackerrank.com/challenges/find-merge-point-of-two-lists/problem
# HackerRank: Find Merge Point of Two Lists


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def _build_list(values):
    head = None
    tail = None
    for v in values:
        node = SinglyLinkedListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head, tail


def findMergeNode(head1, head2):
    """Two pointers swap to the other head at each end so they align at the merge node."""
    # Time: O(m + n)   Space: O(1)
    current1 = head1
    current2 = head2

    while current1 != current2:
        current1 = head2 if current1.next is None else current1.next
        current2 = head1 if current2.next is None else current2.next

    return current2.data


def test():
    # Build a shared tail and two distinct heads pointing into it.
    common_head, common_tail = _build_list([7, 8, 9])  # merge node value 7

    a_head, a_tail = _build_list([1, 2, 3])
    a_tail.next = common_head

    b_head, b_tail = _build_list([4, 5])
    b_tail.next = common_head

    assert findMergeNode(a_head, b_head) == 7

    # Lists of equal length before the merge.
    common2, _ = _build_list([100])
    x_head, x_tail = _build_list([1])
    x_tail.next = common2
    y_head, y_tail = _build_list([2])
    y_tail.next = common2
    assert findMergeNode(x_head, y_head) == 100

    # Merge at the very first node (heads are the same).
    z_head, _ = _build_list([42, 43])
    assert findMergeNode(z_head, z_head) == 42
