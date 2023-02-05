# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def floodFillRec(image: List[List[int]], sr: int, sc: int, newColor: int, targetColor: int) -> List[List[int]]:
            if image[sr][sc] == newColor:
                return image

            if image[sr][sc] != targetColor:
                return image

            image[sr][sc] = newColor

            if sr + 1 < len(image):
                floodFillRec(image, sr + 1, sc, newColor, targetColor)
            if sc + 1 < len(image[0]):
                floodFillRec(image, sr, sc + 1, newColor, targetColor)
            if sr - 1 >= 0:
                floodFillRec(image, sr - 1, sc, newColor, targetColor)
            if sc - 1 >= 0:
                floodFillRec(image, sr, sc - 1, newColor, targetColor)

            return image

        return floodFillRec(image, sr, sc, newColor, image[sr][sc])


def test():
    s = Solution()
    assert s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2) == [[2, 2, 2], [2, 2, 2]]
