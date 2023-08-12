# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List

# Prefix sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {}   # remainder --> end index
        remainderMap[0] = -1    # make sure the first element (if divisible by k) will not return True
        temp = 0

        for i, n in enumerate(nums):
            temp += n
            remainder = temp % k

            if remainder not in remainderMap:
                remainderMap[remainder] = i
            elif i - remainderMap[remainder] > 1:
                return True

        return False

