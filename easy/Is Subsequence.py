# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        temp = 0

        for i in range(len(t)):
            if temp >= len(s):
                return True

            if t[i] == s[temp]:
                temp += 1

        return temp >= len(s)
