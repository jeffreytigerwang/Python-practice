# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) <= 1:
#             return len(s)
#
#         res = s[0]
#         ret = 0
#
#         for i in range(1, len(s)):
#             if s[i] in res:
#                 ret = max(ret, len(res))
#                 res = res[res.index(s[i]) + 1:] + s[i]
#             else:
#                 res += s[i]
#
#         # print(ret)
#         return max(ret, len(res))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        print(l)
        return res
def main():
    sol = Solution()
    s = "pwwkew"

    print(sol.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()