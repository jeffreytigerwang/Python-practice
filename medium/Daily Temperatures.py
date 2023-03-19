# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                # res[stack[-1][0]] = index - stack[-1][0]
                # stack.pop()

                #OR
                tempIndex, tempTemp = stack.pop()
                res[tempIndex] = index - tempIndex

            stack.append((index, temperature))

        return res


sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]

print(sol.dailyTemperatures(temperatures))