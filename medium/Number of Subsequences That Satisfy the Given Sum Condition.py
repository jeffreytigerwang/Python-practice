# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = 0
        mod = 10 ** 9 + 7
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 1 << (r - l)
                l += 1

        return res % mod


