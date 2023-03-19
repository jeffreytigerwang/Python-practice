from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recursion(openN, closeN):
            if openN == n and closeN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                recursion(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                recursion(openN, closeN + 1)
                stack.pop()

        recursion(0, 0)

        return res



# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         def backtrack(openN, closedN, stack):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return
#             if openN < n:
#                 backtrack(openN + 1, closedN, stack + ["("])
#             if closedN < openN:
#                 backtrack(openN, closedN + 1, stack + [")"])
#
#             print(openN, closedN)
#             print(stack)
#
#
#         backtrack(0,0, [])
#         return res


def main():
    n = 2

    test = Solution()
    print(test.generateParenthesis(n))


if __name__ == "__main__":
    main()