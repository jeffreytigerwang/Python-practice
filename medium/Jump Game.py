# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    # My DP approach
    # def canJump(self, nums):
    #     dp = [False] * len(nums)
    #     dp[0] = True
    #
    #     for i in range(len(nums)):
    #         if dp[i]:
    #             # print(nums[i])
    #             for j in range(1, nums[i] + 1):
    #
    #                 if i + j < len(nums):
    #                     dp[i + j] = True
    #                 else:
    #                     return True
    #
    #     return dp[-1]
    #

    # Greedy

    def canJump(self, nums):
        goal = len(nums) - 1    # last index

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal: # whether if we can reach goal at index i
                goal = i

        return goal == 0


def main():
    sol = Solution()
    nums = [2,3,1,1,4]

    print(sol.canJump(nums))


if __name__ == "__main__":
    main()
