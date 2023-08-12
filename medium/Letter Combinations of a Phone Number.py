# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        digitsLength = len(digits)

        def backtracking(string, path):
            if len(path) == digitsLength:
                res.append(path[:])
                return

            for i in range(len(string)):
                for j in range(len(phoneDict[string[i]])):
                    # path.append(phoneDict[string[i]][j])
                    backtracking(string[i + 1:], path + phoneDict[string[i]][j])
                    # path.pop()
            return

        if digits:
            backtracking(digits, '')

        return res