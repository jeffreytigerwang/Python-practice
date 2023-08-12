# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        nums.sort()

        left = 0
        right = left + k - 1
        res = float('inf')

        while right < len(nums):
            res = min(res, nums[right] - nums[left])
            right += 1
            left += 1

        return res