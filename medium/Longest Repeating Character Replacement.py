# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1 or k >= len(s):
            return len(s)

        count = {}
        l = 0
        currMax = 0
        res = 0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            currMax = max(currMax, count[s[i]])

            if i - l + 1 - currMax > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res

