# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if not prices or len(prices) == 1:
        #     return 0
        #
        # max_p = 0
        # temp = prices[0]
        # for i in range(1, len(prices)):
        #     if temp < prices[i]:
        #         max_p = max_p + (prices[i] - temp)
        #         temp = prices[i]
        #     else:
        #         temp = prices[i]
        # return max_p

        if not prices or len(prices) == 1:
            return 0

        tempMax = 0
        tempMin = prices[0]

        res = 0

        for i in range(1, len(prices)):
            if prices[i] < tempMin:
                tempMin = prices[i]
                tempMax = 0
            else:
                tempMax = max(tempMax, prices[i])

            # res = max(res, tempMax - tempMin)
            if tempMax - tempMin > 0:
                print(res)
                res = res + (tempMax - tempMin)
                tempMin = prices[i]

        return res


def main():
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))

if __name__ == "__main__":
    main()
