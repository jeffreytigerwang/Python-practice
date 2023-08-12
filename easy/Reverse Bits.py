# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31, -1, -1):
            if n & 1:
                res += 1 << i

            n >>= 1

        return res