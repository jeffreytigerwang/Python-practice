class Solution(object):
    def longestCommonPrefix(self, strs):
        # longest = ""
        #
        # if len(strs) == 0:
        #     return ""
        #
        # if len(strs) == 1:
        #     return strs[0]
        #
        # for i in range(0, len(min(strs, key=len))):
        #     if (all(strs[0][i] == element[i] for element in strs)):
        #         longest = longest + strs[0][i]
        #     else:
        #         break
        #
        # return longest

        res = ''
        minLength = len(min(strs, key=len))

        for i in range(minLength):
            for string in strs:
                if strs[0][i] != string[i]:
                    return res

            res += strs[0][i]

        return res


strs = ["flower","flow","flight"]

test1 = Solution()
print(test1.longestCommonPrefix(strs))
