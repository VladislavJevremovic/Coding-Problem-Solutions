# https://www.hackerrank.com/challenges/cycle-detection/problem
# HackerRank: Cycle Detection


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def _build_list(values):
    head = None
    tail = None
    nodes = []
    for v in values:
        node = SinglyLinkedListNode(v)
        nodes.append(node)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head, nodes


def has_cycle(head):
    """Floyd's tortoise-and-hare: a cycle exists iff the fast and slow pointers meet."""
    # Time: O(n)   Space: O(1)
    if not head:
        return 0

    slowp = head
    fastp = head

    while fastp and fastp.next:
        slowp = slowp.next
        fastp = fastp.next.next

        if slowp == fastp:
            return 1

    return 0


def test():
    # Empty list has no cycle.
    assert has_cycle(None) == 0
    # Acyclic list.
    head, _ = _build_list([1, 2, 3, 4])
    assert has_cycle(head) == 0
    # Single node, no self-loop.
    head, _ = _build_list([1])
    assert has_cycle(head) == 0
    # Cyclic list: tail points back to the second node.
    head, nodes = _build_list([1, 2, 3, 4])
    nodes[-1].next = nodes[1]
    assert has_cycle(head) == 1
    # Self-loop on a single node.
    head, nodes = _build_list([9])
    nodes[0].next = nodes[0]
    assert has_cycle(head) == 1
