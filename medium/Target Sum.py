# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # key = (index, current sum)

        def backtracking(index, total):
            if index >= len(nums):
                return 1 if total == target else 0

            if (index, total) in dp.keys():
                return dp[(index, total)]

            dp[(index, total)] = backtracking(index + 1, total + nums[index]) + backtracking(index + 1, total - nums[index])

            return dp[(index, total)]

        return backtracking(0, 0)

