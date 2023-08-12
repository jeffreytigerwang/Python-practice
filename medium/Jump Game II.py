# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP
        #
        # dp = [len(nums)] * len(nums)
        # dp[0] = 0
        #
        # for i in range(len(nums)):
        #     for j in range(1, nums[i] + 1):
        #         if i + j < len(nums):
        #             dp[i + j] = min(dp[i + j], dp[i] + 1)
        #
        # return dp[-1]
        #

        # Greedy

        res = 0

        # Left and right pointer; used to determine the interval of possible index
        l = 0
        r = 0

        # guaranteed to reach destination
        while r < len(nums) - 1:
            temp = 0

            for i in range(l, r + 1):
                temp = max(temp, i + nums[i])

            l += 1
            r = temp
            res += 1

        return res

