# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))

            if n in record:
                return False
            else:
                record.add(n)

        return True
