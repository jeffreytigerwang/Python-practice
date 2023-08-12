# https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        # # Approach 1. Two stack - store indices of ( and *
        #
        # leftStack = []
        # starStack = []
        #
        # for i, c in enumerate(s):
        #     if c == '(':
        #         leftStack.append(i)
        #     elif c == ')':
        #         if not leftStack and not starStack:
        #             return False
        #         elif not leftStack:
        #             starStack.pop()
        #         else:
        #             leftStack.pop()
        #     else:
        #         starStack.append(i)
        #
        # while leftStack and starStack:
        #     if leftStack[-1] > starStack[-1]:
        #         return False
        #
        #     leftStack.pop()
        #     starStack.pop()
        #
        # return not leftStack

        # Approach 2. min and max left/( count

        minLeft, maxLeft = 0, 0

        for c in s:
            if c == '(':
                minLeft, maxLeft = minLeft + 1, maxLeft + 1
            elif c == ')':
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            else:
                minLeft -= 1
                maxLeft += 1

            if maxLeft < 0:
                return False

            if minLeft < 0: # required because -> s = ( * ) (
                minLeft = 0

        return minLeft == 0

