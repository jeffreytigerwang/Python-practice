# https://leetcode.com/problems/majority-element/
from typing import List
from collections import Counter


# Space complexity O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2

        temp = Counter(nums)

        for key in temp.keys():
            if temp[key] > n:
                return key

        # return max(temp, key=temp.get)


# Space complexity O(1)

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n

            if n == res:
                count += 1
            else:
                count -= 1

        return res