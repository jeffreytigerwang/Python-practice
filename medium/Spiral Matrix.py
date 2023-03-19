# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # https://leetcode.com/problems/spiral-matrix/solutions/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget/
        if not matrix:
            return []

        res = []

        # top = 0
        # bottom = len(matrix) - 1
        #
        # left = 0
        # right = len(matrix[0]) - 1
        #
        # #   Approach 1
        # while left <= right and top <= bottom:
        #     for column in range(left, right + 1):
        #         res.append(matrix[top][column])
        #     top += 1
        #
        #     for row in range(top, bottom + 1):
        #         res.append(matrix[row][right])
        #     right -= 1
        #
        #     for column in reversed(range(left, right + 1)):
        #         res.append(matrix[bottom][column])
        #     bottom -= 1
        #
        #     for row in reversed(range(top, bottom + 1)):
        #         res.append(matrix[row][left])
        #     left += 1
        #
        # return res[:len(matrix) * len(matrix[0])]


        #Approach 2
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return res