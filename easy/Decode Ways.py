# https://leetcode.com/problems/decode-ways/description/

class Solution:
    # The isBadVersion API is already defined for you.
    # def isBadVersion(version: int) -> bool:

    class Solution:
        def firstBadVersion(self, n: int) -> int:
            # The isBadVersion API is already defined for you.
            # def isBadVersion(version: int) -> bool:

            class Solution:
                def firstBadVersion(self, n: int) -> int:
                    if n == 1:
                        return n

                    l = 1
                    r = n

                    while l <= r:

                        m = l + (r - l) // 2
                        print(m)

                        if isBadVersion(m):
                            if not isBadVersion(m - 1):
                                return m

                            r = m
                        else:
                            l = m + 1

                    # print("GG")
