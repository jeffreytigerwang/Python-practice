# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        threshold = 2 ** 31
        res = 0
        neg = True if x < 0 else False
        x = abs(x)

        while x:
            lastDigit = x % 10
            x = x // 10

            if neg and (res > threshold // 10 or (res == threshold // 10 and lastDigit > threshold % 10)):
                return 0

            if not neg and (res > (threshold - 1) // 10 or (res == (threshold - 1) // 10 and lastDigit > (threshold - 1) % 10)):
                return 0

            res = (res * 10) + lastDigit

        return res if not neg else -res