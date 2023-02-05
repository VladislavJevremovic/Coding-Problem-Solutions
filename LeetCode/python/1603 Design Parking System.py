# https://leetcode.com/problems/design-parking-system/
from typing import List, Optional


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        else:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False


def test():
    def case(actions: List[str], params: List[List[int]], expected: List[Optional[bool]]) -> bool:
        actual = []
        s = None
        for action, param in zip(actions, params):
            if action == "ParkingSystem":
                s = ParkingSystem(param[0], param[1], param[2])
                actual.append(None)
            elif action == "addCar":
                actual.append(s.addCar(param[0]))

        return actual == expected

    assert case(
        ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
        [[1, 1, 0], [1], [2], [3], [1]],
        [None, True, True, False, False]
    )
