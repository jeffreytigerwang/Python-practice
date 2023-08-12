# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

sol.removeDuplicates(nums)