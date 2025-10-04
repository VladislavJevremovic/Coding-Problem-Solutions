"""Unit tests for the shared Helpers package.

These utilities are exercised indirectly by every tree/linked-list solution,
but the tests here pin down their contracts directly so a regression in a
builder or comparison shows up as a focused failure.
"""

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree
from python.Helpers.DoublyLinkedList import DoublyLinkedList, DoublyLinkedNode
from python.Helpers.Functions import sorted_list_of_lists
from python.Helpers.SinglyLinkedList import SinglyLinkedList, SinglyLinkedNode


def test_singly_linked_list_round_trip():
    assert SinglyLinkedList.from_sequence([1, 2, 3]).to_list() == [1, 2, 3]
    assert SinglyLinkedList.from_sequence([]).to_list() == []
    assert SinglyLinkedList(SinglyLinkedNode(7)).to_list() == [7]


def test_singly_linked_list_equality():
    assert SinglyLinkedList.from_sequence([1, 2]) == SinglyLinkedList.from_sequence(
        [1, 2]
    )
    assert SinglyLinkedList.from_sequence([1, 2]) != SinglyLinkedList.from_sequence(
        [2, 1]
    )
    assert SinglyLinkedList.from_sequence([1]) != 123  # NotImplemented path


def test_binary_search_tree_level_order_round_trip():
    tree = BinarySearchTree.from_level_order_sequence([1, 2, 3, None, 4])
    assert tree.to_level_order() == [1, 2, 3, None, 4]
    assert tree.in_order() == [2, 4, 1, 3]


def test_binary_search_tree_equality_is_structural():
    assert BinarySearchTree.from_level_order_sequence(
        [4, 2, 7]
    ) == BinarySearchTree.from_level_order_sequence([4, 2, 7])
    # Same values, different shapes must not compare equal.
    assert BinarySearchTree.from_level_order_sequence(
        [1, 2]
    ) != BinarySearchTree.from_level_order_sequence([1, None, 2])


def test_binary_search_tree_empty():
    assert BinarySearchTree.from_level_order_sequence([]) is None
    assert BinarySearchTree(BinarySearchNode(5)).to_level_order() == [5]


def test_doubly_linked_list_head_tail_ops():
    dll = DoublyLinkedList()
    assert dll.is_empty()

    a = dll.add_value_to_tail(1)
    b = dll.add_value_to_tail(2)
    assert not dll.is_empty()
    assert dll.first_value() == 1

    dll.move_node_to_head(b)
    assert dll.first_value() == 2

    popped = dll.pop_tail()
    assert popped is a
    assert dll.first_value() == 2


def test_doubly_linked_list_remove():
    dll = DoublyLinkedList()
    node = DoublyLinkedNode(value=42)
    dll.add_node_to_head(node)
    assert dll.first_value() == 42
    dll.remove_node(node)
    assert dll.is_empty()


def test_sorted_list_of_lists():
    assert sorted_list_of_lists([[3, 1], [2]]) == [[1, 3], [2]]
    assert sorted_list_of_lists([]) == []
