# https://leetcode.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            # need row + 1 because we need to access the last element in this row
            # e.g, when len = 4; len - 2 = 2; row 2 has elements 6,5,7; we need index 0, 1, 2 to access all
            for col in range(0, row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]


class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle[-1]) + 1)

        for row in range(len(triangle) - 1, -1, -1):
            for col in range(0, row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]