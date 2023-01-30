# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s, path, res):
            if not s:
                res.append(path[:])
                return

            for i in range(1, len(s) + 1):
                if s[:i] == s[i - 1:: - 1]:
                    # path.append(s[:i])
                    # helper(s[i:], path, res)
                    # path.pop()
                    helper(s[i:], path + [s[:i]], res)

        res = []
        helper(s, [], res)
        return res
def main():
    sol = Solution()
    s = "abb"
    print(sol.partition(s))


if __name__ == "__main__":
    main()