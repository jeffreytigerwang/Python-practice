# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # if not matrix:
        #     return []
        #
        # left = 0
        # right = len(matrix[0]) - 1
        # top = 0
        # bottom = len(matrix) - 1
        # res = []
        #
        # while left < right and top < bottom:
        #     res.extend(matrix[top][left: right])
        #     res.extend(col[right] for col in matrix[top: bottom])
        #     res.extend(matrix[bottom][right: left: -1])
        #     res.extend(col[left] for col in matrix[bottom: top: -1])
        #
        #     left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        #
        # # Handle edge case - center
        # for row in range(top, bottom + 1):
        #     for col in range(left, right + 1):
        #         res.append(matrix[row][col])
        #
        # return res

        res = []

        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]

        return res