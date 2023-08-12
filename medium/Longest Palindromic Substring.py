# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1: r]

        for i in range(len(s)):
            res = max(res, helper(i, i), helper(i, i + 1), key=len)
            # if len(helper(i, i)) > len(helper(i, i + 1)):
            #     res = res if len(res) > len(helper(i, i)) else helper(i, i)
            # else:
            #     res = res if len(res) > len(helper(i, i + 1)) else helper(i, i + 1)

        return res

def main():
    sol = Solution()
    s = "babad"
    # sol.longestPalindrome(s)
    print(sol.longestPalindrome(s))


if __name__ == "__main__":
   main()