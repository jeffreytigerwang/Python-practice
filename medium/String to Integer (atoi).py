# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        sList = s.split()

        if not sList:
            return 0

        numString = sList[0]
        sign = -1 if numString[0] == '-' else 1

        # if numString[0] == '-' or numString[0] == '+':
        #     del numString[0]

        res = 0
        start = 1 if numString[0] == '-' or numString[0] == '+' else 0

        bound = 2 ** 31 - 1 if sign == 1 else 2 ** 31

        for i in range(start, len(numString)):
            if numString[i].isdigit():
                res = res * 10 + (ord(numString[i]) - ord('0'))

                if res > bound:
                    return bound * sign
            else:
                break

        return res * sign