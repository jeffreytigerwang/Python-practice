# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List

# Hard
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for n in nums:
            if k < 2 or n != nums[k - 2]:
                nums[k] = n
                k += 1

        return k

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            count = 1

            while r < len(nums) - 1 and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            # update to a distinct value
            r += 1

        return l


sol = Solution()
nums = [1,1,1,2,3]
sol.removeDuplicates(nums)