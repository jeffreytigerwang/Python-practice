# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1   # Buffer If you look closely when i = 2 and at the second if statement. Clearly if the first 2
                    # characters of s form a valid decoding then we need to increment dp[2] by 1. So we add the
                    # buffer dp[0] = 1 to deal with this case. As if we didn't add the buffer and had our dp'[1] = the number of
                    # ways to decode the first two characters in s. Then dp'[1] = dp[0] + dp[-1]. Which is an annoying edge case.
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if int(s[i - 1: i]) > 0:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
