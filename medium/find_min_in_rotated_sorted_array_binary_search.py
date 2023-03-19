# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List



class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        #
        # l = 0
        # r = len(nums) - 1
        #
        # while l <= r:
        #     mid = l + (r - l) // 2
        #
        #     if nums[mid] < nums[mid - 1]:
        #         return nums[mid]
        #
        #     if mid < len(nums) - 1:
        #         if nums[mid] > nums[mid + 1]:
        #             return nums[mid + 1]
        #
        #     if nums[l] < nums[l - 1]:
        #         return nums[l]
        #     if l < len(nums) - 1:
        #         if nums[l] > nums[l + 1]:
        #             return nums[l + 1]
        #
        #     if nums[r] < nums[r - 1]:
        #         return nums[r]
        #     if r < len(nums) - 1:
        #         if nums[r] > nums[r + 1]:
        #             return nums[r + 1]
        #
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #
        #     if nums[mid] < nums[r]:
        #         r = mid - 1
        #
        # return nums[0]

        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1
        minNum = float("inf")

        while l <= r:
            mid = l + (r - l) // 2
            minNum = min(minNum, nums[mid])

            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return min(minNum, nums[0])


