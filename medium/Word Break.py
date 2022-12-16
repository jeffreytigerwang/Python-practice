# https://leetcode.com/problems/word-break/

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        listLength = []
        visited = []
        q = [0]

        for w in wordDict:
            listLength.append(len(w))

        while q:
            print(q)
            startIndex = q.pop(0)
            if startIndex == len(s):
                return True

            if startIndex not in visited:
                visited.append(startIndex)

                for l in listLength:
                    sub = s[startIndex: startIndex + l]
                    if sub in wordDict:
                        q.append(startIndex + l)

        return False