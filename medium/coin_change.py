# https://leetcode.com/problems/coin-change/
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('Inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            temp = [float('Inf')]
            for c in coins:
                if i - c < 0:
                    break
                temp.append(dp[i - c])
            print(temp)
            dp[i] = min(temp) + 1

        print(dp)
        return dp[amount] if dp[amount] != float('Inf') else -1


coins = [2]
amount = 10

answer = Solution()
print(answer.coinChange(coins, amount))
