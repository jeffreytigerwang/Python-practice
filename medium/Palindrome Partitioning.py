# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(string, path):
            if not string:
                res.append(path[:])
                return

            for i in range(len(string)):
                substring = string[: i + 1]

                if self.isPalindrome(substring):
                    path.append(substring)
                    backtracking(string[i + 1:], path)
                    path.pop()

            return

        backtracking(s, [])
        return res


    def isPalindrome(self, substring):
        return substring == substring[:: -1]


def main():
    sol = Solution()
    s = "aab"
    print(sol.partition(s))


if __name__ == "__main__":
    main()