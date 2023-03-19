# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]


        for i in range(2, numRows):
            tempList = [1, 1]
            for j in range(1, i):
                tempList.insert(j, res[i - 1][j - 1] + res[i - 1][j])

            res.append(tempList)

        return res


sol = Solution()
numRows = 6

sol.generate(numRows)