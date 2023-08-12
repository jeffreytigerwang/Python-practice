# https://leetcode.com/problems/4sum/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(nums, N, target, result):
            if len(nums) < N or N < 2 or nums[-1] * N < target or nums[0] * N > target:
                return

            if N == 2:
                l = 0
                r = len(nums) - 1

                while l < r:
                    temp = nums[l] + nums[r]

                    if temp == target:
                        results.append(result + [nums[l]] + [nums[r]])

                        l += 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif temp > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        NSum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]])

        nums.sort()
        results = []
        NSum(nums, 4, target, [])
        return results
