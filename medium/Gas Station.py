# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ##   My approach, O(N^2)

        # if len(gas) == 1:
        #     if gas[0] >= cost[0]:
        #         return 0
        #     else:
        #         return -1
        #
        # n = len(gas)
        #
        # for i in range(n):
        #     sum = 0
        #     for j in range(-n + i, i):
        #         sum = sum + gas[j] - cost[j]
        #
        #         if sum < 0:
        #             break
        #
        #         if j == i - 1:
        #             print(i)
        #             print("reach end?")
        #             return i
        #
        # print("-1")
        # return -1

        #   O(N)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                start = i + 1
                total = 0

        return start

gas = [2,3,4]
cost = [3,4,3]

sol = Solution()
sol.canCompleteCircuit(gas, cost)