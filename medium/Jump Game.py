# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums):
        # # Dynamic programming
        #
        # statusPosition = [False for i in range(len(nums))]
        # statusPosition[0] = True
        #
        # # starting position
        # i = 0
        #
        # for maxReach in range(1, len(nums)):
        #     print("maxReach: ", maxReach)
        #     while i < maxReach:
        #         print("i:", i)
        #         if statusPosition[i] and nums[i] + i >= maxReach:   # how far I can reach from i; i = 0 initially; I
        #                                                             # can not reach maxReach from i, increment i.
        #             statusPosition[maxReach] = True
        #             break
        #
        #         i = i + 1
        #     print("")
        #
        # print(statusPosition)
        # return statusPosition[-1]

        # # Greedy algorithm
        # i = 0
        # maxRange = 0
        #
        # while i < len(nums) and i <= maxRange:
        #     maxRange = max(maxRange, i + nums[i])
        #     i += 1
        #
        # print(maxRange)
        # return i == len(nums)

        statusList = [False for i in range(len(nums))]
        statusList[0] = True

        i = 0

        for maxReach in range(len(nums)):
            while i < maxReach:
                if statusList[i] and i + nums[i] >= maxReach:
                    statusList[maxReach] = True
                    break

                i += 1

        return statusList[-1]

def main():
    sol = Solution()
    nums = [2,3,1,1,4]

    print(sol.canJump(nums))


if __name__ == "__main__":
    main()
