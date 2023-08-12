# https://leetcode.com/problems/repeated-dna-sequences/
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        res = []
        subsequenceMap = {}

        for i in range(len(s) - 9):
            subsequence = s[i: i + 10]
            subsequenceMap[subsequence] = 1 + subsequenceMap.get(subsequence, 0)

        for key in subsequenceMap:
            if subsequenceMap[key] > 1:
                res.append(key)

        return res
