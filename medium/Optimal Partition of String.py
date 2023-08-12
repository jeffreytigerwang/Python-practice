# https://leetcode.com/problems/optimal-partition-of-string/

from collections import Counter
class Solution:
    def partitionString(self, s: str) -> int:
        sMap = {}

        res = 1

        for c in s:
            if c in sMap:
                res += 1
                sMap = {c: 1}
            else:
                sMap[c] = 1

        return res