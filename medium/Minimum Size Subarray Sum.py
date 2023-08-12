from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        sum = 0
        currLength = 0

        while r < len(nums):
            sum += nums[r]
            currLength += 1

            while sum >= target:
                res = min(res, currLength)
                sum -= nums[l]
                currLength -= 1
                l += 1

            r += 1

        return res if res < float('inf') else 0