# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        mostSignificantBit = 1
        # 0000 --> base

        # 0001 --> 1

        # 0010 --> 2
        # 0011

        # 0100 --> 4
        # 0101
        # 0110
        # 0111

        # 1000 --> 8

        for i in range(1, n + 1):
            if mostSignificantBit * 2 == i:
                mostSignificantBit = i

            dp[i] = dp[i - mostSignificantBit] + 1

        return dp
