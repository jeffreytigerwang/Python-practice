# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        res = 0
        count = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            if r >= k:
                if s[l] in vowels:
                    count -= 1

                l += 1

            res = max(res, count)

        return res