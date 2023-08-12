# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
class Solution:
    def maxProduct(self, s: str) -> int:
        palindromeDict = {} # key = bitmap; value = length

        # Can not use DFS because we need bitmask to make sure the palindromes are disjoint!
        # def dfs(index, path):
        #     if path == path[::-1]:
        #         palindromeDict[path] = len(path)
        #
        #     for i in range(index, len(s)):
        #         path += s[i]
        #         dfs(i + 1, path)
        #         path = path[: -1]
        #
        #     return

        # dfs(0, '')

        res = 0
        # 2^N == 2 ** N == 1 << N
        for bitmask in range(2 ** len(s)):
            subsequence = ''

            for i in range(len(s)):
                if bitmask & (2 ** i) != 0:
                    subsequence += s[i]

            if subsequence == subsequence[:: -1]:
                palindromeDict[bitmask] = len(subsequence)

        for key1 in palindromeDict.keys():
            for key2 in palindromeDict.keys():
                if key1 & key2 == 0:
                    res = max(res, palindromeDict[key1] * palindromeDict[key2])

        return res



sol = Solution()
s = "leetcodecom"
sol.maxProduct(s)