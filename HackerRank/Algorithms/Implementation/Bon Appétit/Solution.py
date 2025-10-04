# HackerRank: Bon Appétit
from typing import List, Union


def bon_appetit(bill: List[int], k: int, charged: int) -> Union[str, int]:
    """Compare charged amount to Anna's fair half-share of the bill minus item k."""
    # Time: O(n)   Space: O(1)
    # Anna did not eat item k; her fair share is half of everything else.
    fair_share = (sum(bill) - bill[k]) // 2
    if charged == fair_share:
        return "Bon Appetit"
    return charged - fair_share


def test() -> None:
    assert bon_appetit([3, 10, 2, 9], 1, 12) == 5
    assert bon_appetit([3, 10, 2, 9], 1, 7) == "Bon Appetit"
