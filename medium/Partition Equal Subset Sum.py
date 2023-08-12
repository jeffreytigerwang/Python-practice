# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = set()

        # Base case: sum of not selecting any value
        dp.add(0)

        for i in range(len(nums)):
            # Update dp.
            # temp = all possible sum after adding nums[i]

            # if nums = [1,2,3]          add 2                  add 3
            # dp = (0) --> (0, 1) -> (0, 1, 2, 3) --> (0, 1, 2, 3, 4, 5, 6)
            temp = set()

            for num in dp:
                if num + nums[i] == target:
                    return True

                temp.add(nums[i] + num)
                temp.add(num)

            dp = temp

        return False

