# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [i for i in range(0, len(nums) + 1)]

        for i in range(len(nums)):
            res[nums[i]] = 0

        res = [i for i in res if i != 0]

        return res

