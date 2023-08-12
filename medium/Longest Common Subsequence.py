# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   a c e
        # a 0 0 0 0
        # b 0 0 0 0
        # c 0 0 0 0
        # d 0 0 0 0
        # e 0 0 0 0
        #   0 0 0 0

        m = len(text1)
        n = len(text2)
        dp = [[0 for c in range(n + 1)] for r in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]

t1 = "abcde"
t2 = "ace"

sol = Solution()
sol.longestCommonSubsequence(t1, t2)