# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[0])

        temp = []

        for token in tokens:
            if token == '+':
                temp.append(temp.pop(-2) + temp.pop())

            elif token == '-':
                temp.append(temp.pop(-2) - temp.pop())

            elif token == '/':
                temp.append(int(temp.pop(-2) / temp.pop()))

            elif token == '*':
                temp.append(temp.pop(-2) * temp.pop())
            else:
                temp.append(int(token))

        return temp[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()
print(sol.evalRPN(tokens))


