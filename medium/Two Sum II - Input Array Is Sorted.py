# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l + 1, r + 1]

            elif sum < target:
                l += 1
            else:
                r -= 1
