from typing import List, TypeVar

T = TypeVar('T')


def sorted_list_of_lists(list_of_lists: List[List[T]]) -> List[List[T]]:
    return sorted([sorted(list) for list in list_of_lists])
