# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution:
    def minFlips(self, s: str) -> int:
        res = float('inf')
        length = len(s)
        s = s + s  # iterate through all combination of s; e.g., 1100 --> 1001 --> 0011 --> 0110 --> 1100 --> 11001100
        l = 0
        alt0, alt1 = '', ''
        diff0, diff1 = 0, 0

        for i in range(len(s)):
            alt0 += '0' if i % 2 == 0 else '1'
            alt1 += '1' if i % 2 == 0 else '0'

        for r in range(len(s)):
            if s[r] != alt0[r]:
                diff0 += 1

            if s[r] != alt1[r]:
                diff1 += 1

            if r >= length: # equivalent to (r - l + 1) > length
                if s[l] != alt0[l]:
                    diff0 -= 1

                if s[l] != alt1[l]:
                    diff1 -= 1

                l += 1
                res = min(res, diff0, diff1)

        return res

