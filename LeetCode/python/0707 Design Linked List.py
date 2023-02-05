# https://leetcode.com/problems/design-linked-list/

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()  # sentinel node as pseudo-head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index + 1):  # + 1 for sentinel
            current = current.next

        return current.val

    def add_at_head(self, val: int) -> None:
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int) -> None:
        if index > self.size:
            return

        self.size += 1

        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        to_add = ListNode(val)

        # insert
        to_add.next = predecessor.next
        predecessor.next = to_add

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        predecessor.next = predecessor.next.next


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[int]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "MyLinkedList":
                s = MyLinkedList()
                actual.append(None)
            elif action == "get":
                actual.append(s.get(param[0]))
            elif action == "addAtHead":
                s.add_at_head(param[0])
                actual.append(None)
            elif action == "addAtTail":
                s.add_at_tail(param[0])
                actual.append(None)
            elif action == "addAtIndex":
                s.add_at_index(param[0], param[1])
                actual.append(None)
            elif action == "deleteAtIndex":
                s.delete_at_index(param[0])
                actual.append(None)

        return actual == expected

    assert case(
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
        [[], [1], [3], [1, 2], [1], [1], [1]],
        [None, None, None, None, 2, None, 3]
    )
    assert case(
        ["MyLinkedList", "addAtHead", "addAtHead", "get"],
        [[], [2], [1], [0]],
        [None, None, None, 1]
    )
    assert case(
        ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtHead", "deleteAtIndex", "addAtHead", "get", "get",
         "get", "addAtHead", "deleteAtIndex"],
        [[], [4], [1], [1], [5], [3], [7], [3], [3], [3], [1], [4]],
        [None, None, -1, None, None, None, None, 4, 4, 4, None, None]
    )
