class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        def dynamicApproach(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = dynamicApproach(i + 1, j) + dynamicApproach(i, j + 1)

            return dp[i][j]

        return dynamicApproach(0, 0)

sol = Solution()
print(sol.uniquePaths(3,7))