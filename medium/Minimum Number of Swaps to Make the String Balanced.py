# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
import math


class Solution:
    def minSwaps(self, s: str) -> int:
        maxClose = 0
        close = 0

        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
                maxClose = max(maxClose, close)

        return math.ceil(maxClose / 2)
        # return (maxClose + 1) // 2