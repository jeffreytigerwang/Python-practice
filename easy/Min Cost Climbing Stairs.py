# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) <= 2:
        #     return min(cost)
        #
        # dp = [0] * len(cost)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        #
        # for i in range(2, len(cost)):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        #
        # return min(dp[-1], dp[-2])

        # # Reverse
        # # [1, 2, 3] 0
        # # start from 2 because 3 + 0 = 3; index of 2 = len(cost) - 3
        #
        # cost.append(0)
        #
        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        #
        # return min(cost[0], cost[1])

        if len(cost) <= 2:
            return min(cost)

        d0 = cost[0]
        d1 = cost[1]

        for i in range(2, len(cost)):
            d0, d1 = d1, cost[i] + min(d0, d1)

        return min(d0, d1)