# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        char_occ_dict = collections.Counter(s)

        for key, value in char_occ_dict.items():
            if value < k:
                return max(self.longestSubstring(subString, k) for subString in s.split(key))

        return len(s)