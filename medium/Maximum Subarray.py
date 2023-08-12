# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        temp = 0

        for n in nums:
            temp += n
            res = max(res, temp)

            if temp < 0:
                temp = 0

        return res