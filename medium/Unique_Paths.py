class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n] * m --> results in duplicate of first row; editing one element in any row will change the corresponding elements in other rows.

        dp = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 or j == n - 1:
                return 1

            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)

            return dp[i][j]

        return dfs(0, 0)



sol = Solution()
print(sol.uniquePaths(3,7))