# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # # memo
        # memo = [-1 for i in range(len(nums) + 1)]
        #
        # def recursion(tempList, currIndex):
        #     if currIndex < 0:
        #         return 0
        #
        #     if memo[currIndex] >= 0:
        #         return memo[currIndex]
        #
        #     res = max(recursion(tempList, currIndex - 2) + nums[currIndex], recursion(tempList, currIndex - 1))
        #     memo[currIndex] = res
        #
        #     return res
        #
        # res = recursion(nums, len(nums) - 1)
        # # print(memo)
        # # print(res)
        #
        # return res
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]

def main():
    sol = Solution()
    nums = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
    sol.rob(nums)

if __name__ == "__main__":
    main()