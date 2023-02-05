# https://leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True

        rooms_to_visit = [0]  # DFS (queue for BFS)
        while rooms_to_visit:
            room_to_visit = rooms_to_visit.pop()
            for another_room in rooms[room_to_visit]:
                if not visited[another_room]:
                    visited[another_room] = True
                    rooms_to_visit.append(another_room)

        return all(visited)


def test():
    s = Solution()
    assert s.canVisitAllRooms([[1], [2], [3], []]) is True
    assert s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
