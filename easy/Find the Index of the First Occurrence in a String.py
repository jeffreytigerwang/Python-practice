# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        startIndex = 0
        tempString = ''

        for i in range(len(haystack)):
            tempString += haystack[i]

            if i >= len(needle) - 1:
                if tempString == needle:
                    return startIndex

                tempString = tempString[1:]
                startIndex += 1

        return -1