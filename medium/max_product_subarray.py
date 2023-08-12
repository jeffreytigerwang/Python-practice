# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tempMax = 1
        tempMin = 1
        res = nums[0]

        for n in nums:
            # Keep both max and min of the substring to handle negatives
            # tempMax, tempMin = max(tempMax * n, tempMin * n, n), min(tempMax * n, tempMin * n, n)

            temp = tempMin * n

            tempMin = min(tempMax * n, temp, n)
            tempMax = max(tempMax * n, temp, n)

            res = max(res, tempMax)


        return res



answer = Solution()
nums = [3, -1, 4]
print(answer.maxProduct(nums))

