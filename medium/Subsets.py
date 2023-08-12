# https://leetcode.com/problems/subsets/description/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # dfs
        def backtracking(nums, path):
            res.append(path.copy())

            for i in range(len(nums)):
                path.append(nums[i])
                backtracking(nums[i + 1:], path)
                path.pop()

            return

        backtracking(nums, [])

        return res


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # dfs
        def backtracking(index):
            res.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

            return

        backtracking(0)

        return res

class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for mask in range(0, 2 ** len(nums)):
            temp = []

            for i in range(len(nums)):
                temp.append(nums[i])

            res.append(temp)

        return res

def main():
    nums = 'leetcode'

    sol = Solution2()
    print(sol.subsets(nums))


if __name__ == "__main__":
    main()

