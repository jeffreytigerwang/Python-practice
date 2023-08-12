# https://leetcode.com/problems/boats-to-save-people/
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            # Take both lightest and heaviest person
            if people[l] + people[r] <= limit:
                l += 1

            # Take only the heaviest person on boat
            r -= 1
            res += 1

        return res


