# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Approach 1
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        #
        # def helper(nums):
        #     if len(nums) <= 1:
        #         return nums[0]
        #
        #     dp = [0] * len(nums)
        #     dp[0] = nums[0]
        #     dp[1] = max(nums[0], nums[1])
        #
        #     for i in range(2, len(nums)):
        #         dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        #
        #     return dp[-1]
        #
        # return max(helper(nums[1:]), helper(nums[:-1]))

        # Approach 2
        def helper(nums, i, j):
            rob = 0
            notRob = 0

            for index in range(i, j):
                num = nums[index]
                rob, notRob = num + notRob, max(rob, notRob)    # Equivalent to line 36 to 38
                # temp = rob
                # rob = num + notRob
                # notRob = max(temp, notRob)

            return max(rob, notRob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(helper(nums, 0, len(nums) - 1), helper(nums, 1, len(nums)))

def main():
    sol = Solution()
    nums = [0,0]
    print(sol.rob(nums))


if __name__ == "__main__":
    main()