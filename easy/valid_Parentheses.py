class Solution:
    def isValid(self, s: str) -> bool:
        tempDict = {'(': ')', '[': ']', '{': '}'}
        temp = []

        for char in s:
            if char in tempDict.keys():
                temp.append(char)
            else:
                if not temp or tempDict[temp.pop()] != char:
                    return False

        return not temp