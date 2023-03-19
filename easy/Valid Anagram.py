# https://leetcode.com/problems/valid-anagram/
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_dict = collections.Counter(s)
        # t_dict = collections.Counter(t)
        #
        # return s_dict == t_dict

        if len(s) != len(t):
            return False

        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict