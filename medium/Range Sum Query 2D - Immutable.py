# https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List


# Solution1 - Prefix sum for each row (1D)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = matrix.copy()

        for r in range(len(matrix)):
            for c in range(1, len(matrix[0])):
                self.prefixSum[r][c] += matrix[r][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.prefixSum[r][col2]
            if col1 > 0:
                res -= self.prefixSum[r][col1 - 1]

        return res


# Solution2 - Prefix sum 2D
class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        # +1 for padding: top row and leftmost column are all 0s
        self.prefixSum = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            prefix = 0

            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                above = self.prefixSum[r][c + 1]
                self.prefixSum[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixSum[row2][col2]
        top = self.prefixSum[row1 - 1][col2]
        left = self.prefixSum[row2][col1 - 1]
        topLeft = self.prefixSum[row1 - 1][col1 - 1]

        return bottomRight - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)