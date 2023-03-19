# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # if not columnTitle:
        #     return 0
        #
        # count = len(columnTitle) - 1
        #
        # res = 0
        # for number in columnTitle:
        #     tempNum = ord(number.lower()) - 96
        #
        #     for i in range(count):
        #         tempNum = tempNum * 26
        #
        #     res = res + tempNum
        #     count -= 1
        #
        # return res

        if not columnTitle:
            return 0

        hashTable = {'A': 1,
                     'B': 2,
                     'C': 3,
                     'D': 4,
                     'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                     'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                     'Z': 26}

        count = len(columnTitle)
        res = 0

        for number in columnTitle:
            tempNum = hashTable[number]

            for i in range(count - 1):
                tempNum = tempNum * 26

            res = res + tempNum
            count -= 1

        return res


sol = Solution()

columnTitle = "ZY"

sol.titleToNumber(columnTitle)
