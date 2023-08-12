# https://leetcode.com/problems/move-zeroes/
from typing import List

# Slow
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return

        l = 0

        for r in range(len(nums)):
            if nums[r] != 0 and nums[l] == 0:
                nums[r], nums[l] = nums[l], nums[r]

            if nums[l] != 0:
                l += 1