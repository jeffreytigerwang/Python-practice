# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        m = len(prices)

        def dfs(index, buying):
            if index >= m:
                return 0

            if (index, buying) in dp.keys():
                return dp[(index, buying)]

            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(buy, cooldown)

            else:
                sell = dfs(index + 2, True) + prices[index]
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(sell, cooldown)

            return dp[(index, buying)]

        return dfs(0, True)