# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())

        if len(s) <= 1:
            return True

        def validPalindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if l == -1 and r == len(s):
                return True
            else:
                return False

        if len(s) % 2 == 0:
            return validPalindrome(s, len(s) // 2 - 1 ,len(s) // 2)
        else:
            return validPalindrome(s, len(s) // 2, len(s) // 2)


s = "aa"

sol = Solution()
print(sol.isPalindrome(s))