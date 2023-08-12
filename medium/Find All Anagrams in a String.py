# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List
from collections import Counter

# Sliding window - While loop
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = Counter(p)
        res = []
        left = 0
        right = len(p) - 1
        tempDict = Counter(s[left: right])

        while right < len(s):
            tempDict[s[right]] = 1 + tempDict.get(s[right], 0)

            if tempDict == pDict:
                res.append(left)

            tempDict[s[left]] -= 1

            if tempDict[s[left]] <= 0:
                del tempDict[s[left]]

            left += 1
            right += 1

        return res


# Counter only - Slow
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = Counter(p)
        res = []

        for i in range(len(s) - len(p) + 1):
            tempDict = Counter(s[i: i + len(p)])

            if tempDict == pDict:
                res.append(i)

        return res

# For loop

class Solution3:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pMap, sMap = {}, {}
        startIndex = 0
        res = []

        for i in p:
            pMap[i] = 1 + pMap.get(i, 0)

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)

            if i >= len(p) - 1:
                if sMap == pMap:
                    res.append(startIndex)

                sMap[s[startIndex]] -= 1

                if sMap[s[startIndex]] <= 0:
                    del sMap[s[startIndex]]

                startIndex += 1

        return res

