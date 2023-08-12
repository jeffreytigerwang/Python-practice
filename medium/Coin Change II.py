# https://leetcode.com/problems/coin-change-ii/
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)

        # amount + 1 for base case (all 1s) --> all coins can make up amount 0 by using 0 coin.
        # coins + 1 for padding
        dp = [[0] * (len(coins) + 1) for j in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        #       Coin X X X P
        # amount     1 1 1 1
        #            1
        #            2
        #            3
        #            4


        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                # not using current coin --> sum of using prev coins
                dp[a][i] = dp[a][i + 1]

                # using current coin
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]

        # -1 = amount
        return dp[-1][0]


        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount

        dp = [0] * (amount + 1)
        dp[0] = 1

        # start from last coin (using 1 coin)
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                # not using current coin; looking below
                nextDP[a] = dp[a]

                # using current coin
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]

            dp = nextDP

        return dp[amount]

sol = Solution()

amount = 5
coins = [1,2,5]

print(sol.change(amount, coins))