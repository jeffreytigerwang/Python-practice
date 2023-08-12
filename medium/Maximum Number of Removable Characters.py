# https://leetcode.com/problems/maximum-number-of-removable-characters/

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubstring(s, subs):
            sIndex, subsIndex = 0, 0

            while sIndex < len(s) and subsIndex < len(subs):
                if sIndex in removed or s[sIndex] != subs[subsIndex]:
                    sIndex += 1
                    continue

                sIndex += 1
                subsIndex += 1

            return subsIndex >= len(subs)

        res = 0
        l, r = 0, len(removable) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            removed = set(removable[: mid + 1])

            if isSubstring(s, p):
                res = max(res, mid + 1)
                l = mid + 1
            else:
                r = mid - 1

        return res