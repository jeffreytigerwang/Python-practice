# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            # res += n & 1
            res += n % 2
            n >>= 1

        return res