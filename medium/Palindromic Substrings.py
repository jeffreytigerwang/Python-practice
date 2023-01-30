# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l -= 1
                r += 1

            # return s[l + 1: r]

        # for i in range(len(s)):
        #     temp = helper(s, i, i)
        #
        #     if temp != "":
        #         res.append(temp)
        #
        #     temp = helper(s, i, i + 1)
        #
        #     if temp != "":
        #         res.append(temp)

        for i in range(len(s)):
            helper(s, i, i)
            helper(s, i, i+1)

        print(res)
        print(len(res))
        # return len(res)

def main():
    sol = Solution()
    s = "aaa"
    sol.countSubstrings(s)


if __name__ == "__main__":
    main()
