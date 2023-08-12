# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # O(m*n)
        # length = len(s1)
        # s1 = sorted(s1)
        #
        # for r in range(len(s2) - length + 1):
        #     if s1 == sorted(s2[r: r + length]):
        #         return True
        #
        # return False

        # O(26*n)

        s1Dict = Counter(s1)
        s2Dict = Counter(s2[0: len(s1)])

        if s1Dict == s2Dict:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            # print(s1Dict)
            # print(s2Dict)
            if s1Dict == s2Dict:
                return True

            s2Dict[s2[l]] -= 1
            s2Dict[s2[r]] = 1 + s2Dict.get(s2[r], 0)

            l += 1



            # print(s2Dict)

        return s1Dict == s2Dict

s1 = "adc"
s2 = "dcda"

sol = Solution()

print(sol.checkInclusion(s1, s2))