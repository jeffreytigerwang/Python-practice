from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        #
        # def backtracking(nums, path, currSum):
        #     if currSum == target:
        #         res.append(path)
        #         return
        #
        #     if currSum > target:
        #         return
        #
        #     for i in range(len(nums)):
        #         backtracking(nums[i:], path + [nums[i]], currSum + nums[i])
        #
        # backtracking(candidates, [], 0)
        #
        # return res

        res = []

        def backtracking(i, path, currSum):
            if currSum == target:
                res.append(path.copy())
                return

            if currSum > target or i >= len(candidates):
                return

            path.append(candidates[i])
            backtracking(i, path, currSum + candidates[i])

            path.pop()
            backtracking(i + 1, path, currSum)

            return

        backtracking(0, [], 0)
        return res

def main():
    candidates = [8,7,4,3]
    target = 11
    test = Solution()

    print(test.combinationSum(candidates, target))


if __name__ == "__main__":
    main()
