# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        else:
            res = ['']

        dictionary = {'2': "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        for digit in digits:
            current_combination = []

            for letter in dictionary[digit]:
                for combination in res:
                    current_combination.append(combination + letter)

            res = current_combination

        return res