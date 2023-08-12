# https://leetcode.com/problems/maximum-number-of-balloons/
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        key = ['b', 'a', 'l', 'o', 'n']

        textDict = {}

        for t in text:
            textDict[t] = 1 + textDict.get(t, 0)

        if all(c in textDict for c in key):
            textDict['l'] = textDict['l'] // 2
            textDict['o'] = textDict['o'] // 2
        else:
            return 0

        temp = min(textDict[t] for t in key)

        return temp


# With Counter and without hard-coding // 2
class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res