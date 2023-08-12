# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Dict: key = character; value = frequency of character
        # count = {}
        # temp = -1
        # res = []
        #
        # for c in s:
        #     count[c] = 1 + count.get(c, 0)
        #
        # for i in range(len(s)):
        #     count[s[i]] -= 1
        #
        #     if count[s[i]] <= 0:
        #         if all(count[c] <= 0 for c in s[temp + 1: i]):
        #             res.append(i - temp)
        #             temp = i
        #
        # return res


        # Dict: key = character; value = last index
        count = {}
        res = []
        length = len(s)

        for j in range(length):
            c = s[j]
            count[c] = j

        goal = 0
        currLen = 0

        for i in range(length):
            goal = max(goal, count[s[i]])
            currLen += 1

            if i == goal:
                res.append(currLen)
                currLen = 0

        return res
