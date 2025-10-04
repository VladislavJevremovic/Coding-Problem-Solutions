"""Small test helpers shared across solutions, such as order-insensitive compare."""

from typing import List, TypeVar

T = TypeVar("T")


def sorted_list_of_lists(list_of_lists: List[List[T]]) -> List[List[T]]:
    """Sort each inner list and then the outer list for order-insensitive equality."""
    return sorted([sorted(list) for list in list_of_lists])
