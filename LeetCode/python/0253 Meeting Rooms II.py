# https://leetcode.com/problems/meeting-rooms-ii/

import heapq
import math
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        rooms = [-math.inf]  # end_time for each room
        for meeting in intervals:
            if rooms[0] <= meeting[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meeting[1])

        return len(rooms)


def test():
    s = Solution()
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
