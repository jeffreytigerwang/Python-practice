# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # res = 0
        #
        # for i in range(len(nums)):
        #     res += i - nums[i]
        #
        # return res + len(nums)

        # Bit manipulation - XOR --> order doesn't matter
        res = 0

        for index, num in enumerate(nums):
            res = res ^ index ^ num

        return res ^ len(nums)
