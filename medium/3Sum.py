# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def NSum(nums, N, target, result, results):
            if N < 2 or N > len(nums) or N * nums[0] > target or N * nums[-1] < target:
                return

            if N == 2:
                l = 0
                r = len(nums) - 1

                while l < r:
                    sum = nums[l] + nums[r]

                    if sum == target:
                        results.append(result + [nums[l]] + [nums[r]])

                        l += 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif sum > target:
                        r -= 1

                    else:
                        l += 1

            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        NSum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)

        nums.sort()
        res = []
        NSum(nums, 3, 0, [], res)

        return res