# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(l, r):
            temp = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

                temp += 1

            return temp

        for i in range(len(s)):
            # l, r = i, i
            #
            # while l >= 0 and r < len(s) and s[l] == s[r]:
            #     l -= 1
            #     r += 1
            #     res += 1
            #
            # l, r = i, i + 1
            #
            # while l >= 0 and r < len(s) and s[l] == s[r]:
            #     l -= 1
            #     r += 1
            #     res += 1

            res += helper(i, i)
            res += helper(i, i + 1)

        return res


def main():
    sol = Solution()
    s = "aaa"
    sol.countSubstrings(s)


if __name__ == "__main__":
    main()
