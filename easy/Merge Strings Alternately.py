# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        isWord1 = True
        i = 0
        j = 0
        res = ''

        while i < len(word1) and j < len(word2):
            if isWord1:
                res += word1[i]
                i += 1
                isWord1 = False
            else:
                res += word2[j]
                j += 1
                isWord1 = True

        if i < len(word1):
            res += word1[i:]

        if j < len(word2):
            res += word2[j:]

        return res

