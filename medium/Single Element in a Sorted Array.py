# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List

# Suppose array is [1, 1, 2, 2, 3, 3, 4, 5, 5]
# we can observe that for each pair,
# first element takes even position and second element takes odd position
# for example, 1 is appeared as a pair,
# so it takes 0 and 1 positions. similarly for all the pairs also.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (r - l) // 2 + l

            # check for 1. in bound; 2. odd or even; 3. first of second element in pair
            if (mid - 1 >= 0 and mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid + 1 < n and mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                l = mid + 1
            else:
                r = mid - 1

        # has to be l
        return nums[l]


class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid

        # either left or right would work
        return nums[left]