# https://leetcode.com/problems/perfect-squares/

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [float('inf')] * (n + 1)   # going from 0 to n
        dp[0] = 0   # base case, need 0 perfect square to get to 0
        squares = [x ** 2 for x in range(1, n + 1) if x ** 2 <= n]

        for i in range(1, n + 1):   # from 1 to n
            for j in squares:
                if i - j < 0:
                    break

                dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[n]

def main():
    sol = Solution()
    num = 12
    print(sol.numSquares(num))

if __name__ == "__main__":
    main()
