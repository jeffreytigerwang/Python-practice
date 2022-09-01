from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recursion(res, s, left, right):

            # Base case
            if left == 0 and right == 0:
                res.append(s)
                # return res
                return

            if left > 0:
                recursion(res, s + '(', left - 1, right)

            if right > 0 and left < right:
                recursion(res, s + ')', left, right - 1)

            return res

        res = recursion([], '', n, n)


        return res


def main():
    n = 3

    test = Solution()
    print(test.generateParenthesis(3))


if __name__ == "__main__":
    main()