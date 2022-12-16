class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystackLength = len(haystack)
        needleLength = len(needle)
        res = -1

        for i in range(0, haystackLength - needleLength + 1):
            if haystack[i: i + needleLength] == needle:
                res = i
                break

        return res