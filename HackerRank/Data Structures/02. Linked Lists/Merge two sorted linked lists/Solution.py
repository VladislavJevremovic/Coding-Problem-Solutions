# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
# HackerRank: Merge two sorted linked lists


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
    return head


def _to_list(head):
    out = []
    while head is not None:
        out.append(head.data)
        head = head.next
    return out


def mergeLists(head1, head2):
    """Merge two sorted lists by splicing the smaller head onto a dummy-anchored tail."""
    # Time: O(m + n)   Space: O(1)
    dummy_head = SinglyLinkedListNode(0)
    merged_so_far = dummy_head

    while head1 is not None or head2 is not None:
        if head1 is None:
            merged_so_far.next = head2
            break
        elif head2 is None:
            merged_so_far.next = head1
            break
        else:
            if head1.data < head2.data:
                merged_so_far.next = head1
                head1 = head1.next
            else:
                merged_so_far.next = head2
                head2 = head2.next
        merged_so_far = merged_so_far.next

    return dummy_head.next


def test():
    # Interleaving merge.
    a = _build_list([1, 3, 5, 6])
    b = _build_list([2, 4, 7])
    assert _to_list(mergeLists(a, b)) == [1, 2, 3, 4, 5, 6, 7]
    # One empty list returns the other.
    assert _to_list(mergeLists(None, _build_list([1, 2]))) == [1, 2]
    assert _to_list(mergeLists(_build_list([9]), None)) == [9]
    # Both empty.
    assert _to_list(mergeLists(None, None)) == []
    # Duplicates across both lists are preserved.
    assert _to_list(mergeLists(_build_list([2, 2]), _build_list([2]))) == [2, 2, 2]
