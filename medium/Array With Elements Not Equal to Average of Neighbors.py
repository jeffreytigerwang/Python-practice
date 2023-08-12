# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
from typing import List

# Instead of compute all permutation (with backtracking), sort the list
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = []
        l, r = 0, len(nums) - 1

        while l <= r:
            res.append(nums[l])
            l += 1

            res.append(nums[r])
            r -= 1

        return res[:len(nums)]



class Solution1:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = []
        l, r = 0, len(nums) - 1

        while len(nums) != len(res):
            res.append(nums[l])
            l += 1

            # avoids duplicates
            if l <= r:
                res.append(nums[r])
                r -= 1

        return res