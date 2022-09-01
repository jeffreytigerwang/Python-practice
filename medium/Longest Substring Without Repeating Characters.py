class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = []

        for i in range(len(s)):
            if len(temp) == 0:
                temp.append(s[i])
                ans = max(ans, len(temp))
                continue

            if s[i] not in temp:
                temp.append(s[i])
            else:

                temp = temp[temp.index(s[i]) + 1:]
                temp.append(s[i])
                # print(temp.index(s[i]))
                # print(temp)

            ans = max(ans, len(temp))

        return ans


def main():
    sol = Solution()
    s = "bbbbb"

    print(sol.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()