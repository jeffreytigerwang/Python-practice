# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(nums, path, currSum):
            if currSum == target:
                res.append(path[:])
                return

            if currSum > target:
                return

            for i in range(len(nums)):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    path.append(nums[i])
                    backtracking(nums[i + 1:], path, currSum + nums[i])
                    path.pop()

            return

        backtracking(candidates, [], 0)

        return res