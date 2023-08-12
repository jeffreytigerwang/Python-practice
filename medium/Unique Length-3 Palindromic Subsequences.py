# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
from collections import Counter


# Less than O(26 * n) depending on len(left)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0
        elif len(s) == s:
            return 1 if s[0] == s[2] else 0
        else:
            left = set()
            right = Counter(s)

            # if want to skip first char, namely (1, len(s))
            # right[s[0]] -= 1
            # if right[s[0]] <= 0:
            #     right.pop(s[0])
            #
            # left.add(s[0])

            res = set()

            for i in range(len(s)):
                right[s[i]] -= 1

                if right[s[i]] <= 0:
                    right.pop(s[i])

                for l in left:
                    if l in right:
                        res.add(l + s[i] + l)

                left.add(s[i])

            return len(res)