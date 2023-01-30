# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # works but too complex?
        # # wrong, ab --> a, not ab != ba
        # res = []
        #
        # tempList = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        #
        # for i in tempList:
        #     if i == i[::-1]:
        #         res.append(i)
        #
        # return str(max(res, key=len))

        res = ""

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return s[l+1: r]

        for i in range(len(s)):
            res = max(res, helper(s, i, i), helper(s, i, i+1), key=len)

        return res
def main():
    sol = Solution()
    s = "babad"
    # sol.longestPalindrome(s)
    print(sol.longestPalindrome(s))


if __name__ == "__main__":
   main()