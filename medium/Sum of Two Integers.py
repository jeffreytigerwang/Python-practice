# https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # https://leetcode.com/problems/sum-of-two-integers/solutions/489210/read-this-if-you-want-to-learn-about-masks/

        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        # works both as while loop and single value check
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a

