# https://leetcode.com/problems/find-pivot-index/
from typing import List

# Both solutions have same time complexity
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(0, len(nums)):
            if i > 0:
                left += nums[i]

            right -= nums[i]

            if left == right:
                return i

        return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)  # O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
