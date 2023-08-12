# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd algorithm for cycle detection
        # Consider value as pointer

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow2 == slow:
                return slow


