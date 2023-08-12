# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        pDict = {}
        sDict = {}

        for i, j in zip(pattern, s):
            if (i in pDict and pDict[i] != j) or (j in sDict and sDict[j] != i):
                return False

            pDict[i] = j
            sDict[j] = i

        return True