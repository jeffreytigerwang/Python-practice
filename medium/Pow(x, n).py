# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            # 2^10 = 2^5 * 2^5
            res = recursion(x, n // 2)
            res *= res

            # if n is odd, 2^5 = 2^1 * 2^2 * 2^2. Else, 2^4 = 2^2 * 2^2
            return x * res if n % 2 else res

        res = recursion(x, abs(n))

        return res if n >= 0 else 1/res