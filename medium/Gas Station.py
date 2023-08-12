# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tempGas = 0
        res = 0

        # if we can go from index i, i must be the result because 1. sum(gas) >= sum(cost); 2. there must be an unique solution.
        for i in range(len(gas)):
            tempGas += (gas[i] - cost[i])

            if tempGas < 0:
                tempGas = 0

                # can't be i.
                res = i + 1

        return res



gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

sol = Solution()
print(sol.canCompleteCircuit(gas, cost))